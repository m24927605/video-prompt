參考資料全部讀完（film-producer 五份、video-qc 三份、prompt-director 三份；repo 內沒有既有劇本、charter 或 ledger，所以下面的系統是從零建）。以下是完整的製作系統設計；§2.2 的故事骨架是占位用的範例，ID、狀態機與流程才是交付物。

---

# FILM-ROAD｜75 分鐘 AI 科幻公路電影製作系統（v0.1 規劃稿）

> 定位：一套「外部記憶 + 狀態機 + 可回滾」的製作系統。模型不負責跨鏡頭記憶，製作系統負責。所有流程屬 practice recommendation / team inference；**本專案尚未以任何付費生成驗證任何流程**，所有數字都是初始值，要用你自己的 ledger 校準。

## 0. 證據、日期、平台假設與未知

| 項目 | 狀態 |
|---|---|
| 知識日期 | skill 封存知識 2026-08-22（= 今日）。平台參數/價格/配額/政策屬時間敏感，Gate 0 必須重查當日官方文件 |
| 生成平台/模型 | **未指定**。本計畫 platform-neutral；runtime 欄位（task、aspect、duration、resolution、audio、seed、並行數）在 Gate 0 前一律標 `unknown`。不替你選平台 |
| 已封存官方事實（僅 ModelArk Seedance 2.5 @2026-08-22） | reference 上限 30 圖 / 10 影 / 10 音 / 合計 50，官方建議較小工作集；task hint `auto/reference/edit/extend`；first/last 為 strict role；`return_last_frame` 只是傳輸、不是記憶；`No subtitles / No BGM / No audio` 是 prompt 語言控制；未記載 `negative_prompt` 欄位。**不可套到 LAS、Higgsfield、UI「Seedance 2」或 2.0** |
| 方法證據等級 | 層級分解：MovieBench（peer-reviewed）；三層記憶庫與 entity schedule：StoryMem / EntityBench（preprint 方法啟發）；其餘為製作者自述與團隊推論。皆非 Seedance 內部機制 |
| 明確未知 | 單 clip 可生成時長與實際輸出偏差、並行上限、輸出保留/過期時間、seed 是否可重現、音訊聲道、單價、是否支援 extend / first-last / edit、肖像與聲音權利政策、區域可用性 |
| 授權邊界 | 本計畫不呼叫任何付費生成；規劃與文字測試不等於生成授權 |

## 1. Operating mode：Recommended hybrid（A/B/C 分級）

選擇理由：兩主角 + 逐步損壞的車 + 三天服裝/天候變化，代表**身分與狀態連續性**是最高風險；但公路片同時有大量可平行的行駛 plate、風景、insert。Quality-max 會把 75 分鐘全部壓進高成本審查；speed-max 會在狀態連續性上崩。Hybrid 讓風險集中的鏡頭走品質流程、連接鏡頭走快速平行。

| Tier | 定義（narrative value × technical risk） | 本片對應 | 流程 |
|---|---|---|---|
| A | 高 × 高 | 主角情緒轉折特寫；每個車損狀態 V1–V6 的**首次出現**鏡頭；割傷/包紮；肢體接觸（推車、開引擎蓋、遞物）；天候轉換 establishing；結尾 | 完整 bible + keyframe/blockout + 可行性測試 + 多候選 + 獨立審查 + 鄰接剪輯審查 |
| B | 中 | 車內對話 coverage、走路對話、一般 two-shot、非首次出現的車況鏡頭 | 標準 reference packet + QC；卡住才升級 |
| C | 低 × 低 | 行駛 plate、風景、儀表板/輪胎/天空 insert、天候 cutaway、質感 | 單候選、平行批次、不打磨；失敗換角度 |

**未經測試的政策假設**（ledger 累積後必須校準）：tier 比例、各 tier retry 上限、pickup 預留比例、rolling assembly 的重疊程度、每 tier 候選數、animatic 先行的效益大小、hybrid 的協調成本。

## 2. Film → Sequence → Scene → Beat → Shot

### 2.1 Charter（Gate 0 必鎖）

| 決策 | 建議預設（未鎖，需你決定） |
|---|---|
| 片長/受眾/語氣邊界 | 75 分鐘；科幻公路；兩人戲為主 |
| 畫幅/母帶 | 畫幅比需對應所選平台實際輸出（若平台只出 16:9 而母帶要 2.39:1，每個 shot contract 要含裁切安全區）；24 fps 母帶；生成 fps/解析度未知 → conform |
| 對白語言 | 依你的訊息推定台灣華語（可含台語/英語）；需鎖定 |
| 聲音策略 | 對白以 ADR（真人配音或已授權 TTS）為主，生成對白僅作 scratch；需聲音權利 |
| 權利 | 故事、肖像（若 reference 用真人）、聲音、音樂、字型、品牌、每一張 reference |
| 預算/時程上限 | 未知 → 用來推導 per-shot cost/time ceilings |
| 科幻元素 | 假設為環境/道具型（天空異象、廢棄基礎設施、一個裝置），非生物變形；重複出現的元素走 composite |

### 2.2 狀態時間軸（placeholder 骨架；ID 與狀態機是交付物，劇情待劇本替換）

