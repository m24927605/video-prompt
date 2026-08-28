# 組合配方篇

**這是每次寫提示詞都該打開的檔案。** 單獨一項技法沒有用，
決定成敗的是「哪些該疊、哪些不能疊、疊的順序是什麼」。

---

## 一、提示詞組裝公式

本檔編號規則：`T01–T48` = 圖一攝影技法，`S01–S24` = 圖二影視風格。風格包（S）佔用 1 個主動視覺控制名額；天氣沒有編號但也佔 1 個名額，全篇合計上限 8。

### 固定組裝順序

```
主體 → 景別 → 視角/朝向 → 光位 → 光質 → 光源與色溫
     → 影調與對比 → 色彩 → 景深 → 質感/載體 → 風格總結
```

順序不是美觀問題，是**權重問題**。當代 diffusion / autoregressive 影像模型對前段 token 的注意力配置顯著高於後段；越靠前的詞越接近「這張圖是什麼」，越靠後的詞越接近「這張圖表面長怎樣」。把 `cinematic` 寫在第一個字，模型會先畫出一張「泛用電影海報」，再勉強塞進你的主體。

| # | 槽位 | 寫什麼 | 取自 | 可省略？ | 為什麼放在這個位置 |
|---|---|---|---|---|---|
| 1 | 主體 | 誰／什麼 + 在做什麼 + 穿什麼／材質是什麼 | 使用者需求 | 不可 | 前 10–20 個 token 決定畫面骨架。主體不明確，後面所有技法都作用在一團猜測上 |
| 2 | 景別 | 主體佔畫面比例、切在身體哪個部位 | T19 T20 T21 T23 T31 T32 | 不可 | 景別是後續所有描述的**尺度基準**。寫晚了模型已經構完圖，再改就是拉扯 |
| 3 | 視角/朝向 | 相機高度、相機方位、主體臉朝哪 | T17 T26 T28 T29 T30 T33 T39 | 少數可 | 幾何層。必須在打光前鎖定，因為陰影落點取決於相機與光的相對位置 |
| 4 | 光位 | key light 的方向與高度，**以及陰影落在哪** | T03 T04 T05 T07 T13 T27（+T10 T14 補光） | 不可 | 光位是立體感的唯一來源，且屬於幾何。模型判斷光位靠陰影，所以陰影要跟光位寫在同一句 |
| 5 | 光質 | 陰影邊緣過渡寬度、光源相對尺寸 | T09 T47（+T15 T18 T48 特殊光形） | 可 | 光質是光位的修飾語，方向錯了再軟也沒用，所以必然在光位之後 |
| 6 | 光源與色溫 | 光從什麼東西發出來、幾 K | T06 T08 T11 T12 T36 T41 | 可 | 給光一個「物理來源」是最有效的真實感手段。放這裡是因為它修飾的是上面兩槽 |
| 7 | 影調與對比 | 亮度重心在哪、黑位是否壓死、highlight 是否破 | T02 T42 T43 T44 T46（+T37 T40 照度） | 可 | 屬於全域調光層，晚於局部打光層。放前面會壓過主體描述 |
| 8 | 色彩 | 色溫傾向、飽和度、哪個顏色是主色 | T01 T16 T38 T45 | 可 | 色彩比影調更表層。**放太前面會污染主體**——太早寫 warm，模型會把衣服、皮膚、牆一起染橘 |
| 9 | 景深 | 光圈值、焦段、背景解析程度 | T22 T24 T25 | 可 | 純鏡頭參數，只影響背景，對主體幾何無干擾，所以可以晚 |
| 10 | 質感/載體 | 底片、顆粒、halation、感光元件世代 | S11 S12 S14 S17 S18 S20 | 可 | 全畫面 overlay 層，最後套上去。寫早了模型會用它取代內容 |
| 11 | 風格總結 | 最多一句，收束整體 | S01–S24 | 可 | 收尾用。不是拿來下指令的，是拿來加權的 |

**寫法硬規則**

- 槽位順序固定，但分隔符號依目標模型方言決定：方言 B 用逗號片語、全篇不用句號；方言 A 可分成數句，每句仍必須描述同一個畫面。以 `09-model-dialects.md` 為準。
- 每個槽只寫一個值。同槽兩個值＝互相抵銷，見〈二、互斥矩陣〉。
- 光位槽必須同時寫「光從哪來」與「暗部在哪」。只寫 `side light` 的命中率遠低於 `key light 90 degrees to camera left, the far side of the face falling two stops under`。
- 給數字：`f/1.8`、`85mm`、`5600K`、`45 degrees`、`1/8 second`。數字是模型最難誤讀的指令。
- 否定描述放最後或丟進 negative prompt，不要夾在中段。

---

### 範例 A｜人像

**需求**：「幫我拍一張書店裡的人物照，要有電影感，但不要太做作，要可信。」

**用了哪幾號技法（8 項）**

| 槽位 | 技法 |
|---|---|
| 景別 | T20 中景 |
| 朝向 | T30 四分之三側面 |
| 光位 | T04 側逆光 |
| 光質 | T09 柔光 |
| 光源 | T08 窗光 |
| 影調 | T42 暗色調 |
| 景深 | T25 淺景深 |
| 載體 | S18 十六毫米顆粒 |

**最終英文提示詞**

```
A woman in her mid-thirties wearing a grey wool cardigan, standing between two tall
bookshelves with an open paperback held at her waist, medium shot framing her from
the waist up, three-quarter view with her shoulders turned 40 degrees off axis and
her face angled back toward the lens, key light entering from a tall window at frame
left and slightly behind her so a thin bright edge traces her cheekbone, jaw and the
top of her forearm while the front of her face sits in open shadow, light diffused
through a sheer curtain giving a shadow edge over two centimetres wide, north-facing
window light at 5600K with no other source in the room, low-key overall with the
shelves behind her falling into deep shadow and only her lit edge, her hands and the
open page held above the noise floor, shot at f/2 on a 50mm lens so the spines behind
her dissolve into unread colour blocks, 16mm film capture with visible grain,
soft-shouldered highlights and slight halation where the window clips
```

**為什麼是這個順序**：主體與動作先鎖住（女性／羊毛外套／拿著書），景別緊接著把她固定在腰上，之後所有描述都落在「腰上構圖」這個尺度裡。若把 `16mm film grain` 提前，模型會先進入「復古底片照」模式，人物會被顆粒和整體風格吃掉。

---

### 範例 B｜場景

**需求**：「雨後的城市街道，晚上，想要那種很孤獨的感覺。」

**用了哪幾號技法（8 項）**

| 槽位 | 技法 |
|---|---|
| 景別 | T21 遠景 |
| 視角 | T17 高角度拍攝 |
| 光源 | T11 自發光 |
| 色溫 | T36 冷光源 |
| 影調 | T42 暗色調 |
| 對比 | T46 高對比 |
| 景深 | T22 深景深 |
| 風格 | S06 單光源夜戲 |

**最終英文提示詞**

```
An empty four-lane avenue twenty minutes after rain, a single figure in a dark coat
crossing at the far crosswalk, extreme long shot with the figure occupying less than
one tenth of the frame height and the road running to a vanishing point in the upper
third, camera positioned three floors up looking down at roughly 35 degrees, the
scene lit only by its own practical sources with a convenience store window at frame
right as the dominant one and everything else falling away from it, hard specular
light skidding across the wet asphalt with sharp-edged reflections, mercury-vapour
street lighting and cool storefront LED at 6500K with no warm source anywhere in
frame, low-key with the sky, the building faces and the sidewalk going to black,
high contrast holding clipped speculars on the standing water against dense shadow,
deep focus at f/8 on a 24mm lens keeping the far end of the avenue legible,
single-source night photography with no fill, anamorphic 2.39:1 framing, fine grain
```

**為什麼是這個順序**：`empty` 與 `a single figure` 必須是最前面的資訊，否則模型會自動填滿人。景別（極遠景 + 主體只佔十分之一）在第二槽，直接定義了「孤獨」的視覺機制——是比例造成的，不是形容詞造成的。

---

## 二、互斥矩陣（部分已由第六章取代）

> **本節的表 A／表 B 已由〈六、衝突檢查（三張表）〉取代，請以第六章為準。**
> 本節唯一仍然有效、且被第六章引用的是下方的 **T41 雙性照明例外條款**。

### 表 A：同軸互斥——必須二選一，沒有折衷

| 軸 | 互斥組合 | 為什麼打架 | 決策規則 |
|---|---|---|---|
| 光質 | T09 柔光 ↔ T47 硬光 | 兩者定義的是同一個物理量：光源相對主體的張角。同時下指令＝要求陰影邊緣同時寬和窄，模型輸出中間值，變成「沒有個性的中性光」 | 要柔膚、要親和、要商業安全 → T09。要戲劇、要質感、要皮膚紋理與金屬拉絲 → T47 |
| 影調 | T44 亮調 ↔ T42 暗色調 | 兩者指定的是直方圖重心位置，一個推向右、一個推向左 | 主題是「輕盈／潔淨／希望」→ T44。主題是「壓抑／秘密／重量」→ T42 |
| 對比 | T43 低對比度 ↔ T46 高對比 | 指定同一個動態範圍的展開程度。並列會得到「灰霧又髒黑」的最壞結果 | 要柔和／紀錄／北歐 → T43。要張力／黑色電影／產品 → T46 |
| 色溫 | T06 暖光源 ↔ T36 冷光源 | 同一個全域色溫不能同時是 2700K 和 6500K。模型會取中間值 → 變成無色偏的白光，兩邊的意圖都消失 | 見下方「T41 例外條款」 |
| 色調 | T01 暖色調 ↔ T38 冷色調 | 同上，作用在調色層而非光源層 | 只留一個當主調，另一個降格為「局部點綴色」並明確指定它在畫面哪個物件上 |
| 飽和 | T16 高飽和 ↔ T45 低飽和 | 同一個 saturation 值 | 商品／食物／霓虹 → T16。紀實／情緒／高級感 → T45 |
| 景深 | T22 深景深 ↔ T25 淺景深 | 同一個光圈值 | 環境是敘事的一部分 → T22。環境是干擾 → T25 |
| 景別 | T21 遠景 ↔ T23 全身照 ↔ T20 中景 ↔ T19 近景 ↔ T32 特寫 ↔ T31 極端特寫 | 主體只能有一個佔比。並列兩級模型會取中間，得到一個「切得很尷尬」的構圖 | 由遠到近排序後只挑一級。要同時要遠景資訊與特寫細節 → 出兩張圖，不要出一張 |
| 相機高度 | T33 鳥瞰 ↔ T17 高角度拍攝 ↔ T39 低角度視角 | T33 是 T17 的極端版（俯角 80–90° vs 20–45°）；T39 是反向。三者是同一條連續軸上的三個點 | 要壓迫／渺小／圖案化 → T33（近垂直）。要溫和的俯視／敘事觀察 → T17。要威嚴／權力／英雄 → T39 |
| 主體朝向 | T30 四分之三側面 ↔ T29 側面視角 ↔ T28 背面視角 | 臉只能朝一個方向 | 要眼神接觸與立體 → T30（預設安全牌）。要疏離、要看「他在看什麼」→ T29。要匿名、要觀眾代入 → T28 |
| 光位 | T27 正面光 ↔ T03 側光 ↔ T04 側逆光 ↔ T05 背光 ↔ T07 頂光 ↔ T13 底光 | key light 只能有一個方向。並列＝多個 key，模型會畫出四面八方無源的光，這是「假／AI 感」的最大單一成因 | 只留一個 key。其餘想要的光降格寫成 `rim` / `kick` / `bounce`，並明確給它低於 key 的強度（例如 `two stops under the key`） |
| 光位（垂直） | T07 頂光 ↔ T13 底光 | 陰影方向完全相反（眼窩黑 vs 下巴黑） | 要審訊／宗教／權威 → T07。要恐怖／非人／營火 → T13 |
| 鏡頭運動感 | S09 固定長鏡頭 ↔ S10 手持跟拍 | 一個要求絕對靜止的機位，一個要求呼吸與跟隨。影片生成時直接互相取消 | 要觀察／疏離／時間感 → S09。要臨場／焦慮／貼身 → S10 |

### 表 B：跨軸隱性衝突——可以救，但要知道代價

