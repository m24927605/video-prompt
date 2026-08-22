from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "skill-evals" / "scripts" / "scan_signed_queries.py"
SPEC = importlib.util.spec_from_file_location("scan_signed_queries", MODULE_PATH)
assert SPEC and SPEC.loader
SCANNER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SCANNER)


class PublicArtifactScanTests(unittest.TestCase):
    def init_repo(self, root: Path) -> None:
        subprocess.run(
            ["git", "init", "-b", "main"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )

    def test_scans_staged_research_and_root_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.init_repo(root)
            (root / "README.md").write_text("safe\n", encoding="utf-8")
            manifest = root / "research" / "seedance-2.5" / "source-manifest.json"
            manifest.parent.mkdir(parents=True)
            manifest.write_text(
                'https://example.test/file?x-amz-' + 'signature=private-value\n',
                encoding="utf-8",
            )
            subprocess.run(
                ["git", "add", "README.md", "research/seedance-2.5/source-manifest.json"],
                cwd=root,
                check=True,
            )

            result = SCANNER.scan_public_artifacts(root)

            self.assertEqual("FAIL", result["status"])
            self.assertEqual(
                ["research/seedance-2.5/source-manifest.json"],
                sorted({item["path"] for item in result["findings"]}),
            )

    def test_scans_staged_blob_instead_of_safe_worktree_copy(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.init_repo(root)
            report = root / "README.md"
            report.write_text("sk-" + "x" * 24 + "\n", encoding="utf-8")
            subprocess.run(["git", "add", "README.md"], cwd=root, check=True)
            report.write_text("safe working tree copy\n", encoding="utf-8")

            result = SCANNER.scan_public_artifacts(root)

            self.assertEqual("FAIL", result["status"])
            self.assertEqual(["README.md"], [item["path"] for item in result["findings"]])

    def test_scans_google_signed_query_components(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.init_repo(root)
            report = root / "research.json"
            report.write_text(
                "https://example.test/file?x-goog-" + "credential=private-value\n",
                encoding="utf-8",
            )
            subprocess.run(["git", "add", "research.json"], cwd=root, check=True)

            result = SCANNER.scan_public_artifacts(root)

            self.assertEqual("FAIL", result["status"])
            self.assertEqual("signed_query", result["findings"][0]["type"])

    def test_does_not_scan_ignored_private_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.init_repo(root)
            (root / ".gitignore").write_text("private/\n", encoding="utf-8")
            private = root / "private" / "credentials.txt"
            private.parent.mkdir()
            private.write_text("sk-" + "x" * 24, encoding="utf-8")
            (root / "README.md").write_text("safe\n", encoding="utf-8")
            subprocess.run(
                ["git", "add", ".gitignore", "README.md"],
                cwd=root,
                check=True,
            )

            result = SCANNER.scan_public_artifacts(root)

            self.assertEqual("PASS", result["status"])
            self.assertEqual([], result["findings"])

    def test_cli_writes_scan_result(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.init_repo(root)
            (root / "README.md").write_text("safe\n", encoding="utf-8")
            subprocess.run(["git", "add", "README.md"], cwd=root, check=True)
            output = root / "scan-result.json"

            result = subprocess.run(
                [
                    sys.executable,
                    str(MODULE_PATH),
                    "--repo-root",
                    str(root),
                    "--output",
                    str(output),
                ],
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(0, result.returncode, result.stderr)
            self.assertIn("PASS: scanned 1 files, findings=0", result.stdout)
            self.assertTrue(output.is_file())

    def test_highrisk_filename_is_not_an_openai_key(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.init_repo(root)
            report = root / "research.md"
            report.write_text(
                "browser-evidence/p06-v01-highrisk-t8506-computer-use-2026-08-22.png\n",
                encoding="utf-8",
            )
            subprocess.run(["git", "add", "research.md"], cwd=root, check=True)

            result = SCANNER.scan_public_artifacts(root)

            self.assertEqual("PASS", result["status"])
            self.assertEqual([], result["findings"])


if __name__ == "__main__":
    unittest.main()
