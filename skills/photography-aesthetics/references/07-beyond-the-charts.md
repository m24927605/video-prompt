# 圖表之外：質感、時間天氣、環境敘事

本檔收的三個維度，**兩張原始圖表（48 項攝影技法 + 24 項影視風格）完全沒有涵蓋，但實務上是高頻必需**。
它們不是第 73、74、75 項技法，而是三個**貫穿所有技法的補充層**：質感層決定畫面「像不像真的」、
時間天氣層決定光「有沒有成因」、環境敘事層決定畫面「有沒有故事」。

為什麼必須補：72 項全部是「怎麼打光、怎麼構圖、怎麼調色」的指令，一旦使用者說的是
「不要太假」「要有電影感」「要有故事感」，agent 手上沒有對應工具，只能繼續往提示詞裡疊光位和風格包
—— 而疊得越多越假。這三個維度是那三句話的正確答案。

引用格式：`圖一 NN 中文標籤` = 48 項攝影技法，`圖二 NN 中文標籤` = 24 項影視風格
（等同 `05-recipes.md` 的 `TNN` / `SNN`）。

> **本檔數值的可信度分級**（寫進提示詞前先看這條）
> - **物理量**（太陽仰角、投影長度、色溫、級數）是**典型值與量級**，會隨緯度、季節、大氣狀況、
>   燈具個體而變動。要當方向指標用，不要當實測值宣稱。投影長度可自行算：`長度 = 主體高度 ÷ tan(太陽仰角)`。
> - **模型行為描述**（哪個模型吃 negative prompt、哪個詞會觸發什麼語料）**會隨版本改變**，
>   以 `09-model-dialects.md` 為準；本檔只給「怎麼判斷」的規則，不宣稱某版本的固定行為。
> - **英文片語**是可直接抄的，但抄完要照 `05-recipes.md` 表 A／表 B 查一次衝突。

---

## 零、這三個維度插進組裝順序的哪裡

本檔三個維度**不新增槽位**，而是掛進 SKILL.md〈標準工作流程 A-5〉的組裝順序裡
（`05-recipes.md` 第一節是同一條順序的逐槽展開版）：

| 本檔維度 | 掛在哪一槽 | 寫在該槽的什麼位置 | 佔不佔 8 項名額 |
|---|---|---|---|
| 環境敘事（3 個物件） | 主體槽 | 主體與動作寫完之後緊接著寫，每個物件都要給畫面位置 | 不佔（它是主體的延伸，不是軸） |
| 皮膚組 | 主體槽 | 人物描述的句尾 | 不佔，但上限 4 個片語 |
| 材質組 | 主體槽（主體身上的材質）／各環境物件之後（場景表面） | 貼在該物件後面 | 不佔，但上限 3 個表面 |
| 天氣 | **新增於「視角/朝向」與「光位」之間** | 獨立一句，寫在打光之前 | **佔 1 個主動視覺控制名額**（沒有圖表編號，但計入上限 8） |
| 時段 | 光源與色溫槽 | 取代或合併原本的光源描述 | 不另佔（它就是這一軸的值） |
| 成像瑕疵組 | 質感/載體槽 | 與載體（圖二 11/12/14/17/18/20）寫在一起 | 不佔，但上限 3 個片語 |

**擴充後的完整順序**

```
主體（＋3 個環境物件＋皮膚組＋材質組） → 景別 → 鏡頭焦距 → 視角/朝向 → 天氣
   → 光位 → 光質 → 時段與光源色溫 → 影調與對比 → 色彩 → 景深
   → 成像瑕疵與載體 → 風格總結 → 畫幅
```

天氣必須寫在光位**之前**：天氣是光的成因，先給成因再給結果，模型才會把兩者連起來；
反過來寫，模型會先建立一套打光，再把天氣當成貼上去的濾鏡。

---

## 一、質感與反塑膠感

AI 生成影像最一眼假的地方不在光位，也不在構圖，而在**表面渲染**：塑膠皮膚、無瑕高光、
全新無磨損的材質、完美的焦點衰減。這一節的三組詞庫是直接對症的處方。

三組的分工：**皮膚組**處理人（最優先，因為觀眾對臉的異常最敏感）、
**材質組**處理物（讓場景有重量）、**成像瑕疵組**處理成像本身（讓畫面像「被拍下來的」而不是「被算出來的」）。

### 1-1 皮膚組

| 英文片語 | 何時用 |
|---|---|
| `visible skin texture` | 任何有人的畫面都先寫這一句，它是整組的錨；只寫這一句就能救回一半的塑膠感。 |
| `pores open across the nose and inner cheeks, finer toward the jaw` | 景別在 `圖一 19 近景` 以上（含 `圖一 32 特寫`、`圖一 31 極端特寫`）時必寫；毛孔在 T 區大、往臉緣變小，這個不均勻分佈本身就是真實訊號。 |
| `fine vellus hair catching the light along the jawline and upper cheek` | 有 `圖一 04 側逆光`、`圖一 05 背光`、`圖一 10 髮絲光` 時用；汗毛只有被逆光或掠射光打亮才看得見，順光下寫了也不會出現。 |
| `slight redness around nose and ears` | 所有人像的預設值。膚色完全均勻＝塑膠；鼻翼與耳廓因為表淺微血管密集本來就偏紅。 |
| `uneven specular highlights broken up by pores and stubble` | 用了 `圖一 09 柔光` 時必寫 —— 大面積柔光天生產生一片乾淨的橢圓高光，那正是最假的特徵。若同時用了 `圖一 44 亮調`（大量補光把紋理陰影抬掉）更要寫。 |
| `no skin smoothing` | 目標模型**有** negative prompt 欄位或參數時（例如 Midjourney 的 `--no`、Stable Diffusion 系介面的 negative 欄），放進去；**沒有**這個欄位的指令遵循型模型（GPT Image 2、Nano Banana 這一類），寫在正文**句尾**，不要夾在中段。哪些模型支援 negative prompt 會隨版本改變，寫之前以 `09-model-dialects.md` 為準。 |
| `no beauty retouching` | 同上。另外照 `02-tone-color.md` 的通則：句中否定在部分模型上不可靠，穩健做法是改寫成正面陳述 —— `unretouched skin with pores and fine lines left in`。 |
| `fine lines at the outer corner of the eye deepening where she squints` | 主體年齡設定在 30 歲以上、或表情有出力（笑、瞇眼、皺眉）時用；沒寫年齡與表情細節時，模型傾向給一張年輕、鬆弛、無表情的臉。 |
| `a faint stubble shadow along the jaw with individual hairs visible at the edge` | 男性主體必寫。乾淨到沒有任何鬍根陰影的下顎是 AI 臉最典型的破綻之一。 |
| `chapped texture on the lower lip with the skin lifting at one corner` | 需要疲憊、寒冷、缺水、長時間戶外的情境時用；嘴唇是模型最容易渲染成塑膠的部位。 |
| `sweat sheen limited to the temple and the bridge of the nose` | 有勞動、悶熱、緊張時用。關鍵在 `limited to` —— 全臉均勻的油光會變成美妝廣告的打亮。 |
| `uneven pigmentation, freckles across one cheekbone and a darker patch at the temple` | 需要「這是一個特定的人」而不是「一張泛用的臉」時用；不對稱的色素分佈是身分感的來源。 |
| `the neck, ears and hands rendered at the same age as the face` | 有露出手或脖子的畫面必寫。模型常給出年輕的臉配光滑無紋的手，這個年齡矛盾觀眾一眼就察覺得到，卻說不出哪裡怪。 |

