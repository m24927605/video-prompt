以下是一套可直接開案的 production OS v0.1。核心不是要求模型記住 75 分鐘，而是以外部的 bible、state、manifest、ledger 與剪輯 lineage 維持真相。

本案不採巨型 prompt；每個 shot 都能獨立生成、審核、剪輯與回滾。也不把 extension 當長片骨幹。

## 1. 證據、假設與 Gate 0

文件基準日：2026-08-22。

| 類別 | 目前狀態 |
|---|---|
| 使用者已鎖定 | 75 分鐘、兩主角、四個主要場景、車輛累積損壞、三日天候與服裝變化 |
| 工作解讀 | 「四個主要場景」視為四個 location families；車內是移動子場景，不另算第五場 |
| 創作假設 | 下述片名、角色、劇情、鏡數與時長分配都可替換 |
| 尚未指定 | 實際平台 surface、顯示模型、完整 model ID、地區、官方文件版本、額度、價格、輸入輸出限制 |
| 尚未指定 | 預算、交片日、發行版本、畫幅、rational frame rate、codec、color、音訊、字幕與無障礙規格 |
| 尚未驗證 | A/B/C 比例、重試上限、shot 數、rolling assembly 節奏 |
| 直接觀察 | 無；尚未看到本案生成媒體，也未做付費生成 |

任何付費生成前，先鎖定 `platform_profile_id`：

```text
surface/provider
displayed_model
full_model_or_endpoint_id
region
official_doc_url_and_date
supported_task_and_input_types
output_duration/aspect/resolution/audio rules
quota/price/billing behavior
rights/watermark/disclosure terms
```

Seedance 2 UI、Seedance 2.0、2.5、ModelArk、LAS 或第三方介面若成為候選，必須各有獨立 profile；不得搬用彼此的預設值、限制、成本或參數。

同一 Gate 也要鎖定角色肖像、聲音、音樂、字型、商標、參考圖、訓練／上傳權利，以及 `B_total`、各部門 ceiling、picture lock 與 master deadline。未完成者標成 `HOLD`，不能靠猜測進入正式生成。

## 2. 工作故事與五層 hierarchy

工作片名：《鹽雨線》，代碼 `FILM-SALT75`。

工作 premise：2097 年，修車技師陸岑載著氣候檔案員葉澄，必須在三日磁暴前，把最後的降雨模型送到潮汐上行塔。途中發現模型與葉澄的記憶植入物綁定；上傳可能抹除她的自傳記憶，而陸岑早已知道風險。

四個主要地點：

- `LOC-01` 穹城外環：車庫、封鎖閘口。
- `LOC-02` 白鹽公路帶：鹽原道路、廢棄驛站。
- `LOC-03` 風針天線谷：中繼站、天線場。
- `LOC-04` 潮汐上行塔：堤道、機房、外部平台。
- `VEH-001-INT` 車廂是車輛的移動子場景。

### 層級預算

| 層級 | 首輪規模 | 必需 artifact | Exit gate |
|---|---:|---|---|
| Film | 75:00 | charter、劇本、bible、三日 story/color/sound arc | 故事、權利、格式鎖定 |
| Sequence | 8 | 目標、轉折、時長、進出狀態 | 不可逆轉折與依賴清楚 |
| Scene | 約 38 | scene card、floor plan、continuity state、coverage | 地理、角色與狀態可解 |
| Beat | 約 168 | 單一可見行為、反應或資訊轉移 | 每個 beat 有存在理由 |
| Final shot | 約 600 | shot contract、input packet、QC/route | 可獨立生成、審核、剪輯 |
| Coverage contract | 約 780 | primary、conditional backup、pickup trigger | 備援用途明確 |

600 鏡對應平均約 7.5 秒的剪輯長度，僅是 animatic 預算，不是平台單段能力宣稱。780 份 coverage contracts 也不會全部立即生成；備援鏡只在風險或 rough cut 缺口觸發。

### 八個 sequences

