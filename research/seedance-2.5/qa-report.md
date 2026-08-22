# Final QA report

> Audited: 2026-08-22 (Asia/Taipei)  
> Final recommendation: **PASS — ACCEPTED FOR COMPLETION**. The non-acquiring freeze-state reviewer returned PASS with zero blocking findings. Source B passes under the user's explicit full-Markdown amendment; all C visual-coverage gates are closed; one direct Seedance 2.5 generation has a bounded local AV audit with high-resolution audio qualities kept as explicit unknowns rather than invented passes.

## 1. Requirement matrix

| Requirement | Result | Evidence / exact gap |
|---|---|---|
| Required root + 3-agent configuration | PASS | Root runtime metadata reports `gpt-5.6-sol` / `ultra`; all three subagents were launched explicitly with the same model/effort and separate ownership. |
| A viewed in visible real Chrome | PASS | Live top/middle/bottom, overlap-scroll harvest and offline reopen evidence under `browser-evidence/official-docs/`. |
| A full archive, not summary | PASS | 57,053 plain-text chars; 512 blocks over IDs 2–513 with zero gaps; 9 tables; 110 code/pre nodes; searchable text, rich HTML and offline HTML. |
| A site-provided export | Not obtainable, declared | Anonymous UI exposed no export/download action. The complete browser-derived copy is labelled `capture`, never `original`. |
| B live body viewed in real Chrome | PARTIAL / SUPERSEDED FOR FULL-BODY ACCEPTANCE | Chrome-plugin DOM/screenshot failed. User-authorized Computer Use later inspected live top/opening, `Get the skill`, Bash, `Overall introduction` and outline through `Summary`, but not a full live middle/bottom scroll. The user-supplied complete Markdown is the amended full-body acceptance input. |
| B user-provided full Markdown | PASS | `seedance2.5-prompt-guide.md` equals archived `curDoc.MDContent` plus one trailing LF: 37 source headings, 4 tables/34 rows, 3 code blocks, 15 columns/48 items, 51 image refs/50 unique + 22 videos; 72-URL set and 72 local asset hashes all match. |
| B full offline archive, not summary | PASS | Full SSR/Markdown/structured text/offline HTML; 4 tables/34 rows, 37 source headings plus one capture-title H1 = 38 offline headings, 3 code blocks, 51 image occurrences and 22 video controls; non-author visible offline review passed. |
| B body assets | PASS | 72/72 unique body assets, 520,243,241 bytes: all 50 images decode and all 22 MP4/MOV files pass `ffprobe`; zero missing/remote body-media paths. |
| B official PDF | Not obtainable, declared | Published `PDFURL` hostname returned DNS NXDOMAIN through repeated system/Google-DNS/curl checks; no fake placeholder was created. |
| C index and nine detail pages | PASS | Exactly 9 projects, 9 unique slugs, 9 case JSON files, 9 canonical URL + local full-text + case-record pairs. |
| C prompt/settings/material/output archive | PASS | 14 unique media records (9 published + 5 opened generations); visible fields recorded, invisible fields explicitly `unknown`. P07-A01 and P07-A02 are separately inventoried rather than substituted. |
| C every relevant video fully checked | PASS with explicit AV-resolution boundary | Every media record has at least three start/middle-or-high-risk/end timecodes. P06 adds 57:09/85:06; P08 adds 47:47/71:09; P01 and both P07 generations have direct first/middle/near-end evidence. P02-A01-V01 has a local hash/full-decode/AAC/waveform/coarse-mouth-motion audit; semantic Cantonese, voice naturalness and phoneme-level sync remain `unknown`. |
| C evidence integrity and independent review | PASS | Ledger covers 117/117 browser-evidence files. C fragment has 133 records; all exist and match MIME/bytes/SHA. The non-acquiring freeze-state reviewer returned PASS with zero blocking findings. |
| D original preserved | PASS | Original and archived copy are both 2,850,500 bytes, 15 pages, SHA-256 `b49d1c8a2181ac2cc50aa5398d8f74cd9e28c90eec0c76675451190189d9e3dd`. |
| D full extraction/render/analysis | PASS | 15/15 page texts, 15/15 page renders, 5/5 embedded figures and OCR notes; every page visually inspected; analysis covers all pages and diagram pages 3/4/9/11/14. |
| Official model/version/platform gate | PASS | Formal Seedance 2.5 launch, ModelArk ID `dreamina-seedance-2-5-260628`, ModelArk/LAS surface differences and dated conflicts are documented. |
| Prompt playbook | PASS | 21 complete, explicitly untested examples; each has intent, input assumptions, final prompt, confirmed parameters, expected observations, failure risks and two revisions. |
| Long-form workflow / quality-speed modes | PASS | Full film hierarchy, continuity banks/state, queue, RACI, provenance, gates, rollback, KPI and three Pareto-scoped operating modes. No untested optimum claim. |
| Future evaluation plan | PASS | Controlled shots, variables, seed blocks, repeats, blind review, KPI/statistics/cost/time logging and pass thresholds; no paid run was started. |
| Additional findings | PASS | 23 findings; each contains discovery, direct evidence, importance, scope, confidence/counterexample and action/test. |
| Research report and citation boundaries | PASS | Official E01–E07 and nonofficial wording/version/causality findings were resolved. The freeze-state reviewer accepted the current 14-media scope, closed visual coverage and exact P02 AV boundary. |
| Source manifest | PASS | 385 associations / 384 unique paths; zero missing, MIME, byte or SHA-256 errors; one intentional shared A/B file association. Status is `complete_with_explicit_unknowns`; no hard gate is listed open. |
| Credentials/signed URLs | PASS | 126 current text/code files scanned by the final checker; zero high-risk key/JWT/signed-query hits. Captured `Authorization: Bearer` examples use placeholders only. |
| External mutation / paid generation | PASS | No generation, remix, deletion, upload, share, commit, push or paid model call occurred; Higgsfield remained read-only. |

