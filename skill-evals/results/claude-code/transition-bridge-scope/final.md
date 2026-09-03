Bridge contract is clear from the schema — this is a single generate-task transition bridge, delivered platform-neutral since no runtime is selected. Here is the packet.

## 1. Input basis

- **Task:** generate — one transition-bridge clip cut between two untouched sources. Single primary operation; the sources are boundary references only.
- **Platform / model / parameters:** unknown by user's statement ("runtime not selected"). No aspect ratio, resolution, frame rate, duration value, audio capability, or reference/first-last-frame mechanism is asserted anywhere in the prompt.
- **Input mode:** @Video 1 (outgoing) and @Video 2 (incoming) as boundary references. Whether the chosen runtime accepts whole videos as references, or instead needs Video 1's extracted final frame and Video 2's extracted first frame as strict first/last-frame inputs, is a runtime fact — decide after a platform is chosen.
- **Observation boundary:** I cannot inspect either video. Everything below rests on your report: clockwise top-down spinning black vinyl at Video 1's end; clockwise top-down wet roundabout at night at Video 2's start. Exact screen position, scale, angular speed, camera vector, light, and ambience are therefore expressed as *match the reference*, never as invented values.
- **Assumptions (labeled):** both sources share one aspect ratio; the bridge is one continuous shot with no cut; Video 2's roundabout surface is stationary with motion carried by circulating traffic.
- **Unknowns to resolve at runtime selection:** aspect ratio, duration, resolution, fps, audio generation support, reference-role syntax.

## 2. Final prompt (provider-neutral)

```text
[TASK AND INTENT]
Generate one continuous transition-bridge shot to be cut between two existing
videos. Do not re-render, extend, or alter either source; produce only the new
connecting material. Visible intent: a spinning black vinyl record, seen
straight top-down, transforms in place into a rain-soaked circular roundabout
at night, without the circle ever breaking position, scale, or clockwise motion.

[ACTIVE REFERENCES AND ROLES]
@Video 1 = outgoing source. Inherit only its FINAL frame: the top-down
composition, the record's exact screen position and diameter, its clockwise
rotation direction and angular speed, and its lighting and ambience. This is
the bridge's first frame. Exclude all earlier content of Video 1.
@Video 2 = incoming source. Inherit only its FIRST frame: the top-down camera
position, height, and motion vector, the roundabout's exact screen position and
diameter, the clockwise traffic direction, rain intensity, night lighting and
color grade, and ambience. This is the bridge's mandatory final frame. Exclude
all later content of Video 2.

[EXACT ENTITIES]
Exactly one circular subject on screen for the entire bridge: the record that
becomes the roundabout. One central element throughout: the record's spindle
and label, which becomes the roundabout's central island. Vehicles appear only
as small headlight points and streaks on the circular lanes. No people, no
readable text, no signage, no logos, no second circle.

[FIRST FRAME AND BLOCKING]
The bridge opens as a seamless continuation of Video 1's final frame: same
framing, same record position and diameter, same clockwise spin at the same
angular speed, so the join from Video 1 reads as unbroken footage.

[OPTICS AND CAMERA]
Straight top-down view held for the whole bridge. Camera position, height, and
scale relative to the circle stay constant, then in the final moments take on
exactly the camera vector of Video 2's first frame — including any drift or
motion Video 2 opens with — so the join into Video 2 is invisible.

[ACTION BEATS — semantic pacing, not frame-exact]
1. Opening: the black vinyl spins clockwise, identical to Video 1's ending;
   its concentric grooves catch a moving specular sheen.
2. Transformation: while the disc keeps rotating clockwise at the same angular
   speed, the groove rings widen and resolve into concentric wet asphalt lanes;
   the label becomes the roundabout's planted central island; the glossy vinyl
   sheen reinterprets as wet-road reflectivity; rain begins to fall and streak;
   faint headlights emerge, tracing the rings clockwise.
3. Arrival: the surface's own rotation hands off — the angular motion is now
   carried entirely by clockwise-circulating headlights and their reflections
   while the asphalt settles stationary; rain, streetlight color, grade, and
   camera vector settle into an exact match of Video 2's first frame.

[PHYSICS]
Raindrops strike the glossy surface with small ripples and smeared reflections.
Headlight streaks follow circular paths; their tangential speed at the lane
radius is consistent with the inherited angular speed, so motion continuity is
felt, not just seen. Wet asphalt reflects light sources as elongated vertical
smears consistent with a top-down wet surface.

[LIGHT, COLOR, MATERIAL]
Start: the lighting of Video 1's final frame on glossy black vinyl. The only
allowed change is a continuous grade toward the night palette of Video 2's
first frame — streetlight and headlight sources, rain-diffused. Black vinyl
and wet black asphalt are treated as one continuous material family so the
surface never appears to swap or cut.

[AUDIO]
No dialogue, no voiceover, no music, no subtitles. If the runtime generates
audio: crossfade Video 1's outgoing ambience into steady rain, wet-tire hiss,
and distant traffic at the level of Video 2's opening ambience.

[POSITIVE CONSTRAINTS]
One continuous shot, no cuts, no flash frames. The circle's center stays at the
same screen coordinates and the same diameter for the entire bridge. Rotation
stays clockwise at constant angular speed until the traffic handoff; it never
reverses, stalls, or jumps. No text, captions, logos, watermarks, or UI
elements anywhere.

[END STATE]
The final frame duplicates Video 2's first frame: one stationary wet roundabout
seen top-down at night, clockwise traffic, matching rain, light, grade, and
camera vector, ready for a straight cut into Video 2.
```

