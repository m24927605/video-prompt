#!/usr/bin/env python3
"""Run one held-out case in an isolated Codex or Claude Code workspace."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any


SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
from sensitive_urls import SIGNED_QUERY_REDACTION_RE  # noqa: E402
from case_contracts import PACKAGED_SKILLS, CaseContractError, parse_case_contract  # noqa: E402


SENSITIVE_KEYS = {
    "cwd",
    "id",
    "memory_paths",
    "messaging_socket_path",
    "parent_tool_use_id",
    "receiver_thread_ids",
    "sender_thread_id",
    "session_id",
    "signature",
    "thread_id",
    "tool_use_id",
    "turn_id",
    "uuid",
    "request_id",
    "idempotency_key",
}
UUID_RE = re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I)
TEMP_WORKSPACE_RE = re.compile(
    r"/(?:private/)?(?:tmp|var/folders/(?:[^/\s]+/)+T)/seedance-[^/\s\"']+"
)
PRIVATE_CLAUDE_PATH_RE = re.compile(
    r"(?:<REDACTED_HOME>|~)/\.claude/(?:plans|projects)/[^\s`\"']+"
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def sanitize_string(value: str) -> str:
    home = str(Path.home())
    if home and home != "/":
        value = value.replace(home, "<REDACTED_HOME>")
    value = TEMP_WORKSPACE_RE.sub("<REDACTED_WORKSPACE>", value)
    value = PRIVATE_CLAUDE_PATH_RE.sub("<REDACTED_PRIVATE_PATH>", value)
    value = UUID_RE.sub("<REDACTED_UUID>", value)
    return SIGNED_QUERY_REDACTION_RE.sub(r"\1<REDACTED>", value)


def sanitize(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: sanitize(item)
            for key, item in value.items()
            if key not in SENSITIVE_KEYS
        }
    if isinstance(value, list):
        return [sanitize(item) for item in value]
    if isinstance(value, str):
        return sanitize_string(value)
    return value


def workspace_inventory(workspace: Path, host: str) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []
    for path in sorted(workspace.rglob("*")):
        relative = path.relative_to(workspace).as_posix()
        if path.is_symlink():
            entries.append({"path": relative, "type": "symlink", "target": os.readlink(path)})
        elif path.is_file():
            entries.append({"path": relative, "type": "file", "sha256": sha256_file(path)})

    inventory = {
        "host": host,
        "research_present": (workspace / "research").exists(),
        "grader_present": (workspace / "skill-evals" / "graders").exists(),
        "entries": entries,
    }
    inventory["digest"] = sha256_bytes(
        json.dumps(inventory, sort_keys=True, ensure_ascii=False).encode("utf-8")
    )
    return inventory


def stage_workspace(repo_root: Path, workspace: Path, host: str) -> dict[str, Any]:
    staged_skills = workspace / "skills"
    staged_skills.mkdir(parents=True)
    for name in PACKAGED_SKILLS:
        shutil.copytree(repo_root / "skills" / name, staged_skills / name)

    host_root = workspace / (".agents" if host == "codex" else ".claude") / "skills"
    host_root.mkdir(parents=True)
    for name in PACKAGED_SKILLS:
        (host_root / name).symlink_to(Path("../../skills") / name)

    return workspace_inventory(workspace, host)


def personal_skill_override() -> tuple[str | None, int]:
    personal_roots = (
        Path.home() / ".agents" / "skills",
        Path.home() / ".codex" / "skills",
    )
    skill_files = sorted({
        path
        for personal_root in personal_roots
        if personal_root.exists()
        for path in personal_root.glob("*/SKILL.md")
    })
    if not skill_files:
        return None, 0
    rows = [f'{{path={json.dumps(str(path))},enabled=false}}' for path in skill_files]
    return "skills.config=[" + ",".join(rows) + "]", len(skill_files)


def codex_argv(workspace: Path, prompt: str) -> tuple[list[str], list[str], int]:
    override, disabled_count = personal_skill_override()
    argv = [
        "codex",
        "exec",
        "--ephemeral",
        "--ignore-user-config",
        "--ignore-rules",
        "--skip-git-repo-check",
        "--strict-config",
        "--disable",
        "plugins",
        "--disable",
        "remote_plugin",
        "--disable",
        "apps",
        "--disable",
        "tool_suggest",
        "--sandbox",
        "read-only",
        "-m",
        "gpt-5.6-sol",
        "-c",
        "model_reasoning_effort=high",
        "-c",
        "approval_policy=never",
    ]
    if override:
        argv.extend(["-c", override])
    argv.extend(["--json", "-C", str(workspace), prompt])

    sanitized = list(argv)
    if override:
        index = sanitized.index(override)
        sanitized[index] = f"<PERSONAL_SKILLS_DISABLED:{disabled_count}>"
    return argv, sanitized, disabled_count


def claude_argv(prompt: str) -> tuple[list[str], list[str], int]:
    argv = [
        "claude",
        "-p",
        "--model",
        "claude-fable-5",
        "--effort",
        "high",
        "--no-session-persistence",
        "--permission-mode",
        "dontAsk",
        "--setting-sources",
        "project",
        "--settings",
        json.dumps({"disableBundledSkills": True, "skillOverrides": {"doctor": "off"}}),
        "--strict-mcp-config",
        "--mcp-config",
        json.dumps({"mcpServers": {}}),
        "--no-chrome",
        "--tools",
        "Skill,Read,Glob,Grep",
        "--allowedTools",
        "Skill,Read,Glob,Grep",
        "--output-format",
        "stream-json",
        "--verbose",
        prompt,
    ]
    return argv, list(argv), 0


def parse_events(stdout: str) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for line in stdout.splitlines():
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            event = {"type": "unparsed", "text": line}
        events.append(sanitize(event))
    return events


def extract_final(host: str, events: list[dict[str, Any]]) -> str:
    if host == "codex":
        messages = [
            event.get("item", {}).get("text", "")
            for event in events
            if event.get("type") == "item.completed"
            and event.get("item", {}).get("type") == "agent_message"
        ]
        if messages:
            return messages[-1]
    else:
        results = [event.get("result") for event in events if event.get("type") == "result"]
        for result in reversed(results):
            if isinstance(result, str) and result.strip():
                return result
        messages: list[str] = []
        for event in events:
            if event.get("type") != "assistant":
                continue
            for content in event.get("message", {}).get("content", []):
                if content.get("type") == "text" and content.get("text"):
                    messages.append(content["text"])
        if messages:
            return messages[-1]
    return ""


def _tool_calls(event: dict[str, Any]) -> list[tuple[str, Any]]:
    """Read only tool-call records, never tool results or assistant prose."""
    calls: list[tuple[str, Any]] = []
    if event.get("type") == "assistant":
        for content in event.get("message", {}).get("content", []):
            if content.get("type") == "tool_use" and isinstance(content.get("name"), str):
                calls.append((content["name"], content.get("input", {})))
    elif event.get("type") == "item.completed":
        item = event.get("item", {})
        if item.get("type") == "tool_call" and isinstance(item.get("name"), str):
            calls.append((item["name"], item.get("arguments", {})))
        elif item.get("type") == "command_execution" and isinstance(item.get("command"), str):
            calls.append(("command_execution", {"command": item["command"]}))
    elif event.get("type") in {"tool_call", "tool_use"} and isinstance(event.get("name"), str):
        calls.append((event["name"], event.get("arguments", event.get("input", {}))))
    return calls


def _argument_values(arguments: Any) -> list[str]:
    if isinstance(arguments, str):
        try:
            return _argument_values(json.loads(arguments))
        except json.JSONDecodeError:
            return [arguments]
    if isinstance(arguments, dict):
        values: list[str] = []
        for value in arguments.values():
            values.extend(_argument_values(value))
        return values
    if isinstance(arguments, list):
        values = []
        for value in arguments:
            values.extend(_argument_values(value))
        return values
    return []


def _skill_path_matches(value: str, skill_name: str) -> bool:
    normalized = value.replace("\\", "/")
    if "<REDACTED_HOME>/" in normalized or "/.codex/skills/" in f"/{normalized}":
        return False
    return f"skills/{skill_name}/" in normalized


def _command_reads_skill_content(value: str, skill_name: str) -> bool:
    normalized = "/" + value.replace("\\", "/")
    if "<REDACTED_HOME>/" in normalized or "/.codex/skills/" in normalized:
        return False
    skill_root = f"skills/{skill_name}/"
    if skill_root not in normalized:
        return False
    tail = normalized.split(skill_root, 1)[1]
    return "SKILL.md" in tail or ("references/" in tail and ".md" in tail)


def extract_skill_activity(
    events: list[dict[str, Any]],
) -> tuple[list[str], list[str], dict[str, list[str]]]:
    discovered: set[str] = set()
    evidence = {skill: [] for skill in PACKAGED_SKILLS}
    for index, event in enumerate(events):
        is_native_listing = (
            event.get("type") == "system"
            and event.get("subtype") == "init"
        )
        if is_native_listing:
            for key in ("skills", "slash_commands"):
                values = event.get(key, [])
                if isinstance(values, list):
                    discovered.update(skill for skill in values if skill in PACKAGED_SKILLS)

        for name, arguments in _tool_calls(event):
            values = _argument_values(arguments)
            if name.lower() == "skill":
                for skill in PACKAGED_SKILLS:
                    if skill in values:
                        evidence[skill].append(f"event[{index}] Skill")
            elif name.lower() in {"read", "read_file", "readfile"}:
                for skill in PACKAGED_SKILLS:
                    if any(_skill_path_matches(value, skill) for value in values):
                        evidence[skill].append(f"event[{index}] {name}")
            elif name.lower() in {"command_execution", "exec_command"}:
                for skill in PACKAGED_SKILLS:
                    if any(_command_reads_skill_content(value, skill) for value in values):
                        evidence[skill].append(f"event[{index}] {name}")

    activated = [skill for skill in PACKAGED_SKILLS if evidence[skill]]
    return (
        [skill for skill in PACKAGED_SKILLS if skill in discovered],
        activated,
        evidence,
    )


def media_tool_events(events: list[dict[str, Any]]) -> list[str]:
    blocked_names = {"imagegen", "image_gen", "higgsfield", "video_generation", "audio_generation"}
    found: list[str] = []

    def visit(value: Any) -> None:
        if isinstance(value, dict):
            name = value.get("name")
            if isinstance(name, str) and any(blocked in name.lower() for blocked in blocked_names):
                found.append(name)
            for item in value.values():
                visit(item)
        elif isinstance(value, list):
            for item in value:
                visit(item)

    visit(events)
    return sorted(set(found))


def claude_model_evidence(
    events: list[dict[str, Any]], requested_model: str
) -> dict[str, Any]:
    usage: dict[str, Any] = {}
    for event in reversed(events):
        candidate = event.get("modelUsage")
        if event.get("type") == "result" and isinstance(candidate, dict):
            usage = candidate
            break

    models: list[dict[str, Any]] = []
    for reported_model, details in usage.items():
        details = details if isinstance(details, dict) else {}
        models.append({
            "reported_model": reported_model,
            "canonical_model": details.get("canonicalModel", reported_model),
            "provider": details.get("provider"),
        })

    primary = next(
        (
            item
            for item in models
            if requested_model in {item["reported_model"], item["canonical_model"]}
        ),
        None,
    )
    return {
        "requested_model_observed": primary is not None,
        "actual_primary_model": primary["canonical_model"] if primary else None,
        "actual_primary_provider": primary["provider"] if primary else None,
        "auxiliary_models": [item for item in models if item is not primary],
        "fallback_detected": bool(models) and primary is None,
    }


def render_native_evidence(
    *,
    host: str,
    cli_version: str,
    requested_model: str,
    requested_effort: str,
    invocation_mode: str,
    expected_skill: str | None,
    workspace_digest: str,
    activation_evidence: list[str],
    model_evidence: dict[str, Any] | None,
) -> str:
    lines = [
        "# Native host evidence",
        "",
        f"- Host: `{host}`",
        f"- CLI version: `{cli_version}`",
        f"- Requested primary model: `{requested_model}`",
        f"- Requested effort: `{requested_effort}`",
        f"- Invocation: `{invocation_mode}`",
        f"- Expected skill: `{expected_skill or 'none'}`",
        f"- Isolated workspace digest: `{workspace_digest}`",
    ]
    if model_evidence is not None:
        lines.extend([
            f"- Requested model observed: `{str(model_evidence['requested_model_observed']).lower()}`",
            f"- Observed primary model: `{model_evidence['actual_primary_model'] or 'unknown'}`",
            f"- Observed provider: `{model_evidence['actual_primary_provider'] or 'unknown'}`",
            f"- Fallback detected: `{str(model_evidence['fallback_detected']).lower()}`",
        ])
        auxiliary = model_evidence.get("auxiliary_models", [])
        if auxiliary:
            rendered = ", ".join(
                f"{item['reported_model']} (canonical {item['canonical_model']}, provider {item['provider'] or 'unknown'})"
                for item in auxiliary
            )
            lines.append(f"- Auxiliary models reported by host: `{rendered}`")
        else:
            lines.append("- Auxiliary models reported by host: `none`")
    if activation_evidence:
        lines.extend(f"- Activation/discovery evidence: {item}" for item in activation_evidence)
    else:
        lines.append("- Activation/discovery evidence: `none captured in event schema`")
    return "\n".join(lines) + "\n"


def cli_version(command: str) -> str:
    result = subprocess.run([command, "--version"], capture_output=True, text=True, check=False, timeout=30)
    return sanitize_string((result.stdout or result.stderr).strip())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True, choices=("codex", "claude-code"))
    parser.add_argument("--case", required=True, dest="case_id")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--timeout", type=int, default=900)
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    case_path = repo_root / "skill-evals" / "cases" / f"{args.case_id}.json"
    case = json.loads(case_path.read_text(encoding="utf-8"))
    try:
        contract = parse_case_contract(case)
    except CaseContractError as exc:
        raise SystemExit(f"invalid case contract: {exc}") from exc
    if contract.case_id != args.case_id:
        raise SystemExit("case id does not match filename")

    prompt = case["prompt"]
    skill_name = contract.expected_skill
    if contract.invocation_mode == "explicit":
        prefix = f"${skill_name}" if args.host == "codex" else f"/{skill_name}"
        prompt = f"{prefix}\n\n{prompt}"

    output_dir = repo_root / "skill-evals" / "results" / args.host / args.case_id
    output_dir.mkdir(parents=True, exist_ok=True)
    # A run that dies before it writes its artifacts leaves the previous run's
    # files in place, and the directory then reads as a valid result for a run
    # that never happened. Stamp the directory on entry and clear the stamp only
    # on success, so an incomplete run is visible instead of silent.
    incomplete_marker = output_dir / "INCOMPLETE"
    incomplete_marker.write_text(
        f"case={args.case_id} host={args.host} started={time.time():.0f}\n"
        "This run did not finish. Any other file in this directory is from an\n"
        "earlier run and does not describe the run that wrote this marker.\n",
        encoding="utf-8",
    )
    rubric_path = repo_root / "skill-evals" / "rubric.md"

    with tempfile.TemporaryDirectory(prefix=f"seedance-{args.host}-{args.case_id}-") as temp:
        workspace = Path(temp)
        inventory = stage_workspace(repo_root, workspace, args.host)
        if inventory["research_present"] or inventory["grader_present"]:
            raise SystemExit("isolation failure: research or grader present")

        if args.host == "codex":
            argv, sanitized_argv, disabled_count = codex_argv(workspace, prompt)
            command = "codex"
            model = "gpt-5.6-sol"
            effort = "high"
        else:
            argv, sanitized_argv, disabled_count = claude_argv(prompt)
            command = "claude"
            model = "claude-fable-5"
            effort = "high"

        started = time.monotonic()
        try:
            result = subprocess.run(
                argv,
                cwd=workspace,
                capture_output=True,
                text=True,
                check=False,
                timeout=args.timeout,
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            timed_out = False
        except subprocess.TimeoutExpired as exc:
            result = subprocess.CompletedProcess(
                argv,
                124,
                stdout=(exc.stdout or b"").decode("utf-8", errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or ""),
                stderr=(exc.stderr or b"").decode("utf-8", errors="replace") if isinstance(exc.stderr, bytes) else (exc.stderr or ""),
            )
            timed_out = True
        elapsed = round(time.monotonic() - started, 3)

    events = parse_events(result.stdout)
    final = extract_final(args.host, events)
    media_events = media_tool_events(events)
    model_evidence = (
        claude_model_evidence(events, model)
        if args.host == "claude-code"
        else None
    )
    discovered_skills, activated_skills, activation_evidence_by_skill = extract_skill_activity(events)
    activation_evidence = activation_evidence_by_skill.get(skill_name, []) if skill_name else []
    version = cli_version(command)

    write_json(output_dir / "request.json", {
        "case_id": args.case_id,
        "case_sha256": sha256_file(case_path),
        "rubric_sha256": sha256_file(rubric_path),
        "host": args.host,
        "invocation_mode": contract.invocation_mode,
        "expected_skill": skill_name,
        "coverage_class": contract.coverage_class,
        "forbidden_skills": list(contract.forbidden_skills),
        "base_prompt": case["prompt"],
        "effective_prompt": prompt,
        "sanitized_argv": sanitized_argv,
        "disabled_personal_skills": disabled_count,
    })
    write_json(output_dir / "workspace-inventory.json", inventory)
    (output_dir / "events.jsonl").write_text(
        "".join(json.dumps(event, ensure_ascii=False) + "\n" for event in events),
        encoding="utf-8",
    )
    (output_dir / "final.md").write_text(final.rstrip() + "\n", encoding="utf-8")
    (output_dir / "stderr.txt").write_text(sanitize_string(result.stderr), encoding="utf-8")
    (output_dir / "native-evidence.md").write_text(
        render_native_evidence(
            host=args.host,
            cli_version=version,
            requested_model=model,
            requested_effort=effort,
            invocation_mode=contract.invocation_mode,
            expected_skill=skill_name,
            workspace_digest=inventory["digest"],
            activation_evidence=activation_evidence,
            model_evidence=model_evidence,
        ),
        encoding="utf-8",
    )
    write_json(output_dir / "run.json", {
        "case_id": args.case_id,
        "host": args.host,
        "cli_version": version,
        "requested_primary_model": model,
        "requested_effort": effort,
        "fallback_model": None,
        "model_evidence": model_evidence,
        "exit_code": result.returncode,
        "timed_out": timed_out,
        "elapsed_seconds": elapsed,
        "event_count": len(events),
        "final_present": bool(final.strip()),
        "activation_evidence": activation_evidence,
        "packaged_skills": list(PACKAGED_SKILLS),
        "discovered_skills": discovered_skills,
        "activated_skills": activated_skills,
        "activation_evidence_by_skill": activation_evidence_by_skill,
        "research_present": inventory["research_present"],
        "workspace_digest": inventory["digest"],
        "paid_media_tool_events": media_events,
        "sanitization": "session/thread/turn/request/uuid/idempotency identifiers and signed-query values removed before persistence"
    })

    model_invalid = (
        args.host == "claude-code"
        and (
            not model_evidence["requested_model_observed"]
            or model_evidence["fallback_detected"]
        )
    )
    if result.returncode != 0 or not final.strip() or media_events or model_invalid:
        return 1
    incomplete_marker.unlink(missing_ok=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
