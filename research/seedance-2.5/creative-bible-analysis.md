# 《The Seedance 2.5 Creative Bible》逐章逐頁分析

## 分析邊界與證據標籤

本文件分析本機來源 `seedance-25-creative-bible.pdf` 的全部 15 頁。它是 `MACHINA · AUGUST 2026` 的 production bible，不是 ByteDance/BytePlus 官方文件。為避免把實務經驗誤升格成模型規格，下列標籤固定使用：

- **D 原文主張**：PDF 明文寫出的能力、規則、經驗或數字。
- **視覺圖表內容**：PDF text layer 未完整收錄、但在 render/內嵌圖中直接可見，並以人工視檢及 OCR 交叉確認。
- **可執行映射**：把 D 的原則轉成 prompt、reference、shot planning 或 QC 操作；屬研究團隊推論，不代表官方保證。
- **待交叉驗證**：D 沒有附一手證據、與官方免責語氣不同、或可能只適用作者四次 production run 的說法。

頁碼一律指 PDF 頁碼，與印刷頁碼 01-15 相同。每頁均可回查：

- 文字：`research/seedance-2.5/sources/creative-bible/pages/text/page-NN.txt`
- render：`research/seedance-2.5/sources/creative-bible/pages/rendered/page-NN.png`
- 複雜圖表 OCR：頁 03、04、09、11、14 的 `research/seedance-2.5/sources/creative-bible/ocr/diagram-page-NN.txt`

## 章節索引

| PDF 頁 | 章節 | 主要決策 |
|---:|---|---|
| 1 | Cover / Contents | 能力宣稱、全書導航、版本歸屬 |
| 2 | 01 The Model | 長片段與大 reference budget 不等於可降低 brief 密度 |
| 3 | 02 The Prompt System | 30 秒拆四 beats，每 beat 重複六類資訊 |
| 4 | 03 The Reference System | 每個 reference 同時寫 job 與 do-not-touch contract |
| 5 | 04 Characters | character passport、固定缺陷、封閉 wardrobe、micro-behavior |
| 6 | 05 Composition and Light | camera/light/grade 分欄鎖定、style contract |
| 7 | 06 Sound and Music | 每 prompt 的 audio block、voice anchor、人工後期 |
| 8 | 07 Sharp Text and Products | 文字獨立任務、產品 passport、場景級數量約束 |
| 9 | 08 Consistency | 七道 generation gate、10/10 stress test、pipeline memory |
| 10 | 09 Motion | camera move + in-scene event + no frozen figures、跨 cut 狀態改變 |
| 11 | 10 Iteration Loop and Edit | 單變因迭代、10-15 次停止線、acceptance/frame/edit gates |
| 12 | 11 UGC Factory | customer language、hook-first、voice anchor、平行 batch |
| 13 | 12 Format Recipes | K-pop、vlog、3D product、animation、realistic lighting recipe |
| 14 | 13 Full Production Pipeline | 11 stages、05/06 lock gate、並行 generation/edit、human handoff |
| 15 | 14 Master Checklist | 四階段 render 前後總檢查表 |

---

## 第 1 頁 - Cover / Contents

### 直接內容

頁首把文件定位為「四次 production runs 壓縮出的 reference document」，並用四張卡片提出：30 秒單次片段、1080p native、音畫一 pass、30/10/10 image/video/audio reference budget。下方 contents 正確指向 PDF 2-15 頁的 14 章。

### 可執行映射

這頁適合作為 project intake 的版本 gate，而不是直接當 capability truth：

1. 在每個 project manifest 先記 `model_name`、`platform`、`model_id`、`document_date`、`generation_mode`。
2. 把 30 秒、1080p、reference 數量拆成可驗證欄位，不把它們混成「品質保證」。
3. 在 shot request 中仍保留 `duration`、`aspect_ratio/resolution`、`reference_count_by_type`；若 UI/API 鎖定參數，改標 `locked_by_input`。

### 待交叉驗證