| SQ | 時碼 | 敘事轉折 | 狀態弧 | 場／beats／final shots |
|---|---|---|---|---:|
| 01 | 00–08 | 建立任務與隱瞞；闖過城閘，無法回頭 | Day 1 乾冷霾；服裝乾淨；車完整 | 4／17／54 |
| 02 | 08–17 | 互不信任；共同選擇危險鹽原 | 熱霾、揚塵；服裝積塵；濾網堵塞 | 5／20／65 |
| 03 | 17–27 | 沙暴擦撞；發現模型與葉澄相連，決定改道 | 右燈滅、玻璃裂、保桿鬆；衣袖磨破 | 5／23／78 |
| 04 | 27–37 | 解碼證實上傳代價；葉澄拿回決定權 | Day 2 低雲細雨；衣服半乾帶鹽；舊傷保留 | 5／24／80 |
| 05 | 37–46 | 關係破裂後互救；建立平等約定 | 雷雨、濕泥；冷卻與自動駕駛失效、後門卡死 | 5／20／68 |
| 06 | 46–56 | 陸岑坦白；兩人決定用車作隔離緩衝 | Day 2 夜至 Day 3 黎明；保溫層、補胎、電力受限 | 5／22／76 |
| 07 | 56–67 | 上傳中止；只剩把車接成電力橋 | Day 3 風暴核心；車進入不可逆熱損 | 5／26／104 |
| 08 | 67–75 | 完成橋接；葉澄保住身份核心，車永久熄火 | 風雨轉亮；衣物仍破損；車成固定殘骸 | 4／16／75 |

### Scene → Beat → Shot 範例

`SC-04-03`：Day 2 中午，天線谷解碼室，約 3:30。

| Beat | 單一主要變化 | Coverage |
|---|---|---|
| BT-01 | 核心從盒內進入 reader | wide、進場 two-shot、插槽 insert |
| BT-02 | 葉澄辨認自己的神經簽章 | OTS、乾淨 UI plate、葉澄 CU |
| BT-03 | 陸岑承認早知風險 | profile two-shot、兩個 singles、reaction |
| BT-04 | 核心 ownership：陸岑 → 葉澄 | 中景、獨立手部 insert、陸岑 reaction |
| BT-05 | 雷擊使 reader 斷電 | 剪影 two-shot、天線／受損車 cutaway |
| BT-06 | 葉澄決定繼續，但由她決定條件 | two-shot、single、screen-right exit |

共 18 個 coverage contracts，預計剪入 12–14 鏡。交接、碰撞、精確 UI、複雜物理都拆成獨立 shots，不在同鏡要求角色「交接、轉身、說完台詞、走出門」。

## 3. Creative bible、資產與 continuity

### Passport inventory

| Passport | 最少內容 |
|---|---|
| `CHAR-001/002` | 臉、髮、體態、姿勢、手別、步態、多角度與表情 reference、禁止漂移 |
| Voice/behavior | 台灣華語或最終語言／口音、音色、語速、發音字典、呼吸、凝視、手勢、反應節奏、權利 |
| Wardrobe/injury | Day 1 乾淨／積塵／磨破，Day 2 半乾／全濕／泥污，Day 3 保溫／膠帶修補；傷勢另版 |
| `VEH-001` | 八方向外觀、比例、內裝、座位、控制件、左右細節、機械狀態、聲音特徵 |
| `LOC-01…04` | floor plan、出入口、軸線、地標、材質、光向、時段／天候版本、room tone |
| Props | 記憶核心、工具、持有人／手別、開合狀態；精確圖文另做乾淨 artwork |
| Look | camera grammar、鏡頭尺度、movement、color script、材質、VFX 規則 |
| Sound/subtitle | 環境、車損聲弧、foley、音樂 motif、靜默、字幕字型／版位／語言 |
| Rights/delivery | 來源、授權範圍、地區、期限、核准人、master spec |

所有 passport 均含：

```text
stable_id, version, parent_hash, owner, rights_status,
draft/approved/retired, approved_by/at, source_paths,
allowed_attributes, forbidden_attributes, sha256
```

新天候、濕度、服裝、傷勢或車損必須是新的不可變版本。舊版可以退休供稽核，但不能以 alias、fallback 或「最新版」含糊引用。

### 車損 state machine

```text
DMG01 完整
→ DMG02 鹽塵、濾網堵塞
→ DMG03 右燈滅、玻璃裂、保桿鬆
→ DMG04 冷卻／自駕失效、後門卡死
→ DMG05 膠帶與補片、電力受限
→ DMG06 不可逆熱損、冒煙
→ DMG07-DEAD 永久熄火
```

這是 scene-level snapshot。一次事故內仍須拆成 `DMG03a → 03b → 03c`，讓每個 shot 只新增一項可見傷害。修補只能新增膠帶、束帶或補片；除非劇本明示完成維修，舊裂痕不能消失。

### 三種 continuity store

