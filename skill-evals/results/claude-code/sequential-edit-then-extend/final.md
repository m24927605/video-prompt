The two prompt artifacts are ready below. Per the skill's routing rules, the edit and the extend are delivered as two separate ordered artifacts — Artifact 1 edits `@Video 1` only, and Artifact 2 extends only Artifact 1's verified output, so the original source is never edited and extended in one operation, exactly as you required.

A note on constraints: no platform/model was named and I cannot inspect `@Video 1` itself, so both prompts are platform-neutral, the video's described contents (blue umbrella, central adult, doorway) are treated as user-reported facts, and the extend prompt contains bracketed boundary fields to be filled from the actual final frame of the edited output before submission.

---

## 1. Input basis

- **Task chain:** Artifact 1 = **edit** (sole primary operation); Artifact 2 = **extend, appended after the source** (sole primary operation). Artifact 2's declared source is Artifact 1's output, not `@Video 1`.
- **Platform / model / runtime:** unknown — not specified. Prompts are platform-neutral; no aspect ratio, resolution, frame rate, task-hint flag, or endpoint field is asserted. (Archived ModelArk evidence dated 2026-08-22 documented `edit`/`extend` task hints and `-1` duration for edit on that surface only; recheck current docs for whichever runtime you choose — this is not a current or cross-platform claim.)
- **Source observation:** I could not inspect `@Video 1`. Its contents — one blue umbrella held by a central adult, other people, a doorway, existing sound — are user-reported, low confidence. The extend prompt's boundary block must be completed from the edited output's real final frame.
- **Duration:** "+4 seconds" is duration intent; frame-exact length depends on the runtime and must be verified on output.
- **Assumption (labeled):** the umbrella stays open and held throughout `@Video 1`, and the doorway the adult enters is visible or plausibly adjacent in the final frame. Correct the prompts if either is false.

---

## 2. Artifact 1 — Edit prompt (run first, alone)

```text
[TASK AND INTENT]
Edit @Video 1. @Video 1 is the sole master video. This is a color/prop
replacement edit only; no extension, no new events.

[CHANGE]
Only change: the blue umbrella held by the central adult becomes a red
umbrella. The change applies for the entire duration of the source, from
first frame to last frame. Canopy fabric and any originally blue umbrella
parts become red; handle and frame shape, size, open/closed state, tilt,
and the hand holding it remain exactly as in the source.

[INHERITANCE OF THE CHANGED ELEMENT]
The red umbrella inherits the original umbrella's exact position, motion
path, and timing in every frame, plus its occlusion order with people and
scenery, its contact with the holder's hand, and its shadows, reflections,
and wet/dry material behavior — now rendered in red.

[PRESERVE — NO OTHER CHANGES]
Preserve unchanged: every person and their exact count, identities,
wardrobe, and actions; all action timing; every camera position and move;
the full background and environment; lighting, color grade, and weather;
and the complete original audio track (dialogue, ambience, SFX, and any
music) untouched. No umbrella owned by anyone else changes color. No
frames are added, removed, retimed, or cropped.

[END STATE / ACCEPTANCE]
The output is frame-for-frame the same video as @Video 1 except that the
central adult's umbrella is red in every frame where it is visible.
```

**Handoff:** after this runs, verify the output (checks below), then use that verified output — call it **Edited Video 1** — as the one and only source for Artifact 2. Do not submit Artifact 2 against `@Video 1`.

---

## 3. Artifact 2 — Extend prompt (run second, on Edited Video 1 only)

Fill the three bracketed boundary fields from the actual final frame of Edited Video 1 before submitting.

```text
[TASK AND INTENT]
Extend the supplied source video (the edited result with the red
umbrella; this is the sole source). Append approximately 4 seconds of
new material after the source's final frame. Do not modify, replay, or
retime any existing source frame.

[BOUNDARY STATE — must match the source's final frame exactly]
The new material begins in the exact state of the source's final frame:
the same central adult, identical face, hair, wardrobe, and build, holding
the same open red umbrella in the same hand, at [POSITION IN FRAME AND
DISTANCE FROM THE DOORWAY], moving [DIRECTION/SPEED, OR STATIONARY].
Camera continues from [FINAL CAMERA POSITION AND MOTION — static or
completing its move at the same height and side]. Lighting, weather,
color grade, background, and ambient sound continue seamlessly from the
source with no visible or audible cut.

[NEW EVENT — one causal beat]
Over the added ~4 seconds: the adult reaches the doorway, slows, and
lowers the red umbrella — tilting it forward and down, the canopy closing
as their free hand steadies it — then steps through the doorway. The
umbrella tip clears the door frame; the umbrella never changes back to
blue and never leaves the adult's possession.

[PRESERVE]
Exactly the same adult as the source; no new people enter frame unless
already present in the source's final frame, and any others present
continue their existing motion naturally. Background, light, grade, and
ambience remain continuous with the source. Ambient sound continues at
the same level; footsteps and the soft rustle of the closing canopy are
the only new SFX; no added music, no dialogue, no subtitles.

[END STATE / ACCEPTANCE]
Final frame: the adult is inside or crossing the doorway threshold, red
umbrella lowered and closed at their side, back or profile to camera;
the camera holds its final position; ambience continues, cut-ready.
```

---

## 4. Acceptance checks

**Artifact 1 (edit):** umbrella is red in every frame it appears, including under occlusion and in any reflections/shadows; no other umbrella or garment changed color; person count, actions, and timing identical to source; camera moves identical; audio waveform/content unchanged; output duration equals source duration.

**Artifact 2 (extend):** first new frame is visually and audibly continuous with Edited Video 1's last frame (no jump in position, pose, light, or ambience); umbrella is red throughout the new material; one continuous beat — approach, lower/close, enter doorway — with plausible hand contact and canopy physics; no new characters or camera style change; added length ≈4 s; source frames untouched.

## 5. Failure risks

- **Edit scope bleed:** other blue elements (clothing, signage, a second umbrella) may shift red, or the grade may warm globally. The preserve list targets this but is intent, not a guarantee — inspect frames before proceeding.
- **Boundary drift on extend:** if the edited output's tail drifted (color flicker, pose glitch), extending canonizes it. Verify the tail first; if drifted, re-run Artifact 1 rather than extending.
- **Umbrella reverting to blue** in the extension if the boundary block understates it — it is stated twice deliberately.
- **Doorway geometry:** if no doorway is near the adult in the final frame, 4 seconds may force a teleport or rushed walk; if so, the entry beat needs relocating or more added time.
- No success guarantee on any of the above; duration and audio continuity must be checked on actual output.

## 6. Revision ladder (one variable per step, keep everything else fixed)

1. **Edit bleeds to other objects** → add one precise ban naming the specific wrongly-changed object ("the [object] remains its original color"). Stop if it survives two attempts → route to `seedance-video-qc` / post-production color isolation.
2. **Extend boundary jump** → tighten only the `[BOUNDARY STATE]` block with more exact final-frame facts (pose, hand, camera). Stop after two attempts → supply the final frame as a strict first-frame input if the chosen runtime documents that role.
3. **Lower-and-enter beat overloaded in 4 s** → change only duration intent (e.g., ~5–6 s) or split entering the doorway into a second extend. Stop if physics still fails → diagram/keyframe route.

**One blocking question:** which platform/model will run these? Once named, I can verify its current edit/extend parameters and convert both artifacts into that runtime's exact submission format — until then no endpoint fields are asserted.