| 衝突組合 | 為什麼打架 | 怎麼處理 |
|---|---|---|
| T21 遠景 ↔ T31 極端特寫 | 不只是景別互斥，兩者的**敘事功能相反**：遠景講「人與環境的關係」，極端特寫講「排除環境只剩質感」。混寫模型會給你一個中景 | 二選一。真的要「大場景中的小細節」→ 用 T21 + 前景物件，而不是加 T31 |
| T02 過度曝光 ↔ T46 高對比 | T02 要求 highlight 主動破掉、細節放棄；T46 要求 highlight 與 shadow 同時保留且拉開。兩者對 highlight 的處理直接矛盾 | 要「夏日刺眼／回憶感」→ 用 T02，並主動聲明 `blown highlights left uncorrected`。要「戲劇張力」→ 用 T46，並把曝光壓在 highlight 剛好不破 |
| T48 閃光燈 ↔ T09 柔光 | 直閃美學的定義就是「小光源硬邊 + 背景急遽衰減 + 正面壓平」。加柔光等於把它變成 softbox，那已經不是閃光燈語彙 | 要 snapshot／派對／狗仔感 → T48，接受硬邊與背景黑洞。要商業人像 → T09 並寫 softbox，不要提 flash |
| T48 閃光燈 ↔ T24 動態模糊 | 閃光的功能是凍結瞬間 | **唯一例外**：明寫 `rear-curtain sync, 1/15 second drag` 才能同時得到清晰主體 + 拖影背景。不寫這句就是互斥 |
| T22 深景深 ↔ T37 弱光 | 物理上 f/11 + 低照度 = 長曝或高 ISO。模型會混出「全景清晰但有數位雜訊」的不自然結果 | 要並用就補上成因：`tripod, 4 second exposure` 或 `high ISO with visible luminance noise` |
| T21 遠景 ↔ T25 淺景深 | 遠景存在的意義是環境資訊，淺景深把環境刪掉，功能自相抵銷 | 要壓縮感 → 改寫成 `200mm telephoto compression at f/4`，這是遠距+微淺景深的合理物理解，不要寫 f/1.4 |
| T44 亮調 ↔ T47 硬光 | 亮調需要大量 fill 把陰影抬起來，硬光的定義是不填陰影 | 要亮調 → 換 T09。硬要硬光的亮調 → 只能靠「大量白色反射環境」，必須明寫 `white cyclorama with light bouncing back from all sides` |
| T43 低對比度 ↔ T05 背光 | 背光天生製造最高對比（主體正面全暗、輪廓全亮） | 要低對比背光 → 明寫 `heavy atmospheric haze lifting the shadows` 或 `large bounce filling the front two stops under` |
| T43 低對比度 ↔ T15 舞台光 / T18 丁達爾光 / S05 煙霧體積光 | 這三者全都依賴「亮束 vs 黑周圍」的高反差來成立 | 二選一。要保留光束就放棄低對比 |
| T09 柔光 ↔ T18 丁達爾光 | 丁達爾光需要接近平行的硬光束打進介質才會成形，柔光在煙霧裡只會變成一片均勻霧 | 要光束 → T47 + 明寫 `mist / dust / smoke in the air`。要柔 → 放棄光束 |
| T12 火光 ↔ T36 冷光源 | 火是 1800K，冷光源是 6000K+ | 見 T41 例外條款；否則只留一個 |
| T33 鳥瞰 ↔ T32 特寫 / T31 極端特寫 | 90 度俯視拍臉部特寫在幾何上會得到「頭頂」，不是臉 | 要俯視又要臉 → 降到 T17 高角度拍攝（20–45°） |
| T28 背面視角 ↔ 任何需要眼神／表情的需求 | 背面視角沒有臉，T10 髮絲光、眼神光、微表情全部失效 | 要背面又要情緒 → 情緒必須由肢體語言與環境承擔，明寫肩線、手的位置、頭的傾角 |
| T45 低飽和 ↔ S11 三色印片 / S13 港片霓虹 / S02 義式驚悚紅綠光 | 這三個風格包的核心賣點就是極端飽和的色彩分離 | 選了風格包就不要再加 T45，會把風格包整個抵銷掉 |
| T16 高飽和 / T01 暖色調 / T38 冷色調 ↔ S16 黑白默片 / S15 沙塵單色 | 單色系統裡所有色彩指令都是空指令，只會浪費 token 並讓模型猶豫要不要上色 | 選了 S16 / S15 就把整個色彩槽刪掉，改寫 `tonal separation` 相關描述 |
| T26 斜側視角 ↔ S07 單點透視對稱 / S08 平面正面構圖 | 這兩個風格包的定義就是相機正對牆面、消失點在正中；斜側視角直接摧毀對稱 | 選了 S07/S08 就把視角槽鎖成 `camera perpendicular to the back wall, vanishing point dead centre` |
| T25 淺景深 + T35 居中構圖 ↔ S19 偽紀錄片 | found footage 的可信度來自業餘器材：深景深、構圖失準、對焦遲疑 | 要 S19 → 改用 T22 深景深、離心構圖，並明寫 `autofocus hunting, subject slightly off centre` |
| T24 動態模糊 ↔ S20 定格動畫質感 | 定格動畫每一格都是靜止曝光，天生沒有動態模糊，這正是它的辨識特徵 | 要 S20 就刪掉 T24。除非明寫 `go-motion streaking` |
| T15 舞台光 / T13 底光 / T47 硬光 ↔ S23 生活寫實 | 生活寫實的核心是「光看起來像沒人打過」 | 選了 S23 → 光位只能用 T08 窗光、T11 自發光、T27 正面光的自然版本 |
| T06 暖光源 ↔ S03 北歐冷冽 | S03 的定義包含極端平坦的冷白光 | 二選一。要在冷冽裡放一點暖 → 用 T41 並限定暖光只出現在一個小物件上 |
| T07 頂光 ↔ S04 魔幻時刻 | S04 的定義是太陽在地平線上 5–15 度 | 選了 S04 → 光位只能是 T04 側逆光或 T05 背光 |

### T41 雙性照明的例外條款

T41 雙性照明是**唯一一個被允許同時出現 T06 暖光源與 T36 冷光源的情況**，理由是它改變了衝突的性質：

- 一般的暖／冷並列，是對**同一塊像素**下兩個矛盾的色溫指令 → 模型只能取中間值 → 白光。
- T41 是把兩個色溫**指派到不同的空間分區**（左臉 vs 右臉、前景 vs 背景、key vs rim）。每塊像素只收到一個指令，因此不矛盾。

使用 T41 時必須滿足三個條件，缺一個就退化成髒色：

1. **明寫哪一側是哪個色溫**：`3200K tungsten key from camera left, 6500K practical rim from camera right`。
2. **明寫兩色的交界在哪**：`the two temperatures meet along the bridge of the nose`／`along the centre line of the road`。
3. **明寫強度關係**：通常 `the cool side sits one and a half stops under the warm key`。兩側等亮會讓臉失去主光，變成平面色塊。

且 T41 與 T45 低飽和、T43 低對比度衝突——這兩者會把好不容易分開的兩個色溫壓回同一團灰。

---

## 三、情緒 → 技法對照表

| 使用者說的話 | 圖一技法 | 圖二風格 | 為什麼是這幾項 |
|---|---|---|---|
| 「要有電影感」 | T20 中景 + T04 側逆光 + T42 暗色調 + T46 高對比 + T25 淺景深 | S06 單光源夜戲 | 「電影感」的可操作定義＝單一有動機的光源 + 大量放棄的暗部 + 非 1:1 的寬幅構圖。不是濾鏡 |
| 「要溫暖療癒」 | T08 窗光 + T09 柔光 + T06 暖光源 + T01 暖色調 + T43 低對比度 | S23 生活寫實 | 溫暖來自「大而軟的側前光 + 開放陰影」，療癒來自低對比消除威脅感 |
| 「要恐怖」 | T13 底光 + T47 硬光 + T37 弱光 + T42 暗色調 + T46 高對比 | S24 宇宙恐怖 / S01 德國表現主義 | 底光反轉人臉的自然陰影方向，是最低成本的「非人」訊號；硬光把陰影邊緣切成刀口 |
| 「要高級冷淡」 | T09 柔光 + T36 冷光源 + T45 低飽和 + T43 低對比度 + T35 居中構圖 | S03 北歐冷冽 | 高級感＝資訊減量。低飽和 + 低對比 + 對稱＝把所有情緒訊號拿掉，只剩形狀 |
| 「要復古」 | T01 暖色調 + T16 高飽和 + T45 低飽和（二選一，見下） + T43 低對比度 | S12 柯達克羅姆 / S18 十六毫米顆粒 / S17 VHS 錄影帶 | 復古是**載體特徵**不是色彩偏好。先問是哪個年代：1970s → S12（高飽和 + 暖）、1980s 家用 → S17（低解析 + 掃描線）、獨立電影 → S18 |
| 「要有錢有權」 | T39 低角度視角 + T03 側光 + T47 硬光 + T42 暗色調 + T22 深景深 | S07 單點透視對稱 | 權力＝觀眾必須仰視 + 空間必須對稱且巨大 + 陰影必須是刻意保留的（有錢才付得起「不照亮」） |
| 「要孤獨」 | T21 遠景 + T17 高角度拍攝 + T34 封閉構圖 + T37 弱光 + T45 低飽和 | S09 固定長鏡頭 | 孤獨是**比例問題**：主體佔畫面越小越孤獨。俯角讓主體無法反抗，封閉構圖讓他出不去 |
| 「要浪漫」 | T04 側逆光 + T10 髮絲光 + T09 柔光 + T06 暖光源 + T25 淺景深 | S04 魔幻時刻 | 側逆光 + 髮絲光讓輪廓發光、五官柔化；淺景深把世界刪到只剩兩個人 |
| 「要緊張懸疑」 | T03 側光 + T47 硬光 + T42 暗色調 + T46 高對比 + T34 封閉構圖 | S01 德國表現主義 | 懸疑＝畫面有一半的資訊被藏在暗部。側光正好把臉切成一半亮一半黑 |
| 「要夢幻」 | T05 背光 + T02 過度曝光 + T44 亮調 + T43 低對比度 + T25 淺景深 | S04 魔幻時刻 | 夢幻＝細節流失。背光洗掉輪廓、過曝洗掉高光細節、淺景深洗掉背景 |
| 「要紀實可信」 | T20 中景 + T29 側面視角 + T22 深景深 + T08 窗光 + T45 低飽和 | S18 十六毫米顆粒 / S10 手持跟拍 | 可信度來自「拍攝者不介入」：深景深（沒挑選）、非對稱構圖（來不及構）、自然光（沒帶燈） |
| 「要科技感」 | T36 冷光源 + T11 自發光 + T47 硬光 + T46 高對比 + T35 居中構圖 | S22 太空歌劇 / S21 賽博龐克街景 | 科技感＝光從物件本身發出（螢幕、燈條、LED），而不是從天上打下來 |
| 「要神聖」 | T07 頂光 + T18 丁達爾光 + T05 背光 + T44 亮調 + T35 居中構圖 | S05 煙霧體積光 | 從上方降下的光束是所有文化共通的神聖符號。必須有介質（塵／霧／香煙）光束才成形 |
| 「要頹廢」 | T15 舞台光 + T37 弱光 + T42 暗色調 + T16 高飽和 + T24 動態模糊 | S13 港片霓虹 | 頹廢＝人工光 + 過飽和 + 沒對準焦。乾淨的光會讓頹廢變成時尚 |
| 「要青春」 | T05 背光 + T02 過度曝光 + T44 亮調 + T16 高飽和 + T24 動態模糊 | S12 柯達克羅姆 | 青春的視覺語彙是「曝光失控」：逆光下讓臉曝過頭，加上手持的輕微失焦 |
| 「要危險／有壓迫感」 | T39 低角度視角 + T07 頂光 + T47 硬光 + T42 暗色調 + T34 封閉構圖 | S01 德國表現主義 | 頂光製造眼窩黑洞（看不見眼睛＝不可預測），低角度讓對方比觀眾大 |
| 「要清新日系」 | T08 窗光 + T09 柔光 + T44 亮調 + T45 低飽和 + T43 低對比度 | S23 生活寫實 | 日系＝高亮度 + 低飽和 + 幾乎沒有黑位。關鍵是黑位要抬起來，不能有純黑 |
| 「要史詩感」 | T21 遠景 + T39 低角度視角 + T04 側逆光 + T22 深景深 + T46 高對比 | S22 太空歌劇 | 史詩＝人小、天大、光從遠處逆著來把地形分層 |
| 「要憂鬱」 | T08 窗光 + T38 冷色調 + T45 低飽和 + T43 低對比度 + T28 背面視角 | S03 北歐冷冽 / S09 固定長鏡頭 | 憂鬱不是暗，是**平**。低對比 + 冷 + 沒有眼神接觸 |
| 「要真實不要修圖感」 | T27 正面光 + T48 閃光燈 + T22 深景深 + T46 高對比 | S14 數位早期 / S19 偽紀錄片 | 直閃 + 深景深 + 早期數位的色彩處理＝任何人都認得的「沒人在意美感」的照片 |
| 「要性感」 | T03 側光 + T47 硬光 + T42 暗色調 + T31 極端特寫 + T25 淺景深 | S06 單光源夜戲 | 性感靠遮蔽而非展示：硬側光讓大部分身體落入暗部，只留一條亮邊 |
| 「要荒涼」 | T21 遠景 + T40 強光 + T02 過度曝光 + T45 低飽和 + T22 深景深 | S15 沙塵單色 | 正午強光 + 去飽和 + 沒有陰影可躲＝荒涼。低角度的美光會讓荒涼變成風景明信片 |

