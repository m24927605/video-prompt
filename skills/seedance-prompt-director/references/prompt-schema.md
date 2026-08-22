# Production prompt schema

Read this file when drafting or restructuring a prompt. It turns a brief into a shot contract; it is not a claim that one textual format is universally best.

## Intake and version gate

Record the smallest useful set:

| Field | Record |
|---|---|
| Delivery | purpose, audience, aspect, intended duration, audio/subtitles, downstream edit |
| Runtime | platform/surface, displayed model, model ID if exposed, region, document date |
| Task | generate, reference, edit, extend, first frame, first/last frame |
| Entities | exact count, identity, state, wardrobe, props, owner/hand, invariants |
| Space | location, landmarks, frame-left/right, depth, axis, eyeline, entrance/exit |
| Event | visible start, one primary causal delta, visible end |
| Media | upload order, rights, each reference job and exclusions |
| Look/sound | camera, light, material, color, style, speaker, language/accent, SFX/BGM |

If platform/model is unknown, write a platform-neutral prompt and label runtime parameters unknown. Do not fill “usual” values and do not select a convenient platform on the user's behalf. If exact endpoint JSON is requested, provide the complete prompt plus a parameter-neutral manifest of required decisions, then ask only which runtime to target. Current documentation may validate a candidate after the user chooses it; it does not supply that product decision.

## Task routing

These are contracts, not interchangeable prompt openings. [PD-16]

| Task | Prompt contract | Runtime boundary |
|---|---|---|
| Text generation | State `Generate` and the complete shot | Set only parameters confirmed for the actual surface |
| Reference generation | State `Generate using ... only for ...`; map every reference | Do not infer one platform's reference roles or limits on another |
| Edit | Name the sole master video, A→B change, time/scope, and preserve list | Locked behavior and exact values must come from current endpoint docs |
| Extend | State direction and added duration intent; reconstruct the boundary state before the new event | Do not replay the source ending or treat a drifted tail as canonical |
| First frame | State strict start composition and subsequent delta | A strict runtime role differs from a semantic reference-image instruction |
| First/last | State both endpoints and the causal bridge | Use matching aspect ratios when endpoint behavior is uncertain |

Archived ModelArk evidence dated 2026-08-22 documented `auto/reference/edit/extend` as task hints, strict first/last roles, `adaptive` for locked aspect tasks, and `-1` duration for edit. Recheck the current official endpoint before presenting these as current or before emitting JSON. Do not reuse them for LAS, Higgsfield, or another UI.

## Assembly order

Use only sections that change the result. A compact shot may remain natural prose; a high-risk or multi-reference shot benefits from explicit blocks.

```text
[TASK AND INTENT]
Generate/edit/extend ...
Context, audience, narrative purpose, and one-sentence visible intent.

[EXACT ENTITIES]
Exactly N people/objects. Identity, state, wardrobe, prop ownership, invariants.

[ACTIVE REFERENCES AND ROLES]
@Image/Video/Audio N = job; allowed inheritance; excluded inheritance.

[LOCATION AND SPATIAL MAP]
Landmarks, frame-left/right, depth, axis, eyelines, entrances/exits.

[FIRST FRAME AND BLOCKING]
Who/what occupies each zone; pose, gaze, held props, camera side.

[FORMAT AND DURATION INTENT]
Aspect/duration/audio only when confirmed; otherwise leave in assumptions/unknowns.

[OPTICS AND CAMERA]
Shot size, camera height/side, lens feel, one primary move, speed, focus target.

[TIMECODED ACTION BEATS]
Contiguous semantic intervals. Each: start state → primary event → visible result.

[PHYSICS]
Contact point, force/direction, weight/inertia, material response, result.

[OBSERVABLE ACTING]
Objective, obstacle/tactic, gaze target, hands, breath/blink, timing, state change.

[LIGHT, COLOR, MATERIAL]
Motivated source/direction, palette allocation, material response, allowed change.

[AUDIO]
Speaker, language/accent, exact line, delivery, silent characters, ambience, SFX, BGM.

[STYLE]
Medium/look and only the shot-relevant style grammar.

[POSITIVE CONSTRAINTS]
Expected present state, exact counts, preservation; precise necessary bans only.

[END STATE]
Pose, prop/location state, gaze, camera/motion vector, audio and next-shot handoff.

[ACCEPTANCE CONDITIONS]
Observable pass/fail checks, not aesthetic adjectives.
```

## Task-specific packets

### Reference packet

1. List upload-order bindings before the narrative.
2. Use the smallest reference set that supplies unique information. [PD-06]
3. Separate identity from pose/composition, location from camera framing, motion from performer identity, and audio timbre from music/room tone.
4. If a source already specifies an attribute precisely, do not restate it inconsistently.

### Edit packet

```text
Edit [sole master]. Only change [A] to [B] during [scope/time].
Preserve [identities, untouched geometry, action timing, camera, light, grade, audio...].
The changed element inherits [occlusion/contact/reflection/shadow/material behavior].
Before/after the scope: no other visual or audio changes.
```

Treat preservation wording as intent, not a hard guarantee. Probe actual output frames and duration before conform.

### Extension packet

Reconstruct the source boundary: identity/state, pose, prop owner, positions, motion direction/speed, camera position/velocity, light/color, ambience and audio level. Then specify the new event and a fresh end state. For backward extension, make the source opening the final state of the new material.

### First/last packet

Use strict roles only when the platform documents them. If images are merely semantic references, call the alignment approximate. Specify a plausible causal bridge rather than requesting a teleport between incompatible states.

## Acceptance gate

A prompt is ready only if a reviewer can answer yes/no to all material items:

- Required entities and counts are explicit; forbidden duplicates or intruders are scoped.
- Every active reference has exactly one understandable job and inheritance boundary.
- Start state, primary delta, causality, and end state are visible.
- Space, axis, direction, eyeline, entrance/exit, and prop ownership do not conflict.
- Camera and action are not competing or mutually exclusive.
- Dialogue speaker, language/accent, exact text, silence, subtitles, BGM, ambience, and SFX are resolved.
- Runtime claims are verified for the actual platform/model/date or labeled unknown.
- High-risk failures have a split/input/post-production route and a finite retry policy.
