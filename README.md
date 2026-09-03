# video-prompt

Cross-agent skills for screenwriting, photographic aesthetics, cinematic prompting, Seedance production, and generated-video QC in Codex CLI and Claude Code.

## Skills

- `screenplay-writer` develops, drafts, reviews, and rewrites original short- and feature-film screenplays in Fountain.
- `photography-aesthetics` turns visual intent into precise image prompts or scoped video visual-look/motion subcontracts, and critiques existing photography.
- `seedance-prompt-director` owns complete shot/clip prompt contracts, including task routing, references, blocking, camera, acting, physics, audio, end states, and revisions.
- `seedance-film-producer` plans multi-shot continuity, assets, queues, lineage, editing, and finishing.
- `seedance-video-qc` audits generated-video evidence and selects bounded repair, regeneration, VFX, or acceptance routes.

See [SKILLS.md](SKILLS.md) for invocation examples and [SKILLS_QA.md](SKILLS_QA.md) for the archived three-skill Seedance validation record. The current clean-room integration checkpoint is tracked in [the independent integration review](skill-evals/results/reviews/upstream-integration-adversarial-review.md).

## Native project entry points

```text
.agents/skills/<name> -> ../../skills/<name>   # Codex
.claude/skills/<name> -> ../../skills/<name>   # Claude Code
```

Both hosts discover the same canonical content under `skills/`.

On Windows, enable Git symlink support (and the required OS permissions or Developer Mode) before checkout; copying these entries as plain text files breaks native skill discovery.

## Package validation

- Packaged skills: 5, each with native Codex and Claude Code entry points
- Skill quick validation: 5/5 PASS
- Deterministic tests: 37/37 PASS
- SHA-256 public-artifact manifest: 349 entries, check PASS
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

This repository includes project-authored research reports, text reference libraries, and sanitized evaluation evidence. Third-party source captures, downloaded repositories/media, browser/session evidence, copyrighted PDF/source copies, and temporary extraction files are intentionally excluded from the public repository. Accordingly, `photography-aesthetics` packages its complete text transcription but not the downloaded source charts, and `screenplay-writer` packages newly written film-specific guidance plus source provenance rather than upstream repository copies. The Seedance 2.5 Video Director and Seedance 2.0 Skill OS reviews likewise record [2.5 concept-level decisions](research/seedance-2.5/upstream-clean-room-review.md) and a [strict generic-versus-2.0 classification](research/seedance-2.0/upstream-clean-room-review.md) without vendoring either skill, examples, legacy material, code, or provider-derived text.

Seedance archived knowledge date: 2026-08-22. Screenplay methodology audit date: 2026-08-29. Current model capabilities, pricing, limits, and policies must be checked against the relevant platform's official documentation.