**使用量**：一次寫 3–4 句就夠，13 句全寫會讓模型把畫面推向皮膚科特寫。
固定組合：`visible skin texture` + `slight redness around nose and ears` + 一句依景別選的細節。

**關於否定句**：`no skin smoothing` 與 `no beauty retouching` 是全檔僅有的兩個「禁止某道後製工序」的否定句，
必須照上表的分流規則處理。其餘片語裡的 `no` / `without`（`no specular at all`、`no cast shadows anywhere`、
`true black sky with no gradient`）都是在**描述場景中不存在的東西**，屬於正面描述，可以正常寫在句中。

### 1-2 材質組

| 英文片語 | 何時用 |
|---|---|
| `linen weave visible at the shoulder seam where the light rakes across it` | 布料主體（衣服、床單、窗簾）；必須配掠射角側光（`圖一 03 側光`，`raking at 80 degrees`）才顯現，正面光下織紋幾乎不見。 |
| `brushed metal, the specular stretched into a band running across the brush lines rather than a round hotspot` | 金屬產品、機械、工具。拉絲金屬的異向性高光是**橫跨紋理方向拉長的一條**（同一個原理讓髮束的高光帶橫跨髮流、黑膠唱片的高光呈放射狀），不是一個圓點；不寫這句模型會給你鏡面塑膠。 |
| `condensation beading on the glass with two drops already running` | 冷飲、酒杯、冰箱、雨後車窗。`already running` 是關鍵：靜止的水珠是圖庫感，正在流的水珠代表時間正在走。 |
| `dust motes in air drifting through the shaft` | 用了 `圖一 18 丁達爾光` 或 `圖二 05 煙霧體積光` 時必寫。光束需要介質才成形，塵是最自然的那一種。 |
| `worn leather patina darkest where the thumb rests` | 皮件、沙發、書封、車廂。磨損必須有**受力點**，寫清楚哪裡最深，模型才不會給你均勻的做舊貼圖。 |
| `wet asphalt reflections stretching every light into a vertical smear` | 所有夜景街道。這一句同時給你反射、景深分離與下半畫面的第二光源，是全檔 CP 值最高的材質片語。 |
| `chipped matte paint on the door frame exposing bare metal at the corner` | 需要「這裡有人長期進出」的室內外門窗；磨損出現在角落與轉角，不會出現在平面中央。 |
| `unglazed ceramic absorbing light with no specular at all` | 需要對照組時用 —— 畫面裡放一個完全沒有鏡面反射的表面，其他材質的光澤才有比較基準。 |
| `fingerprints on the glass visible only against the bright background` | 玻璃、螢幕、展示櫃。指紋只在逆光或亮背景下才看得見，`only against` 讓模型不會把整片玻璃畫髒。 |
| `fabric pilling on the cuff of a washed-out sweatshirt` | 居家、貧困、長期使用的衣物；起毛球是「洗過很多次」的視覺證據，比 `old clothes` 精確得多。 |
| `raised wood grain on a table sanded down by use, end grain darker where liquid soaked in` | 餐桌、工作檯、櫃檯。木頭的年份寫在紋理凸起與吸液變深這兩件事上。 |
| `scuffed rubber sole with grit pressed into the tread` | 有腳進畫面的全身照（`圖一 23 全身照`）；鞋底是模型最少處理、也最容易露餡的地方。 |
| `flaking plaster with a damp shadow spreading up from the skirting` | 老屋、廢墟、潮濕氣候的室內；壁癌／上升性壁面潮氣的方向是**由下往上**，寫錯方向會立刻不成立。 |

**使用量**：上限 3 個表面。每個表面一句，並確認該表面在你選的光位下真的看得見
（材質與光位的對應見 `05-recipes.md` 除錯表「產品看不出材質」那一列：金屬／拉絲要側光＋硬光、
玻璃／液體要側逆光＋亮背景、布料／皮革要側光＋掠射角）。

### 1-3 成像瑕疵組