| Day/時段 | 天候/光 | 車況 | A | B | 道具所有權 | 主要 LOC |
|---|---|---|---|---|---|---|
| D1 晨 | 晴、乾熱、高角度光 | V0 完整 | WARD-001-base-v01 | WARD-002-base-v01 | PROP-002 裝置：B | LOC-001 廢棄加油站 |
| D1 日 | 晴、塵 | V1 塵土 + 左側刮痕 | WARD-001-dust-v02 | WARD-002-dust-v02 | | LOC-002 鹽灘公路 |
| D1 黃昏 | 晴、低角度逆光 | V2 + 擋風玻璃蛛網裂、右頭燈破 | + INJ-001-v01 右掌割傷（未包紮） | dust-v02 | PROP-006 布條：B→A | LOC-002 路肩 |
| D1 夜 | 晴、冷 | V2 | INJ-001-v02 布條包紮 | dust-v02 + PROP-004 外套 | PROP-004 外套：A→B | LOC-002 路肩/車內 |
| D2 晨 | 陰 | V3 + 過熱蒸汽、引擎蓋開、冷卻液漬 | dust-v02 | dust-v02 + 外套 | | LOC-002 → 公路 |
| D2 午 | 陰→雨 | V4 + 泥、右後門凹、左前輪蓋缺、單支雨刷失效 | WARD-001-wet-v03 | WARD-002-wet-v03 | | 公路 → LOC-003 |
| D2 夜 | 暴雨 | V5 + 左前備胎（異色）、膠帶封裂縫、單頭燈 | wet-v03 + INJ-001-v03 濕髒繃帶 | wet-v03 | | LOC-003 隧道/避難所 |
| D3 晨 | 霧、雨後 | V6 熄火、推車 | WARD-001-dried-v04 + INJ-001-v04 | WARD-002-dried-v04 | | 公路 |
| D3 日 | 晴、風 | V6 棄置（靜態） | dried-v04 | dried-v04 | 外套：B→A（或留在車上） | LOC-004 前段（步行） |
| D3 黃昏 | 晴 | 無車 | dried-v04 | dried-v04 | | LOC-004 終點 |

規則：狀態只向前；任一 shot 的 car/wardrobe/injury/weather 狀態必須等於所屬 scene 的 continuity state；狀態改變只能發生在指定的 A-tier 轉換鏡頭。

### 2.3 Sequence 卡（9 段 + 片頭尾 = 75'）

| SQ | 名稱 | 故事時間 | LOC | 預算 | 目標 → 轉折 | 狀態 in → out |
|---|---|---|---|---|---|---|
| SQ-010 | 出發 | D1 晨 | LOC-001 | 7' | 建立兩人關係與目的 → 決定上路 | V0/base → V0/base |
| SQ-020 | 第一段路 | D1 日 | LOC-002 | 9' | 關係摩擦 → 世界觀/科幻元素揭露 | V0→V1；base→dust |
| SQ-030 | 碎裂 | D1 黃昏 | LOC-002 路肩 | 8' | 意外 → A 受傷，第一次依賴 | V1→V2；INJ v01→v02 |
| SQ-040 | 夜 | D1 夜→D2 晨 | LOC-002 車內/路肩 | 7' | 夜談 → 外套交予 B；晨起過熱 | V2→V3；PROP-004 A→B |
| SQ-050 | 陰雨 | D2 日 | 公路→LOC-003 | 9' | 天候壓迫 → 繞路或硬闖的選擇 | V3→V4；dust→wet |
| SQ-060 | 暴雨 | D2 夜 | LOC-003 | 10' | 最大衝突 → 換胎；真相揭露 | V4→V5；INJ v03 |
| SQ-070 | 雨後 | D3 晨 | 公路 | 8' | 和解嘗試 → 引擎熄火、推車 | V5→V6；wet→dried |
| SQ-080 | 棄車 | D3 日 | 公路→LOC-004 前段 | 7' | 棄車步行 → 放下 | V6 靜態；外套歸還 |
| SQ-090 | 終點 | D3 黃昏 | LOC-004 | 8' | 抵達 → 結局 | 無車 |
| SQ-100 | 片頭/片尾 | — | — | 2' | 字卡（純 post） | — |

每張 sequence 卡另含：資訊/情緒/節奏曲線、依賴（前一 SQ 的離開狀態）、關鍵風險、A-tier 鏡頭清單。

### 2.4 Scene / Beat 規則

- Scene 估 38–45 個（每 SQ 4–5 個）；每張 scene 卡含：目的、start/end story state、story time、LOC state、cast、服裝/傷、道具與所有權、進出、floor plan、axis/eyeline、coverage plan、fail routes、continuity-state YAML（§3.4）。
- Beat：一個可見行為/反應/資訊單位，有 start/end state。一個 beat 出現兩個以上獨立的「然後」事件 → 先拆 beat，再決定是否拆 shot。估 170–220 個。
- Shot：一個 beat 的一個觀看位置；一個主要 delta；獨立可生成、可審、可剪。

### 2.5 Shot 量級（規劃假設，非實測）

| 假設平均鏡頭長度 | 成片鏡頭數（4500 s） | Manifest 合約數（含 coverage/備援 ×1.5） |
|---|---|---|
| 4 s | ~1,125 | ~1,700 |
| 6 s | ~750 | ~1,100 |
| 8 s | ~560 | ~850 |

實際單 clip 長度、可用秒數比例、waste rate 由 ledger 決定；animatic 完成後以實際節奏重算。

### 2.6 本片的 coverage 邏輯

**車內虛擬機位**（bible 鎖死；車內是公路片最常生成的空間，也是軸線風險最高的地方）

| 機位 | 位置 | 用途 |
|---|---|---|
| CAM-INT-01 | 儀表板中央朝後 | two-shot |
| CAM-INT-02 | 乘客側 A 柱朝駕駛 | A 單人 / OTS-B |
| CAM-INT-03 | 駕駛側 A 柱朝乘客 | B 單人 / OTS-A |
| CAM-INT-04 | 後座中央朝前 | 兩人背影 + 擋風玻璃 + 路 |
| CAM-INT-05 | 車外 hood / side mount | 行駛中透窗看人 |
| CAM-INT-06 | insert 位 | 手/方向盤/儀表/裝置 |

空間規則：**左駕**（駕駛座在左；需你確認）；車內 A 永遠畫左、B 永遠畫右，含 CAM-INT-04 背影。每個 prompt 的首幀占位都重述此規則——「同上一鏡」不是外部記憶。

