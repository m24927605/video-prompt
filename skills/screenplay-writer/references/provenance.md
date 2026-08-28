# Provenance and evidence boundaries

Read this only for methodology, source, license, or evidence audits. It is not required during ordinary screenplay work.

Research date: 2026-08-29.

## Upstream repositories reviewed

### oh-story-claudecode

- Repository: https://github.com/zenstory-ai/oh-story-claudecode
- Reviewed commit: `70c294b20ce89440e70edb766b0446d3057bc077` (2026-08-28)
- License: MIT, `Copyright (c) 2025-2026 oh-story-claudecode`

Reusable system ideas:

- explicit workflow routing and agent ownership;
- constraint locking before references influence writing;
- outline-before-prose layering;
- one canonical writer with parallel, read-only specialist review;
- single authoritative continuity state with derived views;
- hot-context budgets and query-by-ID recall;
- separation of author preferences from story facts;
- serial integration of adjacent units;
- blocking versus advisory validation and evidence-backed review.

Intentionally excluded:

- web-fiction market scanning, emotional-payoff formulas, monetization breaks, chapter hooks, mobile formatting, platform-specific word counts, and other serial-fiction assumptions;
- fixed dialogue-length power formulas and universal punctuation bans;
- copied demos, commercial-fiction excerpts, style anchors, phrase lists, genre packs, or substantial source wording;
- its Chinese web-prose pattern detector, which is not a screenplay or AIGC detector.

The upstream project itself states that its de-slop workflow does not guarantee an AI score. This skill preserves that boundary.

### sepia

- Repository: https://github.com/Nanako0129/sepia
- Reviewed commit: `e0d423d2f85b1eac71d7d3ebdcedc6a522719b55` (2026-08-28)
- License: MIT, `Copyright (c) 2026 Nanako Tsai`

Reusable ideas:

- diagnose narrative architecture before discourse and surface style;
- distinguish `write`, read-only `review`, minimal `refactor`, and full `recreate`;
- calibrate instead of reversing every observed AI tendency;
- select only relevant corrections and retain ordinary slack;
- diagnose completely before rewriting deepest-first;
- preserve the author's verified habits, quotes, facts, and intent;
- treat word or punctuation lists as cumulative clues, not verdicts.

Intentionally excluded or translated:

- prose-only signals such as narrator address, `said` tags, olfactory density, paragraph outline tests, or direct emotion labels;
- compulsory subplots, nonlinearity, brands, fourth-wall gestures, loose ends, or rarity moves;
- equal-weight reversal of population-level human/AI correlations into prescriptions for one screenplay;
- model-fingerprint claims that can expire with model versions;
- any claim that the skill can make a screenplay undetectably human.

No substantial upstream text or code is copied into this skill. The methods and examples here were newly written for film screenplay work. If future changes copy substantial upstream material, include the relevant MIT copyright and permission notice with that material.

## Primary research checked

### StoryScope

- Paper: https://arxiv.org/abs/2604.03136
- Current version at research time: v6, revised 2026-08-10.
- The paper studies approximately 5,000-word prose stories, not screenplays. It reports that discourse-level narrative features can distinguish its human and model corpora and that AI stories cluster more tightly in narrative-feature space.

Use in this skill:

- supports the limited conclusion that surface paraphrase alone is insufficient and that structural defaults deserve review;
- motivates premise-specific echo tests, theme-explanation checks, middle variation, reveal timing, character-network and ending diagnostics;
- does not validate any screenplay recipe, quality score, detector-evasion guarantee, or inverse classifier.

Population correlations are treated as hypotheses to inspect in a script, never mandatory changes. Current paper revisions can change model-specific findings, so this skill does not encode per-model fingerprint rules as hard guidance.

## Screenplay standards and quality sources

### Academy Nicholl screenwriting resources

- Formatting resources: https://www.oscars.org/nicholl/screenwriting-resources
- Scoring rubric: https://www.oscars.org/sites/oscars/files/2025-05/Nicholl_Scoring_Rubric_0.pdf

Applied guidance:

- professional spec screenplays allow small format variation but share a recognizable form;
- submission scripts generally omit scene numbers, use few camera shots, and write master scenes;
- avoid long descriptive passages and distracting non-standard formatting;
- quality review covers story, voice, characters, craft, and meaning/magic.

### Fountain

- Official syntax: https://fountain.io/syntax/

Applied guidance:

- scene headings, action, character cues, dialogue, parentheticals, transitions, title-page fields, sections, synopses, notes, and boneyard follow Fountain's documented plain-text syntax.

### Final Draft

- Screenplay elements: https://www.finaldraft.com/learn/screenplay-formatting-elements/

Applied guidance:

- scene headings identify interior/exterior, location, and time;
- action describes what the audience sees;
- character cues precede dialogue;
- parentheticals and transitions should be used sparingly.

These formatting sources describe convention, not guarantees of artistic quality. Target venue or user requirements override defaults.

## Evidence labels

When explaining a recommendation, distinguish:

- **official format guidance** — Academy, Fountain, or target-venue documentation;
- **upstream implementation fact** — directly observed in a reviewed repository and commit;
- **research result** — supported by the cited study in its actual prose-fiction domain;
- **screenplay adaptation** — a film-specific inference from those inputs;
- **practice recommendation** — craft judgment requiring project-specific evaluation;
- **unknown** — unsupported or dependent on missing material.
