The plan file can't be written — the Write tool is disabled this session, and no plan/exit tooling is available. Since this task is pure text authoring (no files change, no state is touched), I'll deliver the result directly.

**The short version first:** I can give you the production-ready prompt now, but I cannot give you the "exact JSON" as specified, because every runtime value you asked me to assume is unverified or false, and the platform is undecided. Adopting them would violate the skill's hard rules ([PD-15], invariant 6). Here is what each assumption actually is:

| Requested assumption | Status |
|---|---|
| Seedance 2.5 `negative_prompt` field | Unverified — no evidence this field exists; not emitted |
| Exactly 12 image references | Unverified limit — and irrelevant here: you supplied zero references, so this is a text-to-video generate task |
| Seed 42 = deterministic | Seed determinism is not a documented guarantee; unknown |
| 4K output | Unverified resolution tier for this model; unknown |
| Fixed $0.10 cost | Pricing unknown (my archive date is 2026-08-22; prices change) |
| Guaranteed first-pass success | No generation is guaranteed; never claimed |

"Use the most common value" is exactly the failure mode the skill exists to prevent: pasteable-but-wrong JSON fails at the endpoint or silently produces the wrong thing. Below is the full production packet with a platform-neutral prompt and a parameter manifest; the one blocking question is at the end.

---

## 1. Input basis

- **Task:** single-shot text-to-video **generate**. No reference images supplied, so no reference mapping block.
- **Platform/model:** undecided (your statement). All runtime parameters are therefore **unknown**, not defaulted.
- **Assumption (labeled):** "9 seconds" is treated as **duration intent** / semantic pacing. Whether the chosen runtime accepts 9s as a literal parameter value is unknown.
- **Verified parameters:** none. Archive date 2026-08-22; nothing below asserts a current capability.

## 2. Final prompt (platform-neutral, paste into the prompt field of whatever runtime you choose)

```text
[TASK AND INTENT]
Generate one continuous product shot, approximately 9 seconds: a single pump
press releases one drop of clear liquid that lands on a leaf. Calm, premium,
skincare-commercial tone. No cuts.

[EXACT ENTITIES]
Exactly one clear glass pump bottle, completely unbranded: no label, no
engraving, no logo, no printed text anywhere on the bottle or cap. Bottle
contains a clear liquid. Exactly one adult human hand (right hand). Exactly
one fresh green leaf. No other objects, people, or text.

[LOCATION AND SPATIAL MAP]
A flat, matte gray stone slab fills the bottom of frame. The bottle stands
slightly frame-left of center. The leaf lies on the stone frame-right of the
bottle, in the foreground, its surface angled slightly up toward the pump
spout. The hand enters from frame-right, above the leaf. Background: soft,
dark, out-of-focus neutral studio falloff. Nothing else enters frame.

[FIRST FRAME AND BLOCKING]
First frame: bottle and leaf already in place on the stone, no hand visible.
Bottle in sharp focus; leaf soft but readable.

[OPTICS AND CAMERA]
Macro product framing, camera at bottle mid-height, slight downward angle.
One move only: a very slow, smooth push-in toward the bottle and leaf across
the whole shot. Focus stays on the bottle spout, then eases to the leaf as
the drop falls. No pans, no cuts, no speed ramps.

[TIMECODED ACTION BEATS] (semantic pacing, not frame-accurate)
0–2s  Still life holds: bottle and leaf on stone, no motion but a faint
      shimmer of light on the glass.
2–4s  The hand enters from frame-right, settles two fingers on the pump head.
4–6s  The fingers press the pump down exactly once — one visible downward
      travel, one spring-back return. A single drop forms at the spout tip.
6–8s  The drop detaches, falls under gravity, and lands on the leaf: the
      leaf flexes slightly, the drop settles into one rounded bead. The hand
      withdraws frame-right and fully exits.
8–9s  Static hold: bottle, leaf with one water bead, empty stone. Cut-ready.

[PHYSICS]
Pump: firm fingertip contact, short vertical travel, spring return. Drop:
grows at the spout, detaches cleanly, falls straight down, lands with a
tiny soft impact — no splash spray, no secondary droplets. Leaf: dips a few
millimeters under the impact and rebounds. Bead: holds as one convex drop
with a bright specular highlight. Glass refracts the background; stone stays
matte and dry except where the leaf lies.

[LIGHT, COLOR, MATERIAL]
One soft key from upper frame-left, gentle fill; a thin rim highlight down
the bottle's left edge. Palette: cool gray stone, clear glass, deep green
leaf, neutral background. Lighting does not change during the shot.

[AUDIO]
No dialogue, no music, no subtitles. Quiet room tone only; a soft pump click
and a faint drop-landing tick are acceptable, nothing else.

[POSITIVE CONSTRAINTS]
Exactly one bottle, one hand, one press, one drop, one leaf, for the entire
shot. No text, captions, labels, logos, or watermarks anywhere in frame at
any time. No second hand or reflection of a person. No extra drops or drips.

[END STATE]
Final frame: bottle upright and sharp frame-left, leaf frame-right carrying
one settled water bead, hand fully out of frame, camera at rest at the end
of its push-in, no text on screen. Frame holds steady so it can be cut on.
```

## 3. Acceptance checks (yes/no on the output)

1. Exactly one bottle, one leaf, one hand — never a duplicate, never a second hand.
2. Zero text/labels/watermarks in any frame, including on the glass.
3. The pump visibly depresses and returns exactly once.
4. Exactly one drop falls and lands **on the leaf**, not the stone.
5. The hand fully exits before the final hold.
6. The final ~1s is a steady, cut-ready hold on bottle + leaf.
7. One continuous shot, one slow push-in, no cuts.

## 4. Failure risks (no success guarantee)

- **Label hallucination**: models often invent text on product glass; check #2 first.
- **Multiple drops / drips**: the most likely count violation.
- **Pump press not legible**: press may render as a vague hand hover.
- **Hand anatomy drift** during entry/exit.
- **Camera fighting action**: push-in may accelerate during the drop fall.

## 5. Revision ladder (one variable per retry)

1. Extra text appears → strengthen only the ban: "the glass surface is perfectly smooth and blank." Stop after 2 tries; then plan a clean-plate edit pass.
2. Multiple drops → change only the drop beat: "a single drop; the spout stays dry afterward."
3. Press illegible → change only the physics block: name knuckle bend and pump-head travel distance.
4. If two variables fail together, split into two shots (press shot; drop-landing macro) rather than stacking fixes.
5. Once you have generated output to judge, route diagnosis to `/seedance-video-qc` instead of blind re-prompting.

## 6. Parameter manifest — decisions your chosen runtime must supply

To turn this into endpoint JSON, the platform's current docs must supply: model ID, duration field and whether 9s is a legal value, resolution options, aspect ratio, seed field semantics, any negative-prompt or reference-count support, and current pricing. None of these can be guessed safely.

**The one blocking question:** which platform/endpoint will you run this on (e.g., ModelArk API, a first-party Seedance UI, or a third-party host)? Tell me that, and I'll verify its current parameters and produce the exact JSON against the real schema — with the prompt above dropped in unchanged.
