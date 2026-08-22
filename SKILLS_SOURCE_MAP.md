# Seedance Skills Source Map

Archive date: **2026-08-22 (Asia/Taipei)**.

This is the suite-level index for the 53 non-obvious decision rules. It does not
repeat their complete wording. The maintained rule statements, limitations, and
confidence judgments live in each skill's provenance reference:

- [Prompt Director provenance](skills/seedance-prompt-director/references/provenance.md)
- [Film Producer provenance](skills/seedance-film-producer/references/provenance.md)
- [Video QC provenance](skills/seedance-video-qc/references/provenance.md)

Research paths are provenance identifiers, not runtime dependencies. Installed
skills must remain usable when `research/seedance-2.5/` is absent. Claims about
"current", "latest", or present availability require a fresh official-doc check.

## Full-read record

The Research Distiller read every line of all ten required final artifacts. No
original research, media acquisition, or paid generation was rerun.

| Required artifact | Lines | Bytes |
|---|---:|---:|
| `research/seedance-2.5/research-report.md` | 356 | 25,576 |
| `research/seedance-2.5/prompt-playbook.md` | 809 | 59,190 |
| `research/seedance-2.5/long-form-film-workflow.md` | 579 | 35,388 |
| `research/seedance-2.5/higgsfield-nine-projects.md` | 227 | 39,195 |
| `research/seedance-2.5/creative-bible-analysis.md` | 482 | 31,369 |
| `research/seedance-2.5/future-evaluation-plan.md` | 363 | 21,147 |
| `research/seedance-2.5/additional-findings.md` | 210 | 24,433 |
| `research/seedance-2.5/qa-report.md` | 81 | 10,354 |
| `research/seedance-2.5/source-manifest.json` | 2,686 | 126,206 |
| `seedance2.5-prompt-guide.md` | 1,106 | 65,090 |
| **Total** | **6,899** | **437,948** |

The execution contract was also read in full: `SEEDANCE_CROSS_AGENT_SKILLS_GOAL.md`
(362 lines, 16,903 bytes).

## Evidence classes

| Code | Class | Permitted use |
|---|---|---|
| `OF` | Official fact | Dated model, task, parameter, or platform claim within its documented surface. |
| `DO` | Direct project observation | Visible UI, timecoded frame, locally probed media, or other directly inspected evidence. |
| `AS` | Project-author self-report | Workflow or result reported in a project brief; never a controlled causal result. |
| `PR` | Peer-reviewed method evidence | General architecture or evaluation method; not a Seedance product capability. |
| `PX` | Preprint method evidence | Testable method hypothesis; not a Seedance internal or measured Seedance gain. |
| `TI` | Team inference | Bounded synthesis from stronger evidence, labeled as inference. |
| `PA` | Practice recommendation | Operational policy that still requires project calibration. |
| `U` | Unknown / pending verification | Not established at the required version, platform, or evidence resolution. |

Source aliases used below:

