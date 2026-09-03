The Write tool (and plan-file editing) is disabled in this session, so I'll deliver the full continuity plan directly here instead. It follows the seedance-film-producer conventions: the model has no cross-shot memory, so the production system below carries all state.

# Five-Shot Continuity Plan — "The Envelope" (Nia → Tomas)

## 0. Assumptions and unknowns

- Platform/model, aspect ratio, per-shot duration, and budget are unspecified → treat as project-charter gates to lock before generation. Archived Seedance knowledge is dated 2026-08-22; recheck current docs for limits/pricing.
- Retry ceiling: unknown — recorded as a project parameter, not invented.
- Operating mode: **hybrid** — shots 3 and 4 are A-tier (contact/injury and hand-to-hand prop transfer are the highest-failure actions in AI video), shots 1, 2, 5 are B-tier.

## 1. Hierarchy

```
FILM-ENVELOPE
└── SQ-010 "Delivery in the rain"
    ├── SC-010-01  Interior, dry — Nia seals the envelope            → SH-010-01-010
    ├── SC-010-02  Street, rain onset — shoulders wet                → SH-010-02-010
    ├── SC-010-03  Fence, steady rain — cheek cut, envelope pocketed → SH-010-03-010 (+ insert INS-03A)
    └── SC-010-04  Meeting point, steady rain
        ├── SH-010-04-010  handoff                                   (+ insert INS-04A)
        └── SH-010-04-020  Tomas opens; Nia stays wet and injured    (+ insert INS-05A)
```

One primary delta per shot. Shots 1→4 cross scene boundaries, so their continuation relation is **intentional next shot** (story continuity, no promise of frame continuity). Shot 4→5 is inside one scene and may **bridge known states** from shot 4's approved tail frame.

## 2. State-specific assets (versioned passports — a new state is a new immutable version, never an edit of the base)

**Characters**
- `CHAR-NIA` — base passport (face refs, build, right-handed; dry-hair and rain-wet-hair look states as separate reference sheets).
- `CHAR-TOMAS` — base passport. **Forbidden in shots 1–3.**

**Wardrobe (one state per sheet, never combined)**
- `WARD-NIA-COAT-DRY-v1` — cream coat, dry, matte.
- `WARD-NIA-COAT-WETSHLD-v1` — same coat, darkened/saturated **only at shoulders and upper arms**.
- `WARD-NIA-COAT-WET-v1` — rain-soaked shoulders/upper body, damp overall (shots 3–5).

**Injury**
- Base: no facial injury (implicit in `CHAR-NIA`).
- `INJ-NIA-CHEEK-FRESH-v1` — fresh cut, **left cheek**, thin blood line (end of shot 3).
- `INJ-NIA-CHEEK-DRIED-v1` — same cut, identical position/geometry, blood drying and rain-streaked (shots 4–5).

**Prop — `PROP-ENV` (blue envelope) state machine**
```
unsealed → sealed → sealed-pocketed (hidden) → sealed-in-hand → transferred → opened
```
- Versions: `PROP-ENV-UNSEALED-v1`, `PROP-ENV-SEALED-v1` (flap down, intact — kept dry by the inner pocket), `PROP-ENV-OPENED-v1` (torn flap, letter emerging).
- **Ownership ledger:** Nia (shots 1 through the start of 4) → Tomas (end of 4 onward). **Hand:** Nia retrieves and hands off with her **right hand**; Tomas receives with his **left** (his downstage hand on the locked axis below), opens with both.
- If the envelope face carries any legible text/marking, supply it as clean artwork for post compositing — never rely on the model for exact text.

**Locations / weather state machine**
- `LOC-INT-v1`, `LOC-STREET-rainonset-v1`, `LOC-FENCE-rain-v1`, `LOC-MEET-rain-v1`.
- Weather: `dry` (shot 1) → `rain-onset` (shot 2) → `rain-steady` (shots 3–5). Regression is forbidden in every downstream shot.

## 3. Screen direction and axis (locked once, for the whole sequence)

Nia's journey reads **left → right** in every travel shot, and the camera stays on **Nia's left side of the action axis** throughout. This one choice does double duty:

- Her **left cheek is the camera-facing cheek**, so the cut stays visible in shots 3–5 without re-blocking.
- Facing screen-right, her **right arm is the downstage (camera-near) arm**, so the inner-pocket retrieval and right-hand handoff read cleanly.

Shot 4/5 blocking: Nia frame-left facing right, Tomas frame-right facing left, eyelines locked in the scene state. The envelope travels left→right across frame, matching the journey direction.

## 4. Shot manifest — required/forbidden states and handoff deltas

Each shot reads the **prior approved continuity state**; its prompt describes **only the delta**, never a replay of earlier shots' contracts.

