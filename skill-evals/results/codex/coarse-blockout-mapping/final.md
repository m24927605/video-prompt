平台／模型、片長、畫幅皆未指定，因此以下採平台中立的自然語言格式，不加入任何執行參數。音訊預設為無對白、無配樂、無字幕。

### 單一 clip prompt

```text
Generate one finished clip using the four uploaded references. The clip may contain the internal cuts defined by @Video 1, but it must remain one coherent clip with one primary event: the messenger delivers the only letter to the centre of the table.

REFERENCE MAPPING

@Video 1 is a coarse blockout for the entire clip. Map the red proxy character to the messenger defined by @Image 1, and map the blue proxy character to the guard defined by @Image 2. Inherit from @Video 1 only the character paths, blocking, spatial relationships, relative character and environment scale, camera positions, camera movement, shot order, cut placement, and cut rhythm. Do not inherit its grey materials, primitive model appearance, original proxy geometry, guide lines, coordinate axes, camera cone, viewport background, interface elements, or production overlays.

@Image 1 defines the messenger’s appearance throughout the clip: face, hair, body proportions, visible wardrobe, footwear, and accessories. Do not inherit its pose, action, background, composition, crop, camera, or lighting.

@Image 2 defines the guard’s appearance throughout the clip: face, hair, body proportions, visible wardrobe, footwear, and accessories. Do not inherit its pose, action, background, composition, crop, camera, or lighting.

@Image 3 is the sole visual reference for the finished stone gate, the market’s visible materials and surface character, and the dusk illumination. Do not inherit people, character appearance, composition, camera, blocking, action, relative scale, or unrelated scene content from @Image 3.

ENTITIES AND ACTION

Show exactly two people: one messenger and one guard. Show exactly one physical letter for the entire clip. At the messenger’s first visible appearance, the messenger already carries that single letter in one hand. No duplicate letters appear before, during, or after the delivery.

Follow the red proxy’s route from @Video 1 precisely: the messenger passes physically through the finished stone gate, continues along the inherited path toward the visitor side of the table, and stops according to the blockout. The guard occupies the blue proxy’s position and remains behind the table for the entire clip, never walking around it and never exchanging positions with the messenger.

At the delivery beat, the messenger places the letter flat against the tabletop and gives it one controlled forward slide toward the exact centre of the table. The letter remains in continuous contact with the tabletop, glides in the push direction, slows naturally from surface friction, and comes to a complete stop at the tabletop’s centre. The messenger releases it cleanly. The guard may track the moving letter with their eyes but does not reach for it, touch it, or leave the space behind the table.

CAMERA, EDITING, AND SCALE

Reproduce the camera positions, camera height and side, movement direction and extent, shot progression, cut timing, and overall cut cadence of @Video 1. Preserve the blockout’s relative scale among both characters, the stone gate, the table, and the surrounding market. Replace every viewport-like element with the finished market environment; the camera must photograph only the final world and never reveal guide graphics or production geometry.

LOOK AND SOUND

Render the stone gate, market surfaces, material response, and dusk light exclusively from @Image 3. Keep this lighting and material language coherent across every internal cut. Preserve the natural appearance of both referenced characters under that dusk light.

Use only restrained diegetic sound: footsteps, subtle clothing movement, distant market ambience, and the brief dry sound of the letter sliding across the tabletop. No dialogue, narration, music, subtitles, captions, or visible interface text.

END STATE

End on the corresponding final camera state and blocking from @Video 1. The messenger remains on the visitor side of the table, the guard remains behind the table, and the single letter lies flat and motionless at the exact centre of the tabletop. Exactly two people and exactly one letter remain visible or narratively present.
```

驗收重點：紅／藍角色映射不可互換；守衛全程不離開桌後；信只能有一封；信的最終位置必須是桌面中央；攝影機與 cuts 只承接 @Video 1；材質與黃昏光只承接 @Image 3。
