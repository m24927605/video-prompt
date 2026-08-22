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
- automatic metrics and thumbnails are secondary diagnostics, not approval evidence.

## Hard gates

Fail before averaging if any material gate is unmet:

1. rights, safety, policy, delivery or required media specification;
2. correct required entities/identity/reference roles, with no critical extra entity;
3. required story beat and causal action result;
4. correct continuity-critical wardrobe/injury/prop/location/direction/end state;
5. no uneditable structural failure, severe artifact, wrong text/subtitle, or broken audio;
6. an editorially usable interval/transition or an approved repair route.

A beautiful but wrong character, missing prop, wrong end state, or unusable cut remains a failure.

## Dimensions

Use pass/fail for acceptance and optionally 1–5 for comparison. Every score cites timecoded evidence.

### Prompt adherence

- exact entity counts and required/forbidden presence;
- reference identity/role fidelity;
- start state, action order, direction, contact/result and end state;
- camera, light/style, audio/dialogue/subtitle requirements.

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
- SFX causal alignment, room-tone/ambience continuity, music and level/seam;
- no unrequested dialogue, BGM, subtitles or silence.

Do not generalize a coarse mouth-motion correlation to exact dialogue or phoneme sync.

### Editorial usability

- complete usable interval, clean in/out, handles and stable ending;
- match to neighboring pose/state/direction/eyeline/camera/light/audio;
- whether a local repair, insert, cutaway, reframe or VFX route preserves the shot;
- manual fix cost/time versus regeneration/redesign.

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
