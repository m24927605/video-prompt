---
name: photography-aesthetics
description: Design or critique photographic and cinematic visual direction for image prompts and video visual-look subcontracts using lighting, framing, lenses, tone, color, texture, film styles, and motion. Use for visual-direction prompts, photo analysis, and image-edit instructions; do not use for complete video shot/clip contracts, production planning, or generation APIs.
---

# 攝影美學技法庫

一套 72 項可組合的攝影／電影美學技法，加上實務補充維度。
核心用途是**把模糊需求翻譯成精確提示詞**，其次是**用一致的語彙拆解既有影像**。

## Skill ownership and handoff

本 skill 擁有 image prompt 的視覺方向，以及 video 的 **visual-look subcontract**：光、構圖、鏡頭、
色彩、質感、攝影機運動與主體動作的視覺描述。它可以交付一段可嵌入的 look/motion brief，
包括畫面 opening、可見的 change 與 end，但不決定 provider、task、reference scope、timeline、
blocking、physics、acting、audio、end-state acceptance 或操作契約。

- 完整 AI-video single shot／clip prompt，或任何需要 task、references、timeline、blocking、physics、acting、audio、end state、acceptance 的交付，一律 route 到 `seedance-prompt-director`；本 skill 只提供 visual-look subcontract。
- multi-shot、長片、跨鏡 continuity、production planning 或 post-production，route 到 `seedance-film-producer`。
- 生成後的證據診斷，route 到 `seedance-video-qc`。

不要把這個 library 的建議當成平台通則。平台 UI、模式、長度、negative 欄位、參數與 operation 是否支援
transition／edit／extension，皆由 `seedance-prompt-director` 根據已驗證的 provider/task contract 決定。
Do not default aspect ratio, duration, resolution, or format. In a video visual-look subcontract, omit aspect ratio,
duration, resolution, format, frame rate, and provider fields unless the user or selected surface/runtime has confirmed them.
When the target model or provider is unknown, keep an image prompt provider-neutral. Do not name compatible models,
claim cross-model reliability, or recommend a negative-prompt field or provider parameter syntax; those controls remain
unknown until the user selects a runtime.
While it remains unknown, the complete reply must stay narrow: do not mention model names, compatibility,
negative-prompt fields, future model conversion, or provider syntax even as a disclaimer or follow-up offer.

48 項攝影技法與 24 項影視風格已完整轉寫到 `references/` 的 `.md` 參考檔；
編號與中文標籤原樣沿用，不要改動。產生提示詞時一律讀文字參考檔。

---

## 第一原則：技法是正交的軸，不是一堆並列的形容詞

最常見的失敗是「把好聽的技法全部塞進提示詞」。那會讓模型收到互相矛盾的指令，
產出一張誰都不像的平庸圖。

正確做法：**把技法理解成獨立的軸，每個軸最多選一項**，然後照固定順序組裝。

| 軸 | 決定什麼 | 選項來自 |
|---|---|---|
| 1 景別 | 主體在畫面中多大、切在哪 | 19–21, 23, 31, 32 |
| 2 鏡頭 | 透視、臉部比例、背景壓縮、畫幅 | 焦距表 + 畫幅表（`references/03-framing.md` 第 10 軸）|
| 3 相機高度 | 觀眾與主體的權力關係 | 17, 33, 39（眼平是必須明寫的檔位，不是省略時的落點，見 `references/03-framing.md`）|
| 4 主體朝向 | 開放還是封閉、有無眼神接觸 | 26, 28, 29, 30 |
| 5 光位 | 立體感從哪裡來、陰影落在哪 | 03, 04, 05, 07, 13, 27（＋10, 14 為可加的補充光） |
| 6 光質 | 陰影邊緣硬還是軟 | 09, 47（＋15, 18, 48 為特殊光形） |
| 7 光源與色溫 | 畫面的「時間感」與真實感 | 06, 08, 11, 12, 36, 41 |
| 8 影調與對比 | 亮度重心、動態範圍 | 02, 42, 43, 44, 46（＋37, 40 為照度） |
| 9 色彩 | 色溫傾向、飽和度、配色關係 | 01, 16, 38, 45 + 色彩關係六種 |
| 10 景深與動態 | 主體與環境的關係 | 22, 24, 25 |

