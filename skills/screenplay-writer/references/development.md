# Development and structure

Read this for premise development, treatments, outlines, sequence maps, or scene cards. The goal is a dramatic system that can generate scenes, not a beat sheet filled because a template has empty boxes.

## Constraint lock

Record current requirements before proposing story mechanics:

- film form: short or feature;
- target runtime or page scope, if supplied;
- language, cultural setting, audience, rating, and genre promise;
- source material and adaptation boundaries;
- must-happen and forbidden events;
- ending truth and any locked character endpoints;
- production constraints such as locations, cast, period, VFX, animals, children, vehicles, intimacy, or stunts;
- locked lines, images, scenes, and facts;
- the exact layer the user asked for and where to stop.

Do not silently trade one constraint for another. When two conflict, explain the conflict and provide the smallest decision needed.

Record each entry with two attributes beyond its text:

- **tier** — `hard` (violating it invalidates the deliverable), `strong` (may bend only with the reason stated in the delivery), or `default` (a starting position the draft may overturn on its own evidence);
- **span** — the scenes, the sequence, or the whole film that the entry binds.

An entry with no span is read as film-wide, which is usually wider than the user meant. A requirement that holds only for one stretch must say so, and a later scene may then legitimately require what an earlier span forbade — an attribute pinned constant through one sequence and required to change in the next is two entries with different spans, not a contradiction.

When two entries collide, the higher tier wins and the decision is reported in the delivery. When they collide at the same tier, stop and ask; do not trade one for the other silently. Ask the user to set tier and span only where the answer changes what gets written — otherwise record your assumption and label it.

Carry tier and span into every rewrite's intent lock, so a pass knows what may bend before it starts, and into the rewrite log alongside the protected material. Carrying them into `continuity.json` is a schema change: specify the new `locked_material` entry shape and update validation first, as that file requires.

## Story contract

Define these in concrete terms:

| Field | Question |
|---|---|
| Premise | What specific situation could only be this movie? |
| Dramatic engine | What pursuit repeatedly generates pressure, choice, and consequence? |
| Central dramatic question | What uncertain outcome keeps the audience reading? |
| Genre promise | What pleasures, tensions, or emotional experiences must the film actually deliver? Which adjacent genre's pleasures must it refuse, and what would show on the page if it began delivering them? |
| Theme tension | Which two defensible values are placed in conflict? Do not reduce this to a lesson. |
| Protagonist engine | What do they pursue, why now, what tactic do they default to, and what does that tactic cost? |
| Opposition | Who or what actively adapts against that pursuit? |
| Stakes | What changes if the protagonist succeeds, fails, delays, or wins the wrong way? |
| Irreversible choice | Which choice makes returning to the initial life impossible? |
| Ending pressure | What final action, refusal, loss, or consequence resolves the central question without explaining the theme? |

A logline must contain a protagonist, destabilizing condition, active pursuit, opposition, and stakes. Do not hide a weak engine behind tone words.

## Character engine

For each major character, define:

- public identity and private contradiction;
- current want, deeper need, fear, secret, and line they believe they will not cross;
- competence and vulnerability that can both affect action;
- default tactic and the tactic used when the default fails;
- leverage over other characters and what leverage others hold over them;
- knowledge at the beginning, false belief, and information they cannot yet access;
- relationship-specific behavior: the same person should not sound or act identically with a parent, rival, lover, employee, or stranger;
- pressure arc: how behavior changes when safe, challenged, cornered, and out of control;
- endpoint options and the cost of each.

Build a sparse relationship map. Characters may have loyalties, resentments, debts, and histories that do not route through the protagonist. Do not add relationships merely to simulate complexity.

## Sequence map

Use acts, sequences, or another structure only when it helps expose dramatic obligations. Do not force page-number beats.

Each sequence should specify:

1. pursuit or pressure carried into the sequence;
2. audience question active during it;
3. protagonist strategy;
4. opposition's adaptation;
5. reveal, false inference, or withheld information;
6. escalation pattern and production scale;
7. irreversible pivot or meaningful failure to pivot;
8. exit condition that creates the next obligation;
9. approximate page band only when a total page target exists.

