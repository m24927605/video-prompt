# Revision and failure patterns

Read this file when reviewing or repairing a prompt, or when the first draft is overloaded.

## Detect overload before generation

Split or simplify when any condition is true:

- more than one primary state change must complete in a shot;
- several characters perform independent contact actions at once;
- camera, subject, light, scene, and style all transform together;
- the prompt depends on exact text, fine fingers, dense crowds, or long dialogue while also demanding complex motion;
- an asset is asked to control incompatible roles;
- the end state is implicit or incompatible with the next shot;
- a time segment contains more events than can remain legible.

Prompt length is not a quality proxy. Keep information that changes model decisions; move production memory and history into assets/state/ledgers rather than prose.

## Diagnose upstream first

| Failure | First hypothesis | Minimal test | Escalation route |
|---|---|---|---|
| API/task error | role, hint, verb, ratio/duration/format mismatch | align the one mismatched task control | current official docs / endpoint probe |
| Wrong/missing entity | mapping or count ambiguity | rewrite one binding/count; keep all else | cleaner canonical asset or split shot |
| Lateral flip of an asymmetric attribute | side named once, or left implied | restate the side at each mention; hold all else | isolate the attribute in an insert, or mirror-correct in post |
| Reference leakage | one asset controls unintended properties | add allowed/excluded inheritance or remove that asset | rebuild asset by role |
| Identity/state drift | mixed state, weak asset, too many subjects | return to one approved state asset | shorten, reduce cast, composite |
| Spatial/axis error | under-specified first frame or landmarks | add one layout/axis and exact positions | master/insert split, reframe |
| Physics/contact failure | too many actions or competing camera | lock camera and keep one causal event | keyframe/blockout, split, VFX |
| Rigid acting | adjective without tasks or timing | add gaze/hands/reaction cue | separate reaction shot |
| Audio/dialogue failure | speaker/language/timing ambiguity | one speaker with exact line and silence rules | picture-only + ADR/dubbing |
| Text failure | model asked to generate precise graphics | isolate short static text test | graphic composite |
| Edit spill | scope/preserve list unclear | A→B + exact scope + preserve list | splice approved edit region into source |
| Extension drift | rejected boundary promoted | return to last approved checkpoint | independent hard-cut shot |
| Neighbor mismatch | end state/handoff incomplete | repair the one state/direction/level mismatch | cutaway, pickup, re-edit |

Root-cause labels remain hypotheses unless a controlled one-variable test demonstrates them.

## Causal and contradiction audit

Before drafting or repairing, read the shot in causal order: trigger before reaction, and contact before response. For dialogue, reserve a listening/breath/reaction budget so a listener can register the line before their answer or physical response. [PD-10] [PD-11] [PD-13]

Resolve these contradictions before generation; if both outcomes are required, split the shot or choose one constraint:

- one-take vs cuts;
- fixed camera vs viewpoint jump;
- no-two-shot constraint vs a requested shoulder or reflection that reveals the second person;
- fixed distance vs face-filling framing;
- third-person view vs character-owned camera;
- no BGM vs score;
- protected source vs restyle;
- changed outcome vs stale constraints in the action, camera, sound, continuity, or end state.

## One-variable ladder

Preserve the working prompt. Each rung states one changed variable, fixed invariants, predicted diagnostic signal, and stop condition.

Build the prompt so a one-variable rung is mechanical rather than disciplined. Keep the parts that must not move—the reference contract, the invariants, the audio contract, the exclusions—as separable named blocks, carry them to the next rung byte-for-byte, and let the rung change one block, or one line inside one block. Record the ladder's fixed list as the names of the blocks held identical, not as a re-description of their contents: a rung that retypes an invariant has already changed more than one variable.

Resubmitting identical text with identical parameters is not a rung. It samples the generator's variance and tests no hypothesis. Record it as a sample count against the parent rung—how many draws, what the spread was—rather than as a step in the ladder, so the ladder keeps meaning one change per line. Sampling and one-variable testing answer different questions; neither substitutes for the other, and this skill takes no position on which spends a budget better.

```text
Run / parent:
Observed defect and timecode:
Evidence class: direct observation / inference / unknown
Changed variable:
Fixed prompt, references, task parameters, and shot design:
Hypothesis:
Expected observable improvement:
Acceptance gate:
Actual result:
Decision: approve / retry / edit / VFX / redesign
```

Do not simultaneously change prompt wording, reference set, duration, resolution, and shot design. If the user has no run ledger, provide the ladder prospectively and label it untested.

## Stopping conditions

Set a ceiling from project budget, clock, and risk; do not import a universal retry number. Stop generation and route when:

- the same hard defect recurs after isolated relevant changes;
- fixing one critical constraint repeatedly breaks another, creating oscillation;
- the time/cost ceiling is reached and another route has lower expected loss;
- continuity would require using a rejected or drifted output as reference;
- rights, safety, platform, or delivery gates cannot pass.

Stopping means preserving the last approved checkpoint, failed hypothesis, evidence, and next route—not discarding history.

## Compact repair output

```text
Input basis
- Task/platform/model/date:
- Assumptions:
- Verified parameters:
- Unknowns:

Failure diagnosis
- Direct evidence:
- Root-cause hypothesis:
- Competing hypothesis:

Repaired final prompt
[production-ready prompt]

Acceptance checks
- ...

Revision ladder
1. Change only ...; hold ...; stop/route if ...
2. If the defect persists, change only ...
```
