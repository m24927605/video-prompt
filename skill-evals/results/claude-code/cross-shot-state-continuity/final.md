Skill loaded and references read. Two constraints up front: the working directory has no project files (only the three skill folders), and the plan-file/agent/ExitPlanMode tools aren't exposed in this session — so the full plan is delivered inline below. This is planning only: no generation is authorized or run, nothing was modified.

# Five-shot continuity plan — `FILM-ENVELOPE / SQ-010 / SC-010-001`

## 0. Basis, assumptions, unknowns

| Item | Status |
|---|---|
| Platform / model / model ID | **Unknown.** Plan is platform-neutral. Aspect, clip duration, first/last-frame roles, reference limits, audio output are labeled unknown until you name the surface; recheck its official docs (archive date 2026-08-22 = today) before run 1. Don't transfer ModelArk/LAS/Higgsfield/UI-`Seedance 2` facts between surfaces. |
| Evidence class of this design | Hierarchy, passports, three continuity stores, one-delta-per-shot, handoff packets = **practice recommendations** (FP-01/02/04/05/06), not Seedance internals. Retry ceilings below = **project heuristics**, not model statistics. **Nothing here has been run**; it is an untested policy. |
| Rights | Nia and Tomas are original characters → identity sheets must be generated/approved under project rights; no real-person likeness or voice. |
| Generation authorization | None. Passport stills are paid generation too and need separate explicit go-ahead. |

**Decisions I made on your behalf — override any of them:**
1. Overcast daylight (cream coat, wet darkening, blue envelope, and blood all read better than at night).
2. Shots 4–5 take place under an awning/doorway with rain continuing behind; Tomas has been under cover → **Tomas is dry**. This makes "Nia remains wet" a readable story state and gives a clean forbidden state. (Alternative: both in rain → add `WARD-002-v02 wet`.)
3. Nia is right-handed; hair kept off her left cheek so the cut reads.
4. Seal cue = one **blank** white round sticker on the flap, so "still-sealed" is observable in shots 4–5 (plain flap-down is the minimal alternative; never text on it).
5. Tomas receives with his **left** hand (near-camera on his side of the axis); in shot 5 left hand holds, right hand opens.
6. Pocketing the envelope = trimmable tail of shot 1 + protection insert; an ellipsis cut into shot 2 with the envelope already hidden is an allowed fallback. The draw from the pocket before shot 4 is elided (shot 4 starts with the envelope already in her right hand) — avoids a cross-body left-hand reach that could read as a hand swap.
7. No dialogue, no subtitles. Envelope contents are never shown (text-fidelity risk) — out of scope.

## 1. Operating mode — recommended hybrid

Every shot in this scene is a state transition, so the continuity floors (identity, state, ownership, direction) are common to all tiers. Effort differs:

| Tier | Shots | Why |
|---|---|---|
| **A** (previz + keyframe + more candidates + blind compare) | 030 cluster, 040 cluster, 050 cluster | Injury creation during full-body physics; hand-to-hand ownership transfer; seal-break while a *secondary* character must hold two states |
| **B** (standard refs + QC, upgrade when blocked) | 010, 020 and their inserts | Single character, one prop/weather delta |
| **C** (fast, parallel) | rain plates, location establishing/plate | No state truth; used for edit/VFX only |

## 2. Hierarchy and coverage

`FILM-ENVELOPE → SQ-010 → SC-010-001 → BT-010-001-01…05 → SH-010-001-0xx` (short alias `SH-0xx` below). Your five shots are the five **beats**; each beat has one **primary** shot (your shot) plus **protection** coverage that is generated only if needed or cheap, and cut in only if the primary fails a gate.

Design principle that makes "no overwrite" work: **a shot may *cause* a new state, but the state is *canonized* by a state-specific asset, never by a generated frame.** Shot N shows the cause; shot N+1 (or its insert) starts from the canonical state sheet.

