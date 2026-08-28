"""Structural acceptance tests for the cross-host Seedance skill suite.

Behavioral quality is intentionally evaluated by real Codex and Claude Code
sessions.  These tests cover deterministic packaging invariants only.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SEEDANCE_SKILL_NAMES = (
    "seedance-prompt-director",
    "seedance-film-producer",
    "seedance-video-qc",
)
PACKAGED_SKILL_NAMES = (
    *SEEDANCE_SKILL_NAMES,
    "photography-aesthetics",
    "screenplay-writer",
)
PHOTOGRAPHY_TEXT_REFERENCE_FILES = {
    "01-lighting.md",
    "02-tone-color.md",
    "03-framing.md",
    "04-film-styles.md",
    "05-recipes.md",
    "06-analysis.md",
    "07-beyond-the-charts.md",
    "08-motion.md",
    "09-model-dialects.md",
    "10-zh-lexicon.md",
    "11-image-input.md",
}
SCREENPLAY_REFERENCE_FILES = {
    "continuity.md",
    "development.md",
    "dialogue-and-voice.md",
    "formatting.md",
    "provenance.md",
    "rewrite-and-qc.md",
    "scene-writing.md",
    "style-variation.md",
}
REQUIRED_DOCS = (
    "SKILLS.md",
    "SKILLS_SOURCE_MAP.md",
    "SKILLS_QA.md",
    "SKILLS_PROGRESS.md",
    "skills-manifest.json",
    "skill-evals/rubric.md",
)
REQUIRED_CASE_IDS = {
    "ambiguous-single-shot",
    "multi-character-reference-mapping",
    "cantonese-dialogue-audio",
    "fight-physics-contact",
    "cross-shot-state-continuity",
    "long-form-10-to-90-minutes",
    "quality-speed-tradeoff",
    "failed-video-root-cause",
    "version-misattribution-trap",
    "fabricated-parameter-trap",
    "negative-activation",
    "qc-variant-comparison",
    "negative-image-design",
    "negative-live-action-critique",
}
REQUIRED_SCRIPTS = (
    "skill-evals/scripts/run_host_eval.py",
    "skill-evals/scripts/aggregate_scores.py",
    "skill-evals/scripts/build_manifest.py",
    "skill-evals/scripts/scan_signed_queries.py",
    "skill-evals/scripts/collect_direct_eval.py",
    "skill-evals/scripts/resanitize_results.py",
)
SHARED_CORE_FORBIDDEN = (
    "$ARGUMENTS",
    "${CLAUDE_SKILL_DIR}",
    "allowed-tools:",
    "disable-model-invocation:",
    "context: fork",
)


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise AssertionError(f"missing YAML frontmatter: {path}")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise AssertionError(f"unterminated YAML frontmatter: {path}") from exc

    values: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"([a-zA-Z0-9_-]+):\s*(.+)", line)
        if not match:
            raise AssertionError(f"shared frontmatter must be flat: {path}: {line}")
        key, raw_value = match.groups()
        values[key] = raw_value.strip().strip('"\'')
    return values


def local_markdown_links(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    links = re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text)
    return [
        link.split("#", 1)[0]
        for link in links
        if link and not link.startswith(("http://", "https://", "#", "mailto:"))
    ]


class SkillSuiteStructureTests(unittest.TestCase):
    def test_required_delivery_files_exist(self) -> None:
        for relative in REQUIRED_DOCS:
            self.assertTrue((ROOT / relative).is_file(), relative)
        for relative in REQUIRED_SCRIPTS:
            self.assertTrue((ROOT / relative).is_file(), relative)
        self.assertFalse(
            (ROOT / "skill-evals" / "scripts" / "record_direct_eval.py").exists(),
            "obsolete unsanitized recorder must not be distributed",
        )

        for host in ("codex", "claude-code"):
            result_dir = ROOT / "skill-evals" / "results" / host
            self.assertTrue(result_dir.is_dir(), result_dir)
            self.assertTrue(any(result_dir.iterdir()), f"empty results: {result_dir}")

    def test_packaged_skills_have_minimal_shared_frontmatter(self) -> None:
        for name in PACKAGED_SKILL_NAMES:
            skill_md = ROOT / "skills" / name / "SKILL.md"
            self.assertTrue(skill_md.is_file(), skill_md)
            frontmatter = parse_frontmatter(skill_md)
            self.assertEqual({"name", "description"}, set(frontmatter), skill_md)
            self.assertEqual(name, frontmatter["name"], skill_md)
            self.assertGreaterEqual(len(frontmatter["description"]), 40, skill_md)

            text = skill_md.read_text(encoding="utf-8")
            self.assertLessEqual(len(text.splitlines()), 500, skill_md)
            for forbidden in SHARED_CORE_FORBIDDEN:
                self.assertNotIn(forbidden, text, f"{skill_md}: {forbidden}")

    def test_host_entries_are_relative_symlinks_to_canonical_skills(self) -> None:
        for host_root in (ROOT / ".agents" / "skills", ROOT / ".claude" / "skills"):
            for name in PACKAGED_SKILL_NAMES:
                entry = host_root / name
                self.assertTrue(entry.is_symlink(), entry)
                target = Path(os.readlink(entry))
                self.assertFalse(target.is_absolute(), f"absolute symlink: {entry}")
                self.assertEqual((ROOT / "skills" / name).resolve(), entry.resolve())

        self.assertFalse((ROOT / ".claude" / "commands").exists())

    def test_openai_metadata_is_consistent_and_allows_implicit_invocation(self) -> None:
        for name in PACKAGED_SKILL_NAMES:
            path = ROOT / "skills" / name / "agents" / "openai.yaml"
            self.assertTrue(path.is_file(), path)
            text = path.read_text(encoding="utf-8")
            self.assertIn("interface:", text, path)
            self.assertIn("default_prompt:", text, path)
            self.assertIn(f"${name}", text, path)
            self.assertIn("allow_implicit_invocation: true", text, path)

    def test_photography_aesthetics_packages_the_complete_text_reference_library(self) -> None:
        reference_root = ROOT / "skills" / "photography-aesthetics" / "references"
        self.assertTrue(reference_root.is_dir(), reference_root)
        actual = {path.name for path in reference_root.iterdir() if path.is_file()}
        self.assertEqual(PHOTOGRAPHY_TEXT_REFERENCE_FILES, actual)

    def test_screenplay_writer_packages_the_complete_reference_library(self) -> None:
        reference_root = ROOT / "skills" / "screenplay-writer" / "references"
        self.assertTrue(reference_root.is_dir(), reference_root)
        actual = {path.name for path in reference_root.iterdir() if path.is_file()}
        self.assertEqual(SCREENPLAY_REFERENCE_FILES, actual)

    def test_all_local_skill_links_resolve(self) -> None:
        skill_files = sorted((ROOT / "skills").glob("**/*.md"))
        self.assertGreater(len(skill_files), 3)
        for path in skill_files:
            for link in local_markdown_links(path):
                resolved = (path.parent / link).resolve()
                self.assertTrue(resolved.exists(), f"{path}: {link}")
                relative = path.relative_to(ROOT / "skills")
                skill_root = ROOT / "skills" / relative.parts[0]
                self.assertTrue(resolved.is_relative_to(skill_root), f"escaping link: {path}: {link}")

    def test_top_level_document_links_resolve(self) -> None:
        for relative in ("SKILLS.md", "SKILLS_SOURCE_MAP.md", "SKILLS_QA.md", "SKILLS_PROGRESS.md", "skill-evals/rubric.md"):
            path = ROOT / relative
            if not path.is_file():
                continue
            for link in local_markdown_links(path):
                self.assertTrue((path.parent / link).resolve().exists(), f"{path}: {link}")

    def test_public_research_links_do_not_target_excluded_archives(self) -> None:
        result = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        public_paths = set(result.stdout.splitlines())
        for path in sorted((ROOT / "research" / "seedance-2.5").glob("*.md")):
            for link in local_markdown_links(path):
                resolved = (path.parent / link).resolve()
                if not resolved.exists():
                    self.fail(f"{path}: missing local target {link}")
                relative = resolved.relative_to(ROOT).as_posix()
                self.assertIn(relative, public_paths, f"{path}: excluded archive link {link}")

    def test_provenance_rule_ids_have_complete_operational_coverage(self) -> None:
        for name, prefix, count in (
            ("seedance-prompt-director", "PD", 17),
            ("seedance-film-producer", "FP", 18),
            ("seedance-video-qc", "QC", 18),
        ):
            skill_root = ROOT / "skills" / name
            provenance = skill_root / "references" / "provenance.md"
            self.assertTrue(provenance.is_file(), provenance)
            provenance_ids = set(re.findall(rf"\| ({prefix}-\d{{2}}) \|", provenance.read_text(encoding="utf-8")))
            expected = {f"{prefix}-{index:02d}" for index in range(1, count + 1)}
            self.assertEqual(expected, provenance_ids, provenance)

            operational_text = "\n".join(
                path.read_text(encoding="utf-8")
                for path in sorted(skill_root.glob("**/*.md"))
                if path != provenance
            )
            operational_ids = set(re.findall(rf"\b{prefix}-\d{{2}}\b", operational_text))
            self.assertEqual(expected, operational_ids, f"orphan/missing {prefix} rule IDs")

    def test_held_out_cases_cover_every_required_category(self) -> None:
        case_dir = ROOT / "skill-evals" / "cases"
        cases = []
        for path in sorted(case_dir.glob("*.json")):
            cases.append(json.loads(path.read_text(encoding="utf-8")))
        ids = {case["id"] for case in cases}
        self.assertTrue(REQUIRED_CASE_IDS.issubset(ids), REQUIRED_CASE_IDS - ids)
        self.assertEqual(len(ids), len(cases), "duplicate case id")
        for case in cases:
            self.assertIsInstance(case.get("prompt"), str)
            self.assertGreater(len(case["prompt"].strip()), 20)
            self.assertNotIn("expected answer", case["prompt"].lower())
            self.assertNotIn("research/seedance-2.5", case["prompt"])

    def test_host_behavioral_summaries_pass_required_gates(self) -> None:
        for host in ("codex", "claude-code"):
            path = ROOT / "skill-evals" / "results" / host / "summary.json"
            self.assertTrue(path.is_file(), path)
            summary = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual("PASS", summary["status"], path)
            self.assertGreaterEqual(summary["score_percent"], 90.0, path)
            self.assertEqual([], summary["critical_failures"], path)
            self.assertEqual([], summary["negative_activation_failures"], path)
            self.assertEqual([], summary["run_failures"], path)
            self.assertEqual([], summary["digest_failures"], path)
            self.assertEqual([], summary["paid_media_tool_event_cases"], path)
            self.assertEqual([], summary["verdict_failures"], path)
            self.assertEqual([], summary["grade_validation_failures"], path)
            self.assertEqual(set(SEEDANCE_SKILL_NAMES), set(summary["explicit_skill_coverage"]), path)
            self.assertEqual(set(SEEDANCE_SKILL_NAMES), set(summary["implicit_skill_coverage"]), path)

    def test_manifest_hashes_regular_files_and_records_symlinks(self) -> None:
        manifest_path = ROOT / "skills-manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        entries = manifest["entries"]
        self.assertEqual(len(entries), len({entry["path"] for entry in entries}))

        by_path = {entry["path"]: entry for entry in entries}
        public_artifacts = {
            ".gitignore",
            "CHANGELOG.md",
            "README.md",
            "SEEDANCE_CROSS_AGENT_SKILLS_GOAL.md",
            "VERSION",
            "research/seedance-2.5/research-report.md",
            "research/seedance-2.5/source-manifest.json",
        }
        self.assertTrue(public_artifacts.issubset(by_path), public_artifacts - set(by_path))
        for skill_file in sorted((ROOT / "skills").glob("**/*")):
            if not skill_file.is_file():
                continue
            relative = skill_file.relative_to(ROOT).as_posix()
            self.assertIn(relative, by_path)
            digest = hashlib.sha256(skill_file.read_bytes()).hexdigest()
            self.assertEqual(digest, by_path[relative].get("sha256"), relative)

        for host in (".agents", ".claude"):
            for name in PACKAGED_SKILL_NAMES:
                relative = f"{host}/skills/{name}"
                self.assertEqual("symlink", by_path[relative]["type"])
                self.assertEqual(os.readlink(ROOT / relative), by_path[relative]["target"])

    def test_repository_ignores_local_secrets_and_host_state(self) -> None:
        candidates = (
            ".env",
            ".env.production",
            "private.pem",
            "credentials.json",
            ".claude/settings.local.json",
            ".agents/settings.local.json",
        )
        result = subprocess.run(
            ["git", "check-ignore", "--no-index", *candidates],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(set(candidates), set(result.stdout.splitlines()))

    def test_readme_documents_windows_symlink_requirement(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        self.assertIn("windows", readme)
        self.assertIn("symlink", readme)


if __name__ == "__main__":
    unittest.main()
