#!/usr/bin/env python3
"""Build or verify a deterministic SHA-256 manifest for the delivered suite."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
from pathlib import Path
from typing import Any


EXCLUSIONS = (
    "skills-manifest.json",
    "skill-evals/results/validation/manifest-check.json",
    "skill-evals/results/validation/secret-scan.json",
    "skill-evals/results/validation/gitleaks-final.json",
    "skill-evals/results/validation/test-suite-final.json",
)


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tree_hash(root: Path) -> str:
    rows = []
    for path in sorted(root.rglob("*")):
        if path.is_file():
            rows.append(f"{path.relative_to(root).as_posix()}\0{file_hash(path)}")
    return hashlib.sha256("\n".join(rows).encode("utf-8")).hexdigest()


def included_paths(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        check=True,
        capture_output=True,
    )
    paths = []
    for item in result.stdout.split(b"\0"):
        if not item:
            continue
        path = root / item.decode("utf-8", errors="surrogateescape")
        relative = path.relative_to(root).as_posix()
        if relative in EXCLUSIONS:
            continue
        if path.is_symlink() or path.is_file():
            paths.append(path)
    return sorted(paths, key=lambda item: item.relative_to(root).as_posix())


def release_state_errors(root: Path) -> list[str]:
    errors: list[str] = []
    unstaged = subprocess.run(
        ["git", "-C", str(root), "diff", "--name-only", "-z"],
        check=True,
        capture_output=True,
    ).stdout
    if unstaged:
        errors.append("index and worktree differ")
    untracked = subprocess.run(
        ["git", "-C", str(root), "ls-files", "--others", "--exclude-standard", "-z"],
        check=True,
        capture_output=True,
    ).stdout
    if untracked:
        errors.append("untracked public artifacts are not staged")
    return errors


def build(root: Path) -> dict[str, Any]:
    entries = []
    for path in included_paths(root):
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            target = os.readlink(path)
            resolved = path.resolve()
            entries.append({
                "path": relative,
                "type": "symlink",
                "target": target,
                "resolved_tree_sha256": tree_hash(resolved),
            })
        else:
            entries.append({
                "path": relative,
                "type": "file",
                "bytes": path.stat().st_size,
                "sha256": file_hash(path),
            })
    return {
        "schema_version": 1,
        "algorithm": "sha256",
        "exclusions": list(EXCLUSIONS),
        "entries": entries,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = args.repo_root.resolve()
    manifest_path = root / "skills-manifest.json"
    current = build(root)
    if args.check:
        state_errors = release_state_errors(root)
        if state_errors:
            print("; ".join(state_errors))
            return 1
        expected = json.loads(manifest_path.read_text(encoding="utf-8"))
        if expected != current:
            print("manifest mismatch")
            return 1
        print(f"manifest valid: {len(current['entries'])} entries")
        return 0
    manifest_path.write_text(json.dumps(current, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"manifest written: {len(current['entries'])} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
