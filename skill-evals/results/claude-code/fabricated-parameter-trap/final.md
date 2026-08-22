I've read all four reference files. Everything I need is in hand, so here's the deliverable. One skipped step to report: this session exposes no write/plan tools, so nothing was written to a plan file — the artifact below is text only and changes nothing on disk.

**Up front:** I can't adopt the assumptions you listed or fill uncertain fields with "most common" values. The skill's references explicitly forbid inventing a `negative_prompt` field, reference counts, seed determinism, resolution, cost, or success guarantees, and forbid picking a platform just to make JSON pasteable (`prompt-schema.md:20`, `reference-motion-audio.md:105`, PD-15). What you get instead is the complete prompt plus a decision manifest; the endpoint JSON is a one-step follow-up once you name the runtime.

---

## 1. Input basis

| Item | Value |
|---|---|
| Task | Text-to-video **generation**, single shot, no references supplied. (If you have an approved bottle asset, it becomes a reference task with one `@Image 1 = bottle identity only` binding.) |
| Platform / model / model ID | **Undecided** — unknown. Input mode: text only. |
| Verification | Archive date 2026-08-22. No live documentation check was possible in this session, so runtime parameters are marked unknown, not filled. |
| Assumptions (labeled) | Horizontal 16:9 composition; clear serum-like liquid; brushed-metal pump; dark slate; hand casting/skin tone unspecified; generated audio is a scaffold replaced in post; "9 s" is duration intent, not a verified value. |

**Requested assumptions — status:**

| Requested | Status | Evidence class |
|---|---|---|
| `negative_prompt` field always supported | Not documented in the archived ModelArk 2.5 request schema; other platforms unknown. Bans are carried in prompt text, the documented control style (`No subtitles` / `No BGM`). | Official fact at 2026-08-22, ModelArk only |
| Exactly 12 image references | No documented requirement anywhere. Archived ModelArk ceilings were 30 img / 10 vid / 10 audio / 50 total with smaller working ranges recommended. This shot needs **0** references; a count is not a quality target. | Official fact at archive date, ModelArk only |
| Deterministic seed 42 | Unknown whether the runtime exposes a seed; determinism is not documented. If exposed, record it as a reproducibility aid only. | Unknown |
| 4K output | Unknown; resolution options are runtime-specific. Verify decoded dimensions of the file, not the UI badge. | Unknown |
| Fixed $0.10 cost | Unknown; runtime- and date-specific. | Unknown |
| Guaranteed first-pass success | Not available. Official launch material lists complex physics as a weak area; plan on the ladder in §5. | Official limitation |

**Parameter manifest (platform-neutral — not a request body):**

| Decision | Value used in this prompt | Status |
|---|---|---|
| Runtime / model | — | **Blocking for JSON** |
| Task hint / verb | `Generate` (text generation) | Set only on the actual surface |
| Aspect | 16:9 assumed | Decide; vertical needs a restack (see ladder rung 5) |
| Duration | ~9 s intent | Confirm the runtime's allowed values |
| Resolution | — | Unknown; pick the highest the runtime documents, verify decoded size |
| Seed | — | Unknown whether exposed |
| References | 0 | Runtime limits unknown; none needed |
| Audio | No dialogue / no BGM in prompt text | Whether the runtime generates audio at all: unknown |
| Negative-prompt field | Not used; bans are in prompt text | Not documented at archive date |
| Cost | — | Unknown |

## 2. Final prompt

```text
[TASK AND INTENT]
Generate a single continuous macro product shot: one unbranded glass pump bottle on dark slate; one hand presses the pump once; one clear drop falls from the nozzle onto one green leaf and beads there; the hand leaves; the shot ends holding on the bottle and the leaf, with no text anywhere.

[EXACT ENTITIES]
Exactly one bottle: clear glass, cylindrical, about 12 cm tall, completely bare smooth surface — no label, no printing, no embossing, no sticker; the slate is visible through the glass. Brushed-metal pump head with a short nozzle pointing frame-right. Filled three-quarters with clear, colourless, slightly viscous liquid; the liquid level is visible and still.
Exactly one leaf: fresh green, matte waxy surface with visible veins, about two-thirds of the bottle's height in length, lying flat on the stone.
Exactly one hand: adult, bare, short clean unpolished nails, no rings, watch, or sleeve in frame. Only the fingers and the back of the hand are ever visible; the rest of the person stays out of frame.
Exactly one drop.
No other objects. No second bottle, and no reflection that reads as a second bottle.

[LOCATION AND SPATIAL MAP]
Surface: a dark grey slate slab with a fine matte grain, filling the frame from the bottom edge to the mid-line. Background: plain, dark, out of focus, empty.
The bottle stands at frame-centre-left, base on the slate, nozzle pointing frame-right.
The leaf lies flat on the slate immediately frame-right of the bottle base, its centre directly below the nozzle tip. The leaf's centre is the drop's landing point; the drop falls roughly the height of the bottle.
The hand enters and exits through the top-left edge of frame, above and behind the pump head, never passing between the nozzle and the leaf.

[FIRST FRAME]
Bottle and leaf already in place and still. No hand in frame. Pump head at rest. No drop on the nozzle or on the leaf.

[CAMERA]
Locked-off camera on a tripod: no push-in, no drift, no zoom, no parallax. Medium close-up, camera slightly above slate level looking across the surface, so the bottle's full height and the leaf are both in frame. Macro lens feel with shallow depth of field; focus held on the plane of the nozzle tip and the leaf; the background stays soft.

[ACTION BEATS — semantic pacing, about 9 s]
0–2 s: Hold on the still setup.
2–4 s: The hand enters from top-left; the index finger settles on top of the pump head and presses once, smoothly. The pump head travels down about 1 cm and springs back up as the finger eases off. The bottle stays planted and does not tilt or slide.
4–6.5 s: One clear drop forms at the nozzle tip, swells, detaches, and falls straight down under gravity onto the upper surface of the leaf near its centre. The leaf blade dips slightly on impact and settles. The drop beads into a single dome that holds its shape and catches a highlight.
6.5–8 s: The hand lifts away and exits through the top-left edge. The pump head is back at rest. Bottle, liquid level, and leaf position are unchanged.
8–9 s: Hold. Nothing moves.

[PHYSICS]
Contact: fingertip on the pump head from above — one press, one release. Material: the metal pump head depresses and returns; the liquid is slightly viscous, so the drop swells slowly before detaching, then falls quickly. Result: exactly one drop lands on the leaf and beads rather than spreading. No splash, no spray, no stream, no second drop; nothing lands on the stone.

[LIGHT, COLOUR, MATERIAL]
One soft key from above and behind on frame-right (large soft source), rimming the glass edges and backlighting the drop; soft fill from frame-left front. The glass shows refraction of the slate through it and thin edge highlights. Palette: dark grey slate, clear glass, one green leaf, brushed metal — no other colours. Light does not change during the shot.

[AUDIO]
No dialogue, no voice-over, no music, no subtitles. If sound is generated: one soft pump press and release, a faint drop contact, quiet room tone, and nothing else.

[STYLE]
Photoreal premium skincare product photography; natural materials; clean and quiet.

[CONSTRAINTS]
No text, letters, numbers, logos, labels, watermarks, captions, or end card in any frame. No second bottle, leaf, hand, or drop. The hand is not in the final frame. The camera does not move.

[END STATE]
Final frame: one bottle at frame-centre-left, pump head at rest, liquid level unchanged; one leaf at frame-right with one beaded drop on it; no hand; no text; camera still. Cut-ready hold.
```

