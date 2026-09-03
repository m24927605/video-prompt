# Production prompt schema

Read this file when drafting or restructuring a prompt. It turns a brief into a shot contract; it is not a claim that one textual format is universally best.

## Intake and version gate

Record the smallest useful set:

| Field | Record |
|---|---|
| Delivery | purpose, audience, composed framing intent and container geometry, intended duration, audio/subtitles, downstream edit |
| Runtime | platform/surface, displayed model, model ID if exposed, region, document date |
| Task | generate, reference, edit, extend, first frame, first/last frame |
| Entities | exact count, identity, state, wardrobe, props, owner/hand, invariants |
| Space | location, landmarks, frame-left/right, depth, axis, eyeline, entrance/exit |
| Event | visible start, one primary causal delta, visible end |
| Media | upload order, rights, each reference job and exclusions |
| Look/sound | camera, light, material, color, style, speaker, language/accent, SFX/BGM |

If platform/model is unknown, write a platform-neutral prompt and label runtime parameters unknown. Do not fill “usual” values and do not select a convenient platform on the user's behalf. If exact endpoint JSON is requested, provide the complete prompt plus a parameter-neutral manifest of required decisions, then ask only which runtime to target. Current documentation may validate a candidate after the user chooses it; it does not supply that product decision.

## Version isolation

Seedance 2.0 number, model ID, API, tag, and mode facts do not enter a Seedance 2.5 or generic artifact. Keep those runtime assertions on their original verified surface and date. Directing craft transfers across surfaces only when it makes no capability claim: clear entity mapping, causal action, continuity, and observable acceptance remain transferable. [PD-15]

## Task routing

These are contracts, not interchangeable prompt openings. [PD-16]

Assign one primary operation to each artifact: generate, reference-generate, edit, extend, first-frame, or first/last-frame. Do not combine task contracts in one artifact. If the user needs two operations in sequence, return separate ordered artifacts and make the first artifact's output the declared source of the next.

| Task | Prompt contract | Runtime boundary |
|---|---|---|
| Text generation | State `Generate` and the complete shot | Set only parameters confirmed for the actual surface |
| Reference generation | State `Generate using ... only for ...`; map every reference | Do not infer one platform's reference roles or limits on another |
| Edit | Name the sole master video, A→B change, time/scope, and preserve list | Locked behavior and exact values must come from current endpoint docs |
| Extend | State direction and added duration intent; reconstruct the boundary state before the new event | Do not replay the source ending or treat a drifted tail as canonical |
| First frame | State strict start composition and subsequent delta | A strict runtime role differs from a semantic reference-image instruction |
| First/last | State both endpoints and the causal bridge | Use matching aspect ratios when endpoint behavior is uncertain |

Archived ModelArk evidence dated 2026-08-22 documented `auto/reference/edit/extend` as task hints, strict first/last roles, `adaptive` for locked aspect tasks, and `-1` duration for edit. Recheck the current official endpoint before presenting these as current or before emitting JSON. Do not reuse them for LAS, Higgsfield, or another UI.

## Observation and conflict boundary

A final frame can establish only visible pose, position, visible wardrobe, props, environment, light, and framing. Motion, camera velocity, and audio phase remain unknown unless evidence covers them. If you cannot inspect the source, use only user-reported facts at low confidence, list the uncertainties, and do not promote them to observed or canonical state. [PD-04]

Resolve conflicts in this order: rights/safety > verified selected-surface constraint > explicit user must-have > ref authority > continuity > causal legibility > camera/editorial > style > defaults. When resolution loses a user constraint, disclose the loss and its reason instead of silently replacing it. Marking the surviving rank inside the delivered artifact is a separate step; see the head of **Assembly order**. [PD-05] [PD-16]

## Assembly order

Use only sections that change the result. A compact shot may remain natural prose; a high-risk or multi-reference shot benefits from explicit blocks.

Mark rank inside the artifact, not only in your own reasoning. The conflict order above is how you build the prompt; it is invisible to whatever reads it.

