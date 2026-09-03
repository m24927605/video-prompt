Use a serialized, append-only state chain:

`dry/unsealed → dry/sealed+pocketed → wet/sealed+pocketed → wet+injured/sealed+pocketed → wet+injured/sealed/Tomas → wet+injured/open/Tomas`

Every approved shot creates a new immutable continuity snapshot. Later shots may inherit it, but never modify it.

## Production assumptions

- Plan date: 2026-09-01.
- Platform/model, delivery format, duration limits, audio mode, region, rights, and budget are not yet specified. Lock these before enqueueing generation.
- Working mode: hybrid. Shots 3–5 are Tier A because fence contact, injury, hands, prop transfer, and opening are continuity-critical; shots 1–2 are Tier B.
- No paid generation is authorized by this plan.
- Default execution limits if production begins without another budget: 90 minutes per bounded work slice and no more than two complete cut/review cycles. A per-shot run ceiling remains unset until platform cost and delivery time are known.

## Hierarchy and spatial rule

```text
FILM-BLUE-ENVELOPE
└── SQ-010 Escape and delivery
    └── SC-010 West-to-east exterior route
        ├── BT-01 Secure envelope      → SH-010
        ├── BT-02 Rain begins          → SH-020
        ├── BT-03 Fence injury         → SH-030
        ├── BT-04 Envelope transfer    → SH-040
        └── BT-05 Envelope opened      → SH-050
```

Screen-direction contract:

- Nia’s route is west-to-east, always screen-left to screen-right.
- Cameras remain on the south side of the west/east action axis.
- Tomas waits east of the fence: Nia remains frame-left and Tomas frame-right.
- Tomas looks screen-left; Nia looks screen-right.
- Use front-biased three-quarter views when the left-cheek injury must be legible; do not mirror references or cross the axis.
- Shot 3 may briefly become near-frontal during the climb, but Nia must land and continue toward screen-right.

## Immutable asset registry

Each row becomes a separately approved asset with its own file, version, status, rights record, and SHA-256 hash. Never combine conflicting states on one reference sheet.

| Entity | Asset ID | State |
|---|---|---|
| Nia | `CHAR-NIA-v001` | Stable face, hair, build, handedness, gait |
| Tomas | `CHAR-TOMAS-v001` | Stable identity and receiving-hand behavior |
| Coat | `WARD-NIA-COAT-DRY-v001` | Cream coat, completely dry |
| Coat | `WARD-NIA-COAT-WET-SHOULDERS-v001` | Same coat; rain-darkened shoulders only |
| Injury | `INJ-NIA-CLEAR-v001` | No facial injury |
| Injury | `INJ-NIA-LEFT-CHEEK-CUT-v001` | Fresh, localized cut on left cheek |
| Envelope | `PROP-ENV-BLUE-UNSEALED-v001` | Blue envelope, flap open |
| Envelope | `PROP-ENV-BLUE-SEALED-v001` | Same envelope, seal visibly intact |
| Envelope | `PROP-ENV-BLUE-OPENED-v001` | Seal broken and flap open |
| Weather | `WX-DRY-v001` | No rain |
| Weather | `WX-RAIN-ONSET-v001` | First visible rainfall |
| Weather | `WX-RAIN-CONTINUING-v001` | Continuing rain; no spontaneous drying |
| Location | `LOC-ROUTE-v001` | Shelter, alley, fence, Tomas position, west/east axis |
| Camera | `CAM-SC010-v001` | South-side camera zone and left-to-right travel |
| Sound | `SND-SC010-RAIN-v001` | Dry ambience → rain onset → continuous rain |

Ownership, pocket location, pose, and geography live in continuity snapshots—not inside the prop artwork.

Reference packets include only the exact applicable state assets. For example, Shot 4 receives the wet-coat and left-cheek-cut references; it must not receive the dry-coat or clear-cheek references.

## Shot manifest

