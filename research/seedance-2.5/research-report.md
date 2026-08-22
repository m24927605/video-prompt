# Seedance 2.5 高品質 Prompt 與長篇 AI 電影研究報告

> 研究基準日：2026-08-22（Asia/Taipei）  
> 狀態：跨來源整合版；除明標 `官方事實`、`直接 UI／影片觀察` 或 `專案作者自述` 者外，本文的公式、長片架構、三種操作模式、後期分流與失敗診斷順序一律視為 `實務建議／未經本專案付費生成驗證`，不是模型保證或已證明最優解。

## 執行摘要

### 最重要的答案

1. **最好的 prompt 不是形容詞最多，而是最像可驗收的 shot contract。** 它先明示 task，再綁定每個 reference 的工作與禁用範圍，接著定義主體、起始狀態、唯一主要變化、結束狀態、空間、鏡頭、光色、聲音與整鏡不變項。
2. **Prompt 無法替代模型能力、參考素材或後期。** 來源 A 明確提醒：prompt 能降低歧義並提高 instruction following、素材一致性與可控性，但不能保證物理、真人或複雜攝影一定成功。[來源 A 原始頁](https://bytedance.larkoffice.com/docx/A88jd0B47oAd8zxWp5ycZFMfnxh)、本機全文 [archive: `sources/lark/structured.md`] ByteDance 發布文另指出複雜動作的物理合理性與多主體互動穩定性仍有改善空間。[官方發布文](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)
3. **長片不能靠一個超長 prompt 或無限 extension。** 可執行架構是 `Film → Sequence → Scene → Beat → Shot`，配合 canonical asset bank、per-shot entity schedule、continuity state、核准 keyframe memory、shot handoff、版本 ledger、剪輯與後期。
4. **品質最高與速度最快不能無代價同時最大化。** 品質模式把更多時間放在資產、previz、hero shots、多 reviewer 與後期；速度模式先做完整 blocking cut、平行生成獨立低風險鏡頭、只升級故事瓶頸；實務上最推薦混合流程。
5. **資料足夠完整的 Higgsfield project briefs 最強的共同點，是把不確定性移到生成前。** 這些 briefs 反覆自述使用命名資產、固定 descriptor/style/voice blocks、狀態版本、位置圖、storyboard、prompt skeleton、逐鏡資料夾、單變因 retry，以及由粗剪反向要求 pickups；不代表九案每案都公開了同等細節。

### 一句話公式

```text
TASK + ASSET CONTRACTS + ONE-SENTENCE INTENT + GLOBAL INVARIANTS
+ STAGED VISIBLE EVENTS + CAMERA + LIGHT/STYLE + AUDIO
+ END STATE / EDIT SCOPE + ACCEPTANCE CONDITIONS
```

## 1. 證據分層與版本 gate

本文採六種標籤：`官方事實`、`直接 UI／影片觀察`、`專案作者自述`、`團隊推論`、`實務建議`、`未知／待驗證`。前兩者可直接核對頁面或影片；作者對流程、成效、時間、成本與影展的敘述一律單獨標示，不當成本研究的直接觀察或受控實驗。

主要來源的原始／本機對照如下，細部檔案、取得方法、時間、雜湊與缺口見 [source-manifest.json](source-manifest.json)：

| 來源 | 原始來源 | 完整本機擷取／結構化證據 |
|---|---|---|
| A | [Lark 原始文件](https://bytedance.larkoffice.com/docx/A88jd0B47oAd8zxWp5ycZFMfnxh) | 完整結構化全文 [archive: `sources/lark/structured.md`]、取得與完整性說明 [archive: `sources/lark/README.md`] |
| B | [BytePlus 原始文件](https://docs.byteplus.com/en/docs/ModelArk/2607689) | 使用者提供完整 Markdown [archive: `../../seedance2.5-prompt-guide.md`]、完整本機化全文 [archive: `sources/byteplus/structured.md`]、取得與 72 個媒體說明 [archive: `sources/byteplus/README.md`] |
| C | [Higgsfield Studio projects](https://higgsfield.ai/@higgsfield.studio/projects) | [九案完整研究](higgsfield-nine-projects.md)、索引 [archive: `higgsfield/projects-index.json`]、媒體清冊 [archive: `higgsfield/media-inventory.json`] |
| D | 專案原始 PDF [archive: `../../seedance-25-creative-bible.pdf`] | 保存副本 [archive: `sources/creative-bible/seedance-25-creative-bible.original.pdf`]、[逐頁分析](creative-bible-analysis.md) |

### 1.1 Seedance 2.5 是正式模型

- `官方事實`：ByteDance Seed 於 2026-07-31 正式發布 Seedance 2.5。[官方發布文](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)
- `官方事實`：BytePlus ModelArk 目前列出 model ID `dreamina-seedance-2-5-260628`。[官方 tutorial](https://docs.byteplus.com/en/docs/ModelArk/2607688)
- `官方事實`：發布當日 BytePlus API 尚寫 coming soon，後續 API 文件已上線。這是日期差異，不是矛盾。

版本稽核細節見 root-version-gate.md [archive: `worknotes/root-version-gate.md`]。

### 1.2 平台能力不可互換

| 面向 | BytePlus ModelArk | BytePlus LAS Enhanced | 結論 |
|---|---|---|---|
| Model ID | `dreamina-seedance-2-5-260628` | 同 ID | ID 相同不代表 surface 相同 |
| Resolution | 480p、720p、1080p；1080p 10-bit HEVC | 480p、720p | 1080p 不得外推 LAS／Higgsfield |
| Duration | 4–30 秒或 `-1` | 4–30 秒 | 依 task 與 endpoint 驗證 |
| Ratio | 六個固定畫幅加 `adaptive` | 依 LAS schema | 不依賴未明設 default |
| Format | MP4、MOV | MP4 | Editing／extension 的 MOV 建議是 ModelArk 路徑 |
| Audio | `generate_audio` 預設 true；輸出為 mono | audio-video generation | 長片仍需專業聲音後期 |

完整 API 與 defaults 差異見 [additional-findings.md](additional-findings.md)。

### 1.3 Higgsfield 九案的版本邊界

- P02 Red Flag 的 brief 與已開啟 generation UI 都明示 Seedance 2.5，是九案中最強的 asset-level 2.5 證據。
- P04 ZEPHYR: Special 的 brief 明示 Seedance 2.5，但本研究抽查的 generation UI 只顯示 `Seedance 2`；因此只能將它視為 brief-level 2.5 workflow claim，不能當成 2.5 輸出品質證據。
- P07 ZEPHYR 與 P08 HELL GRIND 的 briefs 明示 Seedance 2.0；P09 成片有 `SEEDANCE2.0 4K` 剪輯圖樣，但不是 backend model ID。
- P01 抽查資產的 UI 只顯示 `Seedance 2`；P03、P05、P06 只能確認 generic Seedance，精確版本視為 `unknown`。

因此，九案可以支撐 Higgsfield 作者對製作流程與 prompt 寫法的一手自述，但只有 P02 同時有 brief 與抽查資產的 2.5 標籤；P04 只能稱為 brief-level 2.5 案例。兩者都不是受控模型評測。詳見 root-higgsfield-cross-case.md [archive: `worknotes/root-higgsfield-cross-case.md`]。

## 2. Seedance 2.5 經證實的能力與限制

### 2.1 能力

`官方事實`：指定指南與 ModelArk 文件支持：

- 單次最長 30 秒。
- Text-to-video、first-frame、first-and-last-frame。
- 圖片／影片／音訊的 omni reference 與組合 reference。
- Subject、motion、style、audio、storyboard、independent keyframe、coarse/fine clay/blockout reference。
- Video instruction editing、reference-image editing、audio editing。
- Forward/backward extension、one-click video、seamless transition。
- 整秒 timestamps；ModelArk tutorial 文件化 11 種音訊語言，其他平台需另驗。
- 最多 30 圖、10 影、10 音，合計最多 50 項 reference。

One-click video 與 seamless transition 是 prompt guide 中的工作流名稱，不是可自行填入 `omni_reference_task_type` 的 enum；該 API hint 目前只文件化 `auto/reference/edit/extend`。

來源：[A 原始頁](https://bytedance.larkoffice.com/docx/A88jd0B47oAd8zxWp5ycZFMfnxh)與完整本機版 [archive: `sources/lark/structured.md`]、[B 原始頁](https://docs.byteplus.com/en/docs/ModelArk/2607689)與完整本機版 [archive: `sources/byteplus/structured.md`]、[ModelArk tutorial 原始頁](https://docs.byteplus.com/en/docs/ModelArk/2607688)與本機擷取 [archive: `sources/supplemental/byteplus-modelark-2607688-tutorial.extracted.md`]。

### 2.2 上限不是品質甜蜜點

`官方事實`：官方 guide 建議 subject image 常以 1–8 主體較穩；subject audio/video 常以 1–5 主體、5–10 秒較穩；video edit 以 20 秒內、1–5 張 reference images 較穩；storyboard 常以 15 panels 以下較適合。超過建議範圍可以嘗試，但穩定性可能下降並需要更多 runs。

`實務建議`：從完成任務所需的最小 reference set 開始。新增素材前先回答：「它提供的資訊是否已存在？它是否會和另一素材競爭人物、構圖、場景或風格？」

### 2.3 重要限制

- Timestamps 是 event budgets，不是 frame-accurate edit points。
- Storyboard grid 提供高層 plot／shot structure，不保證逐格還原；獨立 keyframes 較嚴格但仍不是 pixel lock。
- Edit output 的時長可能和 input 有少量差異；官方 guide/tutorial 對保守界線分別出現約 0.3/0.4 秒，必須 probe 實際 frames。
- First/last-frame task 鎖首幀畫幅；首尾同畫幅仍是最安全做法。A/B prompt guides 警告 mismatch 可能拉伸尾幀，ModelArk create-task API 則寫會以首幀為準裁切尾幀；實際行為須按 endpoint/version probe。
- Seamless transition 與 extension 追求 AV continuity，不保證 pixel-identical seam。
- 同 request + 同 `seed` 只產生相似結果，不保證完全一致。
- 官方承認複雜物理與大量主體互動仍是弱點。

## 3. 高可控 Prompt 的正確寫法

### 3.1 先路由 task

在第一行明示 generate、reference、edit 或 extend。ModelArk 的 `omni_reference_task_type` 可選 `auto/reference/edit/extend`，但它只是 task hint；prompt 意圖不一致仍會失敗。

| Task | Prompt 起手式 | 參數 gate |
|---|---|---|
| T2V | `Generate ...` | 依支援值明設 ratio/duration |
| Reference | `Generate a new video using ... only for ...` | Reference role 與 task hint 一致 |
| Edit | `Edit @Video 1. Only change A to B ...` | ModelArk `ratio: adaptive`, `duration: -1` |
| Extend | `Extend @Video 1 forward/backward by N seconds ...` | ModelArk `ratio: adaptive` |
| First/last | 用 `content.role` 明確指定 | `ratio: adaptive`；首尾同畫幅 |

`官方事實／執行硬限制`：ModelArk 嚴格 `first_frame/last_frame` task 不能和 omni references 混用。若必須同時加入其他 references，改用 `reference_image` 並在 prompt 描述哪些圖是首／尾，但它屬 unlocked、近似對齊，不是 role-based 的嚴格首尾幀 task。

### 3.2 每個 reference 都是一份合約

至少寫兩件事：它控制什麼、它不控制什麼。

```text
@Image 1 defines Character A's face, hair and clothing.
Do not use its background or composition.

@Video 1 defines only the hand action, timing and orbiting camera.
Do not use the actor identity, wardrobe, location or lighting.
```

多角色／多場景時，先逐一 mapping，再按 characters／props／locations／motion／audio 分組，為重複角色建立 centralized profile，最後逐 scene 選用 reference。不要要求所有 reference 同時出現在一鏡。

### 3.3 用「狀態」而非模糊故事

30 秒內容以連續 stages 或 timestamps 描述。每段包含：

1. 起始可見狀態。
2. 一個主要動作／事件／state change。
3. 可直接看見的 end state。
4. 鏡頭、聲音與下一段必須延續的 invariants。

```text
[Stage 2]
Continue from Stage 1: Character A still holds the same case in the right hand.
Primary event: Character B opens the paper wrap and A places the object inside.
End state: the wrapped object lies at table center; the bow faces camera.
```

這比「兩人完成包裝，畫面溫馨而專業」更可驗收，也能防止物件 ownership、位置和數量在段落間重置。

### 3.4 正確安排攝影與空間

- 常見景別、pan/track/orbit/push/pull、low angle、overhead、FPV、dolly zoom 等可直接寫。
- 少見術語須翻譯成可見效果，例如 rack focus 要寫誰從清楚變模糊、誰從模糊變清楚。
- 主體動作與 camera movement 分句；一鏡保留一個主要 camera intention。
- 多人／複雜空間把幾何外部化成 diagram、location map、depth/layout guide 或 keyframe；位置綁在可見 landmark 與 frame-left/right，而非「站在某人左邊」。
- 每鏡重申 camera side、axis、eyeline、入口出口與 end state；不要寫「same as previous shot」。

### 3.5 表演要寫成可觀察行為

`實務建議／跨案觀察`：用目標、障礙、tactic、gaze target、反應時機、呼吸、肌肉、blink、手部工作與動作停止點取代單獨的「sad/angry/realistic」。

```text
She keeps sorting the receipts while listening.
Halfway through the other line, her thumb stops on the paper.
Her eyes reach the speaker before her head turns; she exhales once, then answers.
```

這些描述同時是生成指令和 QA 條件。ONEIRIC、Cully Hill Boys、HELL GRIND briefs 都反覆使用這種方法，但其效果大小尚未受控測量。

### 3.6 音訊與對白

- 明寫 speaker、語言／地區口音、delivery、台詞、順序與誰保持沉默。
- 非中文台詞先重申語言；品牌／罕見詞可提供發音寫法。
- 來源 A 提供可選 syntax：music `(...)`、SFX `<...>`、dialogue `{...}`、subtitles `【...】`。這是 prompt syntax，不是 JSON，也不保證逐字。
- 官方明確支持 `No subtitles`、`No BGM`、`No audio` 等文字控制；截至本研究日所歸檔的 ModelArk create-task schema 未文件化獨立 `negative_prompt` JSON 欄位。其他 UI／平台必須另查。
- 長片把 generated audio 視為 timing/scaffolding；連續 ambience、music、ADR/cleanup、foley 與 mix 在 post 完成。

### 3.7 否定條件的使用邊界

`官方事實`：字幕與音訊否定有明確支持，官方示例也會用 `no flicker` 或 identity constraints。  
`專案作者自述`：Red Flag brief 表示廣泛的 `no yellow` 沒有效，改成「主色必須 cold teal-green；yellow 只允許在燈泡和掌心大小 halo」後才獲得可用結果。這是作者經驗，本研究沒有對原始 runs 做受控 A/B。

建議順序：

1. 先寫期待的正面結果與可見界線。
2. 對數量、身份、未發言者、字幕／BGM、edit scope 使用必要明確否定。
3. 同一錯誤重現後才加入針對性 ban；不要堆無限 negative list。

## 4. Edit、Extension 與長內容

### 4.1 Editing

Prompt 依序定義：sole master video、target material、A→B change、time/scope、要 preserve 的畫面／動作／聲音／timing。重申「除指定項目外全部不變」，但仍需逐幀 QC，不能把它當硬保證。

### 4.2 Extension

- Forward：先描述 source 最後一幀的 pose、prop、camera、light、motion direction，再寫新事件。
- Backward：先寫前史，再把 source 第一幀明示為 extension 的 final state。
- Additional references 只能補 identity/prop/audio，不能覆蓋 boundary frame。
- Extended output 的 volume 或 seam 可能有差異；保留 overlap/handles 並在 edit 中檢查。

### 4.3 何時不要 extension

`團隊推論`：當場景、時間、服裝、攝影語法或敘事功能明顯改變時，獨立 shot + canonical references 通常比長 chain 更可恢復。Extension 適合連續動作、相鄰環境與明確 boundary；不適合把一個已漂移的末幀無限放大成全片記憶。

## 5. 長篇電影的可執行系統

完整操作版見 [long-form-film-workflow.md](long-form-film-workflow.md)。核心如下：

```text
Concept / treatment / screenplay
  → Creative Bible and rights gate
  → Sequence / scene / beat / shot breakdown
  → Character/location/prop/voice/style canonical banks
  → Entity schedule + continuity state + shot contract
  → Previz / anchor / blocking generation
  → Final shot generation + select + quality-gated memory
  → Assembly / rough cut / pickups / VFX / picture lock
  → Color / dialogue / foley / music / subtitles / mastering
  → Archive of prompts, assets, ledgers, hashes and approvals
```

### 5.1 三種 continuity 資產

1. **Canonical bank**：人工核准的角色、場景、道具、聲音、風格真相；生成結果不能自動覆寫。
2. **Approved memory**：從已核准 shot 中挑出的少量高資訊、無瑕疵 frames；先過 fidelity gate 才晉升。
3. **Local handoff**：只服務相鄰鏡的 pose、screen direction、camera velocity、light、room tone；不能凌駕 canonical。

MovieBench 支持 movie/scene/shot hierarchy；StoryMem 與 EntityBench 支持 keyframe memory、per-entity bank、entity schedule 與 fidelity gate 作為值得測試的架構，但它們不是 Seedance 2.5 內建功能。直接證據與推論邊界見 長片證據筆記 [archive: `worknotes/root-long-form-evidence.md`]：MovieBench 為 CVPR 2025 論文，StoryMem 與 EntityBench 在本研究中依據的是 arXiv 預印本，它們支持設計假說，不是對 Seedance 2.5 的直接驗證。

### 5.2 每鏡必備資料

- Narrative purpose、起始 state、唯一主要 delta、結束 state。
- Required/forbidden entities 與 passport 版本。
- 空間、axis、screen direction、eyeline、entrance/exit。
- Camera、look、sound、references、prompt、parameters。
- 硬 gate、1–5 rubric、neighbor compatibility、retry/route rule。
- Prompt hash、input/output hashes、run ID、reviewer、decision、實際時間與成本。

### 5.3 為什麼先剪再追求完美

`專案作者自述`：Cully Hill Boys 與 HELL GRIND 明確表示 editing 與 generation 平行；ADILIADA 與 ONEIRIC 則描述 `assembly → rough cut → generation supervision → fine cut → picture lock` 的迭代回路，但未同樣明說全程平行。實務上，剪輯可提早找出 coverage hole、重複 beat、缺 reaction／insert、節奏拖沓與無法銜接的 hero shot；但這些案例是流程自述，不證明因果或最佳重疊比例。

## 6. 品質最大化、速度最大化與推薦混合

### 6.1 品質最大化

- 完整 bible、rights、location maps、entity schedules、color/sound scripts 先鎖。
- Hero／複雜鏡先做 keyframe、diagram、clay 或 feasibility test。
- 使用實際平台可用的最終規格；至少兩位 reviewer 對 hero shot 盲評。
- 每鏡做 intra-shot、prompt fidelity、cross-shot continuity、neighbor cut 四層 gate。
- Picture lock 後完整 cleanup/VFX/color/ADR/foley/music/subtitle/master QC。

代價：較高資產成本、重試、協調與後期時間。

### 6.2 速度最大化但守品質底線

- 只先鎖主角、主要場景、關鍵道具與 camera/color/sound 最小 bible。
- 先完成 animatic 和一版 end-to-end blocking cut。
- 獨立低風險 shots 平行；相依或 identity-critical shots 序列化。
- 首輪每鏡先一個候選；只升級真正阻擋故事的 A/B shots。
- 文字、字幕、clean plate、局部瑕疵、轉場與 sound 優先 route 到成熟後期工具。
- 同一 hard defect 重現後改 input／asset／angle／coverage，不做無限 prompt retry。

不可放寬：故事 beat、身份、必備 entities、方向、道具 state、可理解聲音、blocking artifact=0 與 delivery spec。

### 6.3 推薦混合流程

1. 全片先 working end-to-end。
2. 用「敘事價值 × 技術風險」分 A/B/C shots。
3. A 用品質流程；B 標準 reference/QC；C 快速平行。
4. 先修 script／coverage／continuity，再修像素。
5. 只升級觀眾可見的瓶頸，跨層 hard gates 不變。

這是目前證據最支持的起始政策，不是未實測前的絕對最優。正式比較見 [future-evaluation-plan.md](future-evaluation-plan.md)。

## 7. 品質與效率 KPI

### 品質

- Prompt/story beat adherence。
- Human identity/anatomy/clothing fidelity。
- Character/location/prop/voice/style cross-shot continuity。
- Temporal stability、motion rationality、contact/physics、object permanence。
- Camera、composition、lighting、sound 與 lip-sync。
- Artifact rate、editorial usability、neighbor compatibility。

### 效率

- First-pass approval rate。
- Median/P90 retries 與 time per approved shot。
- Usable seconds/hour。
- Cost per approved second。
- Human correction time、queue wait ratio、waste rate。

不要用生成速度或每秒價格單獨代表效率；如果輸出不能進 cut，便宜快速仍是浪費。

## 8. 失敗診斷順序

1. **Task/parameters 錯**：先修 role、hint、ratio、duration、format。
2. **Reference 衝突**：刪冗餘、重寫 mapping、拆 role、重建弱 asset。
3. **身份／數量／state 漂移**：用 state variant、canonical descriptor、entity schedule、visible count。
4. **空間／camera 錯**：縮小場景自由度，加入 landmark、map/diagram、axis 與 end state。
5. **動作／物理錯**：一鏡一主要變化；把困難 physics 放進 input/keyframe/blockout；拆鏡或 VFX。
6. **表演僵硬**：給 eyes/hands 任務、reaction timing、breath/muscle cues；避免只寫 emotion。
7. **聲音／文字錯**：明示 speaker/language/audio；必要時 silent generation + 合法 post；精確文字後期合成。
8. **相鄰鏡接不上**：檢查 state、screen direction、eyeline、camera velocity、light、room tone；補 cutaway／handoff。
9. **同錯反覆**：停止重寫同一 prompt，改 asset、angle、coverage 或 route。

## 9. Creative Bible 的價值與限制

本機 D 原始 PDF [archive: `../../seedance-25-creative-bible.pdf`] 是 MACHINA 依四次 production runs 整理的 15 頁實戰文件，不是官方模型卡。它提供有價值的 production heuristics：six details、timed beats、asset passports、style contract、voice blocks、consistency gates、motion grammar、single-variable loop、parallel edit、11-stage pipeline 與 master checklist。[逐頁分析與 caveats](creative-bible-analysis.md)

必須保留的 caveats：

- 1080p 已由 ModelArk 文件證實，但不能外推 LAS。
- 3.5 words/second、120–280／80 words、10–15 retries、16-frame check 等是 production heuristics。
- 「逐字說稿」「不能完成某動作」等絕對語句應改成高風險觀察。
- 音樂授權、廣告 disclosure、Cannes feature 等主張需各自一手來源後才能當規範或事實。

完整逐項稽核見 root-creative-bible-claim-audit.md [archive: `worknotes/root-creative-bible-claim-audit.md`]。

## 10. 額外發現與研究限制

23 項額外發現已整理於 [additional-findings.md](additional-findings.md)，包括：平台 defaults、task mismatch、first/last 的雙重語義、edit 時長文件差異、MOV/HEVC、seed 非決定論、末幀錯誤累積、mono audio、真人權利限制、短期 URL 保留、官方 skill 的 supply-chain 邊界，以及 Higgsfield 九案揭示的 input-first physics、rolling edit、版本標籤、aggregate-metric 限制與 prompt timestamp 不等於輸出時長保證。

本研究限制：

- 未經授權啟動任何付費生成，故不能宣稱某 prompt 或流程已由本專案證明最優。
- Higgsfield project briefs 是製作團隊自述；頁面標籤、數值、prompt 內文與影片時碼才是本研究的直接 UI／影片觀察。兩者都不是 controlled experiment。
- 大量 aggregate asset/generation counters 未逐項檢查，不會冒充逐資產研究。
- Higgsfield 已實際開啟 9/9 專案與 14 支媒體；9/9 published cuts 都有啟動、代表性中段／高風險段與 terminal UI 證據。P05 有多個中段時碼，P06/P08 另補查 57:09/85:06 與 47:47/71:09；5/5 generation outputs 均有首中近尾 coverage。直接標示 `Seedance 2.5` 的 P02-A01-V01 已由網站正常 Download 保存並通過 hash、全檔 decode、AAC stream、waveform 與粗粒度 speech-window/mouth-motion gate；粵語文字正確性、聲音自然度與 phoneme 級 lip-sync 仍明列 `unknown`。完整 AV 稽核與邊界 [archive: `worknotes/p02-generation-audio-lipsync-audit.md`]
- A 的匿名頁面沒有正式匯出選項，因此以完整 browser capture 保存，不偽稱 official export。
- B 的 SSR、完整 Markdown 與 72 個正文媒體已完整保存。使用者後續提供的 `seedance2.5-prompt-guide.md` 與網站 `MDContent` 歸檔只差一個結尾換行，並明確指示研究該檔即可；故 B 以使用者修訂 [archive: `goal-amendment-2026-08-22.md`]驗收。Computer Use 另成功查閱 remote live top/opening 與 outline 至 `Summary`，但未做 full middle/bottom live scroll，故只宣稱 partial live inspection。頁面公開的 official `PDFURL` 在取得時為 DNS NXDOMAIN，官方 PDF 仍缺。
- 模型、平台、價格與政策會更新；每次 production run 前需重新通過 version/platform gate。

## 11. 立即可採用的決策

1. 以 [prompt-playbook.md](prompt-playbook.md) 的 task routing 與 shot schema 起步，不用自由散文。
2. 為每個重複 entity 建立文字＋圖像 passport；每個 state 另版本。
3. 多人／複雜空間先做 diagram/location map/keyframe，不把全部負擔塞入文字。
4. 所有 shot 寫 end state、acceptance gate 與 route rule。
5. 先做一個完整 scene 的 pilot，再擴至整片；先完成 rough cut，再升級 hero shots。
6. 以 [future-evaluation-plan.md](future-evaluation-plan.md) 做固定 seed 配對、多 seed、盲評與 Pareto 驗證後，才更新 production policy。

## 12. 研究產物索引

- [完整 Prompt Playbook](prompt-playbook.md)
- [長篇電影工作流](long-form-film-workflow.md)
- [未來受控評測計畫](future-evaluation-plan.md)
- [額外發現](additional-findings.md)
- [Creative Bible 逐頁分析](creative-bible-analysis.md)
- [Higgsfield 九案研究](higgsfield-nine-projects.md)
- Higgsfield 九案索引 [archive: `higgsfield/projects-index.json`]
- Higgsfield 媒體清冊 [archive: `higgsfield/media-inventory.json`]
- [來源 manifest](source-manifest.json)
