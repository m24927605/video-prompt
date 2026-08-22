# Seedance 2.5 Prompt Playbook

> 狀態：製作可用的文件導出版本；本研究未獲付費生成授權，所有自編範例均未送出模型。  
> 存取基準：2026-08-22（Asia/Taipei）。能力與參數必須在送出前重新核對所用平台的最新文件。

## 0. 證據標籤與版本 gate

本文使用五種標籤：`官方事實`、`專案直接觀察`、`團隊推論`、`實務建議`、`未知／待驗證`。沒有標籤的操作步驟皆屬 `實務建議`，不是模型保證。

### 0.1 名稱、發布、平台與 API

| 問題 | 2026-08-22 結論 | 證據與限制 |
|---|---|---|
| 正式名稱 | `官方事實`：ByteDance 正式名稱為 **Seedance 2.5**。 | ByteDance Seed 於 2026-07-31 明寫正式發布；見[發布文](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)與本機正文擷取 [archive: `sources/supplemental/bytedance-seedance-2.5-launch-2026-07-31.body.html`]。 |
| 發布狀態 | `官方事實`：不是僅有傳聞或未命名預覽；2026-07-31 已正式發布。 | 同上。官方同時承認複雜動作的物理合理性與極多主體互動穩定性仍有改善空間。 |
| 消費端平台 | `官方事實`：發布當日正在 Jimeng AI、Doubao Pro 等平台 rollout。 | 發布文只證明當日狀態，不代表所有地區／帳戶皆可用。 |
| BytePlus API | `官方事實`：發布文在 2026-07-31 尚寫「coming soon」；之後 BytePlus ModelArk 文件已提供啟用條件、教學與 API 呼叫，因此截至本研究日已有正式文件化存取路徑。 | 這是**時間差**，不是應混成單一同日事實。ModelArk 教學 first published 2026-08-07、updated 2026-08-18；見[官方教學](https://docs.byteplus.com/en/docs/ModelArk/2607688)與本機擷取 [archive: `sources/supplemental/byteplus-modelark-2607688-tutorial.extracted.md`]。實際帳戶仍受餘額／資源包／地區與啟用條件限制。 |
| API model ID | `官方事實`：BytePlus ModelArk／LAS 文件列出 `dreamina-seedance-2-5-260628`。 | [ModelArk 教學](https://docs.byteplus.com/en/docs/ModelArk/2607688)、[LAS 文件](https://docs.byteplus.com/en/docs/byteplus_las/video_gen_enhanced)與本機 LAS 擷取 [archive: `sources/supplemental/byteplus-las-video-gen-enhanced.extracted.md`]。 |
| 文件適用版本 | `官方事實`：本 playbook 的 2.5 專屬寫法以文件 ID `2607689`（prompt guide，updated 2026-08-13）、`2607688`（tutorial，updated 2026-08-18）及 API `1520757`（updated 2026-08-18）為準。 | [Prompt guide](https://docs.byteplus.com/en/docs/ModelArk/2607689)、使用者提供完整 Markdown [archive: `../../seedance2.5-prompt-guide.md`]、本機擷取 [archive: `sources/supplemental/byteplus-modelark-2607689-prompt-guide.extracted.md`]、[API 文件](https://docs.byteplus.com/en/docs/ModelArk/1520757)、本機 API 擷取 [archive: `sources/supplemental/byteplus-modelark-1520757-create-video.extracted.md`]。 |

### 0.2 平台能力不可互換

`官方事實`：相同 model ID 在不同 BytePlus 產品表面仍有不同輸出規格。ModelArk 2.5 教學列 480p、720p、1080p，且 1080p 為 10-bit H.265/HEVC；LAS Enhanced operator 文件只列 480p、720p、24 fps。故「Seedance 2.5 支援 1080p」必須寫成「**ModelArk 2.5 文件支援 1080p**」，不能外推至 LAS、Jimeng、Doubao 或 Higgsfield。

`未知／待驗證`：Higgsfield 的欄位、reference 上限、輸出規格、預設值與 API model ID，必須由該平台實際 UI／官方文件另證，不能套用 BytePlus 參數。

## 1. 把需求編譯成 prompt

### 1.1 先問八件事

在寫 prompt 前，至少取得以下資料；缺少者明標 `unknown`，不要自行填成「通常值」。

1. 交付目標：敘事片、廣告、動作、表演、VFX、教學或 edit／extend。
2. 平台與模型：ModelArk、LAS 或其他平台；畫面規格與可見參數。
3. 觀眾與時長：預定總長、這一鏡的 duration、畫幅、是否需要聲音。
4. 主體：數量、身份、外觀、服裝、聲音、不可改變特徵。
5. 行為：起始狀態、動作階段、方向、速度、因果、終止狀態。
6. 場景：空間配置、時間、天候、光源、動態背景、必要道具。
7. 攝影與剪輯：景別、機位、運鏡、是否切鏡、轉場觸發、下一鏡 handoff。
8. 參考素材：每個檔案的上傳順序、合法來源、要參考／不要參考的屬性。

### 1.2 先路由 task，再寫文案

| Task | ModelArk 2.5 觸發／角色 | 必須遵守的參數 gate |
|---|---|---|
| Text-to-video | 只有 text | `ratio`、`duration` 可依需求；2.5 duration 為 4–30 秒或 `-1`。 |
| Reference-to-video | 至少一個 `reference_image`、`reference_video` 或 `reference_audio`；建議明設 `omni_reference_task_type: reference` | 不由素材鎖死 ratio／duration；仍須依平台支援值設定。 |
| Video editing | 至少一個 `reference_video`；prompt 要有 edit／add／remove／modify／replace 等明確意圖；建議 `omni_reference_task_type: edit` | ModelArk：`ratio: adaptive`、`duration: -1`；被編輯影片 4–30 秒。建議 input／output 都用 `mov`。 |
| Video extension | 至少一個 `reference_video`；prompt 要有 extend forward/backward／continue 等明確意圖；建議 `omni_reference_task_type: extend` | ModelArk：`ratio: adaptive`；duration 為欲新增的長度；建議 `mov`。 |
| First frame | 一張圖片 `role: first_frame` | `ratio: adaptive`；輸出畫幅跟首幀。 |
| First + last frame | 一張 `first_frame` 加一張 `last_frame` | `ratio: adaptive`；首尾幀應同畫幅，否則尾幀可能被拉伸。 |

`官方事實`：ModelArk 的 `omni_reference_task_type` 只是 task hint；prompt 意圖與 hint 不一致仍可能回 `InvalidParameter.TaskTypeMismatch`。所以不要用參數掩蓋含糊文案。

### 1.3 推薦組裝順序

官方基本公式為「subject + action/event + scene/environment + visual style + camera movement/shot cuts + sound」，並建議把 reference mapping、單句摘要、詳細 timeline／shot sequence、全局補充分開。據此使用下列生產 schema：

```text
[TASK]
一句話明示 generate / reference / edit / extend，以及只允許改什麼。

[ASSET BINDINGS]
@Image 1 = 角色 A 外觀（只參考臉、髮型、體型）
@Audio 1 = 角色 A 音色
@Video 1 = 只參考動作節奏與運鏡，不參考人物與場景

[ONE-SENTENCE INTENT]
主體 + 地點 + 事件 + 類型／風格 + 核心運鏡。

[GLOBAL INVARIANTS]
整鏡都不能變的角色、服裝、道具、場景方位、光線方向、色彩與聲音規則。

[TIMELINE / SHOTS]
0–Ns 或 Shot 1...；每段描述可見狀態、動作因果、攝影、對白／聲音與段末 handoff。

[AUDIO]
語言、說話者、逐句台詞、環境聲、動作聲、BGM；不需要者明寫 no subtitles / no BGM / no audio。

[FINAL FRAME / EDIT INTENT]
最後可見狀態、剪輯出口；edit 類重申其餘皆不變。
```

`實務建議`：若指令衝突，人工按「task 硬限制 → 素材映射 → 身份／continuity → 動作因果與時間 → 攝影 → 風格 → 裝飾」裁決後再送出。這是製作優先級，不是模型內建權重語法。

### 1.4 詳細度與時間

- `官方事實`：2.5 支援整秒 timestamp。以 1 秒為基本單位，區間要連續，不留 `0–3s` 後直接跳 `5–6s` 的空洞。
- `官方事實`：同一區間內容太少，模型可能較自由發揮；太多則可能增加切鏡或漏事件。不要要求「每秒搖頭三次」這類高頻微控。
- `實務建議／案例觀察`：timestamp 是 prompt 內的語意排程，不是 API `duration` 參數。兩者都要明寫，並對輸出重測 milestone drift；P02 抽查 prompt 的時間線到 25 秒，實際輸出為 29.056 秒，因此不得把文字時碼當成時長硬保證，也不能由輸出倒推當時的未顯示 `duration` 設定。
- `實務建議`：每一時間段只安排一個主要狀態變化、一個主要攝影意圖；高風險互動另拆鏡。
- `未知／待驗證`：官方未公布「最佳 prompt 字數」或保證性權重語法。不要把長度當品質代理指標。

### 1.5 Reference 素材規則

- `官方事實`：編號必須對應上傳順序，逐一說明每個素材負責什麼；不要只在圖片內寫「John」而在 prompt 未做綁定。
- `官方事實`：同一素材若只取部分屬性，要明寫，例如「只參考 @Video 1 的手部動作與 orbit camera，不參考人物外觀」。
- `官方事實`：素材本身已精確時，不要再用文字重述一遍而製造衝突。
- `官方事實`：上限不是甜蜜點。Prompt guide 建議 subject audio/video reference 以 1–5 主體、5–10 秒較穩；subject image 以 1–8 主體較穩；9–12 可嘗試但穩定性可能下降；多 panel storyboard 建議不超過 15 格；video edit 以 20 秒內較穩。這些是官方建議，不是硬限制。

### 1.6 否定控制不可虛構欄位

`官方事實`：2.5 prompt guide 明確示範 `No subtitles`、`No BGM; generate only environmental sounds and action sounds`、`No audio`。官方沒有在本文所據 ModelArk 文件中定義獨立 `negative_prompt` 欄位。因此：

- 在主 prompt 用自然語言寫必要的字幕／聲音否定條件。
- 其他「no flicker」「do not change identity」可作自由文字限制，官方範例亦使用，但不得稱為硬性 guarantee。
- 不建立不存在的 `negative_prompt` JSON，也不寫權重如 `(face:1.4)`。

### 1.7 A 文件的音訊／文字 prompt syntax

`官方事實`：指定來源 A 的 prompt 說明列出可選的行內標記：music 用 `(...)`、sound effects 用 `<...>`、dialogue 用 `{...}`、subtitles 用 `【...】`；非中文對白建議在台詞前寫語言／區域口音、說話者與語氣。[來源 A](https://bytedance.larkoffice.com/docx/A88jd0B47oAd8zxWp5ycZFMfnxh)

```text
(restrained cello motif)
<a metal latch clicks once>
{English, Irish accent, Mara, whispering: "Do not open it yet."}
【Three hours earlier】
```

邊界：

- 這些是 **prompt 內的可選 syntax**，不是 JSON parameters，也不是必填欄位。
- BytePlus tutorial／prompt guide 的官方範例也以雙引號標示 dialogue；兩種寫法並存。專案應選一套並保持一致，重點仍是 speaker、language、accent、tone、timing 與原文清楚。
- 標記可提高人類可讀性與角色／聲音區隔，但官方未保證逐字、逐音效或逐秒 deterministic adherence；成片仍需逐字與 lip-sync QC。

## 2. 可直接填寫的模板

### 2.1 一般生成／reference-to-video

```text
[Asset bindings]
@Image 1 = ...（只參考...）
@Video 1 = ...（只參考...；不參考...）

[Intent]
在[地點／時間]，[主體]完成[事件]；[視覺類型]，[核心攝影意圖]。

[Global invariants]
[身份、數量、服裝、道具、空間、光色、風格、聲音]

[Timeline]
0–Xs: [起始畫面 → 動作 → 結果；景別、機位、運鏡；聲音]
Xs–Ys: [...]

[End]
停在[可剪接的最後狀態]。[字幕／BGM 規則]
```

### 2.2 Edit

```text
Edit @Video 1. Only change [A] into [B] during [time range].
Preserve [composition, camera, performance timing, identities, untouched audio...] unchanged.
0–Xs: ...
Xs–Ys: ...
No other visual or audio changes.
```

### 2.3 Extend

```text
Extend @Video 1 forward by [N] seconds. Continue from its final image, motion direction,
lighting, character identity, environment, ambience, and audio level.
0–Xs of the extension: ...
...
End on [state] for the next cut. Do not replay the ending of @Video 1.
```

### 2.4 獨立 keyframes

```text
Use @Images 1 to N in order as keyframes.
[綁定每張的主體／場景意義]
[逐段說明兩 keyframes 之間合理的動作、運鏡、聲音與因果]
[全局身份、風格、光色與文字穩定規則]
```

## 3. ModelArk 2.5 參數檢核表

| 欄位 | 2.5 文件支持的用途 | 本 playbook 規則 |
|---|---|---|
| `model` | `dreamina-seedance-2-5-260628` | 每次 run 固定記錄完整 ID。 |
| `content[].role` | `first_frame`、`last_frame`、`reference_image`、`reference_video`、`reference_audio` | 角色由 task 決定；不要只靠 prompt 模擬 first frame。 |
| `omni_reference_task_type` | `auto`、`reference`、`edit`、`extend` | 已知 task 時明設；同時讓 prompt 使用對應動詞。 |
| `ratio` | 固定畫幅或 `adaptive`；edit／extend／first-frame 類受特殊限制 | 依 task gate；不可把其他平台值照搬。 |
| `duration` | 2.5 為 4–30 整秒或 `-1` | edit 必須 `-1`；其他依 shot budget。 |
| `resolution` | ModelArk 文件列 480p／720p／1080p | LAS 只列 480p／720p；platform-first。 |
| `output_format` | `mp4`、`mov` | editing／extension 建議 `mov`；一般 distribution 可用 `mp4`。 |
| `generate_audio` | boolean，預設 true；輸出音訊為 mono | 若後期要完全重做聲音可 false；否則明寫聲音設計。 |
| `return_last_frame` | 回傳 PNG 最後幀，文件示範可供下一段首幀 | 長片 handoff 建議 true，但仍要人工 QC 後才晉升 anchor。 |
| `watermark` | boolean | 依合規／交付要求，和畫質評測分層記錄。 |
| `seed` | ModelArk 2.5 支援整數 `[-1, 2147483647]`；`-1` 會換成隨機值 | 同 request + 同 seed 只保證「相似」，官方明寫不保證完全一致；未來評測同時做固定 seed 配對與多 seed 抽樣。 |
| `draft` | API 文件只列 Seedance 1.5 Pro | 不得把 draft mode 歸給 2.5。快速流程改用低風險 shot、較短 duration／較低平台允許 resolution 做 blocking，但是否省成本須實測。 |

## 4. 完整範例（全部未實測）

以下每案均為 **「文件導出的未實測範例」**，不是成功保證，也不是本專案生成觀察。

### 範例 01：T2V 單鏡自然動作

- **狀態**：文件導出的未實測範例。
- **意圖**：測低風險單主體、單動作與自然光。
- **輸入假設**：只有文字；8 秒；16:9；需要環境聲。
- **最終 prompt**：

```text
A quiet, realistic nature-film shot on a warm late afternoon. A red fox walks from the left edge of a mossy forest clearing toward a shallow stream, pauses, lowers its head, and drinks.

0–3s: Eye-level medium-wide shot. The fox enters from frame left at an unhurried pace; soft backlight outlines its fur. The camera remains mostly locked with a subtle handheld breathing motion.
3–6s: The fox reaches the stream, stops with all four paws visible, and lowers its head. Grass bends under its paws and a few insects drift through the backlight.
6–8s: Close medium shot without a cut. The fox laps the water, creating small concentric ripples, then briefly looks toward an off-screen sound at frame right.

Keep one fox with the same coat markings and body proportions throughout. Natural forest ambience, water and light paw sounds only. No BGM. No subtitles. End with the fox still beside the stream, looking frame right.
```

- **已證實參數**：ModelArk `model: dreamina-seedance-2-5-260628`、`duration: 8`、`ratio: 16:9`、`generate_audio: true`；resolution 依平台測試層級。
- **預期觀察點**：動作順序、四肢結構、飲水造成水面結果、毛色／體型是否漂移、環境聲是否克制。
- **失敗風險**：假飲水、腳掌滑行、look direction 不明、鏡頭自行切換。
- **修正版 A**：若動作漏失，刪除昆蟲與 handheld，只留「走到水邊 → 停 → 低頭飲水」。
- **修正版 B**：若水物理失真，拆成 0–5 秒走到水邊、5–8 秒只做低頭與第一圈漣漪。

### 範例 02：T2V 30 秒多鏡微敘事

- **狀態**：文件導出的未實測範例。
- **意圖**：測 2.5 文件宣稱的 30 秒、多段故事與轉折。
- **輸入假設**：純文字；30 秒；16:9；四段連續時間，允許 cuts。
- **最終 prompt**：

```text
A restrained live-action short drama at a nearly empty coastal bus terminal before sunrise. A young night-shift cleaner finds a child's paper crown, tries to return it, and finally reunites it with its owner. Cool blue dawn gradually warms to pale gold; realistic skin and fabric; subtle 35mm grain.

0–6s: Wide establishing shot. The cleaner pushes a cart across the wet terminal floor. He notices a small red paper crown beneath a bench and stops. Fluorescent hum, distant surf, cart wheels.
6–13s: Medium shot and insert. He picks up the crown carefully, sees a handwritten star on its inner band, and scans the empty platforms. Keep the crown red with one gold star.
13–22s: Tracking medium-wide shot. He walks toward the exit holding the crown at chest height. A sleepy child in a yellow raincoat appears outside with an anxious parent. The child sees the crown and runs toward him; the cleaner kneels before the child arrives.
22–30s: Shot-reverse-shot followed by a wide closing shot. The cleaner places the crown on the child's head; the child smiles, the parent nods in thanks, and the first sunlight enters through the glass. End with the cleaner returning to his cart while the family leaves together.

Maintain the cleaner's navy uniform, the child's yellow raincoat, the red crown with one gold star, and the terminal layout across all shots. Natural dialogue-free ambience and restrained music entering only after 22s. No subtitles.
```

- **已證實參數**：`duration: 30`、`ratio: 16:9`、`generate_audio: true`；T2V 無特殊 task lock。
- **預期觀察點**：四段是否按順序、三人物數量、紅冠／服裝、日光變化、13–22 秒空間與跪下 handoff。
- **失敗風險**：情節過載、人物重複、紙冠變形、對白被擅加、多 cut 掩蓋動作。
- **修正版 A**：刪成三段，移除 parent 的表演，只保留 child 與 cleaner。
- **修正版 B**：若 continuity 低，改用角色／場景 reference 圖後走 reference-to-video。

### 範例 03：T2V 產品物理與微距

- **狀態**：文件導出的未實測範例。
- **意圖**：測材質、因果與攝影節奏，不依賴品牌字樣。
- **輸入假設**：純文字；10 秒；1:1；無對白。
- **最終 prompt**：

```text
Premium tabletop food commercial. One unbranded dark-chocolate sphere sits at the center of a matte stone plate in a black studio. A narrow warm key light comes from upper left; cool rim light from rear right.

0–3s: Locked macro close-up. Fine condensation beads form on the sphere while the camera makes a very slow push-in.
3–6s: A small silver spoon enters from frame right and presses the top once. The shell cracks from the contact point; it does not explode before contact.
6–10s: Slow-motion close-up. Thick raspberry filling flows downward under gravity onto the plate while several shell fragments settle nearby. The camera arcs no more than 20 degrees clockwise and ends on the intact cross-section.

Keep exactly one sphere, one spoon, and one plate. Preserve light directions and the sphere's position. Crisp shell crack, soft spoon contact, and viscous filling sounds. No BGM. No text or subtitles.
```

- **已證實參數**：`duration: 10`、`ratio: 1:1`、`generate_audio: true`。
- **預期觀察點**：接觸先於破裂、液體向下、物件數量、光向、最後剖面可用性。
- **失敗風險**：無接觸自爆、液體逆重力、產品複製、微距 focus hunting。
- **修正版 A**：若物理錯，移除 arc camera，以 locked camera 降低同時變因。
- **修正版 B**：若碎片失真，改成「形成一道可見裂縫，少量餡料緩慢滲出」。

### 範例 04：T2V 雙人對白與說話者

- **狀態**：文件導出的未實測範例。
- **意圖**：測說話者、台詞順序與克制的表演。
- **輸入假設**：純文字；12 秒；16:9；英文台詞；不燒字幕。
- **最終 prompt**：

```text
Realistic intimate drama in a small all-night laundromat during rain. Two adults only: Mira, wearing a green wool coat, sits frame left; Daniel, wearing a gray work jacket, stands frame right beside a dryer. Soft fluorescent light, rain reflections in the front window, quiet restrained acting.

0–4s: Static medium two-shot. The dryer turns behind Daniel. Mira looks at the folded letter in her hands and says in English, "I read it twice."
4–8s: Over-the-shoulder from behind Mira, medium close-up on Daniel. After a short pause, Daniel answers in English, "Then you know why I came."
8–12s: Close-up on Mira. She folds the letter once, looks up at Daniel, and remains silent. Hold the last frame for one second.

Mira alone speaks the first line; Daniel alone speaks the second. Keep their positions, clothes, faces, and voices consistent. Dryer hum, rain, and paper fold only; no BGM. No subtitles.
```

- **已證實參數**：`duration: 12`、`ratio: 16:9`、`generate_audio: true`。官方文件支援 native multilingual generation，但本案語言／唇形仍需評測。
- **預期觀察點**：說話者歸屬、台詞原文、兩人位置、口型、停頓、衣著 continuity。
- **失敗風險**：互換台詞、擅加字幕、第三人、對白重疊、紙張變形。
- **修正版 A**：若說話者混淆，拆為兩鏡生成並在後期剪接／配音。
- **修正版 B**：若口型不穩，`generate_audio: false`，鎖 picture 後另做 ADR；此為後期策略，不宣稱模型內修復成功。

### 範例 05：單角色＋場景 reference

- **狀態**：文件導出的未實測範例。
- **意圖**：用兩張圖分責，避免把角色背景誤當目標場景。
- **輸入假設**：@Image 1 為角色乾淨半身圖；@Image 2 為無人物車站；10 秒。
- **最終 prompt**：

```text
Reference @Image 1 only for the woman's face, short black hair, body proportions, and rust-red trench coat. Reference @Image 2 only for the old mountain station's architecture, platform layout, wet stone material, mist, and cool dawn lighting. Do not copy the background from @Image 1.

At the mountain station before sunrise, the woman waits alone, hears an approaching train, and turns toward frame left.

0–4s: Medium-wide side view. She stands under the canopy beside one brown suitcase; mist drifts beyond the tracks. Slow lateral track to the right.
4–7s: The distant headlight appears at frame left. Wind from the approaching train moves the hem of her rust-red coat; she grips the suitcase handle.
7–10s: Medium close-up. She turns her head toward frame left, takes one steady breath, and shows a restrained hopeful expression. End before the train enters the platform.

Keep the same woman, coat, suitcase, platform geometry, and cool dawn direction throughout. Distant rail vibration, wind, and station ambience. No dialogue, no BGM, no subtitles.
```

- **已證實參數**：兩個 `reference_image`、`omni_reference_task_type: reference`、`duration: 10`、`ratio: 16:9`。
- **預期觀察點**：素材分責、臉與衣服、車站 layout、列車是否過早出現、風的因果。
- **失敗風險**：混入 Image 1 背景、行李複製、車站鏡像、臉漂移。
- **修正版 A**：若背景混淆，將 Image 1 去背／換中性底後再測。
- **修正版 B**：若角色漂移，縮短到 6 秒並保留單一景別。

### 範例 06：多角色 reference 與聲音 mapping

- **狀態**：文件導出的未實測範例。
- **意圖**：明確綁定三個角色與三個音色，測群像但守在官方較穩建議內。
- **輸入假設**：@Images 1–2 為角色 Aya 兩視角；@Images 3–4 為 Bo；@Image 5 為 Chen；@Audio 1–3 對應三人；15 秒。
- **最終 prompt**：

```text
Asset bindings:
- @Images 1–2 = Aya's appearance; @Audio 1 = Aya's voice.
- @Images 3–4 = Bo's appearance; @Audio 2 = Bo's voice.
- @Image 5 = Chen's appearance; @Audio 3 = Chen's voice.
Use each audio only for the named character's timbre. Do not swap faces, clothes, or voices.

Realistic warm family comedy in a compact apartment kitchen at breakfast. Aya stands at the stove frame left, Bo sits at the table center, and Chen enters through the rear doorway frame right.

0–5s: Medium-wide locked shot. Aya flips one pancake; Bo watches and says in Mandarin, "這次不會黏鍋吧？"
5–10s: Chen enters carrying one empty plate and says in Mandarin, "我只相信成品。" Aya catches the pancake cleanly and gives Chen a brief look.
10–15s: Medium three-shot. Aya places the pancake on Chen's plate; all three laugh once. End with the three fixed positions visible.

Keep exactly three people and one pancake. Maintain kitchen layout, clothing, voices, and left-center-right blocking. Natural kitchen sounds; no subtitles; no BGM.
```

- **已證實參數**：5 reference images、3 reference audio、`omni_reference_task_type: reference`、`duration: 15`、`generate_audio: true`。官方建議 subject audio/video 1–5 主體、subject image 1–8 主體較穩。
- **預期觀察點**：三人是否齊、音色配對、中文台詞、左右站位、鍋／盤／pancake 數量。
- **失敗風險**：聲音互換、角色融合、台詞順序、第三隻手、煎餅物理。
- **修正版 A**：移除多視角圖，只留每角一張乾淨 single-view，降低 mapping 負擔。
- **修正版 B**：若互動失敗，拆成 master shot、Aya insert、Chen reaction 三鏡，在剪輯維持對白。

### 範例 07：只取 video 的動作與運鏡

- **狀態**：文件導出的未實測範例。
- **意圖**：把 motion reference 與外觀／場景完全解耦。
- **輸入假設**：@Video 1 是無關人物的 7 秒滑板動作；@Image 1 是目標機器人；@Image 2 是目標倉庫。
- **最終 prompt**：

```text
Reference @Video 1 only for the skateboarder's motion timing, travel path, landing rhythm, and low side-follow camera movement. Do not reference its person, clothing, skateboard design, location, lighting, or color grade.
Reference @Image 1 for the small orange maintenance robot's appearance and wheel-leg construction. Reference @Image 2 for the abandoned warehouse layout, materials, and cold window light.

Generate a 7-second realistic science-fiction shot. The orange maintenance robot rides a narrow magnetic board through the warehouse, follows the same approach, jump arc, landing timing, and low side-follow camera path as @Video 1, then rolls to a controlled stop.

Keep one robot and one board. Preserve the robot's orange panels and wheel-leg geometry. Add only motor whine, wheel contact, landing impact, and warehouse reverb. No BGM. No subtitles.
```

- **已證實參數**：1 `reference_video`、2 `reference_image`、`omni_reference_task_type: reference`、`duration: 7`。
- **預期觀察點**：motion／camera 是否取自 Video 1、人物與原場景是否洩漏、機器人結構、落地因果。
- **失敗風險**：語意 reference 取錯屬性、機器人變成人、輪腿變形、鏡頭與動作不同步。
- **修正版 A**：只參考「approach–jump–landing」三段，不要求完整 camera match。
- **修正版 B**：先做 clay／previz，把 blocking 穩定後再渲染風格。

### 範例 08：音樂 reference 驅動節奏

- **狀態**：文件導出的未實測範例。
- **意圖**：測 audio reference 的節拍／情緒，不複製視覺。
- **輸入假設**：@Audio 1 為已授權的 12 秒打擊樂；無圖／影參考；直式短片。
- **最終 prompt**：

```text
Use @Audio 1 as the reference for beat timing, percussion accents, tempo, and overall rising energy. Do not add dialogue or vocals.

A stylized paper-cut animation of a tiny red sailboat crossing a dark-blue paper ocean toward a golden lighthouse. The visuals must react to the major accents in @Audio 1 without introducing unrelated cuts.

0–4s: Wide side view. The boat moves steadily from left to right; each low drum hit creates one broad paper wave.
4–8s: The wind grows stronger and the camera moves closer. On the strongest accent, the red sail opens fully and the boat rises over one large wave.
8–12s: The golden lighthouse beam turns toward the boat in time with the final rhythmic phrase. The camera pulls back and ends with the boat, lighthouse, and moon all visible.

Keep one red boat, one lighthouse, consistent paper textures, and left-to-right travel. Use @Audio 1 without added BGM. Add only subtle paper and wave sound effects beneath it. No subtitles.
```

- **已證實參數**：1 `reference_audio`、`omni_reference_task_type: reference`、`duration: 12`、`ratio: 9:16`、`generate_audio: true`。2.5 文件列 audio reference；LAS 文件另明列可單獨以 audio 作 reference，其他平台須另驗。
- **預期觀察點**：節拍對齊、主物數量、方向、紙材質、是否生成額外歌聲。
- **失敗風險**：beat mapping 模糊、BGM 被重寫、過度切鏡、帆船漂移。
- **修正版 A**：把 audio 節點人工註記成三個 time point，prompt 明寫 `at 4s / 8s / final accent`。
- **修正版 B**：畫面先靜音生成，後期依原音樂剪接；保留此案作對照組。

### 範例 09：九格 line-art storyboard

- **狀態**：文件導出的未實測範例。
- **意圖**：以 storyboard 控制高層 shot structure，而不誤稱逐格精準。
- **輸入假設**：@Image 1 為 9 格乾淨線稿、無文字；@Image 2–3 為角色；@Image 4 為場景。
- **最終 prompt**：

```text
@Image 1 is a nine-panel line-art storyboard used for overall shot order, shot sizes, blocking, and camera rhythm; it is not a literal style reference. @Image 2 is the appearance of pilot Nara. @Image 3 is the appearance of mechanic Sol. @Image 4 is the desert hangar environment, materials, and sunset lighting.

A 24-second realistic science-fiction farewell at a desert hangar. Nara prepares to depart in a small aircraft while Sol gives her a worn navigation token. Restrained performances, dusty warm sunset, cool shadows, subtle film grain.

Follow the nine storyboard panels in order as a high-level structure: hangar establishing view → Nara checking the aircraft → Sol approaching → token insert → Nara reaction → handshake → engine starts → Sol steps back → aircraft exits toward the sun. Fill in natural actions and camera movement between panels. Preserve the hangar axis and left-right screen direction.

Keep Nara, Sol, their clothes, the same token, aircraft, and light direction consistent. Engine, wind, metal creaks, and one short instrumental rise; no dialogue, no subtitles. End with Sol in foreground and the aircraft moving away in the same screen direction.
```

- **已證實參數**：4 `reference_image`、`omni_reference_task_type: reference`、`duration: 24`、`ratio: 16:9`。官方建議 storyboard ≤15 panels、簡單 line art、不要在 storyboard 堆文字。
- **預期觀察點**：九段高層順序、軸線、角色與 token、風格是否誤取線稿。
- **失敗風險**：跳 panel、成片變線稿、鏡頭過多、動作被壓縮。
- **修正版 A**：若漏 panel，改為 6 格或把 24 秒拆兩個 12 秒 shot group。
- **修正版 B**：若要求逐格更嚴，將 panel 拆成獨立 keyframe images，使用範例 10。

### 範例 10：六張獨立 keyframes

- **狀態**：文件導出的未實測範例。
- **意圖**：需要比多格 storyboard 更嚴的構圖／故事節點對齊。
- **輸入假設**：@Images 1–6 是同角色同場景、依序的獨立 keyframes；18 秒。
- **最終 prompt**：

```text
Use @Images 1 to 6 in order as keyframes. Keep the woman, white bicycle, blue scarf, riverside path, overcast light, and watercolor illustration style exactly consistent with the references.

Create one coherent 18-second sequence:
0–3s: Begin at @Image 1. Wide view; the woman starts riding along the river from left to right.
3–6s: Move naturally toward @Image 2 as the camera side-tracks and her blue scarf lifts in the wind.
6–9s: Reach @Image 3; she brakes beside the old stone bridge and puts one foot down.
9–12s: Transition to @Image 4; medium close-up as she notices a paper boat below and smiles.
12–15s: Transition to @Image 5; overhead view of the paper boat passing under the bridge while the bicycle remains visible at the bank.
15–18s: Resolve at @Image 6; pull back to the final wide composition and hold for one second.

All transitions must preserve left-to-right geography and plausible bicycle motion. Wind, bicycle chain, and river ambience only. No BGM. No subtitles.
```

- **已證實參數**：6 `reference_image`、`omni_reference_task_type: reference`、`duration: 18`、`ratio` 依 keyframe 一致畫幅。官方寫法要求第一句明示依序作 keyframes。
- **預期觀察點**：六個構圖節點、角色／單車／圍巾、方向、橋的空間、尾幀。
- **失敗風險**：硬切、順序錯、單車消失、overhead 破壞地理、尾幀不符。
- **修正版 A**：刪除 overhead，維持單一側向攝影語法。
- **修正版 B**：拆成 Images 1–3 與 4–6 兩次生成，再以核准 handoff 鏡接合。

### 範例 11：first-frame 啟動鏡頭

- **狀態**：文件導出的未實測範例。
- **意圖**：精確鎖首幀，讓畫面由靜態構圖開始運動。
- **輸入假設**：@Image 1 是 16:9 首幀；6 秒；無其他素材。
- **最終 prompt**：

```text
Begin exactly from the provided first frame. Preserve the red tram, wet rails, storefront positions, evening blue-hour light, and camera height.

0–2s: Hold the initial composition briefly. The tram's interior lights turn on from front to rear while rain continues falling.
2–5s: The red tram starts moving slowly toward frame right. The camera makes a gentle parallel track, keeping the tram centered; wheel spray follows the rails.
5–6s: The camera stops while the tram continues out of frame right, revealing the reflected lights on the wet street. End on the empty rails.

Natural rain, electric motor, wheel and distant street sounds. No BGM. No subtitles.
```

- **已證實參數**：@Image 1 `role: first_frame`、`ratio: adaptive`、`duration: 6`、`generate_audio: true`。
- **預期觀察點**：首幀嚴格度、車輛方向、雨／反射、camera stop 與 tram exit、空軌尾畫面。
- **失敗風險**：首幀被重新構圖、電車倒向、街景漂移、出畫不完整。
- **修正版 A**：移除平行 tracking，改 locked shot，只讓 tram 動。
- **修正版 B**：若要下一鏡銜接，`return_last_frame: true` 並僅在 QC 通過後升格 anchor。

### 範例 12：first + last frame 動作橋接

- **狀態**：文件導出的未實測範例。
- **意圖**：以首尾幀鎖定起終狀態，測中間物理合理性。
- **輸入假設**：@Image 1、@Image 2 同為 16:9；8 秒；首幀是關閉的紙傘，尾幀是完全打開的同一把紙傘。
- **最終 prompt**：

```text
Start exactly from @Image 1 and end exactly at @Image 2. The same indigo paper umbrella remains centered on the same wooden floor under the same soft top light.

0–2s: The closed umbrella lies still. A person's right hand enters from frame right and grips the wooden handle.
2–6s: In one continuous, physically plausible action, the hand lifts the umbrella slightly, slides the runner upward, and the ribs unfold evenly from the center outward. The paper canopy opens without tearing or changing pattern.
6–8s: The fully opened umbrella settles into the composition of @Image 2. The hand releases the handle and exits frame right. Hold the exact final composition for one second.

Keep one umbrella, the same indigo pattern, rib count, handle, floor grain, camera, and lighting. Cloth-and-wood handling sounds only. No BGM. No subtitles.
```

- **已證實參數**：Image 1 `first_frame`、Image 2 `last_frame`、`ratio: adaptive`、`duration: 8`。首尾幀須同畫幅。
- **預期觀察點**：首尾精度、傘骨拓撲、單手因果、圖案、尾幀 hold。
- **失敗風險**：傘骨融化、手數增加、尾圖被拉伸、非因果瞬變。
- **修正版 A**：把手移除，改由 unseen mechanism 緩慢開傘，降低人體交互。
- **修正版 B**：提供中間半開獨立 keyframe，改走範例 10 的 keyframe reference。

### 範例 13：粗粒度 clay previz 渲染

- **狀態**：文件導出的未實測範例。
- **意圖**：使用 clay video 控制 blocking／camera，使用圖片控制外觀／場景。
- **輸入假設**：@Video 1 是簡單幾何 previz；@Images 1–2 是兩角；@Image 3 是場景；12 秒。
- **最終 prompt**：

```text
Use @Video 1 only for shot order, camera position and movement, timing, the red model's path, the blue model's path, and their blocking. Do not reference its gray materials, model shapes, guide lines, or background.
Map the red model in @Video 1 to the courier from @Image 1. Map the blue model to the station guard from @Image 2. Use @Image 3 for the stone gate, market street, materials, warm sunset, and dust atmosphere.

Render the 12-second previz as a realistic historical adventure scene. The courier runs through the gate, passes the guard on the camera side, slides one sealed letter across the market table, and continues without stopping. The guard pivots to follow the courier with his gaze but does not block the path.

Strictly preserve @Video 1's order, paths, camera positions, shot-size changes, and pacing. Keep the courier, guard, sealed letter, and gate consistent. Add footsteps, fabric, table contact, market ambience, and no modern sounds. No subtitles.
```

- **已證實參數**：1 `reference_video`、3 `reference_image`、`omni_reference_task_type: reference`、`duration: 12`。官方建議粗 clay 使用簡單幾何體並逐項說明要取的資訊。
- **預期觀察點**：紅／藍 mapping、路徑與 camera、信件、場景風格、guide lines 是否洩漏。
- **失敗風險**：角色對調、原灰模外觀洩漏、previz 與文字矛盾、路徑碰撞。
- **修正版 A**：若 mapping 錯，把兩角拆成單人 previz shots。
- **修正版 B**：移除市場群眾，只保留 courier、guard、桌子與 gate。

### 範例 14：細粒度 clay rerender

- **狀態**：文件導出的未實測範例。
- **意圖**：完整模型只做材質／光影重渲染，保留其構圖與動作。
- **輸入假設**：@Video 1 為清晰完整的機械鳥 clay animation，沒有座標線／camera cone；6 秒。
- **最終 prompt**：

```text
Render @Video 1. Preserve its mechanical bird geometry, proportions, joints, wing motion, camera movement, timing, composition, and background layout.

Change only the rendering: brushed dark brass body plates, pale ceramic face panels, fine scratches on exposed edges, and small cyan indicator lights. The environment becomes a rain-soaked rooftop at night with deep navy shadows and warm window reflections. Light must react consistently to the existing geometry and wing movement.

No BGM; generate only rain, small servo movements, metal wing articulation, and distant city ambience. Do not add trajectory lines, coordinate axes, camera cones, extra wings, extra birds, text, or subtitles.
```

- **已證實參數**：1 `reference_video`、`omni_reference_task_type: reference`、`duration` 配合 reference intent、`generate_audio: true`。官方區分 fine-grained clay 以 rerender 為主，並建議來源完整清晰、移除干擾線。
- **預期觀察點**：幾何／動作 preservation、材質、光照交互、額外元件、聲音。
- **失敗風險**：被分類成 edit、幾何被重設計、額外鳥、雨與原 motion 不協調。
- **修正版 A**：若 task 分類不穩，明設 `omni_reference_task_type: reference` 並避免 `edit/replace` 動詞。
- **修正版 B**：把材質縮成 brass + cyan lights，先驗核心 rerender，再加雨景。

### 範例 15：video instruction edit，局部 A → B

- **狀態**：文件導出的未實測範例。
- **意圖**：只改指定時段的杯子，其他畫面與聲音不動。
- **輸入假設**：@Video 1 為 10 秒咖啡店手持鏡；原素材 16:9、mov。
- **最終 prompt**：

```text
Edit @Video 1. From 3s to 7s only, replace the plain white ceramic cup on the table with one matte cobalt-blue ceramic cup of the same size and in the same position.

Preserve the people, faces, hands, actions, table, coffee level, steam, composition, camera position and movement, focus, lighting, color grade, timing, dialogue, music, and ambient sound unchanged. The blue cup must inherit the original cup's occlusion, hand contact, reflections, and shadow. Before 3s and after 7s, leave the video unchanged. No other visual or audio changes.
```

- **已證實參數**：@Video 1 `reference_video`、`omni_reference_task_type: edit`、`ratio: adaptive`、`duration: -1`、`output_format: mov`。
- **預期觀察點**：3–7 秒範圍、杯子尺寸／接觸／遮擋、未編輯區、音訊 bit-for-intent preservation。
- **失敗風險**：全片杯色被改、手指穿透、杯形漂移、camera／grade 被重算、片長差異。
- **修正版 A**：把時間縮到手未碰杯的穩定區間先測外觀 replace。
- **修正版 B**：若未編輯區受影響，後期只取 3–7 秒核准區段並與原片無損拼接；記錄為 post workaround。

### 範例 16：edit + reference images 換角色與場景

- **狀態**：文件導出的未實測範例。
- **意圖**：保留原動作／節奏，依圖片替換兩人與環境。
- **輸入假設**：@Video 1 為 12 秒雙人走位；@Image 1 場景、@Image 2–3 角色。
- **最終 prompt**：

```text
Edit @Video 1. Replace the original location with the rain-darkened stone courtyard from @Image 1. Replace the person who begins on frame left with the ranger from @Image 2, and replace the person who begins on frame right with the archivist from @Image 3.

Keep the original two-person blocking, action order, walking speed, pauses, eyelines, camera movement, shot timing, and cut points unchanged. Preserve exactly two people. Adapt clothing movement, wet footprints, reflections, shadows, and rain interaction to the new courtyard. Keep the original dialogue timing and music unchanged.

Do not copy poses or backgrounds from @Images 2–3; use them only for each named character's face, hair, body proportions, and clothing design. No subtitles.
```

- **已證實參數**：1 `reference_video`、3 `reference_image`、`omni_reference_task_type: edit`、`ratio: adaptive`、`duration: -1`、`output_format: mov`。
- **預期觀察點**：left/right mapping、exactly two、原 blocking、角色／場景 reference 分責、雨與足跡。
- **失敗風險**：角色互換、reference pose 洩漏、第三人、動作節奏改變、dialogue 聲音換人不一致。
- **修正版 A**：先只換場景；通過後再以另一 run 測人物替換，避免一次改三大變因。
- **修正版 B**：若角色 identity 低，保留原場景，只做一角替換並建立可比較對照。

### 範例 17：audio edit 與翻譯口型

- **狀態**：文件導出的未實測範例。
- **意圖**：翻譯單一角色台詞、同步口型，不改畫面其餘元素。
- **輸入假設**：@Video 1 為 8 秒單人正面法語對白，已獲語音與肖像授權。
- **最終 prompt**：

```text
Edit @Video 1. Translate only the spoken French dialogue into Mandarin Chinese: "我們明天日出前出發。"

Match the same speaker's lip movements and speaking duration to the Mandarin line while preserving the person's identity, expression arc, gaze, head movement, body movement, composition, camera, lighting, background, ambience, and all non-speech timing unchanged. Remove the original French speech. Do not add a second voice, subtitles, captions, or BGM.
```

- **已證實參數**：@Video 1 `reference_video`、`omni_reference_task_type: edit`、`ratio: adaptive`、`duration: -1`、`output_format: mov`、`generate_audio: true`。官方 prompt guide 有翻譯＋lip movement 範例。
- **預期觀察點**：原聲是否移除、中文精確度、口型／時長、speaker identity、背景聲、字幕。
- **失敗風險**：音色變化、雙語重疊、擅加字幕、畫面重繪、嘴部 artifact。
- **修正版 A**：只修改聲音、不要求口型，建立 audio-only baseline。
- **修正版 B**：保留 picture，後期 ADR／lip-sync 專用工具處理；此項列入人工修正時間。

### 範例 18：forward extension 與 shot handoff

- **狀態**：文件導出的未實測範例。
- **意圖**：延長已核准 shot，保持身份、場景、方向、光色與 audio level。
- **輸入假設**：@Video 1 是已核准 15 秒 mov，尾端角色正向 frame right 行走；新增 8 秒。
- **最終 prompt**：

```text
Extend @Video 1 forward by 8 seconds. Continue directly from its final frame and preserve the same woman, navy coat, leather satchel, cobblestone alley, left-to-right travel direction, walking speed, camera height, focal feel, cool dawn light, wet-surface reflections, ambient sound, and audio level.

0–3s of the extension: She keeps walking frame right while the camera follows at the same distance. A bicycle bell is heard ahead before a cyclist becomes visible.
3–6s: One cyclist crosses the far background from right to left. The woman slows slightly but does not stop or change direction.
6–8s: She reaches a red doorway, raises her right hand toward the brass handle, and pauses before touching it. End on that anticipatory pose for the next cut.

Do not replay or summarize the ending of @Video 1. Do not introduce a second version of the woman. No subtitles and no new BGM.
```

- **已證實參數**：@Video 1 `reference_video`、`omni_reference_task_type: extend`、`ratio: adaptive`、`duration: 8`、`output_format: mov`、建議 `return_last_frame: true`。
- **預期觀察點**：接縫畫面／音量、方向、人物／衣包、步速、cyclist 因果、尾 pose。
- **失敗風險**：重播原尾段、音量跳變、人物漂移、方向反轉、接縫速度 discontinuity。
- **修正版 A**：移除 cyclist，只做同速跟拍到門口。
- **修正版 B**：若接縫不穩，改硬切到下一鏡，使用核准角色／場景 anchors，而非繼續累積 extension。

### 範例 19：兩段影片的 seamless transition

- **狀態**：文件導出的未實測範例。
- **意圖**：只生成過橋轉場，不改原兩片。
- **輸入假設**：@Video 1 結尾為俯拍旋轉唱片；@Video 2 開頭為夜間圓形交通環島；兩片已鎖 picture。
- **最終 prompt**：

```text
Create a seamless transition between @Video 1 and @Video 2 without altering the uploaded source segments themselves.

Continue the clockwise rotation and top-down camera from the end of @Video 1. The black vinyl grooves gradually become wet circular roads; the center label becomes the illuminated island of the roundabout. Preserve continuous angular speed through the transformation. As the texture change completes, lower the camera slightly and arrive exactly at the opening composition, traffic direction, rain, and night lighting of @Video 2.

Carry the final musical rotation sound from @Video 1 into the first traffic ambience of @Video 2 with one smooth crossfade. Do not add text, logos, dialogue, or subtitles.
```

- **已證實參數**：2 `reference_video`、reference／transition intent；`ratio` 應與來源相容並依平台文件。官方 prompt guide 列 seamless transition，但未在此範例中虛構 transition 長度或專用欄位。
- **預期觀察點**：角速度、圓形 match、兩原片是否未被改、視聽 crossfade、進入 Video 2 的精度。
- **失敗風險**：模型重製原片、方向跳、過長 morph、道路拓撲錯、音訊突變。
- **修正版 A**：明確只取各片尾／首 1–2 秒作 input（若平台／剪輯流程允許），縮短轉場負擔。
- **修正版 B**：以 VFX optical／3D morph 後期完成，保留 AI 版本作 comparison。

### 範例 20：one-click 素材短片

- **狀態**：文件導出的未實測範例。
- **意圖**：快速把六張同系列插畫排成小故事，但限制身份與順序。
- **輸入假設**：@Images 1–6 是同一隻紙偶貓在書店的已授權插畫；12 秒；9:16。
- **最終 prompt**：

```text
Turn @Images 1 to 6 into a 12-second vertical one-click video in their upload order. They all depict the same blue paper-cut cat visiting the same small bookshop.

Create a playful paper-cut stop-motion montage: the cat enters → examines a red book → carries it to the counter → receives a paper bag → exits into the evening street → final close-up of the red book visible through the bag. Use small parallax and restrained live-photo motion, but do not redesign, repaint, duplicate, or change the original cat, book, shop, or paper textures.

Transitions should be motivated by page turns and paper shapes. Add light paper rustle, shop bell, footsteps, and a short playful instrumental cue. No dialogue. No subtitles. End on @Image 6's composition.
```

- **已證實參數**：6 `reference_image`、`omni_reference_task_type: reference`、`duration: 12`、`ratio: 9:16`、`generate_audio: true`。官方列 one-click video creation；API 是否另有專用欄位未在本研究假設。
- **預期觀察點**：上傳順序、同一角色、圖像 preservation、red book、paper transitions、尾圖。
- **失敗風險**：自由重排、過度動畫、角色重繪、文字變形、素材複製。
- **修正版 A**：每圖只做 1.5–2 秒微動，在 NLE 人工排序，避免模型自動 montage。
- **修正版 B**：移除 music，由剪輯後期配樂，先驗畫面 preservation。

### 範例 21：green-screen edit／環境物理適配

- **狀態**：文件導出的未實測範例。
- **意圖**：替換綠幕並測衣髮、影子與風向是否適配新環境。
- **輸入假設**：@Video 1 為 9 秒授權角色在綠幕上由左向右步行；@Image 1 為海邊木棧道。
- **最終 prompt**：

```text
Edit @Video 1. Replace only the green-screen background with the windy coastal boardwalk from @Image 1.

Keep the original person's identity, clothing design, body movement, walking cadence, path, camera position, framing, and duration unchanged. Integrate the person into the new environment with physically consistent contact shadows, foot placement on the boards, cool overcast light, reflected sea color, and wind from frame right to frame left. The coat hem and hair should react subtly in that same wind direction without changing the original gait.

Remove all green spill and edge contamination. Add restrained sea, wind, wood footstep, and distant gull ambience. No dialogue, BGM, text, or subtitles. No other changes.
```

- **已證實參數**：1 `reference_video`、1 `reference_image`、`omni_reference_task_type: edit`、`ratio: adaptive`、`duration: -1`、`output_format: mov`。ByteDance 2.5 發布文與官方 prompt guide 均列 green-screen editing 類型。
- **預期觀察點**：key edge、green spill、腳底接觸、影子、風向、原 gait／identity、mono ambience。
- **失敗風險**：人物被重畫、腳滑、風向矛盾、背景透視不合、色邊。
- **修正版 A**：先做無風、locked light 的背景 replace，再分開做風／衣髮細化。
- **修正版 B**：若精細 key 失敗，回到傳統 chroma key＋composite，AI 只生成 clean plate。

## 5. 壞／好 prompt 對照

### 對照 A：模糊主體與動作

**壞**：`A cinematic woman walks dramatically in a beautiful city, amazing camera.`

**好**：`At blue hour on a wet Taipei side street, one woman in a rust-red coat walks from frame left to frame right, slows at a closed noodle shop, and looks through the glass. Medium-wide eye-level side track; cool ambient light with one warm practical inside; rain, footsteps, and traffic only; no BGM.`

**原因**：好版把數量、服裝、空間、方向、動作結果、景別、光與聲分開；「cinematic／beautiful／amazing」不能替代可見規格。

### 對照 B：素材 mapping

**壞**：`Use these images for John and the school. John runs.`

**好**：`@Images 1–2 are John’s face, hair, body proportions, and blue school jacket. @Image 3 is only the school corridor layout and daylight. John runs from the rear doorway toward camera, carrying one yellow folder; do not copy the backgrounds of @Images 1–2.`

**原因**：好版讓 upload order、角色屬性、場景屬性與排除範圍可稽核。

### 對照 C：時間過載

**壞**：`0–2s 她起床刷牙換衣出門；2–4s 開車到公司開會吵架辭職。`

**好**：`0–4s：她在床邊坐起，看見手機上的未接來電；4–8s：她穿上外套走到門口，在握住門把後停住。`

**原因**：兩段各只承擔一個主要狀態變化；未塞入無法在時長內可讀地表演的事件。

### 對照 D：edit 範圍

**壞**：`Make the cup blue and better quality.`

**好**：`Edit @Video 1. From 3–7s only, replace the white cup with a matte cobalt-blue cup of identical size and position. Preserve hands, actions, shadows, reflections, camera, timing, grade, and all audio unchanged. Before 3s and after 7s, make no changes.`

**原因**：好版提供 A→B、時間範圍、幾何／物理 preservation 與未修改區。

## 6. 送出前檢查表

### 6.1 版本與參數

- [ ] 平台、模型顯示名稱、model ID 與文件更新日已記錄。
- [ ] task type 與 prompt 動詞一致；edit／extend 不以 `auto` 掩蓋含糊意圖。
- [ ] `ratio`／`duration` 通過 task-specific gate。
- [ ] `seed` 已記錄；需要 paired comparison 時固定 seed，但未把它誤稱完全決定論。沒有把 `draft`、`negative_prompt` 假稱為 ModelArk Seedance 2.5 支援欄位。
- [ ] 解析度依本次平台，不把 ModelArk 1080p 套到 LAS。
- [ ] 需後期調色／key／extension 時評估 `mov` 與播放器相容性。

### 6.2 Prompt 與素材

- [ ] 主體數量、身份、方向、起始／終止狀態可見且無矛盾。
- [ ] 每個 reference 編號與上傳順序相同，明列要取／不取屬性。
- [ ] timestamps 連續、使用整秒、每段工作量合理。
- [ ] 全局 invariants 未被局部段落推翻。
- [ ] cut／continuous take／camera movement 沒有互斥。
- [ ] 對白有說話者、語言、原文與順序；字幕／BGM／audio 需求明確。
- [ ] 參考素材的肖像、音訊、著作權與使用權已驗證。
- [ ] prompt、輸入與預期輸出均未含敏感憑證或 signed URL。

## 7. 生成後評分規準

每個 shot 先過硬 gate，再算 1–5 分；硬 gate 失敗不得用「平均分很高」放行。

### 7.1 硬 gate

1. 安全、授權、交付規格與時長正確。
2. 必要人物／物件存在且無多餘主體；角色身份可辨。
3. 關鍵故事 beat 與因果成立。
4. 無不可剪的結構崩壞、嚴重 flicker、錯字／亂字幕、聲音爆裂。
5. continuity-critical shot 的服裝、道具、方位、光色與 handoff 可接。

### 7.2 分項 1–5

| 維度 | 1 分 | 3 分 | 5 分 |
|---|---|---|---|
| Prompt adherence | 核心事件缺失／反向 | 主事件成立但次要規格漏失 | 主體、事件、順序、camera、聲音均可逐項勾稽 |
| 角色／場景 continuity | 身份／場景不可辨 | 大體相同、有可修小漂移 | 跨幀與相鄰 shot 穩定，關鍵特徵一致 |
| 時間穩定性 | 嚴重 flicker／形變 | 局部短 artifact | 主體與背景全段穩定 |
| 動作自然度 | 因果／解剖／物理崩壞 | 主要動作可讀、細節不自然 | 軌跡、速度、接觸、結果與常識一致 |
| 攝影 | 意圖不成立、軸線混亂 | 大致符合但速度／景別偏差 | 景別、機位、運鏡、轉場服務敘事 |
| 聲音 | 說話者／同步／音量錯 | 可用但需 ADR／mix | 對白、環境、動作、音樂與畫面精確協同 |
| 剪輯可用性 | 無可用區段 | 可取部分／需遮切 | 完整 shot 可直接入 cut 且 handles 足夠 |

`實務建議`：先記可定位的 defect 與 timecode，再打分；不要先有總體好惡再反填理由。

## 8. 失敗診斷決策樹

```text
失敗
├─ API / task error
│  ├─ TaskTypeConstraint → 核對 edit: adaptive + -1；extend: adaptive；first frame: adaptive
│  ├─ TaskTypeMismatch → 讓 task hint、素材 role、prompt 動詞完全一致
│  └─ Input / moderation → 核對格式、時長、肖像授權與資產 ID；不得繞過限制
├─ 核心事件不成立
│  ├─ 時段過載 → 刪次要 beat 或拆 shot
│  ├─ 指令衝突 → 依優先級裁決，只保留一種 camera / action 結果
│  └─ reference 抢權 → 明列素材只取屬性，或移除一個 reference 做 A/B
├─ Identity / continuity 漂移
│  ├─ mapping 含糊 → 每角逐一列圖、聲音、服裝與位置
│  ├─ reference 品質差 → 換乾淨、單一主體、核准 anchor
│  └─ sequence 累積誤差 → 回到最後核准 checkpoint，不延伸失敗輸出
├─ 動作 / 物理失真
│  ├─ 同時動作太多 → 一次只留一主動作與一互動
│  ├─ camera 與 action 競爭 → 先 locked camera 驗動作
│  └─ 模型能力邊界 → 拆 shot、用 previz / VFX / live action，不靠更長 prompt
├─ Edit 外溢
│  ├─ 改動範圍不明 → 明寫 A→B、時間、preserve 清單
│  └─ 未編輯區仍變 → 只取核准區間與原片後期拼接
└─ 聲音失敗
   ├─ speaker / language 錯 → 一鏡一說話者或另做 ADR
   ├─ 音量接縫 → 用 MOV、匹配 ambience，後期 crossfade / mix
   └─ 擅加 BGM / subtitle → 明寫 No BGM / No subtitles；必要時靜音生成
```

## 9. 最小變因迭代紀錄

每次 retry 只改一個假設，使用下表；若同時換 prompt、reference、duration、resolution，就無法把改善歸因給任何一項。

| 欄位 | 記錄 |
|---|---|
| Run ID / parent run |  |
| 平台／model ID／文件版本 |  |
| 唯一改動 |  |
| 固定不變項 |  |
| 假設與預期改善 |  |
| 硬 gate | pass / fail + 原因 |
| 分項分數與 timecode defect |  |
| 決策 | approve / retry / route-to-VFX / abandon |

## 10. 已知未知與不可保證

- `未知／待驗證`：未經本專案受控生成，無法宣稱上述 schema、任何範例或任何字數是「最佳」。
- `未知／待驗證`：官方展示片與 prompt 只能證明展示／文件內容，不能推出成功率、平均重試數或成本。
- `官方事實／限制`：ModelArk 2.5 支援 `seed`，但官方只稱同 request + 同 seed 產生相似結果，不保證完全一致；實際輸出變異仍待本專案量測。
- `官方事實`：ByteDance 自述複雜動作的物理合理性、極多主體互動穩定性仍有提升空間；因此高風險 shot 必須有替代分流。
- `實務建議`：把 prompt 視為一份可驗收的 shot contract，而不是咒語；真正的長片 continuity 由 bible、資產、狀態、核准 anchors、版本與 QC 共同維持。