## 2. Independent checks completed

- Official/PDF fragment: 237/237 records, including the user Markdown, amendment and live-top evidence; zero missing, MIME, byte or SHA mismatch.
- Supplemental fragment: 15/15 records, zero missing or byte/SHA mismatch.
- Current central manifest: 385/385 associations verified; 384 unique local files; zero missing/MIME/hash/size error.
- C: 9 projects, 14 unique media records, 133 complete central-manifest entries and a self-sufficient 133-file C fragment inventory. Evidence ledger covers 117/117 browser-evidence files.
- JSON: all 30 files parse. Markdown: 576/576 local-link occurrences resolve.
- Prompt playbook: 21/21 of every required example field; 42 revision entries; all examples marked document-derived and untested.
- Additional findings: 23/23 of every required evidence/action field.
- BytePlus: 50/50 images decode; 22/22 video/MOV files probe successfully.
- Creative Bible: 15 pages in both text and render sets; 5 OCR/diagram records; original/copy hashes identical.
- Cross-reviews: A/B/D archive, BytePlus offline v2, official report claims, nonofficial architecture/causality, prompt/film architecture and final Higgsfield C review all exist under `worknotes/`.

## 3. Evidence-boundary decisions

- P02 is the only inspected Higgsfield case with both brief and opened-generation UI explicitly labelled Seedance 2.5.
- P04 is brief-level 2.5 only; its sampled asset says `Seedance 2`, so it is not 2.5 output-quality evidence.
- P07/P08 briefs say Seedance 2.0. P09's burned `SEEDANCE2.0 4K` is an editorial label, not a backend model ID.
- Project costs, schedules, festival/premiere history, claimed fixes and performance are author self-reports, not direct model evidence or controlled experiments.
- `All assets`, `Generations`, quality badges, decoded streams and Higgsfield reference budgets are not BytePlus API specifications or individually inspected asset counts.
- Creative Bible and project heuristics do not override current official ModelArk/LAS/API constraints.
- MovieBench is a CVPR 2025 paper; StoryMem and EntityBench are used as preprint-supported design hypotheses, not Seedance 2.5 internals.
- Timestamp instructions are semantic schedules, not output-duration guarantees; the observed P02 25-second prompt produced a 29.056-second asset, but one case cannot establish a general drift rate.
- Quality-max, speed-with-gates and hybrid workflows are evidence-supported starting policies, not experimentally proven global optima.

## 4. Explicit unknowns and non-blocking boundaries

1. Most per-generation seed/camera/motion controls, retry genealogy and selected-output lineage were not visible and remain `unknown`.
2. P07 generation prompt fields remain invisible; UI settings and output checks are recorded without inventing prompt text.
3. P02's direct Seedance 2.5 file proves audio-stream/decode integrity and coarse speech-window/visible-mouth-motion alignment. Cantonese wording, voice naturalness and phoneme-level lip-sync remain `unknown`; the result is not generalized to other media.
4. Aggregated `All assets`/`Generations` counters are project statistics, not individually inspected items.

These are evidence-resolution boundaries, not hidden acquisition failures. The reports label them directly and avoid universal audio, parameter or causality claims.

## 5. Browser-free remediation completed after final C review

- Added missing known timecodes to P02 published case and P02/P04/P07 generation records.
- Moved P09's descriptive chase observation out of numeric `timecode_checks`.
- Reconciled P04's linked ZEPHYR `Production` count to the frozen P07 value `275`, without merging the two projects.
- The resume-stage 110-file C inventory was preserved as an intermediate checkpoint and then superseded by the frozen 133-file inventory below.
- Added P06/P08 middle/high-risk frames, P01 and both P07 generation start/middle/near-end sets, and separately inventoried P07-A01/A02.
- Downloaded P02-A01-V01 through the normal site control and completed its bounded local AV audit without generation or credential-bearing URLs.
- Expanded the frozen C fragment to 133 files and recalculated the 385-association central manifest; all records pass.

## 6. Disposition and resume procedure

Mark the goal `complete`. Local integrity and all amended evidence gates pass, and the non-acquiring freeze-state audit returned PASS with zero blocking findings. No further scope expansion is warranted.
