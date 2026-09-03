# Upstream clean-room review — Seedance 2.0 Skill OS

Reviewed: **2026-09-01 (Asia/Taipei)**

## Resolved source and scope

- Repository: <https://github.com/Emily2040/seedance-2.0>
- Resolved branch: `main`
- Resolved commit: `44b514992963a2570beee71aaf2a8720785f7ec2`
- Upstream license: MIT, Copyright (c) 2026 Iamemily2050
- Review method: read-only clone; no upstream skill, prompt example, legacy text,
  schema, script, visual asset, or template was copied into `video-prompt`.

Three independent lanes read the complete assigned source, engineering, and
provenance partitions. Their union covers all **269 tracked files** and
**23,767,844 bytes**. The path inventory digest is
`c635ef766cf25dde6b4f0a8eefddfa234c60ce82da1ab0badb65d8abf027d6c6`.
Coverage includes 256 ordinary text/code/data files, `CODEOWNERS`, 10 PNGs, two
TTFs, and one small remaining text asset. Every Python source was read and AST
parsed; every JSON/JSONL source was fully parsed; SVG, font-license, and build
metadata were read; all PNGs were visually inspected; TTFs were inventoried by
metadata, bytes, and license.

This review is engineering input only. It is not an installed-skill dependency,
a current Seedance capability source, or evidence that an upstream claim still
holds on any provider surface.

## Mandatory version classification

Every finding is assigned one of these classes before it may affect a skill:

| Version class | Meaning | Permitted use |
|---|---|---|
| `GENERIC` | Filmmaking, evidence, reference, continuity, authoring, or evaluation policy that does not require a Seedance model feature. | Independently rewrite as a bounded agent-skill rule when it closes a demonstrated gap. |
| `SEEDANCE_FAMILY_CONDITIONAL` | A useful workflow whose exact syntax, media role, mode, or operation depends on a selected Seedance version and surface. | State the intent generically; activate exact behavior only after current official verification for that version and surface. |
| `SEEDANCE_2_0_ONLY` | Model IDs, limits, durations, resolution, pricing, API/UI fields, mode names, or observed behavior tied to Seedance 2.0. | Keep out of generic and 2.5 runtime guidance; mention only in dated 2.0 provenance when explicitly requested and freshly verified. |
| `UNKNOWN_UNPROVEN` | Community heuristic, historical archive, absolute claim, or project default without adequate primary/current evidence. | Use only as a test hypothesis or omit. Never present it as platform behavior. |

The upstream itself explicitly separates craft from product numbers. This
review applies that boundary more strictly: checked-in source metadata proves a
repository claim existed, not that the claim is current or correct.

## Adopt — generic policies that close real gaps

### Reference authority by controlled dimension

When multiple assets can affect the same target, assign exactly one winner for
each active dimension such as identity, wardrobe, location, motion, camera,
timing, audio, or style. An asset that wins no dimension stays inactive. This
extends the current per-reference scope contract into a conflict-resolution
matrix without importing any Seedance tag syntax.

### Inspection honesty in continuation handoffs

Separate what a still can show from what it cannot. A final frame can support
pose, position, visible wardrobe and props, environment, light, and framing; it
cannot establish motion, camera velocity, or audio phase. When media is not
inspectable, record user descriptions as reported evidence with low confidence,
never as direct observation or canonical truth.

### Source carries accepted state; prompt text carries the delta

For an accepted source clip or frame, avoid restating state already transported
by the reference. The successor prompt should concentrate on the new action,
endpoint, non-visible boundary phases, and only the locks needed to prevent a
known drift. This is a prompt-authoring policy, not a claim about model memory.

### Continuation relation and beat firewall

Distinguish same-shot continuation, an intentional next shot, a bridge between
known states, a tail repair, and a re-anchor after drift. Seamless continuity is
appropriate only when geography and open motion genuinely continue. Every
successor identifies completed beats, its one current beat, and beats reserved
for later; accepted deviations update downstream planning so later prompts do
not replay finished events or leak future events early.

### Conflict authority order

Resolve incompatible requirements by the dimension they control: rights and
safety; verified selected-surface constraints; explicit user must-haves;
reference authority; continuity; causal legibility; camera/editorial logic;
style; then skill defaults. A user constraint that loses to a higher boundary is
disclosed, not silently dropped. This is operational policy, not provider fact.

### Observable directorial intent, without a mandatory questionnaire

