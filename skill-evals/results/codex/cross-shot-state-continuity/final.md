The controlling rule is: each shot reads one approved parent checkpoint and may append only its permitted state delta. It cannot edit its parent, reuse a rejected result, or promote future-shot imagery as earlier truth.

## Production assumptions

Plan date: 2026-08-22. The generation platform/model, reference limits, aspect ratio, frame rate, audio mode, budget, and rights status are unspecified; lock and record them before generation. This is a provider-neutral workflow and does not assume cross-shot model memory.

Selected story locks:

- One continuous exterior route: covered area → exposed path → fence → Tomas.
- Nia travels screen-left to screen-right.
- Shot 1 ends with Nia placing the newly sealed envelope in her anatomical-right inner pocket.
- Light rain continues through Shots 2–5; the shoulder wetness does not materially spread during the short scene.
- A fence wire causes a small fresh cut on Nia’s anatomical-left cheek.
- Tomas receives with his left hand, leaving his right hand free to open the envelope.
- The contents remain inside when Tomas opens it.
- No dialogue is specified.

Use a hybrid production mode: blocking-quality passes for all five shots, standard quality for Shots 1–2, and quality-max treatment for the fence injury, handoff, and opening in Shots 3–5. This is an initial production policy, not a tested claim about an unspecified model.

## Hierarchy and coverage

```text
FILM-LETTER
└─ SQ-010 Delivery
   └─ SC-010-010 Fence passage
      ├─ BT-01 / SH-010-010-010 — seal and secure
      ├─ BT-02 / SH-010-010-020 — rain onset
      ├─ BT-03 / SH-010-010-030 — fence injury
      ├─ BT-04 / SH-010-010-040 — sealed transfer
      └─ BT-05 / SH-010-010-050 — envelope opened
```

Shot 2 doubles as the geography master. Shots 1 and 5 provide prop detail; Shot 4 is the unambiguous ownership shot. Give every shot approximately 0.5 seconds of clean head and tail handles.

## Immutable asset bank

| Asset ID | Locked truth |
|---|---|
| `CHAR-NIA_v001` | Nia’s identity and anatomy; no coat, rain, or injury baked into the identity reference |
| `CHAR-TOMAS_v001` | Tomas’s identity |
| `WARD-NIA-COAT_DRY_v001` | Intact cream coat, completely dry |
| `WARD-NIA-COAT_WET-SHOULDERS_v001` | Same intact coat with an approved, repeatable wet pattern on both shoulder caps |
| `WARD-TOMAS-BASE_v001` | Tomas’s unchanged wardrobe for Shots 4–5 |
| `INJ-NIA_CLEAR_v001` | No facial injury |
| `INJ-NIA_LEFT-CHEEK-FRESH_v001` | Small shallow cut on anatomical-left cheek; exact shape and blood level locked before Shot 3 |
| `PROP-BLUE-ENV_UNSEALED_v001` | Blue envelope, flap raised, contents inside |
| `PROP-BLUE-ENV_SEALED_v001` | Same envelope, flap bonded shut, dry and undamaged |
| `PROP-BLUE-ENV_OPENED_v001` | Bond broken and flap raised; contents remain inside |
| `LOC-SC010_v001` | Covered start, path, north–south fence, Tomas’s mark beyond it |
| `WX-DRY_v001`, `WX-RAIN-ONSET_v001`, `WX-LIGHT-RAIN_v001` | Separate weather states |
| `CAM-BLOCK-SC010_v001` | Floor plan, axis, marks, eyelines, framing families |
| `LOOK-SC010_v001`, `SND-SC010_v001` | Locked light/rain direction, palette, dry ambience, rain bed, coat/fence/envelope foley |

Every asset records status, rights, source, approval, and SHA-256. Never place dry/wet, clear/cut, or sealed/open states on one undifferentiated reference sheet.

## Immutable scene states

| State | Nia | Envelope | Weather and position |
|---|---|---|---|
| `ST000_v001` | Dry coat, uninjured | Unsealed; owned by Nia at covered work surface | Dry; west of fence |
| `ST010_v001` | Dry coat, uninjured | Sealed; Nia’s right inner pocket | Dry; moving toward exposure |
| `ST020_v001` | Wet shoulders, uninjured | Sealed; same pocket and owner | Light rain; one step before fence |
| `ST030_v001` | Wet shoulders, fresh left-cheek cut | Sealed; same pocket and owner | Landed east of fence |
| `ST040_v001` | Wet and injured; empty hands | Sealed; Tomas’s left hand | Nia left of Tomas |
| `ST050_v001` | Wet and injured; unchanged | Opened; Tomas supports with left, opens/holds with right | Same positions |

