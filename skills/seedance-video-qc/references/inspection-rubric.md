# Inspection rubric and report schema

Read this file when auditing a generated clip or multi-shot sequence.

## Evidence intake

Record exactly what is available:

- original prompt and runtime platform/model/version/parameters if visible;
- reference assets and intended roles;
- full video and actual audio, or only a subset of frames/screenshots;
- opening, representative middle, ending, every transition, and high-risk action/dialogue/text timecodes;
- neighboring shot/end-state requirements;
- delivery, rights and acceptance criteria.

If evidence is incomplete, continue with bounded findings and label uncovered dimensions unknown. Do not turn the user's failure description into a direct visual observation.

Evidence-resolution rules:

- a screenshot can prove visible state only at that frame;
- spaced frames can suggest but not prove continuous motion, stability, physics or lip-sync;
- an unmuted/player icon proves player state, not audio presence or quality;
- actual audio, decode/waveform/ASR or human listening is needed for audio claims;
- automatic metrics and thumbnails are secondary diagnostics, not approval evidence;
- one qualifying frame settles a presence requirement, but no finite sampling settles a prohibition: report every absence result as bounded by the interval covered and the frame area actually inspected, never as proven absence;
- coverage has a spatial axis as well as a temporal one: a single frame or a single region breaks a suppression requirement, so partial coverage never clears one; [QC-21]
- a reduced-tier run and a delivery-spec run of the same contract are not interchangeable evidence.

A run at lower resolution, shorter duration or a draft quality setting can settle coarse adherence — entity presence and count, blocking, action and beat order, gross camera behavior, obvious prohibition violations. It cannot clear fine artifacts, small or short-lived characters, finger and contact anatomy, grain and texture, edge quality, or lip-sync. Say which dimensions the reduced-tier evidence cleared, and label the rest unknown at delivery spec. A pass earned at a probe tier never transfers to the delivery master: the master is re-inspected on exactly the dimensions the tier could not settle, and the verdict names both scopes. [QC-26]

**Reconcile the declaration surfaces, then test satisfiability.** Timing, length, format and take structure may be declared in the prompt text, in the runtime parameters, or in both, and where both carry the same spec the two can disagree. Some contracts state none of this in text and leave it entirely to the parameters; that silence is a drafting choice, not a defect, and there is nothing to reconcile. Where the text does declare any of it, check before scoring adherence that the contract was satisfiable as issued:

- does the written schedule fit inside the requested runtime;
- do the declared take structure and the requested duration and format agree;
- can the number of state changes asked for occur in the time available.

If the contract over-books its own runtime, the missing material is a contract defect. It routes to a contract fix, not to a regeneration, and charging it to the model is a misdiagnosis that no number of retries will correct. Record it as a finding against the contract, quoting both declared values and naming the surface each came from.

Where the surfaces agree, score them separately: against any written schedule, each beat's presence, order and realized time; against the parameters and the delivered file, total length, aspect, format and take structure. A beat that occurred but landed materially off its scheduled time is an adherence finding with an editorial consequence, not a cosmetic one. [QC-24]

## Hard gates

Fail before averaging if any material gate is unmet:

1. rights, safety, policy, delivery or required media specification;
2. correct required entities/identity/reference roles, with no critical extra entity;
3. required story beat and causal action result;
4. correct continuity-critical wardrobe/injury/prop/location/direction/end state;
5. no uneditable structural failure, severe artifact, wrong text/subtitle, or broken audio;
6. an editorially usable interval/transition or an approved repair route.

A beautiful but wrong character, missing prop, wrong end state, or unusable cut remains a failure. Where the reconciliation step under Evidence intake shows the contract was not satisfiable as issued, the resulting gap is reported as a contract defect and routed to a contract fix rather than counted as a gate failure of the take. [QC-24]

### Gates declared by the contract

Before applying the default gate list, harvest the gates the contract already states. Two forms occur: a named condition the contract declares sufficient on its own to reject the shot, and a block carrying a precedence or severity marker that the contract asserts governs where its own clauses conflict. Both are gates for this review, checked by name and reported individually.

An author-declared precedence is not silently replaced by the default one. A defect on a constraint the contract declared rejecting is a gate failure even where the default list would rate it Minor; a defect on a constraint the contract marked preferred rather than absolute is reported as a score, not as a blocker. Where the two orderings disagree, report both readings and state which one the verdict used.

When the contract declares no precedence, state the gate list applied before scoring, so the user can correct it rather than infer it from the verdict. [QC-19]

## Dimensions