第 11 層是**影視風格**（圖二 01–24）：它不是一個軸，而是**上面十軸的預設組合包**。
選了風格包就等於一次選定多個軸，此時只需覆寫想調整的個別軸，**最多覆寫 2 軸**
（超過 2 軸等於沒選風格包，改成從十軸重新組）。各風格包鎖死哪幾軸，見 `references/05-recipes.md` 表 C。

拍影片時還有第 12 軸：**攝影機運動 + 主體動作**（`references/08-motion.md`）。

---

## 完整索引（72 項）

### 圖一：攝影技法 48 項

**光位與光形**（→ `references/01-lighting.md`）
`03 側光` `04 側逆光` `05 背光` `07 頂光` `10 髮絲光` `13 底光` `14 輪廓光` `27 正面光`

**光質與強度**（→ `references/01-lighting.md`）
`09 柔光` `15 舞台光` `18 丁達爾光` `37 弱光` `40 強光` `47 硬光` `48 閃光燈`

**光源與色溫**（→ `references/01-lighting.md`）
`06 暖光源` `08 窗光` `11 自發光` `12 火光` `36 冷光源` `41 雙性照明`

**影調、對比與色彩**（→ `references/02-tone-color.md`）
`01 暖色調` `02 過度曝光` `16 高飽和` `38 冷色調` `42 暗色調` `43 低對比度` `44 亮調` `45 低飽和` `46 高對比`

**景別、景深與動態**（→ `references/03-framing.md`）
`19 近景` `20 中景` `21 遠景` `22 深景深` `23 全身照` `24 動態模糊` `25 淺景深` `31 極端特寫` `32 特寫`

**視角與構圖**（→ `references/03-framing.md`）
`17 高角度拍攝` `26 斜側視角` `28 背面視角` `29 側面視角` `30 四分之三側面` `33 鳥瞰` `34 封閉構圖` `35 居中構圖` `39 低角度視角`

### 圖二：影視風格 24 項（→ `references/04-film-styles.md`）

`01 德國表現主義` `02 義式驚悚紅綠光` `03 北歐冷冽` `04 魔幻時刻`
`05 煙霧體積光` `06 單光源夜戲` `07 單點透視對稱` `08 平面正面構圖`
`09 固定長鏡頭` `10 手持跟拍` `11 三色印片` `12 柯達克羅姆`
`13 港片霓虹` `14 數位早期` `15 沙塵單色` `16 黑白默片`
`17 VHS 錄影帶` `18 十六毫米顆粒` `19 偽紀錄片` `20 定格動畫質感`
`21 賽博龐克街景` `22 太空歌劇` `23 生活寫實` `24 宇宙恐怖`

> 圖二原表註記：「以下為攝影技法歸納，括號內為風格參照，非指涉特定作品。」
> **提示詞中不可寫導演姓名或片名** —— 一律展開成具體技術描述（光、鏡頭、色彩、質感、構圖）。
> 模型對「具體技術描述」的反應遠比對「導演名」精確。技術／載體名詞（Technicolor、
> Kodachrome、VHS、16mm、DV、anamorphic）可以保留，因為那些是真實存在的成像介質。
> `09 固定長鏡頭` `10 手持跟拍` `19 偽紀錄片` 三項在**靜態圖上幾乎無效**，
> 生圖情境遇到請改用 `references/08-motion.md` 第五節給的靜圖等效替代。

---

## 標準工作流程

### 步驟 0（每次都做）：確定目標模型

不同模型的提示詞是不同方言 —— 自然語言段落 vs 逗號分隔關鍵詞、有無 negative prompt、
畫幅怎麼給，全都不一樣。把 Midjourney 參數餵給 GPT Image 2 會被當成字面文字畫進圖裡。
使用者未指定時，先交付 provider-neutral 自然語言 prompt；只有方言差異會實質改變所求交付時才追問。
不得列出「相容模型」、推測 negative 欄位或補任何 provider 語法。細節見 `references/09-model-dialects.md`。

