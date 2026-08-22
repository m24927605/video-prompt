# Provenance — Seedance Video QC

Archived knowledge date: **2026-08-22**. Source paths are provenance labels, not dependencies.

| Rule | Distilled rule | Primary source and exact section | Evidence / boundary | Limitation or counterexample | Confidence |
|---|---|---|---|---|---|
| QC-01 | Establish evidence modality and sample opening/middle/end/transitions/high risk. | `long-form-film-workflow.md` Gate 6; `higgsfield-nine-projects.md` scope/§11–12; `qa-report.md` §1/§3–4 | Direct project inspection method. | Three frames cannot prove full motion/audio. | High |
| QC-02 | Label findings direct observation, inference or unknown. | `research-report.md` §1; Higgsfield evidence policy; `qa-report.md` §3–4 | Core research evidence discipline. | User reports remain reports unless corroborated. | High |
| QC-03 | Hard gates precede numeric scoring. | `prompt-playbook.md` §7; `long-form-film-workflow.md` Gate 6; `future-evaluation-plan.md` §9 | VBench/EntityBench-aligned method synthesis. | Numeric thresholds require project calibration. | High |
| QC-04 | Verify correct fidelity before self-consistency. | `future-evaluation-plan.md` §9.2–9.3; `additional-findings.md` F-16 | EntityBench-inspired method evidence. | Automated identity metrics require human calibration. | High method |
| QC-05 | Audit required/forbidden entities, reference roles, action, camera, sound and end state. | `prompt-playbook.md` §6–7; `long-form-film-workflow.md` §13.1 | Production framework. | Aesthetic quality cannot substitute. | High |
| QC-06 | Separate identity/wardrobe/injury/prop/location/space/light/voice/neighbor continuity. | `long-form-film-workflow.md` §5–7/§16; `research-report.md` §8 | Production framework. | Evidence scope may leave some dimensions unknown. | High |
| QC-07 | Match sampling density to temporal/anatomy/text risk. | `prompt-playbook.md` §7; `future-evaluation-plan.md` §9.1/§11; `creative-bible-analysis.md` page 11 | Research synthesis plus 16-frame heuristic boundary. | Sparse sampling misses fast hands/lips/short text. | High boundary |
| QC-08 | Inspect trajectory, contact, weight, inertia, result and camera coherence. | `research-report.md` §8; `long-form-film-workflow.md` §10.2; `future-evaluation-plan.md` §9 | Official weakness plus practice rubric. | Root cause remains inference absent controlled test. | High rubric |
| QC-09 | Evaluate observable acting cues, not emotion labels. | `research-report.md` §3.5; `creative-bible-analysis.md` pages 5/10; Higgsfield P03/P05/P06/P08 | Repeated author workflow. | Effect size unmeasured. | Medium |
| QC-10 | Evaluate camera/optics as narrative and continuity controls. | `research-report.md` §3.4; `prompt-playbook.md` §7; `long-form-film-workflow.md` §16 | Official vocabulary plus production practice. | Lens “feel” may be subjective without reference. | High practical |
| QC-11 | Check exact text/subtitle stability/timing; route persistent exact graphics to post. | `creative-bible-analysis.md` page 8; `long-form-film-workflow.md` Gates 8–10 | Official/practice direction. | Post route depends on delivery and rights. | High |
| QC-12 | Audio quality requires actual audio evidence; icon is insufficient. | `higgsfield-nine-projects.md` P02/§11; `qa-report.md` §3–4; `future-evaluation-plan.md` §11 | Direct bounded AV audit. | P02 did not establish Cantonese exactness, naturalness or phoneme sync; no generalization. | High |
| QC-13 | Diagnose upstream task→reference→state→space→physics→acting→audio/text→edit. | `research-report.md` §8; `prompt-playbook.md` §8; `long-form-film-workflow.md` §9.3 | Team diagnostic synthesis. | Case evidence can reorder competing hypotheses, but upstream gates still come first. | High practical |
| QC-14 | Change one variable and preserve working prompt. | `prompt-playbook.md` §9; `long-form-film-workflow.md` §10.1; `creative-bible-analysis.md` page 11 | Experimental hygiene. | Uncontrolled prior runs may not support causal claims. | High |
| QC-15 | Choose accept/edit/repair/regenerate/VFX/redesign. | `long-form-film-workflow.md` §10.2; `research-report.md` §8 | Production routing. | Expected cost/risk must use project evidence. | High |
| QC-16 | Enforce bounded stop conditions. | `long-form-film-workflow.md` §10.3; `future-evaluation-plan.md` §15.2 | Production and experiment safety. | No universal retry number; project policy only. | High |
| QC-17 | Compare variants with same rubric, blind where possible, ties allowed; metrics secondary. | `future-evaluation-plan.md` §8/§10–13; `long-form-film-workflow.md` §15 | Preregistered method design, not executed outcome. | Small samples/reviewer bias must be disclosed. | High method |
| QC-18 | Output verdict, severity, evidence, hypothesis, minimal change, route and stop. | Execution contract §4.3; `prompt-playbook.md` §7–9; `long-form-film-workflow.md` §10 | Contract plus research synthesis. | Verdict scope cannot exceed evidence. | High |

## Evidence cautions

- P02 is the only inspected Higgsfield asset with both brief and opened generation explicitly labeled 2.5. P04's brief says 2.5 but its sampled asset says `Seedance 2`; P07/P08 are 2.0; P09's burned label is not a backend ID.
- A UI `4k` badge, UI size, decoded dimensions and request resolution are distinct evidence.
- ModelArk archived documentation and Higgsfield outputs can differ in channels or post-processing; do not treat them as contradictions without platform evidence.
- `source-manifest.json` proves archival integrity, not the quality or causality of a workflow.
