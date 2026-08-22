from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "skill-evals" / "scripts" / "collect_direct_eval.py"
SPEC = importlib.util.spec_from_file_location("collect_direct_eval", MODULE_PATH)
assert SPEC and SPEC.loader
COLLECTOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(COLLECTOR)


class DirectCollectorTests(unittest.TestCase):
    def test_persists_sanitized_complete_claude_evidence(self) -> None:
        stream = "\n".join([
            json.dumps({
                "type": "system",
                "subtype": "init",
                "session_id": "11111111-1111-1111-1111-111111111111",
                "cwd": "/private/tmp/case",
                "memory_paths": {"auto": "/Users/private/session"},
                "slash_commands": [
                    "seedance-film-producer",
                    "seedance-prompt-director",
                    "seedance-video-qc",
                ],
                "skills": [
                    "seedance-film-producer",
                    "seedance-prompt-director",
                    "seedance-video-qc",
                ],
                "model": "claude-fable-5",
            }),
            json.dumps({
                "type": "assistant",
                "message": {"content": [{"type": "text", "text": "Production answer"}]},
            }),
            json.dumps({
                "type": "result",
                "is_error": False,
                "result": "Production answer",
                "session_id": "22222222-2222-2222-2222-222222222222",
                "modelUsage": {
                    "claude-fable-5": {
                        "canonicalModel": "claude-fable-5",
                        "provider": "firstParty",
                    }
                },
            }),
        ])

        with tempfile.TemporaryDirectory() as workspace_temp, tempfile.TemporaryDirectory() as output_temp:
            workspace = Path(workspace_temp)
            inventory = COLLECTOR.RUNNER.stage_workspace(ROOT, workspace, "claude-code")
            result = COLLECTOR.persist_direct_claude_eval(
                repo_root=ROOT,
                output_root=Path(output_temp),
                workspace=workspace,
                case_id="ambiguous-single-shot",
                stdout=stream,
                elapsed_seconds=12.5,
            )

            case_root = Path(output_temp) / "ambiguous-single-shot"
            events = (case_root / "events.jsonl").read_text(encoding="utf-8")
            run = json.loads((case_root / "run.json").read_text(encoding="utf-8"))

            self.assertTrue(result["success"])
            self.assertNotIn("session_id", events)
            self.assertNotIn("11111111-1111", events)
            self.assertNotIn('"cwd"', events)
            self.assertNotIn("memory_paths", events)
            self.assertEqual((case_root / "final.md").read_text(encoding="utf-8"), "Production answer\n")
            self.assertEqual(run["model_evidence"]["actual_primary_model"], "claude-fable-5")
            self.assertEqual(run["workspace_digest"], inventory["digest"])
            self.assertTrue((case_root / "native-evidence.md").is_file())


if __name__ == "__main__":
    unittest.main()
