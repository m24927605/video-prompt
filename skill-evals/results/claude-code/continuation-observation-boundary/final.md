The Write tool is disabled in this session, so I can't create the plan file — but the deliverable here is pure text, so I'll present the drafted continuation prompt packet directly. It follows the loaded seedance-prompt-director skill's extension rules: boundary facts stay at user-report confidence, the new material sits strictly after the source, and unverifiable dimensions are declared unknown rather than filled in.

---

## Input basis

- **Task:** extend — new material appended **after the supplied source**. The source itself is not replayed, restated, or altered.
- **Platform / model / mode:** none selected, none known. This artifact is provider-neutral; no task hint, endpoint field, aspect ratio, resolution, duration value, or format is asserted.
- **Evidence class of every boundary fact:** *author self-report* (the user's description), low confidence. I have not inspected the clip, its audio, or any playback metadata; nothing below is direct observation.
- **What the report can establish (if accurate):** visible pose class, frame position, wardrobe, one held prop, one environmental surface state, one lighting/color note, one facing direction.
- **What cannot be known from any final frame, and doubly not from a report of one:**
  - **Subject motion:** whether the adult is stationary, mid-step, turning, or decelerating at the cut; umbrella hand and grip; breathing/posture dynamics.
  - **Camera:** position, height, lens feel, shot size, and above all **velocity** — a still description cannot distinguish a locked-off frame from a move caught mid-travel.
  - **Sound phase:** whether audio exists, its ambience content, level, any rain/traffic/BGM/dialogue, and where any periodic sound (footsteps, dripping) sits in its cycle at the boundary.
  - Also unknown: grade, exact framing beyond "adult at frame left," distance to the door, door state (closed/ajar), other entities in frame, weather at the moment of the cut.
- **Assumption (labeled, replaceable):** the user gave no continuation event, so the draft supplies one minimal causal event — the adult enters through the glass door. Swap it freely; everything else stands.

## Final prompt (provider-neutral)

```text
[TASK]
Extend: append a new interval strictly after the supplied source clip. Do not
replay, re-render, or alter any part of the source. The boundary state below is
reconstructed from a secondhand description of the source's final frame, not
from inspection; treat it as approximate and prioritize seamless continuity
with the source's actual last frame over this description wherever they differ.

[BOUNDARY STATE — as reported, low confidence]
Exactly one adult, wearing a yellow coat, positioned at frame left, holding a
black umbrella, body and gaze oriented toward a glass door. The pavement is wet
and reflects blue light. Reported facts end here. Not established by the
report: which hand holds the umbrella, distance to the door, whether the adult
is stationary or mid-motion, the camera's position or whether it is moving, and
what if anything is audible. Inherit all of those from the source's actual
ending; do not introduce a new camera move, a new sound event, or a change of
subject momentum at the join.

[NEW EVENT — assumed continuation, single causal delta]
After the join settles, the adult closes the distance to the glass door, pulls
or pushes it open with the free hand while keeping the black umbrella in the
other, and steps through. The door swings back and settles shut behind them.

[PHYSICS]
The umbrella stays open and in hand until the doorway if raised, or is lowered
naturally at the threshold; no umbrella duplication or hand-swap mid-action.
The glass door shows the street's blue-lit reflection until it opens; the wet
pavement keeps its reflective sheen, with the adult's reflection moving
consistently with their steps.

[CAMERA]
Continue whatever camera state the source ends with; if that state cannot be
matched, hold a neutral static frame from the join onward rather than invent a
move. One camera intention only: keep the door interaction in frame.

[AUDIO]
Source audio phase is unknown. For the new interval only: self-consistent
exterior ambience appropriate to wet pavement (light rain or post-rain street
tone), footsteps and one door sound matched to the visible action. No dialogue,
no BGM, no subtitles. Expect the ambience join to need replacement in post
once the source audio is available.

[END STATE]
The glass door is fully settled shut; the adult is no longer visible on the
street side (visible through the glass is acceptable); the wet pavement still
reflects blue light; camera at rest; ambience continuing steadily — cut-ready.
```

## Acceptance checks

- Exactly one adult; yellow coat and black umbrella persist without color, count, or ownership drift.
- The new interval begins after the source with no replayed or re-rendered source frames.
- One causal chain is visible: approach → hand contact with door → door opens → step through → door settles shut.
- Pavement reflectivity and the blue light quality persist across the interval.
- No new camera move, new character, dialogue, BGM, or subtitles appears.
- End frame matches the stated end state.

## Failure risks

- **Undetectable boundary mismatch (highest):** because the source was never inspected, pose, momentum, camera velocity, and sound phase at the join cannot be matched or even verified — only the actual clip can resolve this. Any output should be treated as unvalidated at the seam.
- **Extension drift:** the model may reinterpret the reported frame (wrong umbrella hand, different door position) and the report gives no authority to overrule it.
- **Wet-surface/reflection physics:** moving reflections on pavement and glass are a known weak area; check for reflection duplicates or static reflections under a moving subject.

## Revision ladder (one variable per rung, untested)

1. **Obtain the source clip or its true final frame** and re-verify every boundary fact against it; promote or correct the report before any other change. Stop here if any reported fact fails — redraft the boundary block only.
2. If the join looks wrong with a verified frame: change only the camera instruction (static hold ↔ matched move); hold entities, event, and audio fixed.
3. If the seam still fails after isolated changes: route to a hard-cut independent shot instead of a seamless extension.

**Smallest blocking gap:** the assumed door-entry event. If the intended continuation differs (e.g., the adult turns away, someone exits the door toward them), tell me the one event and I'll swap only the `[NEW EVENT]`, `[PHYSICS]`, and `[END STATE]` blocks.
