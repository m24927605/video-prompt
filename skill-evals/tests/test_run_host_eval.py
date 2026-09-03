from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest import mock


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
            requested_effort="high",
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

        discovered, activated, evidence = RUNNER.extract_skill_activity(events)

        self.assertEqual(["seedance-video-qc"], discovered)
        self.assertEqual([], activated)
        self.assertEqual([], evidence["seedance-video-qc"])

    def test_only_targeted_skill_or_read_calls_activate_a_skill(self) -> None:
        events = [
            {
                "type": "system",
                "subtype": "init",
                "skills": ["seedance-prompt-director", "seedance-video-qc"],
            },
            {
                "type": "assistant",
                "message": {
                    "content": [{"type": "tool_use", "name": "Glob", "input": {"pattern": "**/SKILL.md"}}]
                },
            },
            {
                "type": "user",
                "message": {
                    "content": [{"type": "tool_result", "content": "skills/seedance-prompt-director/SKILL.md"}]
                },
            },
            {
                "type": "assistant",
                "message": {
                    "content": [{"type": "tool_use", "name": "Skill", "input": {"skill": "seedance-prompt-director"}}]
                },
            },
            {
                "type": "item.completed",
                "item": {
                    "type": "tool_call",
                    "name": "Read",
                    "arguments": {"file_path": ".agents/skills/seedance-video-qc/SKILL.md"},
                },
            },
            {
                "type": "item.completed",
                "item": {
                    "type": "command_execution",
                    "command": "/bin/zsh -lc \"sed -n '1,240p' skills/seedance-film-producer/SKILL.md\"",
                    "status": "completed",
                },
            },
            {
                "type": "item.completed",
                "item": {
                    "type": "command_execution",
                    "command": "/bin/zsh -lc \"ls .agents/skills/photography-aesthetics/\"",
                    "status": "completed",
                },
            },
            {
                "type": "item.completed",
                "item": {
                    "type": "command_execution",
                    "command": "/bin/zsh -lc \"sed -n '1,120p' <REDACTED_HOME>/.codex/skills/photography-aesthetics/SKILL.md\"",
                    "status": "completed",
                },
            },
        ]

        discovered, activated, evidence = RUNNER.extract_skill_activity(events)

        self.assertEqual(
            ["seedance-prompt-director", "seedance-video-qc"],
            discovered,
        )
        self.assertEqual(
            [
                "seedance-prompt-director",
                "seedance-film-producer",
                "seedance-video-qc",
            ],
            activated,
        )
        self.assertEqual(1, len(evidence["seedance-prompt-director"]))
        self.assertEqual(1, len(evidence["seedance-video-qc"]))
        self.assertEqual(["event[5] command_execution"], evidence["seedance-film-producer"])
        self.assertEqual([], evidence["photography-aesthetics"])

    def test_personal_skill_override_disables_agents_and_codex_roots(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            home = Path(temp)
            for relative in (
                ".agents/skills/personal-a/SKILL.md",
                ".codex/skills/personal-b/SKILL.md",
            ):
                path = home / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("---\nname: personal\n---\n", encoding="utf-8")
            with mock.patch.object(RUNNER.Path, "home", return_value=home):
                override, count = RUNNER.personal_skill_override()

        self.assertEqual(2, count)
        self.assertIn(str(home / ".agents/skills/personal-a/SKILL.md"), override)
        self.assertIn(str(home / ".codex/skills/personal-b/SKILL.md"), override)

    def test_final_review_effort_is_high_for_both_hosts(self) -> None:
        codex, _, _ = RUNNER.codex_argv(Path("/tmp/workspace"), "test")
        claude, _, _ = RUNNER.claude_argv("test")

        self.assertIn("model_reasoning_effort=high", codex)
        self.assertNotIn("model_reasoning_effort=ultra", codex)
        self.assertEqual("high", claude[claude.index("--effort") + 1])

    def test_claude_eval_delivers_artifacts_without_plan_mode(self) -> None:
        claude, _, _ = RUNNER.claude_argv("test")

        self.assertEqual(
            "dontAsk",
            claude[claude.index("--permission-mode") + 1],
        )
        self.assertEqual(
            "Skill,Read,Glob,Grep",
            claude[claude.index("--tools") + 1],
        )
        self.assertEqual(
            "Skill,Read,Glob,Grep",
            claude[claude.index("--allowedTools") + 1],
        )

    def test_staged_workspace_contains_all_five_packaged_skills(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            inventory = RUNNER.stage_workspace(ROOT, workspace, "codex")

            self.assertFalse(inventory["research_present"])
            for skill in RUNNER.PACKAGED_SKILLS:
                self.assertTrue((workspace / "skills" / skill / "SKILL.md").is_file())
                self.assertTrue((workspace / ".agents" / "skills" / skill).is_symlink())


if __name__ == "__main__":
    unittest.main()
