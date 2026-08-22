# Research Distiller Provenance Review

Review date: **2026-08-22 (Asia/Taipei)**  
Disposition: **PASS — provenance completeness**  
Blocking findings: **0**

## Independence and scope

This was an independent, read-only Staff-level research pass. The reviewer read
all ten mandatory final research artifacts in full: 6,899 lines and 437,948
bytes. The pass did not rerun the original research, reacquire source media,
invoke paid generation, edit a canonical skill, or review its own authored
behavioral output.

This report reviews provenance completeness only. It does **not** score Codex or
Claude Code discovery, invocation, implicit activation, case responses, or any
other behavioral-evaluation result. Those gates require separate host runs and
an evaluator who did not write the tested artifact.

## Method

1. Read every line of the ten sources required by the execution contract.
2. Classified claims as official fact, direct observation, project-author
   self-report, peer-reviewed/preprint method evidence, team inference,
   practice recommendation, or unknown.
3. Built an independent PD-01..17, FP-01..18, and QC-01..18 rule/source matrix.
4. Compared all 53 IDs against the three canonical `references/provenance.md`
   files without modifying them.
5. Confirmed that each provenance table records an exact source section,
   evidence/version/platform boundary, limitation or counterexample, and
   confidence judgment, and that each records the 2026-08-22 archive date.
6. Created the suite-level `SKILLS_SOURCE_MAP.md` as an index, without copying
   the full maintained rule text out of the canonical provenance references.

## Completeness result

| Skill | Expected IDs | Unique IDs present | Missing | Duplicated | Result |
|---|---:|---:|---:|---:|---|
| `seedance-prompt-director` | 17 | 17 | 0 | 0 | PASS |
| `seedance-film-producer` | 18 | 18 | 0 | 0 | PASS |
| `seedance-video-qc` | 18 | 18 | 0 | 0 | PASS |
| **Suite** | **53** | **53** | **0** | **0** | **PASS** |

All ten mandatory artifacts appear in the suite-level full-read record. The
substantive rules trace to the appropriate research sections; the source
manifest and research QA report are correctly used for archive integrity and
evidence boundaries, not as substitutes for causal evidence.

## Evidence-boundary findings

The provenance is complete only because it preserves the following distinctions:

- **Model attribution:** P02 is the sole inspected Higgsfield case with both its
  brief and opened generation labeled Seedance 2.5. P04 is brief-level 2.5 only;
  its sampled asset says `Seedance 2`. P07/P08 are 2.0, and P09's burned 2.0
  label is editorial rather than a backend identifier.
- **Platform attribution:** ModelArk, LAS, and Higgsfield capabilities, defaults,
  reference budgets, output dimensions, channel layouts, and UI badges are not
  interchangeable even when a displayed model name or ID overlaps.
- **Time control:** prompt timestamps are semantic schedules, not duration or
  frame-accurate locks. The observed 25-second P02 prompt timeline yielding a
  29.056-second asset is one bounded example, not a general drift estimate.
- **Parameter truth:** the archived ModelArk materials do not document a
  separate `negative_prompt` field; natural-language negative controls do exist.
  Same-seed output is similar, not deterministic. Costs, retries, speed,
  resolutions, limits, and success guarantees may not be inferred.
- **Reference control:** storyboard guidance is high-level; independent
  keyframes are relatively stricter but not pixel locks. Maximum reference
  counts are validation ceilings, not demonstrated quality optima.
- **Production claims:** Higgsfield briefs and the Creative Bible provide useful
  workflow evidence, but their claimed fixes, costs, schedules, festivals,
  word counts, retry counts, and stress-test thresholds are self-report or
  heuristics rather than controlled Seedance 2.5 results.
- **Long-form memory:** MovieBench is peer reviewed; StoryMem, EntityBench, and
  VBench-2.0 are method evidence. None documents a Seedance 2.5 internal memory
  mechanism or measured gain from the proposed production architecture.
- **Audio evidence:** an unmuted player icon proves no audio quality. The P02
  local audit establishes decode integrity and coarse speech-window/mouth-motion
  alignment only; Cantonese wording, voice naturalness, and phoneme-level sync
  remain unknown.
- **Operating modes:** quality-max, speed-with-floor, and hybrid are
  evidence-supported policies pending controlled evaluation, not proven global
  optima.
- **Archive state:** `complete_with_explicit_unknowns` means the frozen archive
  passed integrity review while retaining known evidence-resolution limits; it
  does not convert unknowns into passes.

## Non-blocking watch items

- Any current/latest capability claim still requires a fresh official-doc check
  with platform, endpoint, region, model ID, and document update date recorded.
- Behavioral evaluations may expose a decision rule that needs a narrow revision;
  such a change should be justified by the observed failure rather than added
  speculatively.
- Source paths must remain provenance identifiers only. Isolation tests must
  confirm the skills work without the original research directory.

## Final judgment

**PASS for provenance completeness, with zero blocking findings.** All 53 rule
IDs have traceable research sections and bounded evidence claims. This PASS is
strictly limited to research distillation and provenance. It is not a PASS for
host compatibility, behavioral quality, held-out scores, manifest/hash checks,
secret scanning, or final adversarial acceptance.
