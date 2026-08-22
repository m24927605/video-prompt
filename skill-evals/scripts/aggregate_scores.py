#!/usr/bin/env python3
"""Aggregate independently authored behavioral grades and enforce host gates."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _is_integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def grade_validation_errors(
    grade: Any,
    schema: dict[str, Any],
    *,
    case_id: str,
    host: str,
) -> list[str]:
    """Validate the committed grade schema plus cross-file score invariants."""
    if not isinstance(grade, dict):
        return ["grade must be an object"]

    errors: list[str] = []
    required = set(schema["required"])
    properties = schema["properties"]
    missing = sorted(required - set(grade))
    errors.extend(f"missing required field: {name}" for name in missing)
    if schema.get("additionalProperties") is False:
        errors.extend(
            f"unexpected field: {name}"
            for name in sorted(set(grade) - set(properties))
        )

    if grade.get("case_id") != case_id:
        errors.append(f"case_id must equal {case_id!r}")
    if grade.get("host") != host:
        errors.append(f"host must equal {host!r}")
    if grade.get("verdict") not in properties["verdict"]["enum"]:
        errors.append("verdict is not allowed by schema")
    if not isinstance(grade.get("activation_verified"), bool):
        errors.append("activation_verified must be a boolean")

    lane_scores = grade.get("lane_scores")
    lane_schema = properties["lane_scores"]
    lane_total: int | None = None
    if not isinstance(lane_scores, dict):
        errors.append("lane_scores must be an object")
    else:
        lane_properties = lane_schema["properties"]
        missing_lanes = sorted(set(lane_schema["required"]) - set(lane_scores))
        errors.extend(f"missing lane score: {name}" for name in missing_lanes)
        if lane_schema.get("additionalProperties") is False:
            errors.extend(
                f"unexpected lane score: {name}"
                for name in sorted(set(lane_scores) - set(lane_properties))
            )
        lane_values: list[int] = []
        for name, definition in lane_properties.items():
            value = lane_scores.get(name)
            if not _is_integer(value):
                errors.append(f"lane score {name} must be an integer")
                continue
            if value < definition["minimum"] or value > definition["maximum"]:
                errors.append(f"lane score {name} is outside schema bounds")
            lane_values.append(value)
        if len(lane_values) == len(lane_properties):
            lane_total = sum(lane_values)

    total = grade.get("total")
    total_schema = properties["total"]
    if not _is_integer(total):
        errors.append("total must be an integer")
    else:
        if total < total_schema["minimum"] or total > total_schema["maximum"]:
            errors.append("total is outside schema bounds")
        if lane_total is not None and total != lane_total:
            errors.append(f"total {total} does not equal lane score sum {lane_total}")

    for name in ("critical_failures", "evidence"):
        value = grade.get(name)
        definition = properties[name]
        if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
            errors.append(f"{name} must be an array of strings")
        elif len(value) < definition.get("minItems", 0):
            errors.append(f"{name} has too few items")

    grader = grade.get("grader")
    grader_schema = properties["grader"]
    if not isinstance(grader, dict):
        errors.append("grader must be an object")
    else:
        missing_grader = sorted(set(grader_schema["required"]) - set(grader))
        errors.extend(f"missing grader field: {name}" for name in missing_grader)
        if grader_schema.get("additionalProperties") is False:
            errors.extend(
                f"unexpected grader field: {name}"
                for name in sorted(set(grader) - set(grader_schema["properties"]))
            )
        for name in ("role", "model", "effort"):
            if not isinstance(grader.get(name), str):
                errors.append(f"grader {name} must be a string")
        if grader.get("independent") is not True:
            errors.append("grader independent must be true")

    return errors


def aggregate(root: Path) -> bool:
    root = root.resolve()
    cases = {
        path.stem: read_json(path)
        for path in sorted((root / "skill-evals" / "cases").glob("*.json"))
    }
    grade_schema = read_json(root / "skill-evals" / "schemas" / "grade.schema.json")
    rubric_digest = digest(root / "skill-evals" / "rubric.md")
    host_summaries: dict[str, Any] = {}
    overall_pass = True

    for host in ("codex", "claude-code"):
        result_root = root / "skill-evals" / "results" / host
        grades = []
        critical: list[str] = []
        negative_failures: list[str] = []
        explicit_coverage: set[str] = set()
        implicit_coverage: set[str] = set()
        run_failures: list[str] = []
        digest_failures: list[str] = []
        media_events: list[str] = []
        verdict_failures: list[str] = []
        grade_validation_failures: list[str] = []
        validated_grades: list[dict[str, Any]] = []

        for case_id, case in cases.items():
            case_root = result_root / case_id
            grade_path = case_root / "grade.json"
            run_path = case_root / "run.json"
            request_path = case_root / "request.json"
            if not grade_path.is_file() or not run_path.is_file() or not request_path.is_file():
                run_failures.append(f"{case_id}: missing grade/run/request")
                continue
            grade = read_json(grade_path)
            run = read_json(run_path)
            request = read_json(request_path)
            grades.append(grade)
            validation_errors = grade_validation_errors(
                grade,
                grade_schema,
                case_id=case_id,
                host=host,
            )
            if validation_errors:
                grade_validation_failures.extend(
                    f"{case_id}: {error}" for error in validation_errors
                )
                continue
            validated_grades.append(grade)
            critical.extend(f"{case_id}: {item}" for item in grade.get("critical_failures", []))
            if grade["verdict"] != "PASS":
                verdict_failures.append(case_id)
            if run.get("exit_code") != 0 or not run.get("final_present") or run.get("research_present"):
                run_failures.append(case_id)
            if run.get("paid_media_tool_events"):
                media_events.append(case_id)
            if request.get("rubric_sha256") != rubric_digest or request.get("case_sha256") != digest(root / "skill-evals" / "cases" / f"{case_id}.json"):
                digest_failures.append(case_id)

            skill = case.get("expected_skill")
            activation_verified = bool(grade.get("activation_verified", False))
            if skill and activation_verified:
                if case["invocation_mode"] == "explicit":
                    explicit_coverage.add(skill)
                else:
                    implicit_coverage.add(skill)
            if not skill and (grade["lane_scores"]["activation_routing"] < 10 or grade.get("critical_failures")):
                negative_failures.append(case_id)

        possible = len(cases) * 100
        points = sum(grade["total"] for grade in validated_grades)
        percent = round(points / possible * 100, 2) if possible else 0.0
        all_skills = {case["expected_skill"] for case in cases.values() if case.get("expected_skill")}
        host_pass = all((
            len(grades) == len(cases),
            percent >= 90.0,
            not critical,
            not negative_failures,
            explicit_coverage == all_skills,
            implicit_coverage == all_skills,
            not run_failures,
            not digest_failures,
            not media_events,
            not verdict_failures,
            not grade_validation_failures,
        ))
        summary = {
            "host": host,
            "case_count": len(cases),
            "graded_count": len(grades),
            "score_percent": percent,
            "critical_failures": critical,
            "negative_activation_failures": negative_failures,
            "explicit_skill_coverage": sorted(explicit_coverage),
            "implicit_skill_coverage": sorted(implicit_coverage),
            "run_failures": run_failures,
            "digest_failures": digest_failures,
            "paid_media_tool_event_cases": media_events,
            "verdict_failures": verdict_failures,
            "grade_validation_failures": grade_validation_failures,
            "rubric_sha256": rubric_digest,
            "status": "PASS" if host_pass else "FAIL",
        }
        write_json(result_root / "summary.json", summary)
        host_summaries[host] = summary
        overall_pass = overall_pass and host_pass

    write_json(root / "skill-evals" / "results" / "summary.json", {
        "status": "PASS" if overall_pass else "FAIL",
        "hosts": host_summaries,
    })
    return overall_pass


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    return 0 if aggregate(args.repo_root) else 1


if __name__ == "__main__":
    raise SystemExit(main())
