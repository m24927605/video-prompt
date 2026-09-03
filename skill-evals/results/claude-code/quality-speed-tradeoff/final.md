Here is the comparison and recommended plan. Everything below is grounded in the skill's evidence-supported starting policies; since you have run no controlled benchmark, **every number in this document is a project policy you set, not a measured performance claim** — I've kept the two strictly separated and invented no costs or success rates.

## Assumptions and unknowns (state these in the charter)

- Archived Seedance knowledge is dated 2026-08-22; recheck the current docs for your actual platform (Seedance 2.0 vs 2.5, ModelArk vs UI) before locking parameters — limits and defaults do not transfer between surfaces.
- Unknown until you fill in: exact platform/model ID, per-day generation quota, budget ceiling, team size, festival delivery spec (aspect, codec, loudness, subtitle format), and rights status of any likeness/voice/music references. The schedule below assumes at least one dedicated reviewer/editor working alongside generation.

## Shot inventory and risk tiering

Grade every shot by narrative value × technical risk before choosing any workflow:

- **A-tier:** the two hero dialogue scenes (identity, performance, lip-sync, eyeline continuity) and the vehicle crash (contact physics — a known high-risk category).
- **B-tier:** scene masters, reactions, transitions with handoff dependencies, crash-adjacent coverage (approach, aftermath, debris inserts).
- **C-tier:** establishing shots, inserts, texture/plate shots with no continuity handoff.

The crash should be split at the beat level now, regardless of mode: approach → impact → aftermath, each independently generatable, plus alternate coverage (bystander reaction, sound-led off-screen impact, debris insert) so editorial can cut around a failed impact shot.

## The three workflows

**Quality-max.** Full bible and passports first; previz, keyframes, and feasibility tests for all A-tier shots; multiple candidates per shot with blind comparison; full gate stack including neighbor-cut review; complete finishing chain after picture lock. Trade-off: heavy asset, review, and coordination time. **In 10 days this mode is credible only for the A-tier shots; applied to all ~everything it risks missing delivery entirely, because finishing (color, mix, subtitles, QC) needs 2–3 protected days at the end no matter what.**

**Speed-max-with-quality-floor.** Minimum bible (protagonists, main locations, camera/color/sound grammar); complete animatic first; one blocking candidate per shot, upgrade only story-blocking shots; route exact text, clean plates, local defects, and sound to post tools. The floor never relaxes: story beats, identity, required entities, screen direction/prop state, intelligible sound, rights, delivery spec, and no uneditable blocking artifact. Risk: hero dialogue and the crash are exactly the shots where "one candidate, move on" produces a cut that passes gates but underwhelms a festival jury.

**Recommended hybrid (my recommendation for this pilot).** Make the whole film work end to end first, then spend quality only where it buys narrative value:

1. C-tier runs the speed workflow: one blocking candidate, batched in parallel.
2. B-tier runs standard references + QC; upgrade only when a shot blocks the cut.
3. A-tier runs the quality workflow: passports, previz/keyframes, multiple candidates, dedicated review.
4. Fix script, coverage, and continuity before pixel polish anywhere.

"Recommended" means current evidence best supports it as an initial policy — not that it is proven optimal for your team, model, and content.

## Hard floors (common to all modes, all tiers)

A shot cannot be approved, in any tier, unless it passes: rights/safety/delivery compliance; required story beat present; correct character identity, entities, and state versions; unambiguous continuity-critical screen direction and prop ownership; no uneditable structural/blocking artifact; a complete usable interval with handles and neighbor compatibility; and sound/text either passing or carrying an approved post route. Numeric aesthetic floors may be added per project but must never be presented as model averages.

## Parallel vs. serial

**Parallel:** all C-tier establishing/insert/plate shots (batch only within one platform/model/ratio/format so failures stay attributable); the two hero dialogue scenes relative to *each other* once their passports are locked; review, sound spotting, and subtitle prep against approved shots.