---

## 四、常見場景的完整配方

### 配方 1｜商業人像（企業形象、品牌識別照）

- **適用時機**：需要「可信、專業、任何人看了都不會不舒服」的人像。用途是官網、名片、媒體授權照。
- **技法清單**：T19 近景 / T30 四分之三側面 / T03 側光 / T09 柔光 / T10 髮絲光 / T44 亮調 / T43 低對比度 / T25 淺景深

```
A woman in her forties in a charcoal blazer over a white shirt, chin slightly
forward, faint closed-mouth smile, medium close-up from the chest up, three-quarter
view with her shoulders turned 30 degrees off axis and her eyes directly to lens,
key light 45 degrees to camera left and 20 degrees above eye level so a short nose
shadow falls onto the far cheek without touching the lip, large softbox at close
distance giving a shadow edge several centimetres wide plus a white bounce card
under the chin opening the eye sockets, 5600K daylight-balanced studio light,
high-key with the background sitting one stop brighter than her face, low contrast
with open shadows and no crushed blacks anywhere, light grey seamless backdrop at
f/2.8 on an 85mm lens rendering it as an even field, a hair light behind camera
right separating her shoulder and hairline from the background, natural skin texture
with visible pores, individual flyaway hairs left in place
```

- **最容易失敗的地方**：亮調 + 柔光 + 低對比三者疊起來會把立體感歸零，變成證件照。**45° 短鼻影與髮絲光是這個配方唯一的第三維度來源，兩者都不能省。**

---

### 配方 2｜電影感人物劇照

- **適用時機**：角色海報、影集宣傳照、需要「這個人有故事」的單張人物圖。
- **技法清單**：T20 中景 / T26 斜側視角 / T04 側逆光 / T47 硬光 / T11 自發光 / T42 暗色調 / T46 高對比 / S06 單光源夜戲

```
A man in his fifties in a rain-damp overcoat, standing just inside a motel doorway
with one hand still on the frame, medium shot from the waist up, camera at eye level
but placed to his left so his body reads at an oblique angle to the picture plane and
the doorway line cuts diagonally behind him, a single hard source behind him at frame
right and slightly high, throwing a hot narrow edge down his cheekbone, jaw and
shoulder while the whole front of his face sits three stops under, bare small source
with a knife-edged shadow across the wall, motivated by a cyan-white neon sign
visible out of focus behind him at 6500K with no fill from any other direction,
low-key with two thirds of the frame in shadow, high contrast with black shadows and
clipped speculars on the wet fabric, shot at f/1.8 on a 40mm lens, single-source
night photography, 2.39:1 anamorphic framing, fine grain, gentle halation around
the sign
```

- **最容易失敗的地方**：不敢讓臉暗。多數人會忍不住補一句 `with soft fill on his face`，那一句話會把整個配方變回商業人像。**低調人像的張力全部來自「你看不清楚他」。**

---

### 配方 3｜產品攝影（金屬／機械類硬質產品）

- **適用時機**：手錶、刀具、耳機、工具、任何要凸顯材質與工藝的實體商品。
- **技法清單**：T32 特寫 / T39 低角度視角 / T35 居中構圖 / T03 側光 / T47 硬光 / T14 輪廓光 / T42 暗色調 / T22 深景深

```
A brushed stainless steel wristwatch standing upright on a slab of dark slate, dial
facing camera, close-up filling three quarters of the frame height, camera positioned
just below the top plane of the watch so it reads as taller than the viewer, subject
centred with equal negative space left and right, key light raking in from 80 degrees
camera left so the circular brushing on the case catches as a bright directional
streak and the crown throws a defined shadow to the right, hard narrow strip source
with a crisp shadow edge and a black flag on the opposite side keeping the shadow
side dense, a thin white strip behind and to the right placing a continuous bright
line along the watch's right contour so the case separates from the background,
5600K, low-key with a near-black background falling off to nothing, deep focus at
f/11 focus-stacked so the whole dial, the near lug and the strap texture are sharp,
macro rendering of the metal grain and the sapphire crystal's edge reflection
```

- **最容易失敗的地方**：暗背景 + 硬側光 → 產品的暗部輪廓直接消失在背景裡，形狀讀不出來。**T14 輪廓光在這個配方裡不是加分項，是必需品。** 另一個常見死法是把 f/11 寫成 f/2.8，特寫距離下景深只剩幾公釐。

---

### 配方 4｜美食

- **適用時機**：菜單、食譜、餐廳社群、外送平台主圖。
- **技法清單**：T32 特寫 / T17 高角度拍攝 / T04 側逆光 / T09 柔光 / T08 窗光 / T16 高飽和 / T01 暖色調 / T25 淺景深

```
A bowl of ramen with a halved soft-boiled egg and charred pork resting on the
noodles, steam rising off the surface, close-up shot from a 30 degree elevated angle
just above the rim of the bowl, light coming from behind the bowl and slightly to the
left so the steam catches and lights up against the dark background and the broth
surface reads as translucent, diffused through a sheer curtain giving a soft shadow
edge with a small white bounce on the near side lifting the front of the egg, late
morning window light at 5000K as the only source, warm bias through the midtones with
the broth and yolk running amber, saturated colour with the scallion greens held back
from going fluorescent, shot at f/2.8 on a 100mm macro so the far rim of the bowl
softens while the egg stays critically sharp, wet specular highlights along the
noodles and visible fat droplets on the broth surface
```

- **最容易失敗的地方**：用了 T27 正面光或 T07 頂光。**蒸氣、湯汁、油光、酥皮的邊緣全部只在側逆光下才會出現**；正面光會讓食物變成平面色塊。第二個坑是 T16 高飽和把綠色蔬菜推成螢光綠，所以提示詞裡要主動點名壓住綠色。

---

### 配方 5｜街拍紀實

- **適用時機**：報導攝影、城市觀察、需要「這是真的發生過」的畫面。
- **技法清單**：T20 中景 / T29 側面視角 / T05 背光 / T47 硬光 / T22 深景深 / T45 低飽和 / T46 高對比 / S18 十六毫米顆粒

```
A vendor lifting a crate of fish off a van at a wet market, two passers-by crossing
the near edge of frame and partially cut off, medium shot at eye level from across
the street, the vendor in profile facing frame right and unaware of the camera, hard
midday sun coming from behind him so his shoulders and the crate rim are edge-lit and
a long diagonal shadow runs toward camera across the wet ground, direct unmodified
sunlight with knife-edged shadows, 5600K, mid-key with the shadow side going dense
and one blown highlight on the van roof left uncorrected, muted colour with the reds
pulled back, deep focus at f/8 on a 35mm lens keeping the storefront signage and the
crowd behind him legible, 16mm film grain, slight handheld tilt, subject placed off
centre with dead space on the right
```

- **最容易失敗的地方**：構圖太完美。**只要出現 T35 居中構圖、對稱、或乾淨的背景，紀實感立刻變成廣告感。** 必須主動寫進「不完美」：切邊的路人、歪掉的水平線、離心的主體、爆掉的高光。同時絕對不要加 T25 淺景深——背景一糊，「現場」就消失了。

---

### 配方 6｜夜景城市

- **適用時機**：城市空景、片頭鏡頭、地產／旅遊主視覺、賽博龐克概念圖。
- **技法清單**：T21 遠景 / T33 鳥瞰 / T11 自發光 / T41 雙性照明 / T24 動態模糊 / T22 深景深 / T42 暗色調 / S21 賽博龐克街景

```
A six-way intersection seen from a rooftop, traffic mid-flow, asphalt still wet,
extreme long shot with the horizon in the upper fifth of the frame, camera looking
down at about 55 degrees so the road grid reads as a pattern, the scene lit entirely
by its own sources with shop signage, headlight streaks and an LED billboard as the
only light in frame, warm 2700K sodium and shopfront glow pooling across the right
half of the frame against cool 7000K LED and billboard spill on the left, the two
temperatures meeting along the centre line of the main avenue with the cool side one
and a half stops under, 1/6 second exposure so headlights and tail lights draw
continuous unbroken streaks while the buildings stay sharp, deep focus at f/8 on a
24mm lens holding the far towers legible, low-key with the sky and unlit building
faces going to black, every sign doubled in the standing water, dense signage in
mixed scripts stacked up the building faces, fine grain
```

- **最容易失敗的地方**：色溫變成一鍋泥。**雙性照明必須指定「暖在哪半邊、冷在哪半邊、交界在哪」**，否則模型會把兩色混成滿畫面的洋紅。第二個坑是寫了 `long exposure` 卻沒給快門值，模型只會畫出靜止的車。

---

### 配方 7｜風景

- **適用時機**：自然風景、旅遊主視覺、桌布、需要「壯闊但不做作」的地景。
- **技法清單**：T21 遠景 / T39 低角度視角 / T04 側逆光 / T18 丁達爾光 / T22 深景深 / T01 暖色調 / T46 高對比 / S04 魔幻時刻

```
A ridge of pine forest dropping into a river valley with mist still held in the
folds, extreme long shot with the ridgeline placed on the lower third and the far
range stacked in receding layers, camera low near the ground so the foreground
grasses read large against the distant valley, sun 12 degrees above the far ridge and
behind the trees so every trunk is edge-lit and the mist between them separates into
distinct depth planes, visible shafts of light cutting through the canopy where the
mist is densest, 2800K low sun as the only source, warm amber on the lit slopes
against the deep blue-shadowed valley floor, high contrast with the sun disc clipping
and the near shadows staying dense, hyperfocal at f/11 on a 35mm lens sharp from the
foreground grass to the far ridge, the fifteen minutes after sunrise with the light
still changing across the frame
```

- **最容易失敗的地方**：丁達爾光沒有介質。**光束只在空氣中有霧、塵、煙時才成形**——提示詞裡沒有 `mist / dust / haze` 這個詞，模型會畫出一層假的放射狀 overlay 貼在畫面上。第二個坑是同時要求 T22 深景深與 T25 淺景深式的前景虛化，兩者在 f/11 下不可能並存。

---

### 配方 8｜情緒氛圍圖（無人空鏡）

- **適用時機**：影片轉場、簡報底圖、情緒板、需要「留白讓觀眾投射」的畫面。
- **技法清單**：T19 近景 / T08 窗光 / T09 柔光 / T44 亮調 / T43 低對比度 / T45 低飽和 / T25 淺景深 / S23 生活寫實

```
An unmade bed with morning light lying across the crumpled sheet and a half-full
glass of water on the side table, no person in frame and no person implied in any
reflection, close shot of the near corner of the bed with the window frame just
entering at the left edge, camera at seated height looking slightly down, light
entering from a large window at frame left and slightly behind the bed so the folds
of the sheet get long soft gradients running away from camera, heavily diffused
overcast light with shadow edges several centimetres wide, 6000K, high-key with the
brightest fold sitting just under clipping, low contrast with lifted blacks and the
deepest shadow under the bed frame as the only anchor point, desaturated throughout
with the walnut side table as the single element holding any warmth, f/2 on a 35mm
lens so the far wall becomes a smooth undifferentiated field, plain unstyled interior
with a visible power socket and a creased pillowcase, slight film grain
```

- **最容易失敗的地方**：兩件事。第一，**沒有主體時模型會自動補一個人**——必須明寫 `no person in frame`。第二，亮調 + 低對比 + 低飽和三者疊起來會變成一片沒有重量的灰白霧，所以必須指定兩個錨點：**最深的暗部在哪個物件下面、唯一有顏色的東西是什麼。**

---

## 五、除錯對照表

