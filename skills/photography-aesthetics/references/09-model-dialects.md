# 生成模型的提示詞方言

**這是標準工作流程的步驟 0。** 前面所有檔案決定的是「畫面內容」，這一檔決定「這段內容要用哪種語法交出去」。
同一份技法清單，餵給不同模型必須寫成不同形態的文字 —— 這是本 skill 最高頻的實務失效點，
而且失效方式很隱蔽：模型不會報錯，只會安靜地給你一張沒照做的圖。

兩個典型災難：

- 一段照 `05-recipes.md` 十一槽組裝、寫滿因果子句的英文段落餵進 Midjourney → 被平均成一張泛用美圖，
  你寫的 `key light at 90 degrees` 幾乎不起作用。
- 一串 Midjourney 參數（`--ar 4:5 --stylize 50 --no glow`）餵進 GPT Image 2 → 參數不是指令，
  是**字面文字**，模型很可能盡責地把 `--ar 4:5` 這幾個字畫在圖上。

引用格式：`圖一 NN 中文標籤` = 48 項攝影技法，`圖二 NN 中文標籤` = 24 項影視風格。

> **關於時效**：生成模型的版本、參數、甚至產品分級變動極快。本檔刻意把重量放在**結構性、長期穩定的差異**上
> （句子還是關鍵詞、有沒有 negative 欄位、畫幅靠參數還是靠文字、模型會不會自作主張美化）。
> 凡是具體數值或版本相關行為，一律標註 `（會隨版本變動，實際使用前請確認）`。
> 遇到本檔沒寫的參數名稱，**去平台文件查，不要憑記憶編一個旗標** —— 編錯的旗標在多數模型上會變成畫面上的文字。
> 本檔描述的是**實測得到的行為傾向**，不是任何模型的內部實作宣稱。

---

## 一、兩種提示詞方言

### 1-1 兩種方言的本質差異

**方言 A｜自然語言指令句**
前端由一個語言模型解析整段文字，**句法結構是有意義的**：介系詞、從屬子句、`so that`、`while`、
`with the far side falling under` 會被理解成關係，不只是被當成一袋詞。因此你可以寫因果、寫相對位置、
寫條件、寫「保留 X 只改 Y」。

**方言 B｜逗號分隔關鍵詞**
文字先被編碼成一串 token 向量再進入影像模型，**句法關係大多沒有被可靠地保留**。
逗號片語比較接近一袋各自帶權重的標籤：`a man lit from the left` 和 `left, lit, a man`
的差別遠比你以為的小。因果句在這裡是浪費 token —— `so that the far cheek falls into shadow`
多半只被吸收成 `cheek`、`shadow` 兩個弱訊號。
（各家前端的文字編碼器不同，Midjourney 這類閉源產品的架構也沒有公開；
關鍵詞型前端通常還有固定的 token 預算，超過的部分被截斷或切段處理，實作各異、會隨版本變動。
這是「寫太長會被稀釋」的成因之一，但不要當成精確的字數規則。）

| | 方言 A 自然語言指令句 | 方言 B 逗號分隔關鍵詞 |
|---|---|---|
| 權重來自 | 語意角色 + 位置（位置影響較弱） | 位置（越前越重，衰減明顯）+ 重複 |
| 加強某一項的方法 | 把它寫成獨立主要子句、給具體數字、加上可見的結果描述 | 前移到句首、換更精準的單詞、平台支援時用該平台的權重語法（例如 Midjourney 的 `::`，語法與行為會隨版本變動，實際使用前請確認） |
| 否定式 | 可直接寫（`do not add fill light`），指令遵循型模型多半會照做，但仍非保證 | **不可靠，有時反而強化被否定的名詞**（`no smile` 常常笑得更開）。必須改寫成正面描述，或丟進 negative 欄位 |
| 長度甜蜜點 | 80–200 words，可分成數句（會隨版本變動，實際使用前請確認） | 10–25 個逗號片語、約 40–100 words；再長開始稀釋（會隨版本變動，實際使用前請確認） |
| 相對位置／空間關係 | 較可靠（`her hand at the lower right of frame`） | 不可靠，只能靠構圖名詞近似（`off-centre`、`foreground`） |
| 數字（f/1.8、90 degrees、5600K） | 較常被對應到正確的外觀，但**沒有任何模型在算光學**：數字只是統計上與某種長相共現的標籤，仍要補一句看得見的結果 | 幾乎只當風格暗示，**必須配一個看得見的結果詞**，否則等於沒寫 |
| 一次能吃幾項技法 | 8 項（本 skill 的操作上限，見 SKILL.md 硬規則 4，不是模型規格） | 6 項；Midjourney 再往下壓到 5 項 |

