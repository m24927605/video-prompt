Nothing was written to disk in this read-only session — the deliverable is the text artifact below, built from the skill's schema and reference/audio/failure guidance.

## 1. Input basis

- **Task:** reference generation, one continuous shot, ~12 s intent, English dialogue, 7 assets (Image 1–4, Video 1, Audio 1–2). Task verb: `Generate using … only for …`. If your endpoint exposes task hints, use `reference`, not `auto`.
- **Platform / model:** not stated → platform-neutral prompt. Seedance 2.0, the `Seedance 2` UI label, Seedance 2.5, and third-party surfaces are kept separate; none is assumed. The `@Image/@Video/@Audio N` bindings follow archived ModelArk Seedance 2.5 prompt guidance (archive date 2026-08-22); on another surface, re-map by upload order in that surface's syntax.
- **Verified runtime parameters:** none. No live documentation check was possible in this session. Archived ModelArk 2.5 facts (2026-08-22): reference ceilings 30 images / 10 videos / 10 audio / 50 total — your 7 assets sit inside those, but that fact does not transfer to Higgsfield or other UIs.
- **Assumptions (labeled):** 16:9 horizontal (a 9:16 frame cannot hold this lateral two-shot without re-blocking); the brass case is defined by no reference, so it is specified in prose as a briefcase-size hard case; Ivo starts empty-handed; Image 4 contains or can accommodate one bench; "both hands visible" is read strictly as all four hands visible and empty (which also satisfies the looser reading); rights to the Audio 1/2 voices are cleared by you; accents are whatever the audio references carry — none invented.
- **Unknowns:** platform/model/version; whether 12 s is a selectable duration value on your surface; resolution; whether the surface supports two voice references bound to two different speakers plus a motion video in one job; audio output channel; whether `@` bindings are honored or need re-syntaxing.
- **Evidence labels used:** handoff design and acting method = practice recommendation (author self-report / team synthesis); weakness of multi-subject contact physics = official limitation acknowledged in launch material; nothing below is a controlled result.

## 2. Final prompt

