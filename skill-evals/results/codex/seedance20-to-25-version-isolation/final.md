The older Seedance 2.0 numeric mode, model ID, API field, and tag are intentionally excluded. With the current surface unknown, a valid Seedance 2.5 JSON request cannot be specified without inventing runtime facts.

### Platform-neutral prompt

```text
Generate one continuous clip at dawn outside a small neighborhood bakery.

Exactly one adult cyclist rides from frame-left toward frame-right along the curb. The bakery occupies the midground on frame-right: a modest storefront with a glass door and softly illuminated display window. Cool blue dawn light fills the quiet street, contrasting with the warm amber light inside the bakery. No other people or moving vehicles enter the scene.

Begin in a medium-wide three-quarter side view. The camera tracks smoothly alongside the cyclist at an unhurried pace, keeping the rider and bakery entrance clearly visible.

As the cyclist reaches the bakery, they stop pedaling and apply both brakes. The wheels decelerate naturally; the rider’s torso shifts slightly backward with the braking force. The bicycle rolls to a complete stop parallel to the curb beside the bakery entrance. The cyclist plants their left foot firmly on the pavement while the right foot remains on its pedal, keeps both hands on the handlebars, and turns their gaze toward the warmly lit display window.

The camera slows with the bicycle and settles into a stable composition. End with the cyclist and bicycle completely stationary beside the bakery, the planted foot bearing their weight, and their attention fixed on the window.

Naturalistic movement and believable bicycle balance. Preserve exactly one cyclist, one bicycle, and one bakery storefront. No cuts, collisions, duplicated limbs or wheels, sudden position changes, dialogue, captions, subtitles, logos, or added on-screen text.

Sound intent, if the selected runtime supports generated audio: quiet dawn ambience, faint birds, soft tire noise, a brief mechanical brake sound, and subtle bakery activity behind the glass. No music.
```

### Runtime facts still unknown

- Platform, UI, or API surface
- Exact Seedance 2.5 model ID
- Endpoint and request schema
- Operation/mode representation
- Prompt field name
- Supported tags
- Aspect ratio, duration, resolution, and frame-rate controls
- Audio controls and support

These must be verified for the selected surface before constructing JSON. The one blocking question is: **Which Seedance 2.5 platform or API endpoint will receive the request?**