Use pass/fail for acceptance and optionally 1–5 for comparison. Every score cites timecoded evidence.

### Prompt adherence

- exact entity counts and required/forbidden presence;
- reference identity/role fidelity;
- start state, action order, direction, contact/result and end state;
- camera, light/style, audio/dialogue/subtitle requirements.

**Check prohibitions one at a time.** Collect every exclusion the contract states, in whatever form it takes: a labeled exclusion section, a rider attached to one shot or panel, a positive requirement stated together with the counter-case it rejects, or an inventory the contract declares complete. For each, record the prohibited observable, the scope it binds (whole delivery, one shot, one interval, one entity), the evidence actually examined, and a verdict of pass / violated / not checkable. Never collapse the set into a single "no violations found".

A prohibition can bar anything the contract is able to name, not only entities. Whenever the contract negates something, restate that negation as a test another reviewer could run on the same evidence and reach the same verdict; where you cannot, record it as not checkable and say what evidence would settle it. Negated camera behavior, negated editorial events, negated color, negated legibility of lettering or captions, and negated styles all convert this way. Treat that as illustration, not as the list to check — the list to check is whatever this contract negates.

Separate two failures that look alike. A prohibition you cannot restate as a test another reviewer could run is *not checkable* — a limit on the review. A prohibition the generator could not have executed reading it alone is *inert*, and its violation is a finding against the contract rather than against the take. Inertness is established where the clause points at a document that was not submitted with it, since nothing at the other end of the pointer reached the generator; it is only suspected where the clause bounds a diffuse feature by how many there are, a reading that rests on an uncontrolled observation rather than a controlled comparison. Record which of the two applies and, for an inert clause, whether the inertness is established or suspected; they route differently. [QC-28]

Where the contract declares a list complete, the burden inverts: anything present in the evidence but absent from the list is a finding in its own right, independent of how well it is rendered. Report unlisted additions and unmet requirements as two separate lists, because they have different causes and different repairs. [QC-20]

**Reference audit.** Test the binding before judging fidelity, and record each result as its own finding class:

- *unused* — an asset was supplied but none of its declared attributes is visible; the roster and the output disagree about what was in play;
- *misbound* — a supplied attribute landed on a different element than the one it was assigned to;
- *conflated* — two distinct references resolved into one blended entity, or one reference split across two;
- *over-inherited* — the asset contributed on a channel it was not granted.

Then audit inheritance per channel. For each reference, record which channels the contract granted it — identity, geometry, material, palette, light, motion, voice — and check each granted channel for under-inheritance and each ungranted channel for leakage. Extend the check to the channels a contract usually leaves unnamed: an asset's own framing, camera position and lighting can arrive alongside the attribute that was actually wanted, so inspect them even when the contract says nothing about them.

Where the contract grants no channels and addresses a pile of assets collectively, say so. Adherence is then unscorable per asset; only the aggregate result can be judged, and "which asset caused this" stays unknown rather than being guessed. [QC-22]

### Multi-unit generations [QC-23]

Some generations declare more than one internal unit: the prompt segments itself into ordered parts, each carrying directions of its own, however that segmentation happens to be marked. When it does, evaluate the unit structure before the unit content:

- how many units were declared, in what order, and where each boundary actually landed in the result;
- whether a boundary required to be a discrete change of setup is one, rather than being served by a blended or uninterrupted substitute — a morph, a dissolve, a camera move that carries through — and whether any boundary appeared that was never declared;
- each unit against only the clauses that bind it.

Bind every clause to its declared scope before scoring. A clause stated for the whole generation is checked in every unit; a clause stated inside one unit is charged only against that unit. A later unit may legitimately contradict an earlier one: when the declaration itself holds an attribute fixed in one unit and calls for it to change in the next, the change is compliance, not a continuity failure. A finding filed against the wrong unit is a reporting error, not a lenient call.

Report per unit, then per job. A job whose units are each acceptable can still fail on structure, and one failed unit does not condemn the rest when its boundary is cuttable.

### Continuity

- identity/face/hair/build and voice;
- wardrobe, accessories, wet/damaged/injury/age state;
- prop geometry/count/state/owner/hand;
- location geometry/landmarks/weather/time/light;
- blocking, axis, screen direction, eyeline, entrance/exit;
- action/camera velocity, room tone and neighbor edit.

Verify fidelity to the correct entity before measuring self-consistency. A consistently wrong person does not pass continuity.

### Temporal stability and anatomy

