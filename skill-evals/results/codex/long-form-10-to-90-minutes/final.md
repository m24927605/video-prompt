以下是一套可落地、可分段執行、可稽核與回滾的 75 分鐘 AI 科幻公路電影製作系統。它把模型當成「逐鏡生成工具」，跨鏡記憶、連戲、版本與成片品質都由外部製作系統負責。

我先做兩項工作假設：

- 「四個主要場景」解讀為四個反覆使用的主要地點，不是全片只有四場戲。
- 暫用工作片名與故事骨架示範；若已有劇本，可保留整套系統而替換內容。

## 1. 專案章程與證據邊界

### 工作故事

《北向殘光》：氣候製圖師林岑與前氣象工程師周拓，駕駛老舊燃料電池旅行車，穿越失控氣候帶，把一枚「氣候種子」送往海岸氣象塔。三天旅程中，他們發現種子啟動後會抹除用來重建它的災民記憶，必須在拯救現存聚落與保存亡者記憶之間做選擇。

兩名主角：

- `CHAR-001 林岑`：精準、控制欲強；負責導航與氣候判讀。
- `CHAR-002 周拓`：熟悉機械、隱瞞種子真相；負責駕駛與修車。

四個主要地點：

- `LOC-001 鹽海補給站`
- `LOC-002 風廊公路`：鹽灘、風機峽谷、維修隧道等子區域
- `LOC-003 沉降觀測站`
- `LOC-004 海岸氣象陣列`：引道、堤道、主塔

### 平台閘門

文件日期：`2026-09-01`。

官方於 2026-07-31 發布 Seedance 2.5，描述單次最長 30 秒及多輪 extension；這只是官方能力聲明，不代表本專案入口、區域、帳號或 API 一定具備相同能力，也不構成長片工作流已驗證。[ByteDance Seedance 2.5 官方發布](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)

正式付費生成前，以下皆為硬性 `UNKNOWN/BLOCKED`：

- 實際平台：官方 UI、API、ModelArk、LAS 或第三方整合
- 顯示模型名與完整 model ID
- 區域可用性、配額、費率、輸入上限與輸出保存期
- 真實輸出解析度、幀率、音訊格式、色彩標籤
- 商用、肖像、聲音、音樂、品牌及訓練資料披露要求
- 發行規格與地區分級

每次 preflight 必須保存：文件 URL、查核日期、平台畫面或 API 回應、model ID、測試任務、實際輸出 metadata。不同平台的數值不可互相套用。

### 暫定交付規格

在發行商確認前使用：

- 片長：`75:00`，允差待發行方決定
- 畫幅：2.39:1
- 時基：24 fps
- 工作母版：3840×1608、ProRes 422 HQ 或同級 mezzanine
- 色彩：統一色彩管理；最終 SDR/HDR 路線在素材測試後鎖定
- 音訊：48 kHz／24-bit；立體聲與 5.1
- 字幕：主要語言 sidecar；翻譯版本依發行需求
- 精確 UI、路牌與字幕均後製合成，不依賴生成模型拼字

這些是製作提案，不是平台能力聲明。

## 2. 操作模式：Hybrid

採「全片先工作，再按重要性升級」：

- A 級：故事轉折、身份近景、雙人關鍵表演、車禍／複雜物理、最終上傳。
- B 級：一般對話、駕駛、地點內行動。
- C 級：空鏡、插入、反應、道路、天候 plate、轉場與聲音覆蓋。

所有級別共用不可降低的底線：權利、安全、故事 beat、人物身份、服裝／車況／道具狀態、方向、可剪區間與交付相容性。

這是起始政策，不是已由本片實測為最優。A/B/C 分配、候選數及重試上限要在代表性 pilot 後用實際帳本決定。

## 3. 75 分鐘故事分解

全片規劃 8 個 sequence、24 個 scene。暫列約 572 個剪輯鏡位，僅作拆解與工作量基線，不等於必須生成 572 支獨立素材，也不是成本預測。