- A/B 官方來源支持 30 秒與最多 50 個 multimodal assets，且 A 列出 images 30、videos 10、audio 10；但「原生 1080p、不需 upscale」仍要由 B 的正式參數/模型文件逐項確認。
- 「character and voice hold from first frame to last」若在後頁出現，必須視為作者 production observation，不能改寫成成功保證；A 明確說結果仍受模型能力、輸入與隨機性影響。

## 第 2 頁 - 01 The Model

### 直接內容

**D 原文主張**把變化集中在兩點：單 clip 從 15 秒增至 30 秒、reference budget 大幅增加。Capabilities 欄另聲稱音畫同 pass、lip-sync dialogue/SFX/ambience、native 1080p、30/10/10 references、quoted dialogue word-for-word。右欄的「stability law」強調工作範圍應小於上限：images 1-8、video/audio 1-5，reference 越多越不穩定。頁末警告不能把舊 15 秒 prompt 單純拉長；弱 brief 仍可能被漂亮地 render，brief 本身才是產品。

### 可執行映射

- 把 reference 上限與 working range 分開記錄：`hard_limit` 只表示可送出，`recommended_working_range` 才是預設。
- 長度增加時，不增加每句模糊描述的範圍；改為增加 beat/shot 數並維持每 shot 的資訊密度。
- 在送出前做 `reference necessity review`：每個 reference 必須有唯一 job；刪掉無法說明用途者。
- 在 acceptance gate 分開評 `render polish` 與 `brief adherence`，避免漂亮畫面掩蓋錯誤故事、錯誤角色或錯誤事件順序。

### QC

每次 render 至少記：輸入 reference 數、角色/物件錯配、identity drift、事件遺漏、額外物件、lip-sync、首尾半秒穩定性。reference 數增加後若失敗率升高，只能稱相關性，不能由這一頁推成因果。

### 待交叉驗證

「模型從不拒絕不能處理的要求」與「逐字對白」是絕對語氣，官方 A 只有寫 prompt 可提高控制機率且結果可能變動；應降級為 D 的作者經驗。

## 第 3 頁 - 02 The Prompt System

### 直接內容與圖表補全

頁面主張「commercial prompt 是 shot list，不是 description」。**視覺圖表內容**把 30 秒示例拆成四個連續 beats：

| Beat | 角色 | 動作/事件 | 空間 | Camera | Style | Rules |
|---|---|---|---|---|---|---|
| 0-6s Set the scene | 三十多歲、深色 linen apron 的女人 | 把一只杯子放到 counter | 小 cafe、第一道光落在 glass | wide frame 緩慢 push-in | 35mm grain、muted grade、shallow depth | 本 beat 無螢幕文字 |
| 6-14s Build it out | 同一張臉、apron、cup | 倒飲料，steam 從 rim 上升 | 同一 counter、camera 稍後退 | handheld orbit left-to-right、no cut | 同 grade、淺景深 | face 不得在 beats 間 drift |
| 14-24s The turn | 她與完成的杯子同框 | 看向 camera 並說話 | 同 counter、light 提升一 stop | chest-height lock-off | 同 grade、contrast 增一 stop | 逐字 lip-sync；圖中 dialogue 為 `I stopped buying the expensive one.` |
| 24-30s How it ends | 杯子單獨、手離開 | 她走出 frame | counter 留空 | slow pull-back 後 hold | 同 grade、light falloff | held frame 結束、no cut |

圖下另把 audio 分成 same-pass、voice quality、room tone、music；用 3.5 words/sec 得到 30 秒約 105 words、6 秒約 21 words，並警告 generation length 與 timestamp 不一致會壓縮 delivery。

### 可執行 prompt schema

```text
[GLOBAL LOCKS]
Character identity / wardrobe / key prop / location / palette / audio voice anchor.

[BEAT 01 | 0-6s | SETUP]
Subject:
Primary action/event:
Place and spatial state:
Camera framing and one movement:
Style/light/grade:
Continuity and exclusion rules:
Audio/dialogue:
End state:

[BEAT 02 | 6-14s | BUILD]
...repeat all fields; do not write "same as above" for identity-critical data...
```