Adjacent sequences should not repeat the same engine with higher volume. Change at least one of: who has leverage, the arena, the type of opposition, information distribution, moral cost, time pressure, or relationship configuration.

## Scene card

Create one card per intended scene:

```text
ID / slugline / story time / estimated pages
Entrance state:
Characters present and why now (list closed / open):
Objective by character:
Opposition and leverage:
Tactics and tactic shifts:
Audience question:
Truth / audience knowledge / character knowledge:
Visual or aural action:
Event list (closed / open):
Turn or intentional stasis:
Failure condition:
Nearest wrong version:
Exit delta — plot / relationship / knowledge / risk / commitment:
Open setup or payoff:
Next-scene obligation:
Continuity locks:
```

The failure condition and the nearest wrong version make the scene falsifiable in its own terms rather than only against the general rubric.

- **Failure condition** names the observable outcome that invalidates this scene even when every other obligation is met — the audience leaves holding information it must not have yet, the turn arrives from outside the characters, the exit state matches the entrance state without an intended stasis, a character acts on knowledge the card did not give them.
- **Nearest wrong version** names the plausible neighboring scene this brief invites — the version a competent pass would write by default — and the one visible difference that separates it from the intended scene.

Write both before drafting. A failure condition written after the pages describes what was written, not what was required. State it as something a reader can observe on the page, not as a quality adjective.

A `review` or `rewrite` pass tests the declared condition first and the general rubric second. When a scene fails its own declared condition, report that before any craft note; when it passes, say so, because a scene that satisfies its contract and still reads flat has a problem in the contract, not in the pages.

Mark both `closed / open` lists deliberately rather than leaving the question unstated.

- `closed` means a drafting, continuation, or rewrite pass may not add an event, an entrance, a character, or a location beyond what the card lists. A beat that appears to need one is an escalation to the card's owner, not a license to invent.
- `open` means the pass may add behavior, texture, and incident that does not change the exit delta or the knowledge state.

Close the lists when the scene's meaning depends on one action being the only thing that happens, when a later payoff depends on exactly who was in the room, or when the sequence around it is already approved. Leave them open for a first exploratory pass, and record why, so a later reader can tell an authorized addition from drift.

A closed list is a continuity fact, not a style preference: an added third party, an added exit, or an added incident in a closed scene is a defect at the same level as an injury that resets.

The card is a contract, not prose to be expanded sentence by sentence. It locks dramatic obligations while leaving blocking, line order, discoveries, and performance texture to the drafting pass.

## Anti-template development checks

Use only where the draft shows the problem:

- **Echo test:** if the premise were regenerated twenty times, would this turn appear in most versions? Replace generic turns with consequences rooted in the project's characters, setting, work, objects, or history.
- **Middle-third test:** does the middle merely execute the plan established in the opening? Introduce a change in the nature of pressure, not just a larger obstacle.
- **Theme test:** can the theme be inferred from incompatible choices and consequences? Delete speeches that tell the audience the approved interpretation unless a character is using that speech as a tactic.
- **Reveal test:** does a revelation alter the meaning of earlier behavior, or only add information? Prefer recontextualization when the genre promises revelation.
- **Scene-shape test:** list the entry, conflict engine, turn, and exit for adjacent scenes. Repetition is a problem when all four match.
- **Ending test:** did the ending emerge from accumulated choices and conditions, or arrive as scheduled growth, reconciliation, acceptance, punishment, or twist?

Do not force a subplot, nonlinearity, ambiguity, loose end, fourth-wall break, brand reference, or twist to appear more human. Statistical tendencies from prose fiction are diagnostic prompts, not screenplay recipes.

## Development outputs

- For several viable directions, present two or three materially different dramatic engines with tradeoffs, then recommend one.
- A treatment should narrate the movie's causality and emotional movement without pretending every scene is already solved.
- An outline should make omissions and unknowns visible; do not fill gaps with generic connective scenes.
- Stop at the requested layer. Development approval is a product milestone, not permission to draft the whole film.