## 3. Acceptance checks

- The bridge's first frame is indistinguishable from Video 1's final frame; the bridge's last frame is indistinguishable from Video 2's first frame (overlay/AB-flip at both joins shows no jump in position, scale, or grade).
- Circle center coordinates and diameter are constant across the whole clip.
- Rotation is clockwise throughout, at constant angular speed, and the motion handoff to circulating headlights preserves that apparent speed.
- Exactly one circular subject and one central element; no extra discs, roundabouts, or intruding objects.
- Traffic circulates clockwise; rain, night lighting, and color match Video 2's opening.
- Zero frames contain text, logos, subtitles, or watermarks; no dialogue or music.
- One continuous shot with no internal cut.

## 4. Failure risks (no success guarantee)

- **Join mismatch** is the highest risk: without the actual endpoint frames as strict inputs, the model may approximate rather than match Video 1's ending or Video 2's opening, making the cut visible.
- **Center drift or scale breathing** during the morph, since morphs tend to re-compose.
- **Rotation errors:** direction flip, speed change, or the roundabout surface continuing to physically spin into the final frame.
- **Spontaneous text/signage:** road markings, signs, or a record label with readable type violating the no-text ban.
- **Motion handoff reading as a stall** — the moment surface rotation transfers to traffic can look like a freeze if the headlight streaks are too sparse.

## 5. Revision ladder (one variable per step)

1. **If either join mismatches:** switch the input mode to strict first/last-frame — extract Video 1's final frame and Video 2's first frame and supply them as the runtime's documented first/last inputs (only if the chosen runtime documents that role). Everything else in the prompt stays fixed. Diagnostic value: isolates whether mismatch came from loose video-reference inheritance. Stop condition: joins pass the overlay check.
2. **If the center drifts or scale breathes:** add one line pinning the circle's center to the exact frame center (or its reported off-center position) and its diameter as a fixed fraction of frame height. Stop after two attempts; then route to a two-part bridge (vinyl→abstract wet rings, rings→roundabout) as separate ordered artifacts.
3. **If rotation reverses or the road keeps spinning:** move the handoff earlier in beat 3 and add an explicit ban line "the asphalt is stationary in the final third; only lights move." One change, one retry.
4. **If text/markings appear:** add "unmarked asphalt, no lane paint, no signs" as a positive constraint. One retry.
5. **If results still fail after the ladder:** take the generated clips and evidence to `seedance-video-qc` for diagnosis rather than further blind rewrites.

One decision remains open by design: once you pick a runtime, tell me which, and I'll map this neutral contract onto its verified reference mechanism, duration, aspect, and parameter fields — those values are deliberately absent above rather than filled with defaults.