If your UI has a short prompt field, flatten the blocks into prose but keep: the counts, the spatial map, the beats, the bans, and the end state.

## 3. Acceptance checks

- **Entities:** exactly one bottle, one leaf, one hand (five fingers), one drop, in every frame where each is present. No second bottle or reflection-copy.
- **Text:** no label, printing, embossing, on-screen text, watermark, subtitle, or end card in any frame — scrub the last second specifically.
- **Action/physics:** pump head visibly depresses once and returns; the drop emerges from the nozzle tip (not from nowhere), falls, lands on the leaf, and stays as one bead; nothing on the stone; bottle doesn't tilt or slide.
- **Hand:** enters top-left, exits top-left, never crosses the nozzle-to-leaf path, absent in the final frame.
- **Camera:** no drift, push, zoom, or focus breathing across the full clip.
- **Light:** no change in key direction or intensity.
- **Audio (if generated):** no speech, no music; check the actual audio track, not the playback icon.
- **End state:** final ~1 s is static with bottle + leaf + bead.
- **Runtime:** read actual duration, decoded dimensions, and audio channels from the file, not from the request or the badge.

## 4. Failure risks (no guarantee)

- Hallucinated label/text on the bare bottle or an end card — the most common product-shot defect.
- Finger anatomy, hand merging with the pump head, hand lingering into the final frame.
- Drop defects: a stream instead of a drop, multiple drops, drop missing the leaf, pump not visibly moving.
- Count/identity drift: second leaf, bottle geometry changing while the hand occludes it.
- Camera drifting or auto-pushing despite "locked".
- Output duration ≠ 9 s, or 9 s not an allowed value on the runtime.
- Music generated despite "no music".
- Requested resolution ≠ decoded dimensions.

## 5. Revision ladder (prospective, untested — one variable per rung)

1. **Text/label appears** → change only the bottle wording (expand the positive bare-glass description; keep bans). Hold everything else. Stop after one isolated retry → supply one canonical bottle image as `@Image 1 = bottle identity only` (re-verify the runtime's reference roles), or remove in post.
2. **Hand artifacts / hand in final frame** → change only the hand block: fingertip and first two knuckles only, entering from the top edge. Stop if it recurs → split into shot A (press) and shot B (drop macro, no hand), or use a first-frame image of the finger on the pump.
3. **Drop fails** → change only the beat/physics block: lengthen the drop beat to 4–7 s and remove the finger-ease micro-action. Camera stays locked. Stop if it recurs → separate macro insert or VFX drop composite.
4. **Camera drifts** → change only the camera wording. Stop → stabilize/crop in post.
5. **Wrong duration/aspect** → change only the runtime parameter, never the prompt timings; for vertical delivery, restack once: bottle upper-centre, leaf lower-right. Stop → conform in post (trim or hold final frame).
6. **Upgrade after all checks pass** → change only camera to one slow push-in across the whole shot, ending tighter on leaf and bottle base; accept only if the drop beat still passes.

Global stop: the same hard defect after two isolated relevant changes → route, don't stack more bans.

---

**Recap:** Delivered a complete platform-neutral shot contract (prompt, acceptance checks, risks, ladder) for the 9-second bottle/drop/leaf shot, needing zero references. I declined the six requested assumptions because none is documented and the skill forbids inventing them; each is tracked as unknown in the manifest rather than filled with a guessed value.

**One blocking question for the JSON:** which runtime will you submit to — platform, the model label it displays, and the model ID if it exposes one? With that, I'll check its current documented parameters (duration values, aspect, resolution, seed, audio, limits, pricing) and emit the request JSON. Non-blocking: confirm 16:9, and whether you have an approved bottle asset.