**Serial:** shots inside each dialogue scene that depend on an approved prior frame or established geography (approve the scene master before hero close-ups); the crash beat chain (aftermath state depends on the approved impact); any evolving damage/wardrobe state; promotion of any frame to approved memory (human gate, never automatic).

**Ten-day skeleton (hybrid):** Day 1 — charter, script lock, bible/passports, breakdown, risk tiering. Day 2 — blocking generations all tiers, C-tier parallel batch starts, end-to-end animatic. Days 3–4 — rough cut v1; hero previz/keyframes; crash feasibility tests. Days 4–6 — hero final generation (serial within scene, scenes in parallel); crash attempts. **Day 6 — structure lock and crash route deadline.** Days 7–8 — pickups, VFX/cleanup, conform. Days 8–9 — color, mix/ADR/foley, subtitles. Day 9 — master + one full uninterrupted QC playback. Day 10 — buffer and delivery/archive.

## Retry and route ceilings (proposed policy — ratify these, they are not benchmarked)

Change exactly one variable per retry; retry from the parent approved run, never a rejected child. Stop early regardless of ceiling if the same hard defect repeats twice (change variable class) or three times (route immediately).

- **C-tier:** 1 additional valid retry, then route (alternate angle, different C shot, or drop from cut).
- **B-tier:** up to 3 additional valid retries, then route to editorial workaround or simpler design.
- **A-tier dialogue:** up to 5 additional valid retries per shot, then route: split the shot, lock the camera, use reaction/OTS coverage, or ADR over usable picture.
- **Crash impact:** up to 6 total attempts across shot designs, hard-stopped by the Day 6 calendar deadline, then the pre-planned fallback: sound-led off-screen impact + reaction + aftermath, or a composited/VFX impact. The fallback is designed on Day 1, not improvised on Day 6.

## Post-production responsibilities

Post is a planned layer, not a rescue net. Route deliberately: exact text/logos/UI → composite in post, never regenerate for spelling; bounded local defects → paint/roto/local AI edit; unusable model speech over usable picture → ADR (voice rights and pronunciation live in the passport); persistent physics failure → composite/3D or the editorial fallback. Editor owns rough cut, structure lock, pickup requests, and documented (never hidden) retimes. Color owns shot match, state consistency, legal range. Sound owns dialogue cleanup, room tone across cuts, foley, music, loudness spec. Subtitles are timed from the final mixed audio, never from prompt timestamps. Final QC = one full master playback plus targeted checks of every edit/VFX/subtitle/audio transition, then archive masters, stems, ledgers, prompts, hashes, and checkpoints.

## KPIs (computed from your run ledger only)

Log every run (prompt hash, one changed variable, references, times, reviewer decision, route) and report, with medians and P90 where sample size permits:

- `first_pass_approval` = approved on first valid run / valid first runs, split by tier — this is the number that tells you after ~day 3 whether the C-tier speed policy is working;
- `additional_retries` per approved shot vs. the ceilings above (ceiling breaches are a policy alarm);
- `time_per_approved_shot` and `usable_seconds_per_hour`;
- `cost_per_approved_second` and `waste_rate` — from actual billing, never price pages;
- `human_correction_time` and `queue_wait_ratio`;
- schedule KPIs (these are policy targets, legitimately settable now): rough cut exists by end of Day 3, 100% of A-tier approved or routed by end of Day 6, structure lock Day 6, master Day 9.

Do not report marketing counters or UI totals as performance, and don't claim one mode "won" unless it is no worse on every floor dimension and better on at least one, for your specific model, platform, dates, and reviewers.

**Bottom line:** run the hybrid. Quality-max everywhere cannot protect the 2–3 finishing days a festival master needs; speed-max everywhere underserves the three shots the jury will actually judge you on. The two decisions to make today are the crash fallback design and ratifying the retry ceilings — after that, day 3's `first_pass_approval` numbers replace policy with your first real evidence.