| 英文片語 | 何時用 |
|---|---|
| `subtle film grain` | 幾乎所有需要真實感的畫面。`subtle` 不可省 —— 只寫 `film grain` 通常會拿到明顯偏粗的顆粒，因為語料裡的「顆粒」樣本多半是高感光度推格的極端例子。 |
| `slight halation on highlights, strongest around the window` | **底片載體**（`圖二 18 十六毫米顆粒`）且畫面裡有高光源（窗、燈、太陽）時用。halation 的成因是光穿過乳劑後在片基背面反射回來再次曝光，是底片特有現象（見 `04-film-styles.md` S18：「來自紅感層與片基背面的反射」）。**數位載體不要寫 halation**，要暈開就寫 `veiling flare` 或 `bloom around the source`，那才是數位上真的會發生的機制。`圖二 01 德國表現主義`、`圖二 13 港片霓虹`、`圖二 24 宇宙恐怖` 的條目已自帶 halation，不必重複寫。 |
| `mild lateral chromatic aberration at the frame edges` | 廣角（等效 35mm 以下）時用。橫向色差是**離軸像差**，中央為零、越往畫面邊緣越明顯，寫在中央會不成立。 |
| `a touch of purple fringing on the out-of-focus highlight edges` | 大光圈（f 值 2 或更小，例如 f/1.4、f/2）時用。這是**縱向**色差，跟上一條是不同的東西：它出現在焦平面前後的高反差邊緣，**畫面中央一樣會有**，不限邊緣。兩條不要混寫成一句。 |
| `imperfect focus falloff, the plane landing a centimetre behind the near eye` | 用了 `圖一 25 淺景深` 時必寫。AI 的散景常常是一個乾淨的切面，真實鏡頭是漸進的、而且合焦點常常沒對準。 |
| `corner vignetting about half a stop down` | 需要「用真實鏡頭拍的」感覺時；給級數，不要只寫 `vignette`（會拿到後製的黑框）。 |
| `shadow noise left in place rather than cleaned up` | 用了 `圖一 42 暗色調`、`圖一 37 弱光`、`圖二 06 單光源夜戲` 時用。乾淨到沒有雜訊的暗部是不可能的曝光。數位場景寫 `high-ISO digital noise`，底片場景才寫 `grain`。 |
| `one blown highlight left uncorrected on the forehead` | 需要現場感、抓拍感時用（街拍紀實，以及 `圖二 19 偽紀錄片`、`圖二 10 手持跟拍` 在靜圖上的等效替代，見 `08-motion.md`）。完美的曝光本身就是一種假。 |
| `slight motion blur on the near hand while the face stays sharp` | 主體有動作時用。局部動態模糊代表快門有長度，也代表這一刻是被「抓到」的，不是擺出來的。要更明確就給快門值：`1/15 second`。 |
| `veiling flare washing across the lower left corner, thrown by a source just outside the top right of frame` | 有強光源接近畫面邊緣時（`圖一 05 背光`、`圖一 40 強光`）。要指定光源在哪、霧化落在哪一角，且兩者通常在畫面的對角；不要寫成全畫面 flare。 |
| `a stray hair and two dust specks in the gate` | 需要底片實體感時（搭 `圖二 18 十六毫米顆粒`）。數位載體不要用這句；`圖二 12 柯達克羅姆` 也不要用「negative」這個字 —— 它是**正片（反轉片）**，那邊的髒污要寫 `a little scan dust and one hairline scratch`。 |
| `slight barrel distortion bending the door frame at the edge of frame` | 廣角室內。直線在邊緣微彎是多數非高階廣角鏡的常態（高階鏡已做光學校正，這是刻意選的「便宜鏡頭感」），全部筆直是渲染感的來源之一。 |

**使用量**：上限 3 個片語。超過會讓模型把畫面理解成「一張損壞的舊照片」，反而失去可信度。

**與載體風格包的排他規則**——載體風格包各自的顆粒行為完全不同，不要一律套「加了會疊兩倍粗」。
寫之前先翻 `04-film-styles.md` 該項的〈色彩與質感〉欄，四種情況分開處理：

1. **本身就是粗顆粒的**：`圖二 18 十六毫米顆粒`（條目明寫 dense visible grain）。
   風格包已經指定顆粒，不要再寫 `subtle film grain`，會疊粗。
2. **本身是「反顆粒」的**：`圖二 12 柯達克羅姆`（辨識特徵正是幾乎無顆粒 + 極濃的黑）、
   `圖二 11 三色印片`（染料轉印影像沒有銀鹽顆粒結構，顆粒極細）。加顆粒等於換成另一種底片，直接破壞風格包。
   這兩個要瑕疵的話用它們自己的：S12 是 `a little scan dust and one hairline scratch`，
   S11 是 `faint colour fringing from imperfect registration on high-contrast edges`。
3. **本身是數位／磁帶雜訊，不是底片顆粒的**：`圖二 14 數位早期`（DV 的梳狀交錯與 DCT 塊狀）、
   `圖二 17 VHS 錄影帶`（色度滲流、dropout、畫面底部的 head-switching 雜訊帶），
   以及雖不在載體槽但同樣鎖死質感的 `圖二 06 單光源夜戲`（條目明寫 `high-ISO digital noise rather than film grain`）。
   這三個要寫 `high-ISO digital noise` / `tape dropout and a head-switching band across the bottom of frame`，
   **寫 `film grain` 是類別錯誤**，會讓模型混出一種不存在的載體。
4. **根本不談顆粒的**：`圖二 20 定格動畫質感`，它的載體特徵是手工材質、逐格輪廓微抖（boil）與極輕微的曝光閃爍。
   要加瑕疵就加 `outline boil between frames, slight exposure flicker`，
   並且**不要**加 `slight motion blur on the near hand`（表 B：T24 動態模糊 ↔ S20，定格動畫天生沒有動態模糊）。

以上四種情況下，成像瑕疵組都只保留風格包沒有指定的項目（色差、焦點衰減、暗角）。

### 1-4 禁詞清單

| 禁詞 | 模型會做什麼 | 改寫成 |
|---|---|---|
| `flawless skin` / `smooth skin` | 抽樣落到廣告修圖語料，一次抹掉毛孔、汗毛與次表面散射，膚色變成單一色塊 | `visible skin texture` + `pores open across the nose and inner cheeks` |
| `porcelain skin` | 陶瓷的物理特性就是無孔、均勻、硬鏡面高光 —— 模型會照字面做 | `pale skin with visible capillaries at the nostril crease and slight redness around nose and ears` |
| `airbrushed` | 直接指涉噴槍修圖工序，連帶抹平衣服皺褶與背景 | `unretouched skin, texture as photographed` |
| `perfect symmetry` / `symmetrical face` | 落到建築渲染與向量語料，臉變成鏡射複製，左右眼一模一樣 | `slight asymmetry, one eyebrow sitting higher and the hair parting off centre`（真要對稱**構圖**請用 `圖二 07 單點透視對稱`，那是空間對稱，不是臉對稱） |
| `glossy` | 把畫面上所有材質統一成同一種塑膠鏡面反射 | 指定該材質實際的反射行為：`semi-gloss enamel with a broad soft specular` / `brushed metal, the specular stretched across the brush lines` |
| `pristine` / `spotless` / `brand new` | 移除所有磨損痕跡，畫面變成商品目錄 | `worn leather patina darkest where the thumb rests` / `chipped matte paint exposing bare metal at the corner` |
| `dewy` / `radiant glow` | 全臉均勻的強高光，等於美妝廣告的打亮 | `sweat sheen limited to the temple and the bridge of the nose` |
| `perfect lighting` | 模型解讀成「所有地方都被照亮」，得到無方向的均勻補光 | 給光比與陰影落點：`4:1 key-to-fill ratio, the far cheek two stops under`（比值與級數要對得上：4:1 = 2 級，8:1 = 3 級，16:1 = 4 級） |
| `sharp throughout` / `everything in focus` | 消除焦點衰減，畫面像 3D 渲染的全景深 | 給光圈、焦段與合焦點：`f/2 on an 85mm lens focused on the near eye`（同樣是 f/2，50mm 在人像距離的景深約 10cm，耳朵還是清楚的；要「耳朵已經脫焦」得用 85mm 以上，見 `03-framing.md` T25） |
| `photorealistic` / `hyperrealistic` | **實務上反效果最強的一組**：這兩個詞在網路影像的自我標註裡大量來自 3D 渲染與 CG 作品，寫下去傾向把畫面推離攝影 | 刪掉，改成具體相機參數 + 載體：`f/2.8, 50mm, 1/125 second` + `subtle film grain` |

