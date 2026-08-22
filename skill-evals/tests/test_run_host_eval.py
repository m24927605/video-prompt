from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "skill-evals" / "scripts" / "run_host_eval.py"
SPEC = importlib.util.spec_from_file_location("run_host_eval", MODULE_PATH)
assert SPEC and SPEC.loader
RUNNER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RUNNER)


class ClaudeModelEvidenceTests(unittest.TestCase):
    def test_sanitizer_removes_session_derived_paths(self) -> None:
        sanitized = RUNNER.sanitize({
            "type": "system",
            "cwd": "/private/tmp/seedance-claude-case-abc",
            "memory_paths": {"auto": "/Users/private/.claude/projects/session/memory"},
            "skills": ["seedance-prompt-director"],
        })

        self.assertNotIn("cwd", sanitized)
        self.assertNotIn("memory_paths", sanitized)
        self.assertEqual(sanitized["skills"], ["seedance-prompt-director"])

    def test_sanitizer_redacts_home_paths_inside_assistant_text(self) -> None:
        home = str(Path.home())
        sanitized = RUNNER.sanitize({
            "text": f"Draft path: {home}/.claude/plans/private.md"
        })

        self.assertEqual(
            sanitized["text"],
            "Draft path: <REDACTED_PRIVATE_PATH>",
        )

    def test_sanitizer_redacts_ephemeral_workspace_paths_inside_events(self) -> None:
        sanitized = RUNNER.sanitize({
            "text": "Base: /private/tmp/seedance-claude-case.a1b2/.claude/skills/demo"
        })

        self.assertEqual(
            sanitized["text"],
            "Base: <REDACTED_WORKSPACE>/.claude/skills/demo",
        )

    def test_sanitizer_removes_message_and_tool_session_identifiers(self) -> None:
        sanitized = RUNNER.sanitize({
            "message": {"id": "msg_private"},
            "content": [{"id": "toolu_private", "tool_use_id": "toolu_private"}],
            "sender_thread_id": "thread_private",
        })

        self.assertEqual(sanitized, {"message": {}, "content": [{}]})

    def test_sanitizer_redacts_private_claude_plan_and_project_paths(self) -> None:
        home = str(Path.home())
        for raw in (
            f"{home}/.claude/plans/random-plan-slug.md",
            f"{home}/.claude/projects/-private-tmp-seedance-case-random/memory",
            "~/.claude/plans/random-plan-slug.md",
        ):
            with self.subTest(raw=raw):
                self.assertEqual(RUNNER.sanitize_string(raw), "<REDACTED_PRIVATE_PATH>")

    def test_sanitizer_redacts_complete_signed_url_components(self) -> None:
        url = (
            "https://example.test/file?"
            + "X-Goog-" + "Credential=private-google"
            + "&X-Goog-" + "Expires=3600"
            + "&X-Goog-" + "Signature=private-google-signature"
            + "&X-Amz-" + "Credential=private-aws"
            + "&X-Amz-" + "Security-Token=private-aws-token"
            + "&Key-Pair-" + "Id=private-cloudfront-id"
            + "&" + "Policy=private-cloudfront-policy"
            + "&" + "Signature=private-cloudfront-signature"
        )

        sanitized = RUNNER.sanitize_string(url)

        self.assertNotIn("private-", sanitized)
        self.assertNotIn("=3600", sanitized)
        self.assertEqual(8, sanitized.count("=<REDACTED>"))

    def test_extracts_fable_primary_and_keeps_auxiliary_models_separate(self) -> None:
        events = [
            {
                "type": "result",
                "modelUsage": {
                    "claude-haiku-4-5-20251001": {
                        "canonicalModel": "claude-haiku-4-5",
                        "provider": "firstParty",
                    },
                    "claude-fable-5": {
                        "canonicalModel": "claude-fable-5",
                        "provider": "firstParty",
                    },
                },
            }
        ]

        evidence = RUNNER.claude_model_evidence(events, "claude-fable-5")

        self.assertTrue(evidence["requested_model_observed"])
        self.assertEqual(evidence["actual_primary_model"], "claude-fable-5")
        self.assertEqual(evidence["actual_primary_provider"], "firstParty")
        self.assertEqual(
            evidence["auxiliary_models"],
            [
                {
                    "reported_model": "claude-haiku-4-5-20251001",
                    "canonical_model": "claude-haiku-4-5",
                    "provider": "firstParty",
                }
            ],
        )
        self.assertFalse(evidence["fallback_detected"])

    def test_missing_requested_model_is_a_fallback_failure(self) -> None:
        events = [
            {
                "type": "result",
                "modelUsage": {
                    "claude-opus-5": {
                        "canonicalModel": "claude-opus-5",
                        "provider": "firstParty",
                    }
                },
            }
        ]

        evidence = RUNNER.claude_model_evidence(events, "claude-fable-5")

        self.assertFalse(evidence["requested_model_observed"])
        self.assertTrue(evidence["fallback_detected"])
        self.assertIsNone(evidence["actual_primary_model"])

    def test_native_evidence_reports_observed_model_and_provider(self) -> None:
        rendered = RUNNER.render_native_evidence(
            host="claude-code",
            cli_version="2.1.239 (Claude Code)",
            requested_model="claude-fable-5",
            requested_effort="max",
            invocation_mode="implicit",
            expected_skill="seedance-video-qc",
            workspace_digest="abc123",
            activation_evidence=["event[4] assistant"],
            model_evidence={
                "requested_model_observed": True,
                "actual_primary_model": "claude-fable-5",
                "actual_primary_provider": "firstParty",
                "auxiliary_models": [
                    {
                        "reported_model": "claude-haiku-4-5-20251001",
                        "canonical_model": "claude-haiku-4-5",
                        "provider": "firstParty",
                    }
                ],
                "fallback_detected": False,
            },
        )

        self.assertIn("Observed primary model: `claude-fable-5`", rendered)
        self.assertIn("Observed provider: `firstParty`", rendered)
        self.assertIn("Fallback detected: `false`", rendered)
        self.assertIn("claude-haiku-4-5", rendered)

    def test_native_skill_listing_counts_as_discovery_evidence(self) -> None:
        events = [
            {
                "type": "system",
                "subtype": "init",
                "slash_commands": ["seedance-video-qc", "doctor"],
            }
        ]

        evidence = RUNNER.activation_events(events, "seedance-video-qc")

        self.assertEqual(evidence, ["event[0] system/init native skill listing"])


if __name__ == "__main__":
    unittest.main()