### Shot planning 與 QC

- Beat boundaries 是 event time budget，不是 frame-accurate edit points；A 官方文件也明確支持這個限制。
- 每 beat 的 `end_state` 必須能成為下一 beat 的起始 continuity state。
- Speech budget 先用 3.5 words/sec 作 planning heuristic，再以選定 voice 的實際 read 測量，不把 3.5 當語言/聲線無關的常數。
- 比對四 beat 是否都完整寫了 subject/action/place/camera/style/rules；漏一欄即在 prompt lint 階段退回。

### 待交叉驗證

PDF 稱四-beat map 是 ByteDance 自己的，但 A 支持的是「以 stages 與 end states 組織 30 秒」而非強制 0-6/6-14/14-24/24-30。這四段應視為一個 production template，不是 API 規則。

## 第 4 頁 - 03 The Reference System

### 直接內容與圖表補全

核心是每個 reference 都有兩行 contract：`job` 與 `do not touch`。**視覺圖表內容**把四類 reference 拆開：

- Image：capacity 30、作者建議 stable 1-8；`@image 1` 只鎖 face/outfit/prop/location；不要把 30 當工作數。
- Video：capacity 10、stable 1-5；`@video 1` 只鎖 motion/camera/pacing；明寫不要帶入影片中的 identity/clothing/scene。
- Audio：capacity 10、stable 1-5；一支 approved hook 的 audio 作後續 voice anchor；不要把 10 當工作數。
- Clay render：D 圖示把它當 bare 3D shape，只鎖 camera movement/blocking，look/material/light 由 image ref 負責。

下半圖定義 asset passport：descriptor verbatim、neutral grey 的 front/3/4/profile/back/close portrait reference sheets、wet/bloodied 等 state variant 另立資產與 tag。Build order 是先用 image model 建 reference、lock、之後 motion 不對只修 motion prompt，不重生 locked image。

### 可執行映射

```text
@Image 1 job: defines Character A's face, hair, and fixed wardrobe.
Do not use: background, pose, camera angle, lighting, or other people.

@Video 1 job: defines the action timing and left-to-right orbit only.
Do not use: the performer's identity, clothing, props, location, or color grade.

@Audio 1 job: defines Character A's voice timbre and approved delivery.
Do not use: background music or ambience from the clip.
```

資產登錄至少含：`asset_id`、`descriptor_version`、`reference_files`、`allowed_attributes`、`excluded_attributes`、`state_variant`、`status=LOCKED`、`sha256`。

### QC

- 每個 tag 都必須找到唯一 asset registry row，且 job/exclusion 不能互相矛盾。
- 同一人多視角必須明說是同一 identity；不能讓模型自行從 collage 標籤推理。
- Edit prompt 只改一個 dimension，其他維度逐項列 preserve。

### 待交叉驗證

`@clay render 1` 並未在 A 的官方通用語法中獲證實，可能是特定工作流/平台約定；playbook 不得把它寫成 Seedance 2.5 官方 universal tag，除非 B 或平台 UI 再證實。

## 第 5 頁 - 04 Characters

### 直接內容

頁面把 text description 與 identity memory 分開：同一句描述在兩次 generation 不保證同一人，解法是 character sheet。它給出一段完整 headshot prompt，固定 age、hair、eye、skin、freckles、expression、makeup、tank top、earrings、daylight、plain wall、imperfect framing，並用 `not studio, not glossy` 收口。Fullbody 必須從 headshot reference 生成，同 outfit；before/after 用「same character + identical fixed features + new state」表示兩狀態。右欄強調 fixed imperfection、face-framing strands、closed wardrobe、micro-behavior 與眼神 target。

### 可執行映射

Character passport 建議欄位：

- `identity_invariants`：face geometry、eye color、hair shape、skin tone、固定小特徵。
- `wardrobe_closed_set`：服裝、飾品，以及明確沒有的飾品。
- `reference_views`：headshot/fullbody/front/3-4/profile/back。
- `state_variants`：例如 dry/wet/injured/older；每個 variant 有自己的 reference，不用一句「現在變老」覆寫 base sheet。
- `performance_cues`：breath、blink、glance、grip adjustment、half-smile 等可觀察 cue。
- `gaze_target_by_beat`：lens、hand、off-camera partner、prop。