Ownership and prop state are explicit metadata; they are never inferred solely from an image.

## Screen direction and blocking

The fence runs north–south. Nia travels west→east, appearing screen-left→screen-right. All cameras remain south of the travel/Nia–Tomas axis.

- Nia’s anatomical-right pocket and right hand are camera-near.
- During Shot 3 her injured left cheek is initially camera-far. After the fence contact, she turns her head 20–30 degrees toward camera so the correct cheek becomes readable.
- In near-frontal framing, Nia’s anatomical-left cheek appears on the viewer’s right.
- Shot 4 keeps Nia screen-left looking right and Tomas screen-right looking left.
- Tomas’s receiving left hand is camera-near.
- Shot 5 preserves those positions and keeps Nia visibly in frame.
- Never horizontally flip a render; that would exchange the required cheek, hand, and pocket.

## Shot contracts

| Shot | Start → allowed delta → end | Required states | Forbidden states | Approved handoff |
|---|---|---|---|---|
| `SH010` medium-close | `ST000 → ST010`. Nia seals the envelope, then immediately places it into her right inner pocket with her right hand. | Dry cream coat; clear face; blue envelope visibly becomes sealed; accessible right lapel/pocket; no rain. | Wet coat, injury, Tomas, duplicate envelope, wrong pocket, envelope unsealed at cut. | `LH010→020`: dry coat, empty hands, sealed envelope fully concealed in right pocket, Nia oriented screen-right. |
| `SH020` medium-wide geography master | `ST010 → ST020`. Nia leaves cover; rain begins and produces the approved shoulder wetness. | First frame dry; visible rain onset; wet shoulders by end; envelope remains sealed, dry, hidden, and owned by Nia. | Injury, prop exposure, full-body soaking, rain already established at opening, Tomas. | `LH020→030`: exact wet map, rain/light vectors, no injury, sealed envelope in right pocket, Nia one step before fence. |
| `SH030` medium-wide, modest camera movement | `ST020 → ST030`. Nia climbs west→east; fence contact causes the left-cheek cut; she lands and turns enough to reveal it. | Wet shoulders; clear face until contact; fresh anatomical-left-cheek cut afterward; envelope unchanged in pocket. | Right/bilateral/pre-existing cut, dry coat, coat tear, envelope visible/dropped/opened/duplicated, Tomas, axis reversal. | `LH030→040`: both feet east of fence, approved cut geometry, wet map unchanged, envelope sealed in right pocket, Nia looking toward Tomas. |
| `SH040` locked medium two-shot | `ST030 → ST040`. Nia withdraws with her right hand; Tomas accepts with his left; show Nia-only control → brief shared grip → Tomas-only control. | Nia wet/injured; envelope sealed throughout; hands and release unobscured. | Nia’s left hand giving, Tomas owning before contact, teleportation, duplication, opening, wrong cheek, drying or healing. | `LH040→050`: clean beat after release, Nia’s right hand visibly empty, Tomas alone holds sealed envelope in left hand, positions and eyelines locked. |
| `SH050` same-axis medium/tight two-shot | `ST040 → ST050`. Tomas stabilizes with left hand and opens the flap with his right. | Sealed at first frame; visibly opened by end; Nia remains visible, wet, and left-cheek injured. | Already open at start, still sealed at end, Nia touching/owning it, duplicate envelope, contents removed, injury/wetness reset, Nia cropped out. | Final `ST050` checkpoint. |

Only the listed fields may change. For example, Shot 5 may change the envelope’s seal state but must reproduce Nia’s wardrobe and injury fields byte-for-byte from `ST040`.

## Reference and handoff policy

Use three separate stores:

1. Canonical bank: human-approved identities and state assets.
2. Approved memory: scoped crops or frames promoted only from accepted shots.
3. Local handoff: target-specific neighbor information used once.

Precedence is:

```text
canonical state manifest > approved memory > local handoff
```

Any conflict blocks the run.

Promote only:

- Shot 2’s wet-shoulder crop for Shots 3–5.
- Shot 3’s left-cheek injury crop for Shots 4–5.
- Shot 4’s final ownership frame for Shot 5.

