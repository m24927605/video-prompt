from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "skill-evals" / "scripts" / "build_manifest.py"


class BuildManifestTests(unittest.TestCase):
    def run_script(self, root: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--repo-root", str(root), *arguments],
            check=False,
            capture_output=True,
            text=True,
        )

    def init_repo(self, root: Path) -> None:
        subprocess.run(
            ["git", "init", "-b", "main"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )

    def test_check_passes_when_index_matches_worktree(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.init_repo(root)
            (root / "README.md").write_text("public release\n", encoding="utf-8")
            subprocess.run(["git", "add", "README.md"], cwd=root, check=True)
            self.assertEqual(0, self.run_script(root).returncode)
            subprocess.run(["git", "add", "skills-manifest.json"], cwd=root, check=True)

            result = self.run_script(root, "--check")

            self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_check_rejects_partial_staging(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.init_repo(root)
            readme = root / "README.md"
            readme.write_text("staged private content\n", encoding="utf-8")
            subprocess.run(["git", "add", "README.md"], cwd=root, check=True)
            readme.write_text("safe working tree content\n", encoding="utf-8")
            self.assertEqual(0, self.run_script(root).returncode)
            subprocess.run(["git", "add", "skills-manifest.json"], cwd=root, check=True)

            result = self.run_script(root, "--check")

            self.assertNotEqual(0, result.returncode)
            self.assertIn("index and worktree differ", result.stdout)


if __name__ == "__main__":
    unittest.main()