- Give each block a severity: a hard requirement that must hold, or description that may be interpreted. Apply the same marking convention across the whole prompt, and to per-unit riders as well as to global blocks.
- Where two statements in the prompt could be read as conflicting and the conflict cannot be removed, name the one that governs, in one line, above the pair.
- Where a constraint has been dropped in previous takes, hoist it and say it governs the shot, rather than restating it more elaborately in place.
- Where a constraint is repeated rather than hoisted, the repetition must be verbatim. Repeating it *differently* is not legitimate. A detail added on the second pass writes a second specification, and the two then compete with no way for the reader to know which is the correction. Repeat the exact words, or hoist and state it once. This governs repetition only; where a ban belongs is still decided under **Exclusion scope and invalidating conditions**.

Severity marking is an ordering signal only. It does not raise a constraint's chance of being honored on any surface, and a prompt in which every block is marked hard carries no ordering at all. If more than a minority of the artifact is marked hard, the shot is overloaded—split it instead. On a surface that renders text at all, a severity marker written as an all-caps label is itself a text-shaped string and can be drawn into the picture. Whether a given surface does that is unverified, and the label form buys no extra weight either way, so mark severity in ordinary words.

```text
[TASK AND INTENT]
Generate/edit/extend ...
Context, audience, narrative purpose, and one-sentence visible intent.

[EXACT ENTITIES]
Exactly N people/objects. Identity, state, wardrobe, prop ownership.
Invariants: name them in [ENTRY CONDITION AND HELD INVARIANTS], not here.

[ACTIVE REFERENCES AND ROLES]
@Image/Video/Audio N = job; allowed inheritance; excluded inheritance.

[LOCATION AND SPATIAL MAP]
Landmarks, frame-left/right, depth, axis, eyelines, entrances/exits.
Fixed labels for the sides of the space; every lateral term marked with the frame it belongs to.

[FIRST FRAME AND BLOCKING]
Who/what occupies each zone; pose, gaze, held props, camera side.

[FORMAT AND DURATION INTENT]
Aspect/duration/audio only when confirmed; otherwise leave in assumptions/unknowns.
Composed framing intent is picture content and is stated apart from the container.

[TAKE INTEGRITY]
Continuous take, or N delimited internal units. Playback rate. Permitted joins.

[OPTICS AND CAMERA]
Shot size, camera height/side, lens feel, one primary move, speed, focus target.
Fill every field or mark it unspecified; a half-stated field invites the model to complete it, and nothing carries that completion from one shot to the next. Focal length, aperture and focus target are creative values that belong in this block; resolution, frame rate and container are runtime parameters and stay out of it.

[TIMECODED ACTION BEATS]
Contiguous semantic intervals. Each: start state → primary event → visible result.

[PHYSICS]
Contact point, force/direction, weight/inertia, material response, result.

[OBSERVABLE ACTING]
Objective, obstacle/tactic, gaze target, hands, breath/blink, timing, state change.

[LIGHT, COLOR, MATERIAL]
Motivated source/direction, palette allocation, material response, allowed change.

[AUDIO]
Speaker, language/accent, exact line, delivery, silent characters, ambience, SFX, BGM.

[STYLE]
Medium/look and only the shot-relevant style grammar.

[POSITIVE CONSTRAINTS]
Expected present state, exact counts, preservation; precise necessary bans only, each with its scope.

[ENTRY CONDITION AND HELD INVARIANTS]
What is already true, and already in progress, at the first frame.
Each attribute that must not change: the attribute, the interval it holds over, and the observation that would show it moved.

[END STATE]
Pose, prop/location state, gaze, camera/motion vector, audio and next-shot handoff.

[ACCEPTANCE CONDITIONS]
Observable pass/fail checks, not aesthetic adjectives.
```

### Write for a reader who has read nothing else

Every clause that will be submitted must be executable by a reader holding this one submission and nothing else — the prompt text plus whatever assets travel with it, and not the passport it came from, not the registry, not an earlier submission, not a sibling image's prompt. Anything outside the submission is unreachable, and a clause that reaches for it constrains nothing. That is worse than silence: the attribute the clause was written to bound is then unbounded, and an unbounded attribute is filled from the model's own prior.

Two forms fail, for different reasons.

- **Reaching outside the submission** — *the master*, *the other views*, *as approved*, *consistent with the design*, *the same as the previous version*. Nothing at the other end of the pointer is present.
- **Complement over an attribute spread across the submission** — *the damage listed above and nothing beyond it*, *the other surfaces unchanged*, *the rest*, *the others*, *that area*. The referent is present and the clause still fails, because it asks the reader to re-scan the whole text, gather one attribute's scattered specifications, subtract them from a category, and render the difference. In a controlled pair of runs differing only in this wording, the version bounding damage that way returned damage of kinds the text never requested, on objects the text never named; the version that gave each object its own sentence — the object, the place on it, and the state of its surface — did not.