### Prompt 與 shot planning

每一鏡把 identity invariants 原樣複製；只把 pose、emotion cue、gaze target、action、location 當 variable。變化前後若需要同一 identity 的兩個 state，優先分成兩鏡並以 cut handoff，不要求單鏡完成高風險 transformation。

### QC

用 face、freckles、hair strands、earrings、top 作固定 checkpoints；另查 count、左右方向、鏡間 makeup/skin texture 漂移。角色在 solo shot 通過不代表 two-shot 通過，需在其實際 frame-mates 與 light 下 stress test。

## 第 6 頁 - 05 Composition and Light

### 直接內容

頁面要求 camera、light、grade 分開命名。Camera 示例有 UGC 的 front camera/chest-up/micro shake，與 produced spot 的 35mm/slow push-in/product centered；提醒不要寫「viewer is camera」後又讓模型生成手機入鏡。Light 分方向與色溫、近景 hard specular/遠景 haze、bounced color。Grade 以 high contrast/cool tones/warm skin、atmospheric perspective、highlight rolloff、rim light 描述。

Style contract 的方法是挑 5-10 張目標電影畫面，分析 lens/light/palette/grain/contrast/blocking/atmosphere/era，鎖成一段文字，在整個 project 的 image/video prompt 原樣重用。頁末三個 frame rules：objects 比 faces 更穩定地承載情緒、一個 normal place 放一個 impossible thing、角色要有 cost、frame exploration 先於 motion。

### 可執行映射

把視覺規格分成不可變與每鏡變量：

- Global style contract：palette、contrast curve、grain、skin treatment、atmospheric perspective、highlight behavior。
- Shot camera：shot size、angle、lens feel、camera height、單一 move、focus target。
- Shot light：key direction/quality/color、fill source/color、practical、rim、haze。
- Shot grade delta：只允許為敘事轉折指定小幅變化，否則沿用 global contract。

### QC

用 reference stills 做並排 visual audit：lens feel、color temperature、skin tone、black level、highlight clipping、background contrast、camera axis。Prompt 中 subject movement 與 camera movement 必須是不同句，避免主體不動只剩 camera drift。

### 待交叉驗證

Midjourney/Frameset/ShotDeck 等工具選擇與「objects hold emotion better」是 D 的 production taste，不是模型規格；可以作工作流建議，但不要標官方能力。

## 第 7 頁 - 06 Sound and Music

### 直接內容

每個 prompt 結尾都要 camera-and-sound block。D 示例：`iPhone front-facing 23mm equivalent, gentle handheld drift, built-in mic, no music`；UGC voice 用 clear phone-mic + light room tone，produced spot 用 clean studio voice/no echo；music 要說清楚在 dialogue 下方。Delivery 只用一個可表演的詞；先 approve hook 的 face/voice，再抽 audio 作後續 anchor。品牌名若念錯，以讀音重拼；台詞要用口語 contractions 並朗讀。

Feature-grade 區塊把 generated sound 稱為 scaffolding 而非 final soundtrack：保留 lip-sync/SFX/ambience 作剪輯節奏，voice 做 noise/timbre/timing cleanup，音樂與 final mix 交給人；列出 streaming 約 -14 LUFS、TV EBU R128 -23 的交付參考。

### 可執行映射

```text
[AUDIO]
Speaker: Character A, using @Audio 1 for voice timbre only.
Dialogue language / accent / delivery word:
Exact dialogue: {...}
Mic perspective and room tone:
In-frame SFX tied to visible actions:
Music: none / instrument + level relationship to dialogue:
Continuity: preserve voice identity and loudness across beats.
```

在 asset registry 把 voice anchor、ambience、music 分開；不要用一個混合 audio ref 同時控制三件事。每鏡產生後記 lip-sync、pronunciation、voice drift、room tone、SFX causality、music masking。

