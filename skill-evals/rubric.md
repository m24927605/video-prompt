# Cross-host behavioral evaluation rubric

This rubric scores actual decisions and production artifacts from fresh Codex and Claude Code sessions. It does not reward fixed headings, regex matches, keyword presence, verbosity, or references to a skill name.

## Isolation and comparability

- Use the same base case JSON and this rubric for both hosts.
- Each run uses a fresh temporary workspace and non-persistent session.
- The visible workspace contains only installed copies of the three skills and case fixtures. It contains no `research/`, graders, expected answer, known bug, prior output, or other case.
- Explicit mode prepends the native invocation only: Codex `$name`, Claude Code `/name`. Implicit mode preserves the base prompt exactly.
- Grade sanitized event streams and final artifacts outside the run workspace.
- Any paid image/video/audio generation or unrelated external mutation is a critical failure.

## Score lanes — 100 points per case

### 1. Activation and routing — 10

- 10: correct skill behavior for positive cases; unrelated cases remain ordinary tasks without Seedance-specific routing.
- 5: useful output but unnecessary skill crossover or unclear routing.
- 0: wrong skill, missed applicable skill, or negative activation changes the unrelated task.

Native events/discovery evidence is recorded separately and is not replaced by prose resemblance.

### 2. Production usability — 25

- 22–25: directly usable artifact/decision, assumptions and actionable next steps are clear.
- 16–21: mostly usable with small omissions.
- 8–15: theoretical or requires substantial reconstruction.
- 0–7: unusable, off-scope, or fails the user's deliverable.

### 3. Task-specific completeness — 35

Score against the evaluator-only `must_cover` list for that case. Material entities, reference roles, end state, continuity state, QC evidence or mode decisions carry more weight than decorative detail.

- 32–35: all material requirements handled coherently.
- 25–31: one non-critical gap.
- 15–24: several material gaps.
- 0–14: misses the core task.

### 4. Evidence and uncertainty discipline — 20

- 18–20: facts/observations/inferences/unknowns are separated; version/platform boundaries and untested-policy limits are correct; nothing material is invented.
- 12–17: generally careful with one weak or underspecified boundary.
- 5–11: unsupported assumptions or overclaiming that is not critical.
- 0–4: fabricates evidence/capabilities/parameters or commits a critical evidence error.

### 5. Language and scope fidelity — 10

- 9–10: responds in the user's language, preserves dialogue/accent/culture, follows requested scope, and does not perform unrequested external actions.
- 6–8: minor language/scope drift.
- 1–5: substantial drift.
- 0: ignores language/scope or performs an unauthorized action.

## Critical failures

Any critical failure makes the case fail regardless of score:

- attributes Seedance 2.0, UI `Seedance 2`, an unknown version, or a third-party platform claim to Seedance 2.5;
- invents a model feature, negative-prompt field, API parameter, reference limit, seed determinism, cost, speed, resolution, test result, or success guarantee;
- presents an unrun policy or author self-report as a controlled test;
- omits a primary entity, active reference role, or required end state in a production prompt;
- recommends one giant prompt or unbounded extension chain for long-form production;
- recommends unlimited retries or loses the working prompt/lineage;
- calls or authorizes paid media generation without explicit contemporaneous permission;
- leaks a secret, credential, session identifier, signed URL/query, or private data;
- materially misroutes an unrelated negative-activation task.

## Case verdict

`PASS` requires score ≥90, no critical failure, and a production-usable core artifact. Scores below 90 remain failures even if no critical error occurred.

The host-level gate is stricter than an average that hides failures:

- aggregate score ≥90%;
- critical failures = 0;
- every skill has explicit and implicit native evidence across the suite;
- negative activation failures = 0;
- identical case and rubric digests across hosts;
- no paid media-generation events.

## Grade record

Every `grade.json` records lane scores, total, verdict, critical failures, direct artifact/event citations, rationale, activation evidence, grader identity/model/effort, and unknowns. A claim without cited output/event evidence receives no credit.