| Shot | Start state | Primary delta | End state → handoff | Required | Forbidden |
|---|---|---|---|---|---|
| SH-010-01-010 | Nia dry, uninjured, envelope unsealed in hands | Seals envelope | `PROP-ENV-SEALED`, owner Nia | CHAR-NIA, WARD-DRY-v1, PROP-ENV | rain, wet coat, any facial injury, Tomas, opened/torn envelope |
| SH-010-02-010 | Nia dry; envelope pocketed (right inner pocket, hidden) | Rain begins; shoulders darken | `WARD-WETSHLD-v1`, weather `rain-onset` | CHAR-NIA, LOC-STREET | facial injury, Tomas, visible envelope, fully soaked coat, coat ending dry |
| SH-010-03-010 | Wet-shouldered; envelope pocketed | Fence climb; snag cuts **left** cheek | `WARD-WET-v1` + `INJ-CHEEK-FRESH-v1`; envelope still sealed and pocketed | CHAR-NIA, LOC-FENCE, rain-steady | visible/dropped envelope, dry coat, right-cheek or missing injury, Tomas |
| SH-010-04-010 | Nia wet + `INJ-CHEEK-DRIED-v1`; envelope pocketed | Right-hand draw from inner pocket; hands sealed envelope to Tomas | Owner → **Tomas**, envelope still sealed | both characters, PROP-ENV-SEALED | opened/torn envelope, dry coat, healed/absent/wrong-side cut, left-hand handoff, a second envelope |
| SH-010-04-020 | Tomas holds sealed envelope; Nia in frame, wet + cut | Tomas opens it | `PROP-ENV-OPENED-v1`, owner Tomas | both characters, sealed→opened transition | envelope still sealed at end, envelope back with Nia, Nia dry, cut healed or moved |

Note the firewall logic: every forbidden list blocks both **future states** (no shot may pre-complete a reserved beat — e.g., no open envelope before shot 5) and **regressions** (no shot may revert an accepted state — e.g., no dry coat after shot 2). If a take accidentally completes a future beat and is *rejected*, it stays diagnostic only; if it's *accepted* as a deviation, remove that beat downstream and recompute the next delta.

**Risk-split coverage (A-tier insurance, not new story beats):**
- `INS-03A` — close insert of the fence snag/cut moment.
- `INS-04A` — close insert of the envelope changing hands (blue envelope + two hands only).
- `INS-05A` — close insert of the flap tearing open.

These cover the three highest-failure elements (contact, hands, tearing physics) so a defect routes to an editorial cut-around instead of endless full-shot retries.

## 5. Shot handoffs — three separate continuity stores

1. **Canonical bank** — human-approved passports above. A generated result can *never* replace these automatically.
2. **Approved memory** — high-information frames promoted from *accepted* shots only, after QC (identity fidelity, no disqualifying artifact, cross-shot compatibility), with source shot/timecode recorded.
3. **Local handoff** — transient neighbor state written on each shot's approval: last approved frame, positions, screen direction, prop owner/hand, light, room tone. Serves the adjacent shot only; never overrides canonical truth.

On each approval, snapshot `SC-010-0N_continuity-state_vNNN.yaml`, e.g. after shot 3:

```yaml
scene_id: SC-010-03
weather: rain-steady
screen_axis: travel-left-to-right, camera on Nia's left side
characters:
  CHAR-NIA:
    wardrobe: WARD-NIA-COAT-WET-v1
    injury: INJ-NIA-CHEEK-FRESH-v1
    held_props: []
props:
  PROP-ENV:
    state: sealed-pocketed
    owner: CHAR-NIA
    location: right inner coat pocket (hidden)
```

## 6. Versioning, naming, retry lineage

- **Stable IDs, never reused:** `SH-010-04-010`, `CHAR-NIA`, `PROP-ENV`, `WARD-NIA-COAT-WET-v1`…
- **Filenames:** `FILM-ENVELOPE_SH-010-04-010_take-002_run-r009_prompt-p003_ref-r004_<model-id>_<res>_v001.mp4`. `_APPROVED` in a filename is a readable aid; registry status metadata is authoritative.
- **Asset registry:** `asset_id, entity_id, state, version, owner, rights_status, source_paths, allowed/excluded attributes, status, approval, sha256`.
- **Run ledger per generation:** `run_id, parent_run, shot_id, prompt text/hash, parameters, reference IDs/hashes/roles, ONE changed variable, output path/hash, hard gates, reviewer, decision, route, actual time/cost`.
- **Retry rules:** every retry branches from the **parent approved run**, never from a rejected child; exactly one variable changes per retry so failures stay attributable. A rejected output is diagnostic evidence only — it can never become canonical, approved memory, or a handoff source. When the (project-set) ceiling is hit or the same hard defect repeats, route instead of rephrasing: cleaner state-specific reference → simpler action / locked camera → split the shot / use the insert → local edit or VFX → redesign the beat.

## 7. Rollback and overwrite protection

- **Immutable checkpoints** after bible lock and after each shot approval (CP-SH01…CP-SH05), plus sequence picture lock. Each stores the state snapshot, approved hashes, open defects, and tool/model versions.
- **Corrupted-state rule:** if a later run contradicts earlier truth (shot 4 renders a dry coat, an already-open envelope, or a right-cheek cut), reject the run, return to the last good scene checkpoint, and **replay only accepted deltas** forward. Never patch canonical state to match a bad render.
- **No overwrites:** new outputs land in an `incoming/` area; promotion to approved is a separate, human-signed step. Approved renders and passports are read-only.
- **Queue discipline:** shots 1→5 are a strictly serialized dependency chain (evolving wardrobe, injury, weather, and prop ownership). Only the three inserts may run in parallel — each only after its parent shot's state is approved.

## 8. Continuity verification pass (before any generation)

- Trace `PROP-ENV` through all five contracts: exactly one seal (shot 1), one transfer (shot 4), one open (shot 5); pocketed and invisible in 2–3.
- Trace monotonicity: dry→wet never reverses; the cut appears once, left cheek only, constant geometry, fresh→dried only.
- Confirm every camera block keeps the left cheek and right hand camera-facing (single-axis rule).
- Confirm every forbidden list covers both pre-completion and regression for its shot.

If you'd like, next step I can materialize this as actual files (`production/00-charter.md`, `bible/`, `state/*.yaml`, five shot contracts + three inserts, ledger CSV templates, and a rollback runbook) once file writing is enabled — say the word and I'll generate them.