Deleting the phrase does not delete the operation. An author who still needs the bound writes *the rest* or *that area* instead and has written the same instruction again. Test for the operation — is the reader being asked to reconstruct a set from elsewhere in the text and subtract it? — not for the phrase.

Three neighbouring forms stay legitimate, and none of them is that operation.

- **A closed set stated in place** — the complete positive inventory written out in the same clause, then a bar on anything outside it: *exactly two people, and no third figure anywhere in frame*. The reader needs no arithmetic beyond "nothing else", because the list is in front of them. What makes it legitimate is that the inventory is restated, not cited: *no damage other than the damage specified* wears the same shape and is the failing form.
- **A labelled block of the same submission** — a clause may name another labelled block of the submitted text where that block carries the literal values and the clause names it positively. Where the referent is a permitted exception to a standing prohibition, restate the exception in full rather than citing it: *the only camera movement is a slow forward push; no pan, no tilt, no roll, no zoom* rather than *except the movement named for this shot*.
- **An asset submitted with the text** — a reference image, video or audio clip that travels with the prompt is present at the other end of the pointer, so naming it and giving it a job is not abstraction. The whole reference contract depends on this: the rule bars pointers to what was left behind, not the bindings under **Reference packet** and the active-reference contract.

The block labels and scaffold notes in this file's assembly template are authoring furniture: they are replaced by content when the prompt is composed, and are never submitted.

The rule binds submitted text only. Registries, bibles, review sheets and acceptance checklists are read by people, and abstraction is what keeps them maintainable. The boundary is the moment text is pasted into a generator, not the moment it is written.

A sentence that describes the artifact rather than the picture is not ignored — it is drawn. A note written for the author about how several images relate to one another, asserting that they agree, was executed as a picture *of* that relation: one frame carrying a grid of repeated portraits. Before submitting, read each sentence and ask whether it describes something in front of a camera. If it describes the document, delete it or convert it.

### Delivery framing and container

Separate the delivery framing from the container.

- The **container**—the geometry the runtime actually renders—stays a runtime parameter. It is omitted or labeled unknown unless verified for the selected surface. This does not change.
- The **framing intent** can still be stated as picture content: compose for a stated ratio inside whatever frame is delivered. Say which of two things you mean—the excluded bands are simply kept clear of anything the shot needs, or they are rendered as inert borders—because they conform differently downstream.

State the framing intent once. Record in the packet's unknowns that the delivered file's geometry is the container, not the composed ratio, so a later crop or conform is planned rather than discovered. Composing for a ratio is a picture-content instruction and makes no claim that the surface can output that ratio.

### Take integrity

State the clip's internal edit structure instead of leaving it implied.

- **Continuous take** — declare it, then name the specific things that would break it: an internal cut, a soft transition, and any departure from a constant playback rate. A one-shot claim on its own does not rule out a mid-clip rate change.
- **Several internal setups in one job** — give each setup its own delimited unit under its own header. Inside each unit, restate every attribute that must not drift when the setup changes: at minimum framing and camera, plus whichever of environment, light, and look that particular change puts at risk. Mark each join with an explicit token, and state which join types are permitted, barring the rest—in particular any join that blends one setup into the next rather than replacing it. Each unit still obeys one primary causal event, and the units together remain one artifact with one primary operation.

Second counts written into a unit header are semantic pacing, not frame-accurate duration. Decide deliberately whether they are meant to sum to the runtime duration parameter and say which, rather than leaving the reader to assume. Cross-shot planning across separate jobs, and continuity between them, remain with `seedance-film-producer`.

### Exclusion scope and invalidating conditions

Give every exclusion a scope and, for the few that matter most, a verdict.

