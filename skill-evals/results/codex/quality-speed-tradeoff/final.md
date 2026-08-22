Use the hybrid: quality-max treatment for irreplaceable performance and crash anchors, standard treatment for narrative coverage, and speed-max treatment for replaceable establishing/insert shots. This is a production-policy recommendation, not a proven optimum.

## Evidence status and prerequisites

As of 2026-08-22:

- No controlled benchmark has been run. Approval rates, throughput, retry counts, costs, and completion probability are therefore `N/A (n=0)`.
- The retry limits, quality floors, and day gates below are management rules—not performance estimates.
- Day 1 must lock the actual platform/surface, model/version, region, quotas/concurrency, festival rules, delivery specifications, rights, budget ceiling, and named reviewers. Do not transfer capabilities or limits between platforms.
- The plan assumes the script and dialogue can lock on Day 1 and that generation, editorial, and post can overlap. “Parallel” means logically queueable; actual capacity remains an unknown.

## Shot tiers

- **A — hero:** performance-critical singles/two-shots from both dialogue scenes; crash geography, impact, and consequence anchors.
- **B — narrative:** dialogue masters, OTS, reactions, exits, critical prop handoffs; crash approach/recovery and essential transitions.
- **C — connective:** establishing shots, inserts, cutaways, plates, textures, and other replaceable coverage.

Tiering is per shot or beat, not per scene. All tiers keep the same hard floor.

## Workflow comparison

| Decision | Quality-max | Speed-max with floor | Recommended hybrid |
|---|---|---|---|
| Preparation | Full character, voice, wardrobe/injury, location, prop, vehicle/damage, camera, color, VFX, and sound passports; detailed A-shot previz | Minimum approved hero/location/vehicle/prop passports; complete rough animatic; simplify coverage aggressively | Full A passports and previz; standard B packets; lean but approved C packets |
| Dialogue scenes | Multiple performance candidates, deeper independent review, more coverage | Short single-beat shots, minimum viable coverage, early ADR/OTS/reaction routes | A treatment for key performances; B treatment for masters, OTS, reactions, and edit cover |
| Crash | Detailed trajectory/blockout; more generated candidates before VFX route | Pre-route difficult contact to fragmented coverage, sound, compositing, or 3D | Quality treatment for geography and emotional anchors; planned VFX/3D route for persistent contact physics |
| Low-risk shots | Parallel after comprehensive look/state lock; some optional refinement | Broad one-pass fan-out; failed C shots are substituted, not polished | Broad one-pass C queue while A work proceeds |
| Review | Two independent A reviewers; candidate comparison where useful | One accountable shot reviewer plus independent final QC | Two reviewers for A; one for B/C; every edit checked at structure lock |
| Schedule policy | Structure lock Day 8; least finishing contingency | Structure/picture lock around Day 6; most finishing contingency | Structure lock Day 6, picture lock Day 7 |
| Main trade-off | Most selectivity, but final decisions arrive latest | Maximum schedule protection, but little optional refinement | Concentrates time where failure is visible while protecting post-production |

Quality-max is not simultaneously speed-max. Speed-max does not waive the floor; it changes coverage and routes failures earlier.

## Non-negotiable hard floors

Use `PASS`, `FAIL`, or `N/A_WITH_REASON`. Missing evidence is a failure. A shot routed to ADR, VFX, or cleanup is not approved until the finished result passes.