**行進方向規則**：去程全片 frame-left → frame-right；只有明確「折返/轉向」beat 可反向，且需 establishing 交代。太陽方向依 Day/時段 × 行進方向在 LOC passport 固定（例：D1 黃昏向西行，太陽在車頭方向（畫右）→ 朝前的車內鏡頭為逆光）。

**每個 scene 的 coverage 清單**：master/establishing（空間識讀）→ 單人/two-shot/OTS（表演與視線）→ insert/reaction（道具、手、資訊、壓縮時間、剪接掩護）→ 出場/轉場 handle → 備援角度。

**高風險拆解規則（本片）**

| 風險 | 拆法 |
|---|---|
| 手/接觸（割傷、包紮、遞物、推車、開引擎蓋） | insert 鎖定機位、一個接觸事件；反應鏡頭承擔敘事；中景不露細節 |
| 車損「轉變過程」 | 不生成轉變：切前狀態 / 撞擊聲 + 反應 / 切後狀態 insert；轉換鏡頭只做「後狀態首次出現」 |
| 精確文字（車牌、路牌、裝置 UI、地圖） | 避免入鏡或走 composite |
| 長對白 | 每鏡 ≤ 一句；對白以 ADR 為準；生成時可 picture-only |
| 物理（雨、蒸汽、推車、滑行煞停） | 一事件一鏡；鎖機位；plate + post 雨/蒸汽 |
| 群眾/第三者 | 劇本層避免；必要時單一 NPC 另建 passport |
| 重複科幻元素（天空異象） | 不逐鏡生成；canonical plate composite |

**控制資產（只用能解決問題的）**：每個 LOC 與車內的 floor plan/diagram（全部）；全片 storyboard（供 animatic 與順序，不是風格鎖）；keyframe 只給 A-tier；clay/blockout 給推車、開引擎蓋、換胎等接觸鏡頭。Keyframe 相對嚴格但不是 pixel lock。

### 2.7 Worked example：SC-030-014「擋風玻璃碎裂」（D1 黃昏，V1→V2，INJ-001 首次）

Scene 卡摘要：LOC-002-dusk-clear-v01 路肩；車外 master 車頭朝畫右；車內 A 左 B 右。start：V1 行駛中，A dust-v02 駕駛，B dust-v02 手持 PROP-002。end：V2 停在路肩；A 右掌 INJ-001-v01 未包紮；B 站車頭右側手按引擎蓋；PROP-002 在儀表板；PROP-006 布條由 B 交到 A 右手。

| Beat | 內容 | 風險與拆法 |
|---|---|---|
| BT-01 | 前方出現碎片（科幻：無人機殘骸）→ 撞擊擋風玻璃 | 撞擊物理高風險 → pre-impact / 撞擊後起的反應（用 V2 asset）/ 裂紋 insert |
| BT-02 | A 緊急煞停靠路肩 | 車外 master，左→右滑停、塵土；備援：鎖機位車已停 |
| BT-03 | A 撥碎玻璃割傷 | 手部 insert 鎖機位；失敗 → clean plate + 血跡 composite；反應鏡頭承擔敘事 |
| BT-04 | B 下車繞到車頭，看見右頭燈破 | **V2 外觀首次出現 = A-tier hero**；keyframe |
| BT-05 | B 遞布條，A 拒絕後接受 | 所有權轉移 B→A，中景不露手部細節；包紮 insert 放 SC-030-015 |

| Shot | Tier | 機位/內容 | 主要 delta | End state / handoff |
|---|---|---|---|---|
| SH-030-014-010 | C | CAM-INT-04 背影，前方碎片出現 | 碎片進入擋風玻璃前方 | 碎片距玻璃 <1 m；V1 |
| SH-030-014-020 | A | CAM-INT-01 two-shot，從撞擊後瞬間起 | A 猛握方向盤、B 抬手護臉 | 玻璃已裂（V2）；兩人仍在座位 |
| SH-030-014-025 | C | 裂紋 insert（V2 asset，可純影像/post） | 無 | 靜態 |
| SH-030-014-030 | A | 車外 master，左→右滑停 | 車停、塵土落 | 車頭朝右停在路肩；forbidden：完整右頭燈 |
| SH-030-014-040 | B | CAM-INT-02 A 單人 | A 喘氣、低頭看手（手在畫外） | A 視線向下 |
| SH-030-014-050 | A | CAM-INT-06 手部 insert，鎖機位 | 手指觸碎片→縮回→血線 | INJ-001-v01 可見；達 ceiling → composite |
| SH-030-014-060 | B | CAM-INT-03 B 反應 | 視線：A 的手 → A 的臉 | B 視線向左上 |
| SH-030-014-070 | A | 車外，B 從右門下車走到車頭右側 | 看見右頭燈破（V2 hero） | B 站車頭右側、手按引擎蓋 → HANDOFF-070 |
| SH-030-014-080 | B | OTS-A 由車內看 B 在車頭 | B 抬頭看 A | 視線對上 |
| SH-030-014-090 | B | B 回到駕駛側車門遞布條，A 右手接（中景） | PROP-006 B→A | A 右手持布條；B 站門邊 |
| SH-030-014-095 | C | 黃昏鹽灘寬景，車為小點 | 無 | 轉場 handle |
| -030-ALT / -050-ALT | 備援 | 鎖機位已停車 / 反應替代 insert | | |

全部硬切，不規劃 extension；若 070→080 需連續動作，最多從 070 的 approved tail 做一次 extension，仍需通過 QC 才能進 local handoff。

## 3. Bible / passport、狀態模型、登錄與 reference 政策

### 3.1 Passport 清單