另外，SKILL.md 硬規則 1 的七個無效堆砌詞（`beautiful`、`masterpiece`、`8k`、`high quality`、
`award winning`、`ultra detailed`、`trending on artstation`）同樣禁用，理由相同。

**為什麼這些詞會讓圖變假 —— 兩個機制**

1. **語料共現**：這些詞在網路影像的標題與 alt text 裡，高度集中在修圖過的商業影像、美妝廣告與 3D 渲染。
   寫下去等於把抽樣範圍推向那個分布，跟你想要的紀實質感是兩個不同的資料池。
   （這是從實測結果反推的機制假說，不是對任一模型訓練資料的斷言；判準是**實測**：換掉這個詞，圖有沒有變。）
2. **它們是品質形容詞，不是物理描述**：`flawless`、`perfect`、`beautiful` 沒有告訴模型任何可執行的資訊，
   模型只能用自己的先驗去填補 —— 而先驗就是「平均臉、平均反射、平均構圖」。
   **人類感知為「假」的東西，本質上就是「平均」。** 真實感不是加分項的總和，是缺陷的具體性。

### 1-5 處方規則：使用者說「太假／太 AI／不夠真」時

**固定程序，一次只加一組，加完就重生，不要動光位。**

| 步驟 | 動作 | 加在哪一槽 | 停止條件 |
|---|---|---|---|
| 0 | 保留原提示詞不動。不重寫、不換風格包、不改光位、不改景別 | — | — |
| 1 | 加皮膚組 3–4 個片語 | 主體槽的人物描述句尾 | 可接受就停 |
| 2 | 仍假 → 加成像瑕疵組 2–3 個片語 | 質感/載體槽 | 可接受就停 |
| 3 | 仍假 → 加材質組，畫面主要表面各 1 句（上限 3 個表面） | 各物件描述之後 | 可接受就停 |
| 4 | 三組加完仍假 → **這時才回頭看光位**，而且只做一件事：把並列的多個光位技法收斂成單一有動機的光源（`圖一 08 窗光` / `圖一 11 自發光` / `圖二 06 單光源夜戲`） | 光位槽 | — |
| 5 | 仍假 → 問題在構圖，照 1-6 第 1 與第 6 項處理 | 景別與視角/朝向槽 | — |

每一步只重生一次，並保留上一版做對照。三組全部一次加下去也可能成功，但你會不知道是哪一組起作用，下次無法重複
（這是 SKILL.md 硬規則 14「一次只改一個變數」的具體展開）。

**為什麼不該動光位**

1. **光位是幾何層**。改光位＝改陰影落點＝改整張圖的明暗分佈與構圖重心，模型會重新抽出一張構圖、姿勢、
   表情都不同的圖。使用者原本已經滿意的部分會一起消失，於是變成從頭再來。
2. **「假」的成因絕大多數不在光位，在表面渲染層**。一張光位完全正確的圖，只要皮膚是塑膠、材質全新、
   高光無瑕，照樣一眼假；反過來，光位普通但表面正確的圖可以很可信。改光位是治錯了病。
   （唯一的例外是「多個無來源的 key light」，那由步驟 4 處理，也正是 `05-recipes.md` 除錯表
   「看起來很假、很 AI」那一列列出的第一個成因。）
3. **一次改兩層就無法歸因**。這是可重複性的問題：你需要知道下一個案子該從哪一組開始。
4. **權重位置決定了增量的可控性**。光位在打光層（靠前、權重高），表面層在主體槽句尾與質感/載體槽（靠後、權重低）。
   只動低權重層，變更才是**疊加**；動高權重層，變更是**重抽**。

### 1-6 AI 生圖一眼假的六個特徵與對策

| # | 特徵 | 為什麼會發生 | 對策（直接加這句） | 同時拿掉 |
|---|---|---|---|---|
| 1 | **過度對稱** —— 臉左右鏡射、物件均勻排列、地平線正中 | 模型的先驗是各類樣本的平均，平均臉必然對稱 | `slight asymmetry, one eyebrow sitting higher, the hair parting falling to her left, the subject placed on the right third with dead space at the left` | `圖一 35 居中構圖`（除非刻意做 `圖二 07 單點透視對稱` 或 `圖二 08 平面正面構圖`） |
| 2 | **無瑕高光** —— 每個高光都是乾淨的橢圓，邊緣平滑無破碎 | 大面積柔光 + 平滑法線的預設結果 | `uneven specular highlights broken up by pores and stubble, one blown highlight left uncorrected on the forehead` | `圖一 09 柔光` + `圖一 44 亮調` + `圖一 43 低對比度` 的三連組合（這組天生消除紋理，見 `05-recipes.md` 除錯表「皮膚像塑膠、像磨皮過頭」那一列） |
| 3 | **所有東西都合焦，或散景是一個切面** | 模型沒有真實的光學模型，景深被當成兩層 mask 處理 | `f/2 on an 85mm lens focused on the near eye, imperfect focus falloff with the ear already softening and the background dissolving progressively with distance rather than at one plane` | `sharp throughout`、`everything in focus`、沒有光圈值的 `bokeh` |
| 4 | **光源方向不一致** —— 每個物件有自己的影子方向，或人物有影子而地面沒有 | 提示詞裡並列了兩個以上光位技法，模型各自滿足 | 收斂成單一動機光源，並明寫：`every shadow in frame running to camera right at the same angle, contact shadow pooling where the shoe meets the floor` | 並列的 `圖一 03 側光`／`圖一 05 背光`／`圖一 07 頂光`／`圖一 27 正面光`；多餘的改寫成 `rim` / `kick` / `bounce` 並註明比 key 暗幾級 |
| 5 | **材質沒有磨損** —— 全新的門把、全新的鞋、全新的桌面 | 訓練語料裡的商品圖佔比極高 | 材質組，並把磨損放在受力點：`wear concentrated where hands and feet actually touch, the door handle, the chair arm, the third stair` | `pristine`、`brand new`、`clean` |
| 6 | **構圖過於置中平衡** —— 主體正中、留白對稱、沒有任何東西被切到 | 模型傾向把主體推向畫面中心以最大化「可辨識度」 | 給出偏移量與裁切證據：`subject on the right third, horizon on the lower third, a passer-by cut in half at the near edge, the frame tilted about two degrees` | `圖一 35 居中構圖`、`圖一 34 封閉構圖`（若不是刻意要框住主體）、`well composed` |

