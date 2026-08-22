I have everything I need — the working directory contains only the three skills (no script, charter, ledger, or benchmark), so all numbers below are policy, and the claim register at the end marks what is official, self-reported, method evidence, or unknown. One housekeeping note: this session exposes only read tools, so I couldn't create the plan file; the plan is delivered here in full. Nothing in it authorizes paid generation — each batch needs your explicit go.

# 10-day / 12-minute festival pilot — workflow comparison and recommended plan

## 0. Evidence basis and unknowns you must close on day 0

- Archived Seedance knowledge date is **2026-08-22** (today). Limits, prices, concurrency caps, and parameters are time-sensitive; recheck the platform's current docs before the first batch.
- **Unknown until you record them (they gate everything below):** platform/surface, displayed model, model ID, region; per-clip duration, resolution, reference limits, and concurrency on *that* surface; the festival's tech spec (aspect, fps, codec, loudness, subtitle format, AI-disclosure rules); rights for likeness, voice, music, vehicle brand, and every reference; team size; daily generation budget.
- Evidence tags used below: **[official]** platform/launch documentation · **[self-report]** project-author briefs · **[method]** peer-reviewed/preprint method evidence · **[policy]** production rule not validated by paid generation · **[unknown]** no evidence either way.

## 1. Mode comparison

| | Quality-max | Speed-max-with-quality-floor | Hybrid (recommended) |
|---|---|---|---|
| Bible | Full bible, rights, location maps, entity schedules, color/sound scripts first | Minimum: protagonists, main locations, critical props, camera/color/sound grammar | Full passports for tier-A entities only (leads, voices, vehicle base+damaged, hero locations); minimum bible for the rest |
| Previz/anchors | Previz, keyframes/blockout, feasibility tests for every hero/high-risk shot | Animatic + blocking cut first; anchors only when blocked | Whole-film animatic by day 2; keyframes/blockout/feasibility for tier A only |
| Candidates & reviewers | Several per shot; independent reviewers; blind comparison where practical | One blocking candidate; upgrade only story-blocking shots | A: several + blind pairwise · B: one, upgrade when blocked · C: one |
| Review gates | Hard gates + intra-shot + adherence + cross-shot + neighbor-cut on every shot | Hard gates on every shot (never relaxed), lighter rubric beyond | A: full stack · B/C: hard gates + neighbor cut |
| Finishing | Full VFX/cleanup/color/ADR/foley/music/subs/master after picture lock | Exact text, plates, local defects, transitions, sound routed to post tools by default | Speed-max routing for B/C; tier A gets ADR/foley/VFX attention |
| Schedule shape | Heavy front (bible/previz) and heavy back (finishing after lock) | Flat; a cut exists from day 2 | Animatic day 2; tier-A serial chains days 1–6; finishing overlaps from day 6 |
| Fit for this pilot | Fits the three hero scenes; misfit for the rest — spends candidate/review load on replaceable coverage and compresses finishing into the last days | Fits establishing/inserts; misfit for hero dialogue and the crash — single candidate and simplified coverage exactly where floors are hardest to meet | Matches the bimodal risk profile: ~3 scenes carry most narrative value *and* most technical risk; everything else is replaceable coverage |
| Evidence status | [policy] no paid validation [FP-16] | [policy] [FP-16] | "Recommended" = best-supported *initial* policy; coordination overhead unmeasured; not a proven optimum [FP-16][FP-18] |

**Pareto statement:** no mode dominates on evidence. A workflow dominates only if it is no worse on every required quality/efficiency dimension and better on at least one, and that can only be shown on your ledger for your suite, model ID, platform, date, reviewers, floor, and budget [FP-18]. Hybrid is the recommendation because of the risk-profile argument above, not because of a measured win.

## 2. Hard floors — common to all tiers, never relaxed

**Hard gates** (any failure rejects the shot before any score is averaged):

1. Rights/safety/policy/delivery spec pass, and the required story beat is present.
2. Correct identity, required entities, and state; no critical extra entity (no third person in a two-hander, no second vehicle).
3. Continuity-critical direction/ownership/end state is unambiguous (axis, eyeline, who holds what, where the vehicle comes to rest).
4. No uneditable structural or blocking artifact.
5. Complete usable interval with handles, and compatibility with its neighbors.
6. Sound/text either passes or has an **approved post route recorded at approval time** (ADR, composite) — not decided later.

