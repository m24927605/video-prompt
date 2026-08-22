#!/usr/bin/env python3
"""Persist sanitized evidence from a direct Claude Code stream-json invocation.

This collector never starts Claude. It reads the direct host CLI event stream from
stdin so authentication and model execution remain in the approved `claude -p`
process.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import time
from pathlib import Path
from typing import Any


RUNNER_PATH = Path(__file__).with_name("run_host_eval.py")
RUNNER_SPEC = importlib.util.spec_from_file_location("run_host_eval_helpers", RUNNER_PATH)
assert RUNNER_SPEC and RUNNER_SPEC.loader
RUNNER = importlib.util.module_from_spec(RUNNER_SPEC)
RUNNER_SPEC.loader.exec_module(RUNNER)


def direct_discovery(events: list[dict[str, Any]]) -> dict[str, Any]:
    for event in events:
        if event.get("type") == "system" and event.get("subtype") == "init":
            return {
                "model": event.get("model"),
                "skills": event.get("skills", []),
                "slash_commands": event.get("slash_commands", []),
                "tools": event.get("tools", []),
                "mcp_servers": event.get("mcp_servers", []),
                "plugins": event.get("plugins", []),
            }
    return {}


def persist_direct_claude_eval(
    *,
    repo_root: Path,
    output_root: Path,
    workspace: Path,
    case_id: str,
    stdout: str,
    elapsed_seconds: float,
) -> dict[str, Any]:
    case_path = repo_root / "skill-evals" / "cases" / f"{case_id}.json"
    rubric_path = repo_root / "skill-evals" / "rubric.md"
    case = json.loads(case_path.read_text(encoding="utf-8"))
    if case["id"] != case_id:
        raise ValueError("case id does not match filename")

    skill_name = case.get("expected_skill")
    prompt = case["prompt"]
    if case["invocation_mode"] == "explicit":
        if not skill_name:
            raise ValueError("explicit case requires expected_skill")
        prompt = f"/{skill_name}\n\n{prompt}"

    inventory = RUNNER.workspace_inventory(workspace, "claude-code")
    allowed_prefixes = ("skills/", ".claude/skills/")
    unexpected_entries = [
        entry["path"]
        for entry in inventory["entries"]
        if not entry["path"].startswith(allowed_prefixes)
    ]
    if inventory["research_present"] or inventory["grader_present"] or unexpected_entries:
        raise ValueError(f"isolated workspace contains unexpected entries: {unexpected_entries}")

    events = RUNNER.parse_events(stdout)
    final = RUNNER.extract_final("claude-code", events)
    model_evidence = RUNNER.claude_model_evidence(events, "claude-fable-5")
    activation_evidence = RUNNER.activation_events(events, skill_name)
    media_events = RUNNER.media_tool_events(events)
    discovery = direct_discovery(events)
    result_events = [event for event in events if event.get("type") == "result"]
    result_event = result_events[-1] if result_events else {}
    terminal_error = not result_events or bool(result_event.get("is_error"))
    expected_skills = set(RUNNER.SKILLS)
    discovered_skills = set(discovery.get("skills", []))
    discovery_complete = expected_skills.issubset(discovered_skills)
    model_valid = (
        model_evidence["requested_model_observed"]
        and not model_evidence["fallback_detected"]
    )
    success = bool(final.strip()) and model_valid and discovery_complete and not terminal_error and not media_events

    output_dir = output_root / case_id
    output_dir.mkdir(parents=True, exist_ok=True)
    argv, sanitized_argv, _ = RUNNER.claude_argv(prompt)
    version = RUNNER.cli_version("claude")

    RUNNER.write_json(output_dir / "request.json", {
        "case_id": case_id,
        "case_sha256": RUNNER.sha256_file(case_path),
        "rubric_sha256": RUNNER.sha256_file(rubric_path),
        "host": "claude-code",
        "invocation_mode": case["invocation_mode"],
        "expected_skill": skill_name,
        "base_prompt": case["prompt"],
        "effective_prompt": prompt,
        "sanitized_argv": sanitized_argv,
        "execution": "direct claude -p stream-json piped to sanitizer; collector does not invoke host",
    })
    RUNNER.write_json(output_dir / "workspace-inventory.json", inventory)
    (output_dir / "events.jsonl").write_text(
        "".join(json.dumps(event, ensure_ascii=False) + "\n" for event in events),
        encoding="utf-8",
    )
    RUNNER.write_json(output_dir / "response.json", result_event)
    (output_dir / "final.md").write_text(final.rstrip() + "\n", encoding="utf-8")
    (output_dir / "stderr.txt").write_text("", encoding="utf-8")

    native = RUNNER.render_native_evidence(
        host="claude-code",
        cli_version=version,
        requested_model="claude-fable-5",
        requested_effort="max",
        invocation_mode=case["invocation_mode"],
        expected_skill=skill_name,
        workspace_digest=inventory["digest"],
        activation_evidence=activation_evidence,
        model_evidence=model_evidence,
    )
    listed = ", ".join(sorted(discovered_skills)) or "none"
    native += f"- Native skills listed by Claude init: `{listed}`\n"
    native += f"- Native discovery complete: `{str(discovery_complete).lower()}`\n"
    (output_dir / "native-evidence.md").write_text(native, encoding="utf-8")

    RUNNER.write_json(output_dir / "run.json", {
        "case_id": case_id,
        "host": "claude-code",
        "cli_version": version,
        "requested_primary_model": "claude-fable-5",
        "requested_effort": "max",
        "fallback_model": None,
        "model_evidence": model_evidence,
        "direct_discovery": discovery,
        "discovery_complete": discovery_complete,
        "exit_code": 0 if success else 1,
        "timed_out": False,
        "elapsed_seconds": round(elapsed_seconds, 3),
        "event_count": len(events),
        "final_present": bool(final.strip()),
        "terminal_error": terminal_error,
        "activation_evidence": activation_evidence,
        "research_present": inventory["research_present"],
        "workspace_digest": inventory["digest"],
        "paid_media_tool_events": media_events,
        "sanitization": "session/thread/turn/request/uuid/idempotency/cwd/memory-path identifiers and signed-query values removed before persistence",
    })

    return {
        "case_id": case_id,
        "success": success,
        "event_count": len(events),
        "final_bytes": len(final.encode("utf-8")),
        "model_evidence": model_evidence,
        "discovery_complete": discovery_complete,
        "paid_media_tool_events": media_events,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", required=True, dest="case_id")
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
    )
    parser.add_argument("--output-root", type=Path)
    args = parser.parse_args()

    started = time.monotonic()
    stdout = sys.stdin.read()
    repo_root = args.repo_root.resolve()
    output_root = (
        args.output_root.resolve()
        if args.output_root
        else repo_root / "skill-evals" / "results" / "claude-code"
    )
    result = persist_direct_claude_eval(
        repo_root=repo_root,
        output_root=output_root,
        workspace=args.workspace.resolve(),
        case_id=args.case_id,
        stdout=stdout,
        elapsed_seconds=time.monotonic() - started,
    )
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