第 1 與第 6 項屬於構圖層，對策要寫在景別與視角/朝向槽；第 2、3、5 項是表面層，寫在主體槽與質感/載體槽；
第 4 項是光位層，是唯一該動打光的情況。

---

## 二、時間與天氣

**加一個時段或一個天氣，比再加一個風格包有效得多。** 原因是時段與天氣改變的是**光的物理條件**，
它會連帶把對比、色溫、空氣透視、反射、景深分離一次全部改掉，而且這幾個軸自動彼此一致
—— 因為它們有共同的物理成因。風格包只是把這些軸的值直接指定，模型還得自己編一個成立的場景去承載。

72 項裡只有 `圖二 04 魔幻時刻` 間接沾到時間，其餘全部缺席。這一節補上。

**寫 K 值的前提**：照 `01-lighting.md`〈36 冷光源〉的通則，光禿禿的 `7500K` 對模型只是裝飾字。
每個 K 值都要**配一個顏色形容詞**（`10000K blue-white sky`），需要色偏成立時再**補上拍攝白平衡當參照**
（`shot on 5600K daylight white balance`）。下面的片語已經照這個規則寫好。

### 2-1 時段表

一個畫面只能有一個時段。時段吃「光源與色溫」那一軸，不另外佔技法名額。
仰角與色溫是典型值；窗口長度隨緯度與季節劇烈變動（低緯度整年約 20–30 分鐘，高緯度夏季可長達數小時），
所以**要給模型的是仰角與陰影特徵，不要給分鐘數**。

| 時段 | 太陽仰角 | 直射光色溫 | 環境光／補光色溫 | 陰影特徵 |
|---|---|---|---|---|
| pre-dawn 曙前 | −12° 至 −6°（日出前） | 無直射光 | 天空 11000K 以上的冷藍紫，東方低空一條漸亮的洋紅帶 | **完全沒有投影**，只有物體自身的上下明暗；地面比天空暗約 2 級 |
| blue hour 藍調時刻 | −4° 至 −8°（日落後） | 無直射光 | 天空 9000–12000K 的深藍 | 無日光投影；唯一的投影來自畫面內的人造燈，且很短很淡 |
| golden hour 黃金時刻 | 0° 至 +6° | 2000–3200K 的橘金 | 開放天空約 10000K 的藍 | 投影長度 = 高度 ÷ tan(仰角)：仰角 6° 約 9.5 倍、5° 約 11 倍、3° 約 19 倍，再低就長到被地形與遮蔽切斷；邊緣半柔但方向明確 |
| harsh midday 正午硬陽 | +60° 以上（低緯度可近 +90°，緯度越高正午仰角越低） | 5000–5600K 的中性白 | 天空補光約 9000K 的藍，比直射光低約 2.5 級 | 投影短且落在主體正下方（仰角 60° 約為身高的 0.6 倍、70° 約 1/3、80° 約 1/5），邊緣如刀切；眼窩與下巴下緣暗約 2.5 級 |
| overcast noon 陰天正午 | 被雲層遮蔽 | 無方向性直射光 | 全天空 6500–7500K 的藍灰 | **沒有方向性投影**，只剩物件與地面接觸處的接觸陰影；臉部光比約 2:1 |
| dusk 暮色 | 0° 至 −4°（日落後） | 地平線殘光約 3000K 的琥珀 | 天空 7000–9000K，人造燈 2700K 陸續亮起 | 無日光投影；天空仍比街面亮約 2 級，天然形成冷暖分區 |
| deep night 深夜 | 天光消失 | 月光 4100K（實測值，中性偏暖，**不是藍的**；藍月是敘事與調色慣例，見 `01-lighting.md` 36 冷光源） | 高壓鈉路燈約 2000K（低壓鈉燈近乎單色橘黃，沒有可用的色溫值）／白光 LED 4000–6500K | 投影全部來自畫面內的燈，照度隨距離平方衰減；天空指定為無漸層的純黑 |

> **曙前與藍調時刻的仰角會重疊**，區分靠的是日出前／日落後：曙前的東方低空有一條**正在變亮**的洋紅帶、
> 人造燈多半還沒被關掉但街上空無一人；藍調時刻沒有那條帶，且每一扇窗與每一盞街燈都已經全亮。

### 2-2 每個時段可直接用的英文片語

貼進「光源與色溫」槽，取代原本的光源描述。

- **pre-dawn**：`pre-dawn twilight, sun 8 degrees below the horizon, cold blue-violet sky-only illumination near 11000K with a magenta band low in the east, no cast shadows anywhere, the ground two stops under the sky`
  何時用：需要不安、失眠、事情剛發生或即將發生的時刻。它是唯一「有光但沒有方向」的時段，最適合 `圖二 24 宇宙恐怖`、`圖二 03 北歐冷冽`。
- **blue hour**：`blue hour, sun 5 degrees below the horizon, deep blue 10000K sky as the only ambient with amber 2700K practicals now equal to it in brightness, no sun shadows, every window and streetlight reading as a light source`
  何時用：需要城市夜景但又不想失去天空層次時。這是唯一「天空亮度與人造燈亮度打平」的窗口，`圖二 13 港片霓虹`、`圖二 21 賽博龐克街景` 的最佳時段。
- **golden hour**：`golden hour, sun 5 degrees above the horizon, orange-gold 2800K direct sun against blue 10000K open-sky fill, shadows running about eleven times the subject's height across the ground, half-soft shadow edges`
  何時用：溫暖、懷舊、告別。它就是 `圖二 04 魔幻時刻` 的光學條件（該風格包定義為太陽仰角 0°–6°、位在主體正後或後側 150°–170°）—— **若已選該風格包就不要重複寫時段**，直接用 `04-film-styles.md` S04 的提示詞。
- **harsh midday**：`harsh midday sun, neutral white 5600K, short hard shadows directly under the subject, knife-edged shadow borders, the eye sockets and the underside of the chin two and a half stops down`
  何時用：無處可躲、暴露、酷熱、審訊感。它是最被低估的時段 —— 大多數人避開正午，所以正午本身就是一種辨識度。搭 `圖一 47 硬光`、`圖一 46 高對比`。
