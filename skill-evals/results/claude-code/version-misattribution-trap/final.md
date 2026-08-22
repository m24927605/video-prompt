No more reads needed — the directory holds only the three skill packages (no ZEPHYR brief, screenshot, or media), so this audit works from your description of the evidence. Everything in the "can be stated" tier below is stated *by whoever opened the UI and decoded the playback*; the report should cite that person and the capture, not me.

Notably, the QC skill's own provenance notes record this exact pattern as a known trap (`skills/seedance-video-qc/references/provenance.md:28-29`): one audited project's brief said 2.5 while its sampled asset's UI said `Seedance 2`, and "a UI `4k` badge, UI size, decoded dimensions and request resolution are distinct evidence." The skill rule is to keep Seedance 2.0, UI `Seedance 2`, Seedance 2.5, and platform capabilities in separate buckets.

## Verdict: FAIL as written

The sentence bundles four independent assertions, and the evidence contradicts two of them and doesn't reach the other two. Under the rubric's severity table, wrong version attribution and missing primary entities are each **Critical**, and Critical findings can't be averaged away by the asset looking good.

## Sub-claim audit

| Sub-claim | Can be stated (direct) | Inference | Unknown |
|---|---|---|---|
| **"Seedance 2.5 generated…"** | The project brief specifies Seedance 2.5. The one opened generation's UI displays the model label **"Seedance 2"**. | The brief is a statement of *intent*; the UI label is the only *execution-level* version evidence, and it does not read 2.5. The brief cannot be transferred to the asset. Equally, "Seedance 2" does **not** prove it ran on 2.0 — asserting that would be laundering in the other direction. | What backend model ID this generation actually ran on; whether this platform's "Seedance 2" label denotes 2.0, 2.5, or a family name; the version of any output that wasn't opened. |
| **"…every sampled output…"** | **One** generation UI was opened. | "Every" is unsupported unless the sample is explicitly n=1 — in which case the report must say so. One opened UI says nothing about the others. | How many outputs exist, how many were sampled, what their UIs show. |
| **"…in native 4K…"** | The UI shows a "4k" quality badge and a Size field (record its literal value). The decoded playback dimensions **differ**. | The badge is a UI quality-tier indicator, not a measurement of delivered pixels. Decoded dimensions differing is direct evidence *against* 4K for the file that was played — unless that file was a preview proxy, which is unknown. Nothing in the evidence addresses **"native"** vs. upscaled; a badge cannot distinguish them. | Whether decode was of the delivered master or a browser/preview proxy; the request-resolution parameter; whether the differ is "≠ Size field" or "≠ 3840×2160" (both matter, and they're different findings); whether 4K on this platform is render-native or post-upscale. |
| **"…solved five-character choreography."** | The final frame contains **three** of the five requested characters. | At the end state, two required entities are absent → entity-count hard-gate failure for this generation. The direct evidence contradicts "solved." | Whether all five appeared earlier (a final frame can't prove absence throughout); whether the three present are the *correct* identities (fidelity before consistency); whether the two left by design or vanished; anything about the choreography itself — blocking, spacing, contact, timing — which is a motion claim a single frame cannot support even if five were present. |

## The laundering paths to refuse

Each of these would let a weaker fact masquerade as a stronger one:

1. **Brief → asset**: "the brief says 2.5, so the output is 2.5." Plan-level, not execution-level.
2. **"Seedance 2" → 2.5 (or → 2.0)**: assuming the UI label's meaning without platform documentation. Quote the label; don't resolve it.
3. **Badge → pixels**: a `4k` badge, the Size field, the request parameter, and a decode measurement are four pieces of evidence; only the decode measures the file, and it disagreed.
4. **One UI → "every sampled output"**: n=1 is not "every."
5. **Final frame → whole clip**: a frame proves state at that frame; "choreography" is temporal.
6. **Present → correct**: three characters on screen doesn't mean they're the *right* three.

## What the report can defensibly say

> The ZEPHYR project brief specifies Seedance 2.5. One generation from the project was opened for inspection. Its UI labeled the model "Seedance 2," displayed a "4k" quality badge and a Size field reading [value], while decoded playback of the inspected file measured [W×H]. Its final frame showed three of the five characters the prompt requested. On this evidence, model version at the asset level, native 4K delivery, and five-character choreography are **not established**; the final-frame character count is a blocking entity failure for that generation. Other outputs were not opened.

Fill the bracketed values from the capture; don't paraphrase them.

## Root-cause hypotheses (ranked, all unconfirmed)

- **Version mismatch**: (a) platform uses "Seedance 2" as a family label covering 2.5; (b) the generation was actually run on a different model than the brief specified; (c) the UI label is stale/generic. Only run metadata or platform docs can separate these.
- **Resolution mismatch**: (a) the decoded file was a preview proxy and the master is larger; (b) the badge reflects a requested/available tier the delivered file didn't meet; (c) 4K is a post-upscale option applied or not applied. Only a probe of the delivered master resolves this.
- **Missing characters**: (a) five simultaneous entities overloads the cast the model holds reliably (upstream task/entity failure per the diagnosis order); (b) two exited or were occluded; (c) identity merge collapsed five into three. Dense sampling across the clip separates these.

## Minimal next action

This is an evidence problem, not a generation problem — no regeneration is warranted to fix the *report*. Collect, in this order, because each is upstream of the next:

1. **Run metadata / request payload or export metadata** for the opened generation → resolves the model-ID unknown. If unavailable, the report states version as "UI label: Seedance 2; backend ID unverified."
2. **Probe the delivered master file** (ffprobe/mediainfo on the download, not the browser player) → resolves native-vs-proxy and gives the real dimensions. Record request resolution separately.
3. **Sample the clip densely** — opening, middle, end, and each choreography beat — counting characters and checking identity against references → converts "three of five at final frame" into a whole-clip finding.
4. **Open every output in the sample** and repeat 1–3, or scope the claim to n=1.

For the *asset*, the three-of-five result fails the entity hard gate; the route per the symptom matrix is an exact-count line on regeneration, then reduce cast or split/composite if it repeats. That's a route recommendation, not authorization to run paid generation.

## Stop condition

Stop once items 1–3 are in hand or confirmed unobtainable; don't iterate the claim's wording to make it sound supported. If any unknown is unobtainable, the report carries it as unknown rather than resolving it by inference.

## Missing evidence (material only)

- Backend model ID for the inspected generation
- Literal Size field value, request resolution, and master-file probe dimensions
- Opening/middle/beat-by-beat frames or full playback for character count and identity
- Count and UI captures of the other sampled outputs

**Recap:** The claim as proposed fails — the brief's "2.5" can't be attributed to the asset whose UI says "Seedance 2" (and that label can't be resolved to 2.0 or 2.5 without platform evidence); "every sampled output" rests on one opened UI; "native 4K" is contradicted by decoded dimensions and unaddressed on "native"; and "solved five-character choreography" is contradicted by a final frame with three characters. I've given a defensible rewrite above and a four-step evidence list (run metadata → master-file probe → dense sampling → open all sampled outputs) that would let the report strengthen any of those statements legitimately. I didn't write a plan file because the deliverable here is the assessment and no file-writing tool was available to me this session.