| Gate | Final floor |
|---|---|
| Rights, safety, delivery | 100% of used likenesses, voices, references, music, brands, fonts, and outputs have approved status; 100% festival/master checks pass |
| Story | 100% of locked mandatory beats have accepted editorial coverage; no placeholder counts as final coverage |
| Identity and state | Correct character, voice, wardrobe/injury, location/light, vehicle damage, prop owner/hand, screen direction, and required/forbidden entities |
| Editorial usability | Complete contracted interval plus 12 handle frames on each required edge at master frame rate, or an editor-approved intentional-cut waiver; 100% critical neighbor joins reviewed |
| Structural defects | Zero unresolved blocker or major anatomy, topology, temporal, camera, contact, text, or audio defects in selected intervals |
| Dialogue | 100% locked utterances represented; zero unapproved wording/speaker changes; correct voice and pronunciation; zero major sync-defect seconds during visible speech |
| Performance | 100% of scripted tactics, reactions, reveals, and emotional turns have accepted coverage |
| Crash | 100% of required causal beats and state transitions pass; geography, travel direction, impact cue, and consequence are readable; zero major physics-defect frames in visible crash action |
| Provenance | 100% of final picture/audio segments trace to an approved or licensed source, post transform, reviewer decision, and rights record |
| Final master | Zero temp media, missing media, unintended black/silence, watermarks, blockers, or majors; one uninterrupted playback plus targeted checks of every transition |

The crash floor is a coherent event, not a single uninterrupted generated collision. Contact may be fragmented or obscured if cause, impact, and consequence remain clear.

## Parallel and serial queues

The serial spine is:

```text
Charter/specs/rights
→ canonical passports and scene states
→ complete blocking cut
→ dialogue geography and crash trajectory anchors
→ high-risk route decisions
→ content-complete rough cut
→ structure lock
→ picture lock
→ conform/VFX/color and sound
→ final audio
→ subtitle timing
→ master QC
```

Serialize:

- Canonical asset approval and promotion into approved memory.
- Dialogue floor plan, axis, eyelines, and master blocking before hero close-ups.
- Exact prop, pose, or performance handoffs.
- Crash trajectory/direction → impact state → approved damage state → dependent aftermath.
- Extension chains and any shot relying on an approved prior last frame.
- Structure lock, picture lock, final audio, subtitle timing, mastering, and archive checkpoints.

Parallelize after the relevant state packet is locked:

- The two dialogue scenes, unless one requires an exact crash or wardrobe handoff.
- Singles, OTS, reactions, and inserts within each dialogue scene after geography approval.
- Establishing shots, inserts, plates, textures, and non-state-changing cutaways.
- Crash driver reactions, wheel/pedal inserts, exterior approaches, debris plates, obscured-impact angles, and sound/VFX development.
- Rolling editorial, full-clip review, ingest, cleanup preparation, and sound spotting.
- Color and sound after picture lock, reconverging at the master.

Do not make the crash one long prompt or extension chain. Decompose it into geography, recognition, avoidance input, short impact fragments, reaction, and aftermath.

## Retry and route ceilings

These are caps per independently cuttable shot/beat. “Extra retry” means after the first valid, reviewable candidate.

| Mode | A extra retries | B extra retries | C extra retries | Material route pivots |
|---|---:|---:|---:|---:|
| Quality-max | 5 | 3 | 1 | A: 2; B/C: 1 |
| Speed-max | 2 | 1 | 0 | 1 for every tier |
| Hybrid | 3 | 2 | 0 | A: 2; B/C: 1 |

Additional rules:

- The earliest stop condition wins: numeric cap, repeated defect, route gate, budget, or calendar cutoff.
- The same blocker appearing twice triggers rerouting even if attempts remain.
- Stop if identity/action constraints oscillate across revisions.
- Change only one prompt, reference, parameter, or shot-design variable per retry.
- Splitting or renaming a shot does not reset its attempt history.
- A route pivot does not replenish retries.
- Technical/provider failures are logged separately from creative attempts, but still consume wall clock and actual budget.

Route ladder:

1. Improve or state-specialize the reference.
2. Lock the camera, shorten, simplify, or split the action.
3. Replace with OTS, reaction, insert, cutaway, or alternate angle.
4. Use local cleanup, compositing, ADR/dubbing, or sound design.
5. Use 2D/3D/VFX/live action if allowed, or redesign the beat without losing its story function.