| ID | 類型 | 狀態/版本 | 必要內容 |
|---|---|---|---|
| CHAR-001 (A)、CHAR-002 (B) | character | identity v01 | 臉/髮/膚/體型/姿態/慣用手/步態；正面、側面、3/4、全身/中景/特寫、5 種表情參考；行為語法（視線、呼吸、手、反應延遲）；禁止漂移清單 |
| VOICE-001/002 | voice | v01 | 語言/口音/音域/語速/發音字典/權利；ADR 為主 |
| WARD-001/002-{base,dust,wet,dried}-vNN | wardrobe | 各 4 態 | 每態獨立全身 + 細部 sheet；不混態 |
| INJ-001-{fresh,bandaged,bandaged-wet,bandaged-dirty}-v01–v04 | injury | 4 態 | 右掌；特寫與中景可見度各一 |
| VEH-001-V0…V6 | vehicle | 7 態（§3.2） | 每態：前 3/4、側、後、儀表板/車內、損傷細部 |
| PROP-002 裝置 | prop | off/on | 幾何/尺度/材質/發光；UI 文字 → post |
| PROP-003 地圖/照片 | prop | 1 | 精確圖像 → post |
| PROP-004 外套 | prop/wardrobe | owner A→B→A | 所有權狀態機 |
| PROP-005 水壺/油桶 | prop | full/empty | |
| PROP-006 布條 | prop | B→A | |
| LOC-001 加油站 | location | D1-morning-clear | floor plan、進出、axis、機位、地標、材質、光向、room tone |
| LOC-002 鹽灘公路 | location | D1-day-clear / D1-dusk-clear / D1-night-clear / D2-morning-overcast | 同上，每態獨立 |
| LOC-003 隧道/避難所 | location | D2-day-rain / D2-night-storm | 半室內 room tone |
| LOC-004 終點 | location | D3-morning-fog / D3-day-clear / D3-dusk-clear | |
| LOC-CAR-INT | location | clean / dusty / cracked / fogged-wet / taped（綁定 VEH 態） | CAM-INT-01…06 diagram |
| CAM-001 | camera grammar | v01 | 公路片鏡頭語法、行進方向、車內機位 |
| STYLE-001 | style | v01 | 材質/顆粒/對比；不含實體與構圖 |
| COLOR-001 | color script | v01 | D1 暖乾高對比 / D2 冷濕低飽和 / D3 霧→暖 |
| VFX-001 | VFX grammar | v01 | 天空異象、裝置發光、裂紋、雨/蒸汽；重複元素走 composite |
| SOUND-001 | sound bible | v01 | 引擎 ENG-V0…V6、雨、風、車內 room tone × 天候、音樂動機 |
| SUB-001 | subtitle style | v01 | 字型/安全區/行長/閱讀速度/burned vs sidecar |

每個 passport：stable ID、version、owner、rights、`draft/approved/retired`、approval date、sha256。新服裝/傷/天候/燈光/道具狀態 = 新的不可變版本；不覆寫 base、不在同一張 sheet 混態。

### 3.2 車輛狀態機 VEH-001

| State | 時間 | 外觀 delta（累加） | 聲音 asset | 首次出現 hero shot | Forbidden（該態之後不得出現） |
|---|---|---|---|---|---|
| V0 | D1 晨 | 完整 | ENG-V0 | SQ-010 | — |
| V1 | D1 日 | 塵土、左側刮痕 | ENG-V0 | SQ-020 | 乾淨車身 |
| V2 | D1 黃昏 | + 擋風玻璃蛛網裂（駕駛側上方）、右頭燈破 | ENG-V0 + 風切聲 | SH-030-014-070 | 完整擋風玻璃、完整右頭燈 |
| V3 | D2 晨 | + 引擎蓋開/蒸汽/冷卻液漬 | ENG-V3 過熱 | SQ-040 末 | |
| V4 | D2 雨 | + 泥、右後門凹、左前輪蓋缺、單支雨刷失效 | ENG-V3 + 雨刷異音 | SQ-050 | 完整右後門、兩支雨刷正常 |
| V5 | D2 夜 | + 左前備胎（異色）、膠帶封裂縫、單頭燈 | ENG-V5 不穩 | SQ-060 | |
| V6 | D3 晨 | + 熄火、推車、棄置 | 無引擎、推車聲 | SQ-070/080 | 引擎聲 |

規則：每態為 immutable asset 版本；shot 的 `car_state` 必須等於 scene continuity state；每個 shot 的 forbidden 清單自動含所有前態特徵；QC 用「損傷清單」逐項核對。

### 3.3 三個分離的連續性儲存

| 儲存 | 內容 | 寫入規則 | 生命週期 |
|---|---|---|---|
| Canonical bank | §3.1 全部 passports | 只有人類核准；生成結果永不自動覆寫 | 全片 |
| Approved memory | 少量高資訊幀/片段（例：「A，wet-v03 + INJ v03，LOC-003 夜，3/4 左側」） | 來自 approved shot；通過身分/實體/地點 fidelity、無失格瑕疵、adherence、跨鏡相容；記錄來源 shot/timecode/crop/使用邊界 | 指定 SQ/scene 範圍 |
| Local handoff | 相鄰鏡頭的 last approved frame/pose、位置、方向、相機速度、光/色、道具持有、room tone | 僅來自 approved run；`return_last_frame` 類輸出需先過 QC | 同 scene 相鄰鏡頭；scene 結束即失效 |

這是外部製作設計（部分受長影片研究啟發），不是 Seedance 內部機制；效益大小未測。

### 3.4 Continuity state 與 shot delta（SC-030-014）

