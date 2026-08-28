# Screenplay and Fountain formatting

Read this when drafting or validating screenplay pages. Default to a submission/spec screenplay unless the user explicitly requests a shooting/production draft.

## Spec-script defaults

- Use master scenes with scene headings, action, character cues, dialogue, and occasional parentheticals or transitions.
- Do not add scene numbers, shot lists, revision marks, production breakdowns, or constant camera directions.
- Camera or editorial language is allowed when the exact point of view, reveal, or transition is part of the storytelling and cannot be expressed more cleanly through action.
- Rendered screenplay conventions may vary slightly; readability and consistent professional resemblance matter more than imitating one template's margins by hand.
- When a PDF or FDX is requested, use a document-capable workflow and verify the rendered pages. This skill's plain-text canonical format is Fountain.
- Exact page count is a rendered-layout property. Without an available Fountain renderer or screenplay document tool, describe page length as an estimate and never claim deterministic page compliance.

## Fountain essentials

### Scene heading

```text
INT. APARTMENT KITCHEN - PRE-DAWN

EXT. RIVERSIDE ROAD - NIGHT
```

Use `INT.`, `EXT.`, `INT./EXT.`, or another legitimate production heading, followed by a specific location and time condition. Keep the same canonical location name throughout the project.

### Action

Any ordinary paragraph that is not another Fountain element becomes action.

```text
Mei sets the unopened letter beside the kettle. She lights the burner instead.
```

- Present tense.
- Primarily visible, audible, or playable information.
- Break action according to dramatic and reading rhythm, not a fixed line count.
- Capitalize first appearances, essential sounds, or critical props sparingly and consistently.
- Avoid screenplay-engineering terms, analysis labels, scene-card fields, and notes inside canonical pages.

### Character and dialogue

```text
MEI
You fixed the clock.

JUN
It was loud.
```

Character cues are uppercase and followed immediately by dialogue. Fountain can force mixed-case or non-Roman character cues with `@` when needed:

```text
@阿梅
你把鐘修好了。
```

Use one canonical cue per speaker. Track aliases and relationship-specific names in the bible, not by changing cues unpredictably.

### Character extensions

Use extensions only when their production meaning is clear:

```text
MEI (V.O.)
JUN (O.S.)
```

Do not use `V.O.` to avoid converting interior prose into visual drama. It must be an authorized narrative device.

### Parenthetical

```text
MEI
(to the empty hallway)
You fixed the clock.
```

Use parentheticals sparingly for an ambiguous addressee, language, simultaneous action, or a delivery that cannot be inferred. Do not direct every emotion or repeat the action line.

### Transition

Standard transitions end in `TO:`; Fountain can force one with `>`.

```text
SMASH CUT TO:
```

Most scene changes need no written transition. A new scene heading already creates the cut.

### Sections and synopses

Fountain sections and synopses may organize a working file without appearing in the rendered screenplay:

```text
# ACT ONE

## SEQUENCE A

= Mei tries to keep the apartment functioning until Jun returns.
```

Use these only if the user's Fountain tool supports them or the file is an internal working draft. Remove private notes and synopses from a delivery that should contain screenplay pages only.

### Notes and boneyard

`[[notes]]` and `/* boneyard */` are working-draft tools. Do not leave unresolved notes, alternate versions, or commented scenes in a final delivery unless the user asks for them.

## Title page

A Fountain title page can include:

```text
Title: THE TITLE
Credit: Written by
Author: Author Name
Draft date: 2026-08-29
```

Do not invent authorship, contact information, underlying-source credits, or rights status. Leave fields absent or marked for the user when unknown.

## Multilingual scripts

- Preserve the requested script and dialogue language.
- Use production-readable slugline terms consistently; locations may remain in the script's language.
- Do not phoneticize an accent into caricature.
- If dialogue is meant to be spoken in another language, mark it consistently using a note, parenthetical, or project convention selected by the user.
- Translation is a separate operation; do not silently replace culturally specific dialogue with generic equivalents.

## Formatting gate

Before delivery, check:

- every scene begins with a valid, consistent heading;
- action follows headings where needed;
- dialogue follows a valid character cue;
- parentheticals follow a character or dialogue element;
- transitions are rare and correctly formed;
- no accidental all-caps action is being parsed as a character;
- no placeholders, TODOs, analysis labels, or truncated endings remain;
- scene order and canonical location names match the outline and continuity state;
- spec drafts have no accidental scene numbers or production revisions;
- Fountain renders in the user's tool when a parser/renderer is available;
- rendered pages use a conventional screenplay typeface and spacing, normally Courier 12-point for an American-style spec submission unless the target venue specifies otherwise.

Formatting is not an authorship tell. Do not damage standard screenplay conventions to appear less machine-written.
