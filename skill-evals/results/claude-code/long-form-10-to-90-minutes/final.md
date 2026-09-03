以下是依 skill 規範產出的完整製作系統。先講結論:採用「混合分級模式」為起始策略,以「四個外部連續性儲存 + 車損單調狀態機 + 三日天候/服裝矩陣」作為本片的連戲骨幹,所有長度都由剪輯系統組裝、不靠模型記憶。全文任何「建議」都是起始策略,**本專案尚未實跑驗證任何流程為最優**。

---

# 75 分鐘 AI 科幻公路電影 — 製作系統

## 0. 證據基礎、日期與未知項

| 類別 | 內容 |
|---|---|
| 知識日期 | 本 skill 的 Seedance 封存知識日期為 2026-08-22,今天是 2026-09-02。開工前必須重查官方文件的時長上限、解析度、價格、配額、參數與政策。 |
| 平台隔離 | Seedance 2.0、UI 顯示的「Seedance 2」、Seedance 2.5、ModelArk API、LAS、Higgsfield 的預設值、限制、成本、標籤互不通用,不得跨面移植。 |
| 明確未知 | 你的實際生成平台與模型版本、地區、單段時長/解析度上限、是否提供 last-frame 回傳、預算與時程天花板、交付規格(比例/幀率/編碼/響度)、劇本現況、肖像/聲音/音樂權利。這些是 charter 的空欄,不是可以假設的值。 |
| 陳述性質 | 下文分為:平台事實(需重查)、實務起始建議、依你需求做的推論。沒有任何一項被本專案實測證明為最優。 |

**兩條紅線(依你的要求,也是 skill 不變式):**不用一個超長 prompt 產長片;不用無限 extension 鏈當長片方案。75 分鐘由「Film → Sequence → Scene → Beat → Shot」分解後逐鏡生成、在剪輯系統組裝。模型不提供可靠跨鏡記憶,連續性由下述製作系統負責。

## 1. 運作模式:混合分級(A/B/C)

- **為何適合**:75 分鐘估計需要數百顆鏡頭(見 §4 估算)。全面 quality-max 會讓審查與重試成本爆炸;全面 speed-max 又會危及本片的三個高風險連戲軸——兩位主角身份、車損遞進、三日天候/服裝。混合模式把品質預算集中在這三軸上。
- **分級**:
  - **A 級(quality 流程)**:主角特寫與關鍵表演、車損狀態「升級」的那一顆鏡頭、每日/每天候的第一顆定調鏡頭、劇情轉折點。多候選、獨立審查、previz/keyframe 先行。
  - **B 級(標準流程)**:一般對話 coverage、車內雙人戲。標準參考包 + 標準 QC,卡關才升級。
  - **C 級(快速平行)**:公路空景、地景 plate、insert(儀表、油表、手、地圖)、cutaway。單候選先行,可大量平行。
- **未經測試的政策假設(明列)**:A/B/C 的分界、各級候選數、rolling assembly 的重疊比例,都是起始政策,需用前兩個 sequence 的實際 ledger 數據校準。

## 2. Project Charter(開拍前鎖定)

故事目的與觀眾、75 分鐘目標長度與交付面、平台/模型/文件日期 gate、畫幅與母帶規格、劇本/肖像/聲音/音樂/參考素材權利、允許的生成與後期工具、預算與時程天花板、儲存與審查責任人、風險分級、運作模式(§1)。**charter 未鎖定前不進入付費生成;規劃與文字測試不等於生成授權。**

## 3. Creative Bible 與 Passport 清單

每本 passport 都有穩定 ID、版本、負責人、權利狀態、`draft/approved/retired`、核准日期與 hash。**新的服裝/損傷/天候/光線/道具狀態 = 新的不可變版本,絕不覆寫基底狀態。**

### 3.1 角色(CHAR-001、CHAR-002)
- 臉/髮/膚/體型/慣用手/步態 + 正面/側面/四分之三/全中特景與表情參考。
- 聲音:語言、口音、音域、語速、發音字典、權利;行為文法(視線、呼吸、手部習慣、反應節奏)。
- **服裝矩陣**(封閉清單,每格一個版本):

| | Day 1 | Day 2 | Day 3 |
|---|---|---|---|
| CHAR-001 | WARD-A-d1 基底 / 沙塵變體 | WARD-A-d2 基底 / **濕透變體** | WARD-A-d3 基底 / 破損+傷 |
| CHAR-002 | WARD-B-d1 基底 / 沙塵變體 | WARD-B-d2 基底 / **濕透變體** | WARD-B-d3 基底 / 破損+傷 |