```yaml
# 03_breakdown/scenes/SC-030-014/continuity-state_v003.yaml（scene 開始）
scene_id: SC-030-014
story_time: "Day 1 / dusk"
location_state: LOC-002-dusk-clear-v01
travel_direction: frame-left-to-right
sun: ahead of car (frame-right), low, backlight for forward-facing interiors
screen_axis_interior: A-left / B-right (left-hand drive)
vehicle: { id: VEH-001, state: V1, moving: true, engine: ENG-V0 }
characters:
  CHAR-001:
    position: driver seat (frame-left)
    wardrobe: WARD-001-dust-v02
    injury: none
    gaze: road ahead
    held_props: [steering wheel]
  CHAR-002:
    position: passenger seat (frame-right)
    wardrobe: WARD-002-dust-v02
    gaze: PROP-002
    held_props: [PROP-002-on]
props:
  PROP-002: { state: on, owner: CHAR-002, hand: both }
  PROP-006: { state: folded, owner: CHAR-002, location: jacket pocket, visible: false }
lighting: LIGHT-LOC002-dusk-backlight-v01
audio: SOUND-CARINT-dusty-moving-v01 + ENG-V0
```

```yaml
# scene 結束狀態（只列改變）
vehicle: { state: V2, moving: false, position: shoulder, nose: frame-right }
CHAR-001: { position: driver seat, injury: INJ-001-v01, held_props: [PROP-006] }
CHAR-002: { position: driver-door exterior, held_props: [] }
PROP-002: { state: on, owner: none, location: dashboard }
PROP-006: { state: unfolded, owner: CHAR-001, hand: right }
```

```yaml
# 04_manifest/shots/SH-030-014-070.yaml（delta 節錄）
shot_id: SH-030-014-070
reads_state: SC-030-014/continuity-state_v003 @ after BT-03
required: [CHAR-002, VEH-001-V2, LOC-002-dusk-clear-v01]
forbidden: [CHAR-001 outside car, VEH-001-V0, VEH-001-V1, intact right headlight, extra people, extra vehicles]
start_state: B opens passenger door (frame-right); PROP-002 left on dashboard
primary_delta: B walks around the hood to front-right and sees the broken right headlight
end_state: B stands at front-right of hood, right hand on hood, gaze down at headlight; car nose frame-right; A remains in driver seat, visible through cracked windshield
entrance_exit: B exits via passenger door; no one else enters
handoff_out: HANDOFF-030-014-070 (pose, position, gaze, camera vector, light, room tone)
```

每個 shot 讀取前一個 approved state，只提交自己核准的 delta；scene rollback 只重播 accepted deltas。

### 3.5 Asset registry 與 run ledger 欄位

```text
registry: asset_id, entity_id, state, version, owner, rights_status, source_paths,
          allowed_attributes, excluded_attributes, status, approval, sha256
ledger:   run_id, parent_run, shot_id, timestamp, platform/model/document_version,
          prompt_text/hash, parameters, reference_ids/hashes/roles, one_changed_variable,
          output_path/hash/duration/spec, queue/generation/review/human_time, billed_cost,
          hard_gates, scores, timecoded_defects, reviewer, decision, route
```

不保留憑證、cookie、session、簽名 URL；平台輸出若會過期，核准後立即 ingest、hash、保留 sanitized 識別碼。

### 3.6 Reference packet 政策

- Packet = 最小集合：在場角色 identity；可見的 state-specific 服裝/傷；**與鏡頭角度相符**的 VEH 態視角（車可見時）；LOC 態（外景/可見時）；style frame 只給無角色的 C-tier plate；A-tier 加 diagram/keyframe。
- 每個 reference 一個 job + allowed/excluded inheritance（identity 不繼承姿勢/背景/光；location 不繼承主體；motion 不繼承身分）。
- `PKT-<shot>-vNN` 含所有 hash；改任一 reference = 新 packet 版本。
- 禁止：同一 packet 混態；要求 V2 卻附 V1 視角；用未晉升的生成幀當 identity 真值；「同上一鏡」取代明示狀態。
- 數量上限依平台；ModelArk 2.5 封存值見 §0，官方也建議較小工作集，上限不是品質目標。

## 4. Shot manifest、handoff、依賴佇列、命名/版本/lineage

### 4.1 Manifest 欄位（`04_manifest/shot-manifest.csv`）

```text
identity:   shot_id, seq_id, scene_id, beat_id, tier, priority, owner, status
narrative:  purpose, start_state, primary_delta, end_state
state:      story_day, time_of_day, weather, loc_state_id, car_state,
            char_required[], char_forbidden[], wardrobe_ids[], injury_id,
            props_required[], props_forbidden[], prop_owner_map
space:      axis, screen_direction, eyeline, entrance_exit, floor_plan_id
camera:     camera_position, size, side_height, move, lens_feel, focus, duration_intent, handles
sound:      speaker, dialogue_text, language, silent_chars, ambience, sfx, music_intent, subtitle_plan
inputs:     packet_id, packet_hash, control_assets[], prompt_id, prompt_version, prompt_hash
runtime:    platform, model_id, task, aspect, resolution, duration_param, audio_param, seed   # Gate 0 前 unknown
queue:      depends_on[], handoff_in, handoff_out, parallel_group, batch_id
policy:     retry_ceiling, cost_ceiling, route_rules, acceptance_gates[], rubric_id
lineage:    approved_run_id, approved_hash, in_tc, out_tc, handles_tc, cut_version, replaced_by
```

Prompt 文字與 runtime 參數分開存；不假設任一平台 schema 可移植。

### 4.2 Handoff 與 extension 政策

`HANDOFF-<shot>.yaml`：approved run 的 last frame path/hash、pose、位置、screen direction、camera velocity、光/色、道具持有、room tone、使用邊界。只在同 scene 相鄰鏡頭使用。Extension 只用於 beat 內 ≤1–2 次相鄰延續；跨 scene 一律硬切 + coverage；任何 drifted tail 不得成為下一鏡的真值。

### 4.3 依賴佇列

**Film-level lanes**

