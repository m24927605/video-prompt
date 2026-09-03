## Input basis

- **Operation:** Platform-neutral reference generation.
- **Duration intent:** 12 seconds, one continuous shot.
- **Platform/model:** Not specified; runtime fields, supported reference syntax, and audio controls remain unknown.
- **Mapping assumption:** Image 1 is primary when Mara’s two views overlap; Image 2 supplies only details hidden or unclear in Image 1.
- **No invented settings:** Aspect ratio, resolution, frame rate, seed, and provider-specific parameters are omitted.

## Final prompt

```text
[TASK]

Generate one continuous 12-second dramatic shot using the uploaded references only for their explicitly assigned roles below. The single causal event is the controlled transfer of one brass case from Mara to Ivo, followed by Ivo placing it on the bench between them.

[REFERENCE BINDINGS — STRICT ROLE ISOLATION]

Image 1 → Mara, entire clip.
Use only Mara’s primary identity—face, hair, body proportions, stable identifying features—and the visible design, color, fit, and material of her green courier coat.
Do not inherit pose, expression, background, lighting, framing, crop, composition, props, or other people.

Image 2 → Mara, entire clip.
Use only complementary identity and green-coat details that are hidden or unclear in Image 1. Where both images show the same detail, Image 1 is authoritative.
Do not inherit pose, expression, background, lighting, framing, crop, composition, props, or other people.

Image 3 → Ivo, entire clip.
Use only Ivo’s identity—face, hair, body proportions, stable identifying features—and his gray mechanic uniform.
Do not inherit pose, expression, background, lighting, framing, crop, composition, props, or other people. Do not transfer any part of Ivo’s identity or uniform to Mara.

Image 4 → environment, entire clip.
Use only the train-platform geometry, architectural landmarks, surface materials, and wet-night lighting state. Preserve the platform’s spatial relationships and rain-wet reflective surfaces.
Do not inherit people, identity, wardrobe, props, framing, crop, camera position, composition, or audio.

Video 1 → brass-case action only, during the transfer.
Use only its semantic timing and the suitcase handoff’s left-to-right screen path. Apply that path to the brass case.
Do not inherit the suitcase’s appearance, size, material, identity, actors, hands, bodies, wardrobe, setting, camera, composition, lighting, color grade, cuts, or audio.

Audio 1 → Mara’s speaking voice only.
Use only its voice identity, timbre, accent, and natural vocal character for Mara’s exact line below.
Do not inherit words, other voices, ambience, sound effects, music, or timing that conflicts with this shot.

Audio 2 → Ivo’s speaking voice only.
Use only its voice identity, timbre, accent, and natural vocal character for Ivo’s exact line below.
Do not inherit words, other voices, ambience, sound effects, music, or timing that conflicts with this shot.

[EXACT ENTITIES]

Exactly two people: Mara and Ivo.
Exactly one portable case: a rigid brass case with one handle.
No suitcase, duplicate case, extra luggage, extra people, identity blending, wardrobe swapping, or reflection copies.

Mara wears only her green courier coat from Images 1–2.
Ivo wears only his gray mechanic uniform from Image 3.

[LOCATION AND CAMERA]

Use the train platform from Image 4 under its wet-night lighting. The bench is centered between Mara and Ivo in the midground.

Create an original composition independent of every reference: an eye-level, medium-wide, static two-shot from one side of the platform. No cuts, zooms, pans, reframing, or camera shake. Keep both characters, the case, the bench, and every hand continuously readable. Preserve the left-to-right screen axis throughout.

[FIRST FRAME]

Mara already stands frame left, facing slightly toward Ivo. She holds exactly one brass case by its handle in her right hand at thigh height. Her empty left hand is visible.

Ivo already stands frame right, facing slightly toward Mara. Both of his empty hands are visible. The bench occupies the clear space between them. Neither character changes sides.

[TIMECODED SEMANTIC BEATS]

0.0–2.2 seconds:
Hold the tense opening composition. Mara keeps the brass case steady in her right hand and looks directly at Ivo. Ivo meets her gaze. No one approaches the case yet.

2.2–3.8 seconds:
Without changing position, Mara says exactly, “You were late.”
Her delivery is quiet, clipped, and controlled. Only Mara speaks; Ivo remains silent and reacts with a brief delayed blink.

3.8–8.2 seconds:
After a short pause, Mara extends the brass case from frame left toward frame right, following only the timing and left-to-right screen path of Video 1. Ivo reaches with his left hand, the hand nearest the bench.

Mara keeps hold of the handle until Ivo’s left hand has visibly closed around it and taken its weight. Only then does Mara release. The brass case remains rigid and retains the same size, design, and material throughout.

8.2–9.5 seconds:
Ivo controls the case’s remaining momentum, lowers it onto the center of the bench, and releases it. The case settles with a small, believable weight response and remains stationary between them. Mara does not touch it again.

9.5–11.2 seconds:
Ivo lifts his now-empty gaze from the case to Mara and says exactly, “I came anyway.”
His delivery is restrained, steady, and matter-of-fact. Only Ivo speaks; Mara remains silent, watching him without moving toward the case.

11.2–12.0 seconds:
Hold the cut-ready final tableau. The brass case rests alone on the bench between them. Neither character touches it. Mara remains frame left and Ivo frame right. All four hands are empty, separated, unobstructed, and clearly visible.

[PHYSICS AND CONTINUITY]

The case has consistent mass and downward weight. Show an unbroken contact chain: Mara supports handle → Ivo closes his left hand around handle → Ivo assumes the weight → Mara releases → Ivo lowers case → case contacts bench → Ivo releases.

No teleportation, floating, sliding, morphing, duplication, hand fusion, penetrations, or discontinuous changes of ownership.

[AUDIO]

Natural synchronized speech using Audio 1 only for Mara and Audio 2 only for Ivo. Preserve the exact dialogue wording and speaker order.

Use restrained wet-platform ambience and subtle action-linked sounds: distant rain, low station room tone, quiet coat movement, handle contact, and one soft metallic bench-settle sound.

No additional dialogue, voice swapping, narration, announcements, music, subtitles, captions, or visible text.

[FINAL NON-LEAKAGE CONSTRAINT]

Each reference controls only its assigned target and dimension. Mara never inherits Ivo’s face, body, hair, uniform, or voice. Ivo never inherits Mara’s face, body, hair, coat, or voice. Image 4 supplies no character or composition. Video 1 supplies no appearance, camera, location, or sound. Audio 1 belongs only to Mara; Audio 2 belongs only to Ivo.
```

## Acceptance checks

- Exactly Mara, Ivo, and one brass case appear.
- Mara starts frame left holding the case in her right hand; Ivo starts frame right.
- Identities, wardrobes, and voices remain correctly separated.
- The case follows Video 1’s left-to-right timing/path without inheriting its suitcase design.
- Both lines are exact, correctly assigned, ordered, and synchronized.
- Ownership changes through visible contact rather than teleportation.
- Final frame shows the case stationary on the bench, neither character touching it, and all four hands visible.

## Failure risks

The highest-risk failures are identity blending, coat/uniform crossover, replacement of the brass case with Video 1’s suitcase, premature release during the transfer, voice swapping, and hands becoming hidden in the final frame.

## Revision ladder

1. If identities or wardrobe drift, change only the character-reference block to strengthen Image 1/Image 3 authority; keep action, camera, and audio fixed.
2. If the case duplicates or teleports, change only the contact sequence by slowing the transfer and extending the shared-grip moment; keep all references fixed.
3. If voices swap, change only the audio block to repeat speaker-to-audio ownership immediately before each line. After one failed audio-only retry, preserve the visual take and replace dialogue in post rather than altering the shot.
