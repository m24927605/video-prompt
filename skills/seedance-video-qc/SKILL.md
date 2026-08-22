---
name: seedance-video-qc
description: Inspect generated Seedance and AI-video evidence, compare variants, diagnose failures, and choose the next action. Use with videos, screenshots, timestamps, audio evidence, prompt adherence, continuity, physics, acting, camera, text, or edit usability; do not use for initial prompt drafting, whole-film planning, or unrelated live-action critique.
---

# Seedance Video QC

Audit what the evidence actually supports, diagnose the most likely upstream cause, and recommend the smallest useful next action.

## Route the request

- Use this skill when the user supplies or describes generated video, frames, timecodes, variants, an original prompt, or a failed result.
- Use `seedance-prompt-director` for initial prompt drafting or when the user explicitly wants the repaired final prompt after diagnosis.
- Use `seedance-film-producer` for multi-shot production architecture rather than a particular media failure.
- Do not use this as generic film criticism without generated-media adherence or technical QC goals.

## Shared operating invariants

1. Reply in the user's language; preserve the language, accent, and wording of any dialogue under review.
2. Establish evidence modality before judging: full video and audio, screenshots, transcript, waveform/ASR, prompt, reference files, or user-reported symptoms. Ask for opening, middle, end, transitions, and high-risk action timecodes when absent. [QC-01]
3. Label every conclusion as **direct observation**, **inference**, or **unknown**. Screenshots cannot prove continuous motion; an unmuted icon cannot prove audio quality, dialogue accuracy, voice naturalness, or lip-sync. [QC-02] [QC-12]
4. Gate by actual platform/model/version and archive date. Keep Seedance 2.0, UI `Seedance 2`, Seedance 2.5, and platform capabilities separate. For current claims, check current official sources; archived knowledge date is 2026-08-22.
5. Never invent hidden parameters, negative-prompt fields, seed determinism, costs, limits, causes, or guarantees. Root causes are hypotheses unless directly demonstrated.
6. Do not call paid media generation. A recommendation to regenerate is a route decision, not authorization to execute it.
7. Preserve the working prompt. Change one necessary variable per iteration and state the invariants. Stop at a project-specific retry/cost/time ceiling. [QC-14] [QC-16]

## Workflow

1. Reconstruct the contract: required and forbidden entities, reference roles, action order, start/end state, camera, audio, text, and delivery needs.
2. Apply hard gates before scores. A critical identity/entity/story/delivery/rights or uneditable structural failure cannot be averaged away by attractive images. [QC-03]
3. Inspect fidelity before cross-shot consistency: first verify the correct character/object/location, then judge whether it stays consistent. A consistently wrong identity is still a failure. [QC-04]
4. Evaluate prompt adherence; identity, wardrobe, injury, prop, and location continuity; temporal stability; anatomy/artifacts; physics/contact/inertia; blocking/screen direction; camera/optics; observable acting; text/subtitles; audio/dialogue/lip-sync; and edit usability. [QC-05] [QC-06]
5. Record timecoded evidence and sampling limits. Inspect fast hands, short text, cuts, and lip movement densely enough for the claim; automated metrics are diagnostic only. [QC-07]
6. Diagnose in upstream order: task/parameters → reference conflict → entity/state → space/camera → physics → acting → audio/text → neighbor cut. [QC-13]
7. Choose one route: `accept`, `edit/repair`, `regenerate`, `VFX/composite`, or `redesign/split`. Do not answer with an unlimited synonym-rewrite loop. [QC-15]

Read [references/inspection-rubric.md](references/inspection-rubric.md) for evidence coverage, hard gates, scoring, and the report schema. Read [references/root-cause-actions.md](references/root-cause-actions.md) for diagnosis, minimal changes, routes, and stopping conditions. Read [references/variant-comparison.md](references/variant-comparison.md) when ranking variants or comparing workflows. Read [references/provenance.md](references/provenance.md) only for evidence audits or non-obvious claim verification.

## Required output

1. **Verdict** — pass/fail/conditional, scope of evidence, and blocking severity.
2. **Findings** — dimension, severity, exact timecode/frame, direct observation, inference, unknown, and acceptance impact.
3. **Root-cause hypotheses** — ranked, with evidence for and against each.
4. **Minimal next action** — one changed variable, fixed invariants, expected diagnostic signal, and route (`accept/edit/repair/regenerate/VFX/redesign`).
5. **Stop condition** — retry/cost/time ceiling or repeated-defect/oscillation condition.
6. **Missing evidence** — only what is needed to resolve material unknowns.

If the user requests a revised prompt, diagnose first, then hand the specific minimal change to the prompt-director workflow.
