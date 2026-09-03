The skill references are loaded. This is a pure text deliverable — a reference-mapped prompt packet — so producing it makes no system changes; the plan-file and ExitPlanMode tools aren't available in this session, so I'm delivering the packet directly.

---

## 1. Input basis

- **Task**: reference-generate, one shot, one primary causal event (the brass case travels left-to-right and comes to rest on the bench), ~12-second duration intent, English dialogue.
- **Platform/model**: unknown. This is a platform-neutral prompt. No aspect ratio, resolution, frame rate, task-hint parameter, or reference-count limit is asserted; set those only after you name the runtime. The `@Image/@Video/@Audio N` tokens follow your stated upload order — their runtime interpretation is unknown until a surface is selected.
- **Assumptions (labeled)**: (a) Image 4's platform geometry includes or is compatible with a bench between the two positions — if the reference photo has no bench, say so and I'll re-anchor the end state; (b) "both hands visible" means both characters' hands are in frame and free of the case at the final frame; (c) no BGM, no subtitles, natural ambience only. Correct any of these and only that block changes.
- **Motion-reference note**: Video 1 shows a *suitcase*; the target prop is a *brass case*. The prompt inherits only the timing and left-to-right path and explicitly excludes the source prop's design, so the case's appearance comes from prompt text alone.

## 2. Final prompt

```text
[TASK AND INTENT]
Generate one continuous ~12-second night scene: two people meet on a wet train
platform; a brass case passes left-to-right and is set down on the bench between
them. One shot, no cuts.

[EXACT ENTITIES]
Exactly two people and exactly one prop case in the entire clip. No bystanders,
no reflection duplicates, no second case.
- Mara: identity and full wardrobe from @Image 1 and @Image 2 — green courier
  coat, worn closed, consistent from both reference views.
- Ivo: identity and full wardrobe from @Image 3 — gray mechanic uniform.
- The case: one rigid brass case with visible latches, small-suitcase size,
  heavy for its size. Its design is defined only by this text, not by Video 1.

[ACTIVE REFERENCES AND ROLES]
@Image 1 + @Image 2 = Mara only. Use: face, hair, body proportions, green
courier coat, accessories visible in both views. Do not inherit: pose,
background, framing, lighting, crop, or any other person.
@Image 3 = Ivo only. Use: face, hair, body proportions, gray mechanic uniform.
Do not inherit: pose, background, framing, lighting, crop, or any other person.
@Image 4 = location only. Use: train-platform geometry, landmarks, materials,
bench, wet surfaces, night lighting state. Do not inherit: any person, the
source photo's framing or composition, or any wardrobe or prop.
@Video 1 = motion only. Use: the timing and the left-to-right path of the
handoff action. Do not inherit: performer identity, faces, clothing, the source
suitcase's design, location, lighting, color grade, camera framing or movement,
or any audio.
@Audio 1 = Mara's voice only: timbre and delivery for her line. Do not inherit:
any other voice, music, or room tone.
@Audio 2 = Ivo's voice only: timbre and delivery for his line. Do not inherit:
any other voice, music, or room tone. Audio 1 and Audio 2 must never swap
speakers.

[LOCATION AND SPATIAL MAP]
Wet train platform at night per @Image 4. A bench sits mid-frame between the
two characters, parallel to the platform edge. Mara stands frame left of the
bench; Ivo stands frame right of it, about two paces apart, facing each other
across it. Eyelines connect level across the bench. No trains arrive or depart
during the shot.

[FIRST FRAME AND BLOCKING]
Both characters are already present in the first frame. Frame left: Mara,
green courier coat, holding exactly one brass case in her RIGHT hand, arm at
her side, eyes on Ivo. Frame right: Ivo, gray mechanic uniform, both hands
empty and visible at his sides, eyes on Mara. The bench between them is empty.

[OPTICS AND CAMERA]
Static eye-level medium-wide two-shot holding both characters and the bench in
frame for the entire clip. No camera movement, no cuts. Focus stays on the two
characters; camera behavior is NOT taken from Video 1.

[TIMECODED ACTION BEATS] (semantic pacing, not frame-exact)
0–3s  Hold on the two-shot. Rain falls steadily. Mara's grip tightens once on
      the case handle, then she says: "You were late."
3–6s  Ivo holds her gaze through a one-breath pause, then answers, still and
      unhurried: "I came anyway."
6–10s Following the timing and left-to-right path of @Video 1, Mara swings the
      case from her right side toward the bench and sets it down flat on the
      bench seat between them. Her right hand releases the handle and
      withdraws. Ivo does not take the case; his hands stay at his sides.
10–12s End hold: the case rests closed on the bench, untouched. Both
      characters' hands are visible and empty. They keep eye contact. Static
      frame to cut.

[PHYSICS]
The case has real weight: Mara's shoulder dips slightly as she lifts it; it
lands with one dull metallic thud on the wet bench, settles without bouncing
or sliding. Rain beads on the brass and on both coats; wet surfaces reflect
the platform lights per @Image 4.

[OBSERVABLE ACTING]
Mara's objective is to hand off and be done; her reproach shows as the grip
tightening before her line and a clipped, flat delivery. Ivo's objective is to
be accepted back; he answers only after one visible breath, voice low and
even, never breaking eye contact. Neither smiles; the state change is that the
case leaves her hand and neither reaches for it.

[AUDIO]
Only two lines of dialogue, in English, in this order:
1. Mara (voice = @Audio 1): "You were late."
2. Ivo (voice = @Audio 2): "I came anyway."
No other speech. Neither character mouths words outside their line. Ambience:
steady rain on the platform canopy, distant rail hum. SFX: the case's single
dull thud on the bench. No BGM. No subtitles. No on-screen text.

[POSITIVE CONSTRAINTS]
Exactly two people, exactly one brass case, for the full duration. Mara wears
only the green courier coat; Ivo wears only the gray mechanic uniform; wardrobe
never swaps or blends between them. The location stays the @Image 4 platform
throughout. The case never opens.

[END STATE]
Final frame: the closed brass case at rest on the bench between them, no hand
touching it, both characters' hands visible and empty, mutual eye contact held,
camera static — clean cut point.
```

