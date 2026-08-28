# video-prompt

Cross-agent skills for photographic aesthetics, cinematic prompting, Seedance production, and generated-video QC in Codex CLI and Claude Code.

## Skills

- `photography-aesthetics` turns visual intent into precise image/video prompt aesthetics and critiques existing photography.
- `seedance-prompt-director` turns shot briefs into controllable, testable video prompts.
- `seedance-film-producer` plans multi-shot continuity, assets, queues, lineage, editing, and finishing.
- `seedance-video-qc` audits generated-video evidence and selects bounded repair, regeneration, VFX, or acceptance routes.

See [SKILLS.md](SKILLS.md) for invocation examples and [SKILLS_QA.md](SKILLS_QA.md) for the archived three-skill Seedance validation record.

## Native project entry points

```text
.agents/skills/<name> -> ../../skills/<name>   # Codex
.claude/skills/<name> -> ../../skills/<name>   # Claude Code
```

Both hosts discover the same canonical content under `skills/`.

On Windows, enable Git symlink support (and the required OS permissions or Developer Mode) before checkout; copying these entries as plain text files breaks native skill discovery.

## Package validation

- Packaged skills: 4, each with native Codex and Claude Code entry points
- Skill quick validation: 4/4 PASS
- Deterministic tests: 36/36 PASS
- SHA-256 public-artifact manifest: 337 entries, check PASS
- Secret and signed-query scans: 0 findings

The archived behavioral evaluation covers the three Seedance skills only:

- Codex behavioral eval: 100.00%
- Claude Code behavioral eval: 98.14%
- Critical failures: 0

Run the deterministic suite:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skill-evals/tests -v
```

## Public-source boundary

This repository includes project-authored research reports, text reference libraries, and sanitized evaluation evidence. Third-party source captures, downloaded media, browser/session evidence, copyrighted PDF/source copies, and temporary extraction files are intentionally excluded from the public repository. Accordingly, `photography-aesthetics` packages its complete text transcription but not the downloaded source charts.

Archived knowledge date: 2026-08-22. Current model capabilities, pricing, limits, and policies must be checked against the relevant platform's official documentation.
