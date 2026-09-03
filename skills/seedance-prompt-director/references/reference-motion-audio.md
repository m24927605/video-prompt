# References, motion, acting, and audio

Read this file for multi-asset prompts, complex action, performance, or sound. It separates official product facts from evidence-supported production practice.

## Reference contracts

Use upload order exactly. Never depend on labels drawn inside an image.

## Reference token and dimension authority

Treat every user-provided reference token as opaque: preserve it byte-for-byte. Do not invent, normalize, translate, or renumber a token. Specific token syntax is a capability claim only when the selected surface has verified or documented it; otherwise retain the token as user input and label its runtime interpretation unknown. [PD-15]

For each target × dimension, name one unique winner. An explicit user mapping has priority over any reference authority. A dimension with no winner is inactive: do not use media type or upload order to guess an owner. Record the winner, the property it controls, and the excluded properties; a token alone supplies no extra authority. [PD-05]

## Active reference contract

Every active reference must state all five contract fields: **source/upload label**, **target**, **active scope/time**, **preserve/allowed inheritance**, and **excluded inheritance**. A reference is inactive until it has a job; do not let it supply unstated properties. [PD-05]

```text
Source/upload label: @Image 2
Target: Character A in the generated clip
Active scope/time: identity for the entire clip; no control after the final frame
Preserve/allowed inheritance: face, hair, body proportions, and named wardrobe items
Excluded inheritance: background, pose, composition, crop, lighting, and other people
```

- **Declare the channel list closed** — the preserve/allowed field should name the channels the asset governs and state that the named channels are the complete set. Choose the channels the shot actually needs; form and proportion, surface and material, light and atmosphere, color and grade, motion path, and timbre are the usual axes. An allow-list that is not declared complete reads as an open list, and an open list is how an asset acquires authority nobody granted it.
- **One asset may be split across modalities** — where a source contributes on one channel only, activate that channel and exclude the rest of the same asset by name, including the modality it is not being used for. An asset supplied for one modality is not thereby a reference for another: an asset named for its sound is not a picture reference, and an asset named for its picture is not a sound one. State the exclusion; it costs a clause.
- **Bind twice** — declare each asset's contract once, apart from the descriptive body, then re-assert the binding at each point in the body where that entity is acted on. The declaration establishes the contract; the in-body repetition is what keeps a long description attached to it. An entity the shot must respect can also be named without being bound: when you name one, say plainly that no asset is supplied for it, so the name is not read as a reference.

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

