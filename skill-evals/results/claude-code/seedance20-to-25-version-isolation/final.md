The Write tool is disabled in this session, so I can't create the plan file — and since the deliverable here is pure text (no files, no code, no execution), I'll deliver it directly. The skill and its schema are loaded, and they settle both halves of the request: the shot prompt itself, and what to do with the colleague's Seedance 2.0 identifiers.

**Bottom line on the colleague's request:** I'm not putting the Seedance 2.0 numeric mode, model ID, API field, or tag into a Seedance 2.5 JSON request, and I'm not emitting a 2.5 JSON request at all yet. Those four items are runtime facts verified (at best) for a 2.0 surface at a past date; version isolation means they don't carry into a 2.5 or generic artifact, and I won't invent substitute 2.5 values either. Separately, since the current surface is unknown, any endpoint JSON would require guessing field names — so below is the platform-neutral prompt plus a parameter manifest, with one blocking question at the end.

---

## Input basis

- **Task:** text-to-video, single clip, one primary event (cyclist arrives and stops).
- **Runtime:** platform, model, and mode **unknown** — no surface is selected.
- **Kept out of the prompt as unknowns:** aspect ratio, resolution, duration parameter, frame rate, audio support, and every API field name. These are runtime decisions, not directing decisions.
- **Not transferred (version isolation):** the colleague's Seedance 2.0 numeric mode, model ID, API field, and tag. They belong to a 2.0 surface on its original date. Seedance 2.5's actual parameters are **unknown** here (my archived knowledge is dated 2026-08-22); they must come from the current docs of the surface actually chosen, not from the 2.0 run and not from memory.
- **What does transfer:** the directing craft below — blocking, causal action, physics, observable acting, light logic, end state. None of it makes a capability claim, so it's safe on any surface.

## Final prompt (platform-neutral)

```text
[TASK AND INTENT]
Generate one continuous clip: a lone cyclist rides up a quiet street at dawn,
brakes, and comes to a full stop beside a bakery storefront, drawn by its
lit window.

[EXACT ENTITIES]
Exactly one cyclist: adult, light jacket, canvas bag slung across the back,
riding a classic steel-frame city bicycle. One bakery storefront with a large
glass window glowing warm from inside, "open" sign visible, a few loaves on
display. No other people, cyclists, or vehicles anywhere in the shot.

[LOCATION AND SPATIAL MAP]
Narrow street at dawn. Bakery occupies the right third of frame, its window
facing the sidewalk. Street recedes into cool blue haze frame-left. The
cyclist enters small in the background frame-left, traveling toward the
foreground and toward the bakery on the right. Damp pavement, faint mist.

[FIRST FRAME AND BLOCKING]
First frame: bakery window warm and lit on frame-right, empty street
frame-left, cyclist a small figure in the far background already in motion
toward camera.

[OPTICS AND CAMERA]
Medium-wide from sidewalk height on the bakery side of the street. One
primary move: the camera holds, with only a slow, slight drift left as the
cyclist arrives. Focus follows the cyclist. No cuts, no second camera move.

[ACTION BEATS]
Beat 1 — approach: the cyclist pedals steadily toward the foreground,
posture upright, glancing toward the lit bakery window.
Beat 2 — braking: hands squeeze the brake levers; the bike visibly slows
over several meters, body weight shifting forward.
Beat 3 — stop: the bike halts beside the bakery window; one foot lowers
and plants flat on the pavement; the bike tilts slightly toward the
standing leg.

[PHYSICS]
Deceleration is gradual and continuous — wheel rotation slows, no sliding
or teleporting. On stop, the planted foot takes weight, shoulders settle,
the bicycle stays upright between the rider's legs, front wheel turned a
few degrees toward the curb.

[OBSERVABLE ACTING]
The cyclist's gaze moves from the road to the bakery window during the
approach and stays on the window after stopping. On stopping: one visible
exhale that fogs faintly in the cold air, grip on the handlebars relaxes,
a small settling of posture. No dialogue; the cyclist stays silent.

[LIGHT, COLOR, MATERIAL]
Two motivated sources only: low warm sunrise light raking down the street,
and warm tungsten spill from the bakery window pooling on the wet sidewalk.
Everything outside those pools stays cool blue-grey. Wet pavement carries
a soft warm reflection of the window.

[POSITIVE CONSTRAINTS]
Exactly one person and one bicycle for the full duration. The bakery
window stays lit throughout. No on-screen text, no subtitles, no music.

[END STATE]
Final frame: the cyclist stationary astride the bike beside the window,
one foot planted, face turned toward the glass, warm window light on their
face, street empty behind them, camera settled and still — a clean cut point.
```

## Acceptance checks

- Exactly one cyclist and one bicycle in every frame; no bystanders or vehicles appear.
- Deceleration is visible and continuous — braking, weight shift, then foot contact with pavement, in that causal order.
- The stop lands beside the bakery window, not past it or short of it.
- Light logic holds: warm window/sunrise pools against a cool street, window lit for the full clip.
- Final frame matches the end state (stationary, foot planted, gaze at window, camera still) and is cut-ready.

## Failure risks

- Extra pedestrians or cyclists spawning in the background street.
- A "soft stop" with no physics — the bike simply becomes stationary without visible braking or foot-down.
- The camera inventing a second move (push-in or orbit) that competes with the arrival.
- Dawn drifting into full daylight or generic overcast, losing the two-source light contrast.

## Revision ladder (one variable per step)

1. If extra people appear → tighten only the entity constraint ("street completely empty behind the cyclist for the entire clip"); everything else fixed. Stop if clean after one retry.
2. If the stop lacks physics → expand only the braking beat with a longer deceleration distance; keep entities, camera, and light untouched.
3. If the camera drifts → change only the optics block to a fully locked static frame.
4. If two single-variable revisions fail on the same axis → stop revising and route to QC on the rendered evidence rather than stacking prompt changes.

## Parameter manifest — decisions the runtime must supply

| Decision | Status |
|---|---|
| Platform/surface and displayed model | unknown — user choice, not mine to make |
| Model ID / API field names / mode / tags | unknown for 2.5 — take from that surface's **current** docs after selection; the 2.0 values are not valid inputs |
| Aspect ratio, resolution, duration, frame rate | unknown — set only from the selected surface's documented options |
| Audio generation on/off | unknown — prompt assumes ambience-capable but degrades cleanly to silent |

**One blocking question:** which platform/surface (and its displayed model/version) should the JSON request target? Once you tell me that, I'll build the request body from that surface's current documented fields — with the prompt above dropped in unchanged, and none of the 2.0 identifiers carried over.