> **色溫數字的特別提醒**：K 值本身不決定畫面偏暖或偏冷，決定的是**光源色溫與白平衡基準的差**。
> 整場都是 5600K、白平衡也對在 5600K，畫面就是中性白。要看得見的色偏，必須寫成關係或形容詞：
> `3200K tungsten pool against the 6500K window`、`cold white`、`firelight orange`。
> `01-lighting.md 13 底光` 已經指出：模型對 `5600K` 的反應遠不如對 `cold white` 這類色彩形容詞，**兩者要一起寫**。

> **方言不是模型的固有屬性，是「哪一種寫法在該模型上命中率高」。**
> 多數當代模型兩種都能吃，差別在哪一種不會被浪費。判斷不出來時走方言 A —— 關鍵詞串餵給指令型模型只是變弱，
> 指令句餵給關鍵詞型模型至少還能被抽出主要名詞。

### 1-2 A → B 的機械轉換法（照做，不要重寫）

1. **槽位順序完全不動**（順序即權重，`05-recipes.md` 第一節那十一槽在兩種方言都成立）。
2. 每槽壓成 1–2 個名詞片語，刪掉所有連接詞、從屬子句、`so that`、`while`、`with ... falling`。
3. **因果句改成結果狀態句**：`key light at 90 degrees so the far cheek falls four stops down`
   → `key light 90 degrees camera right, far cheek four stops down`。
4. **所有否定式抽出來分流**：有 negative 欄位就搬進去；沒有就照本檔〈三、通則 2 與 3〉改寫成正面描述
   （皮膚類的兩句否定 `no skin smoothing` / `no beauty retouching` 的分流規則見 `07-beyond-the-charts.md` 1-1 最後兩列）。
   注意 `07-beyond-the-charts.md` 1-4 是**堆砌詞／假詞禁用表**，不是否定改寫表，兩者不要混用。
5. 數字保留，但每個數字後面補一個可見結果：`f/1.8` → `f/1.8, the far ear already soft`。
6. 砍到 6 項技法、25 個逗號片語以內。砍的順序：色彩 → 影調 → 景深 → 光質（保留主體、景別、光位到最後）。
7. 畫幅：只有參數型模型才寫成參數尾綴，其餘一律用平台欄位。

B → A 是反向操作：把片語接回句子、把光位與陰影落點合併成一句因果、把 negative 欄位的內容
改寫成正文的正面描述或 `do not` 句。

### 1-3 完整範例：同一組技法的兩種方言

**技法清單（5 項）**
`圖一 32 特寫` `圖一 03 側光` `圖一 47 硬光` `圖一 42 暗色調` `圖一 25 淺景深`

**方言 A｜自然語言指令句（GPT Image 2 / Nano Banana / Flux / 未知模型）**

```
A man in his late fifties with three-day stubble and a scar through his left eyebrow,
jaw set, eyes fixed just past the lens, exhaling slowly through his nose, square to
the camera in an unlit workshop with a bare concrete wall behind him, close-up cut at
the collarbone, his face filling two thirds of the frame height, shot from 1.5 metres
on a 105mm lens so the ears sit tight against the skull, a single small undiffused
source at 90 degrees camera right at eye height, split lighting with one half of the
face lit and the other half unfilled and four stops down, the nose shadow running
sideways into the dark half instead of dropping down the cheek, the line between the
halves knife-thin, the light raking across pores and stubble, low key with the wall
falling to near black so only the lit cheek, the wet lower lip and one catchlight sit
above the noise floor, f/1.8 focused on the near eye with the far ear already soft,
visible skin texture, slight redness around the nose and ear, do not smooth the skin,
nothing bouncing back into the shadow side
```