| Shot | Start state and required action | Approved end state | Forbidden state | Camera and handoff |
|---|---|---|---|---|
| `SH-010` | Nia wears `COAT-DRY`; face clear; owns unsealed blue envelope. She seals it and immediately secures it in her right inner pocket as one continuous “secure the message” action. | Coat dry; no injury; envelope sealed, owned by Nia, inside right inner pocket. | Rain, wet coat, cheek wound, Tomas, open envelope at end, left pocket, duplicated envelope. | Medium-close from south side. Nia faces/moves screen-right. End with a clean tail showing her right hand leaving the closed right inner pocket. |
| `SH-020` | Inherit Shot 1 exactly. Rain begins; Nia continues screen-right without touching the pocket. | Shoulders visibly wet; lower coat not arbitrarily soaked; face clear; sealed envelope remains in right inner pocket, owned by Nia. | Dry shoulders at end, injury, exposed/open/wet envelope, pocket switch, Tomas, travel toward screen-left. | Medium tracking shot; spatial master for the route. Rain onset and wetting are the only new state. |
| `SH-030` | Nia arrives wet-shouldered, uninjured, with coat closed over the sealed envelope. She climbs the fence toward screen-right and a fence edge cuts her left cheek. | Nia lands east of the fence; fresh left-cheek cut; shoulders remain wet; sealed envelope remains in right inner pocket and owned by Nia. | Right-cheek wound, healed/old wound, dry coat, envelope exposure or duplication, left-pocket placement, Tomas, reversal toward screen-left. | Stable medium-wide or restrained tracking. Show credible contact, then a front-biased three-quarter view of the left-cheek cut. Do not let the fence reverse her travel direction. |
| `SH-040` | Nia, still wet and injured, approaches Tomas. She retrieves the visibly still-sealed envelope from her right inner pocket with her right hand and gives it to Tomas. | Tomas owns and holds the sealed envelope; Nia holds none. Her shoulders remain wet and left-cheek cut remains fresh. | Left-hand delivery, open/broken seal, envelope duplication, envelope still in Nia’s pocket at end, dry/healed Nia, position swap. | Two-shot: Nia frame-left, Tomas frame-right. Tomas receives toward frame center. Ownership changes only when Tomas closes his hand and Nia releases. |
| `SH-050` | Tomas begins as sole owner of the sealed envelope. Nia remains visible frame-left with wet shoulders and left-cheek injury. Tomas opens it. | Tomas owns the now-open envelope. Nia remains wet and injured without changing position or state. | Sealed envelope at end, Nia holding it, premature opening before shot start, healed/dry Nia, missing Nia, duplicated envelope, axis reversal. | Front-biased two-shot or over-Nia composition: Tomas and the opening action dominate frame-right while Nia’s wet shoulders and left cheek remain readable. Do not reveal unspecified letter text. |

The envelope’s sealed condition while pocketed in Shots 2–3 is inherited from the accepted Shot 1 action and the absence of any approved removal delta. It should not be claimed from an invisible pocket alone. Shot 4 must visibly reconfirm the intact seal when the envelope reappears.

## State snapshots and handoffs

```text
STATE-v001  pre-SH010: Nia / dry / clear / unsealed envelope / Nia owns
STATE-v002  post-SH010: Nia / dry / clear / sealed / right inner pocket / Nia owns
STATE-v003  post-SH020: Nia / wet shoulders / clear / sealed / right inner pocket / Nia owns
STATE-v004  post-SH030: Nia / wet shoulders / left-cheek cut / sealed / right inner pocket / Nia owns
STATE-v005  post-SH040: Nia wet+injured / sealed envelope / Tomas owns
STATE-v006  post-SH050: Nia wet+injured / opened envelope / Tomas owns
```

Each local handoff package contains:

- Approved source run and output hash.
- Approved end-state snapshot and hash.
- Last useful pose/frame and its timecode.
- Character positions, gaze, screen direction, camera side, and motion vector.
- Coat, injury, weather, prop-state, owner, hand, and pocket fields.
- Neighboring room tone and rain intensity.
- Explicit inheritance exclusions.