### A. 產生提示詞（最常見）

1. **先確定主體**。沒有主體的風格描述等於沒有圖。輸出前必須通過下方的〈輸出閘門〉。
2. **判斷需求落在哪幾個軸**。使用者說的通常是情緒詞或流行標籤。
   抽象情緒（溫暖、緊張）查 `references/05-recipes.md` 的〈情緒 → 技法對照表〉；
   華語圈視覺標籤（氛圍感、高級感、日系、老錢風）查 `references/10-zh-lexicon.md`。
3. **每軸選一項，不要貪**。3–6 項技法是甜蜜點；超過 8 項模型開始丟失指令。
4. **檢查衝突**。對照 `references/05-recipes.md` 的三張表：同軸互斥、跨軸矛盾、風格包鎖定。
   跨軸矛盾比同軸互斥更常見也更難發現，一定要查表 B。
5. **照固定順序組裝**（順序即權重，越前面影響越大）：

   ```
   主體 → 景別 → 鏡頭焦距 → 視角/朝向 → 光位 → 光質 → 光源與色溫
        → 影調與對比 → 色彩 → 景深 → 質感/載體 → 風格總結
   ```

6. **輸出時同時給出技法清單**，讓使用者知道你選了什麼、可以改哪一項。

### B. 分析既有照片

照 `references/06-analysis.md` 的逆向拆解流程走：先讀眼神光與鼻影定出光位，
再由陰影邊緣過渡寬度定出光質，依序填滿各軸，最後輸出標準化的技法標註。

### C. 需求太模糊時

最多問 3 個問題就要開始做。問題設計與「使用者常說的話 → 他其實要的技法」
對照表在 `references/06-analysis.md`。真的問不到就用該檔的〈預設值與安全牌〉。

### D. 提供影片的 visual-look subcontract

先讀 `references/08-motion.md`，輸出可交給 `seedance-prompt-director` 的視覺子契約：
opening look、可見的 change、end look、camera 與 motion。這不是完整影片提示詞，也不決定
provider task contract。若使用者要完整 shot／clip prompt，先 hand off；cut 或 transition 只能在
該 operation contract 明確允許時，由 `seedance-prompt-director` 納入。

第四個欄位是 **invariants**：整段必須維持同一狀態的 look 屬性（主光方向、色彩、質感／載體、天氣），
一行一項。opening → change → end 只回答什麼會變，invariants 回答什麼不准變 —— 沒有被宣告成不變的
屬性，等於允許模型在片段中途重抽它。寫法（含只列環境與光學層的界線）見 `references/08-motion.md`。

使用者若 explicitly excludes blocking 或 timeline，該 scope lock 優先於通用的主體／motion checklist：
visible change 只描述 environmental 或 optical look 的變化，例如雨絲可見度、反射、光色或質感演變；
do not invent subject action or position、pose、eyeline、beat duration 或事件順序。In a scoped visual-look subcontract,
do not invent exposure、camera distance、timing 或 light ratio 的數值；只有使用者或已驗證來源提供時才保留。
Exact numeric values explicitly provided by the user, such as `35mm`, must be preserved; do not add any other numeric
motion amplitude、lighting、exposure、distance 或 timing value.

### E. 使用者給了一張圖要修改

**不要照 A 流程寫一整段十軸提示詞** —— 那會讓模型重畫並毀掉原圖。
讀 `references/11-image-input.md`：核心規則是**只寫要改什麼 + 要保留什麼**，
絕不重述圖中已存在的內容。而且光位、視角、景別、構圖靠提示詞幾乎改不動，
遇到這類要求要明講「這需要重新生成而非編輯」，並直接提供重生用的完整提示詞。

---

## 輸出閘門（不通過不准輸出提示詞）

