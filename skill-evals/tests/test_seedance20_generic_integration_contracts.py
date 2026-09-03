"""Focused clean-room contracts for generic use of Seedance 2.0 research."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROMPT = ROOT / "skills" / "seedance-prompt-director" / "references"
PRODUCER = ROOT / "skills" / "seedance-film-producer" / "references"
REFERENCE = (PROMPT / "reference-motion-audio.md").read_text(encoding="utf-8")
SCHEMA = (PROMPT / "prompt-schema.md").read_text(encoding="utf-8")
PD_PROVENANCE = (PROMPT / "provenance.md").read_text(encoding="utf-8")
LINEAGE = (PRODUCER / "assets-continuity-lineage.md").read_text(encoding="utf-8")
HIERARCHY = (PRODUCER / "production-hierarchy.md").read_text(encoding="utf-8")
FP_PROVENANCE = (PRODUCER / "provenance.md").read_text(encoding="utf-8")
CASE_IDS = {
    "reference-dimension-authority",
    "continuation-observation-boundary",
    "accepted-deviation-beat-firewall",
    "seedance20-to-25-version-isolation",
}


class Seedance20GenericIntegrationContractTests(unittest.TestCase):
    def test_reference_tokens_and_dimension_authority_are_fail_closed(self) -> None:
        self.assertIn("## Reference token and dimension authority", REFERENCE)
        self.assertRegex(
            REFERENCE,
            r"(?is)byte-for-byte.*do not.*(?:invent|normalize|translate|renumber)",
        )
        self.assertRegex(
            REFERENCE,
            r"(?is)target.*dimension.*unique winner.*explicit user mapping.*priority",
        )
        self.assertRegex(
            REFERENCE,
            r"(?is)no winner.*inactive.*do not.*(?:media type|upload order).*guess",
        )
        self.assertRegex(
            REFERENCE,
            r"(?is)token syntax.*only.*selected surface.*(?:verified|documented)",
        )

    def test_continuation_observation_and_conflict_boundaries_are_explicit(self) -> None:
        self.assertIn("## Observation and conflict boundary", SCHEMA)
        self.assertRegex(
            SCHEMA,
            r"(?is)final frame.*(?:pose|position|visible wardrobe|props|environment|light|framing)",
        )
        self.assertRegex(
            SCHEMA,
            r"(?is)(?:motion|camera velocity|audio phase).*unknown",
        )
        self.assertRegex(
            SCHEMA,
            r"(?is)cannot inspect.*user-reported.*low confidence.*uncertainties.*do not.*(?:observed|canonical)",
        )
        self.assertRegex(
            SCHEMA,
            r"(?is)rights/safety.*verified selected-surface constraint.*explicit user must-have.*ref(?:erence)? authority.*continuity.*causal legibility.*camera/editorial.*style.*defaults",
        )
        self.assertRegex(SCHEMA, r"(?is)resolution loses.*user constraint.*disclose")

    def test_film_continuation_and_beat_firewall_keep_accepted_state_separate(self) -> None:
        self.assertIn("## Continuation relation and accepted-state firewall", LINEAGE)
        self.assertRegex(
            LINEAGE,
            r"(?is)(?:same-shot seamless|intentional next shot|bridge known states|repair tail|reanchor drift)",
        )
        self.assertRegex(
            LINEAGE,
            r"(?is)same-shot seamless.*same scene.*geography.*open motion",
        )
        self.assertRegex(
            LINEAGE,
            r"(?is)scene boundary.*intentional next shot",
        )
        self.assertRegex(
            LINEAGE,
            r"(?is)accepted source.*existing state.*prompt text.*only.*delta",
        )
        self.assertRegex(
            HIERARCHY,
            r"(?is)completed.*current.*reserved.*beat firewall",
        )
        self.assertRegex(
            HIERARCHY,
            r"(?is)accepted deviation.*completes.*future beat.*remove.*downstream",
        )
        self.assertRegex(HIERARCHY, r"(?is)rejected.*not.*canonical")
        self.assertRegex(
            LINEAGE,
            r"(?is)do not.*numeric.*(?:retry|chain|work.slice|review.cycle).*unless.*(?:user|project).*provided.*internal agent.*outside.*deliverable",
        )

    def test_version_isolation_and_existing_provenance_rule_ownership(self) -> None:
        self.assertIn("## Version isolation", SCHEMA)
        self.assertRegex(
            SCHEMA,
            r"(?is)2\.0.*(?:number|model ID|API|tag|mode).*not.*(?:2\.5|generic)",
        )
        self.assertRegex(SCHEMA, r"(?is)craft.*transfer(?:able|s)")
        for text, rule_id, terms in (
            (PD_PROVENANCE, "PD-04", r"schema|contract"),
            (PD_PROVENANCE, "PD-05", r"reference|authority"),
            (PD_PROVENANCE, "PD-15", r"version|invent"),
            (PD_PROVENANCE, "PD-16", r"extend|continuation|task"),
            (FP_PROVENANCE, "FP-05", r"accepted|handoff|state"),
            (FP_PROVENANCE, "FP-06", r"beat|schedule|delta"),
            (FP_PROVENANCE, "FP-15", r"extension|continuation|drift"),
        ):
            row = re.search(rf"\| {rule_id} \|(?P<rule>.*?)\|", text)
            self.assertIsNotNone(row, rule_id)
            self.assertRegex(row.group("rule"), rf"(?i){terms}", rule_id)

    def test_held_out_cases_and_graders_cover_each_contract(self) -> None:
        for case_id in CASE_IDS:
            case = ROOT / "skill-evals" / "cases" / f"{case_id}.json"
            grader = ROOT / "skill-evals" / "graders" / f"{case_id}.json"
            self.assertTrue(case.is_file(), case)
            self.assertTrue(grader.is_file(), grader)
            self.assertGreater(len(case.read_text(encoding="utf-8")), 120)
            self.assertIn(case_id, grader.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
