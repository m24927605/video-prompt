## Input basis

- Platform/model/version: not specified.
- Input mode: sequential video edit, then video extension.
- Step 1 source: `@Video 1`, used as the sole master.
- Step 2 source: only the approved edited output from Step 1.
- Runtime-specific parameters such as task fields, aspect ratio, frame rate, resolution, and codec remain unknown. The prompts below are platform-neutral.
- The source was not available for inspection, so its final pose, doorway position, camera velocity, and audio phase are inherited rather than described speculatively.

## Final prompts

### Step 1 — Edit only

```text
[TASK]
Edit @Video 1 as the sole master video. This operation is an edit only. Do not extend, trim, replay, replace, or retime the source.

[SINGLE EDIT]
For the entire source duration, change only the blue umbrella held by the central adult into a red umbrella. The umbrella must be consistently red in every frame where any part of it is visible, from its first visible source frame through its last visible source frame.

Preserve the exact same umbrella: its owner, shape, size, panel construction, handle, grip, open-or-closed state, material, texture, wetness, transparency, highlights, shading, motion blur, deformation, movement, contact, occlusion, and placement. Only its blue surface color becomes red. The red surface must respond naturally to the source’s unchanged lighting.

[PRESERVE]
Preserve every person exactly: identity, face, hair, body, wardrobe, position, expression, gaze, pose, movement, timing, and interactions.

Preserve every original action and its exact timing. Preserve all other props and their ownership. Preserve the complete background, doorway, environment, weather, lighting, shadows, exposure, color grade, composition, focus, camera position, and every camera move.

Preserve the original duration, pacing, frame order, and sound exactly, including dialogue, ambience, music, effects, timing, perspective, and levels.

Do not recolor any other blue object. Do not alter another umbrella or another person. Add or remove nothing. No cuts, transitions, freezes, duplicated frames, subtitles, text, or audio changes.

[END STATE]
The final frame must match the original final frame in every respect except that the central adult’s umbrella is red instead of blue.
```

### Step 2 — Extend only

Use the approved output of Step 1 as the sole input. Do not use the original `@Video 1` for this operation.

```text
[TASK]
Extend only the approved edited output from Step 1. Append four seconds after its existing final frame. This operation is an extension only: do not edit, regenerate, retime, replay, duplicate, or replace any part of the existing edited video.

[BOUNDARY CONTINUITY]
Begin directly from the exact final frame of the edited source, with no cut, dissolve, freeze, jump, or repeated source action. Use the edited source’s final moments to continue the precise motion state at the join.

Preserve the central adult’s identity, face, hair, body, wardrobe, position, pose, gaze, movement momentum, and grip on the same red umbrella. The umbrella remains consistently red and retains its exact design, material, size, open-or-closed state, and physical behavior.

Continue every other visible person and background action naturally from the boundary without adding, removing, replacing, or duplicating anyone. Preserve the doorway and all environment geometry.

Continue the existing camera position, framing, axis, focus behavior, and motion trajectory at the same direction and speed. If the camera has stopped at the boundary, keep it stationary. Preserve the existing lighting, weather, exposure, color grade, and visual texture.

[ACTION — ADDED FOUR SECONDS ONLY]
During the first portion of the added interval, the same central adult naturally lowers the red umbrella while maintaining a secure grip. The umbrella moves with believable weight and inertia and does not snap, collapse, change color, clip through the adult, or intersect the surroundings.

The adult then moves along a physically plausible path to the existing doorway and enters it. The body and red umbrella clear the doorway naturally without teleporting, sliding, or intersecting the doorframe. Other people continue their established actions and do not react unless that reaction was already developing at the source boundary.

[AUDIO]
Continue the existing ambience and sound bed seamlessly at the same perspective and level. Keep action-linked footsteps and umbrella movement natural and synchronized. Do not introduce new dialogue, a new music cue, subtitles, or a conspicuous new sound effect.

[END STATE]
At the end of the four added seconds, the same adult has crossed the doorway threshold while still holding the lowered red umbrella. The umbrella remains red. Camera, lighting, environment, other people, and audio remain continuous with the edited source.
```

## Acceptance checks

- Step 1 changes only the central adult’s blue umbrella to red across every visible source frame.
- Step 1 preserves source duration, people, action timing, camera, background, light, and audio.
- Step 2 uses only the approved Step 1 output as its source.
- No existing frames are changed or replayed during Step 2.
- The extension begins without a visual, motion, lighting, or audio discontinuity.
- The same adult lowers the same red umbrella and crosses the doorway threshold within the added four seconds.
- No identity drift, umbrella-color flicker, duplicate people, clipping, teleportation, new dialogue, or new camera move appears.

## Failure risks

- The edit may spill into other blue objects or allow the umbrella color to flicker during occlusion or motion blur.
- The extension may drift at the join if the final pose, camera velocity, or doorway geometry is difficult to infer.
- Entering within four seconds may cause rushed or physically implausible movement if the adult is far from the doorway.

## Revision ladder

1. If the edit spills, change only the target binding to a more precise visual description of the central adult and their umbrella; keep every other instruction and runtime setting fixed.
2. If red flickers, change only the temporal constraint to emphasize uninterrupted red coverage through occlusion and motion-blurred frames.
3. If the extension jumps at the join, add only observed boundary details from the approved edited output’s final seconds; do not change the action.
4. If doorway entry is incomplete, change only the action pacing so lowering occupies the first third and threshold crossing completes during the remaining two-thirds.

Stop after two isolated attempts reproduce the same hard defect; retain the last approved Step 1 edit rather than extending a drifted result.
