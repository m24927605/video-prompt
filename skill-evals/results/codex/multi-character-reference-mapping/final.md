## Input basis

- **Task:** Reference-based generation of one continuous 12-second shot with dialogue.
- **Platform/model:** Unknown; this is platform-neutral. No model ID, aspect ratio, resolution, reference weighting, or runtime fields are assumed.
- **Input mode:** Images, video, and audio are semantic references—not an edit source or first/last-frame pair.
- **Assumptions:** References are uploaded in the stated order. “Both hands visible” is interpreted as all four human hands visible and empty at the end.
- **Verified runtime parameters:** None. Twelve seconds is the requested creative duration, not a claim about endpoint support. Knowledge archive date: 2026-08-22.

## Final prompt

```text
Generate one continuous 12-second shot with synchronized dialogue. No cuts, transitions, time jumps, or slow motion. The single primary event is the left-to-right transfer of exactly one brass case, ending with that case resting on the bench between Mara and Ivo.

REFERENCE CONTRACT — use upload order exactly:

@Image 1 and @Image 2 together define only Mara’s identity and her exact green courier coat.
Use only: Mara’s face, hair, skin, body proportions, stable identifying features, and the green courier coat’s cut, construction, material, details, and color.
Do not inherit: pose, expression, gaze, hand position, props, other wardrobe, accessories, background, platform, lighting, color grade, camera, lens, framing, composition, text, or other people.

@Image 3 defines only Ivo’s identity and his exact gray mechanic uniform.
Use only: Ivo’s face, hair, skin, body proportions, stable identifying features, and the gray mechanic uniform’s cut, construction, material, details, and color.
Do not inherit: pose, expression, gaze, hand position, props, background, platform, lighting, color grade, camera, lens, framing, composition, text, or other people.

@Image 4 defines only the train-platform geometry and wet-night lighting.
Use only: the platform’s physical layout, bench and structural landmarks, surface materials, wet ground, motivated night-light direction, color, intensity, and wet-surface reflection behavior.
Do not inherit: people, identities, faces, bodies, wardrobe, props, text, source framing, composition, camera position, lens, motion, or audio.

@Video 1 defines only the relative timing and left-to-right spatial path of a single suitcase handoff.
Apply only its reach, contact, grip-transfer, release cadence, and left-to-right trajectory to the brass case in this shot.
Do not inherit: performers, identities, faces, anatomy, hand choice, wardrobe, suitcase appearance or material, location, background, camera, composition, lighting, color grade, text, or audio.

@Audio 1 defines only Mara’s voice identity, timbre, and natural accent. Use it only for Mara’s line. Do not inherit its original words, background noise, music, room tone, or any other voice.

@Audio 2 defines only Ivo’s voice identity, timbre, and natural accent. Use it only for Ivo’s line. Do not inherit its original words, background noise, music, room tone, or any other voice.

Never blend, average, exchange, or transfer roles between references. Mara never acquires Ivo’s identity, uniform, or voice. Ivo never acquires Mara’s identity, coat, or voice. No reference supplies any property beyond its explicitly assigned role.

ENTITIES AND SPACE:
Exactly two people: Mara and Ivo. Exactly one closed brass case throughout; no duplicate, replacement, morph, disappearance, or extra luggage.
Mara wears the green courier coat from Images 1–2. Ivo wears the gray mechanic uniform from Image 3.
Use the platform geometry and wet-night lighting from Image 4.
A bench occupies frame center between them. Mara remains frame left; Ivo remains frame right. Neither crosses the center axis.

FIRST FRAME:
A newly composed, static, eye-level medium-wide two-shot, framed from approximately the knees upward, with both faces, the bench seat, the case, and all four hands visible.
Mara stands frame left in three-quarter profile toward Ivo. She holds exactly one brass case by its handle in her right hand beside her right thigh. Her left hand is empty and visible.
Ivo stands frame right facing Mara. Both of his hands are empty, separate, and visible.
This composition comes from the prompt only, not from any reference.

SEMANTIC PACING:
0.0–2.2 seconds — Mara keeps the case still and looks directly at Ivo. With controlled breath and a clipped, level delivery, using only Audio 1’s voice, Mara says exactly: “You were late.” Ivo remains silent and does not lip-sync.

2.2–4.4 seconds — After a brief reaction pause, Ivo glances once at the case and returns his gaze to Mara. With quiet, steady delivery, using only Audio 2’s voice, Ivo says exactly: “I came anyway.” Mara remains silent and does not lip-sync.

4.4–9.4 seconds — Perform one continuous handoff. Within this interval, preserve Video 1’s relative reach/contact/release timing and left-to-right path. Mara moves the single brass case from frame left toward frame center using only her right hand. Ivo reaches with his left hand. Their grips overlap only after Ivo has securely closed his hand around the handle; Mara then releases. The path terminates directly above the center of the bench. Ivo lowers the case vertically the short remaining distance and places it onto the bench without moving it back toward frame left.

9.4–12.0 seconds — Ivo releases the handle and withdraws his left hand. Both characters remain on their original sides. They hold quiet eye contact while the camera remains still. Preserve a clear final hold.

PHYSICS:
The brass case is rigid and has believable weight and inertia. Arms settle slightly under its weight. The handle remains attached and solid. Hands maintain anatomically clean contact without intersecting each other or the case. The case makes one restrained metallic contact sound when its base meets the bench, then becomes fully supported and motionless. It never opens, bends, floats, or changes size or material.

CAMERA AND LIGHT:
One locked camera position throughout. No pan, tilt, zoom, dolly, reframing, rack-focus distraction, or axis crossing. Keep both people, all hands, the case, and the bench readable during the complete transfer.
Use only Image 4 for platform geometry and wet-night lighting. Wet reflections remain physically soft and subordinate; they must not resemble extra people, hands, or cases.

AUDIO:
English dialogue, exact wording and order, with no overlap.
Audio 1 belongs exclusively to Mara. Audio 2 belongs exclusively to Ivo.
Add only quiet, independently generated diegetic platform ambience and the action-linked case/bench contact sound. Do not copy ambience from either audio reference.
No third voice, narration, music, subtitles, captions, signs, or generated on-screen text.

FINAL STATE:
Exactly one closed brass case rests fully supported and stationary on the bench between Mara and Ivo.
Mara remains frame left and Ivo frame right.
All four human hands are empty, separated from the case and from each other, fully visible inside the frame, and anatomically correct.
Both identities and wardrobes remain unchanged. Hold this cut-ready state through the final frame.
```