| 生成結果的毛病 | 真正的成因 | 加什麼 | 拿掉什麼 |
|---|---|---|---|
| 畫面太平、沒立體感 | 光位是正面或無方向，模型套用了預設的環境光 | T03 側光 或 T04 側逆光，並明寫陰影落在哪一側、暗幾級（`the far cheek falls two stops under`） | T27 正面光、T09 柔光、T43 低對比度（三者同時出現必平） |
| 臉太黑，看不見五官 | 用了 T05 背光或 T04 側逆光卻沒有任何 fill | 一句 `white bounce from camera left placing the shadow side two stops under the key`；或把 T05 降級為 T04 | T42 暗色調（若同時存在）、T46 高對比降為中對比 |
| 看起來像手機自拍，不像電影 | 缺三樣：非眼平機位、非 1:1 光比、寬幅構圖 | T26 斜側視角 + T04 側逆光 + `2.39:1 framing` + `f/2 on a 40mm lens` + S06 單光源夜戲 | 均勻的正面光、4:3 或方形構圖、`everything evenly lit` |
| 顏色髒、發灰發泥 | 兩個以上色溫在同一區域打架，或飽和與去飽和指令並存 | 選定單一色溫並給 K 值；真要兩色 → 用 T41 雙性照明並指定交界 | 同時存在的 T06 暖光源與 T36 冷光源、同時存在的 T16 高飽和與 T45 低飽和 |
| 背景太亂、搶走主體 | 景深指令缺失，或用了 T22 深景深卻沒有背景控制 | T25 淺景深（`f/1.8, 85mm, background rendered as unresolved shape`）；或改用 T42 暗色調把背景壓進暗部 | T22 深景深、背景細節的描述詞 |
| 人物沒有重量感、像貼上去的 | 沒有接觸陰影，主體與地面／背景之間沒有光學連結 | `contact shadow pooling under the feet`、`the wall behind picking up spill from the key`、T22 深景深讓主體與環境同層 | T25 淺景深開太大、純色去背式背景 |
| 氣氛不夠、很空 | 光是「乾淨」的——空氣中沒有東西承載光 | T18 丁達爾光 或 S05 煙霧體積光，並明寫介質：`thin haze in the air`、`dust drifting through the beam` | T09 柔光（柔光在霧裡不成束）、T43 低對比度 |
| 看起來很假、很 AI | 通常是「多個無來源的 key light」+ 「完美對稱」+ 「零瑕疵表面」 | 把光收斂成單一有動機的來源（S06 單光源夜戲 / T08 窗光 / T11 自發光）；加 `one blown highlight left uncorrected`、`visible pores`、`slightly off-centre framing`、S18 十六毫米顆粒 | 並列的多個光位技法、`perfect`、`symmetrical`、任何無效堆砌詞 |
| 皮膚像塑膠、像磨皮過頭 | 模型預設的美膚偏誤，加上柔光沒有給紋理指令 | `visible skin texture, pores, fine lines, a few stray hairs`；加入 T47 硬光或側光讓紋理有陰影可依附 | T09 柔光 + T44 亮調 + T43 低對比度的三連組合（這組合天生消除紋理） |
| 太暗，主體被吞掉 | T42 暗色調用了但沒有指定「哪一塊必須保持亮」 | 明寫主體錨點：`only her face, hands and the lit edge held above the noise floor` | T37 弱光（與 T42 疊加會全黑）、多餘的 `shadow` 描述 |
| 光好像從四面八方來 | 提示詞裡並列了兩個以上的光位技法 | 只留一個 key，其餘改寫為 `rim` / `kick` / `bounce` 並註明比 key 暗幾級 | 並列的 T03／T05／T07／T27 中的多餘項 |
| 構圖無聊、像商品目錄 | 只有景別沒有視角，模型套用預設眼平正面 | T39 低角度視角 或 T17 高角度拍攝 或 T26 斜側視角，任選一個；或 T34 封閉構圖給畫面加框 | T35 居中構圖（若不是刻意要對稱）、預設的眼平正面 |
| 顏色很豔但很廉價 | T16 高飽和全域生效，所有顏色一起飽和 | 指定**單一主色**與它出現在哪個物件上，其餘 `held back to near-neutral`；或改用 S11 三色印片 / S12 柯達克羅姆這種有選擇性的色彩系統 | 全域的 `vivid colors`、`saturated`、`vibrant` |
| 有霧但看起來像蒙了一層灰 | 霧沒有被光穿透，只是均勻降低對比 | T47 硬光 + 明確的光束方向 + `the beam brightest where it enters the haze and falling off with distance` | T09 柔光、T43 低對比度、無方向的 `foggy` |
| 動作僵硬、像擺拍 | 缺少動態證據，模型畫出靜止的姿勢 | T24 動態模糊（給快門值 `1/15 second`）+ 動作的中間狀態描述：`mid-step, weight still on the back foot, coat still swinging` | `posing`、`standing still`、對稱的站姿描述 |
| 夜景像白天調成藍色 | 只寫了 T38 冷色調，沒寫夜晚的光學特徵 | T11 自發光（光必須來自畫面內的燈）+ T42 暗色調 + `sky rendered as true black with no gradient` + 光源周圍的衰減描述 | 單純的 T38 冷色調、`at night` 而無光源說明 |
| 產品看不出材質 | 光位錯了——材質只在特定光位下顯現 | 金屬／拉絲 → T03 側光 + T47 硬光；玻璃／液體 → T04 側逆光 + 明亮背景；布料／皮革 → T03 側光 + 掠射角 `raking at 80 degrees` | T27 正面光（會抹平所有材質）、T09 柔光單獨使用 |
| 生成的是插畫不是照片 | 提示詞裡有風格詞卻沒有攝影錨點 | 補上鏡頭與曝光參數（`f/2.8, 50mm, 1/125 second`）、載體（S18 十六毫米顆粒 / S12 柯達克羅姆）、以及具體的光源物理描述 | `illustration`、`art`、`render`、`concept` 等字眼，以及任何無效堆砌詞 |
| 加了風格包但看不出來 | 風格包被後面的技法抵銷了（見〈二、表 B〉） | 檢查是否誤加了與風格包衝突的軸；風格包的核心特徵要用一句具體技術描述展開，而不是只寫風格名 | 與風格包衝突的色彩／對比／景深指令 |

---

## 六、衝突檢查（三張表）

本章沿用本檔編號：`T01–T48` = 圖一攝影技法，`S01–S24` = 圖二影視風格。
軸名沿用 `SKILL.md` 的**十軸**模型（1 景別／2 鏡頭／3 相機高度／4 主體朝向／5 光位／6 光質／7 光源與色溫／8 影調與對比／9 色彩／10 景深與動態），影視風格是第 11 層。

> **本章取代〈二、互斥矩陣〉的表 A 與表 B。** 那兩張表只查同軸，而且有兩處與 `01-lighting.md`／`02-tone-color.md` 的軸向說明相牴觸（見本章表 B 附錄）。
> 〈二〉唯一仍然有效、且被本章引用的是〈二、T41 雙性照明的例外條款〉。〈五、除錯對照表〉最後一列指向「〈二、表 B〉」，請改讀本章表 B 與表 C。

**執行順序不可顛倒**，因為前一張表刪掉的項目會讓後一張表的檢查量變少：

| 順序 | 表 | 檢查什麼 | 不查會怎樣 |
|---|---|---|---|
| 1 | 表 C 風格包鎖定 | 有沒有選了風格包、又去指定它已經鎖死的軸 | 最致命也最常見。風格包被你自己加的技法整個抵銷，得到一張「有點像但說不出哪裡不對」的圖 |
| 2 | 表 A 同軸互斥 | 同一個軸有沒有塞了兩項 | 模型取中間值，兩邊的意圖同時消失 |
| 3 | 表 B 跨軸矛盾 | 分屬不同軸、但物理上不可能同時成立的組合 | 模型只能執行其中一項、另一項變成噪音，而且無法預測它會挑哪一項 |
| 4 | 表 B 附錄 | 你剛才刪掉的東西裡，有沒有其實合法的 | 過度刪除。把正交的兩個軸誤判成互斥，畫面會少掉本來該有的層次 |

**最大的破口是只查表 A。** 同軸衝突（「柔和的硬光」「明亮的暗調」）在寫的當下就看得出來；
真正會靜默失效的是表 B 與表 C —— 兩項技法各自合法、分屬不同軸，湊在一起卻在物理上互相取消，
而 agent 照「同一個軸只能出現一項」這條規則檢查會全部放行。

**第二大的破口是把「正交」誤判成「互斥」。** 光質不決定對比、光位不決定光質、飽和不決定銳度 ——
這三條在 `01-lighting.md`〈二、光質與強度〉的軸向說明與 `02-tone-color.md` 開頭的四概念表裡都寫死了。刪錯東西和留錯東西一樣傷。

每刪掉一項就重數一次技法總數，維持在 8 項以內。

---

### 表 A：同軸互斥（每軸只能留一項）

