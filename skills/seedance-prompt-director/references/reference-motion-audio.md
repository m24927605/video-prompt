# References, motion, acting, and audio

Read this file for multi-asset prompts, complex action, performance, or sound. It separates official product facts from evidence-supported production practice.

## Reference contracts

Use upload order exactly. Never depend on labels drawn inside an image.

| Role | Take from the reference | Usually exclude unless requested |
|---|---|---|
| Identity | face, hair, body proportions, stable identifying traits | pose, background, framing, light |
| Wardrobe/state | exact garment, wet/dry/damaged/injured state, accessories | a conflicting base or future state |
| Location | geometry, landmarks, materials, weather/light state | the source framing or subject identity |
| Style | medium, texture, palette, grain, contrast behavior | entities, composition, logos/text |
| Motion | action order, path, timing, contact rhythm | performer identity, wardrobe, location |
| Camera | position, move, speed, shot rhythm | subject or scene content |
| Audio | voice timbre/delivery, music rhythm, or ambience—one named job | unrelated voices, BGM, or room tone |
| Storyboard | high-level shot order, blocking, sizes | literal style or frame-perfect alignment |
| Keyframe | relatively strict composition/state checkpoints | pixel-perfect guarantee |
| Diagram/blockout | positions, paths, axis, camera/blocking | shapes, colors, guide lines, render style |
| First/last frame | endpoint image when the runtime role is documented | semantic-only alignment claims |

Template:

```text
@Image 1 defines Character A's identity and approved wardrobe state.
Use: face, hair, body proportions, coat, and scar.
Do not inherit: pose, gray background, framing, lighting, or other people.

@Video 1 defines only the handoff action, timing, and clockwise camera path.
Do not inherit: actor identity, clothing, prop design, room, light, grade, or audio.
```

Archived ModelArk 2.5 documentation dated 2026-08-22 described a maximum of 30 images, 10 videos, 10 audio clips, 50 total, while recommending smaller working ranges for stability. These are ModelArk facts at that date, not universal limits or a quality target. Recheck current official documentation and do not apply them to Higgsfield or another surface.

## Entities and spatial control

- State exact visible counts: `exactly two people`, `one sealed envelope`, `no reflection copies` when material.
- Close open slots: which wardrobe/accessories exist and which do not.
- Fix ownership and hand: `A holds the envelope in the right hand`; write the transfer result.
- Anchor positions to the frame and landmarks: frame-left/right, foreground/mid/background, doorway/table/window, camera side, distance where useful.
- Occupy the first frame. State who is already present, their pose/gaze, held props, and empty zones.
- Repeat critical state in every independent shot. `Same as previous shot` is not an external memory system.

## Action and physics

Use one primary causal event per shot. Small performance cues may support it without adding another major state change.

```text
Start: one intact sphere rests at plate center; the spoon is outside frame right.
Contact: the spoon enters and presses the top once from above-right.
Force/material: the shell resists, then cracks from the contact point; fragments settle downward.
Result: filling flows under gravity and the intact cross-section faces camera.
End: one spoon rests beside one opened sphere; no duplicates.
```

For complex fights or contact:

1. Externalize geometry with a diagram, keyframe, or blockout.
2. Put only one exchange or state transition in a shot.
3. Use locked/simple camera to test action before adding camera complexity.
4. Use inserts/reactions/cutaways to avoid impossible full-body continuity.
5. If the same hard defect survives isolated changes, split or route to VFX rather than lengthening the prompt.

Official launch material acknowledged that complex action physics and very large multi-subject interaction remain weak areas. Input-first fixes and diagrams are evidence-supported practice recommendations, not guaranteed improvements.

## Observable acting

Replace `sad`, `angry`, or `cinematic acting` with testable behavior:

- objective and obstacle;
- tactic toward the other character;
- gaze target before and after the beat;
- hands performing a specific secondary task;
- breath, blink, swallow, grip change, muscle release;
- reaction delay and speaking tempo;
- action stopping point and changed state.

Example: `She keeps sorting receipts while listening. Halfway through the line, her thumb stops on the paper. Her eyes reach the speaker before her head turns; she exhales once, then answers.`

This method comes from repeated production self-reports and team synthesis; its effect size has not been measured in a controlled Seedance 2.5 test.

## Camera, light, and material [PD-12]

- Separate subject movement from camera movement.
- Use one primary camera intention: size, height/side, direction, speed, focus target.
- Translate niche terms into visible focus or movement outcomes.
- State motivated key/fill/practical/rim direction and permitted light changes.
- Describe materials by visible response—roughness, translucency, reflection, viscosity—not prestige adjectives.
- Treat UI quality badges, request resolution, decoded dimensions, container, codec, and color depth as different evidence.

## Dialogue and sound [PD-13]

Specify:

1. speaker and who remains silent;
2. language, regional accent, voice identity reference, and one playable delivery direction;
3. exact dialogue in the original requested language;
4. ordering and pause/reaction timing;
5. mic perspective/room tone, action-linked SFX, BGM or silence, subtitles or none;
6. what final post-production will replace or preserve.

Archived documents used both inline markers—music `(...)`, SFX `<...>`, dialogue `{...}`, subtitles `【...】`—and ordinary quoted dialogue. They are prompt syntax, not JSON or weighting. Do not claim either style is uniquely correct.

`No subtitles`, `No BGM`, and `No audio` were documented prompt-language controls. The archived ModelArk request schema did not document a separate `negative_prompt` field. Necessary textual exclusions remain valid; broad negative stacks are not a substitute for a precise desired state.

Generated sound is a scaffold unless its evidence passes. A playback icon proves neither sound content nor quality. Evaluate actual audio, dialogue accuracy, voice identity/naturalness, lip-sync, SFX causality, room-tone continuity, level, and mix. Platform-specific output channels must be verified rather than inferred.