## Acceptance checks

- Exactly Mara, Ivo, and one brass case appear; no duplicate figures, reflections, or luggage.
- Mara matches only Images 1–2 and wears the green courier coat; Ivo matches only Image 3 and wears the gray mechanic uniform.
- Only Image 4 supplies platform geometry and wet-night lighting—not composition or people.
- Only Video 1 supplies transfer timing and the left-to-right path.
- Mara starts frame left holding the case in her right hand; Ivo starts frame right.
- Dialogue is exact, ordered, non-overlapping, correctly lip-synced, and assigned to the correct audio identity.
- The transfer has continuous grip, weight, release, and bench contact.
- The camera stays locked and never loses the hands, case, or bench.
- Final frame shows the single case stationary on the bench and all four hands empty and visible.

## Failure risks

- Seven role-limited references create a meaningful risk of identity, wardrobe, composition, or audio leakage.
- Fine hand contact may produce intersecting fingers, premature release, or case duplication.
- Wet reflections may resemble duplicate subjects or props.
- Separate audio-reference assignment and lip-sync depend on capabilities of the unspecified platform.

## Revision ladder

Prospective and untested:

1. **If framing hides a hand:** Change only the shot size one step wider. Keep references, blocking, timing, dialogue, and camera axis fixed. Stop if all four hands become continuously readable.
2. **If one reference leaks:** Replace only the offending asset with a clean role-isolated crop or plate. Keep the prompt and all other assets fixed. If the same leakage persists, stop joint generation and route to separate character/background generation plus compositing.
3. **If contact or case continuity fails:** Add only a simple blocking diagram defining the two grip points, left-to-right path, and bench endpoint. If the same defect persists, route the handoff to an insert or VFX instead of lengthening the prompt.
4. **If voices swap or lip-sync remains unusable while picture passes:** Change only the audio route to silent picture generation followed by ADR using Audio 1 for Mara and Audio 2 for Ivo.
