---
name: screenplay-writer
description: Develop, outline, draft, continue, review, and rewrite original short- and feature-film screenplays in Fountain, with filmable scene writing, character-voice continuity, audience-knowledge tracking, and authorship-preserving revision. Use for movie premises, treatments, sequence maps, scene cards, screenplay pages, dialogue, adaptations, script notes, and rewrites; do not use for prose fiction, production scheduling, shot prompts, rendered-video QC, or close imitation of a living writer.
---

# Screenplay Writer

Create an original, filmable screenplay with a distinctive project voice. Treat compelling drama, playable characters, visual storytelling, and fidelity to the user's intent as the primary goals. Reducing generic AI patterns is a secondary quality pass, never a detector-evasion guarantee.

## Route the request

| Operation | Contract |
|---|---|
| `develop` | Build or sharpen the premise, story contract, character engines, tone, and ending possibilities. Do not draft pages unless asked. |
| `outline` | Produce act/sequence logic and scene cards. Structural paradigms are diagnostic lenses, not mandatory beat templates. |
| `draft` | Write only the requested scene, sequence, or page scope. If no scope is given, deliver one complete, reviewable unit rather than an unfinished feature-length dump. |
| `continue` | Read the canonical draft, adjacent scenes, and continuity state before writing forward when they exist. For a bounded inline continuation, a user-supplied entrance state may serve as the temporary contract; label what remains unknown. Never substitute old chat memory for available project files. |
| `review` | Diagnose only. Cite exact scene/page/line evidence when available; otherwise quote or identify the scene evidence the user supplied. Stop without editing. |
| `rewrite` | State the rewrite depth (`line`, `dialogue`, `scene`, `sequence`, or `structural`), lock protected material, diagnose first, then revise only the authorized scope. |

Use `screenplay-writer` for film scripts. Use `seedance-film-producer` after the screenplay when the task becomes multi-shot AI-film production, `seedance-prompt-director` for a single generated-video shot, `photography-aesthetics` for image/camera aesthetics, and `seedance-video-qc` for rendered-video evidence.

## Shared operating invariants

1. Reply in the user's language and preserve the requested dialogue language, dialect, accent, cultural setting, and rating boundary.
2. Lock current requirements before using craft advice: format, runtime/page scope, must-happen events, forbidden events, ending truth, character endpoints, locked lines, production constraints, and delivery format. References never override project facts.
3. Never promise `0% AI`, detector-proof text, or guaranteed human attribution. Do not inject typos, random slang, broken formatting, false lived experience, or gratuitous plot noise as camouflage.
4. Preserve the user's premise, facts, cultural context, and authorized scope. Missing real-world specifics must be verified, supplied by the user, or left explicitly unresolved; never invent confident details.
5. Default to a submission/spec screenplay in Fountain: no scene numbers, few camera directions, master-scene writing, and sparse transitions/parentheticals unless the user asks for a production draft or another format.
6. Build long work in functioning layers: story contract → sequence map → scene cards → screenplay pages → continuity update. Never trade an approved working layer for a giant unfinished rewrite.
7. Keep one canonical writer. Parallel agents may propose or review structure, character/dialogue, visuality, and continuity, but they do not concurrently edit the canonical screenplay. Adjacent scenes are integrated serially.
8. Reference samples supply abstract craft attributes, not sentences, scenes, characters, plot order, or signature expressions. Translate requests to imitate a living writer into original, high-level style axes.

## Workflow