The handoff frame guides adjacent pose and motion only. It cannot override canonical identity or state assets.

## Queue and approval firewall

The generation queue is strictly serialized:

`SH-010 → approve STATE-v002 → SH-020 → approve STATE-v003 → … → SH-050`

Before the full queue:

1. Validate the shot-contract and reviewer schemas on a minimal fixture.
2. Compile and review the representative `SH-010 → SH-020` transition.
3. Lock the wet-coat interpretation and handoff format.
4. Continue to Shots 3–5 only after that path works end to end.

For every shot, inspect the opening, middle, end, high-risk action, and cut to both neighbors. Hard gates precede aesthetic scoring:

- Correct identities and exact state assets.
- Required action completed once.
- Forbidden state absent.
- Correct screen direction, geography, hand, pocket, and ownership.
- No uneditable anatomy, contact, physics, or prop-duplication defect.
- Usable opening/end handles and neighbor compatibility.

Only approved outputs create a new state. A rejected take cannot become canonical truth, approved memory, or the source of the next shot.

## Versioning and retry lineage

Suggested naming:

```text
FILM-BLUE_SH-030_take-002_run-r003_prompt-p002_ref-r004_v001.mov
FILM-BLUE_STATE-SC010_v004.yaml
FILM-BLUE_PROP-ENV-BLUE-SEALED_v001_APPROVED.png
```

Rules:

- Stable shot and asset IDs are never reused.
- Changing wetness, injury, seal condition, ownership logic, or screen axis requires a new semantic version.
- Prompt, reference packet, output, and continuity snapshot have separate versions and hashes.
- Status metadata is authoritative; filenames are only readable labels.
- Do not use a mutable `latest` render as an input.
- Retry one variable at a time: prompt, state reference, camera, duration, or shot design.
- A retry always regenerates from the prior approved state—not from a rejected child.

Example for Shot 3:

```text
SH030/r001
  source_state: STATE-v003
  source_run: approved SH020/r004
  decision: rejected — right-cheek injury

SH030/r002
  source_state: STATE-v003
  source_run: approved SH020/r004
  retry_of: SH030/r001
  one_change: stronger left-cheek spatial constraint
```

If the same blocking defect persists, route to a cleaner state asset, locked camera, shorter fence action, or bounded VFX cleanup. Adding a sixth cutaway requires an explicit scope change because the canonical structure is five shots.

## Rollback

Create immutable checkpoints after bible lock, previz lock, every approved shot, picture structure lock, finishing lock, and final master.

- Shot 4 failure: discard nothing; mark the run rejected and retry from the approved Shot 3 checkpoint.
- Shot 5 failure: return to the approved Shot 4 checkpoint.
- Axis, coat, or injury corruption: return to the last valid scene checkpoint and replay only accepted deltas.
- If the wet-coat asset itself is wrong, retire `WET-SHOULDERS-v001`, create `v002`, and invalidate Shots 2–5 as descendants. Shot 1 remains valid.
- If the left-cheek asset changes, invalidate Shots 3–5 only.
- A platform/model update creates a new branch and regression test; it never replaces approved renders.
- Reopened semantics are repaired and retested before hashes, manifests, or blind-review bundles are resealed.

## Editorial and archive

Build a five-shot blocking cut before final-quality upgrades. Check the rain onset, fence geography, right-hand transfer, and Shot 4–5 seal match in sequence. After structure lock, use cleanup/VFX for bounded defects, match wetness and skin tone in color, carry rain ambience continuously from Shot 2, and add fence/coat/envelope foley. Subtitles are unnecessary unless dialogue is later introduced.

The run ledger should record actual approvals, retries, time, cost, defects, and routes. Report first-pass approval, retries per approved shot, continuity defects, usable seconds, human correction time, and waste rate only from that ledger—never from estimates. Archive all state snapshots, hashes, source and selected renders, rejected-run decisions, timeline, audio, approvals, and rollback checkpoints.