(實際套數依劇本;每個變體都要有自己的核准參考圖。)

### 3.2 車(PROP-CAR-001)— 本片的核心狀態機
- 幾何/比例/材質/內裝/儀表 + 每個損壞狀態的完整參考組:外觀四角、車內駕駛視角、儀表特寫、該狀態的關鍵損傷特寫。
- **損壞狀態單調遞增、不可逆**(範例,依劇本調整):

```text
CAR-S0 完好(Day1 出發)
CAR-S1 沙塵+刮痕(Day1 末)
CAR-S2 車頭凹陷+擋風玻璃裂(Day2 事件後)
CAR-S3 引擎間歇冒煙+缺一側後視鏡(Day2 末/Day3)
CAR-S4 瀕臨報廢(Day3 終局)
```

- 每個狀態同時掛一個**聲音狀態**(引擎音、異音、雨刷聲)進 sound bible。
- 任一鏡頭的 shot contract 必須宣告使用哪個 CAR-Sx,且 forbidden 欄禁止較早狀態的乾淨版本出現。

### 3.3 場景(LOC-001…LOC-004)+ 天候矩陣
四個主要場景各一本 passport:平面圖、出入口、軸線、地標、材質、光向、room tone,以及**天候/時刻變體版本**。三日天候弧(範例):Day1 晴→黃昏;Day2 陰→暴雨;Day3 雨後泥濘→放晴。每個「場景 × 日 × 天候」組合是一個 location state 版本(如 `LOC-002-d2-rainstorm-v01`)。

### 3.4 其他
攝影文法(公路片鏡頭語彙、車內固定機位群,見 §5)、風格/材質契約、**三日色彩弧的 color script**、VFX 文法(雨、煙、科幻元素)、sound bible(含引擎狀態機)、字幕樣式。需要精確文字的圖形(車牌、路牌、螢幕 UI)以乾淨美術檔留給後期合成,不靠生成拼字。

## 4. 層級分解:Film → Sequence → Scene → Beat → Shot

### 4.1 Sequence 骨架(75 分鐘時長預算;待與實際劇本對齊)

| SQ | 日 | 主場景 | 車狀態 | 分鐘預算 |
|---|---|---|---|---|
| SQ-010 開場/出發 | Day1 | LOC-001 | S0 | ~8 |
| SQ-020 公路第一程 | Day1 | 公路/車內 | S0→S1 | ~10 |
| SQ-030 第一站衝突 | Day1 黃昏 | LOC-002 | S1 | ~10 |
| SQ-040 陰天低潮 | Day2 | 公路/車內 | S1 | ~9 |
| SQ-050 暴雨事件(中點) | Day2 | LOC-003 | S1→S2 | ~12 |
| SQ-060 夜談/修車 | Day2 夜 | LOC-003 | S2→S3 | ~8 |
| SQ-070 最後一程 | Day3 | 公路/車內 | S3 | ~9 |
| SQ-080 終局 | Day3 | LOC-004 | S3→S4 | ~9 |

每個 sequence 有 sequence card(宏觀目標、轉折、資訊/情緒/節奏曲線、時長預算)。

### 4.2 Scene / Beat / Shot
- 每場戲一張 scene card + **continuity state**(見 §6.2 範例)+ 平面圖 + coverage 計畫;出場 gate:地理/實體/狀態可解。
- 每個 beat 是一個可見行為/反應/資訊單位,有起訖狀態;維持 **completed / current / reserved beat 防火牆**——已核准偏差若提前完成了未來 beat,就把該 beat 從下游移除並重算 delta;被否決的偏差不推進任何進度。
- 每顆 shot:**一個主要 delta**、可獨立生成/審查/剪輯。
- **數量估算(規劃用,非承諾)**:75 分鐘 ≈ 4,500 秒;若剪入平均每顆 5–8 秒,約需 560–900 顆核准鏡頭,含備援與淘汰,總生成量會更高。實際值以 ledger 回填。

## 5. Coverage 與拆分規則

- 每場戲:master/establishing(空間識讀)、單人/雙人/OTS(表演與視線)、insert 與 reaction(道具、手、資訊、時間壓縮、剪輯保險)、出場/轉場 handle。
- **車內對話是本片主體**,建議固定機位群使每場車內戲可互剪:儀表板正拍雙人、駕駛單人、副駕單人、後座前望、車外側拍行駛 plate、窗外地景 plate(供後期合成窗景)。
- **高風險必拆**:換輪胎/修引擎(手部+接觸)、雨中推車(物理)、精確文字(路牌/儀表讀數 → 後期合成)、長對話(拆短顆+反應鏡)、車損發生的瞬間(碰撞物理 → 拆為「事前/撞擊 insert 或聲音暗示/事後結果」三段,撞擊本身優先走剪輯省略或 VFX 路線)。
- 一顆鏡頭若含多個獨立「and then」事件,先拆 beat 再決定是否拆 shot。