Every unresolved A shot needs an executable fallback by the end of Day 4.

## Recommended ten-day hybrid schedule

| Day | Required outcome |
|---|---|
| 1 | Lock script, specs, rights, platform/model, tiers, passports, shot contracts, ledger, owners, and failure routes |
| 2 | Complete the full 12-minute blocking cut; lock dialogue geography and crash trajectory/damage states; begin compatible C shots |
| 3–4 | Run both dialogue lanes after their anchor approvals; build the crash’s serial spine; run C shots, plates, editorial, VFX planning, and sound in parallel; lock the crash route by Day 4 |
| 5 | Content-complete rough cut containing every beat as accepted media or an owned, executable post route; freeze nice-to-have generation |
| 6 | Only blocking pickups; structure lock at end of day |
| 7 | Final source/pickup cutoff at midday; picture lock at end of day |
| 8 | VFX/cleanup, conform, color, dialogue edit/ADR, foley, crash sound, music, and mix |
| 9 | Final audio, subtitles timed from actual audio, master candidate, first uninterrupted playback |
| 10 | Bounded fixes, re-export, complete playback, targeted transition QC, checksums, delivery, and archive |

## Post-production responsibilities

One person may double-hat, but each function needs a named accountable owner.

- **Editorial:** blocking cut from Day 1, rolling assemblies, selects, handles, pickup list, structure/picture locks, conform, and master assembly.
- **Continuity/data:** immutable canonical bank, approved-memory promotions, local handoffs, state deltas, hashes, run lineage, checkpoints, and rollback.
- **VFX/cleanup:** crash plates/composites or 3D fallback, paint/roto, bounded artifact repair, and exact graphics/text.
- **Sound:** dialogue edit and ADR, pronunciation, room tone, foley, crash design, music, mix, loudness, and stems.
- **Color/conform:** normalize codec, frame rate, color tags, and audio layout; shot matching, skin/material/weather continuity, and delivery validation.
- **Subtitles:** prepare text early, but time only after final audio; verify language, reading, safe area, and delivery format.
- **QC/rights/archive:** independent content/technical/rights review; master, mezzanine, stems, subtitles, project files, sources, prompts, ledgers, approvals, model/version records, and checksums.

## KPI dashboard

Report every metric with date, A-dialogue/A-crash/B/C cohort, platform/model/version, rubric version, numerator, denominator, and sample size.

Hard readiness KPIs:

| KPI | Final target |
|---|---:|
| Required beat coverage | 100% |
| Approved final-timeline coverage | 100% |
| Critical neighbor-continuity pass | 100% |
| Rights, delivery, and provenance coverage | 100% |
| Dialogue-unit and performance-turn coverage | 100% |
| Crash-transition pass | 100% |
| Dialogue sync-blocker exposure | 0% |
| Crash physics-blocker exposure | 0% |
| Open blockers and majors | 0 |
| Routed-task closure | 100% |

Observed efficiency KPIs—no target until ledger data exists:

```text
first_pass_approval =
  approved from first valid candidate / reviewed first valid candidates

additional_retries_per_approval =
  extra valid candidates before approval / approved units

approval_cycle_time =
  approved_at - shot_ready_at

usable_seconds_per_human_hour =
  unique in-cut seconds / logged prep, review, edit, VFX and sound hours

queue_wait_ratio =
  exposed queue time / shot-ready-to-result time

technical_invalid_rate =
  invalid submitted runs / all submitted runs

waste_rate =
  generated frames not entering the cut / all valid generated frames

route_rate =
  approved units requiring an alternate route / approved units
```

Track actual billed cost per approved second only when invoice-level billing coverage is complete; otherwise show `N/A`, not an estimate. Report medians and distributions, adding P90 only with a meaningful sample size.

This production will generate observational ledger data, but because workflows are assigned by shot risk rather than randomly, it will not prove that the hybrid outperforms the other modes.
