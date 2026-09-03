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

## Reference authority

Name, for each attribute class the film must hold — identity, wardrobe, geometry, material, palette, grade, voice, motion — the single authority of record: an approved asset, or the prompt text. Record it in the bible. Never specify the same class in both channels; when they disagree, no record can say which one the take obeyed. A class established in pixels during asset preparation is thereafter carried by reference and dropped from prompt text.

- Scope a reference's authority to named classes, per use, and scope it by default: an asset confers no camera position, framing, composition, or crop unless the shot contract grants it. Keep that exclusion in the registry entry, not only in the prompt.
- One asset may be admitted on one channel and barred on the rest — its picture but not its sound, its geometry but not its light. Register admitted and denied channels per use, because the same asset can hold different authority in different shots.
- Where the interface binds references by position rather than by name, attachment order is part of the contract. Record the ordered packet and reproduce it exactly on retry, or the runs are not comparable.
- The provider's asset record is not the registry. Its category may be machine-assigned, its description empty, its name whatever the uploader typed; none of that is evidence of what the asset may govern, and some projects register no assets with the provider at all. Class, role, admitted channels, version, and rights live in the production registry and are restated in the input packet.

## Prompt blocks as versioned assets

Long shot prompts are assembled, not written. Any constraint block that recurs across shots is an asset: stable ID, version, owner, state, hash, and the passport version it was derived from. A shot's submitted text is a composition — an ordered list of block versions plus that shot's own delta text. Which categories of block a project keeps, and what they say, is the project's business; only the way blocks are identified, versioned and recorded is general.

- Record the composing block IDs and versions in the run ledger beside the prompt hash. Without them, one changed variable cannot be audited inside a long prompt, and two runs differing by one line read as two unrelated texts.
- Editing a block creates a new block version and marks every shot composed from the previous version stale. Decide per stale shot: re-render, or keep the approved take and pin it to the block version it actually used.
- When a shot must depart from a standing block, write the departure as an explicit precedence declaration that names the rule it supersedes, rather than as a contradicting line appended to the tail. A named supersession is auditable and survives recomposition; a bare contradiction leaves a hash describing text the run never honored.
- Fold a correction back into the block once it stops being a one-shot exception and starts recurring. A block that has accumulated per-shot patches has lost its authority as an invariant.
- A block rewritten in another authoring language is a language variant of the same block ID. Any count or audit that scans prompt text must be language-aware; do not trust a platform-supplied language field, which may report a single language for a mixed-language project.
- A block states values, never citations. Where the authority of record for an attribute class is the prompt text, the block carries that class's literal values and never refers to the passport, to another block, or to what an earlier block already said: a citation is legible to whoever maintains the registry and to nothing downstream, so a bound expressed as a citation binds nothing once the composition is submitted. Where the authority of record is an approved asset, the class stays out of the block entirely under **Reference authority** — resolving it into text there would put the same class on two channels. The derivation itself lives in the block's metadata, never in the text that gets sent.
- Blocks carry project vocabulary, not craft rules. Version them with the bible and keep them inside the project.

Block composition is a production hygiene control for attribution and rollback. No controlled evidence links it to output quality; do not present it as a quality lever.

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

### Conditioning before promotion

A candidate may need a bounded conditioning pass before it can serve as approved memory: removing an overlay, badge, or incidental marking the generator added, cropping to the usable region, or repairing one local defect. Conditioning is neither editing nor re-authoring:

- the conditioned asset is a new version whose parent is the accepted source, with the single operation recorded;
- it is bounded to the named operation and may not touch identity, wardrobe, state, or geography; a candidate needing more than that fails promotion instead;
- the unconditioned source is retained, because it, not the repair, is what the run produced.

Run asset preparation as its own lane, with its own queue, ceiling, and reviewer. Preparation is many short single-operation commands against existing images, a register quite distinct from long shot specifications; mixing the two makes cleanup register as shot retries and inflates the shot ledger.

## Continuation relation and accepted-state firewall

Choose one continuation relation before preparing inputs: same-shot seamless, intentional next shot, bridge known states, repair tail, or reanchor drift. The relation names editorial intent; it does not imply a provider feature. [FP-15]

Use same-shot seamless only inside the same scene when geography and open motion genuinely continue. A scene boundary defaults to an intentional next shot, which may preserve story continuity without promising frame continuity.

An accepted source carries its existing state. Prompt text describes only the delta required after that accepted state, rather than replaying the full source contract. A rejected output is diagnostic evidence only and never becomes canonical, approved memory, or a handoff source. [FP-05]

Do not put a numeric retry, chain, work-slice, or review-cycle ceiling into the production deliverable unless the user or project provided it. Internal agent execution defaults stay outside the deliverable. When the production ceiling is absent, keep it unknown and request it only when it changes the plan. [FP-14]

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
invariants: [WARDROBE-A@v3, KEYLIGHT-SC023@v2]
population: {people: 2, key_props: 1, closed: true}
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
prompt text/hash, prompt_block_ids/versions, parameters,
reference IDs/hashes/roles, one changed variable, retry_class,
delivered_shot_ids/in-out, output path/hash/duration/spec,
queue/generation/review/human time, billed cost,
hard gates, scores, timecoded defects, reviewer, decision, route
```

Input packet fields:

```text
reference_id, version, packet_order, role, allowed_attributes, excluded_attributes,
sha256, rights
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