約 190 words，落在甜蜜點上緣；再長就要先砍質感層。
這段通過 SKILL.md〈輸出閘門〉全部適用項目（手不入鏡，該項不適用）。

**方言 B｜逗號分隔關鍵詞**

```
close-up portrait, man in his late fifties, three-day stubble, scar through the left
eyebrow, face square to the lens, framed at the collarbone, face two thirds of frame
height, 105mm, bare concrete wall behind, single hard undiffused key 90 degrees
camera right at eye height, split lighting, one half lit and one half four stops
down, nose shadow running sideways into the dark half, knife-thin shadow edge, raking
light across pores and stubble, unfilled shadow side, small hard speculars, low key,
background near black, f/1.8, far ear already soft, open pores, slight redness around
the nose and ear
```

23 個逗號片語、約 100 words。

**Midjourney 版的完整交付（技法砍到 5 項、片語再壓短，含參數尾綴）**

```
close-up portrait, man in his late fifties, three-day stubble, scar through the left
eyebrow, face square to the lens, framed at the collarbone, single hard undiffused
key 90 degrees camera right at eye height, split lighting, half the face four stops
down, knife-thin shadow edge, nose shadow running sideways into the dark half,
unfilled shadow side merging into the black background, low key, f/1.8, far ear soft,
open pores --ar 4:5 --stylize 50 --no softbox, glamour retouching, glow
```

16 個逗號片語、約 70 words（`--stylize` 的可用範圍與預設值會隨版本變動，實際使用前請確認）。

> **`--no` 的兩條硬規則**：①只放**看得見的東西**（softbox、glow、retouching），
> 不要放抽象概念。②每一項都不能包含你在正文裡需要的字 —— `light`、`skin`、`blur`
> 常常同時出現在正文，寫成 `--no fill light` / `--no smooth skin` / `--no blur`
> 會連你要的打光、皮膚、散景一起削弱。想消掉沒要的邊緣光，改用正面描述
> （`unfilled shadow side merging into the black background`）比放進 `--no` 安全。

**兩版差在哪（逐項對照）**

| 項目 | 方言 A 的寫法 | 方言 B 的寫法 | 為什麼要換 |
|---|---|---|---|
| `圖一 03 側光` | `a single small undiffused source at 90 degrees camera right at eye height, split lighting with ...` + 鼻影走向子句 | `single hard undiffused key 90 degrees camera right at eye height` + `split lighting` + `nose shadow running sideways into the dark half` | 因果子句在 B 被拆散；改成三個獨立片語，各自都是可抽樣的視覺狀態 |
| `圖一 47 硬光` | `the line between the halves knife-thin`、`the light raking across pores and stubble` | `knife-thin shadow edge` + `small hard speculars` + `raking light across pores and stubble` | B 讀不懂「一兩毫米」這種量測，讀得懂 `knife-thin`、`hard specular` 這類狀態詞 |
| `圖一 42 暗色調` | `low key with the wall falling to near black so only the lit cheek ... sit above the noise floor` | `low key` + `background near black` | 因果長句在 B 會被壓成弱訊號，拆成兩個明確片語 |
| `圖一 25 淺景深` | `f/1.8 focused on the near eye with the far ear already soft` | `f/1.8, far ear already soft` | 兩種方言都必須讓數字配一個看得見的結果 |
| 反美化 | `do not smooth the skin`（指令遵循型模型可放句尾） | 正文寫 `open pores, slight redness around the nose and ear`；否定丟 `--no glamour retouching` | B 的正文否定不可靠，甚至反效果 |
| 補光 | `nothing bouncing back into the shadow side` | `unfilled shadow side` + `merging into the black background` | 把否定翻成一個狀態形容詞，比丟進 `--no` 安全 |
| 畫幅 | 用平台畫幅欄位設定，提示詞內不寫 | `--ar 4:5` | 參數字串跨模型就是噪音 |
| 長度 | 約 190 words | 16–23 個逗號片語 | B 超過就開始稀釋 |