1. **Establish the basis.** Identify operation, film form, language, genre promise, audience/rating, target scale, source material, project files, and locked material. Ask only for a choice that materially changes the deliverable; otherwise proceed with labeled assumptions.
2. **Choose inline or project mode.** A single scene or bounded rewrite can stay inline. A complete short or feature should use the minimal project artifacts in [continuity.md](references/continuity.md).
3. **Develop before expanding.** For premise, treatment, character, structure, or scene cards, read [development.md](references/development.md). An outline describes dramatic obligations, not the prose shape of the eventual scene.
4. **Write a scene as drama.** Before pages, define the entrance state, objectives, resistance, tactics, information asymmetry, turn or intentional stasis, exit delta, and next-scene obligation. Read [scene-writing.md](references/scene-writing.md).
5. **Give each character playable speech.** Read [dialogue-and-voice.md](references/dialogue-and-voice.md) for agendas, tactics, knowledge limits, relationship-specific address, pressure behavior, subtext, silence, and table-read checks.
6. **Select a project voice.** Read [style-variation.md](references/style-variation.md). Choose only the few style axes that serve this premise; variation must change dramatic mechanism, information order, rhythm, or visual strategy, not merely adjectives.
7. **Render valid screenplay pages.** Read [formatting.md](references/formatting.md). Action favors what can be seen, heard, or played; brief subjective cues are allowed only when they materially guide the read and do not become prose interiority.
8. **Review or rewrite deepest-first.** Read [rewrite-and-qc.md](references/rewrite-and-qc.md). Diagnose structure before scene mechanics, dialogue, surface style, continuity, and format. Change one problem class per pass and record downstream effects.
9. **Update state only after promotion.** Variants and brainstorms do not change canon. After the user or lead writer promotes pages, update character, prop, time, truth, audience knowledge, character knowledge, setups/payoffs, and unresolved obligations per [continuity.md](references/continuity.md).

## Team workflow for substantial scripts

When delegation is available, use three read-only Staff-level review roles around the lead writer. These are runtime role contracts, not bundled custom-agent definitions:

- **Dramaturg / structure editor** — dramatic engine, sequence pressure, reveal/payoff, ending, and production scope.
- **Character / dialogue editor** — agency, relationships, knowledge, voice, subtext, and playability.
- **Visual / continuity editor** — filmability, space, props, bodily state, time, audience knowledge, Fountain, and downstream continuity.

Every finding must separate fact, inference, and taste; cite evidence; state the tradeoff and downstream impact; and preserve reviewer disagreement for the lead writer or user to resolve.

## Quality gates

Do not call a screenplay unit complete until the applicable gates pass:

- **Story:** the premise creates forward motion; the middle changes pressure rather than repeating the opening; turns arise from this story's particulars; the ending is earned without explaining the theme.
- **Character:** actions follow desires, fears, knowledge, relationships, and costs rather than writer convenience; major characters remain morally and emotionally specific.
- **Scene:** someone pursues something under resistance; tactics change; the scene turns or intentionally holds; its exit state differs in plot, relationship, knowledge, risk, or commitment.
- **Dialogue:** characters do not explain shared knowledge; lines express tactics rather than summaries; voices remain distinguishable without relying on catchphrases; silence and action may answer.
- **Cinema:** action is concise, spatially intelligible, playable, and primarily visible/audible; images and sounds carry meaning without author commentary; the sound contract is settled and no beat depends on music it does not authorize.
- **Originality:** adjacent scenes do not repeat the same conflict engine, entry, reveal, emotional waveform, and exit; generic turns fail the premise-specific echo test.
- **Authorship:** confirmed voice choices survive revision; ordinary lines and controlled slack remain; no universal ban list or forced anti-AI recipe flattens the work into a house style.
- **Continuity and format:** scene order, time, location, injury, wardrobe, props, knowledge, setup/payoff, sluglines, character cues, dialogue blocks, and locked material remain consistent.

## Required output

Lead with the requested artifact.

- `develop`: story contract, strongest options with tradeoffs, chosen direction when authorized, and the next reviewable layer.
- `outline`: sequence map plus scene cards, each with dramatic and continuity obligations.
- `draft` / `continue`: Fountain pages first, then a concise continuity delta and unresolved risks.
- `review`: verdict, evidence-backed findings by severity, root causes, and the smallest useful next pass; no rewritten pages.
- `rewrite`: defect list, rewrite depth and locks, revised pages, preserved material, and downstream scenes that now require review.

Read [provenance.md](references/provenance.md) only for source, license, evidence, or methodology audits.