| Lane | 內容 | 並行/序列 | 解鎖條件 |
|---|---|---|---|
| 0 資產 | canonical passports → LOC 態 → VEH 態 → INJ/WARD 態 | 序列（核准） | 人類核准 + 一個可行性 blocking shot 通過（「production-proven」flag） |
| C plates | 全片行駛 plate、風景、insert、天候 cutaway | 高度平行，可最早開跑 | 對應 LOC 態 + VEH 態 proven |
| B coverage | 各 scene 對話/表演 coverage | 以 scene 為單位平行 | 該 scene master/blocking 核准 + 所需角色態 proven |
| A 狀態鏈 | V1→V2→…→V6、INJ v01→v04、PROP-004 A→B→A、天候轉換 | **依故事順序序列** | 前一態 hero shot approved |
| 晉升 | approved memory 晉升 | 序列、一次一個 | dailies 通過 |

**SC-030-014 scene DAG**

```text
[LOC-002-dusk proven] [VEH-V1 proven] [VEH-V2 proven] [INJ-001-v01 proven]
        │                    │                │                  │
   010 ∥ 025 ∥ 095 (C, 平行)  │                │                  │
                              ▼                ▼                  │
                           030 (A master) ──► 070 (A hero V2) ──► 080 (B, OTS)
                              │                     └─HANDOFF-070─► 090 (B)
                           020 (A) ──► 040 (B) ──► 050 (A insert; ceiling→composite)
                                                 ∥ 060 (B reaction, 與 050 平行)
```

Batching 規則：同平台/模型/task/畫幅/解析度/格式/packet 版本/rubric 才同批；否則失敗無法歸因。並行上限依平台當日文件。

### 4.4 命名、版本、lineage

```text
FILM-ROAD / SQ-030 / SC-030-014 / BT-030-014-03 / SH-030-014-050
CHAR-001 / VEH-001-V2 / LOC-002-dusk-clear-v01 / WARD-001-dust-v02 / INJ-001-v01
PKT-030-014-050-v02 / P-030-014-050-v003 / r0417 / HANDOFF-030-014-070 / AM-0031 / CP-03-SQ030

FILM-ROAD_SH-030-014-050_take-002_run-r0417_prompt-p003_pkt-v02_<model-id>_<res>_v001.mov
FILM-ROAD_VEH-001-V2_front34_v003_APPROVED.png
FILM-ROAD_SC-030-014_continuity-state_v003.yaml
```

- ID 永不重用（剪輯順序改變也不改 ID）；狀態 metadata 是權威，檔名 `APPROVED` 只是可讀輔助。
- 媒體狀態流：`incoming → reviewed(rejected | select) → approved → in_cut → retired`；四個目錄分離。
- Selection lineage（`07_ledger/selections.csv`）：select_id, shot_id, run_id, output_hash, reviewer, decision, reason, defect_tc, in/out, cut_version, replaced_by。每版 EDL/XML 以 run_id + hash 引用媒體；換鏡 = 新 cut 版本；structure lock 後附 change record。
- Retry 一律從 parent approved run 分支；rejected child 不能當 parent；AM 晉升記錄來源 shot/timecode/crop。

## 5. 核准閘門、retry 上限、失敗路線、checkpoint、rollback

### 5.1 Gates

| Gate | 產出 | 離開條件 | Checkpoint |
|---|---|---|---|
| G0 Development | charter、platform gate、rights register、master spec、budget/clock、mode | 全部鎖定 | — |
| G1 Script/bible | 劇本對應 §2.2 狀態時間軸；全部 passports approved | 狀態機無缺口；rights 清 | **CP-01** |
| G2 Breakdown/risk | SQ/SC/BT 卡、floor plans、entity schedule、coverage、fail routes、manifest v1、risk register | 每 scene 空間/實體/狀態可解 | — |
| G3 Previz/anchors | 75' animatic（storyboard + scratch VO + temp music）；A-tier keyframes；接觸鏡頭 blockout | 全片可從頭看到尾 | **CP-02** |
| G4 Blocking generation | 每 VEH/INJ/WARD/LOC 態一個可行性鏡頭；全片 C 品質 blocking cut | 「production-proven」flags 齊；blocking cut 存在 | — |
| G5 Final generation | 鎖定合約；輸出進 incoming，永不覆寫 approved | — | — |
| G6 Dailies/selects | 完整媒體審查；hard gates；AM 晉升 | 每 SQ approved 鏡頭齊 | **CP-03-SQxxx** |
| G7 Structure lock/pickups | rough cut → pickups → fine cut → picture lock | 缺口補齊；change records | **CP-04** |
| G8 VFX/conform/color/sound/subs | 見 §6 | 各部門 lock | **CP-05** |
| G9 Final QC/master/archive | 完整播放 + 針對性檢查 + 獨立核准 | 交付 + 封存 | **CP-06** |

### 5.2 每鏡 hard gates（先於任何分數）

1. rights/safety/delivery/必要故事 beat；2. 正確身分/實體/reference 角色，無多餘實體；3. 連續性關鍵：服裝/傷/道具/地點/方向/end state 無歧義；4. 無不可剪的結構性瑕疵/嚴重 artifact/錯字/壞音；5. 完整可用區間 + 鄰接相容；6. 音/字需求通過或有核准的 post 路線。

**本片專屬 checklist**：駕駛座側與 A 左 B 右｜行進方向｜車損清單逐項對 V 態（含 forbidden 前態）｜服裝態（base/dust/wet/dried）｜繃帶態｜外套持有者｜天候/雨量/光向｜裝置 on/off 與位置｜無多餘人/車/倒影複本｜文字不入鏡或已標 composite｜音訊只依實際音訊證據判定（播放圖示不算）。

### 5.3 Retry 上限與停止條件（初始值，前 50 個有效 run 後校準）

| Tier | 有效 run 上限/合約 | 提前路由 | 單鏡成本上限（公式） |
|---|---|---|---|
| A | 6（每次只改一個變數） | 同一 hard defect 在 2 次孤立變更後仍在 | `budget_gen / contracts × 3` |
| B | 3 | 同上 | `× 1` |
| C | 2 | 任何 hard defect → 換角度/plate | `× 0.5` |