```text
[TASK AND INTENT]
Generate one continuous 12-second live-action shot using the references below only for the jobs assigned to them. Night, wet train platform. Two people, Mara and Ivo, meet at a bench. Visible intent: one brass case travels from Mara's right hand, left to right, and ends resting on the bench between them with nobody holding it.

[ACTIVE REFERENCES — upload order; each has exactly one job]
@Image 1 and @Image 2 = Mara. Two views of the same single person. Use: her face, hair, skin, body proportions, and the green courier coat exactly as shown. Do not inherit: pose, expression, background, framing, lighting, any bag or prop, or any other person in those images. Do not create a second woman from the two views.
@Image 3 = Ivo. Use: his face, hair, skin, body proportions, and the gray mechanic uniform exactly as shown. Do not inherit: pose, expression, background, framing, lighting, props, or any other person.
@Image 4 = location only. Use: the train-platform geometry, surfaces, bench, overhead fixtures, and the wet-night lighting (direction, color, reflections). Do not inherit: any person, any framing or camera angle, any wardrobe, any prop. The shot's composition is defined below, not by Image 4.
@Video 1 = motion only. Use: the internal tempo of the handoff (reach, hold, lower, release) and its left-to-right path. Do not inherit: the performers, their faces or clothing, the suitcase's design, size, or color, the location, light, camera movement, color grade, or any sound.
@Audio 1 = Mara's voice only (timbre and natural delivery). Apply it only to Mara's line. Do not inherit: any words, music, room tone, or noise in the recording. Never apply it to Ivo.
@Audio 2 = Ivo's voice only (timbre and natural delivery). Apply it only to Ivo's line. Do not inherit: any words, music, room tone, or noise. Never apply it to Mara.
Cross-reference bans: no face, garment, color, background, framing, or voice moves from one reference's subject to another. Mara wears nothing gray from Image 3; Ivo wears nothing green from Images 1–2.

[EXACT ENTITIES]
Exactly two people: Mara and Ivo. Exactly one case: a closed, hard-sided, brass-finish case about briefcase size, one top handle, two front latches, no labels or text; it stays closed and latched throughout and never duplicates or changes color. Exactly one platform bench in the materials of Image 4. No other passengers, staff, train, animals, or reflected extra figures.

[LOCATION AND SPATIAL MAP]
Wet night train platform from Image 4. The bench sits at mid-depth at frame center, seat facing camera. Mara stands just left of the bench's left end; Ivo stands just right of its right end; they face each other across the bench, bodies turned three-quarter toward each other so both faces stay visible. Both are on the camera side of the platform edge; the edge and tracks are behind them in the background. Nobody enters or exits frame.

[FIRST FRAME]
Mara already in the left third: standing, turned toward Ivo, the case hanging at her right side, her right hand (the hand nearer camera) on its handle, arm straight, left hand empty at her side. Ivo already in the right third: standing, turned toward Mara, both hands empty and visible at his sides. Bench seat empty at frame center. Foreground: wet platform with lamp reflections.

[CAMERA]
Static medium-wide two-shot, eye level, camera perpendicular to the line between them, slight telephoto compression, focus on the plane of the two faces and the case. Both faces and all four hands stay inside frame for the entire shot. No camera movement, no zoom, no cut.

[TIMECODED BEATS — pacing guide, not frame locks]
0–1 s: Start state holds. Rain drips from the canopy edge. Mara's eyes are already on Ivo's face.
1–3 s: Mara says: "You were late." Level, low, unhurried, no rise in volume; her jaw sets after "late". Ivo's mouth stays closed.
3–5 s: Ivo blinks once, his eyes drop to the case, then return to Mara's eyes; only then he says: "I came anyway." Quieter than her, even, not a question. Mara stays silent.
5–9 s: The handoff, on Video 1's tempo and left-to-right path. Mara's right hand tightens on the handle; she takes one half-step toward the bench center and swings the case rightward across the gap, arm extending, shoulder dipping under the weight. As the case reaches mid-gap, Ivo takes one half-step in and places his left hand (the hand nearer camera) flat under the case's base on its right side. Together they lower it onto the bench seat at center.
9–12 s: Mara opens her right hand and lifts it clear of the handle; Ivo draws his left hand back from under the case. All four hands go to their sides, open and empty. Both look at the case. In the last second Mara's eyes lift to Ivo's face; Ivo keeps looking at the case. Hold; no further movement.

[PHYSICS]
The case has real weight: the handle stays vertical under Mara's hand, the case does not swing or drift, and Ivo's fingers spread as his hand takes load. The base meets the wet seat with one dull knock; no bounce; the thin water film on the seat spreads out from under the base. The case stays level, upright, handle up. Hands stay outside the case's volume at all times; Mara's hand and Ivo's hand never overlap on the handle.

[LIGHT AND MATERIAL]
Light as in Image 4: overhead platform fixtures as the key from above, wet surfaces returning long broken reflections. No change in light level or color during the shot. The brass finish picks up the overhead lamps as soft warm highlights. Fabrics exactly as in their references.

[AUDIO]
Only two lines, in English, in this order, no overlap:
Mara (voice from Audio 1): "You were late."
Ivo (voice from Audio 2): "I came anyway."
Accent as heard in each audio reference. Each person is silent while the other speaks; no other words.
Ambience: continuous light rain on the canopy, dripping water on concrete, a distant low rail hum. No train arrives, no announcement, no other voices.
SFX: a small handle creak as Mara's grip tightens (≈5 s); one dull knock when the case meets the bench (≈8.5 s).
No background music. No subtitles. No narration.

[STYLE]
Photoreal live-action, natural skin and fabric, no stylization, no text or logos anywhere.

[END STATE — cut-ready]
Case closed, upright on the bench seat at frame center between them, handle up, no hand touching it. Mara frame left with both hands visible and empty at her sides; Ivo frame right with both hands visible and empty at his sides. Mara looking at Ivo; Ivo looking at the case. Camera static; rain ambience continues to the last frame.
```

## 3. Acceptance checks (yes/no)

**Entities and counts**
- Exactly two people, one case, one bench in every frame; no extra figure, reflection-figure, train, or second case at any point.
- Case is brass-finish, closed, latched, same size/design from first to last frame.

**Reference roles / leak matrix**
- Mara's face matches Images 1–2 and she wears the green courier coat; Ivo's face matches Image 3 and he wears the gray mechanic uniform. No face swap; no garment or color crosses (no gray on Mara, no green on Ivo).
- No background, pose, or framing from Images 1–3 appears.
- Location matches Image 4's geometry and lighting, but the composition is the described two-shot, not Image 4's camera angle.
- No performer, clothing, suitcase design, location, or sound from Video 1 appears; only the path and tempo.
- Mara's line carries Audio 1's timbre; Ivo's carries Audio 2's. No swap, no third voice, no words/music/room tone from the recordings.