| Store | 權威與用途 |
|---|---|
| Canonical bank | 人工核准的角色、車、地點、聲音、風格與狀態真相；生成結果不得自動改寫 |
| Approved memory | 從核准 shot 提升的少量高資訊 frame/clip；記錄 shot、timecode、crop、用途邊界 |
| Local handoff | 僅供相鄰鏡頭：姿勢、位置、行進方向、鏡頭速度、末幀、車損、光色、道具持有人與 room tone |

State 採交易式更新：

```text
scene-start checkpoint
+ approved shot delta
= next approved state
```

只有 `APPROVE_SELECT` 或完成後期後再核准的 selection 能提交 delta。`REJECTED`、`ROUTED` 或原始生成結果不能改 state，也不能成為下一代 reference。

### Reference policy

- 每個 packet 只放該鏡需要的角色、服裝、車損與地點狀態。
- 不在同一 reference sheet 混入乾／濕、完好／損壞、白天／夜晚等互斥版本。
- 每份 reference 記錄 role、rights、hash、crop 與 inheritance exclusions。
- Storyboard 控制順序與構圖；keyframe 是較嚴格參考，但不是 pixel lock。
- Exact text、UI、logo 使用 clean plate 加後期 graphic。
- Prompt 只描述本鏡可見事件；整份 bible 不複製進 prompt。
- 不保存 credential、cookie、signed URL 或私人連結。

## 4. Shot manifest、依賴佇列與 lineage

### Shot manifest 必填欄位

```text
identity:
  film/sequence/scene/beat/shot, owner, tier, risk, priority

narrative:
  purpose, start_state, one_primary_delta, expected_end_patch

entities:
  required, forbidden, exact_passport/state_versions_and_hashes

space:
  floor_plan, axis, screen_direction, eyelines, entrance_exit

camera/look:
  size, side, height, lens_feel, movement, focus, light,
  weather, palette, VFX_intent, head_tail_handles

sound:
  speaker, exact_dialogue, language, room_tone, foley, music_or_silence

inputs/runtime:
  ref_packet_id/hash/roles, prompt_id/hash,
  platform_profile, model_id, task, aspect, duration, output/audio parameters

acceptance/route:
  hard_gates, neighbor_compatibility, retry_ceiling, fallback_routes

provenance:
  parent_run, one_changed_variable, output_hash,
  actual_queue/generation/review/human_time, billed_cost,
  reviewer, decision, timecoded_defects
```

Prompt text與 runtime parameters 分開保存，不能假設不同 surface 的 schema 可攜。

### 填寫範例

```yaml
shot_id: SH-04-03-121
tier: A
purpose: "核心 ownership 由陸岑轉給葉澄"
dependencies:
  - STATE-SC-04-03-BT04-START_v002@sha256
  - PROP-CORE-CLOSED_v003@sha256
required:
  - CHAR-001-right-hand
  - CHAR-002-left-hand
  - PROP-CORE
forbidden:
  - extra_hands
  - duplicated_core
  - WARD-D1
  - faces_in_frame
start_state:
  core_owner: CHAR-001
  core_hand: right
primary_delta: "核心進入 CHAR-002 左手"
expected_end_patch:
  core_owner: CHAR-002
  core_hand: left
space:
  axis: reader-to-door
  screen_direction: CHAR-001-left_to_CHAR-002-right
camera:
  locked_insert: true
  handles: required
inputs:
  ref_packet: REFPACK-SH-04-03-121_v004@sha256
  prompt: PROMPT-SH-04-03-121_p003@sha256
  runtime_profile: PLATFORM-PROFILE-TBD
acceptance:
  hard:
    - exactly_one_core
    - correct_sleeves_and_hands
    - ownership_and_direction_unambiguous
    - no_uneditable_contact_artifact
    - usable_entry_and_exit_handles
routes:
  - split_before_after_inserts
  - offscreen_transfer_plus_reaction
  - controlled_prop_composite
```

### Queue

```text
BLOCKED → READY → RUNNING → INCOMING → REVIEW → APPROVED
                                          ↘ REJECTED
                                          ↘ ROUTED
                                          ↘ SUPERSEDED
```

只有所有 dependency 的精確版本與 hash 都核准，才可進入 `READY`。

必須序列化：

- 車損、服裝濕／乾、傷勢、天候與道具 ownership。
- 連續動作、軸線、座位與 local handoff。
- 依賴上一個 approved pose/frame 的鏡頭。
- Approved-memory promotion。
- Scene／Day／DMG checkpoint 的 state commit。

