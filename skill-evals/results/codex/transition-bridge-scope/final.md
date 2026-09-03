## Input basis

- **Operation:** Reference-generate one transition bridge.
- **References:** `@Video 1` supplies the outgoing boundary; `@Video 2` supplies the incoming boundary.
- **Locked scope:** Neither source segment may be altered, replayed, or regenerated.
- **Runtime:** Provider, model, duration, resolution, aspect ratio, and frame rate are unselected; no provider-specific parameters are assumed.

## Final prompt

```text
Generate only the previously unseen connecting interval between @Video 1 and @Video 2. Keep both source videos completely unchanged; do not reproduce, trim, extend, restyle, or regenerate either source segment.

REFERENCE CONTRACT

@Video 1
Target: the opening boundary of the generated bridge.
Active scope: the bridge’s first instant only.
Inherit: the exact final composition, perfectly top-down camera orientation, camera-motion vector, central-circle screen position and apparent scale, clockwise rotation direction, angular phase, angular speed, lighting, reflections, and nonverbal ambient tail of the single black vinyl record.
Do not inherit: earlier action, identities or objects outside the boundary state, text, logos, dialogue, subtitles, or unrelated music.

@Video 2
Target: the closing boundary of the generated bridge.
Active scope: the bridge’s final instant only.
Inherit: the exact opening composition, top-down camera vector and motion, central-circle screen position and apparent scale, clockwise traffic direction and motion phase, rain intensity and direction, nighttime lighting, wet-road reflections, and nonverbal environmental ambience of the single circular roundabout.
Do not inherit: later action, text, logos, dialogue, subtitles, or unrelated music.

BRIDGE EVENT

Begin immediately after @Video 1 ends, with exactly one black vinyl record centered in precisely the same screen position and at precisely the same apparent scale. Preserve continuous clockwise motion with no phase jump, pause, acceleration spike, deceleration, wobble, reversal, camera-axis jump, translation, or zoom.

Create one uninterrupted material transformation—no cut, wipe, crossfade, dissolve, or second circle. The record’s concentric grooves deepen and broaden continuously into wet circular road lanes. Black vinyl becomes rain-darkened asphalt; fine groove highlights become lane-edge reflections and flowing rainwater; record-surface speculars evolve into reflections from the practical nighttime lights visible at the opening of @Video 2. The center becomes the roundabout’s central island through the same continuous physical transformation.

Throughout the morph, keep the circle’s center, apparent diameter, clockwise direction, angular phase continuity, and apparent angular speed fixed. As the road geometry becomes structurally stable, transfer the continuing clockwise visual motion naturally from the transforming vinyl surface into the clockwise traffic flow and the opening camera vector of @Video 2. The finished ground must not continue spinning unnaturally.

Bring in rain, traffic, practical lights, reflections, and ambience progressively and causally. End with the transformation fully resolved: exactly one wet circular roundabout at night, matching @Video 2’s opening camera vector, traffic direction and motion phase, rain, lighting, reflections, and ambience. The final instant must be cut-ready for an invisible join into @Video 2.

Generate no text, lettering, road words, signs with legible writing, logos, dialogue, voices, captions, or subtitles. Add no new music.

ACCEPTANCE CONDITIONS

Only the bridge is generated; both source segments remain untouched. There is exactly one continuous central circle. Its screen position, scale, clockwise direction, and angular speed do not drift. Grooves visibly and causally become wet roads rather than changing through a cut or dissolve. The opening joins cleanly from @Video 1, and the final camera motion, traffic flow, rain, light, reflections, and ambience join cleanly into @Video 2.
```

## Acceptance checks

- No duplicated record, roundabout, or central circle.
- No positional, scale, angular-phase, or speed discontinuity.
- Roads emerge from the grooves through visible material continuity.
- The resolved road surface is stationary; clockwise motion transfers to traffic and camera.
- The final audiovisual state matches the opening of `@Video 2`.
- No generated text, logo, speech, or subtitles.

## Failure risks

The main risks are a disguised crossfade, angular-speed drift, duplicated rings, or the completed road surface continuing to rotate. Runtime support for two video references and boundary control remains unknown until a provider is selected.

## Revision ladder

1. If the morph reads as a dissolve, strengthen only the groove-to-road physical deformation.
2. If the ending spins unnaturally, adjust only the point where apparent rotation transfers from surface motion to traffic and camera motion.
3. If either join still drifts after two focused attempts, stop lengthening the prompt and use explicit endpoint keyframes or compositing on a runtime that supports them.