Agent 最常犯也最致命的錯，是在使用者只丟情緒詞時就輸出一段全是風格與光線形容詞、
主體只有 `a person` 的提示詞。輸出前逐項檢查：

以下主體／動作 checklist 適用於完整 image prompt，不適用於使用者明確限縮的 video visual-look
subcontract。後者只填被要求的視覺維度，不得為了通過 checklist 自行加入人物、姿勢或動作。

- [ ] **主體是具體名詞**，不是 `a person`（例：`a woman in her late 30s, short bleached hair`）
- [ ] **有進行中的動詞**，不是 `standing` / `looking at camera`
- [ ] **有姿態與重心**（`weight on her left leg, shoulders turned away from camera, mid-stride`）
- [ ] **有表情與視線方向**（`gaze off-frame left, jaw tense`）
- [ ] **有具體地點**，不是 `in a room`
- [ ] **手有明確狀態**（`hands in her pockets` / `holding a chipped mug`）—— 沒寫清楚模型會生出畸形手
- [ ] **主體描述佔提示詞的前三分之一**
- [ ] **亞洲主體有明寫族裔與具體外貌**（見 `references/10-zh-lexicon.md` 硬規則），否則模型會 default 白人臉
- [ ] **查過表 B 跨軸矛盾**，沒有互相打架的技法
- [ ] 若使用者或已選定 runtime 明確指定畫幅，已將它放在正確的參數區；否則保持未指定
- [ ] **提示詞裡沒有指向本次未一起送出之文件的詞**（母版／已核准／其他視圖／同上一版），也沒有要求讀者回頭蒐集規格再相減的句子（除…外／其餘／該處），每一句單獨讀都畫得出來（硬規則 16）
- [ ] **沒有描述「這份文件」的句子**（版本、母版、幾張圖之間的關係）—— 這類句子會被畫進圖裡

（上面兩項不受本清單開頭那段主體／動作豁免的限制。硬規則 16 管的是**所有會被送出的字串**，
visual-look subcontract 同樣要過這兩項；圖生圖提示詞走的是 `references/11-image-input.md` 2-4 那張
專屬閘門，本清單不適用於它，但硬規則 16 這條規則本身照樣適用。）

診斷捷徑：**數名詞與形容詞的數量，形容詞多於名詞就是壞提示詞，砍形容詞。**

---

## 硬規則

1. **禁止無效堆砌詞**：`beautiful`、`masterpiece`、`8k`、`high quality`、`award winning`、
   `ultra detailed`、`trending on artstation`。這些對當代模型沒有作用，只會稀釋有效指令的權重。
2. **禁止在提示詞中出現導演姓名或電影片名**。展開成技術描述。
3. **同一個軸只能出現一項**，而且要另外查跨軸矛盾表。「柔和的硬光」「明亮的暗調」是自相矛盾的指令。
4. **主動視覺控制上限 8 項**。圖一／圖二技法與天氣合計計入；天氣沒有圖表編號，但仍佔 1 項。焦距、畫幅與構圖補充不計入。超過就砍掉最不重要的控制，讓模型自己決定。
5. **提示詞用英文寫，說明用繁體中文**。生成模型的訓練語料以英文攝影術語為主。
6. **完整 image prompt 可用數字消除美學歧義**。「側光」不如 `90 degree side key light`，
   「淺景深」不如 `85mm at f/1.4`；但數字是創意建議，不是 runtime 事實。使用者明確限縮的
   visual-look subcontract 不得自行補 exposure、distance、timing、light ratio 或生成參數。
7. **描述陰影，不只描述光**。模型判斷光位主要靠陰影落點，寫清楚暗部在哪。
8. **畫幅是 delivery/runtime 決策，不是美學預設。** 使用者或已選定 surface 沒有確認時保持未指定；不得因「電影感」自行補成 2.39:1、16:9、1:1 或其他比例。已確認的比例遇上表達不了它的輸出容器時，處理方式見 `references/03-framing.md`〈畫幅比例〉。
9. **降飽和或強色偏時必附 `preserve natural skin tone`**，否則人會變灰屍。
10. **「不要太假」不靠加光，靠加質感**。依序加皮膚組 → 成像瑕疵組 → 材質組，
    一次只加一組再重生，不要動光位（見 `references/07-beyond-the-charts.md`）。