**First frame and blocking**
- Frame 1: Mara left third, case hanging in her right (camera-near) hand, left hand empty; Ivo right third, both hands empty and visible; bench seat empty at center.
- Nobody enters or exits; the lateral axis (Mara left → Ivo right) never flips.

**Action and physics**
- Case moves left to right in one continuous motion; no teleport, duplication, or direction reversal.
- Mara's right hand on the handle; Ivo's left hand under the base; no finger interpenetration; hands never overlap on the handle.
- Case lands on the seat with no bounce, stays level, handle up; water film responds; nothing passes through the bench.

**Acting**
- Mara's eyes on Ivo throughout her line; Ivo blink → glance to case → back to her eyes → line (≈1 s delay).
- Ending gaze: Mara on Ivo, Ivo on the case.

**Camera**
- Single static eye-level medium-wide; no cut, move, or zoom; both faces and all four hands in frame for the full duration.

**Audio**
- Exact words "You were late." then "I came anyway."; no paraphrase, added words, overlap, or repeats.
- Lip movement matches each line; silent partner's mouth stays closed.
- Continuous rain/rail ambience; knock SFX coincides with the set-down; no BGM, subtitles, narration, announcements.

**End state**
- Case on the bench seat between them, untouched; all four hands visible, open, empty; shot holds still to the last frame (cut-ready).

## 4. Failure risks (no success guarantee)

- **Identity/wardrobe cross-leak** — highest risk with two identity sets plus two voice references; most likely form is coat/uniform color swap or blended faces.
- **Image 4 composition leak** — the model reproduces Image 4's camera angle instead of the described two-shot.
- **Video 1 leak or mirroring** — suitcase design or performer traits bleed in; path renders right-to-left.
- **Contact physics** — shared hand contact on one prop is an acknowledged weak area: interpenetrating fingers, extra fingers, case duplicating mid-transfer, case sinking into the bench.
- **Handedness** — the model may mirror Mara and put the case in her left hand.
- **Dialogue** — speaker/voice swap, merged or paraphrased lines, lip-sync drift, an unrequested announcement/BGM.
- **Duration** — 12 s may not be a valid value on your surface; timecodes are semantic and output length can drift (one archived direct observation: 25 s request → 29.056 s on a third-party surface; no general drift rate).
- **Bench** — if Image 4 has no bench, placement and materials become a prose-only guess.
- **Wet-floor reflections** producing phantom figures.

## 5. Revision ladder (prospective, untested — one variable per rung)

Keep the prompt above as the working baseline; each rung changes one thing and holds everything else (references, camera, dialogue, duration, shot design).

1. **Identity/wardrobe leak** → change only the cross-reference bans (e.g., name the leaked attribute explicitly: "Ivo's uniform has no green panels"). Expected signal: the specific leaked attribute disappears. Stop/route if it recurs: rebuild the leaking character's asset as one clean single-view, neutral-background image, or test that character alone.
2. **Composition follows Image 4** → change only the location input: replace Image 4 with a cropped/figure-free version, or drop it and describe the platform in prose. Expected signal: described two-shot appears with the same lighting. Route if it persists: blockout diagram as an additional reference.
3. **Hand/handle or set-down physics fails** → change only the contact design: Mara sets the case down alone; Ivo's hand reaches the bench only after she releases. Expected signal: clean contact, same path and end state. Route: split into master two-shot + set-down insert, or VFX on the hands.
4. **Path mirrored or tempo wrong** → change only the motion input: remove Video 1 and keep the prose left-to-right path. Expected signal: direction correct; tempo becomes prompt-driven. Route: keyframe of the mid-handoff pose.
5. **Speaker/voice swap or line error** → change only the audio block: add per-beat silence rules ("Ivo's mouth closed 0–3 s; Mara's mouth closed 3–5 s") and keep everything else. Expected signal: correct voice on each line. Route: generate picture-only with "no dialogue" and ADR with the Audio 1/2 voices in post.
6. **Duration rejected or drifts** → change only the duration parameter to the nearest supported value; timecodes stay semantic. Route: trim in post, or an extend task if short.

**Stop condition:** if the same hard defect survives its own isolated rung, route (asset rebuild / split / ADR / VFX) rather than adding more prose.

**Two confirmations before submission (non-blocking):** (a) which platform/model/version you'll submit on, so the binding syntax and duration value can be verified against its current docs; (b) whether Image 4 already contains a bench — if not, rung 2's blockout becomes the safer first input.