| # | 軸 | 互斥項（只能留一個） | 判準：該選哪一個 | 不佔這個軸的例外 |
|---|---|---|---|---|
| 1 | 景別 | T31 極端特寫 ↔ T32 特寫 ↔ T19 近景 ↔ T20 中景 ↔ T23 全身照 ↔ T21 遠景 | 由「觀眾必須讀到的最小資訊單位」反推：毛孔／虹膜／材質紋理 → T31（主體佔畫幅 90–100%）；眉毛與嘴角的微表情 → T32（臉佔畫幅高度 60–75%、切在鎖骨）；表情加肩線 → T19；手勢與上半身動作 → T20；姿態、服裝、全身重心 → T23；人與空間的比例關係 → T21（人佔畫幅高度不到 1/3） | 無。要同時要遠景資訊與特寫細節，出兩張圖 |
| 2 | 鏡頭 | 焦段只能有一個值；畫幅只能有一個值 | 焦段由「你要多少透視收斂」決定，不是由景別決定：要線條往中心暴衝、要體積放大 → 18–28mm，並同句寫 `no barrel distortion`；要背景壓縮、要輪廓落在乾淨底子上 → 85–135mm。人像不變形靠的是 1.2m 以上的工作距離而不是鏡頭本身（`03-framing.md` T32），所以「換長焦修鼻子」是錯的因果 | 無。不要寫「廣角的壓縮感」，也不要同時出現 `24mm` 與 `85mm`。焦段與景別是兩件事 —— 85mm 也能拍遠景，只是要退更遠 |
| 3 | 相機高度 | T33 鳥瞰（俯 75–90°）↔ T17 高角度拍攝（俯 15–45°）↔ 眼平（預設，不用寫）↔ T39 低角度視角（仰 15–45°） | 主體相對觀眾只有一個權力值：垂直維度塌陷、人物去人格化成色塊 → T33；觀察／敘事性俯視、仍讀得到五官 → T17；平等／紀實 → 眼平（省略不寫）；威嚴／體量／英雄 → T39 | 無。俯 45–75° 與仰 45–75° 是兩檔之間的過渡帶，72 項裡沒有編號，要用就直接寫死度數，不要疊兩個編號 |
| 4 | 主體朝向 | T30 四分之三側面（轉 30–45°）↔ T26 斜側視角（轉 45–70°）↔ T29 側面視角（轉 90°）↔ T28 背面視角（轉 180°） | 這是一條連續的旋轉軸，由「遠側那隻眼睛還剩多少」反推：兩眼完整可見、還有眼神接觸 → T30（人像預設值，寫死 35°）；遠眼被鼻樑壓掉一部分、眼神接觸已破裂 → T26（寫 55–65°，寫 45° 模型會退回 T30）；只剩單眼、臉從表情變成輪廓圖形 → T29；完全看不到臉、由肩線與視線向量敘事 → T28 | 無。**T26 佔這個軸**（`03-framing.md` T26 與 T30 互為衝突項），不要把它當成「相機站位」而與 T30／T29 並用。另外 T26／T29 需要 look room，不可與 T35 居中構圖 並存 |
| 5 | 光位 | T27 正面光（方位 0°）↔ T03 側光 ↔ T04 側逆光 ↔ T05 背光 ↔ T07 頂光 ↔ T13 底光 | 由「你要哪一塊是暗的」反推：不要暗部、要陰影藏在主體正後方 → T27；要臉的一半暗 → T03；要正面暗、輪廓亮但正面還讀得到細節 → T04；要正面全暗只剩形狀 → T05；要眼窩黑洞 → T07；要陰影方向反轉的非人感（鼻影往額頭爬）→ T13 | T10 髮絲光**不佔這個軸**：它加了 grid／snoot，只落在頭頂與飛散髮絲的鏡面高光上，不製造任何臉部陰影，因此任何主光位都能配（含 T27 —— 那正是三點打光的標準組合）。出力由髮色決定：深髮可比主光高 1–1.5 級，淺髮要壓到與主光相當或更低，否則髮絲糊成一片白。<br>T14 輪廓光**會佔這個軸**：它的定義性條件是「正面比輪廓暗 2–3 級」，等於把 key 降級成補光，與任何要求正面有立體感的光位打架 |
| 6 | 光質 | T09 柔光 ↔ T47 硬光；複合條目 T15 舞台光 ↔ T48 閃光燈 | 只看陰影邊緣過渡寬度：光源角直徑 >20°（1.2m 柔光箱放 1m 處約 62°、陰天近 180°）、邊緣在數公分到數十公分內漸變 → T09；角直徑 <5°（正午太陽 0.53°、遠距裸燈同理）、邊緣在數毫米內從全亮切到全暗 → T47 | T15／T18／T48 是把光位＋光質＋介質綁死的**複合條目**（見 `01-lighting.md`〈二〉軸向說明），它們取代光質欄而不是與之並列。<br>**T15 + T18 可以疊** —— 聚光燈切邊與 haze 顯形本來就是同一個做法的兩半（`01-lighting.md` T15 的〈強化〉明列 T18）。<br>**T48 與 T15／T18 互斥**：機頂同軸點光源做不出遠距切邊光束；而且同軸方向的散射角接近 180°（後向散射），直閃打進霧裡只會得到一層均勻白紗，不會出現光柱。<br>T47 與 T15／T18／T48 是同義強化，可留；T09 與這三者都不可並存 |
| 7 | 光源與色溫 | 全域色溫 T06 暖光源 ↔ T36 冷光源；發光物件 T08 窗光 ↔ T11 自發光 ↔ T12 火光（可以有主次，但 key 只能是其中一個） | 先決定 key 從**什麼物件**發出，色溫跟著那個物件走，不要另外再下一個全域色溫指令：窗 5000–5600K／家用鎢絲實用光 2700–3000K／鈉氣路燈約 2000K／火 1700–2000K／手機螢幕白點 6500–7500K。冷暖是**相對關係**，必須同時給拍攝白平衡當參照，否則 `7500K` 對模型只是裝飾字 | T41 雙性照明是唯一允許兩個色溫並存的情況，條件是把兩色指派到不同的**空間分區**。兩側亮度規則依配色而定：cyan／magenta 走**等亮**（立體感由色相差建立，重疊區是淡紫白而不是中性膚色，見 `01-lighting.md` T41）；amber／blue 這種真正的互補配置才需要指定 1–1.5 級的主副差（見〈二、T41 雙性照明的例外條款〉）。兩份說明不一致時以配色為準 |
| 8 | 影調與對比 | 四個子參數各留一項 —— 曝光：T02 過度曝光（獨立參數）；亮度重心：T44 亮調 ↔ T42 暗色調；動態範圍：T43 低對比度 ↔ T46 高對比；照度：T37 弱光 ↔ T40 強光 | 曝光看「高光要不要 clip 到 255」（要 → T02，並指名哪一塊過曝與 EV 量）；亮度重心看「面積最大的區域是亮的還是暗的」（T42 = 80–90% 面積落在 IRE 10 以下、小面積亮部曝光正確；T44 = 多數像素在 IRE 60–90 不觸頂、光比 2:1 甚至 1.5:1）；動態範圍看「黑位要不要抬到 IRE 8–15」（要 → T43，不要 → T46 壓到 0）；照度看實際 lux（1–10 lux 夜間內景 → T37；100,000 lux 正午或 10,000–20,000 lux 明亮陰天 → T40） | 四個子參數**不是自由組合**。不合法：T02+T44（一個要求觸頂、一個要求不觸頂）、T02+T43（白點必須壓在純白以下）、T42+T43（大面積不抬起的純黑 vs lifted blacks）、T37+T42（弱光是照度不足、暗色調要求亮部曝光正確；並列得到整張欠曝的灰片）。<br>合法：T42+T46、T44+T43、以及 T42 配**局部** T02（低調畫面裡開一扇過曝的窗是常規做法，衝突的只有「全域 +2 EV」這種下法） |
| 9 | 色彩 | 色相 T01 暖色調 ↔ T38 冷色調；飽和 T16 高飽和 ↔ T45 低飽和 | 色相必須與光源軸的色溫一致，不要兩個軸各下各的；飽和度由題材決定：商品／食物／霓虹 → T16，並指名哪些色相要飽和 + 同句寫 `skin kept at natural saturation`；紀實／情緒／高級感 → T45，並寫「飽和度降 X%、保留膚色與一個重點色」 | 色相與飽和是兩個子參數，T01+T45（低飽暖調）與 T38+T16（高飽冷調）都合法。desaturated／monochrome／black and white **三個詞不可互換**：monochrome 指「單一色相」（含 sepia、藍調），既不等於黑白也不等於低飽和，並列會直接拿到黑白照。想保留第二個色相 → 降格成局部點綴色，並指名它出現在哪個物件上 |
| 10 | 景深與動態 | 景深 T22 深景深 ↔ T25 淺景深；動態 T24 動態模糊 ↔ 凍結（預設，不用寫） | 景深看環境在敘事裡的角色：環境是內容 → T22（f/8–f/16 + 18–35mm，並逐層指名前／中／後各放什麼物件，只寫 `everything in focus` 會拿到清晰但空曠的背景）；環境是干擾 → T25（給 f 值、對焦點、以及從哪個部位開始脫焦）。要動態就必須給快門值（`1/15 second`）加上動作的中間狀態，只寫 motion blur 模型會畫出一個靜止的姿勢 | 景深與動態是兩個子參數，可並存。唯一的陷阱是 T24 + T48 閃光燈，只有 `rear-curtain sync, 1/15 second drag` 一種合法寫法 |

**三條補充**

- **構圖不在十軸上**：T34 封閉構圖與 T35 居中構圖可以同時成立（一個被門框夾住的居中主體，`03-framing.md` T34 的〈強化〉明列 T35）。它們的衝突是跨層的 —— T34 與 T31 極端特寫、S10 手持跟拍、S19 偽紀錄片互斥；T35 與 T26 斜側視角、T29 側面視角、T24 動態模糊互斥（三者都需要 look room 或畫外暗示）。
- **T02 不是 T44 的極端版**：它在曝光參數上，不在亮度重心子軸上。把它當成「更亮的亮調」會同時毀掉兩者 —— 正確關係見表 A 第 8 列的例外欄。
- **風格包只能選一個**：S01–S24 取其一，理由與覆寫額度見本章末〈覆寫規則〉。

---

### 表 B：跨軸矛盾（各自合法、湊起來物理上不成立）