| Beat | Primary | Protection | Why the protection exists |
|---|---|---|---|
| 1 Seal | `SH-010` medium, seals envelope | `SH-011` hands insert: press flap, slide into right inner pocket | hands + small-prop transform; also answers "where did the envelope go" |
| 2 Rain | `SH-020` med-wide, rain starts, shoulders darken | `SH-021` shoulder-fabric insert, already darkening | in-shot wardrobe transform is a known weak area; insert + ellipsis establishes `v02` |
| 3 Fence | `SH-030` wide, climb + wire contact + flinch | `SH-031` contact insert (landing side); `SH-032` landing MCU: cut visible, right palm to right chest | splits cause (030/031) from canonized result (032); 032 is the only place the cut is *introduced as truth* |
| 4 Handoff | `SH-040` OTS over Tomas favoring Nia | `SH-041` hands insert (cream sleeve = Nia, dark sleeve = Tomas); `SH-042` Tomas reaction | contact/ownership is the scene's turn; sleeve color makes hand identity unambiguous |
| 5 Open | `SH-050` two-shot, seal broken | `SH-051` Tomas hands insert; `SH-052` Nia reaction (frontal: cut + wet shoulders) | if Nia's states drift in the two-shot, `051+052` intercut still satisfies the beat |

**Control assets (only what solves a problem):** one floor plan (below); storyboard of the 12 shots for order/sizes; keyframes `K-030` (top-of-fence contact pose), `K-040` (exchange framing), `K-050` (opening framing). No clay/blockout unless 030 physics fails twice.

```
camera side (all shots; SH-031 is neutral, action toward camera)
  Z1 shelter ──► Z2 open ground ──► Z3 chain-link fence (vertical, frame center) ──► Z4 awning: Tomas
frame-left ──────────────────── Nia travels → ──────────────────────────────────────── frame-right
axis for 040/050: Nia(L) ↔ Tomas(R); camera never crosses
```

## 3. Bible: state-specific assets and registry

Every version is write-once. A new wardrobe/injury/weather/prop state is a **new version**, the base is never edited, conflicting states are never on one sheet.

| Asset ID | Versions | Sheet shows | Must exclude |
|---|---|---|---|
| `CHAR-001 NIA` | v01 | face/hair/build; right-handed; hair off left cheek; front, both profiles, 3/4, MCU, expressions | any wardrobe state, injury, wetness |
| `CHAR-002 TOMAS` | v01 | distinct face/hair; `WARD-002-v01` dark (charcoal/navy) jacket, no hood up; dry | cream coat, envelope, wetness |
| `WARD-001 cream coat` | **v01 dry**; **v02 wet-shoulders** (shoulders/upper back/collar darkened with specular; sleeves and front panels still cream) — front, back, 3/4 views each | v02 must not show soaking, tears, mud |
| `INJ-001 left-cheek cut` | **v01**: 2–3 cm diagonal on the left cheekbone below the outer eye corner, fresh red line, thin trace downward, no bruise; frontal + left 3/4 + left profile; sheet note: *"in frontal views the cut is on the viewer's RIGHT"* | right cheek anything; scarring/swelling |
| `PROP-001 blue envelope` | **v01 unsealed** (flap open); **v02 sealed** (flap down, blank white seal); **v03 opened** (seal split, flap torn up, no contents) — cobalt, matte, C6, no writing | text, logos, second envelope, color variants |
| `PROP-002 fence` | v01 | chain-link, twisted wire ends at top rail | barbed wire (changes injury story) |
| `LOC-001` | v01 dry-overcast Z1 · v02 rain-onset Z2 · v03 steady-rain Z3 · v04 steady-rain-under-awning Z4 | — |
| `LIGHT-001` | v01 overcast dry · v02 overcast rain (darker, wet speculars) | direct sun |
| `SOUND-001` | v01 sheltered quiet · v02 rain onset · v03 steady rain open · v04 rain under awning (muffled, drips) | music decisions (placeholder) |
| `CAM-001 / STYLE-001` | v01 | static or slow push, eye level, 35–50 mm feel, no whip pans; naturalistic, desaturated except blue envelope, cream coat, blood red | — |

**Derived character state sheets** (each its own immutable asset; each shot references exactly one per character):

- `NIA-STATE-A` = CHAR-001 + WARD-001-v01 (dry, clean) → SH-010, SH-011, SH-020 start
- `NIA-STATE-B` = CHAR-001 + WARD-001-v02 (wet shoulders, clean) → SH-020 end, SH-021, SH-030, SH-031
- `NIA-STATE-C` = CHAR-001 + WARD-001-v02 + INJ-001-v01 → SH-032, SH-040–052
- `TOMAS-STATE-A` = CHAR-002 + WARD-002-v01 dry → SH-040–051