停止：同一阻斷瑕疵在孤立重試後仍在；修一個關鍵約束反覆破另一個（振盪）；達上限；下一步需要用 rejected/drifted 幀當真值；rights/delivery 過不了；edit/VFX/ADR 的期望成本更低。停止 = 保留 checkpoint、失敗假設、證據、下一路線，不丟歷史。

### 5.4 失敗路線（本片症狀對照）

| 症狀 | 第一步（改一個變數） | 重複後 | 最終路線 |
|---|---|---|---|
| 車損回復（頭燈復原、裂紋消失） | 單一 VEH-Vn 態 asset + forbidden 明示前態 | 換角度不露該部位 | 追蹤 composite 裂紋/破燈 |
| 駕駛座側翻轉 | 首幀占位「駕駛座在左，A 畫左」 | 車內 diagram | 重生成；**禁止**水平翻轉掩蓋（右手傷、右頭燈會錯邊） |
| wet/dry 跳動 | 單一 wet 態 asset | 縮短/去除跑動 | 有限的 post wet pass |
| 手部/割傷/包紮 | insert 鎖機位一個接觸 | keyframe/blockout | clean plate + 血跡/繃帶 composite |
| 雨量/蒸汽不一致 | LOC 態 asset + 明示強度 | plate | post 雨/蒸汽層 + 聲音 |
| 對白/唇形 | 一位說話者、一句、其餘靜默 | picture-only | ADR |
| 精確文字 | 避免入鏡 | — | composite |
| 天空異象不一致 | 不逐鏡生成 | — | canonical plate composite |
| extension 漂移 | 回最後 approved checkpoint | 縮短延續 | 硬切獨立鏡 |
| 鄰接不匹配 | 修那一個 end state/向量/光/音量 | insert/cutaway | pickup/re-edit |
| 多餘人/車 | 精確數量 + forbidden | 更乾淨的單角色 asset | paint-out/拆鏡 |

### 5.5 Checkpoints 與 rollback

每個 CP 存：劇本/bible 版本、state snapshot、approved hashes、timeline/EDL、open defects/routes、預算、工具/模型/平台/文件版本、核准記錄。

Rollback：從 parent approved run 重試；state/axis/wardrobe 被污染 → 回 scene-start checkpoint 重播 approved deltas；structure lock 後任何變更需列 VFX/sound/subs/color 下游影響的 change record；模型/平台更新 → 新分支 + 回歸套件（固定 10–20 個跨 tier 鏡頭），永不覆寫 approved renders。

## 6. Rough cut → pickups → finishing → archive

| 階段 | 內容 | 本片重點 |
|---|---|---|
| Animatic（G3） | storyboard 幀 + scratch VO + temp music，全 75' | 先驗證三天/四地/車況弧線的節奏；在花錢前暴露缺 beat |
| Blocking cut（G4，rolling） | 每 SQ 以 C 品質生成替換 animatic | 暴露 coverage 缺口、軸線/視線錯、不可剪的漂亮鏡頭、用剪輯比重生成便宜的地方 |
| Rough cut（G6→G7） | 以 approved 鏡頭替換 | 記錄 in/out/handles、temp VFX、reframe、變速意圖、音訊佔位；pickups 依優先序 |
| Pickups | 只補缺口（反應、insert、出場、轉場 handle、狀態交代） | 預留比例是假設（初估 10–20% 合約數），以 ledger 校準 |
| Fine cut → Picture lock（CP-04） | 換鏡需 change record | 禁止未記錄的 time-stretch 掩蓋對白/連續性問題 |
| VFX/cleanup | (1) 重複科幻元素 composite；(2) 裂紋/血跡/繃帶追蹤貼合；(3) 多餘實體/倒影 paint-out；(4) 文字/UI；(5) 雨/蒸汽增強；(6) 畫幅裁切/穩定 | regenerate 只在核心合約錯且仍適合模型；局部問題用局部修 |
| Conform | 統一 codec/fps/時長/色彩標籤/聲道/檔名；保留原始與轉換記錄 | 只在有定義需求時 upscale/插幀，並檢查 ghosting/邊緣/紋理爬動 |
| Color | D1 暖乾高對比 / D2 冷濕低飽和 / D3 霧→暖；scene 內 shot match、膚色/材質、legal range、校正監看 | 不要把車損/繃帶調不見；`4k` 標籤不等於生成解析度 |
| Sound | 對白 ADR（VOICE passport 發音字典）；foley：引擎 ENG-V0…V6、車門、玻璃、雨刷（一支異音）、鹽灘/泥地腳步；ambience 依 LOC × 天候；音樂：兩人動機 + 車的動機隨損壞逐步走音（創作建議）；stems DX/FX/AMB/MX；loudness 依交付規格 | 生成聲音只當時間參考；room tone 跨剪點連續 |
| Subtitles | 以**最終音訊**對時，不用 prompt 時間戳；zh-TW + EN；說話者、斷行、閱讀速度、安全區、遮擋、跨剪點、burned vs sidecar | |
| Mastering/QC/Archive | 母帶 + mezzanine、stems、字幕檔、專案/timeline、prompt/reference/state/run ledgers、approved/rejected 決策、工具/模型/文件版本、hashes、核准、waivers、checkpoints | 不封存簽名 URL/憑證 |

## 7. QC 系統

