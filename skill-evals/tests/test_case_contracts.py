from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "skill-evals" / "scripts" / "case_contracts.py"


def load_contracts():
    spec = importlib.util.spec_from_file_location("case_contracts", MODULE_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CaseContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.contracts = load_contracts()

    def test_default_coverage_is_archived_and_known_skills_are_packaged(self) -> None:
        contract = self.contracts.parse_case_contract({
            "id": "archived-case",
            "invocation_mode": "implicit",
            "expected_skill": "seedance-prompt-director",
        })

        self.assertEqual("archived", contract.coverage_class)
        self.assertEqual(5, len(self.contracts.PACKAGED_SKILLS))
        self.assertEqual(
            {
                "seedance-prompt-director",
                "seedance-film-producer",
                "seedance-video-qc",
            },
            set(self.contracts.ARCHIVED_BEHAVIORAL_SKILLS),
        )

    def test_forbidden_skills_are_packaged_unique_and_not_expected(self) -> None:
        valid = self.contracts.parse_case_contract({
            "id": "collision-case",
            "invocation_mode": "implicit",
            "expected_skill": "seedance-prompt-director",
            "coverage_class": "collision",
            "forbidden_skills": ["photography-aesthetics"],
        })
        self.assertEqual(("photography-aesthetics",), valid.forbidden_skills)

        for forbidden in (
            ["unknown-skill"],
            ["seedance-prompt-director"],
            ["photography-aesthetics", "photography-aesthetics"],
        ):
            with self.subTest(forbidden=forbidden):
                with self.assertRaises(self.contracts.CaseContractError):
                    self.contracts.parse_case_contract({
                        "id": "bad-collision",
                        "invocation_mode": "implicit",
                        "expected_skill": "seedance-prompt-director",
                        "coverage_class": "collision",
                        "forbidden_skills": forbidden,
                    })

    def test_unknown_coverage_and_explicit_negative_case_fail_closed(self) -> None:
        with self.assertRaises(self.contracts.CaseContractError):
            self.contracts.parse_case_contract({
                "id": "bad-coverage",
                "invocation_mode": "implicit",
                "expected_skill": None,
                "coverage_class": "future",
            })
        with self.assertRaises(self.contracts.CaseContractError):
            self.contracts.parse_case_contract({
                "id": "bad-archived-photography",
                "invocation_mode": "implicit",
                "expected_skill": "photography-aesthetics",
            })
        with self.assertRaises(self.contracts.CaseContractError):
            self.contracts.parse_case_contract({
                "id": "bad-explicit-negative",
                "invocation_mode": "explicit",
                "expected_skill": None,
            })

    def test_non_string_contract_fields_fail_as_case_errors(self) -> None:
        for field, value in (
            ("expected_skill", ["seedance-prompt-director"]),
            ("coverage_class", ["collision"]),
            ("invocation_mode", ["implicit"]),
        ):
            with self.subTest(field=field):
                case = {
                    "id": "bad-types",
                    "invocation_mode": "implicit",
                    "expected_skill": None,
                }
                case[field] = value
                with self.assertRaises(self.contracts.CaseContractError):
                    self.contracts.parse_case_contract(case)

    def test_live_action_negative_fixture_makes_visibility_goal_explicit(self) -> None:
        case = json.loads(
            (ROOT / "skill-evals" / "cases" / "negative-live-action-critique.json").read_text(
                encoding="utf-8"
            )
        )

        self.assertIn("accidentally", case["prompt"].lower())
        self.assertRegex(case["prompt"].lower(), r"keep both actors visible|restore.*visibility")

    def test_static_image_fixture_makes_unknown_provider_boundary_explicit(self) -> None:
        case = json.loads(
            (ROOT / "skill-evals" / "cases" / "negative-image-design.json").read_text(
                encoding="utf-8"
            )
        )

        self.assertIn("provider-neutral", case["prompt"])
        self.assertIn("不要列出模型名稱", case["prompt"])
        self.assertIn("negative prompt", case["prompt"])


if __name__ == "__main__":
    unittest.main()