| # | 組合 | 為什麼矛盾 | 該保留哪一項 |
|---|---|---|---|
| 1 | T44 亮調 + T46 高對比 | 亮調的定義是「多數像素落在 IRE 60–90 且不觸頂，靠大量白反光板把光比壓到 2:1 甚至 1.5:1」—— 它本身就是一種低光比狀態。高對比要求黑點壓到 IRE 0、白點推到 95–100、中間調過渡壓成很窄一條。同一條曲線不可能既只佔上半段、又橫跨全段 | 要輕盈潔淨 → 留 T44，對比改 T43 低對比度，並指定「最深的暗部在哪個物件下面」當唯一錨點。要張力 → 丟掉 T44，改成 T42 暗色調 + T46 |
| 2 | T42 暗色調 + T44 亮調 | 嚴格說同屬亮度重心子軸，但幾乎不會被寫成並列的兩個詞，而是偽裝成「明亮的暗調」「通透的低調」而漏檢。兩者指定重心位置，一個推右、一個推左，並列的結果是重心回到正中間 = 一張沒有影調個性的中間調 | 先回答「畫面裡面積最大的區域是亮的還是暗的」。亮 → T44。暗 → T42。想要「大面積暗 + 一小塊很亮」那不是亮調，是 T42 + T46 |
| 3 | T02 過度曝光 + T16 高飽和 | 飽和度來自 R／G／B 三通道之間的差值。曝光往上推時先到頂的通道被剪裁，三通道逐漸收斂到 255，差值消失 —— 過曝區必然是白的、無彩的。這是感光的數學結果，不是風格選擇 | 要刺眼夏日／回憶感 → 留 T02，色彩只保留在中間調與暗部的物件上，明寫 `colour held only in the midtones, the blown areas going pure white`。要濃色 → 刪掉 T02，曝光壓低 1/3–2/3 EV 讓色彩不被高光洗淡 |
| 4 | T43 低對比度 + T16 高飽和 | 低對比的實作是 lifted blacks／faded print／Black Pro-Mist 這一類 matte 質地，而它們抬黑位的機制就是「用散射的白光稀釋暗部」—— 稀釋的同時色度一起被拉向中性軸。matte 質地在物理上就會壓低色度 | 要 matte 質感 → 留 T43，飽和度改 T45 低飽和，只保留一個重點色。要濃色 → 刪掉 T43，改 T46 高對比（`02-tone-color.md` T16 的〈強化〉明列 T46） |
| 5 | T02 過度曝光 + T43 低對比度 | T43 要求白點 roll off 在 IRE 85–90、絕不觸頂；T02 要求高光 clip 到純白且細節不可逆喪失。兩者對「白點落在哪」下的是直接相反的指令 | 要褪色回憶感 → 留 T43，並把「亮」交給亮度重心（T44）而不是曝光。要真的洗掉 → 留 T02，對比改 T46 或不指定 |
| 6 | T37 弱光 + T22 深景深 | 1–10 lux 的場景要維持正確曝光只有三條路：開大光圈（與深景深相反）、放慢快門（動態就糊）、拉高 ISO（暗部長噪點）。以 3 lux 為例，f/1.4、1/50s、ISO 6400 才勉強站上正確曝光 —— f/11 + 手持 + 夜晚在物理上不成立，模型會給你「全景清晰卻乾淨明亮的假夜景」 | 兩者都要 → 必須補上成因，三選一寫進提示詞：`tripod, four second exposure`／`ISO 6400 with visible luminance noise`／`the scene lit by one very bright practical`。不補成因就刪掉 T22 |
| 7 | T37 弱光 + T16 高飽和 | 低照度下訊噪比下降，色度訊號最先被雜訊與機內降噪抹掉；ISO 6400 以上還伴隨動態範圍壓縮。要求「很暗又很豔」，模型只能靠整體提亮來滿足飽和度，交回一張偽夜景 | 留 T37。飽和度只留給**自發光源本身**（招牌、螢幕、火），環境與膚色維持近中性：`saturation carried entirely by the light sources, everything they illuminate staying near-neutral` |
| 8 | T45 低飽和 + T11 自發光 / T15 舞台光 | 這不是物理矛盾而是**意圖矛盾**，但後果一樣致命：有色光源存在的全部意義就是它的顏色（霓虹、螢幕、gel 過的聚光燈），全域去彩等於把那盞燈白打。模型會兩邊各讓一步，交回一張「顏色很淡的夜店」 | 留光源。飽和度改成分區指令：光源與它照到的第一層物件維持高彩，其餘 `held back to near-neutral`。真的要全域低彩 → 光源改成無色的 T08 窗光或 T36 冷光源 |
| 9 | T11 自發光 / T12 火光 + T40 強光 | 這兩項的成立條件是「發光物件本身必須是畫面裡最亮的東西 + 陡峭的平方反比衰減 + 照不到的地方直接沉黑」，實拍在 f/1.4、ISO 1600–3200 的區間。T40 指的是 100,000 lux 級的照度。並列會讓模型把畫面整體提亮，自發光源不再是最亮的東西，光源動機整個消失 | 留 T11／T12，並主動把衰減與照明半徑寫進去：`falling off to nothing two metres out`，讓亮度落差本身變成賣點 |
| 10 | T11 自發光 + T44 亮調 | 同上的另一半：亮調要求靠大面積反射把暗部墊到 1.5:1–2:1，那等於把「照不到的地方」全部填亮。實用光的可讀性完全建立在它周圍有東西是暗的 | 留 T44 → 光源改成 T08 窗光（大面積、低反差、不需要衰減當賣點）。留 T11 → 影調改 T42 暗色調 |
| 11 | T21 遠景 + T25 淺景深 | 遠景時主體距離遠、放大率低，同一個光圈下景深急遽變深；而且遠景存在的理由就是交代環境，淺景深把環境刪掉，兩者功能自相抵銷 | 要環境資訊 → T21 + T22 深景深。要「遠但有壓縮與分離」→ 改寫成 `200mm telephoto compression at f/4, the far background compressed into unresolved bands`，不要寫 f/1.4 |
| 12 | T21 遠景 + T10 髮絲光 | 遠景裡人物佔畫幅高度不到 1/3，extreme long shot 可低到 1/10 以下。人物低於約 1/4 畫幅高時，髮絲光那條亮邊在 1024px 的輸出上不到 3 個像素 —— 它不會出錯，只會被無聲丟棄，同時稀釋其他指令的權重 | 留 T21。分離改用大面積明度／色相對比：`the figure reading as the only bright shape against a uniformly dark street`。髮絲光留給 T19 近景以上的景別 |
| 13 | T33 鳥瞰 + T10 髮絲光 | 髮絲光的作用是在**輪廓線**上鑲一條亮邊，而輪廓線只在側視或接近側視時存在。從正上方看，頭髮的頂面就是相機看到的主受光面，光打上去只是把它照亮，沒有邊可鑲 | 留 T33。分離改靠投影：`a long shadow cast across the floor separating the figure from the ground`（投影長短由**光源仰角**決定、與相機無關，所以要另外指定光位）。要髮絲光 → 相機降到 T17 高角度拍攝以下 |
| 14 | T33 鳥瞰 + T25 淺景深 | 從 75–90° 俯視時，地面與感光面平行、面上各點到鏡頭幾乎等距，景深因此失去分離主體的能力，光圈只剩曝光作用。強行寫淺景深只會得到假的移軸微縮玩具效果 | 留 T33 + T22 深景深。真的要那個玩具感 → 明寫 `tilt-shift miniature effect with a single horizontal band of focus across the middle`，那是另一種東西，要有意識地選 |
| 15 | T33 鳥瞰 + T05 背光 / T04 側逆光 | 「背光」定義為光源在主體後方、朝相機方向照。相機在正上方時，主體後方＝主體下方，這要求光從地板底下射出來，幾何上不成立 | 留 T33。俯視只有兩種可用光位：T07 頂光（與相機同軸，等效順光，會壓平）或 T03 側光（掠過地面拉出長投影，這是俯視唯一有效的立體來源）。要逆光輪廓 → 相機降到 T17 或眼平。**唯一例外**是主體躺在發光面上（燈箱、雪地、水面反射），此時必須明寫那個反射面 |
| 16 | 放大率 ≥ 1:4 的近攝 + T22 深景深 | 景深隨放大率遞減：1:1 放大率下即使收到 f/16，景深也只剩約 2 公釐（T31 極端特寫的工作區間是 1:3–1:1）。「整顆眼球連睫毛都清楚」在單張曝光裡做不到 | 兩者都要 → 唯一解是明寫 `focus-stacked`（見〈四、配方 3〉與 S20 定格動畫質感的做法）。不寫 focus stacking 就刪掉 T22，並指定唯一的合焦平面：`focus on the iris, the eyelashes already falling soft`。**注意判準是放大率不是景別名稱**：T32 特寫在 1.2–1.9m 的正常工作距離上放大率只有 1:15 左右，f/8–f/11 的景深綽綽有餘，不算衝突 |
| 17 | T05 背光 + T27 正面光 | 嚴格說同屬光位軸，但幾乎不會被寫成並列的兩個名詞，而是偽裝成「背光，臉再補亮一點」—— 那句補光就是第二盞 key。兩個等亮的 key 從前後夾擊，主體會失去所有方向性，變成無源的環境光，這是「假／AI 感」的最大單一成因 | 留 T05。臉要有細節就把補光**降格**並寫明比例：`a white bounce from camera position placing the front of the face two stops under the rim`。差距在 2 級以內就會退化成正面光 |
| 18 | T48 閃光燈 + T09 柔光 | 直閃美學的成立條件是「極小的光源 + 貼在鏡頭軸線上 + 平方反比造成的背景急速衰減」，產出硬邊影子、壓平的正面、黑掉的背景。加柔光等於把它換成柔光箱，那已經是另一種語彙 | 要 snapshot／派對／狗仔感 → 留 T48，接受硬邊與背景黑洞：`on-camera flash, hard-edged shadow behind the shoulder, background falling to black two metres out`。要商業人像 → T09 並寫 softbox，整段不要出現 flash |
| 19 | T48 閃光燈 + T25 淺景深 | 直閃最強的辨識線索是「主體正後方牆上那道硬邊落影」。淺景深把那面牆糊掉，落影跟著消失；剩下的平方反比衰減與散景在「分離主體」這件事上做同一份工作，讀者只會把它讀成一張普通的夜間人像 | 留 T48 + T22 深景深，讓落影與背景衰減同時可讀。要散景人像 → 改用連續光，刪掉 flash |
| 20 | T18 丁達爾光 + T27 正面光 | 光柱要看得見需要前向散射，也就是以被攝體為頂點時，相機方向與光源方向的夾角必須大於 90°（逆光或側逆光位）。光源與相機同側時散射的光背離鏡頭，煙霧只會變成一層均勻灰紗（S05 煙霧體積光的常見錯誤就是這一條） | 要光束 → 光位改 T04 側逆光或 T05 背光（水平角 110–150°），並補齊另外三個條件：介質 `thin haze in the air`、切出光束幾何的遮擋物、以及**光柱背後要有暗背景**（打在亮牆或亮天空上的光柱等於不存在）。要正面光 → 刪掉光束，霧只當作抬黑位用 |
| 21 | T13 底光 + T08 窗光 | 底光要求光源低於下巴、以 -30°～-45° 往上照。窗戶下緣在建築上通常在腰部以上，窗光的入射方向幾乎都是水平到略高於視線，並列等於要求一扇裝在地板下的窗，模型會退回成普通側光 | 要底光的非人感 → 光源改 T12 火光或 T11 自發光（地面燈條、平放的螢幕），色溫跟著那個物件走。**唯一的窗光解**是讓窗光打在淺色地板或水面上反彈，此時必須明寫那個反射面：`daylight bouncing up off a pale floor`。要一般窗光 → 光位只能是 T03／T04／T27 |
| 22 | T41 雙性照明 + T27 正面光 | 雙性照明的機制是把兩個色相指派到不同的**空間分區**，交界線是它唯一的賣點；水平角必須各約 90°，兩色交界才會落在鼻樑上。正面光從鏡頭軸線均勻涵蓋整張臉，沒有分區可指派，兩色回到同一塊像素上加色混成偏藍紫的淡白 | 留 T41，光位改成雙側（左右各一，各約 90°），並寫滿三件事：哪一側是哪個色相、交界落在臉上的哪一條線、重疊區是什麼顏色。若改用 amber／blue 這種真正的互補配置，還要補上 1–1.5 級的主副差 |
| 23 | T10 髮絲光 + T44 亮調 | 髮絲光靠的是「亮邊 vs 更暗的背景」這個局部反差。亮調把背景抬到與主體同亮或更亮，亮邊沒有對照物，等於白打一盞燈 | 判準是**背景與頭髮的明度差**：背景比臉亮 1 級以內、且是深色頭髮 → 還讀得到，寫成鏡面光澤而不是亮邊（`a hard light from behind camera right putting a specular sheen along her dark hair`，〈四、配方 1〉就是這個邊界案例：淺灰背景只比臉亮 1 級）。背景推到近白或髮色淺 → 直接刪掉 T10，分離交給背景的明度梯度 |
| 24 | T14 輪廓光 + T44 亮調 / T43 低對比度 | 比上一列更硬的衝突：輪廓光的**定義性條件**是「正面比輪廓暗 2–3 級」。亮調要求光比 2:1 以內、低對比要求黑位抬到 IRE 8–15，兩者都直接否定那 2–3 級的落差。留著只會得到一張正面被打亮的普通人像 | 二選一，沒有中間解。要輪廓主導 → 留 T14，影調改 T42 暗色調 + T46 高對比，並寫 `near-black set behind`。要亮調／低對比 → 刪掉 T14，分離改用 T10 髮絲光（見上一列的明度差判準）或背景明度梯度 |
| 25 | T28 背面視角 + T31 極端特寫 / 任何微表情需求 | 背面視角沒有臉：眼神光、微表情、視線方向全部落空，而極端特寫的全部價值就是那些東西。模型的折衷做法是偷偷把頭轉回四分之三側臉，兩個指令一起失效 | 留 T28，情緒改由肢體承擔，並明寫肩線、手的位置、頭的傾角、以及**他在看什麼**（沒有指定對象，背影會被擺在空無一物的背景前，敘事向量整個消失）。要微表情 → 朝向改 T30 |

#### 表 B 附錄：看起來像矛盾、其實合法（不要刪）

這七組是最常被誤刪的。它們之所以看起來衝突，是因為把兩條**正交**的軸誤當成同一條。

| 組合 | 為什麼合法 | 寫的時候要補什麼 |
|---|---|---|
| T47 硬光 + T43 低對比度 | 光質決定陰影**邊緣寬度**，對比決定**黑白位**，兩者互不推導。霧中的硬陽光配 lifted blacks 完全成立，S15 沙塵單色整包就建立在這上面 | 必須寫出把黑位抬起來的物理成因，否則模型交回「邊緣很硬、整體發灰」的不自然結果：`heavy atmospheric haze lifting the shadows`，或 `a large white bounce filling the shadow side to within one stop`。<br>注意 `01-lighting.md` T47 的〈衝突〉欄仍把 T43 列為互斥，那一列與同檔〈二〉的軸向說明及 `02-tone-color.md` T43 相牴觸，**以後兩者為準** |
| T09 柔光 + T46 高對比 / T42 暗色調 | 同上。柔光只保證陰影邊緣是漸變的，光比可以打到 8:1。大柔光源 + 拿掉補光 + 深色背景 = 柔邊但高對比的低調人像，是標準做法 | 光比與受光面積比例要另外寫死：`16:1 key-to-fill, no bounce, roughly 85 percent of the frame in unlifted black` |
| T47 硬光 + T44 亮調 | 定義高調的是光比與亮度重心，不是光源大小。硬光配大量白色反射環境一樣能壓到 1.5:1 | 必須寫出那個反射環境：`white cyclorama with light bouncing back from all sides` |
| T42 暗色調 + T02 過度曝光（局部） | 低調畫面裡開一扇過曝的窗、或一盞爆掉的燈，是常規做法。衝突的只有「全域 +2 EV」這種下法 | 指名過曝發生在哪一塊物件上，並聲明其餘部分曝光正確：`the window clipped to pure white, everything else correctly exposed` |
| T10 髮絲光 + T27 正面光 | 髮絲光不佔光位軸，加了 grid 之後只落在頭頂，不製造臉部陰影。這正是三點打光與美妝打光的標準組合 | 分開寫兩件事：主光的方位與陰影落點；髮絲光的光源面積小、加 grid、高光只限頭頂與飛散髮絲 |
| T17 高角度拍攝 + T13 底光 | 光位與相機高度是不同軸，俯拍配底光完全可行（恐怖片標準組合），只是情緒會從「弱化」翻成「威脅」 | 明寫陰影往上投、鼻影落在額頭，避免模型把底光讀成一般低調 |
| T40 強光 + T09 柔光 + T43 低對比度 | 強光講的是照度（明亮陰天 10,000–20,000 lux 依然是強光），與光質、對比都正交。這三者疊起來就是「明亮陰天」 | 明寫光源本體：`bright overcast, an entire grey sky as one source, flat 2:1 contrast` |

---

### 表 C：風格包鎖定表

「已鎖死」欄的軸不可再指定 —— 在那些軸上加任何技法都不是覆寫，是**取消**該風格。
標「二擇一」的欄位是風格包內建的分歧，選其中一支不算用掉覆寫額度。
「可覆寫」欄是你唯一能動的地方，而且最多動 2 軸（見〈覆寫規則〉）。

