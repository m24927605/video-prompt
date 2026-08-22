# 長篇 AI 電影製作工作流

> 狀態：未經本專案付費生成實測的可執行設計。  
> 結論強度：這是截至 2026-08-22 由官方文件與一手研究支持的流程候選，不是已證明的絕對最優流程。

## 0. 核心結論與證據邊界

長片不是「一個超長 prompt」或「不斷延伸同一支影片」。可恢復的最小系統是：

```text
故事／Creative Bible
        ↓
Sequence → Scene → Beat → Shot contracts
        ↓
Canonical asset bank + continuity state + per-shot entity schedule
        ↓
Generate / select / retry / route-to-VFX（每鏡獨立可驗收）
        ↓
Rough cut → pickups → VFX → sound → subtitles → final QC
        ↓
版本化 checkpoint、可回退的核准資產與 provenance ledger
```

### 0.1 什麼是產品證據，什麼不是

| 類型 | 能支撐的結論 | 不能支撐的結論 |
|---|---|---|
| `官方事實`：Seedance 2.5 發布文、BytePlus 2.5 prompt guide／tutorial／API | 單次最長 30 秒、reference／keyframe／storyboard／clay／edit／extend 類能力、整秒 timestamps、task-specific 參數與平台差異。 | 不能推出長片會自動保持角色、成功率、成本、平均重試數或「延伸到數分鐘必定無漂移」。[官方發布文](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)也承認複雜物理與極多主體互動仍有改善空間。 |
| `同行評審論文`：MovieBench（CVPR 2025） | 長片可用 movie／scene／shot 階層、角色圖像與聲音 bank、shot-level 人物／情節／camera／字幕／audio annotation。本機 PDF p.3–4 [archive: `sources/supplemental/cvf-cvpr2025-moviebench.pdf`] | 不代表 Seedance 2.5 內建這套資料結構。 |
| `一手預印本`：StoryMem、EntityBench | quality-gated keyframe memory、per-entity bank、per-shot character/object/location schedule、跨 shot fidelity gate 是值得測試的方法假設。StoryMem PDF p.6–10 [archive: `sources/supplemental/arxiv-2512.19539-storymem.pdf`]、EntityBench PDF p.5–6 [archive: `sources/supplemental/arxiv-2605.15199-entitybench.pdf`] | 不是 Seedance 2.5 的官方機制；預印本結果也不能直接外推到商用閉源模型。 |
| `一手評測研究`：VBench-2.0 | 美感以外要檢查 human fidelity、controllability、physics、commonsense、instance preservation 與 multi-view consistency。本機 PDF p.2、p.8 [archive: `sources/supplemental/arxiv-2503.21755-vbench-2.0.pdf`] | 自動 metric 不能替代剪輯、敘事與人類盲評。 |

`團隊推論`：將這些證據組合後，最安全的長片架構是「短 shot 生成 + 外部狀態管理 + 核准 anchor + 分層 QC」，而非信任模型有無限長的隱性記憶。

## 1. 版本 gate 與 project charter

開案時建立 `PROJECT-CHARTER`，鎖定：

- 平台、顯示模型名稱、API model ID、文件更新日與地區。
- 片長、畫幅、master frame rate、交付 codec／color pipeline、聲音格式、字幕語言。
- 生成與後期的預算／時限；是否允許付費生成（本研究階段不允許）。
- 肖像、聲音、音樂、字型、故事與 reference 的權利鏈。
- 風險等級：未成年人、真實人物、武器、品牌、醫療／政治等需額外審核。
- 三種操作模式中的一種：品質最大化、速度最大化但守品質 gate、推薦混合。

