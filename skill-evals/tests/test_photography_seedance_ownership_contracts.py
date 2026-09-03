"""Focused ownership contracts for the five-skill suite.

These assertions protect routing boundaries in the photography skill.  They do
not prescribe a generated prompt; host evaluations test that behavior.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "skills" / "photography-aesthetics" / "SKILL.md"
METADATA = SKILL.parent / "agents" / "openai.yaml"
MOTION = SKILL.parent / "references" / "08-motion.md"
LIGHTING = SKILL.parent / "references" / "01-lighting.md"
DIALECTS = SKILL.parent / "references" / "09-model-dialects.md"
PROMPT_DIRECTOR = ROOT / "skills" / "seedance-prompt-director" / "SKILL.md"


class PhotographySeedanceOwnershipContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = SKILL.read_text(encoding="utf-8")
        cls.metadata = METADATA.read_text(encoding="utf-8")
        cls.motion = MOTION.read_text(encoding="utf-8")
        cls.lighting = LIGHTING.read_text(encoding="utf-8")
        cls.dialects = DIALECTS.read_text(encoding="utf-8")
        cls.prompt_director = PROMPT_DIRECTOR.read_text(encoding="utf-8")

    def test_routes_full_video_shot_contracts_to_prompt_director(self) -> None:
        self.assertIn("## Skill ownership and handoff", self.skill)
        self.assertRegex(
            self.skill,
            r"(?is)single.*shot.*clip.*(?:task|reference|timeline|blocking|physics|acting|audio|end.state|acceptance).*seedance-prompt-director",
        )
        self.assertRegex(
            self.skill,
            r"(?is)multi.shot.*(?:production|continuity|planning).*seedance-film-producer",
        )
        self.assertRegex(
            self.prompt_director,
            r"(?is)visual-look-only.*photography-aesthetics.*complete.*(?:shot|clip).*subcontract",
        )

    def test_keeps_visual_look_and_motion_as_a_scoped_subcontract(self) -> None:
        self.assertRegex(
            self.skill,
            r"(?is)visual.look.*subcontract.*(?:lighting|framing|lens|tone|color|texture|camera|motion)",
        )
        self.assertRegex(
            self.motion,
            r"(?is)visual.look.*subcontract.*(?:opening|change|end)",
        )
        self.assertRegex(
            self.motion,
            r"(?is)does not.*(?:own|decide).*(?:provider|task|operation).*contract",
        )

    def test_does_not_keep_universal_single_clip_cut_or_provider_rules(self) -> None:
        self.assertNotRegex(self.skill, r"(?is)單一片段內禁止寫 cut|轉場一律後製")
        self.assertNotRegex(self.motion, r"(?is)單一片段內禁止出現剪接語彙|多鏡頭一律分次生成")
        self.assertNotRegex(self.dialects, r"\| \*\*Seedance\*\*（影片）")
        self.assertRegex(
            self.motion,
            r"(?is)(?:transition|cut).*only.*(?:when|if).*operation contract",
        )

    def test_removes_the_obsolete_full_video_prompt_path(self) -> None:
        self.assertNotIn("影片版組裝順序", self.motion)
        self.assertNotIn("完整範例：一段 20 秒的分鏡", self.motion)
        self.assertNotRegex(self.motion, r"(?is)改用以下十四槽")
        self.assertIn("## Visual-look subcontract export", self.motion)
        self.assertRegex(
            self.motion,
            r"(?is)opening look.*visible change.*end look.*camera.*lighting.*color.*texture.*hand.*seedance-prompt-director",
        )

    def test_ui_only_advertises_visual_direction(self) -> None:
        self.assertRegex(self.metadata, r'(?im)^  short_description: "Visual direction for image and video looks"$')
        self.assertRegex(
            self.metadata,
            r"(?is)default_prompt:.*visual.look.*(?:not|rather than).*full.*(?:shot|clip).*prompt",
        )

    def test_visual_subcontracts_do_not_default_delivery_parameters(self) -> None:
        self.assertNotIn("畫幅是必填的", self.skill)
        self.assertNotIn("2.39:1` 是最便宜的電影感來源", self.skill)
        self.assertRegex(
            self.skill,
            r"(?is)do not default.*(?:aspect|ratio).*duration.*resolution.*format",
        )
        self.assertRegex(
            self.skill,
            r"(?is)visual-look subcontract.*omit.*(?:aspect|ratio).*unless.*(?:user|selected surface|runtime).*confirmed",
        )

    def test_unknown_image_provider_stays_provider_neutral(self) -> None:
        self.assertRegex(
            self.skill,
            r"(?is)target (?:model|provider).*unknown.*provider-neutral.*do not name.*compatible models.*negative.prompt field",
        )
        self.assertRegex(
            self.skill,
            r"(?is)unknown.*complete reply.*do not mention.*model names.*compatibility.*negative.prompt fields.*conversion",
        )
        self.assertRegex(
            self.dialects,
            r"(?is)target (?:model|provider).*unknown.*provider-neutral.*do not (?:name|list).*models.*negative.prompt field",
        )
        self.assertNotIn(
            "相容性最高，可直接用於 GPT Image 2、Nano Banana、Flux、Seedream",
            self.dialects,
        )

    def test_visual_look_exclusions_override_subject_motion_defaults(self) -> None:
        self.assertRegex(
            self.skill,
            r"(?is)explicitly excludes.*blocking.*timeline.*visible change.*(?:environmental|optical).*do not invent.*subject.*(?:action|position)",
        )
        self.assertRegex(
            self.skill,
            r"(?is)scoped visual-look subcontract.*do not invent.*(?:exposure|distance).*timing.*light ratio",
        )
        self.assertRegex(
            self.skill,
            r"(?is)exact numeric values.*explicitly provided.*preserve.*do not add.*numeric.*motion amplitude",
        )
        self.assertNotIn("about one percent of the frame width", self.motion)
        self.assertNotIn("warm tungsten table lamp at 2900K", self.lighting)
        for reference in (self.motion, self.lighting):
            self.assertRegex(
                reference,
                r"(?is)scoped visual-look subcontract.*numeric.*only.*user.*provided",
            )


if __name__ == "__main__":
    unittest.main()
