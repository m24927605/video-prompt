# Root causes, minimal actions, and stopping rules

Read this file after recording direct evidence. Do not jump from a symptom to a fix without a bounded hypothesis.

## Diagnose in order

1. **Task/runtime** — wrong task family, asset role, prompt verb, hint, aspect/duration/format, model/platform assumption.
2. **Reference conflict** — ambiguous mapping, unintended inheritance, redundant/conflicting asset, weak state reference.
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
| Reference leakage | Add allowed/excluded inheritance for the offending asset | remove or rebuild that asset | separate roles across shots |
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

## One-variable action packet

```text
Observed defect and evidence:
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

Record last approved checkpoint, observed defects, tested hypotheses, spent time/cost and next route.