| 層級 | 時機 | 檢查 | 證據要求 |
|---|---|---|---|
| L1 Shot dailies | 每個 incoming | hard gates → adherence → intra-shot（時間穩定/解剖/物理/相機/音） | 看完整 clip（開頭/中段/結尾/高風險 tc）；截圖只能證明該幀 |
| L2 Scene neighbor | scene 鏡頭齊 | continuity state、axis、eyeline、handoff、room tone、剪點 | 相鄰鏡頭並排 |
| L3 Sequence state arc | 每 SQ approved | 逐鏡核對 §2.2 狀態表（車/服裝/傷/天候/道具持有） | 狀態表 × 鏡頭矩陣 |
| L4 Picture | rough/fine cut | 故事、節奏、coverage、變速記錄 | 全片播放 |
| L5 Final | 母帶 | 技術（時長/畫幅/fps/codec/色彩標籤/重複/掉幀/黑幀/音訊/字幕/命名/checksum）+ 內容（故事/連續性/解剖/文字/聲音/rights/揭露/浮水印） | 至少一次不中斷完整播放 + 每個剪點/VFX/字幕/音訊轉場的針對性檢查 |

規則：fidelity 先於 consistency（一致地錯的人仍是錯）；嚴重度 Critical / Major / Moderate / Minor / Unknown；生成者不核准自己的最終 take；自動指標只排序不核准；結論標示 direct observation / inference / unknown。

## 8. KPI 儀表板（只用 ledger 實際數據）

| 面板 | 指標 |
|---|---|
| 效率 | `first_pass_approval`、`additional_retries`（median/P90）、`time_per_approved_shot`、`usable_seconds_per_hour`、`cost_per_approved_second`、`human_correction_time`、`queue_wait_ratio`、`waste_rate` — 各依 tier 分列 |
| 品質向量 | adherence、身分/服裝/傷/地點/道具/聲音連續性、時間穩定與 artifact 率、物理/接觸、相機/構圖/光、對白/唇形/環境/音樂/字幕、剪輯可用性 |
| 本片專屬 | 車損回復率（/VEH 態）、駕駛座翻轉率、wet/dry 跳動率、繃帶態錯誤率、外套持有者錯誤率、行進方向違反率、需 composite 的鏡頭比例、ADR 覆蓋率 |
| 編輯 | 成片秒數 vs 4500 s、coverage 缺口數、pickups/SQ、structure lock 後 change records 數 |
| 預算/時程 | 各 tier 燒耗 vs ceiling、每 SQ 實際 vs 預算 |

規則：每 tier ≥30 個有效 run 才報統計；報 median/分佈/P90；成本與時間只來自 ledger（含人工時），不用行銷計數器、UI 資產總數、價格頁、宣稱時程；比較工作流先過品質 floors，再用 Pareto（每個必要維度不更差且至少一個更好才算支配）；結論只對本片的 suite/model ID/平台/日期/審查者/floor/預算成立。

## 9. 專案目錄骨架（落地用；執行階段第一步就是建這些檔）

```text
FILM-ROAD/
  00_charter/        charter.md  platform-gate.md  rights-register.md  risk-register.md
  01_script/         script_vNN.md  state-timeline.md                       # §2.2
  02_bible/          passports/{CHAR,VOICE,WARD,INJ,VEH,PROP,LOC,CAM,STYLE,COLOR,VFX,SOUND,SUB}-*.yaml  refs/
  03_breakdown/      sequences/SQ-*.md  scenes/SC-*/{scene-card.md,floor-plan.*,continuity-state_vNN.yaml}  beats/
  04_manifest/       shot-manifest.csv  shots/SH-*.yaml  packets/PKT-*.yaml  prompts/P-*.md
  05_control/        storyboards/  keyframes/  blockouts/  diagrams/
  06_queue/          dependency-graph.yaml  batches/
  07_ledger/         runs.csv  selections.csv  promotions.csv  handoffs/HANDOFF-*.yaml
  08_media/          incoming/  rejected/  selects/  approved/  approved-memory/
  09_edit/           animatic/  blocking-cut/  rough-cut/  EDL/  change-records/
  10_post/           vfx/  conform/  color/  sound/{adr,foley,ambience,music,mix}/  subtitles/
  11_checkpoints/    CP-01-bible/ CP-02-previz/ CP-03-SQxxx/ CP-04-picture/ CP-05-sound-color/ CP-06-master/
  12_kpi/            dashboard.md  reports/
  13_master/  14_archive/
```

## 10. Gate 0 需要你決定的事

1. 平台/模型/區域 → 填 runtime 欄位與並行/保留/成本邊界
2. 母帶規格：畫幅比、fps、解析度、聲道、交付平台與 loudness 規格
3. 對白語言與聲音權利：真人 ADR 或已授權 TTS
4. 劇本或 treatment → 替換 §2.2 骨架；確認左駕與行進方向
5. 科幻元素清單 → 決定哪些走 composite
6. 預算/時程上限 → 推導各 tier ceilings

建議以 **SQ-030** 當 pilot（含 V1→V2、INJ 首次、黃昏光、接觸鏡頭），跑完 G0–G6 後用真實 ledger 校準 §2.5 / §5.3 / §8 的所有初始值，再放大到全片——這是建議，不是已驗證的最佳解。

---

**回顧**：我讀了 film-producer 的五份參考與 QC / prompt-director 的 schema，據此建出一套 platform-neutral 的 75 分鐘製作系統：hybrid A/B/C 分級、9 段 sequence 對應三天 × 四地 × 車況 V0–V6 的狀態時間軸、車內虛擬機位與行進方向規則、三層連續性儲存、含 forbidden 前態的 shot delta、依狀態鏈序列化的佇列、hard gates + 分級 retry 上限 + 本片專屬失敗路線、六個 checkpoint、從 animatic 到封存的 finishing 流程、五層 QC 與 ledger-only KPI。全片用硬切 + coverage，extension 只限 beat 內 ≤1–2 次；沒有任何流程被宣稱為本專案實測最優。下一步是你在 Gate 0 鎖定平台/母帶/聲音權利/劇本，然後依 §9 建目錄骨架、以 SQ-030 做 pilot。

一個誠實的備註：這個 session 沒有 Write 工具，所以我無法把計畫寫進 `<REDACTED_PRIVATE_PATH>`，也沒有 ExitPlanMode 可呼叫；上面的內容就是完整計畫，需要時可以直接存檔。
