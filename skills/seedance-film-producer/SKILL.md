---
name: seedance-film-producer
description: Plan multi-shot Seedance and AI-film production for shorts, series, or 10–90 minute films. Use for creative bibles, assets, continuity state, shot hierarchy, queues, lineage, quality/speed modes, editing, sound, and QC; do not use for a single prompt rewrite, clip failure diagnosis, or generic non-generative production.
---

# Seedance Film Producer

Design an end-to-end, recoverable production system. The model does not supply dependable cross-shot memory; the production system does. [FP-02]

## Route the request

- Use this skill for multi-shot projects, long-form planning, continuity, asset systems, shot queues, versioning, selection lineage, coverage, editing, finishing, or production trade-offs.
- Use `seedance-prompt-director` for one prompt or shot contract.
- Use `seedance-video-qc` for evidence-based inspection of generated media or variants.
- Do not turn a generic screenplay or conventional film plan into an AI-generation workflow unless the user asks.

## Shared operating invariants

1. Reply in the user's language and preserve dialogue language, accent, and cultural context.
2. Gate the plan by actual platform, model/version, rights, delivery, region, and document date. Archived Seedance knowledge date is 2026-08-22; recheck current official documentation for time-sensitive claims. [FP-03]
3. Separate official fact, direct observation, author self-report, peer-reviewed or preprint method evidence, team inference, practice recommendation, and unknown. Never claim an unrun workflow is proven optimal.
4. Keep Seedance 2.0, UI `Seedance 2`, Seedance 2.5, ModelArk, LAS, and Higgsfield evidence distinct. Never transfer one surface's defaults, limits, resolution, cost, or labels to another.
5. Never recommend one giant prompt or an unbounded extension chain for a film. Decompose `Film → Sequence → Scene → Beat → Shot`; every shot must be independently generatable, reviewable, and editable. [FP-01]
6. Do not call paid media generation without separate explicit authorization. Planning and text-only behavioral testing do not authorize generation.
7. Never overwrite canonical truth with a generated result. Preserve approved prompts, state versions, hashes, parentage, and rollback points. [FP-05] [FP-13]

## Workflow

1. Create a project charter for story, audience, duration, platform/model gate, aspect/master specs, rights, risk, budget/time ceilings, and operating mode.
2. Build the creative bible and versioned passports for character, wardrobe/injury, prop, location/weather/light, voice/behavior, camera, style, color, VFX, and sound. A new state is a new immutable asset version. [FP-04]
3. Break the story down to shots. Give each scene a continuity state and each shot required/forbidden entities, start state, one primary delta, end state, spatial rules, inputs, parameters, acceptance gates, and route rules. [FP-06] [FP-07]
4. Plan coverage and handles. Use masters, singles/two-shots/OTS, inserts, reactions, cutaways, establishing/exits, and backups. Split high-risk hands, contact, crowds, exact text, long dialogue, complex physics, or transformations. [FP-08]
5. Choose only useful control assets: floor plan, diagram, storyboard, independent keyframe, or clay/blockout. Storyboards guide high-level order; keyframes are relatively stricter but not pixel locks. [FP-09]
6. Build an end-to-end animatic/blocking cut early. Let the rough cut expose missing coverage and request pickups before upgrading every shot. [FP-10]
7. Queue by dependency. Parallelize independent connective shots and plates; serialize extension, continuous action, evolving wardrobe/injury/props, and handoff promotion. [FP-12]
8. Track every run, one changed variable, reviewer decision, selection lineage, actual time/cost, and checkpoint. Retry to a project-specific ceiling, then change asset/input/angle/coverage or route to edit/VFX/live action. [FP-14]
9. Treat raw generation as one layer. Plan assembly, cleanup, VFX, conform, color, ADR, foley, music, subtitles, mastering, final QC, and archive. Subtitle timing comes from final audio, not prompt timestamps. [FP-11]

Read [references/production-hierarchy.md](references/production-hierarchy.md) when building the hierarchy, coverage, gates, or shot contracts. Read [references/assets-continuity-lineage.md](references/assets-continuity-lineage.md) for passports, state, queues, lineage, checkpoints, and rollback. Read [references/modes-kpis.md](references/modes-kpis.md) for quality/speed/hybrid decisions and metrics. Read [references/editorial-finishing.md](references/editorial-finishing.md) for rough cut through mastering. Read [references/provenance.md](references/provenance.md) only for evidence audits or non-obvious claim verification.

## Required output

Return a production-ready plan containing:

1. Evidence/date/platform assumptions and explicit unknowns.
2. Chosen operating mode and why it fits; identify untested policy assumptions.
3. Film/sequence/scene/beat/shot hierarchy and coverage logic.
4. Bible/passport inventory, state model, asset registry, and reference policy.
5. Shot manifest, handoffs, dependency queue, naming/version/lineage rules.
6. Approval gates, retry ceilings, failure routes, checkpoints, and rollback.
7. Rough cut, pickups, VFX/cleanup, color, sound, subtitle, mastering, and archive plan.
8. KPI dashboard using actual ledger data, not marketing counters or invented estimates.