For narrative performance, carry the scene turn, one restrained or suppressed
behavior, and one story-specific visual or sound detail through blocking,
eyeline, prop action, camera endpoint, light, or sound. For packshots, utility,
abstract, or functional work, explicitly refuse to invent character psychology.
Do not import the upstream ten-field Director's Read as a universal gate.

### Source freshness and evaluation integrity

Keep claim freshness separate from ordinary pull-request validation. Dated
metadata can trigger release or scheduled review, but never proves a source was
re-read. Evaluation inputs should be frozen and hashed for a run; structured
judge results must fail closed when criteria are missing or contradictory. These
belong only to authoring/evaluation infrastructure, never a product runtime.

## Adapt — useful only behind explicit boundaries

- Preserve a user-provided reference token byte-for-byte, but never invent a
  token or claim a syntax works until the selected surface documents it.
- Treat accepted footage as continuation authority only after review. Exact
  first/last-frame roles, edit/extend modes, and reference-video behavior remain
  version-and-surface conditional.
- Use project-specific chain ceilings and re-anchor policies. The upstream's
  numeric defaults are not universal.
- Strict JSON, schema fixtures, immutable eval snapshots, and source-freshness
  checks may improve the development harness, but only where a demonstrated
  validation gap justifies their maintenance cost.

## Reject or quarantine

- Every Seedance 2.0 duration, reference ceiling, resolution, price, model ID,
  endpoint, request field, task hint, upload rule, and provider availability
  statement.
- Fixed prompt word counts, fixed extension depth, fixed retry counts, and any
  assumption that a seed exists or is deterministic.
- Community filter workarounds, multilingual moderation claims, broad success
  rates, and universal statements about asynchronous provider behavior.
- The complete JSON compiler/state-engine/ledger, installer, frame-extraction
  security machinery, frontend system, marketing images, fonts, and monolithic
  multi-skill package. They would change product shape or duplicate existing
  ownership.
- All migrated and v5.2 legacy bodies as current evidence. They contain stale
  platform statements, unsafe workaround language, and protected-IP examples.
- Upstream prompt examples and exact section wording. Conceptual lessons must be
  independently expressed and re-tested.

## License and asset boundary

MIT applies only to material the upstream author can license and requires its
notice for substantial copying. No substantial upstream expression is included
here, so its MIT notice is recorded as provenance rather than redistributed as
bundled code. External sources and community corpora are not relicensed by the
repository. Bodoni Moda font files are separately governed by SIL OFL 1.1. PNG
and other visual assets lack a complete rights/source manifest and are excluded;
only abstract information-design ideas may be clean-room recreated.

## Upstream validation evidence and limitations

Sixteen offline validators or self-tests passed, including skill/content/eval
structure, source registry, vocabulary, project state, continuity, behavior,
sequence, generation-run, prompt lint, prompt architecture stress, evaluator
self-test, and frame-extraction self-test. The prompt stress `skill_formula` arm
covered 102 cases with a reported mechanical average of 3.92.

The canonical release runner stopped at schema validation because the local
Python 3.14 environment lacked the lock-supported `jsonschema` dependency. A
complete upstream unit suite was not claimed. A reproducible upstream installer
failure also exists on macOS temporary paths because the OS-owned
`/var -> /private/var` link is rejected as an unsafe ancestor. Neither the
installer nor its 2.0 package is a candidate for adoption.

An independent rerun also exposed interpreter sensitivity: Apple Python 3.9
fails before validation at the upstream `types.UnionType` import, while
Homebrew Python 3.14 can run the dependency-free validators but falls outside
the locked schema dependency matrix. With Homebrew Python 3.14,
`validate_skills.py` passed and the 102-case prompt architecture stress result
was reproduced. These observations reinforce the decision not to import the
upstream validator or installer stack.

## Candidate integration slice

The smallest useful semantic slice is limited to existing skills:

1. `seedance-prompt-director`: exact user-token preservation, per-dimension
   reference authority, inspection honesty, and conflict ordering.
2. `seedance-film-producer`: accepted-source delta prompts, continuation relation,
   completed/current/reserved beat firewall, and observed-deviation propagation.
3. Held-out tests: conflicting reference dimensions; final-frame visible versus
   unknowable state; accepted deviation that completes a future beat; and a
   Seedance 2.5 request baited with Seedance 2.0 numbers.

No new skill, runtime compiler, API layer, database, installer, or media tool is
authorized by this review.
