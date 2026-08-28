# Rewrite and quality control

Read this for script notes, diagnosis, polish, dialogue passes, scene rewrites, sequence rewrites, or structural rewrites.

## Operation boundary

- `review` is read-only: report findings and stop.
- `rewrite` requires an authorized depth and scope.
- `line` changes action/dialogue phrasing only.
- `dialogue` may adjust the exchange and minimal timing action, but not scene order, events, outcomes, knowledge, or character decisions.
- `scene` may rebuild one scene while preserving sequence obligations.
- `sequence` may reorder or replace scenes inside one sequence while preserving locked story facts and downstream contracts.
- `structural` may change the film's larger architecture only after identifying the affected ending, character arcs, reveals, and continuity.

Never hide a deeper required change inside a shallower pass. Report the limitation and let the user authorize expansion.

## Intent lock

Before diagnosing, record:

- user notes and requested outcome;
- exact pages/scenes included;
- locked lines, scenes, facts, ending, characters, tone, rating, and production limits;
- material outside scope;
- current canonical version;
- whether the user wants diagnosis only, alternatives, or applied edits.

## Evidence protocol

Every material finding must include:

1. dimension;
2. severity: `S1 blocking`, `S2 major`, `S3 moderate`, or `S4 polish`;
3. exact scene/page/line or a short quoted excerpt;
4. direct observation;
5. interpretation or root-cause hypothesis, labeled as such;
6. acceptance impact;
7. smallest useful pass and likely downstream effect.

Separate craft judgment from factual or continuity error. Preserve disagreements between reviewers instead of averaging them into false certainty.

## Deepest-first passes

Run one problem class at a time:

1. **Story contract** — premise, central question, genre promise, ending, and constraints.
2. **Reverse outline** — sequence pressure, cause/consequence, reveal order, setup/payoff, middle repetition, and earned ending.
3. **Character** — agency, motive, tactic, cost, relationships, knowledge, contradiction, and arc.
4. **Scene** — objective, resistance, tactic shifts, turn/stasis, entrance/exit, visual action, and sequence obligation.
5. **Audience knowledge** — truth, inference, misdirection, fairness, and reveal timing.
6. **Dialogue/performance** — voice, subtext, exposition, timing, silence, and playability.
7. **Visual/aural writing** — filmability, geography, objects, sounds, repeated explanation, and production scope.
8. **Authorship/style** — project voice, generic turns, uniform scene shapes, template clusters, and overcorrection.
9. **Continuity/format** — time, location, body, wardrobe, props, knowledge, scene order, Fountain, and locked text.

Do not polish dialogue in a scene that will be cut or rebuild action lines before the story purpose is stable.

## Screenplay quality rubric

### Story

- Is the premise specific and fresh in execution?
- Does it create sustained forward motion rather than a sequence of incidents?
- Do beginning, middle, and ending change the nature of the dramatic question?
- Does the film create emotional connection in its chosen genre?
- Are turns earned by previous conditions rather than convenience?

### Voice

- Does the script express a coherent but flexible point of view?
- Does it show choices particular to this writer and movie rather than a familiar composite?
- Is style serving drama, or advertising itself?
- Does the middle retain voice and pressure rather than flatten into competent filler?

### Characters

- Are characters vivid through action, choices, relationships, and speech?
- Do major characters want incompatible things and adapt tactics?
- Do actions fit who they are and what they know?
- Are voices distinct yet socially related?
- Does change, refusal to change, or deterioration arise from accumulated pressure?

### Craft

- Does conflict propel action and expose character?
- Are scenes filmable, spatially clear, and playable?
- Do suspense, comedy, tension, intimacy, and release use description and dialogue effectively?
- Does every sequence change leverage, knowledge, risk, commitment, or the pursuit itself?
- Are setup/payoff, misdirection, and revelation fair and legible?

### Meaning and magic

- Is the film about something without reducing itself to a thesis?
- Is there an image, choice, relationship, rhythm, or contradiction that remains after reading?
- Does the film have purpose beyond misery, cleverness, or mechanical resolution?
- Is there a special quality worth protecting even when the draft has flaws?

### Continuity, production, and format

- Are story time, geography, body state, wardrobe, props, knowledge, and scene order consistent?
- Are production demands intentional and proportional to the film?
- Is the spec screenplay readable, parsable as Fountain, and free of placeholders or accidental truncation?
- Are camera directions, transitions, capitalization, and parentheticals purposeful rather than constant?

## Anti-template review

Do not assign an AI probability. Flag observed patterns and their dramatic cost:

- themes or symbols explained after the audience already understood them;
- generic premise-default turns;
- every scene using the same objective/argument/reveal shape;
- uniform action-block length, tempo, or dialogue polish;
- exposition disguised as questions;
- emotions repeatedly rendered through the same bodily reaction;
- all relationships warm, all characters connected, or opposition existing only for the protagonist;
- ending by scheduled understanding, reconciliation, punishment, or twist;
- references, slang, specificity, or irregularity added without story truth;
- revisions that remove the author's actual voice in pursuit of cleanliness.

Single words, punctuation marks, conventional screenplay elements, formal grammar, or a clean page are not evidence by themselves. Diagnose clusters and function.

## Rewrite procedure

1. Complete the defect list before editing.
2. Select the deepest authorized pass.
3. Preserve locked material and write down what must remain invariant.
4. Change the minimum scope that can solve the root cause.
5. Re-run only affected rubric groups plus continuity and format.
6. Compare the revised unit with its adjacent scenes for new repetition or voice drift.
7. Record changed canon and downstream scenes that require review.
8. Stop when the accepted defect is solved or the next fix requires broader authority.

Prefer replacement or deletion over adding generic explanation. The valid additive fix is concrete, story-supported specificity.

## Blind evaluation for major work

When feasible, compare baseline and skill-assisted variants under anonymous labels. Reviewers should not know which is which and should score:

- dramatic clarity;
- emotional impact;
- character specificity;
- dialogue playability;
- visual filmability;
- originality;
- continuity;
- fidelity to user intent.

AI-detector output may be recorded as an observation but is never a release gate. A passing rewrite must have zero blocking continuity/lock violations and must improve the intended craft dimensions without creating a new house style.

## Report shapes

`review`:

```text
Verdict and evidence scope
Findings by severity
Root-cause hypotheses
Strong material to protect
Smallest useful next pass
Missing evidence
```

`rewrite`:

```text
Rewrite depth and locked material
Defect list
Revised Fountain pages
What changed / what remained fixed
Continuity delta
Downstream scenes requiring review
Remaining risks and stop condition
```
