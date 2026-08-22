# Seedance cross-agent skills — final QA

QA date: **2026-08-22 (Asia/Taipei)**  
Research archive date: **2026-08-22**  
Overall behavioral status: **PASS**

## 1. Runtime and official-spec gate

Current official skill specifications were rechecked before implementation:

- [OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills): repo `.agents/skills`, `$skill` explicit invocation, description-based implicit invocation, `name`/`description`, progressive disclosure, symlink support, and optional `agents/openai.yaml`.
- [GPT-5.6 Sol model](https://developers.openai.com/api/docs/models/gpt-5.6-sol): frontier GPT-5.6 model. Public API effort documentation exposes up to `max`; the Codex host catalog separately exposes `ultra`.
- [Claude Code skills](https://code.claude.com/docs/en/slash-commands): project `.claude/skills`, `/name`, implicit invocation, supporting files, symlink support, and the 500-line entrypoint ceiling.
- [Claude Code model configuration](https://code.claude.com/docs/en/model-config): model selection and `max` effort behavior.

| Host/runtime | CLI | Primary model | Effort | Authentication/provider | Real probe | Fallback |
|---|---|---|---|---|---|---|
| Codex CLI | `codex-cli 0.149.0` | `gpt-5.6-sol` | `ultra` | authenticated Codex/ChatGPT host | `CODEX_ULTRA_OK` | none configured |
| Claude Code | `2.1.239` | `claude-fable-5` | `max` | `claude.ai`, first-party, Max subscription | `CLAUDE_FABLE_MAX_OK`; run metadata resolves canonical Fable | none configured/detected |

Codex `ultra` is a host-specific preset described by the local catalog as maximum reasoning with automatic delegation. This is deliberately distinguished from the public API's `max` value. Claude Code reported a small Haiku auxiliary call in some runs; each `run.json` keeps auxiliary usage separate from the required Fable primary model. No run silently fell back.

All Staff roles used `gpt-5.6-sol` with `ultra`: Research Distiller, Cross-platform Skill Architect, Compatibility Engineer, and independent Adversarial Evaluator.

## 2. Research and provenance

The main agent and independent Research Distiller each read all ten mandatory final research artifacts in full: **6,899 lines / 437,948 bytes**. The original four-hour research, full video playback, and source acquisition were not rerun.

- Suite rules: PD 17/17, FP 18/18, QC 18/18 — **53/53**.
- Missing, duplicate, or orphan rule IDs: **0**.
- Independent provenance review: **PASS**, blocking findings **0**.
- Full source/section index: [SKILLS_SOURCE_MAP.md](SKILLS_SOURCE_MAP.md).
- Research Distiller report: [research-distiller.md](skill-evals/results/reviews/research-distiller.md).

Provenance paths are evidence identifiers, not runtime dependencies. Isolated eval workspaces contain no `research/` directory.

## 3. Canonical structure and native discovery

Canonical content exists only under:

```text
skills/seedance-prompt-director/
skills/seedance-film-producer/
skills/seedance-video-qc/
```

Native entries are relative symlinks to that content:

```text
.agents/skills/<name> -> ../../skills/<name>
.claude/skills/<name> -> ../../skills/<name>
```

There is no legacy `.claude/commands` fallback and no duplicated host-specific skill body. Shared `SKILL.md` frontmatter contains only `name` and `description`; Claude-only interpolation, arguments, dynamic shell injection, invocation controls, and tool grants are absent. Entry lengths are 48, 51, and 52 lines, all below the 500-line hard ceiling.

`agents/openai.yaml` is the only host adapter. Names/default prompts match the skill and `policy.allow_implicit_invocation: true` is explicit.

Post-fix `skill-creator` validation at `2026-08-22T20:37:28+08:00`: **3/3 PASS**.

## 4. Behavioral suite

The suite contains 14 held-out cases, all different from the research examples:

1. ambiguous single shot;
2. multi-character/multi-reference mapping;
3. Cantonese dialogue/audio;
4. fight physics/contact;
5. cross-shot wardrobe/injury/prop continuity;
6. 10–90 minute long-form planning;
7. quality/speed trade-off;
8. failed-video root-cause diagnosis;
9. version-misattribution trap;
10. fabricated parameter/guarantee trap;
11. unrelated coding negative activation;
12. QC variant comparison;
13. static-image negative activation;
14. live-stage negative activation.

Cases use Traditional Chinese, Simplified Chinese, English, and Cantonese dialogue. Each host received the same base case and rubric digest. Explicit mode added only the native `$name` or `/name`; implicit mode preserved the base prompt.

### Isolation

Every run used a fresh temporary workspace containing only copies of the three canonical skills and the tested host's native symlinks. Inventories record `research_present:false` and no grader/expected answer. Sessions were ephemeral/non-persistent, fallback-free, and limited to read-only skill/file tools. No paid media tool event occurred.

Codex personal skills were session-isolated by explicit disables or an empty temporary home while retaining authenticated `CODEX_HOME`. Claude used project-only setting sources, bundled skills disabled, empty MCP config, no Chrome, and only `Skill,Read,Glob,Grep`.

### Results

| Host | Cases | Score | Critical failures | Negative activation failures | Explicit coverage | Implicit coverage | Run/digest/media failures |
|---|---:|---:|---:|---:|---|---|---:|
| Codex | 14/14 | **100.00%** | **0** | **0** | all 3 skills | all 3 skills | **0** |
| Claude Code | 14/14 | **98.14%** | **0** | **0** | all 3 skills | all 3 skills | **0** |

Aggregate: [summary.json](skill-evals/results/summary.json). Per-case raw/sanitized events, final artifacts, requests, inventories, native evidence, run metadata, and independent grades are under [skill-evals/results](skill-evals/results).

The evaluator scored actual decisions and artifacts. Regex, required headings, keyword occurrence, length, and verbosity were not used as behavioral substitutes. Independent grade totals: Codex **1400/1400**; Claude **1374/1400**.

## 5. Observed failure, narrow fix, and rerun

The initial Codex `fabricated-parameter-trap` scored approximately 82/100 without a critical fabrication: it verified real BytePlus LAS fields, but unauthorizedly selected LAS even though the user had not chosen a platform, then emitted endpoint JSON.

Direct evidence and hashes are preserved under [attempts/initial-failure](skill-evals/results/codex/fabricated-parameter-trap/attempts/initial-failure). The narrow correction added one rule only: an agent must never choose a platform/model/endpoint merely to satisfy pasteable JSON; with an undecided runtime it provides a platform-neutral prompt/decision manifest and asks one blocking runtime question.

Fresh post-fix staging hashes are recorded in the rerun inventory. The related case then passed on both hosts:

- Codex: **100/100**, no platform selection or endpoint request.
- Claude Code: **99/100**, same corrected behavior.

No unrelated universal rule was added.

## 6. Evidence-shape and scoring limitations

- Eight direct Codex captures use `request.json`, `run.json`, `workspace-inventory.json`, `native-evidence.md`, and final artifacts rather than a complete persisted `events.jsonl`; the other Codex cases include event evidence. Native explicit/implicit behavior is still traceable, but the event shapes differ.
- Four earlier Claude wrapper runs show discovery through `system/init` and native Skill events but predate the newer `discovery_complete` convenience field. Their event evidence still lists all three skills.
- Two post-fix staging hash cohorts are expected: only the proven failing fabricated case was rerun after the narrow canonical change, as required by the contract.
- Codex JSONL does not expose a server-confirmed model identifier. The exact requested model/effort, local catalog, no-fallback invocation, and real probe are retained. Claude run metadata directly reports canonical Fable/firstParty.
- Claude long-form/max was intentionally slow; latency is recorded but is not a quality score.

## 7. Privacy and security

Persisted event streams are sanitized before final delivery. The current sanitizer removes session/thread/turn/request/message/tool IDs, UUIDs, thinking signatures, cwd/memory fields, user-home paths, Claude plan/project paths, ephemeral workspace paths, and signed-query values. Behavioral text remains unchanged apart from replacing private paths with stable redaction tokens.

Two sanitizer defects were found and fixed during independent review:

1. absolute home path in assistant text;
2. `~/.claude` plan paths, encoded project-memory paths, and message/tool IDs.

They were covered by regression tests and all persisted host results were re-sanitized. No model rerun was needed because the semantic outputs were unchanged.

The public-release review then removed an obsolete direct recorder that could persist raw stderr and absolute workspace paths, centralized AWS/Google/CloudFront signed-query sanitization, made publication scans read the staged Git blobs, and made score aggregation validate the committed grade schema and fail closed on any `FAIL` verdict or score mismatch.

Final security gates are recorded under [skill-evals/results/validation](skill-evals/results/validation):

- post-manifest high-confidence credential/signed-query scanner over the full public index: **PASS**, findings 0;
- post-manifest gitleaks 8.30.1 delivery-stage index scan: **PASS**, leaks 0.

No credentials, cookies, session identifiers, signed media URLs, or private data are intentionally retained.

## 8. Unknowns and limits

- These are text-only skill behavioral evaluations. They do not call Seedance or any paid image/video/audio service and cannot prove real generation quality, speed, cost, first-pass rate, continuity gain, or workflow optimality.
- Quality-max, speed-with-floor, and hybrid remain evidence-supported policies pending authorized controlled production data.
- Model/platform capabilities, prices, quotas, parameters, defaults, and policies are time-sensitive. For “current/latest” questions, the skills require a fresh official-document check.
- P02's archived audit supports only decode and coarse speech-window/mouth-motion alignment; it does not prove Cantonese wording, voice naturalness, or phoneme-level lip-sync.
- UI quality badges, displayed size, decoded dimensions, backend request resolution, container and codec remain distinct evidence.

## 9. Independent acceptance

The independent Staff-level Adversarial Evaluator did not author the canonical skills. Its [adversarial-review.md](skill-evals/results/reviews/adversarial-review.md) disposition is **PASS**, behavioral blocking findings **0**.

Final deterministic closure after this document was included:

- unit/structure/link/symlink/metadata/provenance/security/behavioral-summary tests: **35/35 PASS**;
- SHA-256 public-artifact manifest: **322 entries**;
- manifest `--check`: **PASS**;
- post-manifest credential/signed-query and gitleaks scans: **PASS**, findings/leaks 0.

## 10. Execution constraints honored

The following counts describe the original skill-construction and dual-host evaluation goal, before the user's later explicit request to create and publish this public GitHub repository:

- Paid video/image/audio generation calls: **0**.
- Higgsfield mutations, remix, share, publish or asset changes: **0**.
- API keys, OAuth grants, account tokens, or credential-bearing persistent permissions created: **0**. No project/global permission config was written; host approval state remained user-controlled runtime state.
- Global/personal skills or settings modified: **0**.
- Commits, pushes, uploads or publications during that original goal: **0**.
- Original four-hour research rerun: **0**.