11. **「要有電影感」先加一個時段 + 一個天氣**，再考慮風格包 —— 那比堆風格有效得多。
12. **中文字入畫幾乎必然出錯**。改成在畫面預留乾淨區塊、文字後製加。
13. **超過 3 張正臉時模型會崩臉**。改用背影、側臉，或推進失焦區，或改用 `21 遠景`。
14. **一次只改一個變數再重生**。同時改三處就無法判斷是哪一處起了作用。

    **配套：可重用的區塊逐字複製，不要重打。** 同一組作品共用的 look 區塊（光位與光質、色彩、
    質感／載體、風格總結）在下一張裡應該是**逐字相同的字串**。重打一次就是動了一個你沒記錄的變數，
    之後無法判斷差異來自哪裡 —— 表面上遵守了本條，實際上動了兩處。
    做法：把提示詞當成幾個可替換的區塊，而不是每次重寫的一段散文。要改就只改指定的那一個槽，
    其餘位元不動；改完把新舊兩版並排留著。
15. **否定貼在它守護的那句肯定之後，並指名最接近的錯誤結果。**
    不要把禁止事項收集成**整段提示詞末尾**的一串彙總清單：離開了被守護的那句話，模型無從知道那條禁止在管哪一個屬性。禁止句貼在它所守護的那個子句尾端則是正確作法——`references/07-beyond-the-charts.md` 皮膚組要求把 `no skin smoothing` 寫在**人物描述句的句尾**，指的正是這種貼附，不是段落末尾的彙總。
    寫成「要的樣子 ＋ 緊接著最容易被誤做成的樣子」——
    `shadow edge terminating within a millimetre, not a soft graded falloff`。
    每個技法條目的〈常見錯誤〉欄寫的就是那個最接近的失敗，直接取用，不要自己另編。
    **適用範圍是行為與渲染方式**：光的均勻度、陰影邊緣、對焦面與脫焦起點、運動軸、表面反射行為。
    **色相的排除不適用，物件的排除以正面列舉為原則** —— 色名與物名本身是強 token；
    色相一律走正面列舉（見 `references/02-tone-color.md` 限制調色盤），物件的例外見下。

    **物件的補充出口**：當風險不是「多出一個物件」而是「這個物件被畫成某個現成原型」時，
    往下降一層改成**部位級**的否定，並且**每一條否定都要配一個正面部位**——
    `the crank handle is a plain turned wooden knob, not a moulded plastic D-ring`。
    只禁止而不補上要的那個部位，等於留一個洞讓模型用同一個先驗再填一次。
    整體類別可以另外用一句 is-a / is-not-a 宣告收尾（`a hand-cranked machine, not a typewriter`），
    寫在尺寸之後、表面處理之前；那一句只校正粗粒度的先驗，**不能取代部位級控制**——
    類別名同樣只是一個標籤，只用類別名圈住的物件，幾何仍然照原型長。

    這條講的是提示詞正文的寫法；否定句在不同模型上的擺放與分流照
    `references/07-beyond-the-charts.md` 皮膚組的規則。是否另有 negative 欄位、以及如何表達，
    由 prompt director 依已驗證的 provider/task contract 決定。
