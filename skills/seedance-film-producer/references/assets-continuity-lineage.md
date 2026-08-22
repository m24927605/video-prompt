# Assets, continuity, lineage, and rollback

Read this file when building the creative bible, asset registry, scene state, shot handoffs, generation ledger, or recovery plan.

## Creative-bible passports

Every passport has a stable ID, version, owner, rights status, `draft/approved/retired` state, approval date, and hashes.

### Character and voice

- face/hair/skin/build/posture/handedness/gait and stable identifying traits;
- approved front, profile, three-quarter, full/medium/close and expression references;
- voice language/accent/register/timbre/tempo/pronunciation dictionary and rights;
- observable behavior grammar: gaze, breath, blink, hands, tactics, reaction timing;
- closed wardrobe and accessories, plus state-specific wet/damaged/injured/aged versions;
- forbidden drift and recurring blocking/eyeline relationships.

### Location, prop, and look

- location floor plan, entrances/exits, axis, camera positions, landmarks, materials, light direction, weather/time states, room tone;
- prop geometry/scale/material/moving parts, owner/hand, appearance/disappearance and state machine;
- exact graphics as clean artwork for post when text fidelity matters;
- camera grammar, style/material contract, color script, VFX grammar, sound bible and subtitle style.

A new wardrobe, injury, weather, lighting, or prop state is a new asset/version. Do not overwrite the base state or combine conflicting states in one sheet.

## Three distinct continuity stores

### Canonical bank

Human-approved identity, location, prop, voice, style, and state truth. A generation can never replace it automatically.

### Approved memory

A small set of high-information frames or clips promoted from accepted shots only after:

- correct identity/entity/location fidelity;
- no disqualifying artifact or motion blur for its intended use;
- prompt/story adherence and cross-shot compatibility;
- source shot/timecode/crop/use boundary recorded.

### Local handoff

Transient neighbor state: last approved pose/frame or action tail, positions, screen direction, camera velocity, light/color, prop owner, and room tone. It serves adjacent continuity and never overrides canonical truth.

These stores are an external production design inspired partly by long-video research; they are not claimed as Seedance internals. `return_last_frame`, where documented, is only transport. A last frame must pass QC before promotion.

## Continuity state and entity schedule

```yaml
scene_id: SC-023
story_time: "Day 4 / dawn"
location_state: LOC-007-dawn-rain-v02
screen_axis: door-to-window
characters:
  CHAR-001:
    position: frame-left beside table
    wardrobe: WARD-001-wet-v03
    injury: INJ-001-cheek-cut-v01
    gaze: CHAR-002
    held_props: [PROP-014-letter-open]
props:
  PROP-014:
    state: open
    owner: CHAR-001
    hand: right
lighting: LIGHT-SC023-window-left-v02
audio: SOUND-SC023-rain-roomtone-v02
```

```yaml
shot_id: SH-023-040
required: [CHAR-001, CHAR-002, PROP-014, LOC-007]
forbidden: [CHAR-003, PROP-014-letter-sealed]
start_state: CHAR-001 holds the open letter in the right hand
primary_delta: PROP-014 transfers to table center
end_state: both characters remain seated; letter lies open at table center
entrance_exit: nobody enters or exits
```

Each shot reads the prior approved state and submits exactly its approved delta. Scene rollback replays only accepted deltas from the checkpoint.

## Registry and run ledger

Asset registry fields:

```text
asset_id, entity_id, state, version, owner, rights_status, source_paths,
allowed_attributes, excluded_attributes, status, approval, sha256
```

Run ledger fields:

```text
run_id, parent_run, shot_id, timestamp, platform/model/document version,
prompt text/hash, parameters, reference IDs/hashes/roles, one changed variable,
output path/hash/duration/spec, queue/generation/review/human time, billed cost,
hard gates, scores, timecoded defects, reviewer, decision, route
```

Never retain credentials, cookies, session material, signed media queries, or private URLs. If provider task/URLs expire, ingest the authorized output promptly, hash it, and retain a sanitized source identifier.

## Stable IDs and filenames

```text
FILM-ORCHID
SQ-030
SC-030-012
BT-030-012-04
SH-030-012-040
CHAR-003 / LOC-007 / PROP-014
```

IDs are never reused because editorial order changes. Status metadata is authoritative; `APPROVED` in filenames is only a readable aid.

Example:

```text
FILM-ORCHID_SH-030-012-040_take-003_run-r017_prompt-p004_ref-r006_model-full-id_720p_v001.mov
FILM-ORCHID_CHAR-003_wardrobe-rain_v005_APPROVED.png
FILM-ORCHID_SC-030-012_continuity-state_v012.yaml
```

## Checkpoints and rollback

Create immutable checkpoints after bible lock, previz/anchor lock, approved-shot lock, picture structure lock, sound/color lock, and final master. Save script/bible versions, state snapshot, approved hashes, timeline/EDL, open defects/routes, budget, tool/model/platform/doc versions and approvals.

Rollback rules, including the extension-chain boundary [FP-15]:

- retry from the parent approved run, never a rejected child;
- if state/axis/wardrobe was corrupted, return to scene-start checkpoint and replay approved deltas;
- after structure lock, require a change record listing downstream VFX/sound/subtitle/color impacts;
- test a model/platform update as a new branch and regression suite; never overwrite approved renders.