### 待交叉驗證

「generated music is unlicensed」語義含混且未附來源；不能由此推導法律結論。LUFS 數字是 post-production delivery heuristic，需按實際平台規格查證。

## 第 8 頁 - 07 Sharp Text and Products

### 直接內容

頁面說 in-frame text 最脆弱；每個 sign/screen/label 應是獨立任務。產品示例用 material、shape、orientation、quoted exact label、font style、background/light/composition 描述 sunscreen tube。兩個核心規則是 exact label text + font style、用 material words 而非 brand adjectives；品牌名要大。Titles/captions/UI 應在 graphics/editing 製作。

產品一致性 laws：產品有自己的 still，生成一次後每次附上，真實尺寸與 descriptor 原樣重複；scene-wide count 要寫「exactly one... no duplicate... no reflection copies」；若角色要拿產品，clip 起始就已在手中，不腳本化 reach-and-lift。

### 可執行映射

- Product passport：front/back/side still、dimensions、material、finish、label hierarchy、exact strings、logo placement、cap/connector state。
- Text task inventory：列出每個可見字串、語言、字型類別、位置、大小、是否必須在 generation 或可後製。
- Shot prompt 只把必要 hero label 留在 generation；字幕、UI、法規文字與細小標籤預設進 post overlay。
- Interaction shot 分解：shot A object already held，shot B 使用 cutaway 或下一 state；不要把 grasp、uncap、apply、re-cap 全塞一鏡。

### QC

逐 frame OCR/人工讀 label；檢查品牌字串、字母形狀、位置、比例、tube count、reflection duplicate、hand anatomy、尺寸漂移。A 官方文件同樣提醒字幕、公式、sign、product spec 的完全準確要結合 prepared references 與 post-production，與本頁方向一致。

## 第 9 頁 - 08 Consistency

### 直接內容與圖表補全

頁面標題是「model has no memory - pipeline is the memory」。下方文字把 passport 定義為 verbatim descriptor + neutral-grey multi-view images；state variants 各自有 tag；鎖定前要在實際 angles/light/frame-mates 下 stress test，目標是 10/10 repeatability。

**視覺圖表內容**提供七道 gauntlet：

1. Assets locked：所有 character/location/prop 未鎖前不生成。
2. Descriptor verbatim：每 prompt 原樣複製，不能 `shortened for brevity`。
3. Stress-tested：不同 angle/shot size/scene light/two-shot；失敗就繼續測至 10/10。
4. Objects counted scene-wide：精確數量、任何 surface/reflection 不得 duplicate。
5. Wardrobe closed：把未允許的 jewellery/ring/watch 等 open slot 關閉。
6. State change across cut：swatch/half-blended/clean skin 分三鏡，不在單鏡做變化。
7. In-frame text separate task：exact label + font style；titles 在 edit 做。

通過後標「7/7 gates / locked at 10/10 repeatability」。右欄把「faces anchor, products drift」綁 gate 02，把「objects start in hand」綁 gate 06。四個 golden laws 是 assets first、one passport verbatim、surgical edit、everything versioned/logged。

### 可執行 gate

每個 shot request 必須附一份機器可檢查的 gate record：

```yaml
assets_locked: true
passport_versions: [char_cal_v03, prop_tube_v05, loc_bathroom_v02]
descriptor_verbatim_hash_match: true
stress_test_passes: {char_cal: 10/10, prop_tube: 10/10}
scene_object_counts: {tube: 1, person: 1}
wardrobe_closed: true
state_change_handoff: cut
text_tasks_externalized: [caption_01, legal_01]
```

### QC 與風險

10/10 只能表示指定 stress-test set 的成功率，不是模型普遍保證。`model has no memory` 是實用簡化：每個 generation 應自帶完整 state；不能用它否定平台可能存在的 reference conditioning 或 session features。

## 第 10 頁 - 09 Motion

### 直接內容

三段 motion grammar：一個 named camera move、一個在 scene 中真正發生的 event、顯式 `no frozen figures`。其餘 constraints 優先正向寫 `stable picture, sharp clarity`，而不是大量 negative stack。