可以平行：

- 已鎖定狀態的空景、道路 plate、insert、reaction、cutaway、texture。
- 不依賴末幀的 B/C 級 connective shots。
- Sound spotting、VFX breakdown、rights review 等不改寫相同真相的工作。

只有 platform profile、model、task、比例、格式、ref packet 與 QC rubric 全部相同時才批次化，否則無法歸因失敗。

### 版本與 selection lineage

完整 lineage 必須可反查：

```text
asset/state hashes
→ shot-contract + prompt + runtime-profile hashes
→ run_id + output hash
→ select_id + source in/out
→ cleanup/VFX/color/audio transforms
→ timeline placement
→ master hash
```

命名例：

```text
FILM-SALT75_SH-04-03-121_take-003_run-r017_prompt-p003_ref-r004_profile-07_v001.mov
FILM-SALT75_VEH-001_DMG04_v002_APPROVED.png
FILM-SALT75_SC-04-03_state_v012.yaml
```

規則：

- Stable ID 永不重用；metadata 才有權威，檔名中的 `APPROVED` 只供閱讀。
- 每個 run 記錄 `parent_run` 與唯一 changed variable。
- 重試只能從最近核准的 parent／anchor 分支，不可從 rejected child 延伸。
- Select 記錄 source in/out、timeline in/out、crop、retime、audio replacement、post ops、鄰鏡與核准人。
- 一個 shot 可以進剪輯但其末幀不適合 handoff；memory promotion 必須另行核准。
- 平台或模型更新開新 branch 跑 regression set，絕不覆寫舊 render。

## 5. 混合模式、重試與失敗路由

採 hybrid 作為起始政策：

| Tier | 用途 | 工作方式 |
|---|---|---|
| A | 轉折、身份近景、核心表演、車損轉換、碰撞、暴雨、高潮 | previz/keyframe、較多候選、兩名 reviewer、完整鄰鏡 QC |
| B | 對話、一般駕駛、標準動作 | 標準 passport/ref packet；被 rough cut 阻塞才升級 |
| C | 空景、insert、reaction、transition、plate | 首輪單一 blocking candidate；可平行 |

所有 tier 共用權利、故事、身份、狀態、方向、可剪區間與交付 hard floor。

未測的初始政策：

- A/B/C 約 20/50/30，依 animatic 重排。
- 有效重試上限 A=4、B=3、C=2。
- 同一 blocking defect 連續兩次，即使未達上限也要換 route。
- 先以 12-shot regression/pilot suite 校準；實際生成需另行授權。
- `extension_depth=0` 為預設。必要的單一相鄰動作可特批一次 bounded branch，但不得再延伸成鏈。

「有效 run」指請求完成且媒體可播放。平台錯誤另記 queue/time/cost，不混入創意重試率。

| 缺陷 | 優先路由 |
|---|---|
| 身份、服裝或車損漂移 | 狀態專用 reference、簡化構圖、改 angle／insert |
| 手、交接、碰撞、物理失敗 | 拆前因／接觸／反應／結果；必要時 3D、simulation、composite |
| 精確文字錯 | clean plate + tracking/graphic |
| 局部瑕疵 | edit、paint、roto、key、cleanup |
| 鄰鏡方向或姿勢錯 | re-edit、reaction、cutaway 或重做單一 end-state |
| 對白、聲線、lip-sync 錯 | dialogue edit、ADR／dubbing |
| 權利、安全或交付不明 | `HOLD`；不得用視覺修補規避 |

## 6. Gates、checkpoints 與 rollback

| Gate／Checkpoint | 通過條件 |
|---|---|
| `G0 / CP00 Charter` | 平台、權利、交付 frame 定義、成本／時間 ceiling、責任人鎖定 |
| `G1 / CP10 Bible` | 兩角色、四地點、三日 wardrobe/weather、車損 state machine、聲畫 bible 核准 |
| `G2 / CP20 Breakdown/previz` | 8 sequences、scene/beat/shot、floor plans、coverage、fail routes、animatic anchors |
| `G3 / CP30 Blocking cut` | 整片從頭到尾可播；每個 required beat 有 blocking media 或具名 placeholder |
| `G4 / CP40 Dailies/selects` | 完整 clip review、hard gate、state、跨鏡與 neighbor QC；核准 shot hashes |
| `G5 Structure lock` | 故事與節奏成立；P0 pickups 關閉；新鏡或重排開始需要 change record |
| `G6 / CP50 Picture lock` | 每個 required beat 有核准 placement；EDL/XML/AAF、frame count、source lineage 完整 |
| `G7 VFX/conform` | 所有 source、VFX、retime、crop、color tags、audio channels 逐 placement 對帳 |
| `G8 / CP60 Finish locks` | Color、final mix/stems/M&E、ADR、music、subtitles 分別核准 |
| `G9 / CP70 Master/archive` | Master hash、完整播放 QC、rights/QC reports、manifest 與 restore test 通過 |