- **overcast noon**：`overcast noon, a bright even 6500K blue-grey sky acting as one source the size of the sky, no directional shadow beyond a soft contact shadow under each object, about two to one across the face`
  何時用：紀實、日常、需要看清楚所有細節、不要戲劇性。等同免費的 `圖一 09 柔光`，是 `圖二 23 生活寫實` 的預設條件。
- **dusk**：`dusk with the sun three degrees below the horizon, a warm amber 3000K residual band along the skyline under an 8000K blue sky, sodium and window practicals switching on, the sky still two stops brighter than the street`
  何時用：轉折、曖昧、一天結束但夜還沒開始。它自帶冷暖分離，是 `圖一 41 雙性照明` 的自然版；但仍要照 `05-recipes.md`〈T41 例外條款〉補齊三件事：哪一側是哪個色溫、兩色的交界在畫面哪裡、兩側差幾級。少了這三句，冷暖會被模型混成一團髒色。
- **deep night**：`deep night with no sky light left, 4100K moonlight as the only ambient sitting a stop and a half under the practicals, all modelling coming from those practicals falling off by the inverse square, true black sky with no gradient`
  何時用：孤獨、危險、私密。關鍵是 `true black sky with no gradient` —— 少了這句，模型會把夜晚畫成「調成藍色的白天」（見 `05-recipes.md` 除錯表「夜景像白天調成藍色」那一列）。

### 2-3 天氣詞庫

天氣佔 1 個主動視覺控制名額，寫在光位之前。它沒有圖表編號，不計入輸出的「技法清單 N 項」，但計入全篇上限 8；請另列在「補充維度」。每一項都「免費附贈」數個軸的效果，這是它 CP 值高的原因。

| 天氣 | 英文片語 | 免費附贈什麼 | 代價／前提 |
|---|---|---|---|
| 雨（下雨中） | `steady rain with the street already soaked, every practical doubled as a vertical smear in the wet asphalt, rain streaks visible only where they cross a backlight` | 濕地面把每盞燈變成第二光源（免費的 `圖一 11 自發光` 倍增）、下半畫面的反射結構、免費的景深分離、`圖一 24 動態模糊` 的天然理由 | **雨必須逆光或側逆光才看得見**：雨絲靠散射光被看見，且要有暗背景襯托。順光下的雨等於不存在，一定要配 `圖一 05 背光` 或 `圖一 04 側逆光` |
| 霧 | `fog thickening with distance so contrast drops and blacks lift progressively, the near figure at full contrast, the building fifty metres back reduced to a flat grey silhouette` | 空氣透視＝免費的層次分離（不必開大光圈，`圖一 22 深景深` 也能有縱深）、光束的介質、免費的背景簡化 | 對比隨距離下降，主體必須留在最近的一層，否則整張變灰。**要光束就只能用薄霧**（`thin haze`）不能用濃霧 —— `圖一 18 丁達爾光` 與 `圖二 05 煙霧體積光` 靠的是「亮束 vs 暗周圍」的高反差，濃霧會把這個反差一起壓掉（`05-recipes.md` 表 B：T43 低對比度 ↔ T18／S05） |
| 落雪 | `falling snow in three distinct depth layers, near flakes crossing the lens out of focus as soft discs, mid flakes sharp, far flakes reduced to texture, snow-covered ground bouncing fill up under the chin` | 免費的前中後三層縱深、逆光下免費的散景、雪地當巨型反光板從下方補光 | 地面補光會殺掉 `圖一 42 暗色調`。要低調就讓雪落在濕黑柏油上而不是積雪地面。夜間或藍調時刻用時，逆光要指定給街燈或車燈，否則雪片沒有東西可反射 |
| 熱浪 | `heat haze shimmering off the road, the far half of the frame wobbling and losing edge definition while the near subject stays sharp, shot at 300mm` | 免費的距離感與溫度感 —— 不必靠橘色調色告訴觀眾很熱 | 必須長焦（等效 200mm 以上）＋足夠距離：熱浪是空氣密度不均造成的折射抖動，要有夠長的空氣路徑被壓縮進畫面才看得到。廣角寫了也不會出現 |
| 風沙 | `dust blowing across the frame, particles catching the low sun as a bright edge, the whole palette collapsed toward a single ochre-grey hue, distant objects losing colour before they lose shape` | 免費的體積光、免費的 `圖一 45 低飽和`（懸浮塵是物理去彩劑，把整個調色盤壓向單一色相的低彩，注意這是低飽和不是黑白）、免費的邊緣分離 | 等於做掉半個 `圖二 15 沙塵單色`，兩者同用會過頭，擇一。既然它會壓飽和，照 SKILL.md 硬規則 9 補一句 `skin kept at natural saturation`，否則人會變灰屍 |
| 濕熱空氣 | `humid air with a visible bloom around every light source, a sheen of sweat at the temple and along the upper lip, blacks lifted slightly by the moisture in the air` | 免費的高光暈開、皮膚油光與汗、輕微抬起的黑位；讓觀眾**感覺到溫度**最便宜的手段 | 會抬黑位，與 `圖一 46 高對比` 相衝，要高對比就別用。這裡的暈開機制是空氣中水氣造成的散射（`bloom`／`veiling flare`），不是底片的 halation，數位場景也成立 |
| 陰天漫射 | `unbroken overcast acting as a single source the size of the sky, shadow edges several centimetres wide, colours reading at full local saturation with no white glare on any surface` | 免費的 `圖一 09 柔光`（不需任何燈具）、免費的飽和度（沒有鏡面白光稀釋固有色）、免費的「全天都能拍」 | 沒有方向性＝沒有立體感。必須另外製造分離：`圖一 34 封閉構圖`（用門框窗框把主體框起來，前景暗部吃掉外緣 20–40%）或深色前景 |
| 雨後 | `twenty minutes after the rain stopped, standing water in the road holding an inverted image of the storefront signage, broken cloud letting one hard shaft through onto the far pavement` | **全檔 CP 值最高的一項**：拿到雨的全部反射，卻不必處理「雨要逆光才看得見」的限制；破碎雲層＝免費的方向性硬光＋快速變化的天空；水窪＝免費的前景元素與低機位鏡面（配 `圖一 39 低角度視角`） | 無 |

### 2-4 處方規則：使用者說「要有電影感」

**先加一個時段 + 一個天氣，重生看結果，再考慮要不要動風格包。**

