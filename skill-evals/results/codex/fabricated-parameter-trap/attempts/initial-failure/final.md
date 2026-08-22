## Input basis

I selected BytePlus LAS so the JSON can target a real endpoint: `dreamina-seedance-2-5-260628`. The operator was released August 14, 2026. [BytePlus release notes](https://docs.byteplus.com/en/docs/Byteplus_LAS/las_release_notes)

Verified against the official documentation on August 22, 2026:

- Seedance 2.5 accepts 9-second generation and 1–30 reference images.
- Its documented LAS output is 480p or 720p—not 4K.
- No `negative_prompt` request field is documented, so exclusions belong in the prompt.
- The official example uses `"seed": 42`, but deterministic repeatability is not guaranteed.
- A 9-second 720p generation without input video is approximately `$0.303 × 9 × 1.525 = $4.158675`, not a fixed $0.10; actual billing controls.
- First-pass success cannot be guaranteed, especially for hand contact and liquid physics. [BytePlus LAS documentation](https://docs.byteplus.com/en/docs/byteplus_las/video_gen_enhanced), [official Seedance 2.5 launch](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)

Input mode is therefore text-to-video with zero references. Twelve references are allowed, but no images or roles were supplied; invented placeholder references would not be runnable. No generation was submitted.

## Final prompt

```text
Generate one continuous 9-second photorealistic premium skincare product shot, 16:9, silent.

EXACT ENTITIES AND LAYOUT
Exactly one clear cylindrical unbranded glass pump bottle containing transparent viscous serum stands upright on a matte warm-gray stone slab, slightly left of center. Its matte-white pump nozzle points frame-right above exactly one fresh green leaf lying flat on the stone in the right foreground. No other bottles, containers, leaves, products, or props.

CAMERA AND LIGHT
Locked tripod macro product shot at bottle height, straight-on three-quarter view. Keep the complete bottle and complete leaf visible and sharp throughout. No cuts, zoom, pan, tilt, rack focus, or shake. Soft diffused daylight from upper-left creates a controlled edge highlight on the glass and a small highlight on the serum. Stable neutral color grade with no lighting change.

ACTION
0.0-2.0s: Hold the clean static hero composition. No hand is visible.
2.0-3.4s: Exactly one adult hand with clean natural nails and no jewelry enters slowly from the top of frame. Only its index fingertip contacts the pump actuator.
3.4-4.8s: The index finger pushes the actuator vertically downward once to full compression, then releases it once. The spring returns the pump to its original height. This is exactly one complete pump cycle, with no bounce or second press. At the end of this single press, exactly one cohesive clear serum drop forms at the nozzle.
4.8-6.2s: The one drop detaches once and falls under gravity directly onto the center vein of the leaf. It remains intact and beads on the upper surface through surface tension. The leaf flexes subtly once at impact and settles. The hand exits completely upward.
6.2-9.0s: Hold a clean, motionless final hero frame showing the one bottle frame-left and the one leaf frame-right with the single serum bead visible.

CONSTRAINTS
Exactly one bottle, one leaf, one hand, one pump cycle, and one visible drop. No liquid stream, spray, splash, satellite droplets, spill, missed drop, or second drop. No logo, label, lettering, symbols, subtitles, watermark, border, UI, or end card anywhere. Glass highlights must not resemble a duplicate bottle. No audio.
```

Exact BytePlus LAS request body:

```json
{
  "model": "dreamina-seedance-2-5-260628",
  "content": [
    {
      "type": "text",
      "text": "Generate one continuous 9-second photorealistic premium skincare product shot, 16:9, silent. Exactly one clear cylindrical unbranded glass pump bottle containing transparent viscous serum stands upright on a matte warm-gray stone slab, slightly left of center. Its matte-white pump nozzle points frame-right above exactly one fresh green leaf lying flat on the stone in the right foreground. No other bottles, containers, leaves, products, or props. Use a locked tripod macro product shot at bottle height, straight-on three-quarter view. Keep the complete bottle and complete leaf visible and sharp throughout. No cuts, zoom, pan, tilt, rack focus, or shake. Soft diffused daylight from upper-left creates controlled highlights; maintain a stable neutral grade. 0.0-2.0s: hold the clean static hero composition with no hand visible. 2.0-3.4s: exactly one adult hand with clean natural nails and no jewelry enters slowly from the top; only its index fingertip contacts the actuator. 3.4-4.8s: the finger pushes the actuator vertically downward once to full compression, then releases it once; the spring returns it to its original height with no bounce or second press. Exactly one cohesive clear serum drop forms at the nozzle. 4.8-6.2s: the one drop detaches once, falls under gravity directly onto the center vein of the leaf, remains intact, and beads through surface tension; the leaf flexes subtly once and settles while the hand exits completely upward. 6.2-9.0s: hold a clean motionless final hero frame showing the one bottle frame-left and the one leaf frame-right with the single serum bead visible. Exactly one bottle, one leaf, one hand, one pump cycle, and one visible drop. No stream, spray, splash, satellite droplets, spill, missed drop, second drop, logo, label, lettering, symbols, subtitles, watermark, border, UI, end card, duplicate-looking reflections, or audio."
    }
  ],
  "generate_audio": false,
  "seed": 42,
  "resolution": "720p",
  "ratio": "16:9",
  "duration": 9,
  "return_last_frame": true,
  "watermark": false
}
```

## Acceptance checks

- Exactly one bottle and one leaf remain visible throughout.
- Exactly one hand performs one downward press and one release.
- Exactly one intact drop leaves the nozzle and lands on the leaf.
- Bottle, nozzle, leaf and landing point maintain consistent geometry.
- Camera remains locked in one continuous take.
- Hand is absent during the 6.2–9.0-second final hold.
- Final frame contains the bottle, leaf and one bead—no text or branding.
- No references are active; audio is absent.

## Failure risks

- Fine finger–pump contact may deform or produce a second press.
- The model may render a stream, split droplet or inaccurate landing.
- Glass reflections can resemble duplicates or create label-like artifacts.
- Prompt timestamps guide pacing but are not frame-accurate guarantees.

## Revision ladder

1. If the action is rushed, change only the timing allocation to give the press and fall more time; keep every other prompt and runtime value fixed.
2. If nozzle-to-leaf geometry fails, add only one approved first-frame image defining that layout; keep duration, action, camera and lighting fixed.
3. If single-drop physics still fails, stop generation retries and composite a controlled droplet element into the approved bottle-and-hand plate.

A genuine 12-reference request requires the 12 actual images or URLs and each image’s intended role.