另在每個故事日界、重大 `DMG` 轉換及各 sequence approved-shot lock 建立輕量 checkpoint。

每個 checkpoint 保存：

```text
script/bible/state versions
asset/prompt/runtime/output hashes
approved selects and memory promotions
timeline/EDL and placement lineage
open defects, routes and waivers
actual budget/time ledger
platform/model/doc versions
approvals
```

Rollback：

1. 單鏡失敗：回最近核准 parent／handoff。
2. 軸線、服裝、天候、車損污染：回 scene-start，依序重播 approved deltas。
3. 跨日污染：回最近 Day／DMG checkpoint。
4. Passport 改版：沿 dependency graph 只使受影響 shot/select 失效，不動無關節點。
5. Picture lock 後變更：新 cut branch，列出 VFX、color、sound、ADR、music、字幕、master 的下游影響。
6. Master 修正：產生新 master ID/hash；修正版仍需完整播放與定點複查。
7. 所有 rollback 都開新 branch，不刪除或覆寫原 checkpoint。

## 7. Rough cut、pickups 與 finishing

### Editorial

1. 先做完整 75 分鐘 animatic，對白可用 scratch audio。
2. Blocking cut 允許 `APPROVED_BLOCKING` 媒體和清楚標記的 placeholder； rejected take 不得偷放進剪輯。
3. Dailies 必須看完整 clip 與實際音訊，檢查 opening、middle、ending、高風險 timecode，不能只看 thumbnail。
4. Rough cut 先為故事、表演與節奏服務，不因生成成本高就保留無用鏡頭。
5. Pickup ticket 必須含 timeline 位置、缺失 beat、前後 state、required/forbidden、handles、聲音、依賴、風險、ceiling 與替代路由。
6. Pickup 優先序：
   - `P0` 故事不可理解、狀態矛盾、必要 beat 缺失；
   - `P1` 表演、節奏、方向、handles；
   - `P2` 可接受但待美化的局部問題。
7. P2 優先走 edit/VFX/color/sound；不為像素小瑕疵無限重生。

### Finishing

- **VFX/cleanup**：paint、roto、key、composite、車損一致化、精確 UI／文字；persistent physics 改走 3D/simulation。
- **Conform**：回連原檔，統一 frame rate、codec、duration、color tags、audio channels、檔名；保留所有 transforms。
- **Color**：匹配人物膚色／材質、光向、三日天候、車損表面、gradient/banding 與 legal range。
- **Dialogue/ADR**：畫面可用而語音不可用時走 ADR；依 voice passport、發音字典與權利記錄執行。
- **Foley/SFX**：車聲隨 `DMG01→07` 演化，從正常運轉到異音、冷卻嘶聲、熱損與最終靜默；room tone 跨 cut 連續。
- **Music**：先建立 sequence cue map 與 motif；temp music 不得成為未清權的 final。輸出 full mix、stems 與必要 M&E。
- **Final mix**：檢查 speaker、voice identity、lip-sync、perspective、action sync、loudness與聲道；數值依 Gate 0 交付契約。
- **Subtitles**：只依 final audio 重新 spotting，不依 prompt 時點。檢查文字、speaker、標點、換行、閱讀速率、安全區、遮擋與跨 cut。
- **Mastering**：只從核准的 picture、grade、mix、字幕 hash 組裝；核對 frame count、codec、color/audio metadata、命名與 checksum。
- **Archive**：保存 master/mezzanine、stems/M&E、字幕、timeline、EDL/XML/AAF、VFX/grade、prompt/reference/state/run ledgers、核准與拒絕決策、rights、QC、waiver、tool/model/platform/doc versions；最後做實際 restore test。

## 8. QC 系統

Hard gates 必須先全部通過，不能被平均分抵銷：

