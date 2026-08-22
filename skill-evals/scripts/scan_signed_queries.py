#!/usr/bin/env python3
"""Scan delivered text artifacts for high-confidence secrets and signed queries."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
from sensitive_urls import SIGNED_QUERY_DETECTION_RE  # noqa: E402


PATTERNS = {
    "openai_key": re.compile(r"(?<![A-Za-z0-9])" + "sk" + r"-[A-Za-z0-9_-]{20,}"),
    "aws_access_key": re.compile("AK" + r"IA[0-9A-Z]{16}"),
    "private_key": re.compile("-----BEGIN " + r"(?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "jwt": re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b"),
    "signed_query": SIGNED_QUERY_DETECTION_RE,
}


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _git_paths(root: Path, *arguments: str) -> list[str]:
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", *arguments, "-z"],
        check=True,
        capture_output=True,
    )
    return [
        item.decode("utf-8", errors="surrogateescape")
        for item in result.stdout.split(b"\0")
        if item
    ]


def public_artifact_contents(root: Path) -> list[tuple[str, bytes]]:
    indexed = _git_paths(root, "--cached")
    untracked = _git_paths(root, "--others", "--exclude-standard")
    artifacts: list[tuple[str, bytes]] = []
    for relative in indexed:
        result = subprocess.run(
            ["git", "-C", str(root), "show", f":{relative}"],
            check=True,
            capture_output=True,
        )
        artifacts.append((relative, result.stdout))
    for relative in untracked:
        path = root / relative
        if path.is_file() and not path.is_symlink():
            artifacts.append((relative, path.read_bytes()))
    return sorted(artifacts, key=lambda item: item[0])


def scan_public_artifacts(root: Path) -> dict[str, Any]:
    root = root.resolve()
    findings = []
    scanned = 0
    for relative, content in public_artifact_contents(root):
        try:
            text = content.decode("utf-8")
        except UnicodeDecodeError:
            continue
        scanned += 1
        for name, pattern in PATTERNS.items():
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                findings.append({
                    "type": name,
                    "path": relative,
                    "line": line,
                    "value": "<REDACTED>",
                })
    return {
        "status": "PASS" if not findings else "FAIL",
        "scanned_files": scanned,
        "findings": findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.repo_root.resolve()
    result = scan_public_artifacts(root)
    output = args.output or root / "skill-evals" / "results" / "validation" / "secret-scan.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    write_json(output, result)
    print(
        f"{result['status']}: scanned {result['scanned_files']} files, "
        f"findings={len(result['findings'])}"
    )
    return 0 if not result["findings"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