Plus three process floors: no rejected or drifted frame is ever promoted to reference; the generator does not approve their own final take; review the full clip, never a thumbnail.

**Project-specific floors [policy — not model averages]:**

| Shot class | Floor |
|---|---|
| Hero dialogue | One speaker per shot, exact scripted line in the scripted language; listener silent; eyeline/axis match the scene floor plan; identity fidelity to the canonical passport *before* any consistency judgment; contracted acting cues visible (gaze target, hands, reaction delay); audio passes on actual audio evidence (exact words, voice identity, naturalness, sync checked at dense lip-frame sampling) **or** shot is approved picture-only with ADR route recorded |
| Crash | Visible contact before response; trajectory/gravity/inertia coherent; exact vehicle count, no morph/duplicate; damage matches the `VEH-damaged` passport version; debris/smoke settle to a stable end state; camera motion coherent with subject motion; aftermath shots read the approved impact end state |
| Establishing / inserts | Location passport fidelity (geometry, landmarks, time/weather state); no unrequested people, vehicles, text, or subtitles; stable ending ≥ handle; no BGM unless the sound bible asks |
| Delivery | Meets the festival spec recorded on day 0 [unknown today] |

## 3. Hierarchy, risk tiers, and coverage

**Tiering rule:** grade each shot by narrative value × technical risk. **A** = hero-dialogue turn beats/identity close-ups + crash impact/aftermath. **B** = hero masters, ordinary lines, OTS, reactions, crash approach/inserts. **C** = establishing, inserts, plates, textures.