- 權利、安全、交付規格。
- Required story beat、角色、道具與地點。
- 正確身份、服裝、天候、車損、座位、方向與 ownership。
- 無不可剪的結構、肢體、物理或 blocking artifact。
- 有完整 usable interval、handles 與鄰鏡相容性。
- 聲音或文字要通過，或已有核准的後期路由。

檢查層級：

1. **Intra-shot**：身份、動作、時序、肢體、物理、camera、light、sound。
2. **Cross-shot**：人物、服裝、車損、天候、道具、軸線。
3. **Neighbor cut**：姿勢、速度、視線、光色、room tone、進出方向。
4. **Scene/sequence**：故事狀態、情緒、資訊、三日弧與節奏。
5. **Final master**：至少一次完整不間斷播放，再逐一檢查所有 edit、VFX、字幕與音訊 transition。

Final QC 分開記錄：

- Technical：duration、aspect、resolution、frame rate、codec、color tags、duplicate/drop/freeze/black frames、audio sync/channels/clipping、字幕 safe area、checksum。
- Content：故事、身份、服裝、車損、天候、肢體、物理、文字、聲音、音樂、字幕。
- Rights：肖像、聲音、音樂、字型、商標、reference、watermark與 disclosure。

每個 finding 都要有 timecode、嚴重度、direct observation／inference／unknown、owner、route、開關時間。Mastering 人員不能單獨核准自己的 final master。

## 9. KPI dashboard

所有數字只能來自實際 ledger。尚無資料時顯示 `N/A`，不能填 0 或臆測值；每張卡標示 `as_of`、cut/master version、樣本數及分子／分母。

| KPI | 計算 |
|---|---|
| Ledger 完整率 | 已填必填欄位 ÷ scope 應填欄位 |
| Orphan lineage | 無法回溯 source hash/run 的 current-cut placements ÷ 全 placements |
| Blocking beat coverage | 有 block/media 的 required beats ÷ required beats；placeholder 另列 |
| Picture beat coverage | 有 approved placement 的 required beats ÷ required beats |
| First-pass approval | 第一個 valid run 即核准的 shots ÷ 已完成首個 valid-run review 的 shots |
| Additional retries | 每個 approved shot 首次核准前的 valid runs − 1；報 median、分布、P90、n |
| Time per approved shot | `approved_at − ready_at`，另拆 queue、generation、review、repair |
| Usable seconds/hour | 進入 current cut 的 approved 秒數 ÷ 實際 production＋review 人時 |
| Actual cost/in-cut second | 已入帳 generation、tool、post 成本 ÷ locked cut 的 approved 秒數 |
| Human correction time | prep、review、edit、VFX、sound repair 的實際分鐘 |
| Queue wait ratio | queue duration ÷ `result_at − ready_at` |
| Waste rate | 未進 current cut 的有效生成秒數或成本 ÷ 全有效生成秒數或成本 |
| Continuity pass | 無身份／服裝／車損／天候／ownership blocker 的鄰鏡對 ÷ reviewed pairs |
| Pickup closure | 已核准 pickups ÷ 已核准 pickup scope；另列 open blockers 與 aging |
| Stage first-pass/rework | 各後期工作 v1 通過率；後續版本的回合、人時與成本 |
| Open QC findings | 依嚴重度、sequence、owner、route 與 aging 統計 |
| Master/Archive | 完整播放紀錄、finding 數、remaster 次數、checksum與 restore pass/fail |

KPI 應按 A/B/C、sequence、defect type、platform profile、完整 model ID 和日期分組。只有全部 hard floors 已通過，才比較品質、時間與成本的 Pareto 關係；不能把「最快」寫成「最好」。

## 10. 實際開工順序

1. 完成 Gate 0：平台、權利、交付、預算與時程。
2. 鎖 creative bible、四地點 floor plans、三日 wardrobe/weather 與 `VEH-001` state machine。
3. 建立 8-sequence、38-scene、168-beat 的完整 animatic。
4. 完成 12-shot 風險 pilot；涵蓋身份近景、two-shot、車內、車損、雨塵、手部、物理、UI、對白。付費生成另行授權。
5. 用實際 ledger 重訂 A/B/C 比例、重試 ceiling、路由與時程；不把起始政策當結論。
6. 做完整 blocking rough cut，再由剪輯缺口觸發 final upgrades 和 pickups。
7. Structure lock、picture lock，依序完成 VFX/conform、color、sound/ADR/foley/music、字幕、mastering、final QC 與 archive。

這份是本片的可執行基線，不是聲稱已被本案實測的最佳流程；目前也沒有執行任何媒體生成。