## 3. Acceptance checks (pass/fail on the output)

1. Exactly two people and one case in every frame; no extras or duplicates.
2. Mara matches Images 1–2 (face + green coat); Ivo matches Image 3 (face + gray uniform); no wardrobe color bleed either direction.
3. Background is Image 4's platform; neither person from any image reference appears as a third figure; Image 4's framing didn't override the two-shot.
4. First frame: Mara frame left, case in her right hand; Ivo frame right, hands empty.
5. The case moves left-to-right on Video 1's timing; the case is brass, not the source suitcase; the source performers/location/camera don't appear.
6. Mara's line uses Audio 1's voice, Ivo's uses Audio 2's, in order, exact wording, no swap, no extra speech, no BGM, no subtitles.
7. Final frame: case closed on the bench, untouched, both characters' hands visible and empty, static frame.

## 4. Failure risks (no success guarantee)

- **Bench absent or misplaced** if Image 4 contains no bench — the end state has no anchor (this is the one assumption most worth confirming).
- **Prop bleed from Video 1**: the case renders as the source suitcase despite the exclusion.
- **Handoff completing hand-to-hand** (Ivo grabbing the case) instead of ending on the bench, since the motion reference is a person-to-person handoff.
- **Voice swap or merged timbre** between Audio 1 and Audio 2.
- **Two identity references for Mara** (Images 1–2) blending into inconsistent features across the clip.
- 12 seconds is duration *intent*; supported durations depend on the unselected runtime.

## 5. Revision ladder (one variable per step, keep everything else fixed)

1. If Ivo takes the case → strengthen only the 6–10s beat: "Ivo's hands remain at his sides throughout; only Mara touches the case." Stop if fixed.
2. If the case looks like Video 1's suitcase → add prop detail only (dimensions, latch count, brushed-brass finish) and re-run. If it persists, route to a still image of the case as a new prop reference.
3. If voices swap → drop to one audio reference at a time to isolate which binding fails, then reassert the mapping.
4. If Mara's identity drifts → drop Image 2, run identity from Image 1 alone; reintroduce Image 2 only if the coat detail degrades.
5. If the same defect survives two isolated changes → split into two shots (dialogue shot + placement insert) rather than lengthening the prompt.

**One blocking question before you run it**: which platform/model will this go to, and does Image 4 actually show a bench? Everything above stays valid either way — only the runtime parameter block and possibly the end-state anchor would change.