| Sequence | Scene | 分鐘 | 日／地點 | 可見 beat 鏈 | 車況 |
|---|---|---:|---|---|---|
| SQ-010 出發 | SC-010-010 | 3.0 | D1／LOC-001 | 交接種子 → 拒絕改道 → 啟程 | v01 |
|  | SC-010-020 | 3.0 | D1／LOC-002 | 氣象塔靜默 → 收到倒數 → 選風廊 | v01→v02 |
|  | SC-010-030 | 2.0 | D1／LOC-002 | 掃描機逼近 → 熄燈滑行 → 脫身 | v02 |
| SQ-020 風廊 | SC-020-010 | 3.0 | D1／LOC-002 | 風向突變 → 路標失效 → 林岑接管導航 | v02 |
|  | SC-020-020 | 3.5 | D1／LOC-002 | 亂流推車 → 閃避 → 撞擊護欄 | v02→v03 |
|  | SC-020-030 | 2.5 | D1／LOC-002 | 檢查損傷 → 互相責怪 → 暫時和解 | v03 |
| SQ-030 沙牆 | SC-030-010 | 3.0 | D1／LOC-002 | 熱控警報 → 滑行停車 → 發現漏液 | v03→v04 |
|  | SC-030-020 | 4.0 | D1／LOC-002 | 搶修 → 發現航線遭改 → 周拓說謊 | v04 |
|  | SC-030-030 | 3.0 | D1暮／LOC-002 | 沙牆抵達 → 視野歸零 → 衝向觀測站 | v04 |
| SQ-040 真相 | SC-040-010 | 3.0 | D1夜／LOC-003 | 抵達 → 建立空間 → 封門避沙 | v04 |
|  | SC-040-020 | 4.0 | D1夜／LOC-003 | 解碼種子 → 聽見記憶 → 林岑識破真相 | v04 |
|  | SC-040-030 | 2.0 | D1夜／LOC-003 | 電力不足 → 爭奪種子 → 決定續行 | v04 |
| SQ-050 洪水 | SC-050-010 | 3.0 | D2／LOC-003 | 雨水倒灌 → 搶回種子 → 啟動車輛 | v04 |
|  | SC-050-020 | 4.0 | D2／LOC-003→002 | 水位升高 → 車門受阻 → 破水逃出 | v04→v05 |
|  | SC-050-030 | 3.0 | D2／LOC-002 | 隧道停靠 → 綁固引擎蓋 → 更換路線 | v05 |
| SQ-060 告白 | SC-060-010 | 3.0 | D2／LOC-002 | 雨中失去導航 → 憑地標前進 → 看見海 | v05 |
|  | SC-060-020 | 3.0 | D2／LOC-002 | 周拓坦白 → 林岑欲毀種子 → 中止衝突 | v05 |
|  | SC-060-030 | 4.0 | D2／LOC-004 | 駛上堤道 → 爆胎 → 勉強拖行 | v05→v06 |
| SQ-070 最後里程 | SC-070-010 | 4.0 | D3／LOC-004 | 霧中喚醒 → 拆取備援電芯 → 再次啟動 | v06 |
|  | SC-070-020 | 3.0 | D3／LOC-004 | 車身偏斜 → 懸吊崩壞 → 車輛停駛 | v06→v07 |
|  | SC-070-030 | 3.0 | D3／LOC-004 | 取出種子 → 放棄物資 → 步行到塔 | v07 |
| SQ-080 放晴 | SC-080-010 | 4.0 | D3／LOC-004 | 接入主塔 → 系統要求抹除 → 兩人改寫選項 | v07 |
|  | SC-080-020 | 3.0 | D3／LOC-004 | 上傳 → 風向逆轉 → 雲層裂開 | v07 |
|  | SC-080-030 | 2.0 | D3／LOC-004 | 返回車旁 → 收到記憶訊號 → 留白結尾 | v07 |

分鐘合計為 75。

### Beat／shot 原則

每個 beat 只能有一個主要可見變化。若描述出現兩個獨立的「然後」，先拆 beat，再決定鏡頭。

每場至少規劃：

- 空間 master／establishing
- 雙人鏡頭與必要 OTS／single
- 車內與車外方向匹配
- 手、種子、儀表、受損零件 inserts
- 沉默反應、道路或天候 cutaway
- 入場、離場與前後場 handles
- 複雜接觸、精確文字、長對白及物理破壞的替代 coverage