> **這一組技法為什麼不會打架**：`圖一 47 硬光` 的衝突項是 `圖一 09 柔光`、`圖一 43 低對比度`、`圖一 44 亮調`，
> 這裡都沒有用到；`圖一 03 側光` 的強化項正好就是 `圖一 47 硬光`、`圖一 42 暗色調`、`圖一 32 特寫`。
> 換技法之前先查 `05-recipes.md` 表 A／表 B。

---

## 二、模型對照表

> 模型名稱、產品分級與所有參數都會隨版本變動。本表只保證**結構性差異**的方向，
> 任何具體數值在使用前都要去平台文件確認；文件沒寫的旗標就是不存在，不要憑記憶補。

| 模型 | 方言形態 | 長度甜蜜點 | negative prompt | 畫幅寫法 | 已知傾向與注意事項 |
|---|---|---|---|---|---|
| **GPT Image 2** | 方言 A（強）。整段散文可解析，可下條件式、相對位置、「只改 X 保留 Y」 | 80–200 words，可分成數句（會隨版本變動，實際使用前請確認） | **無獨立欄位**。正文寫 `do not add a rim light` 在這類指令遵循型模型上相對容易生效，但不是保證；仍以正面描述優先，否定句一律集中在句尾 | 用平台／API 的尺寸或畫幅欄位（可選尺寸會隨版本變動）；純文字介面才寫成句子 `vertical 4:5 frame`。**絕不寫 `--ar`** | 指令遵循 > 美感。預設偏乾淨的廣告式打光與整潔皮膚，要暗調與質感必須明寫反制。畫面內英文文字相對可靠。**任何看起來像參數或標籤的字串會被當成要畫進圖裡的文字**。內容政策較嚴，真實人物與品牌標誌多半會被擋 |
| **Nano Banana 系列**（分級與可用性依版本而異） | 方言 A（強），對話式多輪編輯是主場 | 文生圖 60–150 words；**編輯指令越短越準，一次只講一件事** | 無獨立欄位。否定改成正面描述最穩，`do not` 可用但不保證生效 | 平台欄位或參數。**圖生圖傾向沿用輸入圖的比例**（會隨版本變動），要改比例得明講或改用 outpaint | 參考圖／角色一致性是強項，適合同一人物多張。圖生圖時傾向保留原圖，換光位、換視角、換景別常常改不動（見 `11-image-input.md` 可改性分級）。傾向自動修飾臉部，反美化詞不能省 |
| **Seedream** | 兩種都吃；**自然語言句 + 尾段補幾個關鍵詞**的混合最穩 | 60–120 words | 依部署而定，部分 API 提供 negative 欄位（會隨版本變動，實際使用前請確認）。有就用，沒有就全部改正面描述 | 平台欄位，常見為固定比例選單；不要寫參數字串 | 商業／電商美感先驗強，預設光滑、高飽和、乾淨背景。要 `圖一 42 暗色調`、`圖一 45 低飽和`、髒污與粗顆粒，**必須寫得比對其他模型更重、更具體**。中英雙語，中文字渲染在幾個模型裡相對可靠，但仍需逐字驗收 |
| **Seedance**（影片） | 方言 A，而且必須是**時序句**：開場是 X → 過程中 Y → 結束在 Z | 單鏡 40–100 words | 多數影片介面無 negative。用正面描述鎖住：`the camera stays locked off` 取代 `no camera shake` | 平台欄位（比例 + 解析度 + 時長）。若該平台文件列出文字參數就照文件寫，**不要憑記憶編旗標** | 純靜態描述 → 得到幾乎不動的片段。一個片段 = 1 個攝影機運動 + 1 個主體動作，**單一片段內禁寫 cut / transition / 然後切到**。圖生影時首格由輸入圖決定，提示詞只描述「接下來發生什麼」，不要重述圖中已有的內容。詳見 `08-motion.md` |
| **Flux** | 方言 A（對長句解析力好），也吃方言 B | 50–120 words | **依變體而定**：negative prompt 只有在採樣器真的跑 classifier-free guidance 的兩路推論時才有作用；guidance 蒸餾的快速變體沒有那一路，寫了幾乎不起作用（會隨版本變動，實際使用前請確認）。**預設當成沒有**，一律改正面描述 | width / height 或平台欄位 | 美感先驗弱、比較聽話，適合精確幾何與光位。相對地它**不會自己補「好看」**，質感要自己給（`07-beyond-the-charts.md` 三組詞庫）。手部、極端光比、密集小物件仍常崩 |
| **Midjourney** | 方言 B：短關鍵詞串 + 參數尾綴。**長段落會被平均掉** | 10–20 個逗號片語（約 40–80 words） | **有**：`--no <東西>`（可逗號列多項），用法見 1-3 的兩條硬規則。正文不要出現 `no` / `without` | `--ar 4:5` 這類參數尾綴 | 美感優先 > 指令遵循，會自作主張美化、統一風格、加上你沒要的邊緣光與霧氣。`--stylize` 越高越美化越不聽話，要精確就壓低（參數名稱、可用範圍與預設值會隨版本變動，實際使用前請確認）。對材質、載體、氛圍名詞反應極好；對 `f/1.8`、`90 degrees`、`5600K` 反應弱 —— 數字必須配結果描述 |
| **其他／未知模型** | **預設方言 A**（相容性最高） | 60–100 words | **預設當成沒有**，全部改正面描述；先查平台是否有欄位 | **只用平台欄位**，提示詞內不寫任何參數字串 | 先跑下面那張「校準張」，用三個讀數決定寫法。不要一次改三個地方去猜它的脾氣 |

