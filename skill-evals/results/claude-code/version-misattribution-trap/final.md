No ZEPHYR project files exist in this workspace — only the skill definitions — so this audit rests entirely on the evidence as you described it. That's enough to rule on the claim, because the claim fails on its own stated evidence. Here is the audit.

## Verdict

**FAIL — the claim cannot be published as written.** Scope of evidence: one project brief, one opened generation UI, decoded playback dimensions for that one asset, and its final frame. Every load-bearing word in the claim ("proves," "Seedance 2.5," "every sampled output," "native 4K," "solved five-character choreography") either exceeds this evidence or is contradicted by it. Wrong version attribution and fabricated capability claims are **Critical** severity under the QC rubric — they cannot be averaged away by anything else the project did well.

## What can be stated (direct observation)

These four sentences are the entire defensible factual core:

1. The project **brief** specifies Seedance 2.5. A brief is a statement of intent, not generation evidence.
2. The **one** opened generation's UI displays the label "Seedance 2," a "4k" quality badge, and a Size field.
3. That asset's decoded playback dimensions differ from 4K.
4. That asset's final frame shows three of the five requested characters.

## Where the claim launders evidence

**Version.** The claim performs exactly the substitution the QC provenance rules warn against: taking a project-level "2.5" from the brief and attributing it to asset-level outputs. The only asset-level version evidence available says "Seedance 2," which *contradicts* rather than supports the brief. A UI label is also not a backend model ID — whether "Seedance 2" is a family label that could include 2.5, or a distinct model, is a platform-mapping question the screenshot cannot answer. So the honest statement is: the brief and the one inspected asset disagree, and the true backend version is **unknown**.

**"Every sampled output."** One generation was opened. The version, resolution, and content of every other output are unknown. A sample of one cannot support a universal claim even if it had passed.

**"Native 4K."** The 4k badge, the Size field, the decoded dimensions, and the request resolution are four distinct pieces of evidence, and here the only measured one (decoded dimensions) disagrees with 4K. Direct observation: playback decodes at non-4K dimensions. Inference (hypothesis only): the badge likely denotes a quality tier or upscale option rather than delivered resolution. Unknown: the Size field's actual value, whether the source file contains 4K frames that the player downscaled, and — critically — whether any 4K output is *native* render versus post-upscale. "Native" is unprovable from UI evidence alone; it requires pipeline metadata.

**"Solved five-character choreography."** Direct observation: at the final frame, only three of five characters are present — a hard-gate entity-count failure at that frame. Inference: the choreography contract was likely not fully met. Unknown: whether the other two characters appear at earlier timecodes (a single frame cannot prove absence throughout), and the choreography quality of any interval, since no motion evidence was inspected. Note the asymmetry: the frame is insufficient to prove total failure, but the claim asserts *success*, and the only frame in evidence is evidence against it.

**"Proves."** Nothing here reaches proof. The evidence is one screenshot-level inspection with an internal contradiction on version and a measured contradiction on resolution.

## Publishable replacement wording

> The project brief specifies Seedance 2.5. Of the sampled outputs, one generation was opened for inspection: its UI is labeled "Seedance 2" with a 4k quality badge, its decoded playback dimensions are [W×H, non-4K], and its final frame shows three of the five briefed characters. Backend model version, delivered-resolution provenance (native vs. upscaled), and full-clip character coverage remain unverified.

## Minimal next actions to resolve the unknowns

Each resolves one material gap; none require regeneration:

- Pull the asset's **generation metadata or API/request log** for the backend model ID — the only evidence that can settle 2 vs. 2.5.
- Run **ffprobe/mediainfo** on the delivered file for coded dimensions, settling whether the file itself is 4K or only badged 4K.
- **Scrub the full clip** (opening, middle, transitions) for the two missing characters before ruling on the choreography beat.
- Open the remaining sampled generations' UIs before any "every sampled output" language is used, or scope the report to the one inspected asset.

Stop condition: if backend logs and file metadata are unavailable, the report ships with the bounded wording above and the unknowns stated explicitly — absence of metadata is not license to fall back to the brief's claim.
