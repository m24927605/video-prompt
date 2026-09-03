from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "skill-evals" / "scripts" / "resanitize_results.py"
SPEC = importlib.util.spec_from_file_location("resanitize_results", MODULE_PATH)
assert SPEC and SPEC.loader
RESANITIZE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RESANITIZE)


class ResanitizeActivityTests(unittest.TestCase):
    def test_rebuilds_activity_metadata_from_persisted_events(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            case_dir = Path(temp) / "case"
            case_dir.mkdir()
            events = [
                {
                    "type": "item.completed",
                    "item": {
                        "type": "command_execution",
                        "command": "sed -n '1,120p' skills/seedance-prompt-director/SKILL.md",
                    },
                },
                {
                    "type": "item.completed",
                    "item": {
                        "type": "agent_message",
                        "text": "answer with spaces  \nnext line  ",
                    },
                },
            ]
            (case_dir / "events.jsonl").write_text(
                "".join(json.dumps(event) + "\n" for event in events),
                encoding="utf-8",
            )
            (case_dir / "final.md").write_text("answer\n", encoding="utf-8")
            (case_dir / "run.json").write_text(
                json.dumps({
                    "packaged_skills": list(RESANITIZE.RUNNER.PACKAGED_SKILLS),
                    "discovered_skills": [],
                    "activated_skills": [],
                    "activation_evidence_by_skill": {
                        skill: [] for skill in RESANITIZE.RUNNER.PACKAGED_SKILLS
                    },
                }),
                encoding="utf-8",
            )
            (case_dir / "request.json").write_text(
                json.dumps({"expected_skill": "seedance-prompt-director"}),
                encoding="utf-8",
            )
            (case_dir / "native-evidence.md").write_text(
                "# Native host evidence\n\n- Activation/discovery evidence: stale\n",
                encoding="utf-8",
            )

            RESANITIZE.resanitize_case(case_dir, "codex")
            run = json.loads((case_dir / "run.json").read_text(encoding="utf-8"))
            final_text = (case_dir / "final.md").read_text(encoding="utf-8")
            native_text = (case_dir / "native-evidence.md").read_text(encoding="utf-8")

        self.assertEqual(["seedance-prompt-director"], run["activated_skills"])
        self.assertEqual(
            ["event[0] command_execution"],
            run["activation_evidence_by_skill"]["seedance-prompt-director"],
        )
        self.assertEqual(list(RESANITIZE.RUNNER.PACKAGED_SKILLS), run["packaged_skills"])
        self.assertEqual(
            "answer with spaces\nnext line\n",
            final_text,
        )
        self.assertNotIn("stale", native_text)
        self.assertIn("Activated packaged skills: `seedance-prompt-director`", native_text)
        self.assertIn("event[0] command_execution", native_text)


if __name__ == "__main__":
    unittest.main()
