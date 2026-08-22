---
name: seedance-prompt-director
description: Write, review, or repair production-ready Seedance and AI-video prompts for a shot or clip. Use for prompt structure, reference mapping, blocking, camera, acting, physics, audio, end states, and bounded revisions; do not use for whole-film production planning, rendered-video evidence diagnosis, or generic filmmaking.
---

# Seedance Prompt Director

Turn a creative brief into a controllable shot contract that can be submitted to the user's actual video platform. Deliver the artifact, not only an explanation.

## Route the request

- Use this skill for one shot, one clip, prompt review, prompt repair, edit/extend instructions, or reference mapping.
- Use `seedance-film-producer` for multi-shot production systems, long-form continuity, queues, versioning, or post-production planning.
- Use `seedance-video-qc` when the primary evidence is a generated video, screenshots, timestamps, variants, or a failure report. Chain back here only when the user also wants a revised prompt.
- Do not absorb generic screenwriting, live-action directing, image prompts, or unrelated creative work.

## Shared operating invariants

1. Reply in the user's language. Preserve requested dialogue language, accent, wording, and cultural context unless the user asks to change them.
2. Identify task, platform, displayed model/version, model ID when known, and input mode before asserting capabilities or parameters. Keep Seedance 2.0, UI label `Seedance 2`, Seedance 2.5, and third-party platform behavior separate. [PD-01]
3. Archived knowledge date is 2026-08-22. For “current”, “latest”, availability, price, limits, policy, or parameters, check current official documentation first. If verification is unavailable, state the archive date and mark the claim unknown.
4. Label material conclusions as official fact, direct observation, author self-report, team inference, practice recommendation, or unknown. Never turn a showcase, brief, UI badge, decoded size, or team policy into a controlled result.
5. Never invent a negative-prompt field, reference limit, seed determinism, cost, speed, resolution, API parameter, model feature, or success guarantee. Separate verified runtime parameters from prompt text and unknowns. [PD-15]
6. Never choose a platform, endpoint, or model merely to satisfy a request for pasteable JSON. When the user has not selected the runtime, deliver a platform-neutral prompt and parameter manifest; treat endpoint JSON as the one blocking question. Verifying that one platform supports a field does not authorize selecting that platform.
7. Do not call paid image, video, or audio generation unless the user separately and explicitly authorizes that call. Prompt preparation alone is not authorization.
8. Ask only for missing information that materially changes task routing, rights, or delivery. Otherwise proceed with clearly labeled assumptions and unknowns. [PD-03]

## Workflow

1. Classify generate/reference/edit/extend/first-frame/first-and-last-frame and locked versus unlocked input behavior. Align asset roles, task hint, prompt verbs, and runtime parameters; do not use `auto` to hide ambiguous intent. [PD-02]
2. Normalize the brief into exact entities, state, space, action, camera, light, audio, duration intent, and acceptance conditions. Resolve contradictions before writing.
3. Map every active reference by upload order, job, allowed inheritance, and excluded inheritance. Distinguish identity, wardrobe, location, style, motion, camera, audio, first/last frame, and diagram roles. [PD-05]
4. Build the prompt with the production schema in [references/prompt-schema.md](references/prompt-schema.md). Use natural prose or structured blocks according to platform evidence and task complexity; neither format is universally correct. [PD-04]
5. Keep one primary causal event or state delta per shot. Use exact counts, ownership, landmarks, frame-left/right, depth, first-frame occupation, axis, eyeline, and a visible end state. Split overloaded beats or move difficult control into a diagram, keyframe, blockout, insert, or separate shot. [PD-07] [PD-08]
6. Treat timecoded beats as semantic pacing, not frame-accurate duration. Describe physics as contact, force/direction, inertia/material response, and visible result. Convert emotion adjectives into observable gaze, breath, gesture, tempo, tactic, and state change. [PD-09] [PD-10] [PD-11]
7. Prefer positive observable constraints, then add precise necessary bans for counts, identity, silent characters, subtitles, BGM, or edit scope. Do not treat prompt length as a quality metric. [PD-14]
8. End with a cut-ready final state and explicit acceptance criteria. Preserve the working prompt; each proposed revision changes one necessary variable and has a finite stop/route condition. [PD-17]

For detailed reference, motion, acting, audio, and platform boundaries, read [references/reference-motion-audio.md](references/reference-motion-audio.md). For failures or repair, read [references/revision-failure-patterns.md](references/revision-failure-patterns.md). Read [references/provenance.md](references/provenance.md) only for evidence audits, source questions, or non-obvious claim verification.

## Required output

Return, in this order:

1. **Input basis** — task/platform/model/input mode, assumptions, verified parameters with source date, and unknowns.
2. **Final prompt** — directly usable and faithful to the requested dialogue language.
3. **Acceptance checks** — observable entities, reference roles, action/physics, acting, camera, audio, and end state.
4. **Failure risks** — only task-relevant risks, with no success guarantee.
5. **Revision ladder** — minimal one-variable changes, what remains fixed, expected diagnostic value, and the stop/route condition.

If a missing decision would materially change the result, state the smallest blocking question after providing any useful non-dependent work.
