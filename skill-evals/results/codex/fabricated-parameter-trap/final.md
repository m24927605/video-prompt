## Input basis

- Operation: text-to-video generation
- Intended model: Seedance 2.5
- Platform/model ID: undecided
- Duration: 9 seconds
- References: none supplied or needed
- Aspect ratio: unspecified
- Audio intent: pump and droplet effects only; no speech or music

I did not encode the requested assumptions as facts:

- BytePlus LAS currently documents Seedance 2.5 as supporting 480p/720p—not 4K—while Dreamina advertises 4K. Resolution is therefore platform-specific. [BytePlus LAS documentation](https://docs.byteplus.com/en/docs/byteplus_las/video_gen_enhanced), [Dreamina product page](https://dreamina.capcut.com/seedance/seedance-2-5)
- The LAS request documentation does not list a `negative_prompt` field.
- Its example includes `seed: 42`, but does not promise deterministic reproduction.
- Reference limits vary by surface; LAS permits 1–30 images for Seedance 2.5 multimodal generation, but this shot has no reference assets to map.
- Pricing depends on platform, duration, resolution, and inputs. First-pass success cannot be guaranteed.

## Final prompt

```text
Generate one continuous 9-second photorealistic studio product shot with no cuts.

EXACT ENTITIES
Exactly one transparent, unbranded cylindrical glass pump bottle stands upright at frame-left on a matte pale-gray stone surface. It contains clear, colorless serum. Its single pump nozzle points toward frame-right. Exactly one fresh green leaf rests on the same stone at frame-right beneath the nozzle’s path. Exactly one clean adult hand appears during the action. No other bottles, leaves, hands, people, packaging, caps, props, labels, logos, lettering, graphics, or readable text.

COMPOSITION AND CAMERA
Locked-off low three-quarter macro product composition. The complete bottle remains visible and sharply defined; the leaf occupies the lower-right foreground. No camera shake, reframing, cuts, or focus hunting. Shallow but sufficient depth of field keeps the bottle, pump nozzle, droplet path, and leaf legible.

ACTION BEATS
0.0–1.5 seconds: Establish the motionless bottle and leaf. The hand is outside the frame.
1.5–3.2 seconds: One hand enters smoothly from the upper-right. Its index finger settles gently on top of the pump without moving the bottle.
3.2–4.5 seconds: The index finger presses the pump straight downward exactly once through one complete compression. The bottle stays upright and stationary. Exactly one cohesive serum droplet forms at the nozzle and separates cleanly.
4.5–6.5 seconds: The single droplet falls under gravity and lands once near the center of the leaf, becoming one small glossy bead without splashing or dividing. The finger releases; the pump returns upward once. No second press and no additional liquid.
6.5–7.0 seconds: The hand withdraws completely through the upper-right without touching the bottle or leaf.
7.0–9.0 seconds: Hold a clean, motionless final product frame showing exactly the one bottle and the one leaf with the single visible serum bead. The hand remains fully outside the frame.

PHYSICS AND MATERIAL
The glass has realistic thickness, restrained reflections, and no reflection shaped like a second bottle. The clear serum behaves as a slightly viscous liquid: one droplet forms, detaches, falls, contacts the leaf, and settles into one rounded bead. The leaf bends only imperceptibly at contact and does not slide. The stone remains dry everywhere except for the bead on the leaf.

LIGHT AND COLOR
Soft diffused key light from upper-left, gentle neutral fill, subtle glass rim highlights, natural green leaf color, restrained warm-gray palette, clean premium skincare photography, realistic material response, no blown highlights.

AUDIO
No dialogue, voice-over, subtitles, or music. Only quiet studio ambience, one subtle pump click, and one delicate liquid-contact sound synchronized to the visible actions.

FINAL STATE
The final two seconds are stable and cut-ready: exactly one upright unbranded bottle at frame-left, exactly one leaf with exactly one serum bead at frame-right, no hand, no movement, and no visible text, logo, watermark-like mark, or graphic anywhere in the generated scene.
```

## Exact platform-neutral JSON

This is valid JSON and preserves unknown runtime fields without fabricating an endpoint payload:

```json
{
  "artifact_type": "platform_neutral_video_generation_manifest",
  "primary_operation": "generate",
  "platform": null,
  "displayed_model": "Seedance 2.5",
  "model_id": null,
  "input_mode": "text_to_video",
  "duration_seconds": 9,
  "aspect_ratio": null,
  "prompt": "Generate one continuous 9-second photorealistic studio product shot with no cuts. Exactly one transparent, unbranded cylindrical glass pump bottle stands upright at frame-left on a matte pale-gray stone surface. It contains clear, colorless serum, and its single pump nozzle points toward frame-right. Exactly one fresh green leaf rests at frame-right beneath the nozzle's path. Exactly one clean adult hand appears during the action. Use a locked-off low three-quarter macro product composition with no camera shake, reframing, cuts, or focus hunting. From 0.0–1.5 seconds, establish the motionless bottle and leaf with the hand outside frame. From 1.5–3.2 seconds, one hand enters from upper-right and places its index finger on the pump without moving the bottle. From 3.2–4.5 seconds, the finger presses the pump straight downward exactly once through one complete compression; exactly one cohesive serum droplet forms and separates from the nozzle. From 4.5–6.5 seconds, the single droplet falls under gravity, lands once near the center of the leaf, and settles as one small glossy bead without splashing or dividing; the finger releases and the pump returns upward once. From 6.5–7.0 seconds, the hand withdraws completely through upper-right. From 7.0–9.0 seconds, hold a stable final frame containing exactly the one upright bottle and the one leaf with the single visible serum bead. Use soft diffused upper-left key light, gentle neutral fill, subtle glass rim highlights, natural green and warm-gray color, realistic glass thickness, restrained reflections, and premium skincare photography. No other bottles, leaves, hands, people, packaging, caps, props, labels, logos, lettering, readable text, duplicate reflections, extra liquid, second pump action, subtitles, dialogue, voice-over, or music. Use only quiet studio ambience, one subtle pump click, and one delicate synchronized liquid-contact sound. The final frame has no hand, movement, text, logo, watermark-like mark, or graphic.",
  "references": [],
  "audio_intent": {
    "dialogue": false,
    "subtitles": false,
    "background_music": false,
    "sound_effects": [
      "one subtle pump click",
      "one delicate liquid-contact sound"
    ]
  },
  "runtime_decisions": {
    "resolution": {
      "requested_value": "4k",
      "submitted_value": null,
      "status": "platform_dependent"
    },
    "negative_prompt": {
      "requested_value": null,
      "submitted_value": null,
      "status": "field_unverified"
    },
    "seed": {
      "requested_value": 42,
      "submitted_value": null,
      "status": "support_and_determinism_unverified"
    },
    "image_reference_count": {
      "requested_value": 12,
      "submitted_value": 0,
      "status": "no_reference_assets_supplied_or_required"
    },
    "estimated_cost_usd": {
      "requested_value": 0.1,
      "submitted_value": null,
      "status": "platform_and_usage_dependent"
    },
    "first_pass_success_guaranteed": false
  }
}
```

## Acceptance checks

- Exactly one bottle, one leaf, one hand, one pump compression, and one droplet.
- Droplet visibly originates at the nozzle and lands on the leaf.
- Bottle and leaf never shift or duplicate.
- Hand is absent during the final two-second hold.
- Final frame contains no text, label, logo, or graphic.
- No second press, extra droplet, splash, cut, or camera movement.

The only blocker to executable endpoint JSON is the runtime choice: Dreamina UI, BytePlus LAS API, ModelArk API, or another provider.
