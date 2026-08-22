# 額外發現

> 存取基準：2026-08-22（Asia/Taipei）。本文件記錄超出原始問題但會影響可靠性、成本、可恢復性或研究解讀的事項。`未實測` 表示本專案沒有呼叫模型驗證。

## F-01：發布文與 API 文件呈現「時間差」，不是永久狀態

- **發現**：`官方事實`。ByteDance 2026-07-31 正式發布文寫 Seedance 2.5 正在 Jimeng／Doubao Pro rollout，BytePlus ModelArk API「coming soon」；BytePlus 2.5 tutorial／prompt guide 於 2026-08-07 首次發布，之後已給正式 model ID 與啟用／呼叫方式。
- **直接證據**：[ByteDance 發布文](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)及本機正文 [archive: `sources/supplemental/bytedance-seedance-2.5-launch-2026-07-31.body.html`]；[ModelArk tutorial](https://docs.byteplus.com/en/docs/ModelArk/2607688)及本機擷取 [archive: `sources/supplemental/byteplus-modelark-2607688-tutorial.extracted.md`]。
- **為何重要**：只引用發布文會錯誤地把 API 現況寫成未推出；只引用新文件又會抹掉當日發布範圍。
- **適用／不適用**：適用於所有 time-sensitive availability claim；不代表任何地區／帳戶必然已啟用。
- **信心／反例**：高；未實際登入帳戶，不能證明本帳戶可用。
- **建議／測試**：每份報告在 availability 旁寫 `as of`、平台、region、文件更新日；正式執行前只讀檢查 console model list。

## F-02：同一 model ID 的 ModelArk 與 LAS 規格不同

- **發現**：`官方事實`。兩者皆列 `dreamina-seedance-2-5-260628`，但 ModelArk tutorial 列 480p／720p／1080p；LAS Enhanced operator 列 480p／720p、24 fps，不支援 1080p。
- **直接證據**：[ModelArk tutorial §Resolution](https://docs.byteplus.com/en/docs/ModelArk/2607688#2.5_resolution)與本機擷取 [archive: `sources/supplemental/byteplus-modelark-2607688-tutorial.extracted.md`]；[LAS output requirements](https://docs.byteplus.com/en/docs/byteplus_las/video_gen_enhanced)與本機擷取 [archive: `sources/supplemental/byteplus-las-video-gen-enhanced.extracted.md`]。
- **為何重要**：model-level capability 與 product-surface capability 不可混用；錯誤的 1080p request 會失敗或改變研究公平性。
- **適用／不適用**：只適用存取日所見文件；不外推 Jimeng、Doubao、Higgsfield。
- **信心／反例**：高；實際帳戶功能可能晚於文件或受 allowlist。
- **建議／測試**：manifest／run ledger 把 platform、endpoint、region、model ID、文件版本都當主鍵；跨平台只比較共同規格。

## F-03：兩平台連 defaults 都不同

- **發現**：`官方事實`。ModelArk 2.5 tutorial 的 `ratio` 預設 `adaptive`、`duration` 預設 `-1`；LAS 文件範例表列 `ratio` 預設 `16:9`、`duration` 預設 `5`。
- **直接證據**：[ModelArk tutorial §Aspect ratio／Duration](https://docs.byteplus.com/en/docs/ModelArk/2607688)；[LAS Generate parameters](https://docs.byteplus.com/en/docs/byteplus_las/video_gen_enhanced)。本機全文同 F-02。
- **為何重要**：省略欄位不是中性行為，會造成 output shape／length 與成本混雜。
- **適用／不適用**：適用 API／operator；UI 可能另有可見 defaults。
- **信心／反例**：高；文件更新後可能改。
- **建議／測試**：所有 production／evaluation request 明設關鍵欄位，不依賴 defaults；query response 核對實際值。

## F-04：Reference「最大 50」不等於「建議 50」

- **發現**：`官方事實`。2.5 可收最多 30 圖、10 影、10 音；同一 prompt guide 卻建議 subject audio/video 1–5 主體、5–10 秒，subject image 1–8 主體較穩；超過後可能降穩定並需多次嘗試。
- **直接證據**：[Prompt guide §Reference asset input recommendations](https://docs.byteplus.com/en/docs/ModelArk/2607689)與本機擷取 [archive: `sources/supplemental/byteplus-modelark-2607689-prompt-guide.extracted.md`]。
- **為何重要**：上限是 validation ceiling，不是品質甜蜜點；堆素材會增加 mapping entropy、成本與失敗診斷難度。
- **適用／不適用**：適用 ModelArk 2.5 文件情境；複雜群像可能仍值得超過建議值。
- **信心／反例**：官方建議信心高；本專案尚無因果 A/B。
- **建議／測試**：從最小 canonical set 起，逐批增加；用 `REF-1／CURATED／REDUNDANT` 受控比較。

## F-05：Task 是由素材、prompt 意圖與 hint 共同決定

- **發現**：`官方事實`。`omni_reference_task_type` 可提早驗 constraints，但模型執行時仍從 prompt 判斷；不一致會 `InvalidParameter.TaskTypeMismatch`。省略／`auto` 可能延後到 asynchronous validation 才失敗。
- **直接證據**：[Tutorial §Task types／Error handling](https://docs.byteplus.com/en/docs/ModelArk/2607688#2.5_compatibility)與[API `omni_reference_task_type`](https://docs.byteplus.com/en/docs/ModelArk/1520757)；本機 tutorial [archive: `sources/supplemental/byteplus-modelark-2607688-tutorial.extracted.md`]、API [archive: `sources/supplemental/byteplus-modelark-1520757-create-video.extracted.md`]。
- **為何重要**：正確 parameters 不能救含糊 prompt，反之亦然；asynchronous failure 會浪費排隊時間。
- **適用／不適用**：適用 ModelArk Seedance 2.5 omni reference tasks。
- **信心／反例**：高；未實際觸發錯誤。
- **建議／測試**：edit／extend／reference 明設 hint，prompt 第一行用一致動詞；送出前做 schema validation。

## F-06：First/last frame 有兩種語義，不可混稱

- **發現**：`官方事實`。用 `content.role=first_frame/last_frame` 會鎖輸出畫幅、較嚴格對齊；把圖片當 `reference_image` 再在 prompt 說它是首尾幀，屬 unlocked reference，可能相似但不保證精確。
- **直接證據**：[Prompt guide §First and last frames](https://docs.byteplus.com/en/docs/ModelArk/2607689)與本機全文 [archive: `sources/supplemental/byteplus-modelark-2607689-prompt-guide.extracted.md`]。
- **為何重要**：同一句「use as first frame」可能是完全不同的 task contract；會影響畫幅、alignment 與錯誤處理。
- **適用／不適用**：適用 ModelArk API；其他 UI 如何映射 role 待驗。
- **信心／反例**：高。
- **建議／測試**：需要精確首尾時用 role；要保持自選畫幅／較自由創作才用 reference_image，並在報告分開命名。

## F-07：Storyboard 與 independent keyframes 的控制粒度不同

- **發現**：`官方事實`。多 panel storyboard 主要提供高層 plot／shot structure，不嚴格逐格對齊；獨立 keyframe images 可較嚴格對齊。官方建議 storyboard ≤15 panels、用簡單 line art、避免圖上文字。
- **直接證據**：[Prompt guide §Multi-panel storyboards／Keyframe reference](https://docs.byteplus.com/en/docs/ModelArk/2607689)及本機全文 [archive: `sources/supplemental/byteplus-modelark-2607689-prompt-guide.extracted.md`]。
- **為何重要**：把 storyboard 當硬 keyframes 會錯估失敗；把每格拆圖則增加 reference 與 transition 負擔。
- **適用／不適用**：適用 2.5 reference workflow；不是保證每張 keyframe 都命中。
- **信心／反例**：高；精確程度仍待實測。
- **建議／測試**：先依需求選 control object；future evaluation 做相同 beats 的 storyboard vs keyframe paired test。

## F-08：Editing duration tolerance 的兩份官方文件不一致

- **發現**：`官方事實／文件矛盾`。Prompt guide（updated 2026-08-13）寫 edit output 與 input 最多約差 0.3 秒；較新的 tutorial（updated 2026-08-18）寫可能短最多 0.4 秒。Guide 另稱若 input 是 Seedance 2.5 output，duration 不會不同。
- **直接證據**：[Prompt guide §Locked tasks](https://docs.byteplus.com/en/docs/ModelArk/2607689)、[tutorial §Video duration](https://docs.byteplus.com/en/docs/ModelArk/2607688#2.5_duration)及兩份本機全文。
- **為何重要**：frame-accurate conform、對白／字幕／music edit 不能假設 duration bit-exact。
- **適用／不適用**：適用 ModelArk edit；LAS／UI 待另驗。
- **信心／反例**：對矛盾的存在信心高；實際 tolerance 未測。較新 tutorial 暫作保守工程界線，但不是宣布 guide 失效。
- **建議／測試**：以 response／media probe 的實際 frames conform；保留原音與 EDL；同時測 2.5-origin 與外部 input。

## F-09：MOV 是後期品質路徑，但不是萬用相容格式

- **發現**：`官方事實`。2.5 的 MOV 使用 H.264 + YUV 4:4:4 + PCM，官方推薦 edit／extension input/output 都用 MOV，以較好維持 color／brightness／AV consistency；部分播放器不相容。1080p 則是 10-bit H.265/HEVC，屬另一條路徑。
- **直接證據**：[Tutorial §Output format／Resolution](https://docs.byteplus.com/en/docs/ModelArk/2607688)、[API output_format](https://docs.byteplus.com/en/docs/ModelArk/1520757)。
- **為何重要**：`mov` 容器不自動代表 10-bit；錯誤解碼／tagging 會讓生成品質被播放環境誤判。
- **適用／不適用**：適用 ModelArk 2.5；distribution master 可能仍要其他 codec。
- **信心／反例**：高；實際色彩 round-trip 未測。
- **建議／測試**：保存原檔；用支援 4:4:4／PCM／HEVC 的播放器與 NLE；做 decode／conform／color-tag regression。

## F-10：`seed` 可控制隨機性，但不是完全重現

- **發現**：`官方事實`。ModelArk 2.5 支援 `seed` `[-1, 2147483647]`；`-1` 會以隨機值替換；同 request + 同 seed 只產生相似結果，官方明寫不保證完全一致。
- **直接證據**：[API `seed`](https://docs.byteplus.com/en/docs/ModelArk/1520757)與本機 API 全文 [archive: `sources/supplemental/byteplus-modelark-1520757-create-video.extracted.md`]。
- **為何重要**：同 seed paired test 可降低隨機差，但不能把不同輸出都當 pipeline bug；cache／dedupe 也不能只看 seed。
- **適用／不適用**：適用 ModelArk 2.5；LAS 是否正式支援 seed 的參數表未清楚列出，不外推。
- **信心／反例**：高；實際 variance 未測。
- **建議／測試**：記 request hash + seed + output hash；做 same-seed repeat audit 和 multi-seed distribution。

## F-11：`return_last_frame` 是 handoff 能力，也可能放大錯誤

- **發現**：`官方事實 + 團隊推論`。API 可回傳無 watermark PNG 末幀供下一段首幀；但若末幀身份／姿勢／光色已漂移，直接鏈接會把錯誤變成新條件。
- **直接證據**：[API `return_last_frame`](https://docs.byteplus.com/en/docs/ModelArk/1520757)；錯誤累積風險由 EntityBench／EntityMem 的 per-entity verified memory 方法啟發，本機預印本 p.5–6 [archive: `sources/supplemental/arxiv-2605.15199-entitybench.pdf`]。
- **為何重要**：自動 extension chain 容易把「最新」誤當「正確」。
- **適用／不適用**：handoff 原則適用所有 sequence；研究論文不是 Seedance product proof。
- **信心／反例**：API 能力高；對 2.5 改善幅度低至中。
- **建議／測試**：末幀先過 fidelity／motion blur／neighbor gate；和 canonical+gated memory 做長距離 A/B。

## F-12：生成音訊是 mono，且 `generate_audio` 預設 true

- **發現**：`官方事實`。API 文件列 `generate_audio` 預設 true，所有帶音訊生成影片皆為 mono，無論 input channels。
- **直接證據**：[API `generate_audio`](https://docs.byteplus.com/en/docs/ModelArk/1520757)與本機全文 [archive: `sources/supplemental/byteplus-modelark-1520757-create-video.extracted.md`]。
- **為何重要**：不明設 false 可能生成不需要的對白／BGM；mono 不能直接取代專業多軌 soundscape。
- **適用／不適用**：適用文件列支援的 Seedance 2.5／2.0／1.5 Pro。
- **信心／反例**：高；Higgsfield 可能另有後處理。
- **建議／測試**：picture-only runs 明設 false；音訊 runs 記 speaker／language／ambience，之後 ADR／foley／stereo／immersive mix。

## F-13：真人臉 reference 有直接上傳限制與合規替代路徑

- **發現**：`官方事實`。ModelArk tutorial 寫 2.5 不支援直接上傳含真人臉的 reference image／video；平台提供 trusted model outputs、preset digital characters、authorized real-person assets 等合規方案。
- **直接證據**：[Tutorial §Create portrait videos／Usage limits](https://docs.byteplus.com/en/docs/ModelArk/2607688#2.5_multimodal_input)與本機全文 [archive: `sources/supplemental/byteplus-modelark-2607688-tutorial.extracted.md`]。
- **為何重要**：長片 character bank 若從錯誤管道建立，會在 API validation／moderation 才暴露，也可能違反肖像權。
- **適用／不適用**：適用 ModelArk；不表示其他平台允許任意真人臉。
- **信心／反例**：高；實際 authorized asset workflow 未執行。
- **建議／測試**：權利與 asset ID 在 Gate 0 解決；不得繞過限制或保存私人 token。

## F-14：輸出與 task metadata 有短保留期

- **發現**：`官方事實`。ModelArk tutorial 列 task records 保留 7 天；video URL 24 小時、最多下載 100 次。
- **直接證據**：[Tutorial §Retention period](https://docs.byteplus.com/en/docs/ModelArk/2607688#2.5_storage_duration)與本機全文 [archive: `sources/supplemental/byteplus-modelark-2607688-tutorial.extracted.md`]。
- **為何重要**：若沒有 ingestion／hash／backup，研究與長片將不可重現；保存 signed URL 又有洩露風險。
- **適用／不適用**：適用 ModelArk 文件；LAS 或 UI retention 需另查。
- **信心／反例**：高。
- **建議／測試**：成功 task 立即合法下載受控 storage、media probe、hash；manifest 只留去 query 的來源與本機檔，不保存 signed URL。

## F-15：官方推薦的 `sd25-pe` skill 是便利工具，也是 supply-chain 邊界

- **發現**：`官方事實`。Prompt guide／tutorial 建議用 `npx --yes skills@latest add ... --skill sd25-pe --yes` 安裝 prompt optimization skill。
- **直接證據**：[Prompt guide §Get the skill](https://docs.byteplus.com/en/docs/ModelArk/2607689)、[tutorial §Prompt skill](https://docs.byteplus.com/en/docs/ModelArk/2607688)與本機全文。
- **為何重要**：`latest` + `--yes` 會在本機執行／安裝當下內容；若不固定版本與檢查來源，未來結果與安全都不可重現。
- **適用／不適用**：工具由官方文件推薦，但本研究沒有安裝，也不需要它才能讀取 prompt 規則。
- **信心／反例**：官方推薦存在的信心高；其實際程式碼、版本、權限與效果未知。
- **建議／測試**：另案審查 package／skill manifest、hash、version、permissions、network／file writes，再決定是否 sandbox 安裝；不可在此 goal 擅自執行。

## F-16：美感高不等於可交付；先做 fidelity gate

- **發現**：`一手研究 + 實務建議`。VBench-2.0 區分 superficial 與 intrinsic faithfulness；EntityBench 指出若只看跨鏡 self-similarity，可能獎勵「每次都長得一樣但其實是錯角色」的輸出，故先做 per-shot fidelity gate。
- **直接證據**：VBench-2.0 p.2 [archive: `sources/supplemental/arxiv-2503.21755-vbench-2.0.pdf`]；EntityBench p.5–6 [archive: `sources/supplemental/arxiv-2605.15199-entitybench.pdf`]。
- **為何重要**：漂亮、流暢或 embedding 高都可能掩蓋故事、身份、物理、道具或空間錯誤。
- **適用／不適用**：評測原則普遍適用；論文中的 metrics／threshold 不直接適用 Seedance。
- **信心／反例**：架構原則中高；特定自動 metric 的 human alignment 需本專案校準。
- **建議／測試**：評分順序固定為 intra-shot quality → prompt/entity fidelity → cross-shot consistency → editorial usability，missing／gate-fail 不靜默排除。

## F-17：A、B 的音訊標記是 prompt syntax，不是硬參數

- **發現**：`官方事實／文件表述差異`。來源 A 列 `(...)` music、`<...>` SFX、`{...}` dialogue、`【...】` subtitles；BytePlus tutorial／prompt guide 同時有以雙引號寫 dialogue 的官方例子。
- **直接證據**：[來源 A](https://bytedance.larkoffice.com/docx/A88jd0B47oAd8zxWp5ycZFMfnxh)；[BytePlus tutorial §Prompt rules](https://docs.byteplus.com/en/docs/ModelArk/2607688)與本機全文。
- **為何重要**：把符號誤作 JSON／權重會產生不存在的欄位；混用多套符號也降低可讀性。
- **適用／不適用**：可用於 prompt authoring；不保證逐字／逐音效 adherence。
- **信心／反例**：官方語法存在信心高；哪套效果較好未測。
- **建議／測試**：專案選一套 syntax、同時明寫 speaker／language／accent／tone；future eval 對同內容做 syntax A/B，不改其他變因。

## F-18：物理或構圖一直失敗時，改控制輸入是優先測試的假說

- **發現**：`專案作者自述／待實測`。ZEPHYR: Special brief 描述 prompt-only 的 upside-down physics 失敗後，把人物 reference 直接倒置；另以 layout image 提供位置／方向，再只指定關鍵 anchors 讓模型生成可供剪輯選擇的 camera variation。Red Flag 也把 open/closed window 分成不同 state assets，並用 diagram/location 分離 geometry 與 surface/light。
- **直接證據**：P04 brief capture [archive: `browser-evidence/higgsfield/p04-zephyr-special-main-text-2026-08-22.txt`]、P02 brief capture [archive: `browser-evidence/higgsfield/p02-red-flag-main-text-2026-08-22.txt`]、[九案報告](higgsfield-nine-projects.md)。
- **為何重要**：若 input 本身和目標 physics/state 相反，模型同時要解決身份、狀態、空間與運動；文字越長不一定降低這個衝突。
- **適用／不適用**：適合倒置、特定 pose、門窗／道具 state、多人 blocking、複雜 camera path；簡單鏡頭不必為流程而增加資產。
- **信心／反例**：跨兩案方向一致，信心中；沒有 controlled A/B，不能量化收益。
- **建議／測試**：同 shot 比較 prompt-only、state asset、layout/keyframe 三組；固定 seed paired blocks 並量 prompt adherence、retries、human prep time 與 approved-second cost。

## F-19：Feature 專案的巨大 counters 不是效率證據

- **發現**：`直接 UI 觀察 + 專案作者自述／證據限制`。Cully Hill Boys UI 顯示 473,214 generations、HELL GRIND 顯示 115,446；其 briefs 另自述片長、團隊、成本或天數，但沒有公開逐 run 帳務、人時、並行度、失敗分布與 post 時間。
- **直接證據**：P06 capture [archive: `browser-evidence/higgsfield/p06-cully-hill-boys-main-text-2026-08-22.txt`]、P08 capture [archive: `browser-evidence/higgsfield/p08-hell-grind-main-text-2026-08-22.txt`]、projects index [archive: `higgsfield/projects-index.json`]。
- **為何重要**：asset/generation counters 可能包含 tests、regenerations、attachments 或 project history；除以片長不會自動得到 cost/second、成功率或速度。
- **適用／不適用**：適用所有 project-page marketing/self-report metrics。
- **信心／反例**：對 counters 的 UI 讀值信心高；對其定義與效率含義信心低。
- **建議／測試**：只用實際 run ledger 計算 first-pass approval、retry distribution、usable seconds/hour、cost/approved second、human hours 與 waste；self-report 只作 context。

## F-20：剪輯提前介入是重複出現的速度導向流程，不是省略後期

- **發現**：`專案作者自述／跨案相關性`。Cully Hill Boys、HELL GRIND 明示 edit 與 generation 平行，讓 editor 反向提出 masters、reaction、insert、cutaway 或重排需求；ADILIADA、ONEIRIC 則明確描述 `assembly → rough cut → generation supervision → fine cut → picture lock` 的迭代回路。四案在 picture lock 後仍有 cleanup、color、sound、music、voice/subtitle 工作。
- **直接證據**：P03/P05/P06/P08 的本機 brief captures與[九案報告](higgsfield-nine-projects.md)。
- **為何重要**：延後剪輯會把資源花在不能進 cut 的漂亮 shots；完全取消後期又會留下跨 generation color/audio/text/cleanup 不一致。
- **適用／不適用**：適合所有 multi-shot／long-form；單一短 clip 的收益較小。
- **信心／反例**：四案重複出現，流程相關性信心中高；尚未證明因果或最佳重疊比例。
- **建議／測試**：比較 sequential production 與 rolling assembly；記 coverage-hole 發現時間、已浪費 runs、pickup 數、picture-lock wall-clock 與人工協調成本。

## F-21：Project 名稱、brief 與 generation-level model label 必須分層

- **發現**：`直接 UI 觀察 + 專案作者自述`。P02 project brief 與已開 generation 都明示 Seedance 2.5；P04 brief 明示 2.5，但 sampled asset UI 只顯示 `Seedance 2`；P07/P08 briefs 明示 2.0；P09 成片剪輯圖樣顯示 2.0，但不是 backend model ID；其他多只能確認 generic `Seedance`。Project 日期或系列名稱不能替代 generation-level model evidence。
- **直接證據**：[九案報告](higgsfield-nine-projects.md)、P02 generation viewer [archive: `browser-evidence/higgsfield/p02-generation01-viewer-2026-08-22.png`]、各 project JSON。
- **為何重要**：把 workflow observation 誤歸模型版本會讓 prompt、品質與效能結論失真。
- **適用／不適用**：適用第三方平台、remix workspace、跨版本專案。
- **信心／反例**：UI/brief 直接觀察信心高；`Seedance 2` label 的精確 backend snapshot 仍 unknown。
- **建議／測試**：run ledger 分開保存 project claim、UI feature label、backend model ID、created time 與 platform build；不能確認時標 `unknown`。

## F-22：角色一致性的第一個 gate 是權利，不是 prompt

- **發現**：`專案作者自述 + 實務建議`。Cully Hill Boys brief 說 signed actors、contract photography、likeness/voice rights 在 first generation 前完成並送 compliance；官方 ModelArk 另對真人臉 references 設有限制與授權資產路徑。
- **直接證據**：P06 capture [archive: `browser-evidence/higgsfield/p06-cully-hill-boys-main-text-2026-08-22.txt`]、ModelArk tutorial 的 portrait/usage limits、[F-13](#f-13真人臉-reference-有直接上傳限制與合規替代路徑)。
- **為何重要**：技術上穩定的 face/voice passport 若沒有可驗證授權，仍不可成為 production asset。
- **適用／不適用**：真人 likeness、voice、music、品牌、字型與 reference footage。
- **信心／反例**：官方平台限制信心高；P06 合約完整性只有作者自述，未審法律文件。
- **建議／測試**：在 Gate 0 保存 release/asset ID/usage scope/territory/term/owner/approval；生成與 QA 系統只接受 rights status=`approved` 的 canonical asset。

## F-23：Prompt timestamp 是語意排程，不是輸出時長硬保證

- **發現**：`官方事實 + 直接 UI／影片觀察`。ModelArk 以獨立 `duration` 參數設定任務時長，prompt guide 另支援整秒 timestamps。P02 抽查的 Seedance 2.5 prompt 文字時間線結束於 25 秒，但 UI 顯示實際影片長 29.056 秒，且應在 23–25 秒出現的 lamp shot 約到 00:28 才出現。當時的獨立 `duration` 設定未在該檢視層顯示，不可倒推。
- **直接證據**：[ModelArk task 文件](https://docs.byteplus.com/en/docs/ModelArk/1520757)與本機擷取 [archive: `sources/supplemental/byteplus-modelark-1520757-create-video.extracted.md`]；P02 完整 prompt [archive: `browser-evidence/higgsfield/p02-generation01-text-2026-08-22.txt`]；[P02 時碼／設定觀察](higgsfield-nine-projects.md#3-p02--red-flag)。
- **為何重要**：長片剪輯若把 prompt 時碼當成 frame-accurate 時長，對白、音樂 hit point、反應鏡與 handoff 都可能整體漂移。
- **適用／不適用**：適用所有含時間線、多鏡、對白或音樂節點的任務；不代表 timestamp 無效，也不證明所有輸出都會拉長。
- **信心／反例**：對「參數與 prompt 是不同控制層」信心高；時間漂移的頻率與方向只有一支直接樣本，信心低，不可外推。
- **建議／測試**：分開記錄 requested duration、prompt milestone、actual duration 與每個 milestone 的實測 timecode；剪輯預留 handles，並在未來評測中統計 start/end drift 及對白 hit-point error。