Registry row (skill schema): `asset_id, entity_id, state, version, owner, rights_status, source_paths, allowed_attributes, excluded_attributes, status(draft/approved/retired), approval, sha256`. Example: `NIA-STATE-C | CHAR-001 | wet-shoulders+left-cheek-cut | v01 | <you> | original-character | … | face,hair,coat state,cut position | pose,background,light | approved | 2026-08-xx | <hash>`.

**Reference policy**
- Smallest packet per shot, every reference has one job and an exclusion list (identity ≠ pose; state ≠ framing). Keep packets ≤ 5–6 references; actual limits are per-surface and unknown.
- **Forward-only, canonical-first:** the reference for any *state attribute* is always the canonical state sheet. A frame promoted from an approved shot to approved memory carries its state-version tags and a use boundary; it may be used only in shots whose required versions match those tags, and only for neighbor continuity (light, color, position, camera) — never as the state reference, never for an earlier shot.
- `return_last_frame`-type outputs (where documented) are transport only; a last frame must pass QC before promotion.

## 4. Continuity state model

### State ownership matrix (the write-guard)

Only the listed writer may change the attribute; every other shot reads it and must match. **QC compares each take's observed end state to the prior approved snapshot; any difference in a non-delta attribute is a hard fail, whatever else the take got right.** That is the mechanism that stops later shots from overwriting earlier states.

| Attribute | Only writer | Readers (must match) |
|---|---|---|
| `PROP-001.state` unsealed → sealed | SH-010 (011) | 020, 030, 032, 040 |
| `PROP-001.location` hand → right inner pocket (hidden) | SH-010 tail / 011 | 020, 030 (never visible) |
| `WARD-001` v01 → v02 | SH-020 (021) | 030, 031, 032, 040, 041, 050, 052 |
| `INJ-001` none → v01 | cause SH-030/031; canonized SH-032 | 040, 050, 052 |
| `PROP-001.owner/hand` Nia-right → Tomas-left | SH-040 (041) | 042, 050, 051 |
| `PROP-001.state` sealed → opened | SH-050 (051) | — |
| Everything else (identity, Tomas dry, envelope color/count, fence, axis) | nobody | all |

### Scene-state snapshots `FILM-ENVELOPE_SC-010-001_continuity-state_v0N.yaml` (immutable, one per boundary)

| CS | After | WARD-001 | INJ-001 | PROP-001 state / owner / where / hand | LOC | Nia | Tomas |
|---|---|---|---|---|---|---|---|
| v01 | scene start | v01 dry | none | v01 unsealed / Nia / both hands | v01 Z1 | Z1 center, 3/4 to camera | absent |
| v02 | SH-010 ✓ | v01 dry | none | v02 sealed / Nia / right inner pocket, hidden | v01 | Z1 edge, facing → | absent |
| v03 | SH-020 ✓ | **v02 wet-shoulders** | none | v02 / Nia / pocket, hidden | v03 rain | exited frame-right | absent |
| v04 | SH-030 ✓ | v02 | **v01 left cheek** | v02 / Nia / pocket, hidden | v03 | landing side, facing →, exits right | absent |
| v05 | SH-040 ✓ | v02 | v01 | v02 sealed / **Tomas** / left hand | v04 awning | frame-left, facing Tomas | frame-right, dry, facing ← |
| v06 | SH-050 ✓ | v02 | v01 | **v03 opened** / Tomas / both hands (L holds, R opened) | v04 | unchanged | unchanged |

```yaml
# v04 example — the file format every snapshot uses
scene_id: SC-010-001
state_version: v04
derived_from: v03
delta_by: SH-010-001-032      # the shot whose approved take wrote this delta
approved_run: r0xx
story_time: "same afternoon, ~2 min after v03"
location_state: LOC-001-v03-steady-rain
screen_axis: Z1→Z4 left-to-right; Nia travel →
characters:
  CHAR-001:
    state_sheet: NIA-STATE-C
    wardrobe: WARD-001-v02
    injury: INJ-001-v01
    position: Z3 landing side, frame-right, 3/4 to camera-right
    exit_vector: frame-right
    held_props: []
  CHAR-002: absent
props:
  PROP-001: {state: v02-sealed, owner: CHAR-001, location: right-inner-pocket, visible: false}
lighting: LIGHT-001-v02
audio: SOUND-001-v03
sha256: <hash of this file>
```

### Required / forbidden per primary shot

