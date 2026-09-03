# Claude Code upstream integration adversarial review

## Scope and isolation

This is a fresh-context review of the 29 Claude Code cases only. The review used `skill-evals/rubric.md`, `skill-evals/schemas/grade.schema.json`, each case and grader JSON, and each Claude case's `final.md`, `native-evidence.md`, `request.json`, and `run.json`. It did not use Codex outputs/grades, prior integration reviews, implementation diffs, research notes, or implementer reasoning.

The full two-host `aggregate_scores.py` entry point was not executed because it necessarily reads the prohibited Codex lane and rewrites cross-host summaries. Instead, its existing `grade_validation_errors` and `run_activity_errors` helpers, case-contract parser, digest rules, activation rules, and rubric verdict invariant were applied directly to the Claude lane. This produced zero grade-schema or cross-file validation errors.

## Overall verdict

**FAIL**

- Cases: **29**
- PASS: **22**
- FAIL: **7**
- Score: **2603 / 2900 = 89.76%**
- Critical failures: **0**
- Aggregate score gate (≥90%): **FAIL**
- Every-case verdict gate: **FAIL** (7 case failures)
- Critical-failure gate: **PASS**

Host process success is not content success: every run exited successfully and produced a final artifact, but seven finals did not meet the case contract and the score remains below 90%.

## Case results

| Case | Score | Verdict | Critical |
|---|---:|---|---:|
| accepted-deviation-beat-firewall | 98 | PASS | 0 |
| ambiguous-extension-boundary | 94 | PASS | 0 |
| ambiguous-single-shot | 91 | PASS | 0 |
| append-extension-boundary | 98 | PASS | 0 |
| cantonese-dialogue-audio | 94 | PASS | 0 |
| coarse-blockout-mapping | 97 | PASS | 0 |
| continuation-observation-boundary | 95 | PASS | 0 |
| cross-shot-state-continuity | 98 | PASS | 0 |
| fabricated-parameter-trap | 95 | PASS | 0 |
| failed-video-root-cause | 96 | PASS | 0 |
| fight-physics-contact | 96 | PASS | 0 |
| full-seedance-clip-routing | 96 | PASS | 0 |
| long-form-10-to-90-minutes | 98 | PASS | 0 |
| marked-edit-scope | 96 | PASS | 0 |
| multi-character-reference-mapping | 97 | PASS | 0 |
| negative-activation | 97 | PASS | 0 |
| negative-image-design | 88 | **FAIL** | 0 |
| negative-live-action-critique | 55 | **FAIL** | 0 |
| person-and-example-reference-scope | 61 | **FAIL** | 0 |
| prompt-only-output-fidelity | 84 | **FAIL** | 0 |
| qc-variant-comparison | 95 | PASS | 0 |
| quality-speed-tradeoff | 98 | PASS | 0 |
| reference-dimension-authority | 98 | PASS | 0 |
| seedance20-to-25-version-isolation | 94 | PASS | 0 |
| sequential-edit-then-extend | 95 | PASS | 0 |
| storyboard-single-clip-scope | 60 | **FAIL** | 0 |
| transition-bridge-scope | 57 | **FAIL** | 0 |
| version-misattribution-trap | 98 | PASS | 0 |
| video-visual-look-subcontract | 84 | **FAIL** | 0 |

## Gate audit

### Grade and run integrity

- Grade schema validation: **PASS, 29/29**
- Lane-total equality: **PASS, 29/29**
- Rubric verdict invariant (`PASS` iff score ≥90 and no critical): **PASS, 29/29**
- Request case/rubric digests: **PASS, 29/29**
- Run gate (`exit_code == 0`, final present, no research contamination): **PASS, 29/29**
- Paid media-generation events: **0 cases, PASS**
- Secret/private-data findings in the reviewed artifacts: none observed

### Activation and routing

- `activation_verified`: **true, 29/29**, based on native/run evidence rather than exit status or prose resemblance
- Expected-skill activation failures: **0**
- Forbidden-skill activation failures: **0**
- Collision activation-evidence failures: **0**
- Negative-activation failures: **0**; both expected-none cases activated no packaged skill
- Existing aggregate helper's archived explicit/implicit coverage gate: **PASS** for `seedance-prompt-director`, `seedance-film-producer`, and `seedance-video-qc` in both modes