| 風格 | 已鎖死哪幾軸（不可再指定） | 剩哪幾軸可覆寫 | 覆寫時的注意事項 |
|---|---|---|---|
| S01 德國表現主義 | 光位（60–90° 正側、僅高於頭頂 10–30°，光越低影子越長）／光質（裸燈硬光 + gobo 斜影）／影調與對比（16:1 以上、黑位截止）／色彩（原生黑白，色彩軸整個失效）／景深（f/5.6–8）／相機高度（**二擇一**：低於腰位仰拍 或 高處俯視，可加 5–15° Dutch） | 景別（T21 遠景 ↔ T20 中景）、主體朝向、鏡頭（24–35mm 內可調） | 加 T01／T16／T38／T45 全是空指令；加 T09／T43／T44／T27 直接取消（原檔〈衝突〉明列）。景別可從遠景推到中景，但主角是**牆上的斜影不是人** —— 斜影必須佔畫面 50% 以上，所以推到 T32 特寫等於取消。鏡頭不可換長焦：貼近主體放大透視變形是這個包的一部分 |
| S02 義式驚悚紅綠光 | 光位（±90–120° 雙側交叉）／光質（硬光不擴散）／光源與色溫（原色紅、原色綠色片；色溫概念失效，改用主波長 630nm／525nm）／色彩（單通道逼近剪裁的極高飽和，暗部是深紅深綠不是中性黑）／影調（環境壓到近全黑）／鏡頭（40–58mm，避開廣角變形帶來的喜劇感） | 景別、相機高度、景深（f/2–2.8 內；主體必須貼牆、與牆落在同一焦平面） | 加 T45／T09／T27／T43 = 取消（原檔〈衝突〉明列）。T41 雙性照明不算覆寫，原檔〈可組合〉明列 —— 但沿用的是它的**分區機制**而不是 cyan／magenta 配色，這裡的兩色是原色紅與原色綠。重疊帶必須壓到最窄並明寫 `no yellow blend`，否則加法混色會給你一片髒黃 |
| S03 北歐冷冽 | 光位（0–20° 近正面）／光質（整面牆大小的柔光、近無影）／光源與色溫（5600–6500K，白平衡刻意設低到約 5000K 才會偏冷偏綠）／影調（1.5:1、黑位抬高成深灰）／色彩（低飽和 -25 至 -40，灰綠米白）／景深（f/8–11）／相機高度（120–140cm、水平垂直校準）／主體朝向（正面、站在中軸上） | 景別，而且只能在 T21 遠景 ↔ T23 全身照 之間移動 | **覆寫空間最小的包，只有 1 軸。** 人物必須佔畫面高度不到一半 —— 換成 T20 中景以上就失去「人與空曠空間一樣蒼白」的機制 = 取消。加 T03／T47／T25／T01 全部是取消（原檔〈衝突〉明列）。想把人從背景拉出來的任何分離光都是取消 |
| S04 魔幻時刻 | 光位（太陽仰角 0–6°、位在主體後方 150–170°，等於 T05／T04）／光源與色溫（直射 2000–3200K + 天光約 10000K 的天然冷暖分離）／影調（逆光造成的整體對比下降、高光柔滾降）／色彩（暖高光配冷藍陰影的 split-tone）／景深（f/1.8–2.8） | 景別（T19 近景 ↔ T20 中景）、主體朝向、鏡頭（35–85mm 內） | 加 T27／T07／T36／T22 = 取消（原檔〈衝突〉明列）。主體朝向可自由改（太陽在主體後方，朝向不影響光位），但**相機高度不可升到 T17／T33** —— 俯視會把地平線與天空推出畫面，冷藍補光的來源就沒了。想「補亮臉」只能用白反光板且明寫低於主光 2 級；補過頭冷藍陰影一消失，整包退化成一層橘色濾鏡 |
| S05 煙霧體積光 | 光位（110–150° 逆側、40–60° 仰）／光質（超強遠距硬光 + 油霧介質）／影調（高對比但黑位被散射抬起，主體低於光柱 3 級）／色彩（近單色、飽和約 -30）／景別（人物佔畫面高度不超過 1/3）／光源與色溫（**二擇一**：5600K 冷白 或 3200K 暖白，不混色） | 相機高度、景深（f/2.8–4 內）、鏡頭（35–50mm 內） | 加 T09／T27／T16／T44 = 取消（原檔〈衝突〉明列）。煙給太滿等於沒有光柱 —— 提示詞要寫 `separate hard-edged shafts with clear dark gaps between them`，不要只寫 `foggy`。機位若抬高到胸位以上，光柱的高度感會塌掉，這是覆寫相機高度時的唯一限制 |
| S06 單光源夜戲 | 光位（入鏡實用光在側後 120–150°、高於頭頂）／光源與色溫（畫面內可見的單一實用光，鈉氣 2000K 對遠景 4000–5000K，混色不校正）／影調（暗面低 3–4 級、黑位不壓死，遠處燈點細節必須留住）／色彩（陰影 teal、高光琥珀、中低飽和）／景深（f/1.4–2，主體與背景留 30m 以上實距） | 景別、相機高度、主體朝向 | 加 T27／T22／T44／T48 = 取消（原檔〈衝突〉明列）。最常見的隱形覆寫是一句 `soft fill on his face` —— 這個包的張力全部來自「臉的另一半真的沉進黑裡」。噪點必須寫成 `high-ISO digital noise`，寫成底片顆粒就變成 S18 |
| S07 單點透視對稱 | 相機高度（100–120cm、零傾斜零旋轉零橫移）／主體朝向與構圖（光軸正對空間中軸、消失點在正中、嚴格左右鏡像）／光位（80–90° 對稱吸頂燈）／景深（f/5.6–11）／景別（人物佔畫面高度不到 1/5）／鏡頭（18–28mm 且必須直線畸變修正良好） | 光質（燈罩的擴散程度，但不可大到消滅頭頂的垂直落影）、光源與色溫（**二擇一**：3200K 或 4300K）、色彩（色盤可換，但必須收斂到 1–2 個主色） | 加 T26／T33／T25／T03 = 取消（原檔〈衝突〉明列）。消失點偏離畫面正中心幾公分，整包就垮成一張普通走廊快照，所以提示詞必須包含 `zero tilt, no roll, no barrel distortion`。地毯花紋與壁紙紋理是透視的刻度尺，不可用淺景深糊掉 |
| S08 平面正面構圖 | 相機高度（主體臉部高度正中）／主體朝向（正面直視、置中對稱）／光位（T27 正面 0°、垂直角僅高於鏡頭 10–15°）／光質（極柔、主暗比 2:1 內）／景深（f/5.6–8）／影調（中對比、黑位微抬）／鏡頭（等效 27–40mm，直線必須筆直） | 景別（中景 ↔ 全身可換）、光源與色溫（3200–4000K 內可調）、色彩（色盤可換） | 色盤可換但**飽和度不可換** —— pastel 的定義是高明度加中低飽和，加 T16 高飽和等於取消。加 T26／T25／T03／T47 也都是取消（原檔〈衝突〉明列）：這個包的全部效果來自平面性，一出現縱深就變成普通室內照。注意平面感來自「光軸與背景牆呈 90° + 正面平光」，不是靠焦段換來的 |
| S09 固定長鏡頭 | 相機高度（三腳架鎖死在坐姿眼平 110–120cm）／景深與動態（f/4–5.6 深景深、機位完全不動）／光源與色溫（現場窗光 5000–5600K + 家用鎢絲 2700–3000K 混色、完全不校正，光比 4:1–6:1）／色彩（低飽和 15–20%、色偏不修）／景別（人物佔畫面高度 1/4–1/3 且偏離中心）／鏡頭（35–50mm） | 主體朝向、光位（窗開在哪一側可選）、影調（中等對比，暗部深度可微調） | 加 T25／任何電影燈／反光板／T10 髮絲光 = 取消。與 S10 手持跟拍在運鏡上直接互斥，不可並存。生**靜態圖**時這個包只剩「深景深 + 混色不校正 + 人小偏心 + 門框畫中畫」四個特徵，時間感與走位在單張圖上無效 —— 需要那兩者就得出影片 |
| S10 手持跟拍 | 相機高度（肩高 150–165cm、距主體 0.8–1.5m）／主體朝向（背面或側後，後腦或側頸佔畫面 1/3 並被上緣切掉）／光源與色溫（100% available light、混色不統一）／景深與動態（f/2.8–4、1/48 快門拖影、跟焦慢半拍）／色彩（去飽和中性紀錄片調）／鏡頭（25–35mm 略帶變形） | 光位（現場光從哪一側來）、光質、影調（臉可掉 2–3 級，深度可調） | 加 T35 居中構圖／T22 深景深／棚燈柔光 = 取消。主體前方不留視線空間、鏡頭永遠慢半拍是辨識點，改成完整平衡的構圖等於取消。手持要寫成「行走的低頻起伏 + 構圖的細微追補」，寫成劇烈抖動只會被讀成業餘素材。與 S09 互斥 |
| S11 三色印片 | 色彩（紅綠藍極飽和且不互染、暗部偏青、亮部暖奶油、套準偏移彩邊）／影調（超高照度、光比 2:1 甚至 1.5:1、臉上不存在純黑）／光質（硬主光 + 極強補光 + 每人一盞硬髮絲光）／光位（30–45° 水平、20–30° 仰）／光源與色溫（5500K 碳弧）／景深（f/2.3–3.5）／畫幅（1.37:1 Academy）／鏡頭（35–50mm） | 景別（全身／七分身 ↔ 中景）、相機高度（眼平或略低）、主體朝向 | 加 T45 低飽和 = 取消（〈技法核心〉的「純淨原色」直接被否定）；加 T42 暗色調或任何現代式壓黑 = 取消，「幾乎沒有純黑」正是這個載體的胎記。T10 髮絲光在這裡是必需品不是可選項，不要當成可省略的覆寫刪掉。景別不可推到全身以外太遠：75mm 在 1.37:1 上已是長焦，拍不了舞台化調度 |
| S12 柯達克羅姆 | 光源與色溫（太陽 5000–5500K、完全不補光、暗部只靠藍天而偏冷偏濃）／光位（順光或 45° 側前光）／光質（直射硬光）／影調（曝光鎖亮部、高光硬切無滾降、暗部堵死，寬容度只有約 5 級）／色彩（紅橙強勢、綠壓成橄欖、藍偏深）／景深（f/11 配 1/125，ISO 64 的 sunny 16 組合） | 景別、相機高度、主體朝向 | 加粗顆粒 = 取消（這個載體幾乎無顆粒，加了就變成 S18）。加 T09／T43／T45 = 取消。整包只有約 5 級寬容度，任何「暗部也要看得見」的要求都在覆寫影調軸。要開到 f/8 只有薄雲或側逆光一種說得通的理由，要寫出來 |
| S13 港片霓虹 | 光源與色溫（霓虹與店鋪實用光為唯一主光，2700K 鎢絲與 4200K 偏綠日光燈同框，有色光直接污染膚色、不補白光）／色彩（洋紅、青、翡翠綠、琥珀四色極飽和，黑位被色光污染而不純）／景深與動態（85–135mm、f/1.4–2、step printing 的頓挫拖影，與單純慢快門不同）／光質（實用光本身，不加擴散）／影調（黑位壓死）／光位（**二擇一**：(a) 兩色分邊、光比 1:1、鼻梁中線留暗帶，或 (b) 只有單側被招牌照到、另半邊沉 3 級以上） | 景別、相機高度、主體朝向 | 兩種光位混用 = 取消。加 T45／T22／任何白光補臉 = 取消（一補白光就退化成商業廣告打光）。前景遮蔽（玻璃、鐵窗花、路人）與濕地面的第二層反射是這個包的基礎設施，不要為了「乾淨」刪掉 |
| S14 數位早期 | 景深與動態（1/4 吋 CCD 全景深、完全沒有散景）／影調（AE 呼吸、亮部硬切、黑位被電子增益抬起）／光源與色溫（AWB 在 3200K 與 5600K 之間漂移、常偏綠）／色彩（4:1:1 色度水平糊邊、青綠暗部、機內銳化白邊、DCT 塊狀瑕疵）／景別與鏡頭（1/4 吋 CCD 裁切約 10.8×，等效 48mm 起跳，廣角端一點都不廣）／畫幅（4:3，或機內裁切的假 16:9） | 相機高度、主體朝向、光位（現場光 或 機頂燈） | 加 T25 淺景深 = 取消，小感光元件在物理上做不出來，而這正是辨識點。想拍大場面也不行 —— 「退無可退還是拍不進去」是這個載體的胎記，要廣角就得換包。要求乾淨畫質 = 取消 |
| S15 沙塵單色 | 光質（懸浮介質當擴散器、沒有硬輪廓光）／影調（2:1 以內、黑位被霧抬起發灰）／色彩（**二擇一**的單一色相：琥珀橙 或 石板藍灰）／光源與色溫（跟色彩連動：2000–2500K 或 6500K）／景深（f/4–5.6，前後分離交給空氣透視）／景別（人物佔畫面高度 3–8%）／相機高度（**二擇一**：貼地 或 俯視地貌） | 主體朝向、鏡頭（21–40mm 變形寬銀幕內可調） | 加 T10 髮絲光／T14 輪廓光 = 取消（背光被介質打散後只留柔化的剪影邊緣，不可能出現銳利亮邊）。加 T46 高對比／T16 高飽和 = 取消。只調色相而不寫介質 = 只是蓋了一張色片，這個包的物理基礎是懸浮粒子。人物一旦大過畫面高度 8%，尺度落差就沒了 |
| S16 黑白默片 | 色彩（原生黑白 + 正色片響應：紅→黑、藍→白且雲層不分離）／影調（8:1 以上、大面積純黑、約 ±1/3 級曝光跳動）／光質（硬弧光無擴散、刀口投影）／光位（45–60° 仰角 + 硬邊輪廓光、完全無補光燈）／景深（f/4–5.6）／相機高度（三腳架鎖定、眼平或略低）／景別（全身或七分身居中、舞台化正面調度）／畫幅（1.33:1 默片全片幅，不是 1.37:1 Academy） | 主體朝向（僅能在正面調度的範圍內微調）；整場印片染色（琥珀 或 藍的單色 tinting，這是唯一合法的顏色指令） | 加 T01／T16／T38／T45 全是空指令，只會讓模型猶豫要不要上色 —— 選了這個包就把色彩槽整個刪掉，改寫明度分離：`red lips going black, blue sky going white with no cloud separation`。加 T09／T43／T44／T27 = 取消。直接把彩色去飽和也是取消，正色片的關鍵是光譜響應錯位而不是去彩 |
| S17 VHS 錄影帶 | 光位（機頂燈沿鏡頭軸線正面直打）／光質（單一小硬光、完全無補光）／光源與色溫（3200K 鎢絲攝影燈 + AWB 在暖橘與偏綠之間漂移）／影調（近端過曝剪裁、2 公尺外全黑、黑位灰霧）／色彩（紅與洋紅色度向右拖尾、可見掃描線、dropout 白色短橫線）／景深（1/2 吋成像面的天然深景深）／景別與鏡頭（裁切約 5.4×，等效 45mm 起跳）／畫幅（4:3） | 相機高度、主體朝向 | 只有 2 軸可動。三個缺一不可的辨識點：4:3、色度滲流、底部約 2% 高度的 head-switching 撕裂帶。任何「乾淨的光」或「講究的構圖」都在取消它。要 16:9 只能是機內裁切的假寬幅（上下加黑邊），不是變形寬銀幕。景別靠變焦而不是走位改變，這也要寫進去 |
| S18 十六毫米顆粒 | 光源與色溫（窗光約 5600K + 室內鎢絲實用光 2800–3000K 混色，以日光平衡而不強行統一）／影調（欠曝推一級、臉低於窗 2 級、窗過曝 2–3 級帶柔性 rolloff、暗面約 1:4）／色彩與質感（自然飽和、中間調顆粒會蠕動、紅橘 halation、gate weave）／景深與動態（T2–2.8、1/48 拖影、手動跟焦看得見失誤）／相機高度（肩高、略低於眼平）／畫幅（1.66:1 或裁 1.78:1） | 景別、主體朝向、光位（窗開在哪一側） | T09 柔光可以疊（窗光本身就是大面積柔光，原檔〈常見錯誤〉明講），衝突的是**光量**：顆粒來自照度不足與推感光，加 T40 強光或補足照度＝顆粒消失＝取消。加 T22 的 f/11 深景深同樣是取消，那個光量這個包沒有。也不要期待奶油散景，Super 16 片幅小，T2 的背景仍然相對收斂 |
| S19 偽紀錄片 | 光位與光源（全 diegetic：機頂 LED 5500–6500K 或角色手上的手電筒，光軸隨機身擺動）／影調（中央過曝、3 公尺外只剩噪點黑、AE 抽動）／景深與動態（超廣角深景深、rolling shutter 斜切、自動對焦反覆搜尋）／相機高度（腰際到臉部劇烈變動）／景別與鏡頭（14–24mm 等效超廣角、f/1.8–2.8、ISO 6400 以上） | 主體朝向、色彩（**二擇一**：高 ISO 彩色噪點 ↔ 夜視單色綠加瞳孔反光） | 加 T25 淺景深／T35 居中構圖／任何無來源的臉部補光／第三人稱機位或正反打 = 不只是取消風格，是整個前提垮掉。這個包的每一個「缺陷」都必須在故事世界內部說得通：誰在拿這台機器、為什麼還在拍 |
| S20 定格動畫質感 | 景深與動態（f/8–16、focus stacking、**絕無動態模糊**、輪廓逐格微抖、每格 1–2% 曝光跳動）／光質（小尺寸硬主光 + 小白卡 1:4 補光；燈要拉遠或用光纖逼近平行光，以壓制縮尺下的平方反比衰減）／相機高度（偶的眼睛高度）／光源與色溫（2700K 迷你實用光入鏡）／鏡頭（24–50mm 微距，距 1:6 的偶 20–40cm；不要做等效換算，縮尺改變的是景深不是透視） | 景別（寬鏡 staging 與 T32 特寫是**交替使用**，兩者都合法）、主體朝向、色彩（色盤可換）、光位 | 加 T24 動態模糊 = 取消，除非明寫 `go-motion streaking`。只寫 stop-motion style 會得到光滑的 3D 塑膠感 —— 必須指名材質與縮尺：毛氈纖維、黏土指紋、替換頭的分模線、1:6 縮尺。材質特寫不是可有可無的補充，「實物」的證據就在那裡成立 |
| S21 賽博龐克街景 | 光源與色溫（畫面內霓虹與 LED 招牌為唯一主光，2000K 琥珀對 9000K 青藍，完全沒有天光）／光位（側上方灑髮際與肩線 + 穿透雨霧的強力背光，臉部正面幾乎不打燈）／影調（8:1，黑位壓低但仍保留青與洋紅的色相）／色彩（青與洋紅分離、**膚色維持近中性**）／景深（2x anamorphic、T2.8、橢圓散景、水平藍色條狀耀光）／相機高度（胸口或膝蓋高度略仰）／鏡頭（40–100mm） | 景別、主體朝向、光質（招牌可硬，也可被雨霧柔化） | 加 T45／T44／乾燥清澈的空氣 = 取消 —— 霓虹的戲劇性來自雨、霧、濕地面的二次放大，少了介質就只是廉價色片。把膚色也推成高飽和色片是最常見的失敗。三層分離（前景遮擋／主體／樓體招牌）不可壓成一層 |
| S22 太空歌劇 | 光質（平行硬光、投影邊緣幾乎沒有半影、**沒有大氣散射**）／光位（單一恆星）／光源與色溫（恆星 + 7000–9000K 行星反照 + 1800K 尾焰／4300K 艙窗三層）／影調（16:1）／色彩（高光近中性、陰影冷藍、星空純黑無漸層）／景深（T5.6–11、motion control 慢速運動）／鏡頭（50–200mm 長焦壓縮 + 2x 變形寬銀幕）／相機高度（低於物體下緣仰拍） | 景別、主體朝向 | 加 T18 丁達爾光／任何霧或體積光／柔化的陰影邊緣 = 取消（真空沒有介質，加了巨大感立刻縮水成塑膠模型）。景別可覆寫，但有一個不可刪的條件：畫面裡必須留一個**比例尺物件**（一個人、一架小艇、一扇艙門），否則「巨大」無從判讀。講法要準確：船體曲面上的明暗仍依表面法線平滑遞減，真正「數公分內斷掉」的是邊緣、凸起與投影 |
| S23 生活寫實 | 光位（**二擇一**：日戲窗光側前 或 夜戲室內既有頂燈／桌燈自上而下）／光質（障子或側窗漫射出的大面積柔光）／光源與色溫（自然光 5000–5600K 或室內既有燈具，完全不加電影燈）／影調（1:1.5–1:2、低對比、陰影抬起、高光柔收）／相機高度（榻榻米坐姿 60–90cm）／色彩（膚色自然優先、輕度降飽和、白平衡保留現場混色）／鏡頭（35–50mm，偶爾 85mm 遠遠觀察） | 景別（中近景 ↔ 中景）、主體朝向、景深（T2.8–4 內可調） | 加 T15 舞台光／T13 底光／T47 硬光 = 取消。最常見的隱形覆寫是把機位抬回眼平 —— 低機位與低對比都是刻意的技術選擇，抬回眼平再把臉打亮就變成普通家庭劇。畫中畫框（門框、走廊、窗櫺）與生活痕跡是這個包的構圖基礎設施 |
| S24 宇宙恐怖 | 光源與色溫（無來源的巨大輝光；色溫軸與 tint 軸必須**分開下指令**，紫與黃綠只能靠 magenta–green 軸做出來）／光位（框外上方或地平線之下，只給輪廓光與四分之三背面的邊緣，完全無補光）／影調（欠曝 1.5–2 級、黑位只剩約 5% 細節）／色彩（近單色低飽和 + 單一非自然高飽和光源、膚色推向青灰）／景別（人物佔畫面底部十分之一） | 主體朝向、相機高度＋鏡頭＋景深（**三者連動、二擇一**：18–24mm 貼地仰拍配 T2–2.8，或 135–300mm 長焦壓縮配 T5.6–8，不能兩頭都要） | 加 T01 暖色調／T44 亮調／清晰的主體特寫 = 取消。恐懼機制是比例、留白與無來源的光；主體越清晰、畫面越滿，效果越低。寫成「偏紫的 8000K」是錯的指令，必須拆成色溫與 tint 兩句。把恐怖寄託在怪物本身、寫滿觸手與血，也是取消 |

