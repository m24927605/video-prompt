# Higgsfield Studio 九案研究（最終證據版；長片 terminal 與中段已補證）

> 狀態：`final-capture-complete-with-explicit-unknowns`。本研究員只記錄 2026-08-22 以可見 Chrome、使用者既有登入狀態取得的證據。9 支 published cuts 均有 start/middle-or-high-risk/terminal 證據；5 支直接打開的 generation outputs 均完成首中近尾檢查。P02 的直接 `Seedance 2.5` 樣本另以網站正常 Download 保存並完成 stream/decode/waveform/嘴部動作稽核。粵語文字正確性、聲音自然度與 phoneme 級 lip-sync 仍明列 `unknown`，不冒充通過。Aggregated assets 未逐一打開。
>
> 證據標籤：`直接 UI／影片觀察`＝頁面欄位、實際展開狀態、播放器與 timecoded frames；`直接文本觀察`＝prompt/brief 原文確實可見，但不驗證其中成效敘述；`專案作者自述`＝brief 對流程、製作史、成本、效率或效果的說法，除非另有 UI／影片證據，均未獨立驗證。

## 1. 範圍與索引 gate

- `直接 UI／影片觀察`：來源頁是 <https://higgsfield.ai/@higgsfield.studio/projects>，頁面標題為 `Projects by @higgsfield.studio on Higgsfield`。
- `直接 UI／影片觀察`：`Projects` tab 為 selected；完整捲動頁面後仍為 9 個不同 project links，沒有可見 pagination、load-more 或 filter；只看到 Search。
- `直接 UI／影片觀察`：九案順序固定為 P01 `kok-boru-film`、P02 `red-flag`、P03 `adiliada`、P04 `zephyr-special`、P05 `oneiric`、P06 `cully-hill-boys`、P07 `zephyr`、P08 `hell-grind`、P09 `kok-boru`。
- `重要口徑`：下表的 **All assets** 是 project UI 顯示的 aggregated project metric，不是本研究已逐一列舉／檢查的媒體數。`Generations`、`Views` 是另一組分離欄位；不能互換。
- 索引證據：index-full [archive: `browser-evidence/higgsfield/index-full-2026-08-22.png`]、index-top [archive: `browser-evidence/higgsfield/index-top-2026-08-22.png`]、index-bottom [archive: `browser-evidence/higgsfield/index-bottom-2026-08-22.png`]；結構化索引：projects-index.json [archive: `higgsfield/projects-index.json`]。

| ID | 顯示名稱 | 公開路徑 | 主片 | 解碼畫面尺寸 | All assets（聚合） | Generations | 建立時間（最終可見文字） |
|---|---|---|---:|---:|---:|---:|---|
| P01 | Kok Boru | `kok-boru-film` | 14:59 | 4096×1716 | 14,021 | 12,052 | Aug 17, 21:09 |
| P02 | Red Flag | `red-flag` | 2:16 | 1920×1080 | 3,525 | 3,524 | Aug 19, 17:21；早期 SSR 快照曾顯示 09:21，需視為時區 hydration 差異 |
| P03 | Adiliada | `adiliada` | 6:16 | 1920×1080 | 11,299 | 11,023 | Aug 14, 21:01 |
| P04 | ZEPHYR: Special | `zephyr-special` | 5:07 | 1678×720 | 4,838 | 4,837 | Aug 11, 20:00；早期 SSR 快照曾顯示 12:00 |
| P05 | ONEIRIC | `oneiric` | 19:48 | 3438×1440 | 41,118 | 41,096 | Aug 12, 20:36 |
| P06 | Cully Hill Boys | `cully-hill-boys` | 1:54:48 | 3438×1440 | 473,600 | 473,214 | Aug 11, 00:01 |
| P07 | ZEPHYR | `zephyr` | 10:48 | 1920×1080 fresh replay；早期 854×480 stream | 19,002 | 18,682 | Aug 6, 00:52 |
| P08 | HELL GRIND | `hell-grind` | 1:35:59 | 4096×1716 | 115,451 | 115,446 | Aug 4, 18:17 |
| P09 | Kok Boru | `kok-boru` | 1:20 | 5156×2160 | 2,781 | 2,693 | Jul 11, 12:10 |

### Model version gate（project claim 與 asset label 分層）

| Project | Project/brief claim | Opened asset / frame label | 可用結論 |
|---|---|---|---|
| P01 | generic `Seedance` | sampled asset UI=`Seedance 2` | workflow 與該 asset 的 Seedance 2 observation；不可歸 2.5 |
| P02 | every video shot=`Seedance 2.5` | sampled generation Model=`Seedance 2.5` | 可作 project-specific 2.5 evidence；仍不是成功保證 |
| P03 | generic `Seedance` | 未開 generation label | version unknown |
| P04 | brief=`Seedance 2.5` | sampled workspace asset=`Seedance 2` | brief-level 2.5 workflow claim；sampled asset不能當2.5 performance evidence，project 可混版本／iterations |
| P05 | generic `Seedance` | 未開 generation label | version unknown |
| P06 | generic `Seedance` | 未開 generation label | version unknown；9/3/3 等只能作 Higgsfield practice |
| P07 | brief=`Seedance 2.0` | sampled Production asset=`Seedance 2` | 2.0/project workflow，非2.5 |
| P08 | brief=`Seedance 2.0` | 未開 generation label | 2.0/project workflow，非2.5 |
| P09 | generic `Seedance` | published frames 燒錄 `SEEDANCE2.0 4K` | project-visible 2.0 label，非 backend ID、非2.5 |

