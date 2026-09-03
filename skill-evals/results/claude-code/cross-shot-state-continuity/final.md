Here is the production plan. One framing note up front: the generator will not remember shot 1 when it renders shot 5 — continuity lives entirely in the state system below, where each shot reads the prior approved state and submits exactly one delta.

## 0. Assumptions and unknowns

Platform/model, aspect, per-shot duration, reference-slot limits, and the project retry ceiling are **not specified** — the plan is platform-agnostic and those must be filled in at charter time (my archived Seedance knowledge is dated 2026-08-22; re-check current docs). No numeric retry ceiling is invented below; it's a required input. Operating mode assumed: **quality-max on hero states** (envelope, cheek, coat wetness) since the whole scene is a continuity exercise.

## 1. Scene state machine (the spine)

Three tracked entities evolve; everything else is invariant. Each state is a separate immutable asset version — never overwrite the dry coat sheet with a wet one.

| Track | S1 | S2 | S3 | S4 | S5 |
|---|---|---|---|---|---|
| Coat | `WARD-NIA-CREAM-DRY-v1` | → `WARD-NIA-CREAM-WETSHLDR-v1` | frozen | frozen | frozen |
| Injury | none | none | → `INJ-NIA-LCHEEK-FRESH-v1` | frozen | frozen |
| Envelope | unsealed → **sealed** | sealed, Nia's right inner pocket | sealed, pocket (invariant) | sealed, Nia right hand → **Tomas** | sealed → **opened** (Tomas) |
| Weather | dry `LOC-A-DRY-v1` | → rain begins `LOC-B-RAIN-v1` | rain `LOC-C-FENCE-RAIN-v1` | rain, under awning `LOC-D-AWNING-RAIN-v1` | frozen |

Key design decisions:

- **Wetness is frozen at "shoulders wet" after shot 2.** Progressive soaking across 3–5 is unverifiable drift bait; declare `WETSHLDR` an invariant for shots 3–5 rather than letting each render pick its own saturation.
- **Shots 4–5 happen under an overhang/awning.** Rain continues in the background (preserves weather continuity and Nia's wet/injured look) but the envelope and its contents stay dry and legible when Tomas opens it — otherwise shot 5 has a physics problem (soaked paper).
- **Envelope has exactly four legal states**: `unsealed → sealed → in-pocket-sealed → opened`. `opened` is reachable only in shot 5 and only in Tomas's hands.

## 2. State-specific asset inventory (passports)

Each entry: stable ID, version, `draft/approved/retired` status, sha256, owner, and admitted/denied reference channels recorded in the production registry (not the provider's asset panel).

**Characters**
- `CHAR-NIA-v1` — face/hair/build, front + both profiles. Both-cheek references matter: the left-cheek cut is a mirror-flip hazard, and QC needs a clean baseline of each cheek.
- `CHAR-NIA-LCHEEK-CUT-v1` — Nia identity sheet with the fresh cut composited on the **left** cheek, approved before shot 3 queues. This, not prompt prose, is the authority of record for the injury from shot 3 onward.
- `CHAR-TOMAS-v1` — enters registry at shot 4; forbidden in shots 1–3.

**Wardrobe** — `WARD-NIA-CREAM-DRY-v1` and `WARD-NIA-CREAM-WETSHLDR-v1` (same coat, darkened saturated patches on shoulders/upper arms only, dry below chest). Two sheets, never combined.

**Props** — `PROP-ENV-BLUE` geometry sheet (color, size, flap style, any seal mark) plus per-state versions: `-SEALED-v1` (authority for shots 1–4) and `-OPENED-v1` (torn flap, shot 5 only). If the envelope carries visible text, render it clean in post, not in generation.

**Reference authority rule:** identity, coat color/cut, envelope look, and injury are carried by approved image assets; prompt text carries only the shot's delta and blocking. Never state the same attribute in both channels. Reference packet order is part of the contract — reproduce it exactly on retry.

## 3. Screen direction and geography

One line of action for the whole scene, locked before any generation:

- **Nia travels frame-left → frame-right** in shots 2 and 3 (fence crossed left-to-right).
- **Camera stays on Nia's left side of the axis for shots 3–5.** This is deliberate: with camera on her left, her cut left cheek faces camera — visible, checkable, and any mirror-flip by the model is instantly caught in QC.
- **Shot 4–5 axis:** Nia frame-left facing frame-right; Tomas frame-right facing frame-left; eyelines locked to each other. The envelope transfer moves left-to-right, matching her travel direction, from her **right hand** to his **left hand** (the natural facing-transfer geometry — specify his receiving hand or the model will improvise).
- Forbidden in every shot: axis jumps, mirrored compositions, Nia entering from frame-right.

## 4. Shot contracts (manifest)

`SC-001` scene state file `SC-001_continuity-state_vNNN.yaml` is updated only on shot approval.

```yaml
SH-001-010:  # Seal
  required: [CHAR-NIA-v1, WARD-NIA-CREAM-DRY-v1, PROP-ENV-BLUE, LOC-A-DRY-v1]
  forbidden: [CHAR-TOMAS, rain, wet-coat, any-injury, PROP-ENV-BLUE-OPENED]
  population: {people: 1, key_props: 1, closed: true}
  start: envelope unsealed in Nia's hands
  primary_delta: Nia seals the blue envelope
  end: sealed envelope in Nia's right hand; coat fully dry; face unmarked
  coverage: medium + insert on hands/flap (hands + prop = high risk; the insert
    is the edit cover if the master's seal action fails)

SH-001-020:  # Rain begins
  required: [CHAR-NIA-v1, WARD-NIA-CREAM-DRY-v1→WETSHLDR-v1, LOC-B-RAIN-v1]
  forbidden: [CHAR-TOMAS, any-injury, envelope-visible-out-of-pocket, fully-soaked-coat]
  start: coat dry, envelope already stowed right inner pocket (stow happens
    off-screen between 1 and 2 — a hand-into-pocket action is a cheap
    insert pickup if the edit needs it)
  primary_delta: rain starts; shoulders darken with wet
  end: WETSHLDR state established; travel direction L→R
  invariants: [FACE-CLEAN, ENV-POCKETED]

SH-001-030:  # Fence / injury
  required: [CHAR-NIA-LCHEEK-CUT-v1(end-state), WETSHLDR-v1, LOC-C-FENCE-RAIN-v1]
  forbidden: [CHAR-TOMAS, right-cheek-injury, envelope-visible, dry-coat,
    blood-on-coat-beyond-cheek, torn-coat]
  population: {people: 1, key_props: 0 visible, closed: true}
  start: Nia approaches fence frame-left, face unmarked
  primary_delta: climbs fence L→R; wire/edge cuts LEFT cheek
  end: over the fence, thin fresh cut on left cheek, envelope never seen
  note: contact + injury + climb = highest-risk shot. Coverage split:
    (a) climb wide, (b) close on the cheek moment, (c) landing single
    showing the cut — three jobs, one shot, reassembled in edit.

SH-001-040:  # Handoff
  required: [CHAR-NIA-LCHEEK-CUT-v1, CHAR-TOMAS-v1, WETSHLDR-v1,
    PROP-ENV-BLUE-SEALED-v1, LOC-D-AWNING-RAIN-v1]
  forbidden: [PROP-ENV-BLUE-OPENED, left-hand-give, dry-coat, clean-cheek,
    bandage, third-person]
  population: {people: 2, key_props: 1, closed: true}
  start: Nia frame-left wet/injured; Tomas frame-right; envelope in her
    right inner pocket
  primary_delta: Nia draws envelope from RIGHT inner pocket with RIGHT hand,
    extends it; Tomas takes it — ownership transfers Nia→Tomas
  end: sealed envelope in Tomas's hands; seal visibly intact at boundary frame
  coverage: two-shot master + insert on the hand-to-hand exchange (the insert
    is the QC evidence that the seal survived and the correct hands were used)

SH-001-050:  # Open
  required: [CHAR-TOMAS-v1, PROP-ENV-BLUE-SEALED→OPENED-v1,
    CHAR-NIA-LCHEEK-CUT-v1, WETSHLDR-v1, LOC-D-AWNING-RAIN-v1]
  forbidden: [envelope-back-in-Nia's-hands, dry-coat, healed/clean cheek,
    injury-migrating-to-right-cheek, second-envelope]
  start: exact end state of SH-001-040
  primary_delta: Tomas breaks the seal and opens the envelope
  end: envelope open in Tomas's hands; Nia unchanged (wet, cut, watching)
  note: Nia is pure invariant here — her contract line is "no change,"
    which must be stated as inherited invariant IDs, not re-described prose
```

**Invariant slots** (referenced by ID so a change is a version bump, not five edits): `INV-COAT-STATE`, `INV-INJURY-STATE`, `INV-ENV-STATE`, `INV-AXIS-LR`, `INV-LIGHT-SC001`. Each shot inherits the current pointer; QC compares invariants at every boundary.

## 5. Handoffs between shots

At each approved boundary, write a **local handoff record**: last approved frame (QC-passed before promotion — `return_last_frame`-style transport is not approval), Nia's position/pose, travel vector, camera side of axis, prop owner + hand, wetness level, light direction, rain audio bed. Continuation relations: S1→S2 and S3→S4 are **intentional next shots** (story continuity, no frame-continuity promise — location changes); S4→S5 is **bridge known states** at the same setup and is the strictest boundary: Tomas's grip, envelope orientation, and both characters' positions must match frame-adjacently. Serialize the whole queue — every shot depends on its predecessor's approved end state (evolving wardrobe/injury/prop ownership forbids parallel generation). Only the inserts (envelope flap, hand exchange) can run in parallel once their parent master's state is approved.

## 6. Versioning, naming, retry lineage

- **Naming:** `SC001_SH-040_take-002_run-r011_prompt-p003_ref-r005_v001.mov`; assets as `CHAR-NIA-LCHEEK-CUT_v001_APPROVED.png`. IDs are never reused; `APPROVED` in a filename is a readable aid — status metadata is authoritative.
- **Run ledger** per generation: `run_id, parent_run, shot_id, prompt hash + composing block versions, ordered reference packet with hashes, the one changed variable, retry_class (resample vs. single-variable revision), output hash, timecoded defects, reviewer, decision, route`.
- **Retry rules:** retries always branch from the **last accepted parent run**, never from a rejected child — a rejected take is diagnostic evidence only and can never become a handoff source, approved memory, or canonical truth, even if one nice frame in it "looks right." Change exactly one variable per retry so failures are attributable. When the (project-supplied) ceiling is hit, route sideways instead of grinding: cheek cut won't hold → composite it in post from the approved injury asset; hand exchange keeps failing → tighter insert or an over-the-shoulder that hides the contact frame.

## 7. Rollback — how later shots can't overwrite earlier state

- **Three stores, one-way flow:** the canonical bank (approved passports + scene-state YAML) is human-write-only — no generated output ever updates it automatically; approved memory holds promoted frames from *accepted* shots only; local handoffs serve adjacent shots and never override canonical truth.
- **Checkpoints:** immutable snapshot after bible lock and after each shot approval (`CKPT-SC001-SH010` … `-SH050`), containing the state YAML, approved hashes, and open defects.
- **Corruption recovery:** if shot 5 comes back with a dry coat or a right-cheek cut, the fix is *never* to edit earlier assets to match — roll back to `CKPT-SC001-SH040` and retry shot 5 from the shot-4 approved end state. If the state file itself was corrupted, return to scene start and **replay only accepted deltas** (seal → wet shoulders → cut → transfer) to reconstruct it.
- **Downstream firewall:** shots 1–3's approved renders and their state versions are pinned; nothing queued for 4–5 has write access to them. A shot-5 output showing a resealed envelope fails the `forbidden` gate at QC and is rejected before it can touch anything.

## 8. Remaining pipeline (brief)

Rough-cut the five approved takes plus inserts before final-quality upgrades — the cut will tell you whether you need the pocket-stow pickup between 1 and 2. Post handles: cut/blood touch-up consistency, any envelope text as a clean graphic, rain audio bed continuous across 2–5 (level drop under the awning), color match of the cream coat across dry/wet states in the grade. Archive checkpoints, ledger, and registry with the master.

**Inputs I still need from you before anything queues:** platform + model version, aspect/duration per shot, and the retry ceiling per shot. Everything else above is ready to execute.