**Shot count** comes from the breakdown, not from me: 720 s ÷ your target average shot length (e.g. a 5 s ASL → ~144 shots; that's arithmetic, not a performance claim).

**Hero dialogue scene (×2):**
- Scene card: purpose, start/end story state, cast, wardrobe state, props/ownership, floor plan with axis, eyelines, camera positions, room tone.
- Beat = one line plus its reaction. Never put a multi-line exchange in one clip [FP-08].
- Coverage: master two-shot (B, locks geography) → speaker singles per line (A for turn beats, B otherwise) → OTS pairs (B) → **silent reaction singles** (B/C — dialogue-free, cheap edit cover, and the standard rescue when a speaking take fails) → hand/prop inserts (C) → entrance/exit handles (C).
- Audio: generated dialogue is a scaffold; the archive's only bounded AV audit did not establish dialogue exactness, naturalness, or phoneme sync [unknown, QC-12/PD-13]. Pre-approve ADR; keep voice rights and a pronunciation dictionary in the voice passport. Whether to generate *with* dialogue or picture-only is itself untested — test it on day 2 (§10).

**Crash:**
- Beats: B1 approach · B2 trigger/swerve · B3 impact · B4 aftermath/settle · B5 reactions & inserts · B6 exit/transition. One causal event per shot.
- B3 on a locked/simple camera first [practice recommendation]; inserts (tire lock, hands on wheel, windshield, mirror) and bystander reactions are parallel B/C shots that let the edit carry the impact if B3 picture is weak.
- Assets: `VEH-001-base` and `VEH-001-damaged-v01` as separate immutable versions, built from clean art — never from a generated frame unless that frame passed QC and was promoted with source/timecode/crop recorded. Diagram/blockout of path and camera positions; keyframes for pre- and post-impact states (relatively strict, never pixel locks) [FP-09].
- Route ladder, one variable per rung: lock camera + single event → add blockout/state asset → split B3 into contact / result → **implied impact** (cut at contact; aftermath + sound design — the editorial route live-action uses constantly) → VFX composite / 3D sim → story redesign.
- Boundary: official launch material acknowledged complex action physics and large multi-subject interaction as weak areas [official, qualitative]; **no failure rate exists**, so plan the fallback from day 1 rather than betting on retries.

**Tier C rules:** one candidate, lighter rubric (hard gates + stability + neighbor), fully parallel, replaceable — the route after ceiling is "another approved candidate, another angle, or drop the shot."

## 4. Bible, passports, state, and references

- **Passports:** `CHAR-001/002` (+ supporting) with identity refs (front/profile/¾, sizes, expressions), behavior grammar, handedness; `WARD-*-base` and any post-crash variants; `INJ-*` if the crash causes injury; `VOICE-*` (language/accent/register/tempo/pronunciation/rights); `VEH-001-base`, `VEH-001-damaged-v01`; `LOC-*` for both hero scenes, the crash site, and each establishing location, with time/weather/light states; `PROP-*` with owner/hand state machines; camera grammar, color script, sound bible (room tones, crash SFX intent, music motif/silence), subtitle style, VFX grammar. A new state is a new immutable version — never overwrite the base [FP-04].
- **Three stores** [policy, not Seedance internals — FP-05]: canonical bank (human-approved only) · approved memory (frames promoted from accepted shots after QC, with source/timecode/crop/use boundary) · local handoff (transient neighbor pose/direction/light/room tone; never overrides canonical).
- **Reference policy:** smallest set that adds unique information; every reference has one job and explicit inheritance exclusions; upload-order bindings; rights recorded. The archived ModelArk ceiling (30 images/10 videos/10 audio/50 total at 2026-08-22) is a ModelArk fact at that date, not a target, and does not transfer to other surfaces.
- **IDs/lineage:** `FILM-*`, `SQ-nnn`, `SC-nnn-nnn`, `BT-…`, `SH-…`; IDs never reused; status metadata is authoritative. Run ledger per run: parent run, prompt hash, references/hashes/roles, the one changed variable, output hash/duration/spec, queue/generation/review/human time, billed cost, gates, timecoded defects, reviewer, decision, route [FP-13][FP-14].

## 5. Queue — what runs in parallel, what runs serially

```text
Day 0 bible/passport lock
 ├─> Tier C establishing / inserts / plates ........... PARALLEL, any time after the LOC passport is approved
 ├─> SC-H1 master ─> singles A ∥ singles B ∥ OTS ∥ reactions ─> inserts
 ├─> SC-H2 master ─> (same)            H1 ∥ H2 unless a carried wardrobe/injury state links them (see note)
 └─> Crash feasibility (B3, locked cam) ─> B1 approach ∥ inserts ∥ reactions
        └─> B3 approved ─> VEH-damaged passport approved ─> B4 aftermath ─> any later scene showing damage/injury
Rolling assembly ∥ sound spotting ∥ VFX breakdown ∥ subtitle prep  (parallel: they don't mutate the same truth)
Structure lock ─> pickups ─> VFX/cleanup/conform ∥ ADR/foley/music ─> color ─> subtitles (from final audio) ─> master ─> QC ─> archive
```

- **Parallel:** independent establishing/insert/reaction/cutaway/plate/texture shots; scenes with locked canonical assets and no handoff dependency; within a hero scene, both characters' singles once the master has locked geography; review/sound/VFX/subtitle prep alongside generation.
- **Serial:** extension chains and continuous action (use extension only for short adjacent continuity, never a long drift chain [FP-15]); evolving wardrobe/injury/weather/prop ownership in entity-schedule order; any shot that depends on an approved prior last frame or motion vector (the crash B3→B4 chain); canonical/approved-memory promotion; hero close-ups **after** scene geography/blocking is approved.
- **Note on carried state:** if hero scene 2 is post-crash, its `WARD`/`INJ` versions must be approved before generation — the dependency is on passport approval, not on scene-1 renders, so the scenes still run in parallel.
- **Batching:** batch only identical platform/model/task/ratio/resolution/format/reference-packet/rubric, or failures cannot be attributed. Concurrency cap: [unknown] — record it on day 0; it may force serialization the graph doesn't.

## 6. Retry / route ceilings and stop rules

Ceilings are derived from the 10-day clock and each tier's replaceability, not from model data. The archive's 10–15 / 15–20 figures are heuristics from a production document, **not model averages** [FP-14]. Recalibrate all of these from the day-2 ledger using P90 retries per tier.

| Tier | First pass | Ceiling (valid one-variable retries beyond the first) | Early stop | Route after ceiling |
|---|---|---|---|---|
| C establishing/inserts | 1 candidate | 2 | same defect twice | other approved candidate / alternate angle / drop |
| B standard | 1 candidate | 4 | same defect twice, or oscillation | split / insert-reaction-cutaway / reframe / local edit |
| A hero dialogue | 2–3 candidates, blind pairwise | 6 per shot **and** a per-scene time box (policy: ~1.5 days of generation wall-clock per hero scene) | same blocking defect twice after an isolated change; oscillation; would need a drifted frame | split beat / picture-only + ADR / reaction-shot reconstruction / reframe |
| A crash impact | feasibility ladder days 1–2 | 6 per shot **and** calendar gates: route decision end of day 4, hard switch no later than day 6 | same physics defect twice after an isolated change | implied-impact edit → VFX composite/3D sim → redesign |

**Universal stop conditions:** the same blocking defect survives isolated relevant retries; fixing one critical constraint repeatedly breaks another; the ceiling is hit; progress would require a rejected/drifted frame as truth; rights/platform/delivery cannot pass; a mature edit/VFX/ADR/graphics route has lower expected loss. Stopping preserves the last approved checkpoint, failed hypotheses, evidence, and next route — never discards history.

**Rollback:** retry from the parent approved run, never a rejected child; if axis/state/wardrobe is corrupted, return to the scene-start checkpoint and replay approved deltas; after structure lock every change needs a record of downstream VFX/sound/subtitle/color impact; a model/platform update is a new branch with a regression check, never an overwrite. **Checkpoints:** bible lock, previz lock, approved-shot lock (rolling), structure lock, sound/color lock, master.

## 7. Ten-day schedule [policy — no throughput evidence says it fits; it is built to degrade gracefully: drop C, imply the crash, ADR the dialogue]

| Day | Generation | Review / editorial | Post | Checkpoint |
|---|---|---|---|---|
| 0 | none | Charter: platform/model/doc date, festival spec, rights, disclosure; minimum bible + tier-A passports; breakdown, floor plans, tiering; ledger/naming; role assignment | Sound bible, color script, subtitle style | CP-bible |
| 1 | Crash feasibility (B3, locked cam); hero masters; tier-C batch 1 | Storyboard/blockout animatic with human temp VO | Temp sound | CP-previz |
| 2 | Hero-beat dialogue A/B test (§10); tier-C batch 2; crash B1 + inserts | Animatic complete end to end; dailies; **recalibrate ceilings from ledger** | — | — |
| 3–4 | Hero singles/OTS/reactions (H1 ∥ H2); crash chain B3→B4 | Rolling assembly; dailies; **crash route decision end of day 4** | VFX breakdown; ADR prep | CP-approved-shots (rolling) |
| 5 | Remaining A/B; pickups identified | Rough cut v1 | ADR records begin | — |
| 6 | Pickups only; **crash hard route-switch deadline** | **Structure lock**; change control after | VFX/cleanup start | CP-structure-lock |
| 7–8 | None planned (change request only) | Conform | VFX/cleanup, color, dialogue edit/ADR, foley, music, mix | CP-sound/color lock |
| 9 | — | — | Subtitles from final audio; master; one full uninterrupted playback + targeted checks | — |
| 10 | — | — | Fixes, re-QC, delivery, archive (buffer) | CP-master |

## 8. Post-production responsibilities

| Role | Owns | Must not |
|---|---|---|
| Producer | Charter, rights, clock/budget ceilings, change control after lock, KPI dashboard | Promote generated output to canonical |
| Generation lead / prompt director | Shot contracts, prompts, one-variable ladders, ledger entries | Approve own final takes |
| Independent QC reviewer(s) | Hard gates, full-clip review, timecoded findings, route decisions, memory promotion | Accept on thumbnails; generalize coarse mouth motion to lip-sync |
| Editor | Animatic, rolling assembly, rough cut, pickups list, structure lock, EDL, handles | Hide retiming or continuity damage with undocumented time-stretch |
| VFX / cleanup | Exact-text composites, paint/roto, crash composite/sim if routed, plates, normalize/conform | Treat regenerate as the default |
| Sound | Dialogue edit, ADR/dubbing under voice rights, foley, crash sound design, music, loudness | Treat generated audio as final without actual-audio evidence |
| Color | Shot match, motivated light, skin/material, day/weather state, legal range, calibrated playback | Trust a `4k` badge as generation resolution |
| Subtitles | Timed from **final audio**; language/speaker/reading speed/safe area; burned vs sidecar per spec | Time from prompt timestamps |
| Mastering / QC | Spec conformance, full playback, checksums, naming | — |
| Archive | Master, stems, subs, project files, ledgers, hashes, approvals, checkpoints | Retain credentials, cookies, or signed URLs |

On a small team people double up, but reviewer independence is the one separation that must survive.

## 9. KPIs — all from the run ledger, never from UI counters or price pages [FP-17]

```text
first_pass_approval      = approved on first valid run / valid first runs          (per tier)
additional_retries       = extra valid runs before approval / approved shots       (median, P90 per tier)
time_per_approved_shot   = shot-ready → approved wall clock
usable_seconds_per_hour  = approved seconds entering cut / production-review hours
cost_per_approved_second = all billable runs + dedicated post tools / in-cut seconds
human_correction_time    = prep + review + edit/VFX/sound fix hours
queue_wait_ratio         = queue time / shot-ready-to-result time
waste_rate               = generated seconds (or cost) not entering cut / total generated
```

**Quality vector per shot** (pass/fail, optional 1–5 for comparisons, every score timecoded): beat adherence; identity/wardrobe/injury/location/prop/voice continuity; temporal stability and artifact rate; motion/contact/inertia causality; camera/composition/light; dialogue/lip-sync/ambience/SFX/music/subtitle correctness; editorial usability.

**Schedule KPIs [policy targets, not performance claims]:** animatic covers 100% of runtime by end of day 2; % of runtime covered by approved shots (daily, target 100% at structure lock day 6); tier-A hard-gate passes vs. planned; open critical/major defects trend; crash route status (in-model / implied / VFX); ADR coverage of hero lines; human correction hours.

**Reporting rules:** declare the denominator rule for failed/moderated/corrupt runs; report median and P90; state results only for this suite, model ID, platform, date, reviewers, floor, and budget. The dashboard may not claim model averages, cross-platform rates, or "fastest and best."

## 10. Embedded mini-benchmark (turns days 1–2 into your first real data)

You have no controlled benchmark; the feasibility and first-batch runs can double as one if designed as such [method — QC-17]: same shot contract, rubric, and evidence scope; blinded labels and order; ties allowed; same-seed pairs only where the platform documents seeds, treated as approximately comparable; declared denominator rule; reviewer ≠ generator. Three one-variable contrasts worth the spend:

1. One hero beat: generate **with dialogue** vs **picture-only + ADR** → sets the dialogue default for both hero scenes.
2. Crash B3: **locked camera** vs **moving camera** (or with/without blockout) → sets the impact ladder order.
3. A small affordable sample of tier-C shots: **one candidate** vs **two candidates** → sets whether C ever gets a second candidate.

Output on day 3: recalibrated ceilings per tier and defaults, valid for this project only.

## 11. Policy vs. proven — claim register

| Claim used in this plan | Evidence class | Boundary |
|---|---|---|
| Film→Sequence→Scene→Beat→Shot decomposition; no giant prompt | [official] clip duration + [method] MovieBench, high confidence | Architecture, not a Seedance built-in |
| Versioned passports / external memory improve continuity | [self-report] + synthesis, medium-high | Effect size unmeasured |
| Early animatic and rolling assembly expose coverage holes | [self-report] across four briefs | No controlled causality or ideal overlap |
| Complex action physics and multi-subject interaction are weak | [official] launch acknowledgement, qualitative | **No failure rate exists** |
| Generated dialogue/lip-sync is dependable | [unknown] | Only bounded audit did not establish exactness, naturalness, or phoneme sync |
| Diagrams/keyframes/locked camera help physics shots | practice recommendation | Not controlled; keyframes are not pixel locks |
| Retry ceilings in §6 | [policy] clock-derived | 10–15 / 15–20 are heuristics, not model averages |
| Three modes; hybrid recommended | [policy] evidence-supported | No paid validation; hybrid overhead unmeasured; no Pareto winner |
| Same-seed comparisons | approximate only where documented | No determinism claim |
| Costs, times, success rates | **none available** | Ledger only; I have invented none |
| ModelArk reference ceilings (30/10/10/50) | [official] at 2026-08-22, ModelArk only | Not a target; not transferable; recheck |

---

**Recap.** I loaded the producer skill and its references, confirmed the directory holds no project data (so every number here is policy), and built the comparison around the pilot's bimodal risk profile: quality-max fits the two hero dialogue scenes and the crash but wastes its heaviest review on replaceable coverage and back-loads finishing; speed-max fits the establishing/insert shots but applies single-candidate, simplified coverage precisely where the floors are hardest; the hybrid applies each mode where it fits, under common floors that never relax. The plan gives six hard gates plus per-class floors, a dependency graph (hero scenes and all tier-C shots parallel; the crash B3→B4→damaged-passport chain and any carried wardrobe/injury state serial), tier-scaled retry ceilings with calendar gates for the crash (decide day 4, switch by day 6), a role-by-role post table, ledger-defined KPIs, and a day-1–2 mini-benchmark that produces your first real numbers for recalibrating the ceilings on day 3. Your next step is day 0: record the platform/model/doc date, the festival tech spec, and rights — those three unknowns gate everything else — then authorize the feasibility batch.
