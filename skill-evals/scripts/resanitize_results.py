#!/usr/bin/env python3
"""Reapply the current sanitizer to persisted Claude evaluation artifacts."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


RUNNER_PATH = Path(__file__).with_name("run_host_eval.py")
SPEC = importlib.util.spec_from_file_location("run_host_eval_helpers", RUNNER_PATH)
assert SPEC and SPEC.loader
RUNNER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RUNNER)


def resanitize_case(case_dir: Path, host: str) -> dict[str, object]:
    events_path = case_dir / "events.jsonl"
    events = (
        RUNNER.parse_events(events_path.read_text(encoding="utf-8"))
        if events_path.is_file()
        else []
    )
    final = RUNNER.extract_final(host, events) if events else ""
    final_path = case_dir / "final.md"
    if not final and final_path.is_file():
        final = RUNNER.sanitize_string(final_path.read_text(encoding="utf-8"))
    result_events = [event for event in events if event.get("type") == "result"]
    result_event = result_events[-1] if result_events else {}

    if events_path.is_file():
        events_path.write_text(
            "".join(json.dumps(event, ensure_ascii=False) + "\n" for event in events),
            encoding="utf-8",
        )
    if host == "claude-code" and result_event:
        RUNNER.write_json(case_dir / "response.json", result_event)
    if final:
        final_path.write_text(final.rstrip() + "\n", encoding="utf-8")

    run_path = case_dir / "run.json"
    if run_path.is_file():
        run = RUNNER.sanitize(json.loads(run_path.read_text(encoding="utf-8")))
        run["sanitization"] = (
            "Current sanitizer reapplied: session/thread/turn/request/uuid/cwd/memory, "
            "user-home and ephemeral-workspace paths, and signed-query values redacted."
        )
        RUNNER.write_json(run_path, run)

    for filename in ("request.json", "grade.json"):
        path = case_dir / filename
        if path.is_file():
            RUNNER.write_json(path, RUNNER.sanitize(json.loads(path.read_text(encoding="utf-8"))))
    for filename in ("native-evidence.md", "stderr.txt"):
        path = case_dir / filename
        if path.is_file():
            path.write_text(RUNNER.sanitize_string(path.read_text(encoding="utf-8")), encoding="utf-8")

    return {
        "case": case_dir.name,
        "status": "PASS",
        "events": len(events),
        "final_bytes": len(final.encode("utf-8")),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--results-root",
        type=Path,
    )
    parser.add_argument("--host", choices=("codex", "claude-code"), default="claude-code")
    parser.add_argument("--case")
    args = parser.parse_args()

    root = (
        args.results_root.resolve()
        if args.results_root
        else Path(__file__).resolve().parents[1] / "results" / args.host
    )
    case_dirs = [root / args.case] if args.case else sorted(path for path in root.iterdir() if path.is_dir())
    results = [resanitize_case(case_dir, args.host) for case_dir in case_dirs]
    print(json.dumps(results, indent=2, ensure_ascii=False))
    return 0 if all(item["status"] in {"PASS", "SKIP"} for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