### 未知模型的校準張（原樣貼上，不要改）

```
A woman in her early forties in a grey mechanic's overall, both hands tightening a
bolt on a workbench, close shot from the chest up in a windowless workshop, a single
hard undiffused lamp at 90 degrees camera left at eye height, one half of her face
lit and the other half unfilled and four stops down, low key with the wall behind
falling to near black, f/1.8 focused on the near eye, visible skin texture, pores
open across the nose and inner cheeks, do not add a rim light
```

只讀三件事，每一件直接對應一個寫法決定：

| 讀數 | 看什麼 | 是 → 怎麼寫 |
|---|---|---|
| ①自動美化 | 皮膚有沒有被抹平、有沒有多出你沒要的邊緣光或霧 | 有 → 反美化詞加倍（`07-beyond-the-charts.md` 1-1 固定組合再加一句），並把打光寫得更絕對（`unfilled`、`no source on that side` 的正面版本） |
| ②數字有沒有被執行 | f/1.8 的背景是不是真的散、暗半邊是不是真的暗 | 沒有 → 所有數字後面補結果描述，並把光比改寫成看得見的狀態 |
| ③正文否定有沒有生效 | 有沒有出現 rim light | 有出現 → 這個模型不吃正文否定，全部改正面描述或搬進 negative 欄位 |

### 各模型的一句話操作準則

- **GPT Image 2**：把提示詞當成「給攝影師的拍攝指示」來寫，包含要避免什麼；但整段裡不能有任何 `--` 開頭的東西。
- **Nano Banana**：不要一次到位。第一輪只鎖主體與構圖，第二輪改光，第三輪改質感，每輪只講一件事。
- **Seedream**：反美化詞寫到 `07-beyond-the-charts.md` 1-1 的上限（4 句，不要再多），並同時明寫降飽和。
- **Seedance**：先寫完「這幾秒發生了什麼變化」，再回頭補光線與色彩；順序反過來會得到一張會動的靜照。
- **Flux**：可以放心給精確數字與幾何，但質感層不給就沒有，`subtle film grain` 那一組別省。
- **Midjourney**：技法砍到 5 項以內，剩下的交給 `--stylize` 與 `--no`。要精確控制就換模型，不要跟它硬拗。
- **未知模型**：先跑校準張，再決定寫法。