## 6. 資產登錄、三個連續性儲存與狀態模型

### 6.1 三個儲存(外部製作設計,非模型內建)
1. **Canonical bank**:人工核准的身份/場景/道具/聲音/風格/狀態真值。生成結果永遠不能自動取代它。
2. **Approved memory**:僅從「已核准」鏡頭晉升的少量高資訊幀/片段;晉升前過四關(身份正確、無失格瑕疵、符合 prompt/劇情、跨鏡相容),並記錄來源 shot/timecode/裁切/使用邊界。
3. **Local handoff**:相鄰鏡頭的暫態(最後核准幀/動作尾、位置、銀幕方向、鏡頭速度、光色、道具持有者、room tone),只服務相鄰連戲,永不覆寫 canonical。

`return_last_frame` 之類功能(若你的平台有文件支持)只是傳輸;最後一幀必須通過 QC 才能晉升。

### 6.2 Continuity state(每場一份,版本化)

```yaml
scene_id: SC-050-021
story_time: "Day 2 / 暴雨午後"
location_state: LOC-003-d2-rainstorm-v01
car_state: CAR-S2-v01          # 擋風玻璃裂、車頭凹
screen_axis: 車頭朝銀幕右
characters:
  CHAR-001: {wardrobe: WARD-A-d2-wet-v02, position: 駕駛座, gaze: CHAR-002}
  CHAR-002: {wardrobe: WARD-B-d2-wet-v01, injury: INJ-B-手掌擦傷-v01,
             held_props: [PROP-005-地圖-濕]}
lighting: LIGHT-SC050-雨天車內-v01
audio: SOUND-SC050-雨+S2引擎異音-v01
```

每顆 shot 讀上一個核准狀態,只提交自己的核准 delta;續接來源已帶狀態,prompt 只描述 delta,不重播整份契約。

### 6.3 登錄與 ledger 欄位
- Asset registry:`asset_id, entity_id, state, version, owner, rights_status, source_paths, allowed/excluded_attributes, status, approval, sha256`。
- Run ledger:`run_id, parent_run, shot_id, timestamp, 平台/模型/文件版本, prompt 文字/hash, 參數, 參考 ID/hash/角色, 這次唯一改變的變數, 輸出路徑/hash/時長/規格, 排隊/生成/審查/人工時間, 實際費用, hard gates, 評分, 帶時碼缺陷, 審查者, 決定, 路由`。
- 不留存憑證、cookie、簽名網址;供應商連結會過期,授權輸出要即時入庫並 hash。

## 7. Shot Manifest 與 Shot Contract

Manifest 是全片鏡頭總表(CSV/表格),每列一顆 shot,欄位對應 contract 摘要 + 狀態(`planned/ready/generating/review/approved/rejected/in-cut`)+ 依賴指標。Contract 範例(車損升級的 A 級鏡頭):

```text
Identity : SH-050-021-030 / A 級 / 高風險 / owner: 你
Narrative: 撞擊後首次看清車況;start: CAR-S1 完好車頭(前場最後核准狀態)
           delta: 揭示車頭凹陷與裂紋(S2 首次可見);end: 兩人站在車頭前,雨中
Entities : required [CHAR-001@WARD-A-d2-wet, CHAR-002@WARD-B-d2-wet, CAR-S2-v01,
           LOC-003-d2-rainstorm] / forbidden [CAR-S0, CAR-S1, 任何乾燥服裝]
Space    : 車頭朝右;兩人由畫左入;視線先車後互看
Camera   : 中景緩推;handle 前後各 1s;下一顆接 CHAR-001 單人反應
Look     : 暴雨、冷灰藍(color script Day2)、雨在凹陷處積流
Sound    : 無對白;雨 + S2 引擎熄火 tick 聲(後期為準)
Inputs   : CAR-S2 參考組 hash、兩人濕裝參考 hash、LOC-003 雨天參考 hash
Accept   : 硬門檻(§10)+ 凹陷位置/形狀與 CAR-S2 參考一致 + 鄰接可剪
Route    : 凹陷形狀漂移 → 換更近角度參考重試;仍失敗 → 生成乾淨車 + 後期合成損傷
```