`官方事實`：截至本研究日，BytePlus ModelArk 的 2.5 model ID 為 `dreamina-seedance-2-5-260628`。ModelArk 文件列 480p／720p／1080p；LAS 只列 480p／720p，故規格表必須以**實際平台**為準。[官方 ModelArk tutorial](https://docs.byteplus.com/en/docs/ModelArk/2607688)、[LAS 文件](https://docs.byteplus.com/en/docs/byteplus_las/video_gen_enhanced)。

## 2. Creative Bible：長片的 source of truth

Creative Bible 不是氣氛板，而是所有 shot contract 的不變約束。每個項目要有唯一 ID、版本、owner、狀態（draft／approved／retired）與核准日期。

### 2.1 Story bible

- Logline、theme、genre contract、target audience、tone boundaries。
- Treatment、sequence synopsis、scene purpose、character arc 與不可刪的 story beats。
- 世界規則：科技／魔法、物理、社會、年代、地理、時間尺度、禁忌。
- 故事時間線與 screen time 對照；flashback／dream／montage 的視覺語法。

### 2.2 Character passport

每個 `CHAR-###` 至少包含：

- canonical 名稱、年齡範圍、體型、臉、髮、膚色、姿勢、慣用手、步態、表情範圍。
- 正／側／3/4、全身／半身、neutral／關鍵表情的核准圖；每圖標用途與不得參考的背景。
- voice passport：語言、口音、音域、語速、氣質、發音詞典、核准聲音 reference 與權利狀態。
- 衣裝狀態：`WARD-CHAR-SCENE-STATE`，含污損、濕度、破損、口袋／飾物與變更事件。
- 關係與 blocking 規則：身高差、誰站哪側、親密／衝突距離、典型 eyeline。
- forbidden drift：不能改的痣、疤、髮線、眼鏡、戒指、四肢、服裝色與配件。

### 2.3 Location passport

每個 `LOC-###` 至少包含：

- 平面圖、入口／出口、主要軸線、方位、相鄰空間、鏡頭可站位置。
- wide／medium／detail、多視角 reference；白天／夜晚、天候、破壞前後 state。
- 固定物件、材質、光源方向／色溫、反射、窗外景、環境動態與 room tone。
- 180-degree line、screen direction、eyeline map 與禁止鏡像的文字／標誌。

### 2.4 Prop、vehicle、creature 與 graphic passport

- `PROP-###` 幾何、尺寸、材質、顏色、磨損、可動部件、持有人、左右手、出現／消失事件。
- 道具狀態機，例如 `sealed → opened → blood-stained → lost → recovered`，每次 transition 只在指定 beat 發生。
- 文字／介面／招牌提供可合成的乾淨 artwork；不依賴生成模型精確拼字。

### 2.5 Style、camera、color、VFX、sound grammar

- Style key：實拍／動畫媒介、材質、detail level、禁止的「AI 油亮感」與過度 beautification。
- Camera grammar：常用焦段感、景別比例、機位高度、handheld 幅度、可用運鏡、禁止運鏡、cut 規則。
- Color script：sequence／scene palette、曝光、光源動機、日夜與情緒轉折。
- VFX grammar：粒子密度、能量顏色、物理交互、clean plate／matte／tracking 需求。
- Sound bible：角色 voice、room tone、環境、foley、音樂 motif、silence、loudness 與字幕 style。

## 3. 階層拆解與 coverage

MovieBench 將長片資料分成 movie／scene／shot；本流程在 scene 與 shot 中間加入 beat、在 movie 與 scene 間加入 sequence，形成：

| 層級 | 問題 | 必備產物 | Gate |
|---|---|---|---|
| Film | 這部片說什麼？ | treatment、script、bible、color／sound arc | 故事與權利鎖定 |
| Sequence | 一段戲的宏觀目標／轉折？ | sequence cards、情緒／資訊／節奏曲線 | 轉折與片長 budget |
| Scene | 何時何地、誰想要什麼、狀態如何變？ | scene card、floor plan、continuity state、coverage plan | 空間／角色／道具狀態可解 |
| Beat | 一個可見的行為／反應／資訊單位？ | beat list、因果、開始／結束 state | 每 beat 有敘事功能 |
| Shot | 觀眾從哪裡看到哪個 beat？ | shot contract、prompt、inputs、QC rubric | 可獨立生成／驗收／剪接 |

### 3.1 Coverage plan

每 scene 先規劃：

- Master：建立空間與人物關係。
- Singles／two-shots／OTS：表演與 eyeline。
- Inserts／cutaways：道具、手部、反應、時間壓縮與遮切。
- Establish／exit／transition：相鄰 scene 的地理與節奏。
- Handles：入點前／出點後保留可剪時間；數值由專案規格定義，不假設模型必定給足。
- High-risk split：手部交互、多人接觸、精確文字、複雜物理、長台詞與速度突變優先拆鏡或 route-to-VFX。

`實務建議`：每 shot 只有一個主要 state change；若一句描述包含三個以上 `and then`，先拆 beat，再判斷是否拆 shot。

## 4. 三類 continuity 資產，不互相污染

### 4.1 Canonical bank（永續真相）

Creative Bible 核准的 character／location／prop／voice／style reference。由人工核准，不能由一次生成結果自動覆寫。

### 4.2 Approved memory bank（生成後晉升）

每個核准 shot 可提名少量 keyframes：

- 身份與服裝清楚、無 motion blur／artifact。
- 可代表新 state、角度或場景，而非重複畫面。
- 通過單鏡品質、prompt adherence 與 cross-shot fidelity gate。
- 記錄來源 shot、timecode、crop、使用範圍與不得作 canonical 的限制。

`一手預印本證據`：StoryMem 的 semantic selection 加 aesthetic filtering、EntityBench 的 fidelity gate 都顯示「不是每個生成幀都適合進記憶」。因此本流程把它當待實測的 production policy，而非 Seedance 內建機制。

### 4.3 Local handoff（相鄰鏡暫態）

- 前鏡最後核准 frame／短動作 tail、人物位置、運動向量、camera velocity、光色、room tone。
- 只服務相鄰 continuation；不能凌駕 canonical bank。
- 硬 cut 不強迫首尾畫面一致，但仍需維持故事 state、screen direction、eyeline 與聲音連續性。

`官方事實`：BytePlus API 文件提供 `return_last_frame`，可將末幀作下一段首幀；這只是一個 transport capability，末幀仍須 QC 才能當 handoff。[API 文件](https://docs.byteplus.com/en/docs/ModelArk/1520757)。

## 5. Continuity state 與 entity schedule

每個 scene 有一份可機讀 state，每個 shot 只讀前置 state 並提交 delta：

```yaml
scene_id: SC-023
story_time: "Day 4 / 05:42"
location_state: LOC-007-dawn-rain
screen_axis: "door-to-window"
characters:
  CHAR-001:
    position: "frame-left, beside table"
    wardrobe: WARD-001-SC023-wet
    hair_makeup: HMU-001-rain-02
    emotional_state: "guarded; just heard accusation"
    held_props: [PROP-014-letter-open]
props:
  PROP-014:
    state: open
    owner: CHAR-001
    hand: right
lighting: LIGHT-SC023-dawn-window-left
audio: SOUND-SC023-rain-roomtone-v02
```

每個 shot 另有 entity schedule：

```yaml
shot_id: SH-023-040
required: [CHAR-001, CHAR-002, PROP-014, LOC-007]
forbidden: [CHAR-003, PROP-014-letter-sealed]
entrance_exit: "CHAR-002 enters rear-right at beat 2; nobody exits"
state_delta: "PROP-014 transfers from CHAR-001 right hand to table center"
```

`一手預印本證據`：EntityBench 以每 shot 的 character／object／location schedule 分開測 presence、fidelity 與 cross-shot consistency；這直接啟發上述 schema，但不證明該 schema 對 Seedance 2.5 的提升幅度。

## 6. Shot contract 與 prompt packet

每個 shot 在排隊前必須有：

| 欄位 | 內容 |
|---|---|
| Identity | `FILM-SEQ-SC-BEAT-SH`、owner、risk tier、priority |
| Narrative | scene purpose、beat、起始 state、唯一主要變化、結束 state |
| Entities | required／forbidden、角色／服裝／道具／場景 passport 版本 |
| Space | floor plan、軸線、screen direction、eyeline、entrance／exit |
| Camera | shot size、position、movement、cut／continuation、handles |
| Look | light、palette、material、weather、VFX intent |
| Sound | speaker、台詞、語言、room tone、foley、music／silence |
| Inputs | 每個 reference 檔案、role、要取／不取屬性、權利狀態、SHA-256 |
| Prompt | 使用 [prompt playbook](prompt-playbook.md) schema 的送出文字與版本 |
| Parameters | 平台、model ID、task type、ratio、duration、resolution、format、audio、watermark |
| Acceptance | 硬 gate、1–5 rubric、neighbor compatibility、route rules |
| Provenance | parent run、唯一改動、輸出 ID、本機檔、reviewer、決策 |

## 7. Anchor frame 策略

1. **先建立 canonical**：角色、衣裝、場景與 hero props 在影片生成前核准。
2. **先圖後影只用於需要之處**：身份、構圖、複雜 blocking 或精確 end state 需要時才建 keyframes；普通 cutaway 不必為流程一致性而增加資產。
3. **Storyboard 與 keyframes 分工**：多格 storyboard 是高層 plot／shot structure；官方文件說不會逐格嚴格對齊。需要更嚴時，把每格拆成獨立 keyframe 並在 prompt 第一行明示順序。
4. **首尾幀同畫幅**：first／last frame task 的尾圖畫幅若不同可能被拉伸。
5. **不要全盤接受末幀**：末幀若 identity、姿勢、光色或 motion blur 不合格，回到上一個核准 anchor；不能因它是「最新」就成為真相。
6. **長距離回歸 canonical**：角色相隔多個 shots 再出現時，使用 canonical passport + relevant approved memory；不只依靠最近一個可能已漂移的幀。

## 8. End-to-end 製作流程與 gates

### Gate 0：Development／權利與規格

- 鎖 logline、treatment、audience、format、rights、預算與排程。
- 識別不可生成／不應外包給生成模型的內容。
- **Exit**：Project charter 核准；模型／平台 gate 已記錄；無未解權利阻擋。

### Gate 1：Script／bible

- 劇本由 table read、故事／角色／可拍性 review 通過。
- 建立所有 passport 與 story time、prop／wardrobe state machines。
- **Exit**：每個不可替代 beat 有 owner；主要角色、場景、道具、聲音與風格有 approved canonical assets。

### Gate 2：Breakdown／coverage／risk

- 拆 sequence → scene → beat → shot；生成 scene cards、floor plans、entity schedules 與 coverage。
- Shot 分級：
  - `A / hero`：臉部特寫、關鍵表演、複雜物理、多角色交互、品牌／文字、長鏡。
  - `B / narrative`：重要動作與 continuity，但可由常規 reference 控制。
  - `C / connective`：establishing、insert、texture、cutaway、無身份高風險。
- 為每個 A shot 設替代方案：拆鏡、live action、3D previz、傳統 VFX、ADR 或設計改寫。
- **Exit**：每鏡只有一個主要 state change；相鄰 shot 的 start／end state 可接；高風險 shot 有 fail route。

### Gate 3：Previz／anchors

- 先以 storyboard、animatic、line-art 或簡單 clay 驗證 blocking、軸線、節奏與 camera。
- 角色／場景 canonical assets 先核准，再開始大批影片生成。
- 建立 temp score／dialogue timing，但最終聲音不綁死未鎖 picture。
- **Exit**：animatic 時長在 project budget；每鏡 reference packet 完整；沒有 prompt 與 previz 矛盾。

### Gate 4：Blocking generation

- 目的：驗證 shot 是否可讀、story beat、空間與剪輯節奏，不追求每一鏡最後畫質。
- C shots 與低風險 B shots 可先跑；A shots 先做最小動作／locked-camera feasibility test。
- 低解析度／短 duration 是否真的省成本與時間需依平台帳單實測；不得假定。
- **Exit**：rough cut 能完整講故事；缺口已標為 pickup／VFX／rewrite，不用「之後再修」掩蓋核心 beat 缺失。

### Gate 5：Final shot generation

- 只對已鎖 shot contract 發出 run；所有輸出進 `incoming`，不能直接覆蓋 approved。
- 每批按 reference packet 相同、task 相同、風險相近分組；每鏡保留 parent run 與唯一改動。
- 相鄰 continuation 依賴前鏡 approved handoff，故序列化；獨立 C shots 可平行。
- **Exit**：每個 shot 有 approved take，或已正式 route-to-VFX／rewrite／omit 並由導演核准。

### Gate 6：Dailies／selects／continuity memory

Reviewer 看完整影片，不只看 thumbnail；記錄開頭、中段、結尾、轉場與高風險 timecode。

三層 gate：

1. **Intra-shot quality**：結構、temporal stability、motion、imaging、audio。
2. **Prompt／story fidelity**：required entities、action order、camera、sound、end state。
3. **Cross-shot continuity**：identity、wardrobe、prop state、location、axis、light、audio、neighbor cut。

只有三層皆通過的幀才能進 approved memory bank。`reject` 輸出保留 provenance 供診斷，但永不作新 reference。

### Gate 7：Rough cut／picture structure lock

- 依故事與表演選片，不以單鏡炫技破壞節奏。
- 建立 temp VFX、split screen／reframe、必要的 speed change 標記；禁止隱性 time-stretch 對白。
- 檢查 sequence-level arc、shot repetition、screen direction、action cut、handles 與 scene transitions。
- **Exit**：structure lock；後續新增 shot 必須有 change request 與 downstream impact。

### Gate 8：Pickups／VFX／cleanup／conform

- Defect route：重生、局部 edit、傳統 paint／roto／key、3D／composite、reframe、插入遮切、換 shot。
- 精確文字／logo 用圖形或 VFX 合成；不要反覆重生整鏡求拼字。
- Upscale／interpolation 先保留原幀率／motion baseline，逐鏡檢查 ghosting、edge、texture crawl；工具與設定另記版本。
- Conform 到 project master；AI 檔案的 codec、frame rate、color tags、audio channels 必須正規化。
- **Exit**：VFX finals 有 plate／matte／project provenance；沒有未解 placeholder。

### Gate 9：Color／sound／dialogue／music／subtitles

- **Color**：shot match、skin／material、daylight continuity、legal range、gradient banding；ModelArk 1080p 10-bit HEVC 與 MOV 4:4:4 是不同輸出路徑，不能以容器名稱推定相同 color pipeline。
- **Dialogue**：picture lock 後 ADR／edit／mix；角色 voice passport、語言、台詞、口型與 room acoustics 一致。
- **Sound**：room tone 跨 cut、foley 接觸點、perspective、LFE／music motif、silence、loudness 與 mono 生成音的後期配置。
- **Subtitles**：由最終音訊做實際時間對齊；校對 speaker、語言、標點、換行、安全區、畫面遮擋與 burned／sidecar 規格。不可用 prompt 時間估算最終字幕。
- **Exit**：mix／subtitle QC 通過；文字、語音、畫面 cut 三者時間一致。

### Gate 10：Final QC／master／archive

- 完整播放 master；另檢查首、中、尾、每個 edit、VFX、subtitle、audio transition 與 credit。
- 技術 QC：解析度、畫幅、frame rate、codec、color、音訊通道、峰值／響度、字幕、黑場、凍結幀、drop／duplicate frames。
- 內容 QC：故事、身份、continuity、物理、文字、合規、權利、AI disclosure／watermark policy。
- 保存 master、mezzanine、stems、subtitles、project files、approved／rejected ledger、source hashes、模型／平台／文件版本。
- **Exit**：兩位不同 reviewer 簽核；所有 blocking defect 關閉或有書面 waiver。

## 9. Generation queue、平行化與 early failure

### 9.1 安全平行化

可平行：

- 不共享即時 handoff 的 establishing、insert、cutaway、clean plate、texture shots。
- 角色／場景 anchor 已鎖、彼此無 state dependency 的不同 scenes。
- 同一 prompt 的重複抽樣（future evaluation），前提是 run IDs 與輸出不混淆。
- 選片、聲音 spotting、VFX breakdown、字幕準備等不會改同一 source of truth 的任務。

必須序列化：

- extension chain、同一 continuous action、服裝／傷勢／道具狀態逐鏡演變。
- 下一鏡首幀取決於前鏡核准末幀。
- 會更新 canonical／approved memory 的操作。
- 同一 scene 的軸線／blocking 尚未核准時的 hero close-ups。

### 9.2 Batch key

批次只用相同 `platform + model ID + task type + resolution + ratio + output format + reference packet version + review rubric` 的 shots。把不相容的 task 混批會讓錯誤與品質差難以歸因。

### 9.3 Early failure order

先檢查最便宜且最致命的條件：

1. API／task constraints、輸入格式、權利與 moderation。
2. 必要人物／物件 presence、故事 beat、起／終 state。
3. identity／continuity／物理／動作。
4. camera、aesthetic、細節與聲音 polish。

任何上層 hard gate 失敗即停止對該 take 的細部打磨。

## 10. Retry、failure routing 與停止條件

### 10.1 Retry 規則

- 一次只改 prompt、reference、task parameters、shot design 其中一類的一個關鍵變因。
- 新 run 指向 parent run，記錄假設、預期改善、實際 defect 與 timecode。
- 不能用 rejected output 作 identity／location reference。
- 若 defect 是模型能力而非描述含糊，增加形容詞通常無效；拆 shot 或改 route。

### 10.2 Failure routes

| 症狀 | 第一修正 | 第二修正 | 最終 route |
|---|---|---|---|
| 人物／服裝漂移 | 清理 mapping、回 canonical、多視角改單視角 | 短化 shot／減角色／拆 reaction | 角色專用合成、live action、2D／3D替身 |
| 手部／接觸／多人互動 | locked camera、一次一動作、簡化接觸 | 分解 action／cutaway 遮切 | 傳統 VFX、3D、替代 blocking |
| 空間／軸線錯 | floor plan、screen direction、起終位置明寫 | master／insert 分生成 | 重剪 coverage／reframe／替代 shot |
| 物理／材質錯 | 描述接觸→結果、移除 camera 競爭 | clay previz／首尾幀 | simulation／composite／practical plate |
| Edit 外溢 | A→B + 時段 + preserve list | 只取 edit 區與原片拼接 | roto／paint／key／composite |
| Extension 漂移 | 回最後 approved checkpoint + canonical | 縮短新增段、改 hard cut | 新 shot 生成，不再延伸 |
| 對白／口型／聲音 | 一鏡一 speaker、明語言／台詞 | 靜音 picture + ADR | 專用 dubbing／foley／mix |
| 精確文字 | reference artwork、靜態短 hold | 後期 planar track | 直接 graphic composite |

### 10.3 停止條件

每鏡在開案時設定 project-specific retry／cost／clock ceiling；數字來自預算，不冒充模型平均值。出現任一條件就停止生成並 route：

- 同一 blocking defect 在已隔離變因的連續 retries 仍重現。
- 改善一項必然破壞另一個更高優先級硬約束，形成 oscillation。
- 累計 cost／time 已超 ceiling，且替代 route 期望損失更小。
- continuity 需要從 rejected／漂移 frame 繼續才能成立。
- 交付規格、權利或安全 gate 無法通過。

「停止」不是放棄：要留下 last approved checkpoint、defect、已排除假設與下一 route。

## 11. 角色與責任矩陣

`A` accountable、`R` responsible、`C` consulted、`I` informed。小團隊可一人兼任，但簽核角色仍要分離。

| 產物／決策 | Director | Producer | Writer | DP／Previz | Prompt／Gen TD | Continuity | Editor | VFX／Color | Sound／Subtitle | QC／Rights |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Charter／scope／budget | A | R | C | C | C | I | I | I | I | C |
| Script／story bible | A | C | R | C | I | C | C | I | C | C |
| Character／location／prop passports | A | C | C | R | C | R | I | C | C | C |
| Voice／sound／subtitle bible | C | C | C | I | C | C | C | I | R/A | C |
| Breakdown／coverage／risk | A | C | C | R | R | R | C | C | C | I |
| Shot contract／prompt packet | C | I | C | C | R/A | R | C | C | C | I |
| Generation queue／run ledger | I | C | I | C | R/A | C | I | I | I | C |
| Dailies／select | A | I | C | C | R | R | C | C | C | C |
| Canonical／memory promotion | A | I | I | C | C | R | C | C | C | C |
| Picture lock | A | C | I | C | I | C | R | C | C | I |
| VFX／color final | A | C | I | C | C | C | C | R | I | C |
| Mix／subtitle final | A | C | C | I | I | C | C | I | R | C |
| Final master／rights／archive | A | R | I | I | C | C | C | C | C | R |

任何人不得單獨核准自己產生的 final shot；至少由 continuity／editor／director 中另一角色複核。

## 12. 命名、版本與 provenance

### 12.1 Stable IDs

```text
Project:      FILM-ORCHID
Sequence:     SQ-030
Scene:        SC-030-012
Beat:         BT-030-012-04
Shot:         SH-030-012-040
Asset:        CHAR-003 / LOC-007 / PROP-014
```

ID 永不因排序而重用；重排只改 `editorial_order`。

### 12.2 檔名

```text
FILM-ORCHID_SH-030-012-040_take-003_run-r017_prompt-p004_ref-r006_model-dreamina-seedance-2-5-260628_720p_v001.mov
FILM-ORCHID_CHAR-003_passport-front34_neutral_v005_APPROVED.png
FILM-ORCHID_SC-030-012_continuity-state_v012.yaml
```

狀態是 metadata 的 source of truth；`APPROVED` 可作人類可讀輔助，但不能只靠檔名判斷。

### 12.3 Run ledger

每個 run 記錄：

- 平台、model ID、文件版本、建立／完成時間、task ID（不保存 signed output URL）。
- prompt 原文／hash、parameters、reference IDs／hash／roles、parent run、唯一改動。
- 輸出 path／hash、時長、規格、實際費用／排隊／生成時間、人工時間。
- hard gate、分項 score、timecode defects、reviewer、decision、route。
- 若 task／輸出 URL 有保留期限，立即在合法範圍下載到受控 storage 並驗 hash。

## 13. KPI 與公式

### 13.1 品質 KPI

每鏡 1–5 分，權重由 project charter 鎖定；所有 hard gates 另算，不能被加權平均掩蓋。

| KPI | 定義／量法 |
|---|---|
| Prompt adherence | required entities、story beats、動作順序、camera、sound 的逐項通過比例與 reviewer 1–5 分。 |
| Character／scene continuity | identity、服裝、道具、location、光色、聲音與相鄰鏡可接性；跨 shot 評分。 |
| Temporal stability | 無 flicker、形變、texture crawl、突然出現／消失的有效幀比例。 |
| Motion naturalness | 解剖、軌跡、速度、接觸、結果、物理／常識與 camera-motion coherence。 |
| Cinematography | 景別、機位、軸線、運鏡、focus、lighting、composition 與剪輯功能。 |
| Sound quality | 說話者、台詞、口型、環境、foley、music、同步、音量／room-tone continuity。 |
| Artifact rate | 含 blocking／major／minor artifact 的 frames 或 seconds ÷ inspected frames／seconds；須先定義 severity。 |
| Editorial usability | 可直接或僅輕修入 cut 的核准秒數 ÷ 生成秒數；另記 handles 與 neighbor compatibility。 |

`實務建議`：cross-shot continuity 先做 fidelity gate；錯角色即使每鏡都「很一致」也不得得高分。這與 EntityBench 的三層評測原則一致，但本專案閾值需自行校準。

### 13.2 速度／成本 KPI

| KPI | 公式 |
|---|---|
| First-pass approval rate | 第一次有效 run 即核准的 shots ÷ 有效首輪 shots |
| Average retries | 核准前的額外有效 runs ÷ 核准 shots；另報中位數與 P90 |
| Time per approved shot | 從 shot-ready 到 approved 的 wall-clock；另報 active human time |
| Usable seconds/hour | 核准且入 cut 秒數 ÷ 生成／review wall-clock hours |
| Cost per approved second | 該 shot 所有 billable runs + 專屬後期工具費 ÷ 入 cut 秒數 |
| Human correction time | prompt／asset prep + review + edit/VFX/sound fix 的人時；分類記錄 |
| Queue wait ratio | queue time ÷ shot-ready→result time |
| Waste rate | 未入 cut 的生成秒數或費用 ÷ 全部生成秒數或費用 |

所有費用與速度採實際 task／帳單時間，不以網站 marketing 數字估填；失敗但未收費也要記時間與失敗類型。

## 14. 三種操作模式

### 14.1 品質最大化

**目標**：在預算／檔期內最大化故事、表演、畫面、聲音與 continuity；接受較高重試與人工後期。

操作：

- 全量 creative bible、floor plans、entity schedules、color／sound scripts 先鎖。
- A／B shots 先 previz；hero shots 使用 approved multi-view／keyframes／clay，逐鏡 shot contract。
- 平台支援時以最終需要的高品質規格生成；但先做 feasibility run 隔離動作／物理風險。
- 每鏡候選數、retry ceiling 由預算決定；盲選後才看 run metadata，降低 sunk-cost bias。
- 三層 QC + neighbor A/B cut test；hero shot 需 director、continuity、editor／VFX 多方核准。
- picture lock 後完整 VFX、color、ADR、foley、mix、字幕與雙人 final QC。

**暫定品質 gate（`實務建議／待校準`）**：所有硬 gate pass；任一 continuity-critical 分項不得低於 4/5；hero shot 的 prompt、identity、motion、editorial usability 由至少兩 reviewer 均評 4/5 以上。數值是 project policy，不是 Seedance 成功率。

**何時使用**：長期可見的 hero work、品牌／角色 IP、影院／高階串流、複雜表演與 VFX。  
**代價**：較慢、較貴、流程依賴更多；不能稱同時速度最大。

### 14.2 速度最大化但守品質 gate

**目標**：最短 wall-clock 交付一個完整可看版本，不犧牲故事可讀、安全、身份與可剪性底線。

操作：

- 先鎖最小 bible：主角 passport、主要 locations、關鍵 props、camera／color／sound 規則。
- Coverage 偏向 C／低風險 B：較短、單一動作、較少人物、locked／simple camera、cuts 取代連續複雜互動。
- 建立完整 animatic；獨立 shots 平行、相依 shots 序列化。
- 首輪只跑一次 blocking candidate；先組 rough cut，再把真正阻擋故事的 shots 升級。
- 精確文字、清理、轉場、字幕與聲音用成熟後期工具，不用整鏡重生。
- 低優先 aesthetic defect 若不影響 cut 可接受，但必須留下 waiver；硬 gate 不得放寬。

**不可跌破的暫定 gate（`實務建議／待校準`）**：故事 beat、required entities、identity、方向／道具 state、可理解音訊與 delivery spec 全 pass；blocking artifact 為 0；editorial usability 至少有完整可用區間。分項低於 3/5 的 shot 不入 cut。

**停止**：首次 retry 若未針對 hard-gate defect，取消；同一 hard defect 連續重現即 route，不在 prompt 上無限迭代。  
**何時使用**：內部 pitch、快速教育／社群內容、時效性高且允許簡化 coverage 的成片。  
**限制**：這是「速度最大化但有底線」，不是最高單鏡品質。

### 14.3 推薦混合流程

**目標**：把高成本精力集中在觀眾最會注意、且失敗最傷故事的 shots；其餘以快速但合格流程完成。

1. **全片先 working end-to-end**：script → minimal bible → animatic → blocking rough cut。
2. **風險 × 敘事價值分級**：
   - A：hero／情緒轉折／identity close-up／複雜物理 → 品質流程。
   - B：主要敘事 coverage → reference + standard QC；需要才升級。
   - C：連接／氣氛／insert → 速度流程；盡量平行。
3. **先修結構，後修像素**：rough cut 不成立時回 script／coverage；不要用漂亮 hero shot 掩蓋敘事洞。
4. **只升級 visible bottleneck**：按 timecode defect 與觀眾重要性選 pickups／VFX。
5. **跨層 gate 不變**：安全、權利、故事、identity、continuity、交付規格對所有 tier 一致。

**為何推薦**：它同時承認 quality／speed 的代價，且能在 future evaluation 中形成可比較的 Pareto 點。`未知／待驗證`：在本專案未實測前，不能稱它是全域最優；它只是目前證據最支持的起始政策。

## 15. Pareto 驗證

### 15.1 定義

把每種 workflow 產生的點寫為：

```text
(quality vector, approval rate, retries, wall-clock, human hours,
 usable seconds/hour, cost/approved second, waste rate)
```

Workflow A **支配** B，只有在：

- A 的所有預先指定 quality floors 均不差於 B；且
- A 在至少一個 quality KPI 更好而 time／cost 不更差，或在至少一個 time／cost KPI 更好而 quality 不更差。

若某流程畫質更好但更慢，它與另一流程可能都在 Pareto frontier；不可用單一加權總分假裝客觀最優。

### 15.2 可驗證流程

- 使用相同代表性 shots、inputs、平台、model ID 與 review rubric。
- 每個 shot／workflow 做兩層重複：相同 seed 的 paired comparison 用來降低隨機差，另以多個預先登記 seed 估計輸出分布；官方只保證同 request + 同 seed「相似」，不保證完全一致。
- 盲化影片順序與 workflow 名稱；ties 允許。
- 以 shot 為 paired block；報中位數、分布、95% bootstrap CI 與 effect size，不只報平均。
- 分 A／B／C risk tier 與 task type，避免低風險 C shots 稀釋 hero failures。
- 只有 frontier 在不同抽樣／reviewer 下穩定，才更新 production policy。

完整實驗見 [future-evaluation-plan.md](future-evaluation-plan.md)。

## 16. Continuity QC 矩陣

| 維度 | 每鏡 | 相鄰鏡 | Scene／sequence | Final |
|---|---|---|---|---|
| 角色 | 臉、髮、體型、解剖 | 衣裝／傷勢／情緒／手持物 | arc、age、recurrence gap | 全片 identity spot-check + hero 全查 |
| 空間 | 背景、幾何、perspective | 軸線、方向、eyeline、入口出口 | 地理、日夜、場景狀態 | continuity map audit |
| 時間 | 動作順序、速度、flicker | action match、camera velocity | story time、天候、服裝濕損 | timeline audit |
| 道具 | 數量、材質、手、狀態 | transfer、出現／消失因果 | state machine | prop ledger audit |
| 光色 | 光向、曝光、材質反應 | shot match | color script | calibrated display QC |
| 攝影 | 景別、機位、運鏡、focus | cut、handles、screen direction | grammar、節奏、coverage | full editorial playback |
| 聲音 | speaker、台詞、口型、sync | room tone、perspective、level | motif、語言、voice identity | mix／loudness／channel QC |
| 字幕 | 文本、speaker、時間 | 換行、跨 cut | terminology、style | 全片 proof + safe area |

## 17. Checkpoint／回退

至少在 Gate 1、3、5、7、9、10 建 immutable checkpoint：

```text
checkpoint_id
timestamp / owner / approvals
script+bible versions
continuity state snapshot
approved asset+shot hashes
edit decision list / timeline version
open defects / routes / budget remaining
tool+model+platform+document versions
```

回退規則：

- Shot retry：回 parent approved run，不從 rejected child 繼續。
- Scene rollback：若 state／axis／wardrobe 被錯誤更新，回 scene-start checkpoint，重放核准 deltas。
- Picture rollback：structure lock 後的變更要列 downstream VFX、sound、subtitle、color 影響，producer 批准才開。
- Model／平台更新：建立新 branch 做對照，不覆寫舊 approved renders；重新通過版本 gate 與代表性 regression suite。

## 18. 限制與待反證事項

- Seedance 2.5 單次 30 秒與 extension capability 不等於長片 continuity 已解決；官方宣稱的展示成果沒有公開平均成功率與成本。
- MovieBench 是資料／benchmark 的 hierarchical evidence；StoryMem、EntityBench 是特定研究系統／預印本，不能當 Seedance 內部架構。
- Reference 上限 50 不代表應填滿；官方 prompt guide 明示較低主體數與短 reference 較穩。
- 第一／最後一幀、reference、extension、edit 各有不同鎖定行為；Higgsfield／其他 UI 的同名功能需另做 platform gate。
- 生成 audio 為 mono；專業長片仍需後期聲音設計、mix 與 subtitle timing。
- 品質／速度三模式的 thresholds、retry ceiling、tier 分級與 Pareto frontier 都要用本專案未來資料校準；目前信心：架構原則高、Seedance 2.5 專屬收益幅度低至中。
