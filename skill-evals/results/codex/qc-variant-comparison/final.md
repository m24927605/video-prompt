## Verdict

Select **Variant A** — no tie.

- **A: CONDITIONAL PASS.** All story and continuity hard gates pass on the supplied report. Its defects are local and repairable.
- **B: FAIL.** It breaks three continuity-critical requirements. Better camera movement cannot offset failed hard gates.

| Hard gate | Variant A | Variant B |
|---|---|---|
| Correct courier and red coat | Pass, reported | Unknown |
| One sealed silver case | Pass, reported | **Fail:** opens at `00:06` |
| Case remains in right hand | Pass, reported | **Fail:** shifts to left hand |
| Left-to-right travel | Pass, reported | Unknown |
| Ends at blue door | Pass, reported | **Fail:** door is green |
| Required end state | Pass, reported | **Fail** |

## Evidence classification

**Direct reviewer observations:** None; no clips or frames were supplied for independent inspection.

**User-reported observations used for this decision:**

- A preserves the courier, coat, case count, direction, and required end state.
- A’s push-in is slower than requested.
- A has a small four-frame reflection flicker.
- B’s case opens at `00:06`, transfers to the left hand, and ends at a green door.
- B has stronger camera movement and no reported flicker.

**Hypotheses:**

- A’s flicker is probably localized temporal/reflection instability and suitable for a short paint or clean-plate patch.
- B likely suffers broader entity-state and location-continuity drift. Whether that arose from prompt ambiguity, reference conflict, or generation instability is unknown.
- A’s slower push-in may be correctable with a keyframed crop if resolution and framing provide enough margin.

## Minimal repair route

Use **A → edit/VFX repair**, not regeneration.

1. Change only the four flickering frames: patch the reflection from adjacent clean frames.
2. Hold fixed the courier, red coat, sealed case geometry, right-hand contact, motion direction, timing, and blue-door ending.
3. Accept the slower push-in if camera speed is a preference rather than a delivery gate.
4. If exact speed is mandatory, test a separate keyframed digital push-in after the flicker repair. Do not retime subject motion unless required.

Pass condition: the reflection remains stable at native frame rate with no ghosting, duplicated case, or altered hand contact.

Stop after one local cleanup pass and, if necessary, one isolated camera-speed pass. Reject any repair that disturbs a hard-gate element.

## Evidence still needed

Selection does not require more evidence, but final approval needs:

- Both native-resolution clips and their frame rates.
- Exact frame range of A’s flicker and dense frame inspection around it.
- A’s opening, hand-occlusion moments, and final frames to verify the case stays sealed, silver, and in her right hand continuously.
- B frames around `00:05–00:07` and the final frame to confirm the reported failures.
- Camera-speed tolerance plus delivery resolution/crop margin.
- Original prompt, references, model/platform/version, and settings only if root-cause diagnosis is required.