16. **提示詞裡的每一句，都要能被「只讀到這一份提交」的畫師執行。**
    生成器手上只有你送出去的那串字、加上隨它一起上傳的素材；你手上的設定表、母版、上一版、
    另一張圖的提示詞，它一個都看不到。指向那些東西的句子沒有約束到任何東西，
    而被它放掉的屬性是**自由的**，不是預設安全的。
    **判準是「有沒有跟這次一起送出」，不是「有沒有出現抽象詞」。** 圖生圖時附上的那張輸入圖、
    以及隨提示詞上傳的參考素材，都是有送出的，指向它們的句子指得到東西
    （圖生圖裡的 `keep the same lighting` 成立）；`consistent with the approved master` 指不到，
    因為那份母版沒有附上。
    寫給自己看的話不能留在會被送出去的字串裡。英文提示詞裡常見的有：`as specified above`、
    `the specified ones`、`other than those listed`、`the rest`、`the others`、`that area`、
    `consistent with`、`the master`、`the other views`、`this prompt`、`the design`、`this version`
    （中文草稿階段對應的是「如上所述／已指定的／除…以外／其餘／其他／該處／與…一致／母版／其他視圖／本提示詞／這個設計／這一版」）。
    **刪掉一個詞不等於刪掉那個運算**：拿掉「除已指定者外」之後，人會自然改寫成「其餘」「其他」「該處」，
    那是同一句話。要檢查的是**有沒有要求讀者回頭把某個屬性的規格從整段裡蒐集起來再相減**，不是有沒有出現某個詞。
    做法：展開成逐個物件的句子，一個物件一句，寫出物件、位置、表面狀態。字數是代價。
    **兩種相鄰寫法仍然合法**：(a) 把完整的正面清單**當場逐字寫在同一句裡**再封口
    （`exactly two people, and no third figure anywhere in frame`）——清單是寫出來的，不是引用來的；
    (b) 逐字重述那個例外，而不是指向它（`the only camera movement is a slow forward push`
    取代 `except the movement named for this shot`）。
    **另一半同樣要記住：描述「這份文件」而不是描述「畫面」的句子，會被畫進畫面。**
    一句寫給作者看的「這幾張圖之間完全一致」曾被執行成一張畫著多格重複人像的圖。
    這一條只管**會被貼進生成器的字串**；工作用的檢查表、說明文件與交付說明照常使用抽象語言。
    **這一條沒有豁免**：完整 image prompt、圖生圖指令（`references/11-image-input.md`）與
    video visual-look subcontract 一律適用，因為三者交出去的都是會被送進生成器的字串。

---

## 參考檔案

| 檔案 | 內容 | 何時打開 |
|---|---|---|
| `references/01-lighting.md` | 光位 8 項、光質 7 項、光源 6 項的完整條目 | 要決定怎麼打光時 |
| `references/02-tone-color.md` | 影調、對比、色彩 9 項 + 色彩關係六種 + 膚色保護 | 要決定整體調性與配色時 |
| `references/03-framing.md` | 景別/景深/動態 9 項、視角/構圖 9 項 + 鏡頭第 10 軸 + 構圖補充 10 項 + 單幀多格版面 + 多人構圖 | 要決定拍多近、用什麼焦段、從哪拍時 |
| `references/04-film-styles.md` | 24 項影視風格的技術配方 | 使用者說了風格詞或想要某種「感覺」時 |
| `references/05-recipes.md` | 組裝公式、三張衝突表、情緒對照表、8 個場景配方、除錯表 | **幾乎每次都該打開** |
| `references/06-analysis.md` | 逆向拆解流程、需求釐清問句庫、預設值安全牌 | 分析照片或需求模糊時 |
| `references/07-beyond-the-charts.md` | 質感與反塑膠感、時間與天氣、環境敘事 | 圖太假、太空洞、要加故事感時 |
| `references/08-motion.md` | video visual-look 的攝影機運動、主體動作與連續性建議 | 提供 video visual-look subcontract 時 |
| `references/09-model-dialects.md` | 各生成模型的提示詞方言與輸出格式 | **步驟 0，每次都該確認** |
| `references/10-zh-lexicon.md` | 中文視覺標籤對照表、族裔與中文字硬規則 | 使用者說了華語圈流行視覺標籤時 |
| `references/11-image-input.md` | 圖生圖三模式、可改性分級、strength 對照 | 使用者給了一張圖要改時 |

每個技法條目的欄位固定為：英文關鍵詞 / 原理 / 情緒 / 提示詞 / 強化 / 衝突 / 常見錯誤。
**不要憑記憶引用條目內容** —— 打開對應的參考檔，直接取用裡面的「提示詞」欄位。