Prompt laws 包括：one verb per shot、以 blink/sip/look-up 等 small actions 取代抽象 emotion、T2V 120-280 words/I2V under 80、one action/one emotion、one physics cue、closing pose hold。右欄列高風險操作（pick up、button、lace、uncap、transformation），主張每個 state change across cut；shot N 的 last frame 作 N+1 reference；可用 timestamp 控 single generation 的 wide/push-in/close-up/reveal。最後要求 beat 間改 room/framing，lived-in set 勝過過度整潔。

### 可執行映射

```text
Camera: one named move + direction + speed + focus target.
Primary event: one causally complete event.
Subject micro-motion: 2-4 cues that support the event.
Physics cue: one secondary motion with a visible cause.
End state: pose, prop state, gaze, camera position held for handoff.
```

「one verb」與「five small actions」看似衝突，可操作解讀為：一個 primary causal event，外加少量不改變 state 的 micro-behaviors；不要同時要求多個需要不同物理/手部狀態的主要動作。

### QC

檢查 camera 是否照寫、主體是否只站著、event 是否有因果、physics cue 是否合理、state change 是否在 cut、hand/object 是否 duplicate、末幀是否可作 handoff。最後一幀若當下一鏡 anchor，需另記 pose/orientation/prop ownership/light/motion vector。

### 待交叉驗證

字數 120-280/80 與「cannot fasten/uncap」是作者工作範圍的 heuristic/失敗觀察，不是官方 hard limit；模型/輸入/版本改變時要重新測。

## 第 11 頁 - 10 Iteration Loop and Edit

### 直接內容與圖表補全

**視覺圖表內容**把 shot 放在 loop 中央：Generate -> Watch -> Diagnose -> Log pass -> Change one variable -> Regenerate。Stop rule：10-15 passes 還不落地就不是 wording 問題，應拆 shot、drop action 或 change angle。每 pass 要記 version/change/result/keep；resolution ladder 是 low-res 多探索、high-res 少量 keeper、最後只在 finished cut upscale 一次。

Acceptance checklist 六項：references、artifacts、camera、dialogue/lip-sync、continuity with neighbors、palette。通過後 accepted take 才進 `/selects/`，editor 不碰 raw generations。Frame check 從 finished cut 抽 16 個 evenly spaced frames，查 limbs/fingers、object permanence、label text、background continuity、device leaks；它會把 intentional cuts 也標異常，因此只能 measure broken，不能 judge good。Edit law：首尾半秒 drift 要 trim、action 常拖延要 aggressive cut。

下方文字再要求 joins 檢查 eye-line/axis/size/light；cut list 可是可重現的 text file + ffmpeg；honesty cut 刪除無聊 clip；平台 AI disclosure 要在 upload 流程處理。

### 可執行映射

Iteration log 最少欄位：`shot_id`、`take`、`prompt_hash`、`references_hashes`、`one_changed_variable`、`result`、`failure_category`、`keep/kill`、`next_action`、`render_time/cost`。

停止決策樹：

1. 第一次 fail 先分類 adherence/identity/motion/physics/text/audio/editability。
2. 每 pass 只改與分類直接對應的一個欄位。
3. 同類 fail 連續出現且到 10-15 pass，停止 wording 微調；改 shot architecture。
4. 拆 shot 或把高風險 state change 移到 cut，再從新 shot ID 開始。

### QC

16-frame sampling 適合查稀疏 artifact，但嘴型、快速手部動作、短暫文字錯誤仍需逐幀或更高 sampling。Acceptance 要與 neighbors 一起評，不能只評單 clip。Upscale-once 是成本/一致性策略，若最終 VFX/文字 overlay 需要高解析 pipeline，仍應依交付規格調整。

## 第 12 頁 - 11 UGC Factory

### 直接內容

頁面宣稱 factory 從 customer language 開始。Winning patterns：named enemy、live physical proof、authority from exhaustion、one checkable detail、先 reviews/comments 後 competitor ads。Script math：每 clip <9 秒、3.5 words/sec、hook 用 offer/confession/call-out、one message/CTA last、tear-down 分 persuasion record 與 capture record。