一個生成 clip 可以含多個剪輯鏡位，但不得把它當成 sequence 記憶來源。每個可剪 shot 仍有自己的 contract 與選擇 lineage。

## 4. Creative bible 與不可變 passport

### Bible 清單

- `STORY-BIBLE`：主題、世界規則、角色知情範圍、時間線、禁止提前揭露事項
- `CHAR-001/002`：臉、體型、髮型、慣用手、步態、表演語法、禁漂移特徵
- `VOICE-001/002`：語言、口音、音域、節奏、發音字典與聲音權利
- `WARD-*`：每一天及乾／濕／破損狀態
- `VEH-001`：車身幾何、內裝座位、方向盤、損壞狀態機
- `PROP-001 氣候種子`：尺寸、材質、發光規則、持有人與開關狀態
- `LOC-001..004`：平面圖、出入口、地標、光向、軸線與可用機位
- `WEATHER-*`、`LIGHT-*`：三天氣候與時段
- `CAMERA-BIBLE`：鏡頭尺寸、運動、手持程度、軸線政策
- `COLOR-SCRIPT`：赭黃 → 鉛灰／青綠 → 冷藍後暖白
- `VFX-BIBLE`：天空、沙塵、雨水、介面與氣象塔效果
- `SOUND-BIBLE`：車內共鳴、風、雨、塔台脈衝、記憶聲音
- `SUBTITLE-STYLE`：字體權利、安全區、斷行與說話者規則

每個 passport 都要有：

```text
asset_id, entity_id, version, owner, rights_status,
draft/approved/retired, approval_date, source_paths,
allowed_attributes, excluded_attributes, sha256
```

新服裝、濕度、污損、光線或車況都是新版本；不得把互相衝突的狀態塞進同一張 reference sheet。

### 三天狀態弧線

| 狀態 | 天候／光 | 林岑 | 周拓 | 車 |
|---|---|---|---|---|
| D1-A | 強烈乾燥日光 | 赭色工作外套、乾淨 | 深藍外套、乾淨 | v01 基準舊化 |
| D1-B | 塵霾、橙灰暮色 | 同套積塵 | 袖口磨破、積塵 | v02 積塵 |
| D1-C | 沙暴、低能見度 | 防塵巾、髮亂 | 領口封閉 | v03 擋風玻璃裂、右前葉子板凹 |
| D1-N | 觀測站冷白夜光 | 積塵未清 | 同前 | v04 右鏡脫落、熱控漏液、頭燈閃 |
| D2-A | 陰雨 | `WARD-001-D2-wet` | `WARD-002-D2-wet` | v04 |
| D2-B | 暴雨、泥水 | 濕透、外套較深 | 肩部臨時防水補片 | v05 泥線、車門卡、引擎蓋束帶 |
| D3-A | 冷霧 | 半乾、鹽漬固定 | 半乾、補片固定 | v06 左後胎毀、電量危急 |
| D3-B | 雲裂、暖白 | 狀態不回復 | 狀態不回復 | v07 懸吊崩壞、停駛 |

污損只能累積，除非故事中出現清洗或換衣 beat。

### Continuity store

分成三個不可混用的庫：

1. `canonical_bank`：人工批准的人物、車、地點、服裝與世界真相。
2. `approved_memory`：只從通過 QC 的鏡頭提升，記錄來源 shot、timecode、crop 與允許用途。
3. `local_handoff`：相鄰鏡頭的姿勢、位置、運動尾端、車況、道具持有人與 room tone；不能覆蓋 canonical truth。

參考素材必須標註角色，例如 `identity`、`wardrobe_state`、`vehicle_state`、`location_geometry`、`motion_only`、`audio_timing`。不得把被拒鏡頭或漂亮但錯誤的 frame 提升成身份真相。

## 5. Shot manifest 與 contract

Manifest 至少包含：