Do not pass Shot 1’s full dry-coat frame into later wet shots. Rejected output never becomes a reference. Hidden facts—such as the envelope remaining inside a pocket—come from the state manifest, not visual guesswork.

## Versioning and dependency queue

Use separate counters:

- `vNNN`: immutable asset/state version
- `cNNN`: shot contract
- `pNNN`: prompt
- `rbNNN`: reference bundle
- `gNNNN`: generation run
- `aNNN`: approval record

Example names:

```text
FILM-LETTER_WARD-NIA-COAT_state-wet-shoulders_v001_<hash>.png
FILM-LETTER_SC-010-010_state-ST030_v001_<hash>.yaml
FILM-LETTER_SH-010-010-040_run-g0014_parent-CP030.mov
```

The serialized queue is:

```text
CP000 Bible lock
→ CP005 floor-plan/anchor lock
→ SH010 → QC → ST010/CP010
→ SH020 → QC → ST020/CP020
→ SH030 → QC → ST030/CP030
→ SH040 → QC → ST040/CP040
→ SH050 → QC → ST050/CP050
→ CP060 scene/picture-structure lock
```

A run writes only to its own incoming directory. Approval appends a new approval record, state object, and checkpoint; it never edits an existing one. Every run declares an expected parent checkpoint hash. A late result from an obsolete branch cannot be promoted when that hash no longer matches.

Retired contracts and reference bundles are excluded. There are no compatibility aliases, missing-version fallbacks, or reuse of obsolete paths.

## Retry lineage

Initial ceiling:

- Shots 1–2: three valid candidates each.
- Shots 3–5: four valid candidates each.
- Stop earlier if the same hard defect repeats twice.
- Change exactly one prompt, reference, parameter, or blocking variable per retry.

Example:

```text
CP020 / ST020
├─ g0011 SH030 → REJECT: cut appears on right cheek
└─ g0012 SH030 parent=CP020
   one_change=head turns 25° toward camera
   → APPROVE → ST030 / CP030
      ├─ g0013 SH040 → REJECT: Nia gives with left hand
      └─ g0014 SH040 parent=CP030
         one_change=right-hand crossing-body block
         → APPROVE → ST040 / CP040
```

`g0012` is a sibling of rejected `g0011`, not its child. No rejected image, frame, or motion tail enters a later reference bundle.

At the ceiling, keep the same five-shot editorial structure and route locally:

- Shot 2: add rain/wetness in tracked VFX.
- Shot 3: generate a clean climb and track the approved cheek cut in post.
- Shot 4: lock the camera and composite a clean envelope/hand pass if necessary.
- Shot 5: replace only the bounded envelope-opening region.

Adding another editorial shot requires an explicit structure change.

## Rollback

- Current-shot rejection: the scene remains at the preceding checkpoint.
- Bad handoff: revoke that handoff and rebuild it from its approved source; rerun only its target.
- Bad approved memory: mark every consuming run stale and restart from the last unaffected checkpoint.
- Earlier approved defect: retain the old branch for audit, mark it and all descendants `stale-by-ancestor`, then branch from immediately before the bad delta.
- Canonical asset change: create `v002` and restart at the earliest affected checkpoint. Never edit `v001`.
- Model/platform change: create a new branch and regression-test the critical states.
- Missing object or hash mismatch: halt; never silently substitute a similarly named older asset.
- After picture lock: require a change record covering editorial, VFX, color, sound, and subtitle consequences.

Example: if Shot 3’s cut is later found on the right cheek, Shots 3–5 are retained but invalidated. Roll back to `CP020`, create corrected `ST030_v002`, and regenerate Shots 3–5. Shots 1–2 remain untouched.

## Approval, finishing, and measurement

Hard rejects include any wrong cheek, hand, pocket, owner, seal state, wetness reset, horizontal mirror, axis crossing, prop duplication, or Nia being unreadable in Shot 5. Review the full opening, middle, contact moment, ending, and adjacent cut—not thumbnails.

Build the complete five-shot blocking cut before upgrading hero shots. Finish with localized rain/wound/hand cleanup, shot-matched wet materials and skin, rain onset plus continuous rain bed, coat/fence/envelope foley, and a full uninterrupted master playback. No subtitles are needed unless dialogue is later added.

Track first-pass approvals, retries per approved shot, continuity rejects by category, time and cost per approved second, usable seconds per hour, queue wait, and waste rate. All values remain `N/A` until actual runs exist; do not substitute estimates or platform marketing counters.
