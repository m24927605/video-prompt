"""Focused behavioral-contract tests for Seedance Prompt Director routing.

These assertions intentionally check durable skill instructions, not generated
prose. Host evaluations exercise whether an agent follows the contracts.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "skills" / "seedance-prompt-director" / "SKILL.md"
SCHEMA = SKILL.parent / "references" / "prompt-schema.md"
PROVENANCE = SKILL.parent / "references" / "provenance.md"


class SeedancePromptDirectorRoutingContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = SKILL.read_text(encoding="utf-8")
        cls.schema = SCHEMA.read_text(encoding="utf-8")
        cls.provenance = PROVENANCE.read_text(encoding="utf-8")
        cls.operational_text = f"{cls.skill}\n{cls.schema}"

    def test_requested_deliverable_controls_output_shape(self) -> None:
        self.assertIn("## Requested deliverable lock", self.skill)
        self.assertRegex(
            self.skill,
            r"(?is)prompt-only.*only.*(?:one )?pasteable prompt.*no.*(?:input basis|acceptance|risk|revision)",
        )
        self.assertRegex(
            self.skill,
            r"(?is)diagnosis-only.*(?:diagnos|evidence).*do not.*(?:rewrite|replacement|final prompt)",
        )
        self.assertRegex(
            self.skill,
            r"(?is)revision.*preserve.*(?:requested|supplied).*structure.*do not.*default.*packet",
        )
        self.assertRegex(
            self.skill,
            r"(?is)full production packet.*only.*(?:when|if).*requested deliverable.*(?:requires|calls for)",
        )
        self.assertRegex(
            self.skill,
            r"(?is)(?:write|create|give).*a prompt.*does not.*prompt-only.*explicitly.*only",
        )
        self.assertRegex(
            self.skill,
            r"(?is)no explicit narrowing.*default production packet",
        )
        self.assertRegex(
            self.skill,
            r"(?is)prompt-only.*complete response.*prompt itself.*(?:do not add|no).*title.*preface.*separator.*code fence.*postscript",
        )

    def test_each_artifact_has_exactly_one_primary_operation(self) -> None:
        self.assertIn("## Primary-operation routing", self.skill)
        self.assertRegex(
            self.skill,
            r"(?is)each (?:returned )?artifact.*exactly one primary operation",
        )
        self.assertRegex(
            self.skill,
            r"(?is)(?:generate|edit|extend).*not.*mixed.*(?:within|in).*same artifact",
        )
        self.assertRegex(
            self.skill,
            r"(?is)two.*(?:sequential|consecutive).*operations.*separate.*ordered artifacts",
        )
        self.assertRegex(
            self.schema,
            r"(?is)primary operation.*(?:generate|reference|edit|extend|first frame|first/last)",
        )

    def test_extension_direction_contracts_do_not_invent_a_boundary(self) -> None:
        self.assertIn("## Extension direction and boundary", self.schema)
        self.assertRegex(
            self.schema,
            r"(?is)bare.*(?:forward|backward).*ask.*one.*(?:before|after).*boundary question",
        )
        self.assertRegex(
            self.schema,
            r"(?is)do not.*(?:assume|infer).*before.*after",
        )
        self.assertRegex(
            self.schema,
            r"(?is)append.*only.*added.*(?:interval|material).*preserve.*source",
        )
        self.assertRegex(
            self.schema,
            r"(?is)prepend.*only.*added.*(?:interval|material).*preserve.*source",
        )
        for phrase in ("向前續寫", "向後續寫", "往前延長", "往後延長"):
            self.assertIn(phrase, self.schema)
        self.assertRegex(
            self.schema,
            r"(?is)prompt-only.*does not override.*boundary.*question",
        )
        self.assertRegex(
            self.schema,
            r"(?is)after.*confirmed.*use only.*(?:before the source|after the source).*do not.*(?:forward|backward).*label",
        )

    def test_narrow_delivery_never_licenses_unverified_parameters(self) -> None:
        self.assertRegex(
            self.skill,
            r"(?is)prompt-only.*does not relax.*runtime.*gate",
        )
        self.assertRegex(
            self.skill,
            r"(?is)unverified.*(?:aspect|ratio).*resolution.*format.*omit.*prompt",
        )

    def test_existing_provenance_rules_cover_the_new_routing_contracts(self) -> None:
        pd16 = re.search(r"\| PD-16 \|(?P<rule>.*?)\|", self.provenance)
        pd17 = re.search(r"\| PD-17 \|(?P<rule>.*?)\|", self.provenance)
        self.assertIsNotNone(pd16)
        self.assertIsNotNone(pd17)
        self.assertRegex(pd16.group("rule"), r"(?i)operation|edit|extend")
        self.assertRegex(pd17.group("rule"), r"(?i)deliverable|revision|output")
        self.assertIn("PD-16", self.operational_text)
        self.assertIn("PD-17", self.operational_text)


if __name__ == "__main__":
    unittest.main()