```text
shot_id, sequence_id, scene_id, beat_id, tier, risk, priority, owner,
required_entities, forbidden_entities, start_state_id, primary_delta,
end_state_id, axis, screen_direction, camera, look, sound,
input_packet_id, prompt_version, parameter_set_id,
platform, model_id, task, intended_duration, handles,
dependencies, continuation_relation, max_valid_runs,
extension_allowed, max_extension_rounds,
hard_gates, reviewer, decision, selected_run, route
```

`prompt_version` 與 `parameter_set_id` 必須分開；不可把某平台參數藏進自然語言 prompt。

範例：

```yaml
shot_id: SH-060-030-020
beat_id: BT-060-030-02
purpose: 讓爆胎成為最後里程的不可逆代價
required:
  - CHAR-001@WARD-001-D2-wet-v02
  - CHAR-002@WARD-002-D2-wet-v03
  - VEH-001-damage-v05
  - LOC-004-causeway-rain-v02
forbidden:
  - VEH-001-damage-v01
  - dry_clothing
start_state: 車以低速沿堤道前進，兩人仍在車內
primary_delta: 左後輪失壓並塌陷
end_state: 車停在原車道；人物尚未下車；輪胎已毀
screen_direction: left_to_right
continuation_relation: intentional_next_shot
extension_allowed: false
hard_gates:
  - 人物與車況版本正確
  - 爆胎位置是左後輪
  - 車未翻覆、人物未離車
  - 無無法以剪輯或 VFX 修復的車體變形
```

## 6. 依賴佇列

狀態流：

```text
BLOCKED → READY → RUNNING → INCOMING → QC
        → REJECTED / SELECTED → APPROVED
        → HANDOFF_PROMOTED → IN_CUT → LOCKED
```

主要依賴：

```text
權利與平台 preflight
  → canonical passports
  → scene continuity state
  → animatic/blocking
  → shot contract
  → generation
  → dailies/select
  → local handoff promotion
  → rolling rough cut
  → pickups
  → picture lock
  → VFX/color/sound/subtitles
  → master QC
```

可以平行：

- 獨立空鏡、plate、insert、reaction、道路 texture
- 已鎖定狀態且無相鄰 handoff 的場次
- room tone、foley spotting、VFX breakdown
- 不修改同一 canonical truth 的審查工作

必須序列化：

- 車況 v01→v07 的提升
- D1→D2→D3 服裝與天候狀態
- 同動作或同 shot 的有限 continuation
- approved-memory promotion
- 依賴上一鏡末幀、運動向量或道具交接的鏡頭

不同 model、比例、reference packet、任務或 rubric 不得混成同一批，否則無法判斷失敗來源。

## 7. 版本、命名與 selection lineage

穩定 ID 永不因剪輯重排而重用：

```text
FILM-NORTHLIGHT
SQ-060
SC-060-030
BT-060-030-02
SH-060-030-020
```

檔名：

```text
FILM-NORTHLIGHT_SH-060-030-020_take-003_run-r017_
prompt-p004_ref-r006_model-full-id_v001.mov
```

完整 lineage：

```text
canonical asset hashes
→ input packet r006
→ prompt p004 + parameters cfg003
→ parent run r012
→ run r017 + output sha256
→ review decision d006
→ select sel002
→ timeline item TL-v023-00418
→ VFX/color/audio transforms
→ master checksum
```

每次 run 只能改一個變數，並記錄 queue、生成、審查、人工修正時間及實付成本。Rejected output 只能作診斷，不能作 handoff 父節點。

## 8. 最小端到端 pilot

不要直接展開 572 個鏡位。先做約 12 鏡的代表性 vertical slice，涵蓋：

- D1 日光雙人車內對話
- 車外完整身份鏡頭
- v02→v03 的損壞變化
- D2 雨中濕服裝
- 道具交手與手部 insert
- D3 冷霧身份近景
- LOC-004 大遠景與 VFX plate
- ADR、foley、色彩匹配、字幕與一個交付片段

正式 pilot 前，先用 3 個假素材驗證 reviewer 輸入／輸出 schema、timecode defect、decision 與 lineage 是否可讀寫。

Pilot 的出口不是「畫面漂亮」，而是：

- schema 能走完
- 狀態能重播
- 選片能追溯
- 進 NLE 後可剪
- 一個完整影音字幕 master 能通過 QC
- 實際時間與成本可寫入 KPI