1:1 shortcut 是對已轉換的 UGC 做 timestamped breakdown，再換 product 與 judged script。Factory run：先單獨 render hook 判 face/voice，抽 hook audio 作 anchor，之後 same sheet/product still/anchor 的 clips 平行送出，尊重 concurrency cap；raw generation 再加真產品 b-roll、screen recording、captions、sound。

### 可執行映射

- Research record：原句 customer complaints、頻率、情境、proof、objection、CTA；每項保留來源。
- Script gate：one belief、one named enemy、one live proof、CTA final、實測朗讀時長。
- Hook gate：先生成並 approve identity/voice；失敗時不啟動 batch。
- Batch template：共享 locked passport/product/voice，只有 room/framing/beat dialogue 等允許欄位不同。
- Edit plan 在 generation 前就建立 b-roll/caption/UI/sound task，不把 raw clip 當 final ad。

### 待交叉驗證

「human ads still won」「only about a quarter could tell」沒有研究名稱、樣本、方法或引用，不能當研究事實。任何下載 competitor UGC 的流程也必須遵守版權、平台條款與使用授權。

## 第 13 頁 - 12 Format Recipes

### 直接內容

四個主要 recipe 加一個跨格式 lighting recipe：

- K-pop：hard cut 對 snare/drop、中心對稱、portal/dolly-back、單一 saturated palette、medium close-up lip-sync、one dance move per cut。
- Vlog：handheld micro-jitter/arm's-length/body sway、available light、cut on movement、mic cable/hair/direct lens gaze 等 giveaway details。
- 3D product：用物理材質詞、360 orbit 與 pull-back 分開、softbox/rim/specular sweep、infinite backdrop/AO/lifted blacks。
- Animation：只選一個 era/style、character on twos vs smooth camera、painterly texture、單一 palette family。
- Realistic lighting：warm key/cool fill、close specular/distant haze、rim hair、sun flare、bounced shadow color、atmospheric perspective。

### 可執行映射

每個 format recipe 應成為選一個的 preset，而不是把五種混在一 prompt。Preset 只填 global style/camera/edit/audio defaults；shot 的 subject/event/continuity 仍逐鏡明寫。對 music video，cut map 應由音樂 beat grid 驅動；對 vlog，movement cue 驅動 cut；對 product 3D，材質/lighting QC 優先；對 animation，frame cadence 與 camera cadence 分開。

### QC

檢查 recipe purity、palette drift、cut motivation、lip-sync framing、material response、frame cadence、light direction與 atmospheric perspective。這些是 taste patterns，不是 Seedance 專屬功能清單。

## 第 14 頁 - 13 Full Production Pipeline

### 直接內容與圖表補全

**視覺圖表內容**列出 11 stages：

1. Breakdown：每 shot 是 22-column card，含 scene ID、asset tags、verbatim dialogue、shot goal、blocking、lens、cut type。
2. References：casting/location/prop shop 變成固定 reference file；new version is a new file。
3. Visual bible lock：資產繪製前先鎖 look；locked once, not renegotiated。
4. Asset sheets：每 character/variant/location/prop 一張 sheet。
5. Library：每 asset 一 row，status 必須 `LOCKED`。
6. Generation：每 shot prompt 同一組 15 blocks、固定順序；圖中作者主張把 prohibition 改寫成正向 present-state，例 `exact N characters - no duplicates`。
7. Edit：N-1 組接時 N 正在 iteration、N+1 正在 shotlist，三者並行。
8. Cleanup：最後 in-house pass，出口是 picture lock。
9. Color：classic human handoff，EDL/XML + sources、no recompression，不用 regeneration 修 grade。
10. Sound：native sound 作 edit scaffold/timing anchor，human mix。
11. Master：DCP/ProRes archive，並保存 prompts/log/asset registry。