## 2. P01 — Kok Boru 完整短片

來源對：[原始 project](https://higgsfield.ai/@higgsfield.studio/projects/kok-boru-film) · 本機 main text [archive: `browser-evidence/higgsfield/p01-kok-boru-film-main-text-2026-08-22.txt`] · case JSON [archive: `higgsfield/projects/P01.json`] · 片尾證據 [archive: `browser-evidence/higgsfield/p01-v01-end-replay-2026-08-22.png`]

### 可見結構與工作流

- `直接 UI／影片觀察`：主片實測 899.041667 秒；頁面可見的 brief 稱它為 15 世紀中亞背景的第一支動畫短片。
- `專案作者自述`：brief 說明混合 human art 與 generative AI。character designs、props、painted textures 先以 AI 生成，再由藝術家以 Photoshop／Higgsfield Plug-In 手工編修；AI 再負責生成、in-betweening、環境、群眾與動物動作，以及光線／氣氛迭代。
- `專案作者自述`：影片 prompt 由 system prompts 經 Higgsfield Claude MCP 處理，並連同 15-page script 提供情節上下文；每鏡固定重複 `Style Prefix` 與 `Constraints`。
- `專案作者自述`：production 以 Acts → Scenes → Shot 組織，每個 shot folder 保存多次 iteration；post 包含人工 color grade、配樂／原創音樂、手工 sound cleanup/SFX 與 native Kazakh voice rerecording。
- `直接 UI／影片觀察`：workspace 頂端清楚顯示 `Read-only`。All assets 聚合 14,021；ACT 1=5,761、ACT 2=5,083、ACT 3=3,064。
- `直接 UI／影片觀察`：展開 ACT 1 顯示 SC01=1,374、SC02=614、SC03=1,067、SC04=504、SC05=414、SC06=246、SC07=138、SC08=753、SC09=93；ACT 2 顯示 SC10（數字在該狀態不可見）、SC11=1,930、SC12=1,910、SC13=386；ACT 3 顯示 SC14=2,115、SC15=925。

### Prompt／參考／設定證據

- `直接文本觀察`：brief 的完整 Style Prefix 與 Visual Constraints 已保存在 `research/seedance-2.5/browser-evidence/higgsfield/p01-kok-boru-film-main-text-2026-08-22.txt`。核心包括 hand-painted 2D moving oil painting、true 12fps／animated on twos、painterly boil、禁止 smooth interpolation／motion blur／morphing／liquid surfaces，並明確把 Image 1–6 分配為 style、角色與 yurt 內外景參考。
- `直接文本觀察／專案作者自述`：音訊約束原文寫 `No music. Only SFX.`；brief 另稱音樂在 post-production 建立。介面未顯示獨立 negative-prompt 欄位，不能把 prompt 中的 `NO ...` 誤記為 separate negative prompt。
- `直接 UI／影片觀察`：在 ACT 1 → SC01 實際打開第一個可見影片 generation。Accessibility tree 顯示 7 個 reference slots；prompt 明確使用 5 個命名 reference（`@Image 1/4/5/6/7`），目前 viewport 同時可見 4 張縮圖。介面另顯示作者、完整超長 prompt、Feature=`Seedance 2`、Quality=`4k`、Bitrate=`High`、Size=`4032x1728`、Created=`July 2, 2026 at 7:12 PM`；影片實測 15.041667 秒、解碼 4398×1886。
- `直接 UI／影片觀察`：該 prompt 使用三個 hard-cut shots，明確指定 child-height POV、~32mm、wolves 的單向環形流動、smear-frame／solid-pose 交替、fog/snow、光線、聲音、動力學、禁止攻擊，以及每鏡 ending state。完整原文（不是摘要）在 `research/seedance-2.5/browser-evidence/higgsfield/p01-sc01-asset01-text-2026-08-22.txt`。
- generation 檢視證據：00:00 [archive: `browser-evidence/higgsfield/p01-generation01-start-computer-use-2026-08-22.png`]、00:05 [archive: `browser-evidence/higgsfield/p01-generation01-mid-t0005-computer-use-2026-08-22.png`]、00:13 [archive: `browser-evidence/higgsfield/p01-generation01-near-end-t0013-computer-use-2026-08-22.png`]；完整 loop 亦在 viewer 保持開啟時觀察。三個時間點持續可見固定 stone idols、深色 wolf silhouettes、blizzard／fog，00:13 有清楚 stretched smear；`直接 UI／影片觀察` 支持該樣本的視覺風格、主體與氣氛 adherence。三張靜態幀仍不足以獨立證明 true-12fps cadence、每個動作的物理連續性或音訊品質。

### 主片播放狀態

- `直接 UI／影片觀察`：fresh replay 無 pause/seek/reload 播至 14:59/14:59。00:27 與 04:20/12:02 的 ANA 臉、髮、紅衣持續可辨；01:30 wolves/balbal、05:22 wolf-child、08:56 large wolf、13:35 child-wolf contact 都維持 hand-painted solid-surface 語言；02:38 valley、10:25 camp 的 day/night state 仍在同一 palette family；06:57/07:49 多人與 wolves 的 battle/crowd 敘事可讀。抽查幀未見明顯 morph/liquid-surface、extra limb 或亂文字，但 12fps cadence、完整動作物理與 audio/lip-sync 仍不能由靜態證據單獨通過。

## 3. P02 — Red Flag

來源對：[原始 project](https://higgsfield.ai/@higgsfield.studio/projects/red-flag) · 本機 main text [archive: `browser-evidence/higgsfield/p02-red-flag-main-text-2026-08-22.txt`] · case JSON [archive: `higgsfield/projects/P02.json`] · 2.5 generation 證據 [archive: `browser-evidence/higgsfield/p02-generation01-viewer-2026-08-22.png`]

### 可見結構與工作流

- `專案作者自述`：brief 稱本片為 ~2-minute photoreal Hong Kong neo-noir，1.85:1、Cantonese、minimal dialogue，且 every frame generated、無 set/camera/filmed footage。
- `專案作者自述`：brief 稱 Seedance 2.5 用於 every video shot、Higgsfield Soul Cinema 用於 character sheets、Seedream 5.0 用於 image edits；下方 sampled generation 的 Model=`Seedance 2.5` 是獨立的直接 UI 證據。
- `直接 UI／影片觀察`：All assets=3,525，folders：`1 scene`=386、`2 scene`=283、`3 scene`=252、`assets`=214、`test`=59。
- `專案作者自述`：約 30 個 tagged assets；每個 asset 是 text descriptor + image，descriptor 逐字放進每個 prompt，引用一律用 `@tag`。
- `直接文本觀察`：brief 展示固定 style prefix：Arriflex 35 III、Zeiss Super Speed、1.85:1、Fuji Eterna 500T、cool processing、coarse grain、halation、shallow focus。
- `專案作者自述`：brief 指出 `no yellow` negative lists 沒有效，改用正向比例：cold teal-green 為 dominant，yellow 僅限 bulb 與 palm-sized halo；也直接覆寫 reference 中不該存在的 lit window。
- `專案作者自述`：diagram 專司 composition/camera，location photo 只供 surfaces/light；diagram last，並明寫 `Composition and camera = the diagram`。如果 reference 仍奪走構圖，做法是移除該 reference。
- `專案作者自述`：門鉸方向、開門方向、彩繪所在門面、欄杆公分尺度、手的數量都重複寫入；open-window continuity 以獨立 state asset 解決。walking 以 heel-first、left-right alternation、one foot grounded；兩人同框以 same depth line／same head size；matching shots 直接鎖定 camera speed。
- `專案作者自述`：三招 takedown 採 last-frame→next-first-frame chaining；money move 則單一 continuous take、逐秒 timeline、real-time speed、明確禁止 slow motion。blocking diagrams 用於手腳 keyframes，並用 hands/waist/feet inserts 降低 full-body continuity 風險。
- `直接 UI／影片觀察`：實際打開一支 workspace generation，介面明示 Model=`Seedance 2.5`、1080p/High、1920×1080、29.056 秒、Created 2026-08-19 20:56。Prompt 是中文、25 秒 timeline（Shot 0/9–14），含 WKW/HK-noir style、green/yellow color budget、location geometry、左右站位、兩人／bags、Cantonese dialogue、acting tasks 與 audio；完整原文在 `research/seedance-2.5/browser-evidence/higgsfield/p02-generation01-text-2026-08-22.txt`。
- `直接檔案／AV 稽核`：以該 viewer 的正常 Download 保存 P02-A01-V01.mp4 [archive: `higgsfield/media/P02-A01-V01.mp4`]（30,389,049 bytes；SHA-256 `d522df307b4671c724593d3fb70a089c130ec1618a831c5ed5b6f165d2bad5d5`）。HEVC 1920×1080/24fps 與 AAC-LC stereo 32kHz/29.056s 全檔 decode 通過；waveform 的 speech-like bursts 與 4fps mouth contacts 支持粗粒度 speech-window／嘴部動作對齊。粵語台詞正確性、音色自然度與 phoneme 級 lip-sync 仍為 `unknown`；完整方法與邊界見 audio/lip-sync audit [archive: `worknotes/p02-generation-audio-lipsync-audit.md`]。
- `直接 UI／影片觀察`：prompt 有 8 個 named asset tags，其中同時出現 `@char_granny_ver1` 與 `@char_granny_ver1.1`，且部分 tag 重複；介面沒有獨立 lineage。Prompt 要 25 秒、實際 29.056 秒；00:28 才到本應 23–25 秒的 lamp shot，存在 timing stretch。00:00 woman-right/granny-left、bag/count/color 成立，但 tiger-painted door 已緊貼人物後方，與「停在前一扇 iron-grille neighbor door、尚未到 tiger door」的 geometry intent 有衝突；00:14/00:18 bag handoff、granny close-up 與 green grade 可讀；00:28 globe lamp 僅自身 warm halo、其餘暗綠黑，color lock 成立。
- `直接 UI／影片觀察`：All assets 在執行初始 public capture 為 3,525，約一小時後 workspace surface 顯示 3,575。這可由 live update、cache/hydration 或 surface counting semantics 造成，原因 `unknown`；初始 scope value 保留、不覆寫成後值。

### 主片時間碼觀察（完整播放已驗證）

- 00:00：Hong Kong skyline，cold teal-green／yellow practical lights 已建立；顆粒、halation、夜景與 1990s noir intent 一致。
- 01:08：室內從背後拍男子；green walls、局部 warm window/light、人物 silhouette 與淺景深一致，未見明顯幾何跳變。
- 01:45：女主 close-up；臉部細節、skin texture、bokeh 與色調穩定，未見明顯 extra anatomy 或文字 artifact。
- 01:58：男子在同一公寓／窗景前拿 bouquet；空間色彩與 prop continuity 可辨。
- 02:08：bouquet 落地、人物下肢進出畫面；單張未見 bouquet/legs 明顯破形。高風險 fight 的逐動作物理仍需影片人工複核，截圖不能替代運動判讀。
- 02:16：播放列到達 2:16/2:16，顯示片尾黑畫面／Higgsfield mark，完整播放 gate 通過。
- 證據：`p02-v01-start-2026-08-22.png`、`p02-v01-t0068-2026-08-22.png`、`p02-v01-t0105-2026-08-22.png`、`p02-v01-t0118-2026-08-22.png`、`p02-v01-t0129-2026-08-22.png`、`p02-v01-end-2026-08-22.png`。

## 4. P03 — Adiliada

來源對：[原始 project](https://higgsfield.ai/@higgsfield.studio/projects/adiliada) · 本機 main text [archive: `browser-evidence/higgsfield/p03-adiliada-main-text-2026-08-22.txt`] · case JSON [archive: `higgsfield/projects/P03.json`] · 片尾證據 [archive: `browser-evidence/higgsfield/p03-v01-end-2026-08-22.png`]

- `專案作者自述`：brief 稱它為 6:16 photoreal AI short、series-opening 結構；cold open → title sequence → post-title episode continuation，且 every frame generated。
- `直接 UI／影片觀察`：All assets=11,299；四個 root groups 為 `1. COLD OPEN: The Crow Hunt`=1,451、`2. MAIN TITLE SEQUENCE`=4,637、`3. SPACE SCENES`=2,296、`4. MEETING THE VILIAN`=2,363。
- `專案作者自述`：Seedance 用於 every shot/all video/all generations；Claude skills 包含 acting system 與 CINEDANCE；Diagram Skill 固定多人 staging；depth map 固定 3D space、composition、volume、proportion。
- `專案作者自述`：同一角色跨 universes 使用不變 base face pixels，只改 wardrobe/makeup/hair/scars；close-up anchor 不再整張進模型。locations 先建立 visual anchors，再統一 color/light/saturation。
- `直接文本觀察／專案作者自述`：brief 展示 CINEDANCE 每鏡 schema：SCENE CONTEXT → ACTIVE REFERENCES → LOCATION MAP → GAZE/EYELINES → FIRST FRAME/BLOCKING → timed SEGMENTS → DIALOGUE → AUDIO → PHYSICS → LIGHTING → STYLE/FORMAT → POSITIVE LOCKS，並稱 `same as previous shot` 無效。
- `專案作者自述`：post 流程為 assembly、rough cut、generation supervision、fine cut、picture lock；picture lock 後只允許 emergency fixes，再進 cleanup/color/sound。
- `直接 UI／影片觀察`：主片完整播放到 06:16/06:16。00:58 與 03:46 都看見同一 bald alternate character、red clothing 與相同 retro control-room set，支持跨段 identity/wardrobe/location continuity；03:08 是明確黑場轉場；05:01 進入更暗的 action/ship interior，prop 與人物下肢在單幀未見明顯破形。這些仍是 timecoded visual checks，不足以獨立驗證整段 audio/lip-sync。

## 5. P04 — ZEPHYR: Special

來源對：[原始 project](https://higgsfield.ai/@higgsfield.studio/projects/zephyr-special) · 本機 main text [archive: `browser-evidence/higgsfield/p04-zephyr-special-main-text-2026-08-22.txt`] · case JSON [archive: `higgsfield/projects/P04.json`] · 片尾證據 [archive: `browser-evidence/higgsfield/p04-v01-end-2026-08-22.png`]

- `直接 UI／影片觀察`：主片 5:07、decoded 1678×720；頁面 brief 可見機甲 squad 成員遇險、guest character 介入的描述。
- `直接 UI／影片觀察`：All assets=4,838、Generations=4,837；root folder `regenerations`=90。
- `直接文本觀察`：brief 明確寫 `Seedance 2.5` 與 Higgsfield Cinema Studio scene control；這是 project-level version/workflow claim，不是每個 asset 的 backend label。
- `專案作者自述`：三個 impossible-shot 方法：把 Naomi character sheet 倒置、直接在 input 烘入 upside-down physics；用 layout images 當 spatial/directional positional guide（不是 direct shot input）；救援鏡只指定 key anchors、讓模型增加 camera angle/motion variation，再從多 take 剪出最 cinematic cuts。
- `專案作者自述`：brief 稱 attached project 同時保留 bloopers/failed takes 與 final cuts，且 prompts open-sourced；本研究直接確認了兩個不同 workspace 入口與部分 outputs，但未逐一驗證全部 prompts/files。
- `直接 UI／影片觀察`：頁面提供 `Open project` 至 `projectId=b39dd57b-adda-4d1a-98a6-cec042eef77b`，並有 `Download assets`；本研究沒有下載、重跑或 remix。
- `直接 UI／影片觀察`：`View full project` 與 `Open project` 是不同入口。前者展開真正的 `ZEPHYR Special FINAL`（4,838 assets、regenerations=90）；後者進入原始 `ZEPHYR` Episode 1 remix workspace（19,002 assets；Characters=54、Iterations=18,673）。兩者的 metrics 與 generations 不可合併。
- `直接 UI／影片觀察`：在 Special workspace 實際打開一支 14.041667 秒 generation。Prompt 綁 6 images（五位角色＋花田）與 1 song audio，要求三個 hard cuts、五人同步 K-pop choreography、24fps aesthetic、wind/cloud/flowers、lip-sync。介面顯示 Feature=`Seedance 2`、4k/High、Size=4032×1728、Created 2026-06-29；因此即使 P04 brief 明示整案使用 2.5，這支 sampled asset **不能**被當成 2.5 output-quality evidence，並顯示專案資產可能跨版本／含 earlier iterations。
- `直接 UI／影片觀察`：sampled generation 的 00:00 低飛越花田符合起始 camera intent；00:07 五人服裝／角色均可辨、medium orbit/push 符合第二鏡；00:14 只見三人近景，未達 prompt 要求的五人 wide final group pose，屬 final-framing／subject-count adherence failure。完整 prompt 與時碼證據在 `research/seedance-2.5/browser-evidence/higgsfield/p04-generation01-text-2026-08-22.txt` 及相鄰 screenshots。
- `直接 UI／影片觀察`：P04 final 重新完整播放至 05:07/05:07。00:00/00:21 倒置 cockpit framing 能持續讀成 shift-gravity state；02:52 mech 與大型敵體／牆面接觸時，單幀可讀出 scale、mass 與接觸方向，未見明顯額外肢體／HUD 文字；片尾正常到達黑場。單幀不足以證明整段 mech physics 或 audio sync，仍以保守措辭處理。
- `未知／待驗證`：sampled generation 的 seed、actual fps、camera/motion UI parameters、variant lineage 不可見。

## 6. P05 — ONEIRIC

來源對：[原始 project](https://higgsfield.ai/@higgsfield.studio/projects/oneiric) · 本機 main text [archive: `browser-evidence/higgsfield/p05-oneiric-main-text-2026-08-22.txt`] · case JSON [archive: `higgsfield/projects/P05.json`] · replay 起點 [archive: `browser-evidence/higgsfield/p05-v01-replay-start-2026-08-22.png`] · resume 後片尾 [archive: `browser-evidence/higgsfield/p05-v01-end-resumed-2026-08-22.png`]

- `專案作者自述`：brief 稱它為 19:48 photoreal AI short；一個四人 dorm dialogue spine，加 Troy、deep-space、fairy-tale 三個 fantasy worlds，且 every frame generated。
- `直接 UI／影片觀察`：All assets=41,118、Generations=41,096；ASSETS=22,960、regenerations=292、SCENE 1–12 以 location/sequence 分資料夾。
- `專案作者自述`：Seedance 用於 every shot/all video and speech；Claude skills 包含 scene-drama engine、acting system、CINEDANCE；Diagram Skill 固定多人 staging。
- `專案作者自述`：anamorphic optics 不只寫在 video prompt；brief 說其穩定度不足，因此把 lens character 烘入 location assets，讓模型從 reference 讀取。
- `專案作者自述`：Voice Bible 以固定 register/timbre/tempo/manner block 逐字貼入每一 generation；同義詞也不更換。Brief 再次明示每個 prompt 是 island，所有 positions/poses/wardrobe/props/optics/light 必須重述。
- `專案作者自述`：全團隊 tag convention 以 element type/project/name/scene/version 命名；新 state 建新 asset，不覆寫舊版。Soul Cinema 先鎖 close-up face，Soul 2.0 建 full-body looks，再以 Seedream/Nano Banana/ChatGPT + masks 組 sheet，base portrait pixels 不再整張過模型。
- `直接文本觀察`：brief 保留一個 11 秒 real prompt：四角的 ACTIVE REFERENCES、固定 LOCATION MAP／eyelines、0–0.5s silent wide、兩個 hard-cut mediums、逐秒 dialogue、physics、lighting、三個 voice locks、style、positive locks。這是 generic Seedance project prompt，不可升格為 2.5 template。
- `專案作者自述`：Diagram Skill 把 composition 轉成 front-view colored outlines，顏色綁角色；style/light/identity 只來自真正 assets，diagram 只管位置。每次修改都從 original frame 重畫，不把舊 diagram 再餵回去；letters 留在 text connector，不渲染進圖。
- `專案作者自述`：acting system 用 motive/goal/obstacle/tactic 與 eye tasks，避免只寫 emotion adjective；post 是 Assembly→Rough cut→Generation supervision→Fine cut→Picture lock，再 cleanup/color。這支持 iterative 回補，不單獨證明全程 parallel edit。
- `直接 UI／影片觀察`：fresh replay 00:55 Bob common-room、02:41 同角 Troy armor、04:28 Sam common-room、05:19/06:33 space cast、08:45 space action、10:19 alien close-up 均可讀；Bob/Sam 在 world-state 轉換後仍可辨，dorm set/wardrobe 在回切時相容，sampled frames 未見明顯 extra limb/亂文字。
- `直接 UI／影片觀察`：replay 15:32:09 開始且未 pause/seek/reload；直接中段幀保存至 10:19。Codex CLI resume 後，保留播放器明確顯示 `19:48 / 19:48` 與 Play 控制，terminal gate 通過。

## 7. P06 — Cully Hill Boys

來源對：[原始 project](https://higgsfield.ai/@higgsfield.studio/projects/cully-hill-boys) · 本機 main text [archive: `browser-evidence/higgsfield/p06-cully-hill-boys-main-text-2026-08-22.txt`] · case JSON [archive: `higgsfield/projects/P06.json`] · replay 起點 [archive: `browser-evidence/higgsfield/p06-v01-start-2026-08-22.png`] · 57:09 中段 [archive: `browser-evidence/higgsfield/p06-v01-mid-t5709-computer-use-2026-08-22.png`] · 85:06 高風險段 [archive: `browser-evidence/higgsfield/p06-v01-highrisk-t8506-computer-use-2026-08-22.png`] · resume 後片尾 [archive: `browser-evidence/higgsfield/p06-v01-end-resumed-2026-08-22.png`]

- `直接 UI／影片觀察`：published player 時長為 1:54:48；`專案作者自述`：brief 稱全片 137 scenes、2026-08-05 New York premiere、every frame generated、簽約演員 likeness 未實拍，唯一 motion-reference 例外是手機拍攝的 stunt fight。
- `重要口徑`：All assets=473,600、Generations=473,214 是 project aggregated metrics，**本研究未逐項檢查 473,600 assets**。Brief 另稱 Canvas 裡有 600 approved assets（74 leads/antagonists、52 supporting/animals、90 episodic characters、159 props、200+ location plates），兩者是不同層級指標。
- `直接 UI／影片觀察`：root folders：0 Regenerations=562、ACT 1=146,471、ACT 2=140,693、ACT 3=125,007、Epilogue=25,918、PRE PROD=34,388。
- `專案作者自述`：全部影片與 speech 用 Seedance；faces/character sheets 用 Soul Cinema；edits/reverse angles/point changes 用 Seedream/Nano Banana；Claude 分 image/video 兩個 chats，避免平光 anti-CG 規則污染 video 的 FOV/motivated-light 規則。
- `專案作者自述`：LIRA 產 image prompts；CINEDANCE 有 writer/auditor/workbench，workbench 只 patch 失敗 section；Acting System 以 behavior 取代 emotion label。
- `專案作者自述`：2011 是每個 location plate/prompt 的硬限制；角色 manner 與 accent block 固定重複。從 HELL GRIND 沿用 scene context、occupied first-frame spatial lock、每句後 1 秒 silence tail、逐 beat mimic/acting。
- `專案作者自述`：signed actors 的 likeness/voice rights 在 first generation 前以合約完成，release 先送 platform compliance；本研究未審合約，不能把它當法律充分性驗證。
- `專案作者自述`：該案沒有 separate negative block；prohibition 盡量寫成 desired outcome。每個 tag 只放一次於 ACTIVE REFERENCES；location reference 控 geometry/material/light/atmosphere，但不繼承 framing。Brief 自述 Higgsfield 每 generation budget 為 9 images / 3 videos / 3 audio；因本案 Seedance 版本未明，這只能是 Higgsfield project practice，不可外推成 2.5／ModelArk model limit。
- `專案作者自述`：15–20 generations 仍失敗時改 shot design，而非繼續換句子；complex action 放在 timing 開頭／already mid-action。這是團隊的 project ceiling，不是模型平均值。
- `專案作者自述`：生成 speech 多數保留並做 noise/timbre/space cleanup；只有 unusable voice 才 studio record。所有 prompt 固定 `SFX only. No music.`，continuous ambience、sound design 與 music 在 post 建立。
- `直接 UI／影片觀察`：P06 於 14:03:47 從 00:00 啟動，未 pause/seek/reload/navigation。Codex CLI resume 後，保留播放器明確顯示 `114:48 / 114:48` 與 Play 控制，terminal gate 通過；其後 direct seek 補查 57:09（戶外兩人場景）與 85:06（dramatic green-backlit 多人／表演段），首中高風險尾的視覺採樣 gate 已補齊。這不等於音訊/lip-sync 已獨立通過。

## 8. P07 — ZEPHYR

來源對：[原始 project](https://higgsfield.ai/@higgsfield.studio/projects/zephyr) · 本機 main text [archive: `browser-evidence/higgsfield/p07-zephyr-main-text-full-2026-08-22.txt`] · case JSON [archive: `higgsfield/projects/P07.json`] · 片尾證據 [archive: `browser-evidence/higgsfield/p07-v01-end-2026-08-22.png`]

- `直接 UI／影片觀察`：主片 10:48；頁面可見的 brief copy 描述 glamorous female heroes 對抗 alien bug invasion。
- `直接 UI／影片觀察`：All assets=19,002、Generations=18,682；folders 為 Characters=54、Iterations=18,673、Production=275。主頁列出至少 18 個 named assets，例如 concert/battle outfits、cockpit、mecha、rooms、city plates。
- `直接文本觀察`：brief 明確說第一集製作時使用 `Seedance 2.0`，尚未建立 efficient fixed pipeline 或 unified style prefix；因此此案不得支撐 2.5 performance claim。
- `專案作者自述`：五位 heroine 的 personality/acting arcs 先定義；Higgsfield Soul 2 做角色設計，Nano Banana 2 Pro／Seedream 組 character sheets。Battle gear 與 concert outfits 是 distinct states。
- `專案作者自述`：master mecha sheet 若同時放 open hatch/retractable weapon，模型會優先把可見 detail 畫出，甚至與 closed state 衝突並改掉 robot design。做法是從 canonical sheet 移除 inactive state、按場景另做 sheet，需要精細 weapon operation 時提供 separate close-up，且在 prompt 重新寫完整運作過程；sheet 上小文字描述不足。
- `專案作者自述`：brief 的「傳統需 years/millions」沒有可核算 baseline，不得作效率 KPI。
- `直接 UI／影片觀察`：Production 中兩支實際打開的 output 分開列入 inventory，未互相取代。`P07-A01-V01` 是 askar/mecha、10.053991 秒、2 refs、Created 2026-03-27，完成 00:00 [archive: `browser-evidence/higgsfield/p07-generation01-start-t0000-computer-use-2026-08-22.png`]／00:05 [archive: `browser-evidence/higgsfield/p07-generation01-mid-t0005-computer-use-2026-08-22.png`]／00:09 [archive: `browser-evidence/higgsfield/p07-generation01-near-end-t0009-computer-use-2026-08-22.png`]。`P07-A02-V01` 是 rinan/concert、15 秒、4 visible reference links、Created 2026-04-08，完成 00:00 [archive: `browser-evidence/higgsfield/p07-generation02-start-t0000-computer-use-2026-08-22.png`]／00:07 [archive: `browser-evidence/higgsfield/p07-generation02-mid-t0007-computer-use-2026-08-22.png`]／00:13 [archive: `browser-evidence/higgsfield/p07-generation02-near-end-t0013-computer-use-2026-08-22.png`]。兩者 UI 均為 `Seedance 2`、720p/Standard、1280×720；prompt 欄位不可見。
- `直接 UI／影片觀察`：fresh replay 解碼 1920×1080；第一次背景載入曾是 854×480，兩者都只是 stream decode。主片 00:00–00:07 自動播放後有一次診斷 pause，隨即從 00:07 無 seek/reload 繼續，最後到 10:48/10:48。00:07 opening action 有強 motion blur；03:38 cockpit heroine、04:25 nose-patch close-up、07:01 blonde heroine dialogue 均保有清楚 identity/wardrobe；05:18 mech-body contact 可讀、10:01 兩台 mechs 設計相容；09:02 是清楚 black transition。未從靜態證據外推 lip-sync／audio quality。

## 9. P08 — HELL GRIND

來源對：[原始 project](https://higgsfield.ai/@higgsfield.studio/projects/hell-grind) · 本機 main text [archive: `browser-evidence/higgsfield/p08-hell-grind-main-text-2026-08-22.txt`] · case JSON [archive: `higgsfield/projects/P08.json`] · replay 起點 [archive: `browser-evidence/higgsfield/p08-v01-start-2026-08-22.png`] · 47:47 中段 [archive: `browser-evidence/higgsfield/p08-v01-mid-t4747-computer-use-2026-08-22.png`] · 71:09 高風險段 [archive: `browser-evidence/higgsfield/p08-v01-highrisk-t7109-computer-use-2026-08-22.png`] · resume 後片尾 [archive: `browser-evidence/higgsfield/p08-v01-end-resumed-2026-08-22.png`]

- `直接 UI／影片觀察`：published player 為 95:59；`專案作者自述`：brief 稱 95-minute feature、15 人團隊、under $500K、assets 後 14 days generation、2026 Cannes Marché du Film screening、every frame generated，並列 Seedance 2.0／Soul Cinema／Nano Banana Pro／Seedream 4.5／GPT Image 2 分工。
- `重要口徑`：All assets=115,451、Generations=115,446 是 aggregated metrics，未逐項列舉。主頁保留大量 scene folders與重複命名，完整 raw list 在 `research/seedance-2.5/browser-evidence/higgsfield/p08-hell-grind-main-text-2026-08-22.txt`。
- `專案作者自述`：character sheet 包含 close-up、front full-body、back full-body；front full-body 故意無頭，避免 wide shots 使用模糊小臉。Sheet 刻意 flat light/neutral grey/visible pores/no retouch；每個 asset 先做十次 poses/lighting stress test，10/10 recognizable 才鎖定。
- `專案作者自述`：point changes 用 mask 疊回 original；原始 image 不整張過模型第二次，因為 repeated full-image passes 會毀 texture、漂 color、造成 symmetric/plastic/lifeless face。
- `專案作者自述`：voice block 與 behavior profile 固定；wet/wounded/clothes-change 都拆成 separate state assets。locations 用 3/4 plates、visual anchor、single light logic；reverse angle 可用空場 Seedance camera-walk 截圖，再以 image model改善 texture/light。
- `直接文本觀察／專案作者自述`：brief 展示 reference roles、location inheritance ban 與 rigid prompt skeleton；其 claimed production effect 未獨立測試。
- `專案作者自述`：實際 prompt 約 3,000–4,000 words；brief 同時說「length is not the enemy，overloaded beat 才是」，並限制每 beat 約三句。由於此案明示 Seedance 2.0，此長度不可提升成 2.5 best practice。
- `專案作者自述`：GEO SPATIAL LAYOUT 以固定 landmarks、frame-left/right、meter distances、camera side、180° axis 重複進每鏡；first second 用 wide 拍定位置。生成按 scene batches；每次只改一行並記 prompt version/change/verdict。10–15 iterations 仍不成就 split/remove/change angle，這是 project rule。
- `專案作者自述`：threshold transition 同時使用兩個 location assets，以 doorway + warm/cool contrast 解釋 palette change；giants 用 every-prompt scale law + human anchor。Post 先 aggressively trim generated clip edges，再 cleanup extra fingers/boiling/fake text，然後 color unification、generated-voice cleanup、continuous ambience/music。
- `作者自述／未獨立驗證`：95 分鐘、15 人、under $500K、assets 完成後 14 generation days、Cannes Marché du Film screening；這些不能推成 Seedance 2.5 的 cost/speed benchmark。
- `直接 UI／影片觀察`：P08 於 14:07:56 從 00:00 啟動，未 pause/seek/reload/navigation。Codex CLI resume 後，保留播放器明確顯示 `95:59 / 95:59` 與 Play 控制，terminal gate 通過；其後 direct seek 補查 47:47（elderly-man close-up／第二角色）與 71:09（skeletal/demon leader 與 armored group），首中高風險尾的視覺採樣 gate 已補齊。這不等於音訊/lip-sync 已獨立通過。

## 10. P09 — Kok Boru trailer

來源對：[原始 project](https://higgsfield.ai/@higgsfield.studio/projects/kok-boru) · 本機 main text [archive: `browser-evidence/higgsfield/p09-kok-boru-main-text-2026-08-22.txt`] · case JSON [archive: `higgsfield/projects/P09.json`] · 片尾證據 [archive: `browser-evidence/higgsfield/p09-v01-end-replay-2026-08-22.png`]

- `直接 UI／影片觀察`：1:20 trailer，5156×2160 decode；All assets=2,781、Generations=2,693、Credits spent=345,038、Created Jul 11 12:10。
- `直接 UI／影片觀察`：folder tree 以 shot 為單位：SH01=40、SH02=64、SH03=194、SH04=41、SH05=76、SH06=151、SH07=55、SH08=84、SH09=461、SH10=80；另有 FULL10MIN、Project Brief、角色資料夾。
- `專案作者自述`：brief 與 P01 同一套 hybrid production、Style Prefix、Visual Constraints、Claude MCP + 15-page script；差異是 P09 為早期 trailer，post 使用 Artlist music，而 full short 預計 original score。
- `直接 UI／影片觀察`：初次播放與 fresh replay 都到 1:20/1:20。Published frames 右上角燒錄 `HIGGSFIELD SEEDANCE2.0 4K` 圖樣；這是 project/editorial visible label，不是 backend model ID，但明確排除把 P09 當 2.5 output evidence。Late-middle horse+wolf chase 維持 painterly style、主體與方向；01:04 bloody heroine close-up 的臉、髮、衣裝仍可辨，未見明顯融化；片尾正常黑場。

## 11. 跨案模式、反例與不可推論事項

### Brief 文本反覆出現的模式（專案作者自述／跨案相關性）

以下原則的「文字反覆出現」可直接核對，但其品質／效率效果沒有 controlled A/B；不得改標為已證明因果。

1. 多案把 asset 定義為「固定 text descriptor + image reference」，並稱 descriptor／tag 逐字重複到每鏡；這不是模型具有跨鏡 memory。
2. 複雜 blocking 不只靠 prose；diagram/depth map/first-frame geometry 被用於多人、空間、fight 與 reverse angle。
3. prompt 經常採固定區塊順序：context、refs、map、first frame、timed beats、dialogue/audio、physics、light、style、positive locks。
4. continuity 以 separate state assets、anchor objects、reference-role declarations、last-frame chaining、Voice Bible、behavior profile 與 post-production gate 分層處理。
5. 成片不是純 generation output；brief 反覆明示 selection/iteration、rough/fine cut、cleanup、color、sound、voice rerecording 等人工階段。

### 反例／邊界

- P02 明說 `no yellow` negative list 無效，正向色彩配置才有效；P01 sample 卻大量用 `NO ...` 作 visual constraints。九案可支持「正向界定常更可靠」的相關性，不能推論所有否定詞都無效。
- P02 明示 Seedance 2.5；P08 明示 Seedance 2.0；P01 已打開的 generation 顯示 Seedance 2。不得把一案證據套成所有九案都用同一模型版本。
- UI `Quality=4k`、`Size=4032×1728` 與 browser decoded frame 4398×1886 是不同訊號；不能把 decode dimensions 直接當生成 request resolution。
- 文章中的製作方自述（成本、天數、影展）是 project brief claim；未由獨立帳務／production logs 驗證。

### 目前不可見／未知

- 多數 project-level fps、seed、camera/motion UI parameters、retry history、variant genealogy、selected-output chain 尚未顯示。
- 只有在實際 asset viewer 可見時才記 model、quality、bitrate、size、created；未出現的 negative prompt 欄位一律標 `unknown/absent from visible UI`。
- 除 P02-A01-V01 外，模型仍無法從靜態截圖獨立聽覺稽核音色、lip-sync 或聲音漂移；播放器為 unmuted 只證明播放狀態。P02 的本機 AV audit 已完成 stream/decode 與粗粒度嘴部動作對齊，但未把粵語語義、自然度或 phoneme 級同步假稱為已驗證。
- 473,600、115,451 等是 aggregated project metrics，並非 473,600/115,451 個媒體已逐一列入 inventory；目前 inventory 有 14 支直接打開的影片（9 published cuts + 5 generation outputs）。
- Chrome transport blocker 的完整安全操作與缺口記錄在 browser-transport-blocker-2026-08-22.txt [archive: `browser-evidence/higgsfield/browser-transport-blocker-2026-08-22.txt`]。

## 12. 信心與交叉審查

- 索引 9/9、主片時長、聚合 counts、P01/P02/P04 generation prompt/settings 與 P07 generation settings：高信心（直接 UI + 本機證據；P07 prompt 明列不可見）。
- Brief 原文的存在與內容：高信心；其工作流成效、成本、效率與製作史：作者自述，未獨立驗證，信心低至中。
- 播放品質結論：9/9 published cuts 皆有啟動、代表性中段／高風險段與 terminal UI 證據；5/5 directly opened generations 皆有首中近尾 evidence。P02-A01-V01 的 audio stream/decode 與 coarse speech-window/mouth-motion gate 通過；phoneme 級 lip-sync 等高解析度聲音品質仍 `unknown`。
- 需官方文件研究員交叉審查：P02/P04 project-level `Seedance 2.5`、P01/P04/P07 asset-level `Seedance 2`、P07/P08 brief `Seedance 2.0`、P09 burned-in `SEEDANCE2.0` 與官方 backend model identity 的關係。
- 需主代理交叉審查：aggregated asset counts 與 individually inspected media count 的口徑、P02/P04 SSR↔hydrated time 差、音訊不可獨立判讀的限制。