- **Scope** — state what each ban binds: the whole artifact, one named unit inside it, or the single constraint it defends. A ban whose scope is one constraint belongs next to that constraint, not in a pooled list at the end; a pooled list must say that its scope is the whole artifact. If a later unit requires what an earlier ban forbids, the ban was mis-scoped: scope it to its unit or delete it. Both architectures are legitimate—exclusions gathered under one label, or exclusions distributed to the constraints they qualify. Neither is established as better; what is not legitimate is a ban whose scope the reader has to guess.
- **Form** — for a feature that has no natural unit to count, state the bound as geometry, not as a number. A clause forbidding a second instance, or capping instances at one, was observed to leave the feature free and return it repeatedly. State where it sits, how far it runs, and which surfaces stay whole: *one dent and no other damage* is arithmetic; *the dent occupies the lower half of the door panel and stops at the crease line; the panel above the crease is continuous and unbroken* is a place and an edge. This covers diffuse features only — marks, cracks, tears, patches, stains, wear. Counts of whole discrete entities, positive and negative alike, are a different control and stay exactly as they are under **Entities and spatial control**. Both halves of this bullet rest on one run: inside a single prompt, a count-form bound on a diffuse feature was not held while a position-form bound in the same text was. That is an uncontrolled within-prompt observation, not a controlled comparison — the controlled pair this project ran varied pointer-versus-literal wording, not count-versus-geometry.
- **Verdict** — for the small number of constraints whose violation would make the take unusable, write the invalidating condition into the prompt itself, beside the constraint: the required state, then the specific observable that would void the take. One per genuinely take-killing constraint. An invalidation clause attached to every line restates the whole prompt and defends nothing.

Writing the verdict into the prompt moves the pass/fail test into the generator's input. It does not make the test enforceable and is not a success guarantee, so the same condition still appears in the reviewer-facing acceptance checks.

### In-world written matter

Written matter inside the world of the shot is a separate control from subtitles and overlays. Pick one of three states and say which:

- no written matter in frame at all;
- written matter present but not resolving into readable characters;
- written matter whose exact strings, placement, and count are enumerated and closed against any additional string.

The third is the high-risk case and keeps the text-failure route: isolate it as a short static text test, or composite the graphic. The first two cost one clause each and are otherwise decided for you.

State two is not free of failure, only of a different one. In direct project observation, a bare ban on text over a surface that ordinarily carries markings — a keyboard, a control panel, a label, a spine, a machined housing, a printed carton — returned glyph-shaped debris: shapes that read as characters without being any. Whether that holds on a given surface is unverified; write for it anyway, because the cost is two clauses. First a malformation guard naming what must not appear: no invented glyphs, no character-like marks, no misspelled or partial words. Then a positive target for that same surface, tied to the physical cause of what is seen there — an even wear sheen and shallow depressions where fingers rest; moulded seams and a stamped-then-worn finish; a plain field with the grain of the material running through it — with legibility stated as the outcome: no letters or digits readable anywhere on it. Do not write *blurred text*: it asks for text and then for a treatment of it, and returns text. The surface must be given a described reason to look the way it does that is not writing. The same two-clause shape is used on the image side in `photography-aesthetics` (`references/10-zh-lexicon.md` §3-2); keep the two aligned.

### Entry condition and held invariants

Not every target condition is an arrival. Three pins are distinct and a shot may need all three.

- **Entry condition** — beyond who occupies the frame, state the motion phase at frame zero: whether the primary action is already in progress as the shot opens, or starts only after a stated delay. Leave it unspecified and the generator picks the opening motion phase for you.
- **Held invariant** — for an attribute that must survive the shot rather than land somewhere new, name it, give the interval it covers (first frame through final frame, or a stated sub-interval), and give the observable whose appearance would prove it moved. Name each invariant the same way every time it appears, so the same words can be carried between takes unchanged rather than re-described.
- **End state** — unchanged: where the shot lands.

A held invariant does not replace an end state and is not a continuity note about neighboring shots. The end state says where the shot arrives; the invariant says what was never permitted to move on the way there. Keep the invariant set small; name an attribute only when its unwanted change would cost the take.

## Task-specific packets

### Reference packet

1. List upload-order bindings before the narrative.
2. Use the smallest reference set that supplies unique information. [PD-06]
3. Separate identity from pose/composition, location from camera framing, motion from performer identity, and audio timbre from music/room tone.
4. If a source already specifies an attribute precisely, do not restate it inconsistently.

### Edit packet

```text
Edit [sole master]. Only change [A] to [B] during [scope/time].
Preserve [identities, untouched geometry, action timing, camera, light, grade, audio...].
The changed element inherits [occlusion/contact/reflection/shadow/material behavior].
Before/after the scope: no other visual or audio changes.
```

