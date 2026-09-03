# Production hierarchy and gates

Read this file when turning a concept, treatment, or screenplay into a multi-shot production plan.

## Project charter

Lock before production:

- story purpose, audience, tone boundaries, target length and delivery surfaces;
- actual generation platform, displayed model, model ID if exposed, region, current documentation date;
- aspect ratio, master frame rate, codec/color/audio/subtitle/master specifications;
- the channel of record for every delivery spec: runtime parameter, prompt text, or geometry drawn into the picture;
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

## Completed, current, and reserved beat firewall

Keep a completed, current, and reserved beat firewall for every scene. Completed beats are accepted visible facts; the current beat is the next required delta; reserved beats are future work and must not be pre-completed by convenience.

If an accepted deviation completes a future beat, remove that beat from downstream work and recalculate the next delta. A rejected deviation is not canonical, even when it looks useful; it may inform diagnosis but cannot advance the schedule. [FP-06]

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
Invariants: attributes that must hold constant for the whole interval and still match at the boundary with adjacent shots
Population: exact counts of people and continuity-critical props; whether the set is closed
Space: floor plan, landmarks, axis, screen direction, eyelines, entrance/exit
Camera: size, side/height, lens feel, movement, focus, cut/continuation, handles
Look: light, palette, material, weather, VFX intent
Sound: speaker, exact dialogue/language, room tone, foley, music/silence, layer assignment
Inputs: reference IDs/hashes/roles/packet order/admitted and denied scope/inheritance exclusions/rights
Prompt and parameters: version, platform/model/task/aspect/duration/format/audio
Spec channels: which channel enforces ratio, duration, resolution, audio
Acceptance: hard gates, rubric, neighbor compatibility, route rules
Provenance: parent run, one change, output hash, reviewer, decision, actual time/cost
```

Two contract lines the delta model does not supply on its own:

- **Invariants** are inherited from scene state, not re-described as prose inside the action. A start state plus one delta says what changes; it never says which unchanged things were required to stay unchanged. Invariants are what the neighbor shot and QC compare at the interval boundary, and what a retry must preserve. Carry them as opaque identifiers that resolve to a state entry, never by restating the attribute in each shot, which is exactly how two shots drift apart. Pick invariant IDs that name a slot rather than its content, so a change to the pinned attribute is a version bump instead of an edit to every shot that inherits it.
- **Population** bounds quantity, which `required/forbidden` does not. Duplication, extra figures and silently added props are only detectable against a declared count and a closed/open flag. How a prompt phrases a count belongs to `seedance-prompt-director`; the schedule is what makes the count inheritable across shots and checkable after the run.

Never assume one platform's request schema is portable. Keep prompt text and runtime parameters separate.

## Shot-to-job mapping

A generation job is not a shot. Decide and record the mapping for every queued shot:

- **one job, one shot** — the default; state in the request that the job runs continuously with no internal cut;
- **one job, several shots** — internal cuts written into one request. This buys cut-adjacent continuity and costs retry granularity: the job is the unit of re-run, so no internal shot can be redone alone. Choose it only where that coupling is worth paying for;
- **several jobs, one shot** — a split for risk, length, capacity, or coverage, reassembled in the edit.

Accounting stays per shot whatever the mapping. Record, for every job output, the shot IDs it delivers and their in/out points, so review, acceptance, retry counts, coverage, and cost attribute to shots rather than to jobs. A job carrying several shots is accepted per interval; one unusable interval does not approve the others.

Treat job capacity as a shot-design constraint. Record the platform's current per-job ceilings — clip length, reference slots, permitted cut structure, and which decisions have a runtime control at all — and check each shot's entity set and beat count against them at breakdown. A shot that exceeds capacity is a split or a pre-composite decision made before queueing, not after a failed run. Capacities are platform- and date-specific; re-read them at charter time.

## Spec channel of record

For every delivery spec — aspect and framing, duration, resolution, frame rate, audio presence — record which channel enforces it: a runtime parameter, a sentence in the prompt, or geometry drawn into the picture. They are not interchangeable, and only the runtime container binds delivery.

- Bars, mattes, or a wider ratio drawn inside the picture are content. They are baked in, they do not change the container, and conform, reframe, safe areas, and archive specs must be planned against both facts.
- Timing written into prompt text is editorial notation, not a render budget. Give each shot a target duration in the manifest, compare it with the delivered clip length in the ledger, and treat a systematic gap as a shot-design or coverage problem rather than a wording problem. How a prompt should phrase timing belongs to `seedance-prompt-director`; the reconciliation is a production control.
- Where a decision could have been set by a runtime control but was written in prose instead, mark it unenforced in the shot contract. Nothing in the record will show whether the model honored it.
- Where both channels state the same spec, keep them equal deliberately and re-check both after any parameter change.

Requested picture geometry and in-text beat timing diverge from the delivered container and duration often enough to make reconciliation a standing duty rather than an assumption about model behavior.

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
- asset preparation and conditioning passes, which run in their own lane and never mutate approved state;
- review, sound spotting, VFX breakdown, or subtitle preparation that does not mutate the same truth.

Serialize:

- extension chains and continuous action;
- evolving wardrobe, injury, weather, and prop ownership;
- any next shot dependent on an approved prior last frame or motion vector;
- canonical or approved-memory promotion;
- hero close-ups before scene geography/blocking is approved.

Batch only compatible platform, model, task, ratio, resolution, format, reference-packet version, and rubric. Otherwise failures cannot be attributed.

Queue by the recorded shot-to-job mapping. A job carrying several shots is one unit of re-run and cannot be re-queued shot by shot, so its shots are scheduled, reviewed, and retried together.