- `RR` — [research report](research/seedance-2.5/research-report.md)
- `PB` — [prompt playbook](research/seedance-2.5/prompt-playbook.md)
- `LF` — [long-form workflow](research/seedance-2.5/long-form-film-workflow.md)
- `HF` — [Higgsfield nine-project study](research/seedance-2.5/higgsfield-nine-projects.md)
- `CB` — [Creative Bible analysis](research/seedance-2.5/creative-bible-analysis.md)
- `FE` — [future evaluation plan](research/seedance-2.5/future-evaluation-plan.md)
- `AF` — [additional findings](research/seedance-2.5/additional-findings.md)
- `QA` — [research QA report](research/seedance-2.5/qa-report.md)
- `SM` — [research source manifest](research/seedance-2.5/source-manifest.json)
- `OG` — [official BytePlus prompt guide](https://docs.byteplus.com/en/docs/ModelArk/2607689), archived locally during the private research pass but not redistributed in this public repository

## Prompt Director index

| Rule | Topic key | Exact research sections | Classes / controlling boundary |
|---|---|---|---|
| PD-01 | Version/platform/task gate | RR §1.1–1.3; PB §0; HF §1 “Model version gate”; AF F-01/F-02/F-03/F-21; OG “Differences from Seedance 2.0” | `OF`, `DO`; project, UI label, and backend model identity stay separate. |
| PD-02 | Locked/unlocked routing | OG “Task instructions” and “Locked/Unlocked”; PB §1.2; RR §3.1; AF F-05/F-06 | `OF`; ModelArk roles and parameter gates are endpoint-specific. |
| PD-03 | Minimum intake | PB §1.1; RR §3; OG “Basic prompting techniques” | `PA`, `TI`; the eight-question intake is not an official mandatory form. |
| PD-04 | Production schema | PB §1.3; RR executive summary and §3; OG “Basic prompting techniques”; HF P03 | `OF`, `AS`, `TI`; structured blocks are not API weighting syntax. |
| PD-05 | Reference job/inheritance | OG “Reference tasks (multi-asset mapping)”; RR §3.2; CB page 4; HF P02/P03/P05/P08 | `OF`, `AS`, `PA`; effect size was not controlled. |
| PD-06 | Reference working range | OG “Reference asset input recommendations”; PB §1.5; RR §2.2; AF F-04 | `OF`; ModelArk ceilings do not transfer to Higgsfield or define a quality optimum. |
| PD-07 | Counts/spatial/first frame | RR §3.3–3.4; HF P02/P03/P05/P08; PB §5 comparisons B/C | `AS`, `DO`, `PA`; P04 supplies a direct subject-count counterexample. |
| PD-08 | One primary state delta | OG “Timestamps” and “Action and expression descriptions”; PB §1.4; CB page 10 | `OF`, `PA`; “one verb” is a heuristic, not literal prohibition of micro-actions. |
| PD-09 | Semantic timestamp budget | OG “Timestamps”; PB §1.4; AF F-23; HF P02; RR §2.3 | `OF`, `DO`; one 25s→29.056s case proves no general drift rate. |
| PD-10 | Physics/control-input boundary | RR §2.3 and §8; OG “3D clay-model reference/rendering”; AF F-18; HF P02/P04 | `OF`, `AS`, `TI`; limitation is strong, remedy magnitude remains untested. |
| PD-11 | Observable acting | RR §3.5; CB pages 5 and 10; HF P03/P05/P06/P08 | `AS`, `PA`; no controlled effect size. |
| PD-12 | Camera/light/grade separation | OG “Camera language”; RR §3.4; CB page 6 | `OF`, `PA`; not a required official section layout. |
| PD-13 | Dialogue/audio/language | RR §3.6; PB §1.7; AF F-12/F-17; HF P02 and §11; QA §3–4 | `OF`, `DO`, `U`; P02 does not establish Cantonese semantics, naturalness, or phoneme sync. |
| PD-14 | Positive constraints/precise bans | OG “Basic prompting techniques” and “Negative control”; RR §3.7; HF P01/P02 | `OF`, `AS`; P02 `no yellow` and P01 `NO ...` prevent a universal positive-only rule. |
| PD-15 | No invented capability/parameter | PB §1.6, §3, §10; AF F-02/F-04/F-09/F-10/F-12; RR §10; QA §3–4 | `OF`, `U`; current platform documents control current claims. |
| PD-16 | Edit/extend/first-last packets | OG “Locked” plus Edit/Extension examples; PB §2.2–2.4 and examples 15–19; RR §4; AF F-06/F-08/F-09/F-11 | `OF`; ~0.3/~0.4s edit tolerance and first/last mismatch wording remain explicit document conflicts. |
| PD-17 | Delivery/revision packet | PB §6–10; RR §8; CB page 11; execution contract §4.1 | `PA`, `TI`; no paid-generation validation occurred. |

## Film Producer index

| Rule | Topic key | Exact research sections | Classes / controlling boundary |
|---|---|---|---|
| FP-01 | Film hierarchy | RR §5; LF §0 and §3; CB page 14 | `OF`, `PR`, `TI`; hierarchy is external production structure, not model memory. |
| FP-02 | External memory | LF §0 and §4; CB page 9; RR §5.1 | `TI`, `PA`; does not deny platform reference/session conditioning. |
| FP-03 | Charter/rights/delivery | LF §1 and Gate 0; AF F-13/F-14/F-22 | `OF`, `AS`, `PA`; P06 contracts were not legally audited. |
| FP-04 | Versioned state passports | LF §2; CB pages 4–9; RR §9 | `AS`, `PA`; improvement magnitude is unmeasured. |
| FP-05 | Three continuity banks | LF §4; RR §5.1; AF F-11 | `OF`, `PX`, `TI`; return-last-frame is transport, not automatic approval. |
| FP-06 | Scene state/entity schedule | LF §5; FE §5.4 and §9.3 | `PX`, `TI`; Seedance-specific gain is untested. |
| FP-07 | Shot contract/provenance | LF §6; RR §5.2; CB page 15 | `PA`; not an API-mandated schema. |
| FP-08 | Coverage/high-risk split | LF §3.1 and Gate 2; RR §8; CB pages 8 and 10 | `OF`, `PA`; splitting adds editorial complexity but bounds model risk. |
| FP-09 | Relevant previz/anchors | LF §7 and Gate 3; OG storyboard/keyframe/clay sections; AF F-07/F-18 | `OF`, `AS`, `TI`; keyframes are relatively strict, not pixel locks. |
| FP-10 | Early rough cut/pickups | LF Gates 4 and 7; RR §5.3; AF F-20; HF P03/P05/P06/P08 | `AS`, `PA`; cross-case correlation is not causality or an optimal overlap ratio. |
| FP-11 | Finishing layers | LF Gates 8–10; RR §5–6; CB pages 14–15; HF §11 | `AS`, `PA`; raw generation is not final delivery. |
| FP-12 | Dependency-aware queue | LF §9 | `PA`; current platform concurrency still needs verification. |
| FP-13 | IDs/lineage/checkpoints | LF §12 and §17; CB pages 11/14/15; AF F-14 | `OF`, `PA`; never retain credentials or signed URLs. |
| FP-14 | Single-variable retry/route | LF §10; PB §9; CB page 11 | `PA`, `AS`; 10–15 and 15–20 are project heuristics, not model averages. |
| FP-15 | Extension boundary | RR §4.2–4.3; LF §10.2; AF F-11 | `OF`, `TI`; long-chain 2.5 drift magnitude remains untested. |
| FP-16 | Three operating modes | RR §6; LF §14; FE RQ5 and §5.5 | `TI`, `PA`, `U`; no mode is a proven global optimum. |
| FP-17 | Ledger-derived KPI | RR §7; LF §13; FE §12; AF F-19; HF §11 | `DO`, `PA`; aggregate project counters are not efficiency evidence. |
| FP-18 | Quality floors/Pareto | LF §15; FE §13.3–14 | `PA`, `U`; the evaluation design was not executed. |

## Video QC index

| Rule | Topic key | Exact research sections | Classes / controlling boundary |
|---|---|---|---|
| QC-01 | Evidence modality/sampling | LF Gate 6; HF opening evidence policy and §11–12; QA §1 and §3–4 | `DO`, `PA`; sparse frames cannot prove full motion or audio. |
| QC-02 | Observation/inference/unknown | RR §1; HF opening evidence policy; QA §3–4 | `DO`, `TI`, `U`; verdict scope cannot exceed evidence. |
| QC-03 | Hard gates before scores | PB §7; LF Gate 6; FE §9 | `PR`, `PX`, `PA`; numeric thresholds require project calibration. |
| QC-04 | Fidelity before consistency | FE §9.2–9.3; AF F-16 | `PX`, `TI`; automatic identity metrics require human calibration. |
| QC-05 | Contract adherence | PB §6–7; LF §13.1; FE §9.2 | `PA`; aesthetic quality cannot compensate for a missing contract item. |
| QC-06 | Continuity dimensions | LF §5–7 and §16; RR §8 | `PA`; unavailable dimensions remain unknown. |
| QC-07 | Risk-matched sampling | PB §7; LF §13.1; FE §9.1 and §11; CB page 11 | `PX`, `PA`; the 16-frame check is only a heuristic. |
| QC-08 | Physics/contact/inertia | RR §8; PB §7–8; LF §10.2; FE §9 | `OF`, `PA`, `TI`; root cause is a hypothesis without controlled isolation. |
| QC-09 | Acting evidence | RR §3.5; CB pages 5 and 10; HF P03/P05/P06/P08 | `AS`, `PA`; effect size is unknown. |
| QC-10 | Camera/optics function | RR §3.4; PB §7; LF §16; CB page 6 | `OF`, `PA`; subjective lens feel needs a reference or declared inference. |
| QC-11 | Text/subtitle routing | CB page 8; LF Gates 8–10; FE §11 | `OF`, `PA`; persistent exact graphics normally route to post. |
| QC-12 | Actual audio evidence | HF P02 and §11; QA §3–4; FE §11 | `DO`, `U`; an unmuted icon is not audio-quality evidence. |
| QC-13 | Upstream diagnosis order | RR §8; PB §8; LF §9.3 | `TI`, `PA`; observed evidence may reorder competing hypotheses after upstream gates. |
| QC-14 | One-variable revision | PB §9; LF §10.1; CB page 11 | `PA`; uncontrolled prior runs support no causal attribution. |
| QC-15 | Accept/edit/repair/regenerate/VFX | LF §10.2; RR §8; PB §8 | `PA`; expected cost and risk need project evidence. |
| QC-16 | Bounded stopping | LF §10.3; FE §15.2; CB page 11 | `PA`; no universal retry count. |
| QC-17 | Fair variant comparison | FE §8 and §10–13; LF §15 | `PR`, `PX`, `PA`, `U`; design is preregistered-method guidance, not an executed result. |
| QC-18 | Actionable QC packet | PB §7–9; LF §10; execution contract §4.3 | `PA`, `TI`; finding scope remains evidence-bounded. |

## Archive-integrity boundary

`SM` records `complete_with_explicit_unknowns`: four primary sources, ten
supplemental sources, 385 associations / 384 unique local files, and no open
research hard gate. This establishes archive integrity, not workflow causality,
success rate, or optimality. `QA` independently accepted the frozen research
state while preserving these boundaries:

- Source A is a complete browser capture, not an official export.
- Source B's supplied Markdown matches archived MDContent except one trailing
  line feed; its official PDF was unavailable and live remote middle/bottom
  inspection was partial.
- Higgsfield coverage is 9 projects and 14 directly opened media records;
  aggregate `All assets` / `Generations` counters were not individually audited.
- The 15-page Creative Bible is a third-party production document, not an
  official ByteDance or BytePlus model card.
- No credential, cookie/session data, signed query, or private media URL was
  retained in the frozen manifest.