### 誤投方言的症狀對照表

畫面**內容**不對（太平、太黑、顏色髒、皮膚像塑膠）查 `05-recipes.md` 第五節除錯表；
**語法投錯方言**才查這一張。

| 症狀 | 幾乎確定的原因 | 修法 |
|---|---|---|
| 圖上出現 `--ar 16:9`、`--no glow` 之類的字 | 把參數尾綴餵給非參數模型 | 刪掉全部參數，改用平台畫幅欄位 |
| 精確寫了一整段，結果是一張泛用美圖 | 把方言 A 長句餵給美感優先模型 | 砍到 10–20 個片語，只留 4–5 項技法，其餘交給參數 |
| 寫了 `no smile` 結果笑得更開 | 在不吃正文否定的模型裡寫句中否定 | 抽出否定，改正面描述或搬進 negative 欄位 |
| `--no` 下去之後畫面整個變暗／皮膚變糊 | `--no` 裡放了正文也需要的字（`light`、`skin`、`blur`） | 換成不與正文重疊的具體名詞，或改用正面狀態描述 |
| 皮膚一律光滑、光一律變柔、多出沒要的邊緣光 | 模型自動美化未被反制 | 加皮膚組正面描述 + 依模型分流的反美化否定，並降 stylize 類參數 |
| 給了 f/1.8 但背景還是清楚 | 兩個成因：數字被當成風格暗示；或景別本身就不可能糊 | 補結果描述（`the background dissolving into unread colour blocks`）；同時檢查景別 —— `圖一 21 遠景` 在任何光圈下背景都不會糊，淺景深要配 `圖一 19 近景` 以上或長焦（見 `05-recipes.md` 表 B） |
| 影片幾乎不動 | 靜態描述餵影片模型 | 改寫成時序句（開場 → 過程 → 結束） |
| 圖生圖整張被重畫 | 用文生圖的完整十一槽提示詞去做編輯 | 只寫「改什麼 + 保留什麼」，見 `11-image-input.md` |

---

## 三、跨模型都成立的通則

1. **越前面權重越高，兩種方言都成立，方言 B 更極端。** 主體永遠是第一個資訊，
   `05-recipes.md` 的十一槽順序不因換模型而改變。
2. **否定先分流，再下筆。** 三選一，不准混用：有 negative 欄位 → 全部搬進去、正文一個否定都不留；
   無欄位但指令遵循強（GPT Image 2 類）→ 否定句集中寫在正文最後；其餘 → 全部改寫成正面描述。
3. **改寫否定的標準做法是描述「你要的狀態」，不是描述「你不要的東西」。**
   `no fill light` → `unfilled shadow side, the far cheek four stops down`；
   `no people` → `an empty avenue with wet asphalt and a single parked car`（空景要靠正面填滿，不是靠禁止）；
   `no blur` → `deep focus at f/8, the far end of the street legible`。
4. **模型自作主張美化時，兩手同時做**：否定端 `no beauty retouching` / `no skin smoothing`（依第 2 條分流），
   正面端補 `visible skin texture` + `slight redness around nose and ears` + 一句依景別選的細節
   （詞庫與分流規則見 `07-beyond-the-charts.md` 1-1）。只做否定端在多數模型上救不回來。
5. **一次只改一個變數再重生。** 平台若提供 seed 就固定 seed，否則同一提示詞連生 4 張再判斷 ——
   單張差異可能只是隨機性，不是你的修改起了作用。
6. **數字要配結果。** 這條在指令型模型上是加分，在美感型模型上是必要條件：
   `85mm at f/1.4` 後面永遠跟一句「所以看起來怎樣」。沒有任何模型在算光學，
   數字只是與某種長相共現的標籤。色溫數字尤其要配色彩形容詞或另一個色溫當對照。
7. **畫幅一定要給，而且只給一次。** 平台有欄位就用欄位，提示詞裡不要重複寫；
   純文字介面才寫進句尾。兩邊都寫等於發出兩個可能衝突的指令。
