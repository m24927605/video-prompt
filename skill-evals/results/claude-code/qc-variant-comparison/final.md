**Verdict: Select Variant A (conditional pass). Variant B fails three hard gates and is not a tie candidate regardless of its camera work.**

One caveat up front on evidence modality: I have no video files or frames in this session — everything below is graded from your reported symptoms. Where I say "direct observation," I mean "as observed in your review notes"; none of it is independently frame-verified by me yet, which is why the missing-evidence list matters.

## Hard-gate results

| Gate | Variant A | Variant B |
|---|---|---|
| Correct entity: one courier, red coat | Pass | Pass |
| Prop count/state: one **sealed** silver case | Pass | **Fail** — case open at 00:06 |
| Direction: left-to-right | Pass | Pass |
| End state: blue door | Pass | **Fail** — door is green |
| End state: case in **right** hand | Pass | **Fail** — shifts to left hand |
| No uneditable structural failure | Pass (flicker is local, 4 frames) | Pass |

A's two defects — slower-than-requested push-in and a four-frame reflection flicker — are adherence and temporal-stability deviations, not gate failures. Neither breaks entity, story beat, or end state. B's defects are exactly the continuity-critical prop-state, hand-ownership, and location facts the contract names, so they cannot be averaged away by camera quality.

## Direct observations vs. hypotheses

Reported observations (treat as direct pending frame verification):
- A: push-in speed below the requested rate; reflection flicker lasting 4 frames (timecode not yet recorded); all contract facts held.
- B: case transitions sealed → open around 00:06; case ends in left hand; final door green.

Hypotheses (not demonstrated):
- B's open case + hand switch likely share one upstream cause: the prompt's case-state and hand-ownership constraints were under-specified for the mid-clip beat, letting the model "animate" the prop. The green door is plausibly a separate color-binding drift (red coat competing with blue door in the color palette). These are inferences about cause, not observed facts.
- A's flicker is likely a reflection/specular instability, which is usually local and paintable; whether it's visible at delivery frame rate is unknown until viewed at speed.
- A's slow push-in is plausibly a camera-speed phrasing issue in the prompt, but it could also be duration/pacing interaction. Unknown until the prompt and spec are compared.

## Selection

**Variant A**, not a tie. Scoring order puts hard gates and prompt adherence above camera aesthetics; B fails three gates (prop state, hand, door color) that would each require repair, and fixing three coupled facts means a full regenerate — at which point B's advantage evaporates. A is editorially usable as-is or with a small repair.

## Minimal repair route for A

1. **Flicker (4 frames): edit/repair route.** Paint-out or clone the reflection region from adjacent stable frames. At 24 fps this is ~0.17 s in a static region — low-cost VFX, no regeneration. Do this first; it may be the only fix needed.
2. **Slow push-in: decide by acceptance criteria, don't auto-regenerate.**
   - If camera speed is *not* a hard requirement, **accept** A with the flicker repair.
   - If it is, the cheapest edit-side option is a modest digital push (scale animation) to augment the move — costs some resolution, doesn't touch any passing gate. A retime is riskier because it also speeds up the courier's walk.
   - Only if edit-side fixes are rejected: **regenerate with exactly one changed variable** — explicit camera-speed language (e.g., a concrete push-in rate or "reaches MCU by 00:0X") — holding courier, coat, case, direction, door color, and hand as stated invariants. Route the wording change through prompt revision.
   - **Stop condition:** cap at 2 regeneration attempts for camera speed. If speed oscillates or a new gate fact breaks, fall back to A + edit repair.

Do not attempt to repair B; three coupled gate failures make it a regenerate-or-discard, and A already exists.

## Evidence still needed

- **Frame verification of both clips**: opening, middle, and final frames of A and B; the exact timecode + 4 frames of A's flicker; B's 00:05–00:07 window (to confirm the case-opening moment and whether the hand switch happens there too or later).
- **Dense sampling of A's case state** across the full duration — "sealed throughout" needs more than start/end frames, since B shows this model can drift mid-clip.
- **The quantitative camera spec**: what push-in speed was requested and how far A falls short, plus whether camera speed is a hard gate in this project's acceptance criteria.
- **A's flicker viewed at delivery frame rate and compression** — it may be invisible in playback, changing the repair from "do it" to "skip it."
- **Platform/model/version, parameters, and seed documentation** for both runs, needed if a regeneration is attempted and for comparability claims.
- **Neighbor-shot requirements**: does the next cut depend on the final framing size the faster push-in would have produced? If yes, the digital-push option becomes more attractive.
- **Audio**: the contract as stated says nothing about audio; if there is an audio requirement, neither variant has been evaluated on it — currently unknown.

Note: I'm in plan mode with read-only tools, so this is the assessment deliverable; no files were changed. If you want, next step I can turn the camera-speed fix into a bounded prompt revision via the prompt-director workflow once you confirm whether push-in speed is a hard requirement.