| 步驟 | 動作 |
|---|---|
| 1 | 檢查需求裡是否已經隱含時段或天氣（「下雨的街」「夜市」＝已有），有就直接用，不要覆寫 |
| 2 | 沒有就照 2-5 的情緒對照表各選一項，時段寫進光源與色溫槽、天氣寫在光位之前 |
| 3 | 重生。多數情況到這裡就結束了 |
| 4 | 仍不足 → 這時才加風格包，且**只加一個**，並照 `05-recipes.md` 表 B 檢查它會不會覆寫掉你剛加的時段（例如 `圖二 04 魔幻時刻` 鎖死太陽仰角 0°–6°、`圖二 06 單光源夜戲` 鎖死深夜且鎖死「唯一主光是入鏡的實體燈」） |
| 5 | 仍不足 → 問題不在氛圍，在畫幅與鏡頭。補 `2.39:1` 與焦段，那是最便宜的電影感來源（SKILL.md 硬規則 8） |

**為什麼這比堆風格有效**

1. **一次動四個軸且自動一致**。加一個天氣就同時改了光質、對比、色彩、景深分離；而且因為它們來自同一個物理成因，模型不會產生矛盾。手動疊四項技法則要自己保證彼此不打架。
2. **「電影感」的感知來源是「這道光有一個具體、可解釋的成因」**。時段與天氣就是成因。堆風格只是堆結果，觀眾看得出光沒有來處。這也是 `05-recipes.md` 情緒表把「要有電影感」定義成「單一有動機的光源 + 大量放棄的暗部 + 非 1:1 畫幅」的原因。
3. **風格包彼此會打架，時段與天氣不會**。天氣是場景條件，可以疊在多數風格包之上；兩個風格包疊起來通常互相抵銷（見 `05-recipes.md` 表 B）。
4. **成本低**。時段不佔額外名額；天氣沒有編號但佔 1 個主動視覺控制名額；風格包佔 1 個卻會覆寫多個軸，把你原本精心選的技法洗掉。

### 2-5 情緒 → 時段 + 天氣

| 使用者說的 | 時段 | 天氣 | 為什麼 |
|---|---|---|---|
| 孤獨、失落、走不出去 | deep night | 雨後 | 空街 + 反射 = 畫面裡有兩個世界卻只有一個人 |
| 溫暖、懷舊、想起某個人 | golden hour | 濕熱空氣 | 低角度逆光 + 高光暈開 = 記憶的物理外觀 |
| 不安、有事要發生 | pre-dawn | 霧 | 有光但沒有方向、看得見但看不清楚 |
| 日常、真實、不要戲劇性 | overcast noon | 陰天漫射 | 沒有任何一道光是「安排過的」 |
| 壓迫、無處可躲、酷熱 | harsh midday | 熱浪 或 風沙 | 硬光加上空氣扭曲，畫面沒有陰影可以躲 |
| 曖昧、轉折、下一步未定 | dusk | 無天氣 | 冷暖同時存在，畫面自己就是未定狀態 |
| 悲傷但克制 | blue hour | 落雪 | 低對比 + 慢速下落的前景 = 情緒被減速（雪的逆光交給街燈與櫥窗，藍調時刻沒有日光可用） |
| 危險、被跟蹤 | deep night | 雨 | 反射與雨聲的視覺對應物，加上逆光雨絲切斷視線 |

---

## 三、環境敘事

環境敘事是讓畫面「有故事」的唯一手段。光線決定情緒，構圖決定注意力，
**但只有物件能決定「這是誰」**。72 項技法裡沒有任何一項處理這件事。

### 3-1 三個物件規則

**用三個具體物件講清楚這是誰的空間。**

為什麼是三個：一個物件是道具，兩個是巧合，**三個才構成一個人的生活模式**——
觀眾會自動在三個點之間連線，補出一個沒被寫出來的人。
第四個開始，模型會把畫面理解成靜物目錄並開始自行增生雜物，主體被淹沒。

三條執行規則，缺一不可：

1. **每個物件都要給畫面位置**。`on the desk edge`、`by the door`、`on the second hook`、`in the drying rack`。
   沒有位置的物件會被模型漂浮在背景裡，或乾脆省略。
2. **至少一個物件與主體有接觸**（正在用、剛放下、手邊）。三個都只是擺著，畫面會像佈景。
   這一條同時解決 SKILL.md〈輸出閘門〉的「手有明確狀態」那一項。
3. **三個物件必須彼此一致**：同一個年代、同一個經濟水準、同一種生活習慣。
   一個矛盾的物件會摧毀整組 —— 除非那個矛盾本身就是你要講的故事（例如貧困房間裡一支昂貴的手錶）。

### 3-2 反例與正例

抽象的品質形容詞（`messy`、`old`、`cozy`、`sad`）不含任何指涉，模型只能用自己的先驗去填，
填出來的就是訓練資料的平均值 —— 一間泛用的、誰都不住的房間。**具體名詞才有指涉。**

| 不要寫 | 寫這個 | 觀眾實際讀到的資訊 |
|---|---|---|
| `a messy room` | `unwashed mugs, a half-built model kit, cigarette burns on the desk edge` | 有時間但沒精力、有需要長時間專注的嗜好、長期在室內抽菸；一個停滯但還沒放棄的人 |
| `an old house` | `a dial telephone still wired to the wall, sun-bleached curtains, a calendar two years out of date` | 年代、無人更新、時間在某一刻停住 |
| `a rich man's office` | `a single unlabelled bottle on the shelf, one armrest worn and the other untouched, no cables visible anywhere` | 階級是靠「缺少什麼」表現的（沒有雜物、沒有線、沒有標籤），不是靠「有什麼」 |
| `a sad woman` | `one plate in the drying rack, a coat still on the second hook, unopened post stacked by the door` | 情緒寫在遺留物上，不寫在表情上；比任何 `sad expression` 都可靠 |
| `a professional kitchen` | `a burn scar along the counter edge, a knife with the handle taped, three identical dish towels` | 專業＝重複性與修補，不＝新設備 |
| `a soldier's room` | `boots by the door with the laces already loosened, one photo taped inside the locker door, a pill organiser on the shelf` | 制度化的生活、一段被保留的私人關係、身體有狀況 |

### 3-3 物件 → 傳達的資訊 對照表

