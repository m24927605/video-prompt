"""Focused contract tests for asset scope, generic packets, and causal audits."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SKILL_ROOT = ROOT / "skills" / "seedance-prompt-director"
SCHEMA = (SKILL_ROOT / "references" / "prompt-schema.md").read_text(encoding="utf-8")
REFERENCE = (SKILL_ROOT / "references" / "reference-motion-audio.md").read_text(encoding="utf-8")
FAILURES = (SKILL_ROOT / "references" / "revision-failure-patterns.md").read_text(encoding="utf-8")
PROVENANCE = (SKILL_ROOT / "references" / "provenance.md").read_text(encoding="utf-8")


class SeedancePromptDirectorAssetModeContractTests(unittest.TestCase):
    def test_active_reference_contract_has_all_scope_fields(self) -> None:
        self.assertIn("## Active reference contract", REFERENCE)
        for field in (
            "source/upload label",
            "target",
            "active scope/time",
            "preserve/allowed inheritance",
            "excluded inheritance",
        ):
            self.assertIn(field, REFERENCE)
        self.assertRegex(
            REFERENCE,
            r"(?is)every active reference.*all five.*contract fields",
        )

    def test_person_and_face_only_reference_scopes_do_not_leak(self) -> None:
        self.assertIn("## Person-reference scope", REFERENCE)
        self.assertRegex(
            REFERENCE,
            r"(?is)(?:unqualified|unscoped).*person.*full visible person.*identity.*hair.*body.*visible wardrobe.*footwear.*accessories",
        )
        self.assertRegex(
            REFERENCE,
            r"(?is)full visible person.*exclude.*background.*pose.*composition.*crop.*light",
        )
        self.assertRegex(
            REFERENCE,
            r"(?is)(?:face-only|identity-only).*explicitly.*(?:face|identity).*not.*lock.*wardrobe",
        )

    def test_structure_only_examples_inherit_only_structure_dimensions(self) -> None:
        self.assertIn("## Example inheritance by dimension", REFERENCE)
        self.assertRegex(
            REFERENCE,
            r"(?is)structure-only.*(?:hierarchy|control depth|granularity)",
        )
        self.assertRegex(
            REFERENCE,
            r"(?is)structure-only.*do not inherit.*story.*POV.*camera.*style.*assets.*dialogue.*outcome",
        )

    def test_generic_packets_are_scoped_without_claiming_provider_support(self) -> None:
        self.assertIn("## Generic conditional packets", SCHEMA)
        self.assertRegex(
            SCHEMA,
            r"(?is)not.*(?:provider|platform).*support.*claim",
        )
        self.assertRegex(
            SCHEMA,
            r"(?is)marked edit.*annotation.*target.*A→B.*time.*preserve",
        )
        self.assertRegex(
            SCHEMA,
            r"(?is)transition bridge.*two sources.*unchanged.*exit.*bridge.*entry.*continuity",
        )
        self.assertRegex(
            SCHEMA,
            r"(?is)coarse.*clay/blockout.*map every.*(?:model|shape|object).*paths.*blocking.*camera.*exclude.*(?:primitive|gray|guide|overlay)",
        )
        self.assertRegex(
            SCHEMA,
            r"(?is)fine.*clay/blockout.*preserve.*structure.*action.*spatial.*camera.*change only.*(?:appearance|material|environment|render).*exclude.*(?:guide|axis|cone|overlay)",
        )
        self.assertRegex(
            SCHEMA,
            r"(?is)ordered storyboard.*single.*generate.*clip.*reading order.*each panel.*(?:complete )?shot.*composition.*action.*end state.*(?:line art|annotation|placeholder).*multi-shot.*seedance-film-producer",
        )
        self.assertNotIn("Dreamina", SCHEMA)

    def test_causal_and_contradiction_audits_cover_known_conflicts(self) -> None:
        self.assertIn("## Causal and contradiction audit", FAILURES)
        for phrase in (
            "trigger before reaction",
            "contact before response",
            "listening/breath/reaction budget",
            "one-take vs cuts",
            "fixed camera vs viewpoint jump",
            "no-two-shot",
            "no BGM vs score",
            "protected source vs restyle",
            "fixed distance vs face-filling framing",
            "third-person view vs character-owned camera",
            "changed outcome vs stale constraints",
        ):
            self.assertIn(phrase, FAILURES)

    def test_existing_provenance_rules_cover_added_contracts(self) -> None:
        for rule_id, terms in {
            "PD-05": r"reference|inheritance",
            "PD-10": r"contact|blockout|physics",
            "PD-11": r"acting|reaction|causal",
            "PD-13": r"dialogue|audio|listening",
            "PD-16": r"edit|extend|task",
        }.items():
            row = re.search(rf"\| {rule_id} \|(?P<rule>.*?)\|", PROVENANCE)
            self.assertIsNotNone(row, rule_id)
            self.assertRegex(row.group("rule"), rf"(?i){terms}", rule_id)


if __name__ == "__main__":
    unittest.main()
