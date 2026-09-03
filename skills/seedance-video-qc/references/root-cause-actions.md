# Root causes, minimal actions, and stopping rules

Read this file after recording direct evidence. Do not jump from a symptom to a fix without a bounded hypothesis.

## Locate the defect before choosing its level

A defect's distribution is diagnostic and is cheaper to establish than any hypothesis about its cause. Test three axes:

1. **Across takes** — re-firing the identical text with identical parameters changes no variable and varies only the sample. This is a control run, not a wasted retry. A defect that survives N identical re-fires is contract-determined and routes to a rewrite, a split, or another route; a defect that appears in some samples and not others is sampling variance and routes to selection among takes under a declared take budget, never to a rewrite. Without a control, a defect cannot be attributed to the prompt at all.
2. **Across the clip** — a defect confined to an interval is a repair, insert or trim candidate. A defect present in every frame is contract- or model-level and has no local repair route.
3. **Across the frame** — a defect confined to a region is a repair, cutaway or composite candidate. A defect present everywhere in the rectangle is not.

Record the distribution in the finding. `Change only: nothing (control run, N samples)` is a valid action packet entry, and the ceiling that bounds it is a take budget, not a rewrite budget. [QC-25]

## Diagnose in order

1. **Task/runtime** — wrong task family, asset role, prompt verb, hint, aspect/duration/format, model/platform assumption; text and parameters disagreeing on timing, length or take structure, or a schedule that over-books the requested runtime. [QC-24]
2. **Reference conflict** — test the binding before the inheritance: an asset may be unused, misbound to the wrong entity, conflated with another, or correctly bound but over-inherited. Then audit inheritance channel by channel, since leakage usually appears on a channel the reference was never granted. Ambiguous mapping, redundant/conflicting asset, and weak state reference sit under the same step.
3. **Entity/state** — wrong count/identity, mixed wardrobe/injury/weather/prop state, ownership or end-state omission.
4. **Space/camera** — missing first-frame occupation, landmarks, axis, eyelines, directions, or competing movement.
5. **Physics/action** — too many state changes, no contact causality, impossible body/material burden, camera masking action.
6. **Acting** — emotion adjective without gaze/hands/reaction timing/tactic.
7. **Audio/text** — speaker/language/timing ambiguity, generated text burden, missing real audio evidence.
8. **Neighbor edit** — end state, action/camera vector, light or room-tone mismatch.

Higher upstream failures invalidate lower-level polish work.

## Symptom-to-action matrix

| Symptom | First minimal action | If repeated | Final route |
|---|---|---|---|
| Wrong task/error | Align one mismatched role/verb/hint/parameter from current docs | endpoint probe | stop until runtime contract is known |
| Missing/extra entity | Add exact count/required/forbidden line | cleaner single-role asset, reduce cast | split/composite |
| Identity/wardrobe drift | Return to one approved state-specific canonical asset | shorten shot or isolate character | identity composite/2D/3D/live action |
| Reference leakage | Name the channel that leaked, then add allowed/excluded inheritance for the offending asset on that channel | remove or rebuild that asset | separate roles across shots |
| Spatial/axis failure | Add first-frame occupation, landmarks, camera side and end positions | use floor plan/diagram/master | reframe/cutaway/new coverage |
| Hands/contact | Lock camera and keep one interaction | keyframe/blockout, split into inserts/reactions | traditional VFX/3D/practical |
| Wrong physics/material | State contact→force→inertia/material→result | state asset or blockout | simulation/composite/redesign |
| Rigid acting | Add one gaze/hand/reaction timing cue | separate reaction shot | editorial performance reconstruction |
| Edit spill | State sole master, A→B, exact scope and preserve list | use only approved changed interval | roto/paint/key/composite |
| Extension drift | Return to last approved checkpoint + canonical context | shorten continuation | independent hard-cut shot |
| Wrong dialogue/lip | One speaker, exact language/line, silent others | picture-only generation | ADR/dubbing/lip tool |
| Text/subtitle failure | Isolate short static requirement | clean plate + tracking | graphic/subtitle composite |
| Audio seam | Match room tone/perspective/level intent | crossfade/mix | replace generated soundtrack |
| Neighbor mismatch | Repair the one end-state/vector/light/level mismatch | insert/reaction/cutaway | pickup/re-edit |
| Unrequested damage or feature appearing where the contract bounded it by number | Restate the bound as the object, the place on it, and the surface that stays whole | Give each object its own sentence naming its state | Isolate the object in its own shot or insert |
| Defect on an attribute the contract appears to forbid | Read that clause standing alone before charging the model | Resolve every pointer in it to a literal value | Contract rewrite, not another take |

**An inert clause is a contract defect, not a take failure.** Before filing a prohibition as violated, read it by itself with nothing else in view. A clause that points at a document not submitted with it — *the listed items*, *the rest*, *that area*, *the master* — never bound anything, because nothing at the other end of the pointer reached the generator; report it the way a contract that over-books its own runtime is reported, as a defect of the text routed to a rewrite, and expect no number of retries to change it. A clause that bounds a diffuse feature by how many there are — *no second one*, *only one of them* — carries a weaker warrant: it rests on an uncontrolled observation of such a bound leaving the feature free, not on a controlled comparison, so record it as suspected inert, restate the bound as a place and an edge, and say in the finding that the rewrite is precautionary. Either way, charging the clause to the model before reading it alone is a misdiagnosis that spends the take budget on nothing. [QC-28]

Edit spill is diagnosed only after the job has been inspected as a differential against its source; see the delta-edit dimension in the inspection rubric. [QC-27]

## One-variable action packet

```text
Observed defect and evidence:
Defect distribution across takes / clip / frame:
Root-cause hypothesis:
Alternative hypothesis:
Change only:
Hold fixed:
Expected diagnostic signal:
Pass/fail condition:
Next route if failed:
```

Changing prompt, reference, duration, resolution and shot design simultaneously destroys attribution. Preserve the last working prompt and parent run.

## Choose the route

- **Accept** when all hard gates pass and residual defects are inside the agreed floor.
- **Edit/repair** when the approved performance/state is usable and the defect is local, bounded and cheaper to fix.
- **Regenerate** when the model-suitable core contract failed and one testable upstream change remains.
- **VFX/composite** for persistent text, hands/contact, local identity, keying, geometry, physics or cleanup problems.
- **Redesign/split** when shot architecture overloads the model or retries oscillate.

Do not use “regenerate” as a default. Compare expected loss, human time and continuity risk.

## Stop conditions

The project sets numeric ceilings; research heuristics such as 10–15 retries are not universal.

Stop generation when:

- the same blocking defect survives isolated relevant retries;
- solving one critical requirement repeatedly breaks another;
- budget/time ceiling is reached;
- further progress requires a rejected or drifted frame as truth;
- rights, policy, platform or delivery cannot pass;
- a mature edit/VFX/ADR/graphics route has lower expected cost/risk.

A retry counts as isolated only where it was controlled. State how many samples were taken and whether the text and parameters were unchanged; an uncontrolled retry sequence cannot support the repeated-defect stop condition. [QC-25]

Record last approved checkpoint, observed defects, tested hypotheses, spent time/cost and next route.