## 8. 依賴佇列

**可平行**:公路空景/地景 plate、insert、反應鏡、不同場景間無 handoff 依賴且 canonical 已鎖的戲、審查/聲音 spotting/字幕準備(不互改同一真值)。

**必序列化(本片特別重要)**:
1. **車損軸**:全片含車鏡頭按 CAR-S0→S4 分層;同層內可平行,**跨層晉升(S1→S2 的那顆核准)是序列化關卡**,未核准前不得生成下一層任何含車鏡頭。
2. **日/天候/服裝軸**:同理,Day2 濕裝定調鏡核准前,不批量生成 Day2 濕裝戲。
3. Extension 鏈與連續動作、依賴前一核准末幀的下一顆、canonical/approved-memory 晉升、場面地理未核准前的主角特寫。

**批次規則**:只把相同平台/模型/任務/比例/解析度/參考包版本/評分標準的鏡頭放同一批,否則失敗無法歸因。

## 9. 版本、命名與 Selection Lineage

```text
FILM-ROAD / SQ-050 / SC-050-021 / BT-050-021-03 / SH-050-021-030
CHAR-001 / LOC-003 / PROP-CAR-001
FILM-ROAD_SH-050-021-030_take-002_run-r041_prompt-p003_ref-r009_<model-id>_720p_v001.mov
FILM-ROAD_PROP-CAR-001_S2_v001_APPROVED.png
FILM-ROAD_SC-050-021_continuity-state_v003.yaml
```

- ID 永不重用(剪輯順序會變);狀態以 metadata 為準,檔名的 `APPROVED` 只是可讀輔助。
- **Lineage 鏈**:run → take → select → in-cut,每一步記 parent、審查者、決定;每次重試只改一個變數;被否決的輸出只作診斷,永不成為 canonical、approved memory 或 handoff 來源。

## 10. 審查 Gate、重試上限與失敗路由

**十道端到端 gate**:development → script/bible → breakdown/risk → previz/anchor → blocking 生成(端到端粗剪存在)→ 正式生成(輸出進 incoming,絕不覆寫已核准)→ dailies/selects(先保真後一致,看完整片段不看縮圖)→ 結構鎖/pickups → VFX/conform/color/sound/字幕 → 終審 QC/母帶/歸檔。

**硬門檻(先於評分)**:權利/安全/交付、必要劇情 beat、身份/實體/狀態正確、方向與道具持有無歧義、無不可剪的結構性瑕疵、可用區間完整且鄰接相容、聲音/文字通過或有核准的後期路由。

**重試上限**:按 A/B/C 風險層設定,**具體數值取決於你的預算與時程天花板,目前未知,請在 charter 補上**;規則是每次只改一個變數,同一阻斷性缺陷重複出現、關鍵約束震盪、或觸頂時即停止並改路由。

**路由選項**:更乾淨/狀態專屬的資產、簡化動作、鎖定機位、拆短/分割、改用 insert/反應/cutaway、局部修補、傳統 VFX 合成(車損、精確文字首選)、2D/3D/實拍、ADR/配音、圖形疊加、劇情重設計。

## 11. Checkpoint 與 Rollback

不可變 checkpoint 節點:bible 鎖、previz/anchor 鎖、**每個 CAR 狀態層核准後**、每 sequence 核准後、結構(picture)鎖、聲音/調色鎖、最終母帶。每個 checkpoint 存:劇本/bible 版本、狀態快照、核准 hash、timeline/EDL、未結缺陷與路由、預算實耗、工具/模型/平台/文件版本與簽核。

Rollback 規則:從父核准 run 重試,永不從被否決的子輸出;狀態/軸線/服裝被污染時回到場景起點 checkpoint、只重放已核准 delta;結構鎖後的任何變更需附下游 VFX/聲音/字幕/調色影響清單;模型/平台更新一律開新分支跑回歸,不覆寫已核准渲染。

## 12. Rough Cut 與 Pickups

- **儘早建立端到端 animatic/blocking cut**(C 級快速輸出 + 佔位),用它暴露:coverage 洞、重複/拖沓 beat、缺 master/反應/insert/出場 handle、軸線與視線錯位、以及「重生成不如剪輯/VFX 便宜」的位置。
- 粗剪以故事與表演為準,不為沉沒的生成成本留鏡頭;記錄核准 in/out 與 handle、temp VFX/重取景/變速意圖、音訊佔位、缺口與 pickups 優先序、每次結構變更的下游影響。
- 不得用未記錄的變速掩蓋對白節奏或連戲損傷;結構鎖後新增鏡頭或改狀態順序需走 change request。
- Rolling assembly(邊生成邊組裝)是強實務起始政策,**沒有對照研究證明理想重疊度**。