## 9. 重試、失敗路由與上限

目前使用者尚未提供生成預算，因此不虛構重試數字。

在任何付費生成前，A/B/C 各級的 `max_valid_runs` 必須填入整數；空值即不能進 `READY`。上限由 pilot 實際成本、交付時鐘及剩餘預算批准。

通用政策：

- 每次只改 prompt、reference、parameter 或 shot design 其中一項。
- 同一 hard defect 重現、限制彼此振盪、需要使用 rejected frame、達到上限或權利不明時，停止再生。
- extension 預設關閉；例外僅限同場、同 shot 的連續動作，且 `max_extension_rounds` 必須事先填定。
- extension 不跨 scene，更不承擔長片記憶。

失敗路由依序評估：

1. 修正 canonical source 或狀態資產
2. 簡化單一動作或鎖定鏡位
3. 拆成短 shot
4. 改用 insert、reaction、cutaway
5. 局部剪輯、paint、roto、composite
6. 3D／模擬處理車體與複雜物理
7. ADR／配音處理可用畫面
8. 最後才改寫故事 beat

## 10. Rough cut、pickups 與 finishing

### Editorial

依序建立：

1. 75 分鐘 animatic：場景卡、storyboard、暫時對白與聲音。
2. Blocking cut：先讓所有故事 beat 存在，不追求最終畫質。
3. Rolling rough cut：只有 accepted takes 可進時間線。
4. Pickups cut：按缺口而非按漂亮程度升級。
5. Structure lock：P0/P1 缺口解決後凍結場序與狀態。
6. Picture lock：之後新增或換鏡必須列出 VFX、color、sound、ADR、music、subtitle 影響。

Pickups 分級：

- P0：缺故事資訊或因果
- P1：人物、方向、車況、服裝或道具連戲錯
- P2：表演、節奏、反應不足
- P3：純視覺升級

先處理 P0/P1；P3 不得拖延結構鎖。

### VFX／cleanup

- 沙塵、雨水、塔台能量與遠景天空做分層 plate。
- 車損若核心物理不穩，使用 3D／composite，不無限重生。
- 手、臉、邊緣、反射與局部車牌用 paint／roto 修復。
- 所有 UI、路牌、精確字樣後製合成。
- Conform 統一 codec、fps、色彩標籤、音訊通道與命名；保存原始媒體及每次 transformation。

### Color

- 先做 input normalization，再做鏡間 match。
- 逐場核對皮膚、衣料、車漆、濕度、日別與動機光。
- 檢查 banding、天空漸層、暗部壓縮、邊緣爬動與 upscale ghosting。
- D1、D2、D3 使用 color script，但不能用調色掩蓋錯誤的天候狀態。

### Sound、ADR、music

- 對白、ADR、foley、車輛、環境、VFX、music 分 stem。
- 車況 v01–v07 有不同機械聲：正常共鳴、頭燈／熱控異常、濕艙、爆胎拖行、最後斷電。
- 每個地點保存 room tone passport。
- 原生生成語音只可作素材；發音、聲音身份、lip-sync 或噪聲不合格便走 ADR。
- 音樂以「記憶脈衝」為 motif，避免覆蓋關鍵車況或氣象敘事聲。
- 最終 loudness、峰值與聲道規格依發行方鎖定。

### 字幕與 mastering

字幕必須從 final mix 的實際音訊重新定時，不讀 prompt 時間碼。檢查說話者、斷行、閱讀速度、安全區、遮擋、跨切點與 sidecar／burn-in 需求。

Master 至少包含：

- Picture master
- Textless master
- Stereo／5.1 mix 與 stems
- M&E
- Subtitle sidecars
- QC report、checksum
- 使用到的模型、工具、權利、waiver 與披露記錄

## 11. QC 閘門

### Shot QC

先 hard gate，後評分：

- 必要／禁止 entity
- 人物、服裝、車況、道具狀態
- primary delta 是否唯一且完成
- 軸線、方向、eyeline
- 完整可用區間與 handles
- anatomy、motion、contact、physics
- 音訊／文字是否通過或已有批准的 post route
- 與前後鏡可剪