Stage 05/06 之間有 lock gate：scene 所需每個 character/variant/location/prop 都有 registry row 且 `LOCKED` 才能生成。圖下 file system：`/assets/characters`、`/assets/locations`、`/assets/props`、`/prompts`、`/generations`、`/selects`、`/edit`、`/color`、`/sound`、`/master`、`/docs`；只有 `/selects` 進 edit，reference 不覆寫，新版本新檔。

### 可執行 pipeline

```text
Gate A - Script/shot cards complete
Gate B - Visual bible approved
Gate C - Asset registry 100% LOCKED for the scene
Gate D - Prompt assembled from versioned cards/passports
Gate E - Take acceptance + neighbor continuity
Gate F - Picture lock
Gate G - Human color/sound handoff
Gate H - Master + reproducibility archive
```

Generation queue 要以 scene dependency graph 排序；N render、N-1 edit、N+1 shotlist 可並行，但同一 asset 未鎖不能跨 gate。每個 shot 的 prompt/reference/model/parameter/take/status 都要可由 archive 重建。

### 待交叉驗證

「first feature-length AI film shown at Cannes」沒有片名、年份、場次或引用，不能寫入研究報告的事實層。15-block prompt 與模型每六個月改變也屬作者 pipeline 說法，不是 API 規則。

## 第 15 頁 - 14 Master Checklist

### 直接內容

四區 checklist：

- Before writing：script judged/count、one message/CTA、reference images locked、character headshot+fullbody+fixed imperfection+closed wardrobe、product still/exact label/brand big、asset stress test。
- Inside prompt：four timed beats/six details/exact dialogue、每 ref job+do-not-touch、camera/light/grade 分開、subject/camera movement 分句、audio block、scene-wide count、no scripted grasp、state changes across cut。
- In loop：hook first + audio anchor、single variable、log、10-15 stop/simplify、acceptance refs/artifact/camera/lip-sync/neighbors。
- After render：trim edges/aggressive cut/join eye-line+axis、16-frame check、captions/b-roll/sound post、honesty cut、AI disclosure。

### 可執行總 gate

這頁可以直接做 production checklist 的人工 UI，但每一項要能連到 artifact：script word count、asset registry row、prompt section、generation log、QC report、edit decision list、disclosure record。`checkbox=true` 不足以驗證，應附檔案路徑、版本與 reviewer。

### 完成判準

一個 shot 只有在下列都成立才可進 `/selects`：

1. Prompt adherence、identity/prop/location continuity、motion/physics、text/audio、artifact、editability 均過門檻。
2. 與前後鏡的 axis/eye-line/scale/light/motion-vector continuity 通過。
3. Prompt、references、model/params、take、成本/時間與 acceptance evidence 可重建。
4. 任何需後製的 text/audio/VFX task 已在 edit backlog，有 owner 與完成條件。

---

## 全書交叉結論

### 可直接採納為流程骨架

- 先 lock assets，再 generation。
- 每 reference 有 job + exclusions；passport verbatim 且 versioned。
- 30 秒用 stages/beats 和 end states，不用一個長段落。
- Camera、subject event、light、grade、audio 分欄寫。
- 高風險 state change/hand-object interaction 跨 cut。
- Hook/anchor first、single-variable iteration、acceptance + neighbor continuity、picture-lock 後 human color/sound。
- 原始 generation、selects、edit、master 與 reproducibility archive 分層。

### 只能標為 D 的 production heuristic

- 3.5 words/sec、T2V 120-280 words、I2V under 80、10-15 iterations、16 frames、10/10 stress test。
- 特定工具與 taste recipe。
- 模型「不能」做某類手部/變形的絕對說法。
- consumer testing、Cannes film、generated music licensing 等未附引用的敘述。

### 必須由 A/B/平台文件決定的模型事實

- 正式模型名稱與 model ID。
- 1080p、duration、ratio、input limits、locked/unlocked task parameter rules。
- 支援的 reference role/tag、audio/edit/extension/first-last-frame 語法。
- API 與 UI 的實際參數、格式與可用平台。

因此，本 Creative Bible 最有價值的是 production system 與 failure-aware workflow；它不能單獨替代官方 capability/parameter 文件。