## 13. Finishing:VFX / Color / Sound / ADR / Music / 字幕 / Mastering

- **VFX/cleanup 路由原則**:契約錯但題材適合模型 → 重生成;缺陷有界 → 局部 AI 修補或傳統 paint/roto/key;可剪輯救 → 重取景/cutaway/拆分;**精確文字/車牌/UI → 一律合成**;持續性物理/接觸失敗 → 模擬/3D/實拍。本片專屬:車損細節漂移優先用合成貼修而非重生成;車窗外景可用地景 plate 合成統一。Conform 時統一編碼/幀率/色彩標籤/聲道/檔名進母帶專案,保留來源與變換紀錄。
- **Color**:依三日色彩弧檢查鏡間匹配、光的動機、膚色/材質、日/天候狀態、漸層/banding、legal range,校準環境下看;容器或「4K」徽章不代表生成解析度或色彩管線。
- **Sound**:精確對白、說話者/聲音身份、發音、對嘴、空間感、跨剪 room tone、動作連動 foley、**引擎聲隨 CAR-Sx 的狀態機**、音樂動機、靜默、響度與聲道。生成音只當時間參考,不取代專業清理與混音。畫面可用而模型語音不可用時走 ADR/配音,聲音權利與發音字典在 passport 裡。
- **字幕**:**時間軸以最終成片音軌為準,絕不用 prompt 時間戳**;查語言、說話者、轉寫、斷行、閱讀速度、安全區、遮擋、跨剪行為、burn-in vs sidecar。
- **Mastering**:依 charter 的交付規格(目前未知)產母帶 + mezzanine + stems。

## 14. 終審 QC 與歸檔

至少一次完整不間斷母帶播放 + 針對每個剪點/VFX/字幕/音訊轉場的定點檢查。技術 QC:時長/畫幅/解析度/幀率/編碼/色彩標籤、重複/掉/凍結/黑幀、壓縮瑕疵、聲道/同步/削波/響度、字幕格式、交付命名與 checksum。內容 QC:劇情與必要 beat、身份/服裝/傷/道具/**車損不回退**/場景/天候連戲、解剖/運動/物理、對白/聲音/音樂/字幕、權利/政策/揭露/浮水印。歸檔:母帶、stems、字幕檔、專案/時間軸檔、prompt/參考/狀態/run ledger、核准與否決紀錄、工具/模型版本、hash、簽核、waiver、rollback checkpoint;不歸檔簽名網址與憑證。

## 15. KPI 儀表板(只用實際 ledger,不用行銷計數或發明的估計)

品質軸:beat 符合度、角色/服裝/傷/場景/道具(**含車損狀態**)/聲音/風格連戲、時間穩定與瑕疵率、運動/接觸/因果、攝影/構圖/光/材質、對白/對嘴/環境音/音樂/字幕正確性、剪輯可用性與鄰接相容。

效率軸(全部從 run ledger 計算,報中位數、分布與 P90):

```text
first_pass_approval   = 首次有效 run 即核准 / 有效首 run
additional_retries    = 核准前額外有效 run / 已核准鏡頭
time_per_approved_shot / usable_seconds_per_hour
cost_per_approved_second / human_correction_time
queue_wait_ratio / waste_rate(未進片的生成秒數與費用占比)
```

建議另按 **A/B/C 級與 CAR 狀態層分組**看 KPI,用前兩個 sequence 的實測值校準分級與重試上限。Pareto 原則:先過所有品質地板;一個流程只有在所有必要維度不更差且至少一維更好時才「支配」另一個;「又快又好」沒有對照證據前不成立。

## 16. 待你決定的事項(會改變計畫的未知)

1. **平台/模型 gate**:用哪個面(Seedance 2.0/2.5、ModelArk、其他)、地區、當前文件日期——決定單段時長、參考輸入方式、批次與成本結構。
2. **預算與時程天花板** → 決定各級重試上限與候選數(§10)。
3. **交付規格**:畫幅、幀率、母帶編碼、響度標準、字幕交付形式。
4. **劇本現況**:已有完整劇本或需先開發?§4 的 sequence 骨架是佔位,需與實際劇本對齊(如需劇本開發可另用 screenplay-writer skill)。
5. **權利**:兩位主角的臉/聲音來源、音樂、任何參考素材。

補齊這五項後,系統即可從 gate 1(charter 鎖定)啟動;付費生成另需你的明確授權。