@Audio 1 defines only the speaker's voice for the lines quoted in [AUDIO].
Use: timbre, accent, apparent age, breath placement, and speaking rate.
Do not inherit: the source's reverb and noise floor, its ambience, its music, and its level.
The figure speaks only the words quoted in [AUDIO] and no other words.
```

An audio reference takes the same take-and-exclude pair as a picture reference, and for the same reason: a voice asset arrives with a room, a distance and a level alongside its timbre, and naming the speaker grants none of those. Where an acoustic property is part of what the asset is for rather than an accident of its recording — a space it is meant to keep, a proximity effect, a stated degree of dryness — declare that property as taken *before* the exclusion list, or the general exclusion of the source's space silently deletes the thing the asset was made for.

Archived ModelArk 2.5 documentation dated 2026-08-22 described a maximum of 30 images, 10 videos, 10 audio clips, 50 total, while recommending smaller working ranges for stability. These are ModelArk facts at that date, not universal limits or a quality target. Recheck current official documentation and do not apply them to Higgsfield or another surface.

## Person-reference scope

An unqualified person or character reference means the full visible person: identity, hair, body, visible wardrobe, footwear, and accessories. For that scope, exclude background, pose, composition, crop, and light unless the user explicitly activates one of them.

`Face-only` or `identity-only` explicitly limits inheritance to face/identity and does not lock wardrobe, footwear, or accessories. Name a wardrobe/state reference separately when those details must remain fixed.

## Example inheritance by dimension

Treat an example as a reference with dimensions, not as a permission to recreate its whole content. A structure-only example inherits only hierarchy, control depth, and granularity.

Structure-only examples do not inherit story, POV, camera, style, assets, dialogue, or outcome. Activate any of those dimensions separately and label the chosen source, target, scope, preserve list, and exclusions.

## Entities and spatial control

- State exact visible counts: `exactly two people`, `one sealed envelope`, `no reflection copies` when material.
- Close open slots: which wardrobe/accessories exist and which do not.
- Ban an unwanted archetype by its parts, not by its name. A category or brand name is a label the model can satisfy while still building the object it already knows: forbidding the label leaves the geometry untouched. Name instead the specific features by which that archetype is recognised — the grip and carry geometry, the vent array, the mount, the port shape, the proportion of one section to another — and pair every part you forbid with the part you require in its place, so the object stays buildable. A part forbidden with nothing put there is a hole filled from the same prior that produced it.
- Give an unfamiliar or hybrid object one category sentence, placed immediately after its dimensions and before its finish: what it is, and the nearest category it is not. *An early hand-cranked calculating machine, not a typewriter.* *A glazed ceramic storage jar, not a laboratory flask.* This sentence sets a coarse prior and does not replace the part-level control above — a category name is still a label, and an object bounded only by its category name is still built from the archetype's geometry. Without the sentence, an unfamiliar description resolves toward the nearest familiar category and every later detail is rendered as that category's.
- Fix ownership and hand: `A holds the envelope in the right hand`; write the transfer result.
- Extend that pinning beyond held objects to any asymmetric attribute the shot depends on: anything worn, carried, marked, or affixed on one side of a body, and the facing of an object or garment that is not symmetrical. Name the side once, then repeat that same side at every later mention of the attribute rather than relying on the first statement to hold. A side named once can still flip and a count stated once can still clone, so treat lateral flip and duplication as two failure modes needing two separate guards.
- Anchor positions to the frame and landmarks: frame-left/right, foreground/mid/background, doorway/table/window, camera side, distance where useful.
- Occupy the first frame. State who is already present, their pose/gaze, held props, and empty zones.
- Repeat critical state in every independent shot. `Same as previous shot` is not an external memory system.

Left and right mean nothing until you say what they are relative to. Three uses of the same words collide; label every lateral and depth term with the one it belongs to.

- **The space** — give each side of the location a fixed label and reuse those labels unchanged in every setup, so a camera position can be stated as a direction within the space rather than as a description of the view. This is the only anchor that survives a change of camera.
- **The picture rectangle** — frame-left/right, the band or third the subject occupies, which edge it enters or exits, near plane or far plane. This anchor is valid only for the setup that states it.
- **Light direction** — state it as a direction on the subject or within the space; never as a bare left/right that a reader could take for placement.

Write the layout once, then say that it is the layout: the shot may be framed from any permitted position within it, but no geometry may be added that the layout does not contain. A layout that is written but not declared authoritative is a suggestion.

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

A line supplied to drive a performance is not a line to be spoken. When you write interior text, subtext, or an intention sentence to steer the face, mark it explicitly as never uttered and pair it with the matching audio and mouth state in the same artifact: no vocalization from that figure, and whether the mouth moves at all. Without both, an unspoken line is an invitation to speak it.

Declare a mouth state for every figure in frame, including the ones who never speak, and keep it consistent with the speaker and silence list under **Dialogue and sound**. A figure with no stated mouth state is unconstrained, and lip movement without a line is as costly a defect as a line without lip movement.

A silence declared in the audio contract is a statement about sound and constrains nothing in the picture. A figure the audio contract lists as silent can still be rendered mouthing syllables, because nothing on the picture side said otherwise. For a shot with no dialogue at all, state the mouth state on the picture side — lips closed and at rest — and state the exception in the same sentence, so a gasp, a cry, an impact or a held breath can open the mouth without forming syllabic rhythm. Without the exception, the shots that need one of those read as violations of the rule that was supposed to protect them. This closed-lips default is stated per shot, not per film: in a shot that does carry dialogue, every figure still takes an individually stated mouth state under the paragraph above.

Where a figure does speak and their identity is bound to a reference, say which of the two governs rather than listing both: identity governs and sync follows, as an instance of the conflict order in **Observation and conflict boundary** of `prompt-schema.md`, where reference authority already outranks causal legibility. Stretching the jaw, dentition or mouth shape to reach a syllable is identity drift, not synchronisation. Two requirements written as equals are both relaxed.

## Camera, light, and material [PD-12]

- Separate subject movement from camera movement.
- Use one primary camera intention: size, height/side, direction, speed, focus target.
- Close the axis set. Naming the one move you want leaves the rest open. Name the axes that must stay still as well, in the plain vocabulary the surface is most likely to read: pan, tilt, roll, push and pull, lateral travel, orbit, vertical travel. Closing vertical travel fixes only how the height changes, not where it starts, so state the vantage under **Pin vantage separately from shot size** below and exclude an elevated, overhead or aerial viewpoint by name where it is unwanted. Close the set once, not once per beat. Where the same closed set is reused across shots as one identical string, it must carry its own exception written ahead of the list rather than appended after it, and the exception must restate the permitted movement in full rather than pointing at it — *the only camera movement is a slow forward push* rather than *except the movement named for this shot*; a reused blanket prohibition contradicts every shot that has a move of its own, and a shot whose slight instability is a deliberate positive spec must have that instability struck from its copy of the list.
- State a rig or stability class as a positive property—locked, supported, operator-carried, or a named degree of unsteadiness matched to the beat—and, where the wrong pole is the likely failure, state the excluded pole too. A camera held rigidly still and a camera carrying visible operator movement both need saying; neither is the default.
- Pin vantage separately from shot size: height relative to the subject's eyeline, and whether an elevated or overhead viewpoint is permitted at all. Shot size constrains how much of the subject is in frame and implies nothing about where the camera stands.
- Translate niche terms into visible focus or movement outcomes.
- State motivated key/fill/practical/rim direction and permitted light changes.
- Describe materials by visible response—roughness, translucency, reflection, viscosity—not prestige adjectives.
- Treat UI quality badges, request resolution, decoded dimensions, container, codec, and color depth as different evidence.

## Dialogue and sound [PD-13]

Specify:

1. speaker and who remains silent, with the mouth state of every figure in frame fixed under **Observable acting**;
2. language, regional accent, voice identity reference, and one playable delivery direction;
3. exact dialogue in the original requested language;
4. ordering and pause/reaction timing;
5. the audio channel as a closed set rather than a description: mic perspective and room tone; every sound the clip is permitted to contain, each linked to the origin that produces it—an on-screen event or object, an off-screen source, or a deliberately unsourced element where one is intended; and subtitles or none. State that nothing outside the list is present. Exclude by name whichever unwanted categories are at issue—music or score, ambience the scene does not motivate, added room noise, voices no character produces—rather than leaving them to a general quality request. Silence is a listed element, not the absence of a statement: where a stretch is meant to be silent, say so and say over what interval;
6. what final post-production will replace or preserve.

Archived documents used both inline markers—music `(...)`, SFX `<...>`, dialogue `{...}`, subtitles `【...】`—and ordinary quoted dialogue. They are prompt syntax, not JSON or weighting. Do not claim either style is uniquely correct.

`No subtitles`, `No BGM`, and `No audio` were documented prompt-language controls. The archived ModelArk request schema did not document a separate `negative_prompt` field. Necessary textual exclusions remain valid; broad negative stacks are not a substitute for a precise desired state.

A closed audio set is prompt language whose effect is unverified on any given surface. It states intent precisely; it does not guarantee the output channel. Everything in the evaluation paragraph below still applies—generated sound remains a scaffold until its own evidence passes.

Generated sound is a scaffold unless its evidence passes. A playback icon proves neither sound content nor quality. Evaluate actual audio, dialogue accuracy, voice identity/naturalness, lip-sync, SFX causality, room-tone continuity, level, and mix. Platform-specific output channels must be verified rather than inferred.
