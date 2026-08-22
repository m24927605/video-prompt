from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "skill-evals" / "scripts" / "aggregate_scores.py"
SPEC = importlib.util.spec_from_file_location("aggregate_scores", MODULE_PATH)
assert SPEC and SPEC.loader
AGGREGATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AGGREGATOR)


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class AggregateScoresTests(unittest.TestCase):
    def build_repo(self, root: Path) -> None:
        eval_root = root / "skill-evals"
        (eval_root / "cases").mkdir(parents=True)
        (eval_root / "schemas").mkdir(parents=True)
        shutil.copyfile(
            ROOT / "skill-evals" / "schemas" / "grade.schema.json",
            eval_root / "schemas" / "grade.schema.json",
        )
        (eval_root / "rubric.md").write_text("fixture rubric\n", encoding="utf-8")
        case = {
            "id": "negative-case",
            "invocation_mode": "implicit",
            "expected_skill": None,
        }
        case_path = eval_root / "cases" / "negative-case.json"
        write_json(case_path, case)

        grade = {
            "case_id": "negative-case",
            "host": "",
            "lane_scores": {
                "activation_routing": 10,
                "production_usability": 25,
                "task_completeness": 35,
                "evidence_discipline": 20,
                "language_scope": 10,
            },
            "total": 100,
            "verdict": "PASS",
            "critical_failures": [],
            "activation_verified": False,
            "evidence": ["fixture evidence"],
            "grader": {
                "role": "fixture grader",
                "model": "fixture-model",
                "effort": "high",
                "independent": True,
            },
        }
        request = {
            "case_sha256": sha256(case_path),
            "rubric_sha256": sha256(eval_root / "rubric.md"),
        }
        run = {
            "exit_code": 0,
            "final_present": True,
            "research_present": False,
            "paid_media_tool_events": [],
        }
        for host in ("codex", "claude-code"):
            case_root = eval_root / "results" / host / "negative-case"
            host_grade = dict(grade, host=host)
            write_json(case_root / "grade.json", host_grade)
            write_json(case_root / "request.json", request)
            write_json(case_root / "run.json", run)

    def test_valid_grades_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.build_repo(root)

            self.assertTrue(AGGREGATOR.aggregate(root))

    def test_fail_verdict_blocks_host_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.build_repo(root)
            grade_path = root / "skill-evals" / "results" / "codex" / "negative-case" / "grade.json"
            grade = json.loads(grade_path.read_text(encoding="utf-8"))
            grade["verdict"] = "FAIL"
            write_json(grade_path, grade)

            self.assertFalse(AGGREGATOR.aggregate(root))
            summary = json.loads(
                (root / "skill-evals" / "results" / "codex" / "summary.json").read_text(encoding="utf-8")
            )
            self.assertEqual(["negative-case"], summary["verdict_failures"])

    def test_schema_and_score_mismatches_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.build_repo(root)
            grade_path = root / "skill-evals" / "results" / "codex" / "negative-case" / "grade.json"
            grade = json.loads(grade_path.read_text(encoding="utf-8"))
            grade["case_id"] = "wrong-case"
            grade["total"] = 99
            write_json(grade_path, grade)

            self.assertFalse(AGGREGATOR.aggregate(root))
            summary = json.loads(
                (root / "skill-evals" / "results" / "codex" / "summary.json").read_text(encoding="utf-8")
            )
            failures = summary["grade_validation_failures"]
            self.assertTrue(any("case_id" in item for item in failures))
            self.assertTrue(any("lane score sum" in item for item in failures))


if __name__ == "__main__":
    unittest.main()
