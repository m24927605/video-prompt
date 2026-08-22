## Input basis

- Task: new 9-second text-to-video shot; no first/last-frame assets; zero active references. Platform, model ID, aspect ratio, and endpoint remain unknown.
- Official fact, checked 2026-08-22: Seedance 2.5’s announcement says **up to 30 images**, not exactly 12. No images were supplied, so inventing 12 bindings would be harmful. It also acknowledges remaining physical-interaction limitations. [ByteDance Seed launch note](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)
- Official fact/inference: the published ModelArk task schema documents an integer `seed`, but neither guarantees deterministic replay nor lists a separate `negative_prompt` parameter. Because that schema predates Seedance 2.5’s launch, the selected 2.5 runtime behavior remains unknown. [Volcengine task API](https://api.volcengine.com/api-docs/view?action=CreateContentsGenerationsTasks&serviceCode=ark&version=2024-01-01)
- Official fact: current Volcengine Seedance 2.5 pricing is usage-based, not a fixed US$0.10 per generation. [Volcengine model pricing](https://www.volcengine.com/)
- Practice assumptions: silent video; locked camera; “final frame holds” means a static end composition.
- Unknown: 4K availability, exact reference limit, negative-prompt support, seed repeatability, cost, and guaranteed nine-second output on the eventual platform. First-pass success cannot be guaranteed.

## Final prompt

```text
Generate one continuous photorealistic studio product shot with a nine-second duration intent.

ENTITIES AND SET
Exactly one clear, colorless cylindrical glass pump bottle stands upright on matte warm-gray stone, left of center. It is completely unbranded: no label, logo, engraving, lettering, or numbers. It contains clear viscous serum and has one matte-black pump. The spout points frame-right. Exactly one fresh green leaf lies on the stone directly beneath the spout tip, right of center. Exactly one clean bare adult hand may appear, with no jewelry or nail decoration; no face, person, or second hand.

FIRST FRAME / CAMERA / LIGHT
At 0.0 s, the bottle and dry leaf are motionless and the hand is outside frame. Locked tripod three-quarter product close-up from slightly above, 85 mm macro feel, with the bottle, pump, nozzle, falling path, and leaf all sharp. One continuous take. No cut, pan, tilt, zoom, dolly, shake, or focus rack. Soft diffused key light from upper-left, gentle frontal fill, thin rim through the glass, controlled non-mirror reflections, plain neutral background.

SEMANTIC PACING
0.0–1.5 s: Static establishing hold.
1.5–3.0 s: One hand enters from frame-top. One index finger settles on the pump without depressing it.
3.0–4.0 s: The finger drives the pump vertically downward in exactly one slow continuous stroke to its mechanical stop, then holds it fully depressed. The bottle remains planted without sliding, rotating, or tipping.
4.0–5.2 s: That single press produces exactly one cohesive drop at the nozzle. The drop detaches, falls under gravity along an unobstructed path, and lands once near the center of the leaf. Surface tension keeps it as one glossy bead. No stream, spray, mist, splash, satellite droplets, bounce, or second emission.
5.2–6.4 s: The finger lifts once, the pump returns to rest once, and the hand exits through frame-top without touching the bottle or leaf. There is no second downstroke.
6.4–9.0 s: Completely static, cut-ready final hero hold.

AUDIO, TEXT, AND END STATE
Silent: no dialogue, voice-over, ambience, music, or sound effects. No captions, subtitles, logos, labels, letters, numbers, watermarks, embossed marks, or UI. No reflected duplicate bottle, extra leaf, extra hand, additional pump action, extra liquid, liquid on the stone, or morphing.

The final frame contains exactly one upright unbranded bottle and exactly one leaf bearing exactly one intact clear bead. The pump is at rest, the hand is fully outside frame, and nothing moves.
```

Exact platform-neutral JSON—valid JSON, but intentionally not an endpoint request:

```json
{
  "schema": "platform-neutral-shot-manifest",
  "submission_ready": false,
  "blocking_decision": "platform_and_surface",
  "task": "generate",
  "input_mode": "text_to_video",
  "platform": null,
  "model": {
    "display_name": "Seedance 2.5",
    "model_id": null
  },
  "prompt": "Generate one continuous photorealistic studio product shot with a nine-second duration intent. Exactly one clear, colorless cylindrical glass pump bottle stands upright on matte warm-gray stone, left of center. It is completely unbranded: no label, logo, engraving, lettering, or numbers. It contains clear viscous serum and has one matte-black pump. The spout points frame-right. Exactly one fresh green leaf lies directly beneath the spout tip, right of center. Exactly one clean bare adult hand may appear; no face, person, or second hand. At 0.0 s the bottle and dry leaf are motionless and the hand is outside frame. Use a locked tripod three-quarter product close-up from slightly above, 85 mm macro feel, keeping the bottle, pump, nozzle, falling path, and leaf sharp. One continuous take with no camera movement, cut, or focus rack. 0.0–1.5 s: static hold. 1.5–3.0 s: one hand enters from frame-top and one index finger settles on the pump. 3.0–4.0 s: the finger makes exactly one slow complete downward stroke and holds the pump fully depressed; the bottle does not move. 4.0–5.2 s: exactly one cohesive clear drop forms, detaches, falls under gravity, and lands once near the center of the leaf, remaining as one glossy bead. No stream, spray, mist, splash, satellite droplets, bounce, or second emission. 5.2–6.4 s: the finger lifts once, the pump returns to rest once, and the hand exits without touching the bottle or leaf. 6.4–9.0 s: completely static final hero hold. Silent. No text, branding, UI, duplicate reflections, extra objects, extra pump actions, extra liquid, morphing, or camera movement. Final frame: exactly one upright unbranded bottle and exactly one leaf with exactly one intact clear bead; no hand and no text.",
  "references": {
    "active_images": [],
    "active_image_count": 0,
    "official_model_announcement_max_images": 30,
    "selected_runtime_limit": null
  },
  "requested_delivery": {
    "duration_seconds": 9,
    "aspect_ratio": null,
    "resolution_label": "4K",
    "seed": 42,
    "audio_intent": "silent",
    "text_in_frame": false
  },
  "runtime_validation": {
    "exact_nine_second_output": "unverified",
    "resolution_4k_supported": "unverified",
    "seed_parameter_supported": "unverified_for_selected_runtime",
    "seed_determinism_guaranteed": false,
    "separate_negative_prompt_field_supported": "unverified_and_intentionally_omitted",
    "fixed_cost_usd": null,
    "first_pass_success_guaranteed": false
  }
}
```

## Acceptance checks

- Delivered duration is 9.0 seconds.
- Exactly one bottle and one leaf appear; at most one hand appears during the action.
- One complete pump downstroke occurs—never two.
- Exactly one cohesive drop leaves the nozzle and lands once on the sole leaf.
- Bottle remains stationary; no spray, splash, extra drops, or duplicate reflection.
- Camera remains locked; contact, trajectory, and landing stay visible and sharp.
- Zero active references, since none were supplied.
- Video is silent and contains no text or branding.
- Final 2.6 seconds hold bottle, leaf, and one bead with no hand.

## Failure risks

- Fine finger contact may produce malformed anatomy or an unintended second press.
- Pump output may become a stream, split, or miss the leaf.
- Glass reflections may resemble another bottle; random pseudo-branding may appear.
- Timecoded beats are pacing instructions, not frame-accurate controls.
- Platform-added watermarks and runtime delivery settings remain outside prompt control.

## Revision ladder

1. If the press repeats, change only the hand’s start state: begin with the finger already hovering above the pump. Keep all other variables fixed.
2. If the drop splits or misses, change only the nozzle-to-leaf gap to an explicit short vertical distance. Keep camera, timing, bottle, and hand motion fixed.
3. If the final hold drifts, change only temporal allocation by finishing the action earlier and lengthening the static hold.
4. If the same press/drop defect survives the first two isolated tests, stop retrying and route the drop to a separate insert or controlled compositing pass.

Blocking question: Which platform or API surface should the submission JSON target?
