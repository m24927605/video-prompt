### Input basis

- **Operation:** Append new material only after the source.
- **Evidence:** Author self-report, not direct observation.
- **Reported final-frame facts:** An adult in a yellow coat stands frame left, holds a black umbrella, faces a glass door, and wet pavement reflects blue light.
- **Unknown:** Subject motion and direction, camera movement and velocity, audio content and phase, duration, frame rate, identity details, umbrella state, and playback timing.

### Provider-neutral continuation prompt

```text
APPEND AFTER THE SOURCE ONLY. Preserve the existing source unchanged; do not regenerate, replay, summarize, or modify it.

The following boundary description is author-reported and was not verified through direct inspection of the source:

At the source endpoint, an adult wearing a yellow coat is positioned frame left, holding a black umbrella and facing a glass door. Wet pavement reflects blue light.

Begin the newly added interval from that reported arrangement. Preserve the adult’s frame-left placement, yellow coat, black umbrella, orientation toward the glass door, and the blue reflection on the wet pavement. Do not invent identifying features or an unreported state for the umbrella, door, or surrounding scene.

No new narrative action has been specified. Continue with a restrained hold: the adult remains in place and maintains their orientation and possession of the umbrella, with only minimal natural body settling. Do not introduce another person, a new prop interaction, dialogue, or an abrupt lighting change.

The source clip itself, if available at execution time, is the sole authority for boundary motion, camera motion, and sound. Match only what the source actually establishes. This text does not assert that the subject was stationary, that the camera was locked, or that any sound was present.

If the runtime cannot inspect those boundary properties, do not infer a motion vector, camera velocity, or audio phase from this description. Treat motion matching, camera-velocity matching, and phase-continuous sound as unresolved. Introduce no new foreground dialogue, music, or designed sound cue; final audio continuity must be conformed after the source audio is available.

End on the same clear spatial relationship: the adult remains frame left, holding the black umbrella and facing the glass door, while the wet pavement continues to carry the blue reflection.
```

The visual boundary can be approximated from the report, but a seamless motion, camera, or audio join cannot be validated without the source clip, its audio, and playback metadata.
