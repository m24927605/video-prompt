# Project files and continuity

Read this for complete shorts, features, continuation, multi-session work, or rewrites that affect later scenes. Do not force project scaffolding onto a single inline scene.

## Minimal project structure

```text
{title}/
├── brief.md
├── story-bible.md
├── outline.md
├── scene-cards/
│   └── SC-001.md
├── screenplay.fountain
├── continuity.json
└── rewrite-log.md
```

Use these files as separate concerns:

| Artifact | Owns |
|---|---|
| `brief.md` | format, runtime/pages, language, audience/rating, genre promise, must/forbid, ending truth, production and delivery constraints |
| `story-bible.md` | world rules, character engines, relationships, secrets, voice cards, recurring visual/aural behavior |
| `outline.md` | sequence pressure, audience questions, pivots, reveal/payoff plan, approximate page bands |
| `scene-cards/` | scene obligations and continuity locks; planning only, never canonical dialogue/action prose |
| `screenplay.fountain` | the only canonical screenplay pages |
| `continuity.json` | structured current truth and state |
| `rewrite-log.md` | user note, authorized depth, protected material, changed pages, promoted version, downstream review |

Do not create duplicate canonical drafts with ambiguous names. Variants may live in a temporary workspace until one is explicitly promoted.

## Continuity schema

Use the following version-1 shape as the current contract. Do not add alternate key names, compatibility fallbacks, or parallel state files. Any future schema change requires an explicit specification and updated validation before use.

```json
{
  "schema_version": 1,
  "canonical_draft": "screenplay.fountain",
  "last_promoted_scene": "SC-014",
  "story_time": {},
  "locations": {},
  "characters": {},
  "props": {},
  "objective_truth": {},
  "audience_knowledge": {},
  "character_knowledge": {},
  "setups_payoffs": {},
  "open_obligations": [],
  "locked_material": [],
  "revision": 1
}
```

Constraint tier and span are not part of version 1. Recording them on `locked_material` entries is exactly this kind of change: write the new entry shape and update validation before any file uses it.

### Character state

Track only future-relevant fields:

- location and entry/exit route;
- physical condition, injury, fatigue, intoxication;
- wardrobe and visible changes;
- carried, hidden, lost, or transferred objects;
- immediate objective and commitment;
- current relationship state by counterpart;
- known, suspected, misunderstood, concealed, and disclosed information;
- unresolved promise, threat, debt, or task.

### Knowledge state

Keep separate:

- **objective truth** — what is actually true in the story world;
- **audience knowledge** — what the film has shown or made fairly inferable;
- **character knowledge** — what each character knows, suspects, misremembers, or falsely believes;
- **planted evidence** — what exists on screen and whether it has been noticed;
- **reveal state** — planned, planted, noticed, understood, contradicted, or paid off.

This separation is mandatory for mystery, suspense, deception, dramatic irony, and any scene where characters act on unequal information.

### Singulars

Some elements mean what they mean because they happen once. A gesture, an image, a sound, a word, a silence, a break in a character's habit, a departure from the film's own rhythm — the force comes from having no neighbors.

Record each one with the span it must be unique across (a scene, a sequence, an act, the film) and the reason it is singular. Then treat that span as spent: no other scene inside it may use the same element, and a rewrite that adds an instance is a continuity defect, not a stylistic choice, even when the new instance reads well on its own page.

Singulars are not a new key in the version-1 shape. Record each one inside the existing setups and payoffs entry it belongs to, naming the span it must stay unique across and why. Review singulars alongside setups and payoffs, and in the same pass:

- a payoff rehearsed three times before it arrives has already been paid;
- a habit-break in a character who has already broken the habit is a repetition, not a turn;
- a singular whose span was cut has lost its meaning and needs a new span or a different function.

A singular is not the same as a locked line. The locked line's text is fixed; the singular's scarcity is fixed, and it can be violated by a scene that never touches the original at all.

## Hot context for one scene

Load only:

1. the current sequence obligation;
2. the target scene card;
3. previous and next scene when present;
4. active characters' compact state and voice cards;
5. relevant location/world rules;
6. open setups/payoffs and knowledge differences that can affect the scene;
7. current user constraints and locked material.

Do not load the entire bible or every prior scene by default. Query older material by scene ID, character, object, setup ID, or event.

## Promotion protocol

Only promoted screenplay pages change canon.

1. Draft or generate variants without touching `continuity.json`.
2. Select the canonical version.
3. Verify locked material and adjacent-scene compatibility.
4. Record the scene's actual exit delta.
5. Update continuity once, then advance the revision.
6. Re-read the new state before drafting the next adjacent scene.

One writer owns `screenplay.fountain`. Reviewers return findings or alternatives; they do not simultaneously edit the canonical file.

## Revision protocol

When an earlier scene changes:

1. preserve or identify the prior canonical version;
2. determine the new truth, audience, character, prop, time, relationship, and obligation deltas;
3. scan later scenes that consume any changed fact;
4. list affected scenes and exact reason;
5. do not silently repair downstream pages outside the authorized scope;
6. update continuity only after the earlier rewrite is promoted;
7. record the user note, protected material, actual change, and unresolved downstream work in `rewrite-log.md`.

Typical propagation failures:

- a character uses information before learning it;
- an injury, wet garment, missing key, weapon, vehicle, or phone state resets;
- geography changes between adjoining scenes;
- a setup disappears but a later payoff remains;
- a lie changes but later reactions still refer to the old version;
- elapsed time or daylight no longer fits;
- a relationship reverses without an intervening event.

## Continuity gate

- Scene IDs and order are unique and aligned across outline, cards, draft, and state.
- Every promoted scene has an exit delta or a documented intentional no-change function.
- Character actions use only available knowledge.
- Object ownership and body/wardrobe state survive cuts.
- Audience inference remains fair after rewrites.
- Open setups/payoffs have status and owner; no payoff points to a deleted setup.
- Singulars remain unique across the spans they were recorded for.
- Locked material remains verbatim where required.
- The canonical screenplay and continuity revision describe the same story state.

Continuity consistency is a hard gate. Dramatic quality remains a Staff-level semantic review; do not pretend a JSON shape proves the screenplay is good.