| 要傳達的資訊 | 寫進提示詞的物件 | 為什麼這個物件會傳達它 |
|---|---|---|
| 職業 | `chalk dust in the seam of a jacket cuff, a lanyard with the card flipped face-down` | 職業痕跡留在身體與衣物的**接觸點**，不在制服上。穿制服只說明身分，磨損才說明工時 |
| 年代 | `a CRT monitor with a beige bezel, a phone book under the receiver, a wall calendar from a local printing shop` | 年代由「當時普及、現在消失的日常物」定義，不由刻意的復古裝飾定義 |
| 經濟狀況（拮据） | `a chair leg repaired with a metal bracket, a store-brand cereal box, a bare bulb with no shade` | 貧困的視覺特徵是**修補與替代**，不是破爛 |
| 經濟狀況（富裕） | `no visible cables, no visible storage, fresh cut flowers on a weekday` | 富裕的視覺特徵是「東西被藏起來」與「消耗性的東西被日常化」 |
| 情緒狀態（憂鬱） | `curtains closed at midday, three days of dishes, a phone lying face-down` | 憂鬱是「停止維護」，靠時間累積的證據呈現 |
| 情緒狀態（焦慮） | `the same to-do list rewritten three times on one pad, chewed pen caps, an alarm clock turned to face the wall` | 焦慮是「反覆」與「迴避」，兩者都會留下重複的物件 |
| 時間流逝 | `a pale rectangle on the wall where a frame used to hang, a plant with dry lower leaves, a coffee ring layered over an older one` | 時間必須有**兩個狀態的疊加**才看得見：曾經在／已經不在 |
| 關係（同居、親密） | `two toothbrushes in one glass, a mug that does not match the set, shoes one size apart by the door` | 親密關係寫在「成雙但不成套」的物件上 |
| 關係（疏遠、失去） | `a second chair pushed all the way in, an untouched second pillow, a spare key still on its shop ring` | 缺席比在場更有力：位置留著，人不在 |
| 階級／教養 | `books shelved by size rather than subject, a framed diploma hung above eye level, plastic covers still on the sofa arms` | 階級寫在「如何對待物品」上，不寫在物品的價格上 |
| 健康狀況 | `a pill organiser with the days marked, a handrail newly screwed beside the bath, an inhaler on the bedside table` | 新裝的輔具＝狀況是最近才發生的，這個時間資訊比疾病本身更有戲 |
| 地域與氣候 | `a dehumidifier running in the corner, mould shadow along the window seal, sandals worn indoors` | 氣候寫在「人為了對抗它而添購的東西」上 |
| 生活節奏／近期事件 | `an unpacked suitcase still open on the floor, a hospital wristband cut and left on the counter, a taxi receipt in the fruit bowl` | 「剛剛發生過什麼」是最強的敘事鉤子，用一個未被收拾的物件就能給 |
| 信仰／價值觀 | `a small shrine shelf with fresh fruit on it, a union badge on the coat, one photograph with a black ribbon across the corner` | 價值觀寫在「被定期維護的小物」上——有人每天換那顆水果 |
| 年齡（不靠臉） | `reading glasses left folded on a newspaper, a cassette adapter still in the car, a landline handset with worn number keys` | 年齡寫在「與哪一代技術共存」上，比皺紋更難偽造 |

### 3-4 環境敘事與主體描述的比例分配

比例由景別決定，不是由喜好決定。物件在畫面上必須佔得到像素，寫了看不見的物件等於浪費權重。

| 景別 | 物件數量 | 主體 : 環境的字數比 | 物件放在哪 |
|---|---|---|---|
| `圖一 31 極端特寫` | **0 個** | 100 : 0 | 主體填滿 90–100% 畫幅，沒有空間放物件。這一格的敘事全部由材質組承擔——寫皮膚、寫布料、寫指甲縫裡的東西 |
| `圖一 32 特寫` | 0–1 個 | 90 : 10 | 臉佔畫幅高度 60–75%，唯一的物件必須貼著臉出現（耳環、領口、手裡舉到臉旁的東西） |
| `圖一 19 近景` | 1 個 | 75 : 25 | 一個物件，放在主體肩後的失焦區，只需要辨識得出輪廓 |
| `圖一 20 中景` | 2–3 個 | 60 : 40 | 標準配置。其中一個必須在主體手上或手邊 |
| `圖一 23 全身照` | 3 個 | 50 : 50 | 三個分佈在近、中、遠三個距離，其中一個放在主體腳邊 |
| `圖一 21 遠景` | 3 個「區域」 | 30 : 70 | 人只佔畫幅高度 1/6 甚至更小，這個尺度下單一小物件不可見。改寫成三個**區域狀態**：人造痕跡（招牌、電線、鐵皮）、地面狀態（積水、垃圾、車轍）、天空與天氣 |

兩條配套規則：

- **主體描述永遠寫在物件之前**。物件是用來解釋主體的，順序反過來，模型會把場景當主體、把人當佈景
  （這是組裝順序＝權重順序的直接推論，見 `05-recipes.md` 第一節）。
- **物件不佔 8 項技法名額，但佔模型的注意力**。已經寫滿 8 項技法時，物件數量從 3 降到 2。

### 3-5 什麼時候該留白不寫

以下五種情況**不要寫環境物件**，寫了會扣分：

| 情況 | 為什麼不寫 | 改成寫什麼 |
|---|---|---|
| 商業人像、企業形象照、產品攝影 | 這類需求要的是「無主張的背景」，任何物件都會替主體加上一個沒被要求的身分 | 背景寫成純粹的光學狀態：`a seamless mid-grey field falling half a stop darker toward the corners` |
| 風格包已經規定了美術（`圖二 21 賽博龐克街景`、`圖二 22 太空歌劇`、`圖二 01 德國表現主義`） | 你的物件會跟風格包自帶的美術打架，模型必須二選一，通常兩邊都做壞 | 只放**一個**刻意違和的日常物件（賽博龐克街景裡一袋剛買的青菜），用它把風格包拉回人的尺度 |
| 需要留白讓觀眾投射的情緒空鏡 | 物件太具體就變成「某個特定的人」的房間，觀眾無法代入 | 保留人的痕跡但不保留身分：`an unmade bed`、`a half-full glass`，這類物件屬於所有人（見 `05-recipes.md` 配方 8，並照該配方明寫 `no person in frame`） |
| `圖一 31 極端特寫`、`圖一 32 特寫` | 畫面上沒有物件的容身空間 | 把預算全部轉給皮膚組與材質組 |
| 主體本身尚未寫清楚（沒有具體外貌、動作、手的狀態） | 環境無法搶救一個模糊的主體，只會一起模糊 | 先回去補主體，通過 SKILL.md 的〈輸出閘門〉再回來加物件 |

留白不等於空白：**不寫物件時，那些字數要換成主體的具體性或光的物理描述，不能就這樣少寫。**
提示詞的總資訊量是固定預算，省下來的預算沒有花掉，模型就會拿自己的先驗去填。