- flicker, morphing, texture crawl, popping/disappearance;
- face/body/limb/finger topology and contact anatomy;
- object permanence, duplication and reflection copies;
- short-lived text/UI errors, motion blur and edge artifacts.

Sampling density must match the risk. Sparse frames are insufficient for fast fingers, short text, transitions or lips.

Prohibitions drive sampling density rather than inheriting it: choose the interval and rate from the prohibition list, not from the action. Cover the frame as well as the timeline — a scene-wide exclusion, a suppression requirement or a closed inventory can be broken anywhere in the rectangle, so inspect periphery and corners, background population, reflective and out-of-focus areas, and any surface able to carry marks or characters, not only the subject. State the covered interval and the inspected areas in the verdict, alongside the evidence modality. [QC-21]

### Physics and action [QC-08]

- trajectory, speed/acceleration and gravity;
- visible contact before response;
- weight, momentum/inertia, follow-through and balance;
- material deformation, liquid/particle response and stable result;
- coherence between camera motion and subject motion.

Describe visible failure directly; label its cause as hypothesis.

### Camera and optics [QC-10]

- shot size, camera side/height/angle and intended lens feel;
- movement type/direction/speed, stability and focus target;
- axis/eyeline and transition/cut function;
- whether camera complexity hides or causes action unreadability.

### Observable acting [QC-09]

- gaze target and eye-before-head timing;
- hand task, breath, blink, swallow, tension/release;
- reaction delay, tempo, tactic and clear state change;
- line attribution and silence of non-speakers.

Do not score an emotion adjective; score the requested visible behavior.

### Text and subtitles [QC-11]

- exact string, language, spelling, glyph stability and placement;
- timing, speaker, punctuation, line break, safe area and occlusion;
- consistency across frames/cuts and burned/sidecar requirement.

### Audio, dialogue and lip-sync

- audio stream/decode integrity;
- exact words/language/accent, speaker attribution, voice identity/naturalness;
- speech timing, mouth movement and phoneme-level sync when evidence permits;
- mouth movement in figures the contract lists as carrying no line;
- jaw, dentition or mouth-shape deformation at syllable peaks, reported against the identity gate rather than against sync;
- SFX causal alignment, room-tone/ambience continuity, music and level/seam;
- no unrequested dialogue, BGM, subtitles or silence.

Do not generalize a coarse mouth-motion correlation to exact dialogue or phoneme sync.

### Editorial usability

- complete usable interval, clean in/out, handles and stable ending;
- match to neighboring pose/state/direction/eyeline/camera/light/audio;
- where the generation declares internal units, whether a failed unit is cuttable without losing the rest;
- whether a local repair, insert, cutaway, reframe or VFX route preserves the shot;
- manual fix cost/time versus regeneration/redesign.

### Delta edits against a supplied source [QC-27]

When the job is a scoped change to a supplied image, frame or clip rather than a fresh render, inspect it as a differential:

- did the requested change occur, within the scope stated;
- what else changed. Enumerate every difference outside the declared change scope; each is a finding regardless of whether it is attractive. Where the contract names no preserve set, everything outside the named change is the preserve set by default.

Unchanged-ness cannot be judged from memory or from a description of the source. It requires the source and the output inspected together, aligned frame to frame, and across the same interval for a moving source. Without the source in hand, out-of-scope drift is unknown, not absent, and the verdict says so.

Report the change and the drift as separate findings. They route differently: a correct change riding on unrequested drift may still be unusable, and re-issuing the edit is not the same action as re-scoping it.

## Severity

| Severity | Meaning |
|---|---|
| Critical | Wrong version attribution, fabricated capability/parameter/evidence, rights/data leak, missing primary entity/reference role/end state, or structurally unusable required beat |
| Major | Blocks approval/cut but has a plausible regeneration/redesign/VFX route |
| Moderate | Material deviation requiring local repair or pickup |
| Minor | Cosmetic defect that does not break meaning, continuity or delivery |
| Unknown | Evidence cannot support pass or fail |

## Finding schema [QC-18]

```text
Finding ID / dimension / severity / acceptance impact
Evidence modality and exact timecode/frame
Direct observation:
Defect distribution across takes / clip / frame:
Inference or root-cause hypothesis:
Unknown / missing evidence:
Minimal next action:
Route: accept / edit / repair / regenerate / VFX / redesign
Changed variable:
Fixed invariants:
Stop condition:
```

## Verdict

Return `PASS`, `FAIL`, or `CONDITIONAL` only for the reviewed evidence scope. Summarize blockers separately from numeric scores. A high mean never clears a failed hard gate.