Treat preservation wording as intent, not a hard guarantee. Probe actual output frames and duration before conform.

### Extension packet

Reconstruct the source boundary: identity/state, pose, prop owner, positions, motion direction/speed, camera position/velocity, light/color, ambience and audio level. Then specify the new event and a fresh end state. For backward extension, make the source opening the final state of the new material.

Write every boundary attribute as continuation, never as a fresh specification, and watch optics in particular. A focal length or aperture restated in the ordinary declarative form reads as a new setup and can produce a visible optical change at exactly the join the extension exists to hide. Phrase it as inheritance — continue the source's lens and aperture; do not change focal length or depth of field — and give grade, ambience and level the same treatment. This is a drafting practice, not a measured result: the same value stated two ways is being treated as two different instructions because one of them announces a setup, and no controlled comparison of the two phrasings has been run.

## Extension direction and boundary

For a bare request to continue forward or backward, do not assume or infer a before/after boundary. Ask one before/after boundary question: “Should the new material go before or after the supplied source?” Do not draft an extension until that answer identifies the side.

Chinese phrases such as `向前續寫`, `向後續寫`, `往前延長`, and `往後延長`, and equivalent bare forward/backward wording in any language, are ambiguous direction labels. They do not establish which source boundary to use. A prompt-only or “final prompt only” request does not override this boundary question: ask it once and stop before drafting.

For an explicit **append**, describe only the added interval after the source and preserve the source material. For an explicit **prepend**, describe only the added interval before the source and preserve the source material. In either case, reconstruct the adjoining boundary only to make the new interval connect; do not restate, replay, or alter the existing source.

After the boundary is confirmed, use only `before the source` or `after the source` language. Do not retain forward/backward direction labels in the final artifact.

### First/last packet

Use strict roles only when the platform documents them. If images are merely semantic references, call the alignment approximate. Specify a plausible causal bridge rather than requesting a teleport between incompatible states.

## Generic conditional packets

These are generic intent packets, not a provider or platform support claim. Use one only when the selected runtime has a documented task that can receive it; otherwise preserve it as a production brief without implying a UI feature or capability. [PD-16]

- **Marked edit** — name the annotation, target, A→B change, time scope, and preserve list. The annotation identifies the intended region; it does not prove a provider can read a mark.
- **Transition bridge** — keep two sources unchanged; state the exit from source A, the full bridge event, and the entry to source B. Match the connection object's screen position, scale, direction, speed, motion trend, camera vector, light, and audio across both joins.
- **Coarse clay/blockout** — map every model, shape, or object to its final entity. Inherit only the required paths, blocking, scale relationships, camera, cuts, or timing; exclude primitive or gray materials, guide lines, viewport texture, and other overlays. [PD-10]
- **Fine clay/blockout** — preserve the completed structure, actions, spatial relationships, camera, composition, and cuts. Change only the requested appearance, material, environment, light, or final rendering, and exclude guide lines, coordinate axes, camera cones, and production overlays. [PD-10]
- **Ordered storyboard** — for a single generate clip, declare the reading order and treat each panel as one complete planned shot. Give every panel a composition, action, and end state; exclude line art, annotations, and placeholder characters unless the user assigns one of those a role. A multi-shot production storyboard belongs with `seedance-film-producer`, which owns cross-shot planning and continuity.

## Acceptance gate

A prompt is ready only if a reviewer can answer yes/no to all material items:

- Every clause is executable by a reader holding this submission alone — the text plus the assets submitted with it: no pointer to a document that was left behind, and no bound on a diffuse feature — marks, cracks, tears, patches, stains, wear — whose only content is how many there are.
- Required entities and counts are explicit; forbidden duplicates or intruders are scoped. Entity counts, positive and negative alike, are unaffected by the clause above.
- Every exclusion states what it binds, and no exclusion contradicts a requirement in a later unit of the same artifact.
- Every active reference has exactly one understandable job and inheritance boundary.
- Start state, primary delta, causality, and end state are visible.
- Space, axis, direction, eyeline, entrance/exit, and prop ownership do not conflict.
- Camera and action are not competing or mutually exclusive.
- Dialogue speaker, language/accent, exact text, silence, subtitles, BGM, ambience, and SFX are resolved.
- Runtime claims are verified for the actual platform/model/date or labeled unknown.
- High-risk failures have a split/input/post-production route and a finite retry policy.