Coverage caveat: the literal rubric phrase “every skill has explicit and implicit native evidence” is broader than the helper's `ARCHIVED_BEHAVIORAL_SKILLS` gate. In these 29 cases, `photography-aesthetics` has implicit collision evidence but no explicit case, and `screenplay-writer` has no expected case. Therefore broader all-packaged-skill explicit/implicit coverage is **unknown/unproven**, even though the existing aggregate helper's implemented coverage gate passes.

## Root-cause findings

### RC-1 — Plan-mode non-delivery replaces the requested artifact

Affected failures:

- `person-and-example-reference-scope` (61)
- `storyboard-single-clip-scope` (60)
- `transition-bridge-scope` (57)

All three finals correctly reason through much of the grader contract, then stop at “plan for approval” and promise to create the actual prompt later. The case prompts already supplied enough information for provider-neutral artifacts; missing Write/ExitPlanMode tooling was irrelevant to a text-only response. This is the largest shared failure because it turns correct reasoning into zero usable deliverable.

Evidence:

- `person-and-example-reference-scope/final.md`: “請你確認後我再產出完整交付物”
- `storyboard-single-clip-scope/final.md`: “請你確認後我再產出最終交付物”
- `transition-bridge-scope/final.md`: “say ‘go ahead’ and I'll write the full production packet”

### RC-2 — Explicit output/scope locks are treated as optional

Affected failures:

- `prompt-only-output-fidelity` (84)
- `video-visual-look-subcontract` (84)

The prompt-only case contains a strong prompt, but adds an expressly prohibited preface, separators, and postscript. The visual-look subcontract activates the correct skill and covers the requested look, but invents subject blocking and a two-second action despite explicit bans on blocking/timeline, then adds numerous exact numeric choices not grounded in the brief. These are not cosmetic formatting complaints: each case exists to test whether the deliverable lock overrides a default expansive packet.

### RC-3 — Core semantic inversion in an unrelated negative case

Affected failure:

- `negative-live-action-critique` (55)

The final interprets the stronger performer masking the other actor as an intentional concealment effect and teaches how to optimize it. The grader requires solving the audience-sightline problem. Routing was correctly ordinary/non-Seedance, but the answer solves the opposite task.

### RC-4 — Unsupported cross-runtime guidance contaminates an otherwise correct static artifact

Affected failure:

- `negative-image-design` (88)

The static Swiss-poster prompt and photography-aesthetics ownership are correct. The score falls below threshold because the final makes unsupported compatibility claims across named current image systems and gives provider-field/negative-prompt advice while the target model is explicitly unknown. The artifact would have passed by remaining provider-neutral.

## Non-failing recurring weaknesses

- Many successful cases open with irrelevant Write/plan-mode/tooling commentary. It usually costs only scope points, but RC-1 shows the same habit can suppress the actual deliverable.
- Several answers add unsourced current-platform compatibility language, exact visual numbers, or generalized “known weakness” claims. Most are caveated and non-critical, but they repeatedly reduce the evidence-discipline lane.
- Some answers invent finite retry ceilings. Where the case explicitly requested a proposed ceiling and the answer labeled it policy, this is valid. Where not requested, project-defined/unknown ceilings would be cleaner.
- `seedance20-to-25-version-isolation` includes an invented visible “open” sign while also banning on-screen text; this is a non-critical internal contradiction.
- `negative-activation` accepts `True` as an integer fps because Python `bool` subclasses `int`; this is a minor validation edge case.

## Strongest evidence-backed behavior

The suite is strongest on continuity/state design and evidence boundaries:

- Accepted/rejected state firewalls and rollback: `accepted-deviation-beat-firewall`, `cross-shot-state-continuity`, `long-form-10-to-90-minutes`
- Provider/version uncertainty: `fabricated-parameter-trap`, `reference-dimension-authority`, `version-misattribution-trap`
- Output-evidence QC: `failed-video-root-cause`, `qc-variant-comparison`
- Edit/extend boundary ownership: `append-extension-boundary`, `marked-edit-scope`, `sequential-edit-then-extend`

These cases preserve parent lineage, distinguish observations from hypotheses/unknowns, avoid paid generation, and keep runtime parameters unclaimed.

## Final assessment

The Claude lane is close but does not pass: **89.76%, 22/29 PASS, 0 critical**. The failure concentration is narrow and actionable. The primary fix is not more production detail; it is enforcing the user's deliverable lock before default plan/packet behavior, followed by correcting one theatre-language semantic inversion and removing unsupported cross-runtime claims. After root-cause repair, rerun focused regressions for the seven failing cases before one full validation/reseal cycle.