8. **不要跨方言貼參數。** `--ar`、`--stylize`、`--no`、`::` 只屬於支援它們的前端，
   其他地方一律是會被畫進圖裡的字串。查不到文件就不要寫。
9. **技法上限 8 項是本 skill 的操作上限（SKILL.md 硬規則 4），方言 B 在 6 項就飽和，Midjourney 壓到 5 項。**
   換模型時要跟著砍，不要整份搬過去。
10. **影片模型必須描述變化。** 靜態九軸描述在影片模型上的結果是「一張會微微呼吸的照片」。
11. **中文字入畫預設當成會失敗**（Seedream 相對可靠但仍需逐字驗收）。標準做法是在畫面預留乾淨區塊、文字後製加。
12. **換模型時不要沿用另一個模型的提示詞。** 走 1-2 的機械轉換法重出一版，並在回覆中標明是哪個模型的版本。
13. **每次交付都要能被重現**：模型名稱、完整提示詞、negative（若有）、畫幅、seed（若有）一起記下來。
    少記畫幅是最常見的失誤 —— 畫幅一改，景別與構圖比例全部重算，等於整張重來，
    它是唯一一個改了就沒辦法再用「只改一個變數」來比較的項目。

---

## 四、輸出格式規則

### 4-1 固定五段格式（每次輸出提示詞都照這個排）

````
**目標模型**：<模型名稱>（方言：自然語言指令句／逗號分隔關鍵詞）
**技法清單（N 項）**：`圖一 NN 中文標籤` `圖一 NN 中文標籤` …（風格包用 `圖二 NN 中文標籤`）
**補充維度**：<有使用時才列 `時段：...`、`天氣：...`、`質感：...`；天氣不算入上方 N，但計入 8 項主動視覺控制上限>
**提示詞**

```
<英文提示詞全文，不夾任何中文>
```

**Negative prompt**：<僅在該模型有獨立 negative 欄位時才出現這一段；
Midjourney 的 `--no` 併在提示詞尾綴裡，不另開這一段>
**建議畫幅**：<比例>（<用平台欄位設定／寫在句尾／參數尾綴>）
**想調整的話**：<一句話，必須指名一個編號技法與它的替代編號，並附上要換掉的那個英文片語>
````

### 4-2 範例（照上面格式的實際輸出長相）

**目標模型**：Midjourney（方言：逗號分隔關鍵詞）
**技法清單（5 項）**：`圖一 32 特寫` `圖一 03 側光` `圖一 47 硬光` `圖一 42 暗色調` `圖一 25 淺景深`
**提示詞**

```
close-up portrait, man in his late fifties, three-day stubble, scar through the left
eyebrow, face square to the lens, framed at the collarbone, single hard undiffused
key 90 degrees camera right at eye height, split lighting, half the face four stops
down, knife-thin shadow edge, nose shadow running sideways into the dark half,
unfilled shadow side merging into the black background, low key, f/1.8, far ear soft,
open pores --ar 4:5 --stylize 50 --no softbox, glamour retouching, glow
```

**建議畫幅**：4:5（已寫成 `--ar 4:5` 參數尾綴）
**想調整的話**：想讓臉更柔和、更好親近，只把 `圖一 47 硬光` 換成 `圖一 09 柔光` ——
`knife-thin shadow edge` → `soft wrapped shadow edge, light spilling around the jaw, broad soft speculars`，
其他一字不動（方言 B 讀狀態詞不讀量測，所以不要寫成「幾公分寬」）。

### 4-3 沒指定目標模型時

**優先做法**：把「這段要餵給哪個模型？」放進第一輪釐清問句（`06-analysis.md` 規定最多問 3 個問題，
這一題排第一 —— 方言選錯會讓後面所有技法歸零），不要為了它單獨多開一輪對話。

**若不適合追問**（使用者急、或已在多輪對話中）：預設輸出方言 A 自然語言版，
並在回覆最上方用一行標明假設：