### Scene／sequence QC

- geography 是否能理解
- completed/current/reserved beat 是否被越權提前完成
- 車損、濕度與服裝是否單向演化
- 是否缺 master、reaction、insert、exit
- 聲音透視與 room tone 是否連續
- 演員知情範圍是否提前洩漏

### Final QC

- 至少一次不中斷完整播放
- 再逐一檢查每個 cut、VFX、字幕與音訊轉場
- 技術檢查：片長、fps、codec、色彩標籤、黑／凍／掉幀、sync、clipping、聲道、字幕與 checksum
- 內容檢查：故事、身份、服裝、車況、天候、物理、文字、音樂、權利、披露與 watermark

## 12. Checkpoint 與 rollback

| Checkpoint | 內容 |
|---|---|
| CP-00 Charter lock | 權利、平台、model ID、交付、預算、重試上限 |
| CP-01 Schema/pilot lock | 三鏡 schema fixture、12 鏡 vertical slice、實際 KPI |
| CP-02 Bible semantic lock | 劇本、passport、狀態機、地點圖、camera/color/sound bible |
| CP-03 Previz lock | 75 分鐘 animatic、coverage 與風險路由 |
| CP-04 Blocking-cut lock | 全片第一次可看的 end-to-end cut |
| CP-05 Structure lock | 場序、狀態、P0/P1 pickups |
| CP-06 Approved-shot lock | selects、approved memory、timeline lineage |
| CP-07 Picture/sound/color lock | conform、VFX、mix、字幕 |
| CP-08 Master/archive | master、QC、checksum、權利與完整帳本 |

回滾規則：

- 重試永遠從 approved parent 分支，不從 rejected child 繼承。
- 車況、服裝、軸線或道具損壞時，退回 scene-start state，依 approved delta 重播。
- Structure lock 後的變更必須附 downstream impact。
- 模型或平台更新只能建立新 branch，通過 pilot regression 後才可採用。
- Canonical truth 不被生成結果覆寫。

語義尚未凍結前不建立全域 seal。若審查重開語義，先按根因聚類，修 source of truth 或 compiler/schema，跑 focused regression，再做一次全驗證與 reseal。預設每個工作 slice 90 分鐘、最多兩次完整 seal/review cycle；達上限時保存最新有效 checkpoint，列出 blocker，不能假稱完成。

## 13. KPI dashboard

目前所有值都應顯示 `N/A—尚未執行`。Pilot 後才建立 baseline 與專案門檻。

| KPI | 計算方式／資料源 |
|---|---|
| First-pass approval | 首個有效 run 即批准的 shot／有效首 run |
| Additional retries | 批准前額外有效 run／批准 shot |
| Time per approved shot | shot-ready 到 approved 的實際壁鐘時間 |
| Usable seconds/hour | 進 cut 的批准秒數／製作與審查工時 |
| Cost per in-cut second | 所有付費生成及專用 post 成本／成片秒數 |
| Waste rate | 未進 cut 的生成秒數或成本／全部生成 |
| Queue wait ratio | 排隊時間／shot-ready 到結果時間 |
| Human correction time | prep、review、edit、VFX、sound 修復工時 |
| State violation rate | 車況／服裝／天候／道具 hard-state 錯誤 shot／有效受審 shot |
| Pickup rate | pickup 鏡位／structure-lock 鏡位 |
| Lineage completeness | 有完整 asset→run→select→timeline→master 路徑的時間線項目／全部項目 |
| Defect escape | 下一關才發現的 blocking defect／本關已審項目 |
| ADR replacement | ADR 對白時長／最終對白時長 |
| Master QC reopen count | master QC 後重新開啟 picture、sound 或 subtitle 的次數 |

報告中位數、分布與樣本足夠時的 P90；不得以平台宣傳速度、UI 素材數、價格頁或解析度 badge 取代實際 ledger。這套架構的成功標準不是「生成很多」，而是 75 分鐘每個剪輯項目都能說明：它從哪個已批准狀態出發、改變了什麼、由誰批准、如何進入成片，以及出錯時應退回哪個 checkpoint。