| Shot | Required | Forbidden (past *and* future states, plus intruders) |
|---|---|---|
| 010 | NIA-STATE-A; PROP-001 v01→v02 in-shot; LOC v01 dry ground; envelope ends in **right** hand | rain, wet fabric, facial marks, Tomas, second envelope, color shift, text, envelope in left hand at end |
| 020 | NIA-STATE-A → NIA-STATE-B; LOC v02→v03; exit frame-right; envelope hidden | envelope visible, Tomas, fence, injury, fully soaked coat, dry coat at end, hood/umbrella, travel ←  |
| 030 | NIA-STATE-B; PROP-002; LOC v03; one continuous climb L→R; contact + flinch | envelope visible/falling, Tomas, coat tear/mud, cut visible before contact, **right**-cheek cut, second Nia, climbing R→L |
| 032 | NIA-STATE-C (cut on viewer's right of her face); right palm to own right chest; exit right | clean cheek, cut on wrong side, envelope visible, added coat damage |
| 040 | NIA-STATE-C; TOMAS-STATE-A; PROP-001 v02 with seal visible at transfer; transfer Nia-right → Tomas-left | envelope from Nia's left hand, opened envelope, two envelopes, Tomas wet, Nia dry, clean cheek, hood/umbrella, Tomas in cream, axis cross |
| 050 | NIA-STATE-C; TOMAS-STATE-A; PROP-001 v02→v03 in-shot; Tomas keeps ownership | Nia dry, clean cheek, right-cheek cut, Nia holding the envelope, any letter/text, Tomas wet, envelope color/size change, resealing |

### Screen direction rules

| Rule | Detail |
|---|---|
| Travel | Nia moves **left → right** in 020, 030, 032 and enters 040 from frame-left. |
| Axis | 040/050: Nia frame-left facing →, Tomas frame-right facing ←; camera on the near side only. 031 is the only landing-side shot and is neutral (action toward camera) — it may not show her moving R→L. |
| Nia's right hand | = **screen-left of her body** when she faces camera; = near-camera when she faces screen-right in profile. Prompts say "her own right hand". |
| Right inner pocket | = **screen-left lapel** when she faces camera. Prompts say "wearer's right". |
| Left cheek | = **screen-right of her face** when she faces camera; **hidden** in right-profile (i.e., whenever she faces screen-right). Hence every injury-readable shot is frontal/3/4 from the camera side: 031, 032, 040 (OTS favoring Nia), 052. |
| Tomas's left hand | = near-camera when he faces screen-left; = screen-right of his body when frontal. |
| Eyelines | Nia → Tomas (screen-right). Tomas → Nia (screen-left), then down to the envelope in 042/050. |

### Prop ownership timeline — `PROP-001`

| Point | State | Owner | Location | Hand |
|---|---|---|---|---|
| 010 start | unsealed | Nia | both hands | — |
| 010 end | sealed | Nia | right hand → (tail/011) right inner pocket | right; left hand only opens the lapel |
| 020 · 030 | sealed | Nia | right inner pocket, **never visible** | — |
| 032 | sealed | Nia | pocket; presence confirmed by right palm on right chest | — |
| 040 start | sealed | Nia | right hand, chest height (draw elided) | right |
| 040 end · 042 · 050 start | sealed | **Tomas** | left hand | left |
| 050 end | **opened** | Tomas | both hands | left holds, right opened |

## 5. Shot manifest and handoffs

Each contract (full schema per skill: identity / narrative / entities / space / camera / look / sound / inputs / prompt+params / acceptance / provenance). Duration intents are story intents, not platform claims.

**SH-010 · Seal (B)** — Z1, static medium, Nia 3/4 frontal, coat open. Start: blue envelope in both hands, flap open. Delta: folds flap, presses blank seal. End: sealed envelope in right hand at chest height, facing →; trimmable tail: left hand opens right lapel, right hand slides it into the right inner pocket, coat closes. Refs: NIA-STATE-A, PROP-001 v01 and v02, LOC v01. Accept: one envelope, blue throughout; open→closed visible; sealed state holds ≥ several clean frames before the tail; coat dry everywhere; face clean. Route: hands fail → tighter MCU → `011` carries the seal → sticker composite.

**SH-020 · Rain (B)** — Z2, static or slow pan →, med-wide; Nia steps out from frame-left, walks →. Start: NIA-STATE-A, coat closed, dry ground. Delta: first drops → steady rain; shoulders/upper back darken. End: exits frame-right in rain; NIA-STATE-B. Refs: STATE-A (start), STATE-B (end), LOC v02/v03. If the chosen surface documents strict first/last-frame roles, use STATE-A/B as endpoints; otherwise they are semantic state references + timecoded beats. Accept: rain starts inside the clip; darkening localized to shoulders; exit right; no new props. Route: transform fails → `021` + ellipsis → post: roto/grade wet-darkening on a dry take + rain plate.

**SH-030 · Fence and cut (A)** — Z3, approach side, static wide/med-wide, fence vertical at center; Nia enters frame-left in rain. Start: NIA-STATE-B, coat closed. Delta: climbs; at the top the left side of her face brushes a wire end → flinch; drops to landing side. End: frame-right, facing →, no coat damage, envelope hidden. Keyframe `K-030`. Accept: one continuous climb; contact + flinch readable; lands right; nothing drops from the coat. Route: lock camera + shorten to top-of-fence→landing → split `031` + `032` → blockout → redesign (gap in fence, wire catches cheek) → composite the cut on `032` (small, local, tracked — a good VFX candidate).
**SH-031** landing side, low angle at fence top, face comes over, wire catches left cheek (viewer's right), sharp inhale, blood bead. **SH-032** landing side MCU, NIA-STATE-C canonical, right palm to right chest, turns and exits right.

**SH-040 · Handoff (A)** — Z4, OTS over Tomas's left shoulder favoring Nia (3/4 frontal), static medium, rain behind. Start: NIA-STATE-C holding sealed envelope in right hand at chest height (pocket draw = optional trimmable head); TOMAS-STATE-A hands empty. Delta: she extends right hand; Tomas takes it with his left; release. End: envelope sealed in Tomas's left hand; Nia's right hand empty, lowering; positions held. Keyframe `K-040`. Accept: one envelope leaves Nia's right hand and ends in Tomas's left; seal intact; Nia's wet shoulders **and** cut visible in ≥ 1 clean frame; Tomas dry. Route: lock tighter, one exchange → `041` hands (sleeve identity) → `042` reaction → edit-around: cut on the reach, `050` starts with Tomas holding.

**SH-050 · Open (A)** — same axis, static medium two-shot, both 3/4 so Nia's left cheek stays visible. Start: Tomas holds sealed envelope in left hand; Nia watches, hands empty. Delta: Tomas's right hand splits the seal and lifts the flap (v02→v03). End: open envelope in Tomas's hands; Nia unchanged; no contents. Keyframe `K-050`. Accept: seal visibly breaks in-shot; Nia's two states visible in ≥ 1 clean frame; ownership stays with Tomas; no text. Route: tear fails → `051`; Nia drifts → `052` and intercut; persistent → editorial reconstruction `051 + 052` (still satisfies the beat).

### Handoff packets (local handoff store — transient, never overrides canonical)

| Boundary | Carries forward | Must **not** carry |
|---|---|---|
| H1 010→020 | STATE-A; envelope sealed, hidden in right inner pocket; Nia at Z1 edge facing →; LIGHT v01; SOUND v01 | envelope in hand, open flap, rain |
| H2 020→030 | STATE-B; steady rain; exit vector →; envelope hidden; LIGHT/SOUND rain | dry coat, visible envelope |
| H3 030/032→040 | STATE-C (cut = canonical INJ sheet, not the 030 frame); coat unchanged except wetness; envelope sealed; arrives from frame-left | right-cheek cut, coat tear, envelope visible/lost |
| H4 040→050 | envelope sealed, Tomas left hand; Nia right hand empty, frame-left; Tomas dry frame-right; awning light; SOUND v04 | Nia holding envelope, opened envelope, Tomas wet |
| H5 050→scene exit | envelope opened, Tomas; Nia unchanged | — |

### Dependency queue

- **Wave 0 (serial):** charter → passports → `CP-01` bible lock.
- **Wave 1 (parallel):** all state sheets, derived STATE-A/B/C, floor plan, storyboard, keyframes, rain/location plates (C), animatic with temp rain bed.
- **Wave 2 (parallel, low-cost blocking):** one blocking candidate for each of the five primaries **at once** — legal because every start state comes from canonical sheets, not from a prior output → blocking rough cut → pickups list → `CP-02`.
- **Wave 3 (serial finals, story order):** 010 → approve → CS v02 → 020 → CS v03 → 030/031/032 → CS v04 → 040/041/042 → CS v05 → 050/051/052 → CS v06. Inserts whose start state is fully canonical (011, 021, 051) may run alongside the chain; those needing a neighbor's handoff (032, 041, 042, 052) run after their cluster primary.
- Batch only identical platform/model/aspect/resolution/ref-packet version; otherwise failures can't be attributed.

## 6. Naming, versioning, retry lineage

**IDs (never reused, never renumbered for edit order):** `FILM-ENVELOPE`, `SQ-010`, `SC-010-001`, `BT-010-001-01…05`, `SH-010-001-010/011/020/021/030/031/032/040/041/042/050/051/052`, `CHAR-001/002`, `WARD-001/002`, `INJ-001`, `PROP-001/002`, `LOC-001`, `LIGHT-001`, `SOUND-001`, `CAM-001`, `STYLE-001`, continuity state `CS v01–v06`, checkpoints `CP-00…10`, prompts `p###`, reference packets `ref-r###`, runs `r###`, takes `t###`.

**Filenames** (status metadata is authoritative; `APPROVED` in a name is only a reading aid):
```
FILM-ENVELOPE_SH-010-001-040_take-002_run-r011_prompt-p003_ref-r004_<model-id>_<res>_v001.mov
FILM-ENVELOPE_WARD-001_wet-shoulders_v002_APPROVED.png
FILM-ENVELOPE_SC-010-001_continuity-state_v004.yaml
```

**Immutability rules**
1. Asset versions, CS snapshots, prompts, ref packets, and runs are write-once. Status moves `draft → approved → retired`; retired is not deleted.
2. A generated output never replaces a canonical asset or CS snapshot. Corrections create the next version with a change record.
3. Outputs land in `incoming/`; `rejected/`, `selects/`, `approved-memory/` stay separate. Only approved takes enter the cut.

**Run ledger** (per skill): `run_id, parent_run, shot_id, timestamp, platform/model/doc version, prompt text+hash, parameters, reference IDs/hashes/roles, one changed variable, output path/hash/duration/spec, queue/gen/review/human time, billed cost, hard gates, scores, timecoded defects, reviewer, decision, route`. No credentials, signed URLs, or private URLs retained — ingest and hash promptly.

**Retry lineage rules**
1. Every run names its `parent_run` and exactly **one** changed variable (prompt, one reference, one parameter, or shot design — never several).
2. A retry's parent is the last *valid* run of the same shot contract. Rejected outputs are never references or frames for anything; they stay in the ledger for diagnosis only.
3. Once a shot is approved, any new run branches from the approved run's inputs as a new take. The approved take is superseded only by a human change record — never silently.
4. No in-place edits of approved media: fixes are new takes or post versions with their own IDs and parents.
5. Approved-memory promotion records source run, timecode, crop, state-version tags, and use boundary.

Example chain for `SH-040`: `r021 (p001, ref-r003)` hands merge → `r022` parent r021, change: lock camera → `r023` parent r022, change: swap STATE-C sheet for cleaner v01b → **approved** → pickup later: `r031` parent **r023** (not r022), change: +0.5 s tail.

**Proposed retry ceilings (project heuristics, not model averages — set your own):** A primaries 6 valid runs; B primaries 4; inserts/reactions 3; passport stills 5 per sheet. Stop earlier and route when the same hard defect survives two isolated changes, fixing one gate breaks another twice, the ceiling is hit, or a rejected/drifted frame would have to become truth.

## 7. Gates, checkpoints, rollback

**Hard gates before any scoring:** required story beat; correct identity and state sheet; ownership and direction unambiguous; **write-guard pass** (no non-delta attribute differs from the prior CS snapshot); no structural artifact; complete usable interval with handles; neighbor compatible; sound either passes or has an approved post route. Dailies review the full clip — opening, middle, end, and every contact timecode (seal press, first drops, wire contact, hand exchange, seal break).

**Checkpoints (immutable):** `CP-00` charter · `CP-01` bible/state sheets · `CP-02` previz/animatic · `CP-03…07` after each beat approval (= CS v02…v06) · `CP-08` structure lock · `CP-09` sound/color lock · `CP-10` master. Each stores script/bible versions, CS snapshot, approved hashes, timeline/EDL, open defects/routes, budget, tool/model/platform/doc versions, approvals.

**Rollback rules**
- Retry from the parent approved run, never a rejected child.
- A later take that contradicts an earlier state is **rejected at the write-guard**; the earlier state is never re-approved to match it. Example: a beautiful `SH-050` take with a dry coat fails; `WARD-001-v02` and CS v03–v05 stay canonical.
- Director-driven change to an earlier state (e.g., cut moved to the right cheek) = change record → `INJ-001-v02` (v01 retired), new `NIA-STATE-C-v02`, new CS snapshots v04b…, and re-opening of 030-cluster/040/050 with listed VFX/sound/color impacts.
- Corrupted axis/state found at rough cut (e.g., 030 accepted with R→L climb): return to `CP-04`, regenerate 030 cluster, replay approved deltas. Because downstream shots took their **state** truth from canonical sheets, 040/050 are re-validated for *handoff* compatibility (position, vector, light) rather than automatically regenerated.
- Model/platform update mid-project = new branch + regression on approved shots; approved renders are never overwritten.

## 8. Rough cut → finishing

- **Animatic (Wave 1):** storyboard + keyframes + temp rain bed; checks whether the pocketing ellipsis (010→020) and the elided pocket draw (032→040) read.
- **Blocking cut (Wave 2):** exposes missing coverage; pickups prioritized by beat risk (expect 031/032 and 041 to be the first pickups requested).
- **Structure lock (`CP-08`):** after this, new shots or reordered state need a change request listing VFX/sound/subtitle/color impacts.
- **Cleanup/VFX routes:** seal-sticker composite; tracked cut composite on 032/040/050 if under-rendered; paint-out of accidental second envelope; localized wet-darkening roto/grade on 020 fallback; rain-plate enhancement; no undocumented time-stretch.
- **Color:** cream coat is the match anchor (dry vs wet-shoulder darkening must be a localized, consistent shift); cobalt envelope identical across 010/040/050/041/051; blood is the only saturated red; check wet speculars and banding in overcast gradients.
- **Sound:** no dialogue (change record if added). Rain bed starts inside 020 and runs continuously through 030, shifts to under-awning perspective for 040/050; foley: flap press, coat fabric, chain-link rattle, landing, sharp inhale at contact, paper tear; music placeholder. Generated audio is a timing scaffold, replaced in the mix.
- **Subtitles:** none; if dialogue is ever added, time from final audio, not prompt timestamps.
- **Master/QC/archive:** one uninterrupted playback + targeted checks of every cut, VFX, and audio transition; technical + content QC per skill; archive master, stems, EDL/project, all ledgers, CS snapshots, approved/rejected decisions, hashes, checkpoints, waivers — never credentials or signed URLs.

## 9. KPI dashboard (ledger-fed; empty until runs exist — no invented numbers)

| KPI | Formula | Value |
|---|---|---|
| first_pass_approval | approved on first valid run / valid first runs | — |
| additional_retries | extra valid runs before approval / approved shots (median, P90) | — |
| time_per_approved_shot | shot-ready → approved wall clock | — |
| usable_seconds_per_hour | approved seconds in cut / production+review hours | — |
| cost_per_approved_second | all billed runs + post tools / in-cut seconds | — |
| waste_rate | generated seconds or cost not in cut / total | — |
| write-guard fail rate (project-specific) | takes rejected for non-delta state change / reviewed takes | — |
| continuity KPIs | wardrobe/injury/prop-state/direction/ownership pass per take | — |

---

**Recap.** Nothing was generated or modified; this is a platform-neutral plan. The scene is structured as five beats with one primary shot each plus protection inserts/reactions; every character/wardrobe/injury/prop/weather state is an immutable versioned asset (`NIA-STATE-A/B/C`, `WARD-001 v01/v02`, `INJ-001 v01`, `PROP-001 v01/v02/v03`), each shot reads the prior scene-state snapshot and may write exactly one delta, and a write-guard gate rejects any take that alters a non-delta attribute — so a later shot can never overwrite an earlier state. Screen direction (left→right travel, fixed Nia-left/Tomas-right axis, injury visible only in frontal coverage), prop ownership (Nia-right → Tomas-left), forward-only reference policy, run lineage with one variable per retry, proposed ceilings, checkpoints, and rollback scenarios are all specified above. Next steps that need your input: name the generation surface/model and aspect/duration, confirm or override the eight decisions in section 0, set your own retry/budget ceilings, and separately authorize passport-still generation when ready.
