# Production hierarchy and gates

Read this file when turning a concept, treatment, or screenplay into a multi-shot production plan.

## Project charter

Lock before production:

- story purpose, audience, tone boundaries, target length and delivery surfaces;
- actual generation platform, displayed model, model ID if exposed, region, current documentation date;
- aspect ratio, master frame rate, codec/color/audio/subtitle/master specifications;
- rights for story, likeness, voice, music, type, brands, and every reference;
- allowed generation and post tools, budget/clock ceilings, storage and review responsibilities;
- risk tier and chosen operating mode: quality-max, speed-max-with-floor, or recommended hybrid.

Treat availability, prices, quotas, parameters and policies as time-sensitive. Archived skill knowledge is dated 2026-08-22.

## Hierarchy

| Level | Decision | Required artifact | Exit gate |
|---|---|---|---|
| Film | What is the complete experience? | charter, treatment/script, bible, story/color/sound arcs | story, rights, format locked |
| Sequence | What macro objective and turn occur? | sequence card, information/emotion/pace curve, duration budget | turn and dependency clear |
| Scene | When/where/who wants what and what state changes? | scene card, floor plan, continuity state, coverage plan | geography/entities/state solvable |
| Beat | What single visible behavior, reaction, or information unit occurs? | causal beat list with start/end state | each beat earns its screen time |
| Shot | From where does the audience see one beat? | shot contract, input packet, prompt, parameters, QC/route | independently generatable/reviewable/editable |

Model capability does not replace this hierarchy. Single-clip duration or extension support is not long-form memory.

## Scene and coverage planning

For every scene establish:

- narrative purpose, start/end story state, story time and location state;
- cast, wardrobe/injury, props/ownership, entrances/exits, geography, axis and eyelines;
- master/establishing view for spatial literacy;
- singles, two-shots, and over-the-shoulders for performance and eyelines;
- inserts and reactions for props, hands, information, time compression and edit cover;
- exits/transitions and handles for adjacent scenes;
- alternative coverage for identity, hand/contact, crowd, exact-text, dialogue, speed, or physics risks.

If a proposed shot contains several independent `and then` events, separate beats before deciding whether to split the shot.

## Shot contract

Every queued shot needs:

```text
Identity: film/sequence/scene/beat/shot ID, owner, risk, priority
Narrative: purpose, start state, one primary delta, end state
Entities: required/forbidden and passport/state versions
Space: floor plan, landmarks, axis, screen direction, eyelines, entrance/exit
Camera: size, side/height, lens feel, movement, focus, cut/continuation, handles
Look: light, palette, material, weather, VFX intent
Sound: speaker, exact dialogue/language, room tone, foley, music/silence
Inputs: reference IDs/hashes/roles/inheritance exclusions/rights
Prompt and parameters: version, platform/model/task/aspect/duration/format/audio
Acceptance: hard gates, rubric, neighbor compatibility, route rules
Provenance: parent run, one change, output hash, reviewer, decision, actual time/cost
```

Never assume one platform's request schema is portable. Keep prompt text and runtime parameters separate.

## End-to-end gates

1. **Development** — charter, rights, format, budget, risks.
2. **Script/bible** — story and state machines; canonical hero assets approved.
3. **Breakdown/risk** — hierarchy, floor plans, entity schedules, coverage and fail routes.
4. **Previz/anchors** — animatic/blockout; only necessary diagrams/storyboards/keyframes/clay.
5. **Blocking generation** — low-cost narrative and edit feasibility; an end-to-end rough cut exists.
6. **Final shot generation** — locked contracts; outputs enter incoming, never overwrite approved.
7. **Dailies/selects** — full-media review, fidelity before consistency, only approved memory promotion.
8. **Structure lock/pickups** — rough cut exposes missing coverage; downstream impact controlled.
9. **VFX/cleanup/conform/color/sound/subtitles** — normalize and finish rather than endlessly regenerate.
10. **Final QC/master/archive** — complete playback, technical/content/rights checks, independent approvals.

## Queue and dependency graph

Safe to parallelize:

- independent establishing, insert, reaction, cutaway, plate, and texture shots;
- scenes with locked canonical assets and no immediate handoff dependency;
- review, sound spotting, VFX breakdown, or subtitle preparation that does not mutate the same truth.

Serialize:

- extension chains and continuous action;
- evolving wardrobe, injury, weather, and prop ownership;
- any next shot dependent on an approved prior last frame or motion vector;
- canonical or approved-memory promotion;
- hero close-ups before scene geography/blocking is approved.

Batch only compatible platform, model, task, ratio, resolution, format, reference-packet version, and rubric. Otherwise failures cannot be attributed.