---

### 覆寫規則

**核心規則：選了風格包（S01–S24 任一）之後，覆寫最多 2 軸。超過 2 軸等於沒選風格包 —— 刪掉風格名，改成從十軸（景別／鏡頭／相機高度／主體朝向／光位／光質／光源與色溫／影調與對比／色彩／景深與動態）逐軸重新組。**

- **一次只能有一個風格包。** 兩個風格包 = 十幾條互相矛盾的指令，模型會挑一個執行、另一個變成噪音，而且你無法預測它挑哪一個。
- **2 軸怎麼數**：一個軸算 1，不管你在那個軸上寫了幾個字、用了幾項技法。景別從遠景改成中景是 1；同時改景別與景深是 2；再動色彩就是 3，超額。表 C 標「二擇一」的欄位不算，那是風格包內建的分歧。
- **只能動表 C「剩哪幾軸可覆寫」欄列出的軸。** 碰到「已鎖死」欄的任何一項，不是覆寫，是取消。
- **覆寫必須寫成具體技術描述，不是換一個技法名。** 例：S06 單光源夜戲把景別覆寫成 T32 特寫，就必須同時重寫「那盞入鏡的實用光在特寫距離下落在臉的哪一塊、暗面還剩幾級」。只把 `close-up` 貼上去，風格包原有的光位描述會與新景別對不上。
- **補光是最常見的隱形覆寫。** `soft fill on the face`、`a bounce card lifting the shadows` 這類句子同時動了光質軸與影調軸，一句話用掉整個額度；而且對 S01／S06／S12／S13／S16／S22 而言直接等於取消。
- **色彩軸被載體鎖死的四個包（S02／S11／S15／S16），色彩軸的覆寫永遠是取消，沒有例外。** 單色或色片系統裡的色彩指令是空指令，只會稀釋其他 token 的權重。
- **覆寫空間最小的六個包，動之前先想清楚**：S03（只剩 1 軸）、S15／S16／S17／S19／S22（各 2 軸）。這幾個幾乎沒有犯錯餘裕，通常直接照原樣走比較快。
- **超額時的正確處置**：刪掉風格包，但把你真正想要的那 2–3 個技術特徵手寫成句子留下來，例如 `red halation blooming around highlights`、`mixed uncorrected colour temperature`、`crushed blacks tinted rather than neutral`。一個被覆寫到面目全非的風格名，效果遠不如三句具體的技術描述。

**判斷一個覆寫是「調整」還是「取消」—— 三個測試，任一不過就是取消**

1. **核心句測試**：把該風格在 `04-film-styles.md` 的〈技法核心〉那一句話唸出來，你的覆寫有沒有動到那句話裡的任何一個名詞？動到 = 取消。例：S22 太空歌劇的核心句是「真空中的單一平行硬光 + 行星反照的冷色弱補光 + 長焦深景深」，加霧就動到了「真空」。
2. **因果測試**：這個特徵是「載體或物理條件造成的**後果**」，還是「創作者可以另選的**選擇**」？後果不可覆寫。後果類清單（背下來）：S11 的「幾乎沒有純黑」（三條片 ASA 5–10 逼出的巨量補光）、S12 的「幾乎無顆粒」、S14 的「全景深、沒有散景」（1/4 吋 CCD）、S17 的「色度滲流」（color-under 的 0.4MHz 色度頻寬）、S20 的「沒有動態模糊」（逐格單張曝光）、S22 的「陰影邊緣沒有半影」（真空無散射）、S15 的「沒有硬輪廓光」（介質把背光打散）。
3. **抵銷測試**：把風格包與覆寫項同時餵給模型，兩者對**同一塊像素**下的指令方向是否相反？相反 = 取消。例：S11 三色印片要求臉上不存在純黑，T42 暗色調要求大面積落入黑位，同一塊像素收到相反指令。若兩者作用在**不同的空間分區**（S13 港片霓虹的暖側與冷側、S06 入鏡實用光與沉黑的暗面），那就不是取消。

**判定為取消之後只有兩個選項**：(a) 放棄那個覆寫需求，照風格包原樣走；(b) 放棄風格包，取它的 2–3 個技術特徵當作零件，再從十軸重新組。
不要選 (c)「兩個都留著讓模型自己決定」—— 那必然得到一張兩邊都不像的圖，也就是使用者說的「加了風格包但看不出來」（見〈五、除錯對照表〉最後一列）。