> 假設：未指定目標模型，以自然語言方言輸出（相容性最高，可直接用於 GPT Image 2、Nano Banana、Flux、Seedream）。
> 若要餵 Midjourney，告訴我，我改成關鍵詞版並附上參數尾綴。

**禁止**：在未確認模型時就寫參數尾綴。參數是最不可攜的部分，寧可少給也不要給錯。

### 4-4 多模型並列時

使用者明說「三個模型都給我」才並列。並列時**每個模型完整走一次五段格式**，
不要共用一段提示詞再附註「Midjourney 請自行加 `--ar`」—— 那正是本檔要消滅的錯誤。
並列上限 3 個模型，超過就先問使用者最想先試哪一個。

### 4-5 建議畫幅速查

使用者明確指定的畫幅或交付版位永遠優先；下表只是在需求未指定時的預設值。風格包鎖死畫幅時，應說明衝突並請使用者在交付規格與風格忠實度之間做選擇，不可靜默覆寫使用者要求。

| 用途 | 畫幅 | 備註 |
|---|---|---|
| 人像、社群主圖 | 4:5 | 直式最泛用的預設 |
| 電影感單張 | 2.39:1 | 僅限使用者未指定畫幅時；最便宜的電影感來源（SKILL.md 硬規則 8）。平台不支援時生 16:9 再上下裁，不要拿 1:1 去裁 |
| 一般橫幅、影片 | 16:9 | 影片平台的預設 |
| 短影音、手機直式 | 9:16 | |
| 方形、頭像 | 1:1 | 只在真的需要時用 —— 預設 1:1 是最沒有意圖的畫幅 |
| `圖二 17 VHS 錄影帶`、`圖二 14 數位早期` | 4:3 | `04-film-styles.md` 把 4:3 列為這兩項的辨識點之一，不給就不成立 |
| `圖二 16 黑白默片` | 1.33:1（silent aperture） | **不可寫成 1.37:1** —— 1.37 Academy 是 1932 年有聲之後才定的規格，見 `04-film-styles.md` 該項〈構圖〉欄。平台只有 4:3 時用 4:3 代替 |
| `圖二 11 三色印片` | 1.37:1 Academy | 這一項才是 1.37；與上一列不可互換 |
| `圖二 09 固定長鏡頭`、`圖二 23 生活寫實` | 1.85:1 | `04-film-styles.md` 兩項的〈構圖〉欄都以 1.85:1 為首選（09 另可 1.66:1，23 另可 1.78:1） |

其餘風格包**一律以 `04-film-styles.md` 該項〈構圖〉欄列出的第一個畫幅為準**，不要憑印象給。
畫幅與風格包衝突時以風格包為準：選了 `圖二 17 VHS 錄影帶` 卻給 2.39:1，等於選了一個不存在的載體。

### 4-6 提示詞區塊的硬規則

- 區塊內**只有英文**，一個中文字都不要。說明、理由、替代方案全部寫在區塊外。
- 不要在區塊內寫註解（`// key light` 這類），部分模型會照字面畫。
- 不要排成分行的詩句形式。
- **方言 B 全篇用逗號連寫，不用句號**（`05-recipes.md` 第一節的寫法硬規則）。
  方言 A 可以分成數句 —— `04-film-styles.md` 多數提示詞就是多句寫成的 ——
  但每一句都必須指向**同一個畫面**，絕不出現 `another shot`、`second image`、`then` 這類會被讀成第二張圖的措辭。
- 交付前對照 SKILL.md 的〈輸出閘門〉逐項檢查，**閘門不通過不准輸出**（不在畫框內的項目才可免除，並要註明）。
- 交付前再掃一次禁詞：`beautiful`、`masterpiece`、`8k`、`high quality`、`award winning`、
  `ultra detailed`、`trending on artstation`，`07-beyond-the-charts.md` 1-4 的整張禁詞清單，
  以及任何導演姓名與電影片名。
  技術與載體名詞（Technicolor、Kodachrome、VHS、16mm、DV、anamorphic）不在此限。
