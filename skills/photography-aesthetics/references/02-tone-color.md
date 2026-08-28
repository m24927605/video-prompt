# 影調、對比與色彩篇

本檔涵蓋 9 項技法。**這一層是整體調性，與打光是不同層次的參數** —— 同一組打光可以被調成亮調或暗調、高對比或低對比、高飽和或低飽和。

四個常被混為一談、必須嚴格切開的概念：

| 概念 | 是什麼 | 項目 |
|---|---|---|
| 曝光 | 進光量是否超出感光範圍 | `02 過度曝光` |
| 影調 | 亮度分布的重心在哪 | `44 亮調` ↔ `42 暗色調` |
| 對比 | 動態範圍被拉開還是壓縮 | `46 高對比` ↔ `43 低對比度` |
| 色彩 | 色溫傾向與飽和度 | `01 暖色調` ↔ `38 冷色調`、`16 高飽和` ↔ `45 低飽和` |

---

### 01 暖色調｜Warm Color Grade

- **英文關鍵詞**：`warm color grade` / `amber warm tone` / `orange-and-teal split tone`
- **原理**：本組九項（01/02/16/38/42/43/44/45/46）屬於曝光、影調、對比、色彩這四個「後期／整體調性」層級的參數，與打光層（03–15、18、27、36–37、40–41、47–48 的光位／光質／光源）是不同層次，必須分開下指令；原則上可疊加在任一種打光上，但色彩軸要跟光源色溫軸對得起來（見各條「衝突」）。暖色調的物理成因是**白平衡設定高於光源實際色溫**：光源是 2800–3200K 的鎢絲或燭火，相機仍用 5600K 日光白平衡，相機以為光比實際更藍而補紅，畫面整體往橙紅位移。調色端則是把 highlights 與 midtones 的色相推向 orange（hue 約 20–40°）而 shadows 保留一絲 teal（hue 約 180–190°）。
- **情緒**：親密、懷舊、安全感、慵懶、人情味、黃昏將盡
- **提示詞**：`warm amber color grade, 3200K tungsten practicals recorded on a 5600K daylight white balance, orange highlights and midtones across skin and wood, shadows holding a faint teal, neutral white point kept in the brightest speculars, gentle halation around lamp filaments, skin pores and fabric weave still visible`
- **強化**：`06 暖光源`、`12 火光`、`08 窗光（限黃昏低角度側窗）`、`16 高飽和`
- **衝突**：`38 冷色調`（同軸互斥）、`36 冷光源`（僅限冷光源當**主光**時；小面積冷色 practical 反而靠對比強化暖調，那是 `41 雙性照明`）
- **常見錯誤**：只寫 "warm tone" 會讓模型在整張圖蒙一層黃、膚色變成髒橘；正確做法是給出「光源色溫 + 白平衡設定」兩個數字，並明確要求分離式偏色（暖高光／中性或微冷陰影），而不是全域染色。另外，句中否定（"no yellow wash"）在 Flux／Midjourney 上不可靠，一律改成正面陳述（"neutral white point kept in the speculars"）。若畫面本來就是 `41 雙性照明`，全域暖調會把冷側拉回中性、抹平冷暖對照，此時只能用 split-tone 而不能下全域色偏。

### 02 過度曝光｜Overexposure

- **英文關鍵詞**：`overexposed` / `blown-out highlights` / `clipped whites`
- **原理**：進光量超過感光元件飽和點（視場景動態範圍而定，一般是正確曝光再 +1.5 至 +3 EV），高光區 RGB 三通道同時撞上數位上限（8-bit 下為 255）而細節不可逆喪失。明暗交界那圈溢出的白光要注意歸因：現代 CMOS 多半有抗溢出設計，實際看到的 bloom 主要來自鏡頭內部散射（veiling glare）與感光層／底片的 halation，不是電荷溢出。這是「曝光」軸的錯誤或刻意錯誤，與影調重心（`44 亮調`）不是同一個軸；但兩者的指令互斥——44 要求高光不觸頂，02 要求高光洗掉，不可寫在同一段提示詞裡。
- **情緒**：刺眼、抽離、記憶漂白、夢境、脆弱、被沖散
- **提示詞**：`deliberately overexposed by +2 EV, window highlights clipped to pure white with no recoverable detail, blooming spill creeping over the cheek and hairline, skin texture washed flat, only the lower shadows still holding shape`
- **強化**：`05 背光`、`08 窗光`、`40 強光`、`48 閃光燈`
- **衝突**：`37 弱光`、`43 低對比度`（白點必須 roll off 在純白以下，與 clipped 直接對立）、`44 亮調`（要求不觸頂）、`16 高飽和`（高光洗白等於去色）
- **常見錯誤**：把「過曝」寫成 "very bright"，模型只會整體提亮而細節仍在；正確是明講 clipped / blown / no recoverable detail，並指定過曝發生在哪一塊（窗、天空、臉部高光）與 EV 量。注意 `42 暗色調` 與本項**並非互斥**：低調畫面裡開一扇過曝的窗或一盞爆掉的燈是常規做法，衝突的只有「全域 +2 EV」這種下法。

### 16 高飽和｜High Saturation

- **英文關鍵詞**：`high saturation` / `vivid color grade` / `saturated color palette`
- **原理**：把像素往色彩空間的中性軸外推（HSL 的 S 通道中間調 +20–40%），色度提高、相鄰色相的視覺分界更明確——但飽和度本身不改變空間銳度，不會讓邊緣變硬。實拍端的真正槓桿有三個：低 ISO（100–200）保住色彩訊噪比、偏光鏡消掉非金屬表面的鏡面反射白光（角度依賴，與光源夾角約 90° 時效果最強）、曝光壓低 1/3–2/3 EV 讓色彩不被高光洗淡。硬光的作用要講清楚：它在**漫反射面**上讓物體固有色（local color）不被灰白稀釋，但它產生的**鏡面高光本身是去飽和的**，所以硬光必須配偏光鏡與略低曝光才成立。
- **情緒**：熱烈、亢奮、通俗、商業、卡通化、感官刺激
- **提示詞**：`high-saturation grade, midtone saturation up 30 percent, reds and cyans near full purity with no channel clipping, skin kept at natural saturation, polarized surfaces with the white glare removed so local color reads clean, exposure held a third of a stop down to keep colors dense, neutral blacks with no color cast`
- **強化**：`47 硬光`、`15 舞台光`、`11 自發光`、`46 高對比`
- **衝突**：`45 低飽和`（同軸互斥）、`02 過度曝光`（高光 clip 到 255 就是白，色度歸零）、`43 低對比度`（matte／faded 質地本質上會壓低色度）
- **常見錯誤**：寫 "vibrant colors" 會讓模型連帶拉高對比與銳度，膚色跟著變橘、紅色溢邊；正確是指定哪些色相要飽和，並同句寫上 "skin kept at natural saturation"。也不要用「色塊邊界變硬」這類措辭（例如 "hard edges between color blocks"），那會把模型推向平面海報／向量插畫，而不是高彩的攝影。

### 38 冷色調｜Cool Color Grade

- **英文關鍵詞**：`cool color grade` / `teal blue tone` / `cold daylight palette`
- **原理**：**白平衡設定低於光源色溫**時畫面往青藍位移，例如光源是 5600K 日光而相機設 3200–4300K 鎢絲白平衡（相機以為光比實際更紅而補藍）；另一條路是相機維持 5600K 日光白平衡、直接拍未修正的陰天／陰影天空光（7500–10000K），同樣是 WB 設定低於光源色溫。調色端把 shadows 推向 blue（hue 約 210–230°），highlights 維持中性白點，否則整張會蒙一層藍灰、黑位浮起、反差看起來變糊。
- **情緒**：疏離、清醒、臨床、危險、寒冷、理性的夜
- **提示詞**：`cool blue color grade, tungsten white balance under 5600K daylight, shadows falling toward the blue of open shade around 8000K, highlights kept at a neutral white point, skin holding a trace of warmth so it still reads as living flesh, cold ambient fill from an unseen window`
- **強化**：`36 冷光源`、`08 窗光（限北向天光／陰天）`、`37 弱光`、`45 低飽和`
- **衝突**：`01 暖色調`（同軸互斥）、`06 暖光源`、`12 火光`（後兩者僅限**作為主光**時；小面積暖色 practical 反而靠對比強化冷調，那是 `41 雙性照明`）
- **常見錯誤**：整張蒙藍會讓黑位浮起、膚色變屍青；正確是 split-tone 思路，只推陰影往藍、保住高光白點，並單獨聲明膚色保留一點暖（要屍青是另一個刻意變體，此時才寫 "skin drained toward grey-blue"，不要兩句並存）。同 `01`：若畫面是 `41 雙性照明`，全域冷偏會吃掉暖側，只能做 split-tone。

### 42 暗色調｜Low-Key

- **英文關鍵詞**：`low-key lighting` / `low-key chiaroscuro` / `single-source low key`
- **原理**：影調重心整體左移，畫面約 80–90% 面積落在直方圖左端（IRE 10 以下的深黑），只有小面積主體被打亮且**曝光正確**。標準做法是單一光源、拿掉補光板、光比（key:fill）拉到 8:1 至 16:1，配深色背景與旗板控制溢光。硬光只是預設值不是必要條件——柔光低調（大柔光源＋負片補光／黑旗吃掉反射）同樣成立，因為本項描述的是亮度分佈，不是照度不足，也不是光質。
- **情緒**：危險、內斂、神秘、壓迫、罪惡、莊嚴
- **提示詞**：`low-key lighting, single hard key 60 degrees off the lens axis and just above eye level, 16:1 key-to-fill with no fill bounce, roughly 85 percent of the frame in unlifted black, one bright sliver correctly exposed across cheekbone and jaw, matte black background absorbing the spill`
- **強化**：`47 硬光`、`03 側光`、`14 輪廓光`、`46 高對比`
- **衝突**：`44 亮調`（同軸互斥）、`43 低對比度`（lifted blacks 與大面積不抬起的純黑對立）
- **常見錯誤**：把 42 暗色調寫成「很暗」或直接混用 `37 弱光`，會拿到整張欠曝的灰片；正確是「大面積純黑 ＋ 小面積正常曝光的亮部」，明確給出光比與受光面積比例，亮部本身必須是亮的。角度也要寫清楚是相對什麼（離鏡頭軸 60°、略高於眼平），只寫 "60 degrees" 模型不知道是水平方位還是仰角。`09 柔光` 不是本項的互斥項——柔光低調是標準做法，不要把光質軸誤當影調軸的對立面。

### 43 低對比度｜Low Contrast

- **英文關鍵詞**：`low contrast` / `lifted blacks matte finish` / `faded film look`
- **原理**：把 tone curve 的黑點抬到 IRE 8–15（lifted blacks）、白點壓到 IRE 85–90，整個動態範圍被壓縮進中間段，明暗過渡帶變得極長。實拍可用 Black Pro-Mist 1/2–1 號濾鏡（靠高光周圍的散射把黑位抬起，所以畫面裡要有高光才有效）、逆光空氣霧、鏡頭 flare，或沖印褪色（faded print）取得同一種 matte 質地。它動的是黑白位，與光源大小（光質）無關。
- **情緒**：溫柔、回憶、疲倦、含蓄、時間感、鈍化的哀傷
- **提示詞**：`low-contrast matte grade, blacks lifted to soft charcoal that never reaches zero, highlights rolled off well below pure white, milky halation from a Black Pro-Mist 1/2 diffusion filter, faded darkroom print tonality, long gentle transitions through the midtones`
- **強化**：`09 柔光`、`45 低飽和`、`44 亮調`、`18 丁達爾光`
- **衝突**：`46 高對比`（同軸互斥）、`42 暗色調`、`02 過度曝光`（白點必須壓在純白以下）、`16 高飽和`
- **常見錯誤**：以為寫 "soft lighting" 就會得到低對比，但柔光只改變陰影邊緣的硬度、不改變黑白位；正確是直接下 lifted blacks / matte / faded film 指令，並言明黑位不觸 0、白位不觸頂。反過來同理：`47 硬光` 也不是本項的互斥項——霧中的硬陽光配 lifted blacks 完全成立，硬光一樣不決定黑白位。另外 "faded print" 會連帶壓低色度，不要跟 `16 高飽和` 同用。

### 44 亮調｜High-Key

- **英文關鍵詞**：`high-key lighting` / `high-key soft white` / `low-ratio high-key studio`
- **原理**：亮度分佈重心整體右移，多數像素落在 IRE 60–90 但不觸頂，細節完整保留。做法是面積達主體 3–4 倍的大柔光罩當主光，**另外**用大量白反光板／白牆白地把陰影側墊起來，把光比壓到 2:1 甚至 1.5:1——填光來自反射面而不是主光箱本身。陰影仍在，只是變淺，不是被消滅。
- **情緒**：乾淨、輕盈、樂觀、無威脅、廣告感、開放
- **提示詞**：`high-key lighting, oversized softbox key with large white bounce on the shadow side holding a 2:1 ratio, near-white background still readable as light grey, highlights held just under clipping, skin retaining pores and fabric weave, airy open space`
- **強化**：`09 柔光`、`27 正面光`、`08 窗光`、`43 低對比度`
- **衝突**：`42 暗色調`（同軸互斥）、`46 高對比`（crushed blacks 與填平的淺陰影對立）、`02 過度曝光`（要求高光洗掉，與「不觸頂」直接對立）
- **常見錯誤**：把 44 亮調寫成「很亮／過曝」會直接掉進 `02 過度曝光` 的白掉畫面；正確是同句聲明 bright but nothing clipped、shadows filled not erased、texture retained，讓亮部仍有層次。`47 硬光` 不必然互斥——硬光配大量補光一樣能壓到低光比，只是不常用；真正定義高調的是光比與亮度重心，不是光源大小。

### 45 低飽和｜Desaturated

- **英文關鍵詞**：`desaturated` / `muted color palette` / `low-saturation grade`
- **原理**：全域飽和度下降 30–60% 即 desaturated（膚色與單一重點色仍可辨識），下降到 0 是 greyscale／black and white（只剩明度資訊）。注意英文裡的 **monochrome 指「單一色相」**（含 sepia、cyanotype 這類單色調），既不等於黑白也不等於低飽和，三個詞不可互換。實拍端靠陰天散射光、空氣灰霧、低彩度美術陳設，或 bleach bypass 沖印（保留銀鹽，得到低彩 ＋ **高**反差 ＋ 粗顆粒——所以 bleach bypass 不能跟強化欄的 `43 低對比度` 同時要）。
- **情緒**：冷靜、紀實、荒涼、克制、沉重、去戲劇化
- **提示詞**：`desaturated palette, overall saturation down 50 percent, only a single muted rust accent surviving, skin near neutral grey with a trace of warmth, overcast diffuse light, fine grain, shadows staying neutral grey`
- **強化**：`38 冷色調`、`43 低對比度`、`37 弱光`、`09 柔光`
- **衝突**：`16 高飽和`（同軸互斥）、`15 舞台光`、`11 自發光`（後兩者是意圖衝突：有色光源存在的意義就是那些顏色，去彩等於白打）
- **常見錯誤**：把 desaturated 與 monochrome／black and white 當成同義詞寫在同一句，模型會直接交黑白照；要低彩就寫「飽和度降 X%、保留膚色與一個重點色」，要全黑白單獨寫 black and white，要單色調（褐調／藍調）才寫 monochrome，三者不可並列。

### 46 高對比｜High Contrast

- **英文關鍵詞**：`high contrast` / `crushed blacks` / `steep tone curve`
- **原理**：tone curve 的 S 形被拉陡，黑點壓到 IRE 0、白點推到 95–100（鏡面高光可以觸頂，但漫射白面不該整片洗掉，否則就掉進 `02 過度曝光`），中間調過渡被壓得極短，映射到中間調的那條明暗交界在畫面上只佔很窄一條。實拍端以單一光源、不補光、光比 8:1 以上，或高反差沖印／數位曲線達成。它拉開的是動態範圍兩端，與亮度重心在哪一側無關，也與光源大小無關。
- **情緒**：尖銳、對立、果決、暴力感、戲劇化、無退路
- **提示詞**：`high-contrast grade, steep S-curve with the midtones compressed, blacks crushed to pure zero with no shadow detail, specular highlights bright and clean, an abrupt narrow transition band splitting the lit and unlit halves of the face`
- **強化**：`47 硬光`、`03 側光`、`42 暗色調`、`16 高飽和`
- **衝突**：`43 低對比度`（同軸互斥）、`44 亮調`
- **常見錯誤**：用 "dramatic lighting" 這類抽象詞只會拿到隨機打光；正確是直接描述曲線與交界行為（crushed blacks、clean speculars、short transition band）並附上光比數字。`09 柔光` 不是互斥項——大柔光源配陡曲線（柔邊陰影但黑位全壓死）是很常見的組合，光質軸與對比軸各走各的。

---

## 色彩關係

前面九項處理的是**單軸的色彩參數**（往暖還往冷、飽和多少）。但決定一張圖是「高級」還是「俗豔」的，
從來不是飽和度的高低，而是**畫面裡有幾種顏色、這幾種顏色在色輪上是什麼關係、各佔多少面積**。
`16 高飽和` 與 `45 低飽和` 只是幅度旋鈕，本章是它們的上位參數：先決定關係，再決定幅度。

**執行順序（四步，不可跳）**

1. **數顏色**：這個畫面允許幾個色相？（預設 2–3，上限 4。膚色不計入，它有自己的規則，見規則二。）
2. **選關係**：下面六項不是平行的六選一，是「四個色輪關係 + 兩個可疊加的紀律層」：
   - **色輪關係（互補／分裂互補／類比／單色）四選一，只能挑一個。**
   - **限制調色盤**是紀律層，疊在上面四者任一之上（例如「類比色 + 限制在三色」）。
   - **重點色**也是紀律層，疊在單色或限制調色盤之上最穩（近中性底 + 一個色彩事件）。
3. **配面積**，並把每個色相綁到具體物件上（牆／衣服／燈／地面）：
   - 三色 → 60 / 30 / 10。
   - 兩色 → 70 / 30 或 80 / 20。**不要 50 / 50**，兩色等面積會互相搶主角，畫面沒有主從。
4. **再談飽和與色溫**：這時才接上 `16 高飽和`／`45 低飽和`、`01 暖色調`／`38 冷色調`，並補膚色保護句。

**關於本章所有數字（先讀這段，否則會誤用）**

- 色相角（30°、190°）是**給 agent 自己算關係用的**，不是提示詞裡的魔術參數。寫進提示詞時它只是輔助線索，
  真正生效的是同句的顏色名詞（amber、teal）與承載物件。
- 面積比與百分比（`seventy percent by area`、`saturation down fifty percent`）**模型不會照字面執行**，
  它們提供的是「方向 + 強度」。可靠的是**相對關係**（誰多誰少、誰亮誰暗、誰是唯一的飽和色），不是絕對值。
- 因此每個數字旁邊都要配一句相對描述（`one step lighter than the wall`、`the only fully saturated hue in frame`）。
  數字被忽略時，相對描述還撐得住畫面。
- 生成端的實際行為隨模型與版本變動。以下所有「模型會做 X」的敘述都是可觀測傾向，不是保證；
  下一版模型改掉了就以實測為準。判斷方法：把懷疑的那一句拿掉，跑一組對照圖比較。

| 關係 | 類型 | 色相數 | 對立強度 | 最適用 | 主要風險 |
|---|---|---|---|---|---|
| 互補色 | 色輪關係 | 2 | 最強 | 類型片、海報、需要立即辨識的對立 | 兩色重疊處加法混色變髒；面積各半會打架 |
| 分裂互補 | 色輪關係 | 3 | 強但可控 | 敘事劇情、人物與環境的緊張關係 | 第三色沒綁到獨立表面就退化成一團藍綠 |
| 類比色 | 色輪關係 | 2–3 | 弱 | 統一氛圍、自然場景、單一情緒 | 主體與背景同色相又同明度，直接黏住 |
| 單色 | 色輪關係 | 1 | 無 | 極端統一、風格化、時代感 | 膚色被完全吃掉（這是必然，不是失誤） |
| 限制調色盤 | 紀律層 | 3–4 | 由內含關係決定 | 整部片／整組照片的一致性 | 執行不徹底就等於沒做 |
| 重點色 | 紀律層 | 近中性底 + 1 | 局部極強 | 單點視線終點、象徵物 | 被模型做成廉價的選擇性上色 |

---

### 六種配色關係

#### 互補色｜Complementary

- **是什麼**：色輪上相隔約 180° 的兩個色相，因同時對比（simultaneous contrast）在視覺上互相把對方的彩度推到最高。
- **提示詞**：`complementary two-hue scheme, warm amber near thirty degrees hue carried by the subject's coat and one practical lamp, a teal field near one hundred ninety degrees covering the wall and the floor behind, each hue held on its own surface and meeting at a hard edge, roughly thirty percent amber to seventy percent teal by area, preserve natural skin tone with its warm undertone intact`
- **心理效果**：對立、張力、外放、辨識度高
- **典型場景**：主體與環境屬於兩個世界——溫暖的人站在冷掉的城市裡；或兩個角色分邊對峙。
- **搭配**：`41 雙性照明`、`16 高飽和`、`03 側光`、`圖二 02 義式驚悚紅綠光`、`圖二 21 賽博龐克街景`

**兩種落地方式，先選一種再下筆**：

1. **分表面**：兩色各據不同物件／不同牆面，交界是硬邊。`圖二 02 義式驚悚紅綠光`、`圖二 21 賽博龐克街景` 屬此類。
2. **分影調段（split-tone）**：暖色給高光、冷色給陰影，不分表面。`圖二 04 魔幻時刻` 的「橘金高光 + 冷藍陰影」屬此類，
   而且是自然光自己完成的。這一種務必同時遵守規則五（指定 shadows／highlights）。

**常用互補對與座標**（HSL 色相角）：

| 對 | 座標 | 實際夾角 | 備註 |
|---|---|---|---|
| 橙／青（teal & orange） | ≈ 25–30° vs ≈ 190–200° | 約 165–175° | 商業片預設案。它其實不是精確互補——因為主色是**膚色本身的色相**（約 25°），對面那一端才跟著調整 |
| 藍／黃 | 240° vs 60° | 180° | 精確互補 |
| 紅／青 | 0° vs 180° | 180° | 精確互補 |
| 洋紅／綠 | 300° vs 120° | 180° | 精確互補 |

`圖二 02 義式驚悚紅綠光` 是互補色的極端案例，但要講準它為什麼成立：
**紅與綠在 HSL 上只相隔 120°，不是 180°**；它們是傳統 **RYB 藝術色輪**上的互補對，
在 RGB／HSL 與現代 CMY 印刷色輪上都不是（RGB 裡紅的對面是青，綠的對面是洋紅）。
它之所以讀起來像嚴格互補，是因為**兩束光各自只讓一個通道有訊號**（紅光幾乎只有 R、綠光幾乎只有 G），
在**不重疊的區域**兩色互不污染，對立感被推到最大。

但這正是互補色最大的坑：**紅光與綠光重疊處是加法混色，會變黃，不會變中性白**（見 `圖二 02` 條）。
所以互補色的鐵律是——**兩色重疊帶壓到最窄，或乾脆讓兩色完全不接觸**。不管是打光還是調色，重疊帶就是畫面變髒的地方。

#### 分裂互補｜Split-Complementary

- **是什麼**：取一個主色，不用它正對面那一色，改用對面色左右各 ±30° 的兩個鄰色（即主色 +150° 與 +210°）。
- **提示詞**：`split-complementary palette, one warm orange key hue near thirty degrees answered by two cool hues sitting either side of its opposite — cyan-teal near one hundred eighty degrees washing the background wall, a deeper blue near two hundred forty degrees filling the shadows and the far end of the street — the orange confined to the subject and a single practical lamp, each cool hue kept on its own surface, preserve natural skin tone one step warmer and brighter than the cool field`
- **心理效果**：緊張但不對撞、有層次、成熟、可控
- **典型場景**：夜戲裡人物帶著一盞暖燈走過藍色街區，冷側再被青綠招牌切開一塊。
- **搭配**：`41 雙性照明`、`06 暖光源`、`36 冷光源`、`42 暗色調`、`圖二 21 賽博龐克街景`、`圖二 13 港片霓虹`

比純互補少一分廣告感、多一分敘事感。使用紀律：兩個冷色**必須分派到不同的物理表面**（一個給背景牆、一個給陰影或次要光源），
不可混在同一面牆上，否則兩者會被模型平均成一團藍綠，等於退回單一冷色。

搭配的兩個風格包各自是三色讀法：`圖二 21` 是「琥珀 practical／青藍招牌／洋紅高光」，
`圖二 13` 是「琥珀店燈／翡翠綠／洋紅霓虹」。兩者都不是教科書式的精確 ±30°，
但都符合「一個暖主色 + 兩個分開落在對側的冷色」這個可執行結構。

#### 類比色｜Analogous

- **是什麼**：色輪上相鄰、落在同一段 30–60° 弧內的 2–3 個色相。
- **提示詞**：`analogous palette held inside a forty-degree arc of the wheel — rust, amber and ochre only — every surface drawn from those three, separation carried by brightness with one dominant hue covering about sixty percent of the frame, preserve natural skin tone held one value step lighter and slightly less saturated than the surrounding ochre so the face separates`
- **心理效果**：統一、和諧、沉浸、無衝突
- **典型場景**：黃昏室內全暖木色調；或整片雨天灰藍到藍綠的街道。
- **搭配**：`01 暖色調` 或 `38 冷色調`（同軸互斥，二擇一）、`43 低對比度`、`09 柔光`、`圖二 03 北歐冷冽`（灰綠／米白／灰藍落在同一段弧內）

類比色沒有色相對立可用，**分離主要靠明度、其次靠飽和度差**（同色相下把主體做得比背景乾淨一階也有效），
這是它唯一的失敗點：色相一致、明度又一致，主體會直接黏進背景。
下指令時一定要同句寫出主體與背景的明度關係（見規則三）。

注意 `圖二 12 柯達克羅姆` **不是**類比色：它同時有強勢的紅橙、濃藍與橄欖綠，色域是寬的、對比是高的，
只是紅橙最搶戲。把它當類比色用會得到不一致的結果。

#### 單色｜Monochromatic

- **是什麼**：全畫面只有一個色相，靠明度階與飽和度變化拉開層次。
- **提示詞**：`monochromatic palette locked to a single blue-grey hue, every surface sharing that one hue while the value steps run from near-black to near-white, saturation varied across the frame with the hue held fixed, skin folded into the same blue-grey family as a lighter and slightly cleaner step so the face reads by value alone`
- **心理效果**：極度統一、風格化、抽離、時代感
- **典型場景**：沙塵中的單一橙褐世界；或全片藍灰的冷調空間。
- **搭配**：`45 低飽和`、`42 暗色調` 或 `44 亮調`（同軸互斥，二擇一）、`圖二 15 沙塵單色`、`圖二 05 煙霧體積光`（近單色）、`圖二 16 黑白默片（限 tinting 染色變體）`

英文詞務必分清（沿用 `45 低飽和` 條的定義）：**monochrome = 單一色相**，不等於 black and white，也不等於低飽和。
`圖二 16 黑白默片` 本體是無彩的黑白，只有它的**印片染色（tinting）變體**才是真正的單色；不要拿無染色的黑白當單色範例。

單色是四個色輪關係裡唯一天生與膚色衝突的：膚色本身就是一個色相，被單色系統吃掉是必然結果。
**因此規則二的 `preserve natural skin tone` 在嚴格單色下不成立**——那句話會要求模型生出第二個色相，直接違反單色。
只有兩種合法寫法：

- **折進去（嚴格單色）**：膚色寫成同色相裡較亮、飽和度較低的一階，臉靠明度被讀出來，不靠膚色。如上方提示詞。
- **明講吃掉**：`skin hue fully absorbed into the wash, faces reading as value only`。

（第三種其實是「單色 + 一個例外色相」，那已經不是單色而是重點色，見下條；此時才寫 `preserve natural skin tone as the single exception`。）
三者都不寫，模型就自己決定，結果隨機。

#### 限制調色盤｜Restricted Palette

- **是什麼**：不是色輪關係，而是一條紀律——全片／全組只准出現指定的 3–4 個色相，其餘顏色一律從美術端移除。
- **提示詞**：`restricted three-colour palette, desaturated olive, chalk off-white and deep oxblood only, every colour in frame drawn from those three and named to a surface — olive tiled wall, off-white shirt, oxblood velvet chair — preserve natural skin tone as the single exception to the three`
- **心理效果**：控制感、設計感、秩序、一致性
- **典型場景**：一整組要放在一起看的照片，或一部片的統一視覺識別。
- **搭配**：`35 居中構圖`、`22 深景深`、`圖二 08 平面正面構圖`（本身就規定 3–4 個主色）、`圖二 07 單點透視對稱`（本身就規定收斂到一到兩個主色）

執行是全有全無：**只要畫面裡漏掉一個沒被納管的鮮豔物件（一個藍色垃圾桶、一件紅衣路人），整套就失效**。
提示詞裡要逐一點名承載顏色的物件，並用**正面列舉**收尾（`every colour in frame drawn from those three`），
不要寫 `no fourth hue` 或 `no blue`——色名本身就是強 token，否定句在多數擴散模型上不可靠（見 `01 暖色調` 常見錯誤）。

這是「高級感」最可靠的單一手段，因為它同時滿足窄色域與低色相數兩個條件（見規則六）。

#### 重點色｜Accent Colour

- **是什麼**：整體壓到近中性，只留單一物件保持高飽和，成為畫面唯一的顏色事件。
- **提示詞**：`near-neutral grade with a trace of colour surviving everywhere, one crimson coat at full saturation as the only fully saturated hue in frame, the accent covering about four percent of the picture area and sitting at the end of the eye path, every other surface pulled toward warm grey, preserve natural skin tone so faces keep their warm undertone while the crowd around them goes grey`
- **心理效果**：指向性、象徵、記憶點、克制
- **典型場景**：灰調人群裡唯一一件紅外套；或全冷色房間裡一盞暖燈。
- **搭配**：`45 低飽和`、`43 低對比度`、`11 自發光`、`12 火光`、`圖二 24 宇宙恐怖`（近單色低飽和底 + 單一非自然色高飽和光源）、`圖二 06 單光源夜戲`（唯一入鏡的鈉燈就是那個顏色事件）

三條硬性條件，缺一不可：重點色面積 **≤10%**（理想 3–5%）、**全畫面只出現一次**、位置在視線動線的終點。
出現兩次以上就不是重點色，是限制調色盤沒做好。
重點色的色相必須是**近中性底裡沒有的那一個**，否則它跟環境混成一片，讀不出「事件」。

禁止寫 `selective color` 或 `black and white with one red object`——這兩句在多數擴散模型上會命中「選擇性上色」的濾鏡語料，
交出去背式的粗糙結果，其餘全部去彩成純灰（臉也是）。正確做法是「整體降到近中性但仍有色，單一物件維持純色」。

**與 `45 低飽和` 衝突欄的關係**：`45` 把 `11 自發光`、`15 舞台光` 列為衝突（「有色光源存在的意義就是那些顏色，去彩等於白打」）。
重點色正是這個衝突的合法解——**環境去彩、有色光源本身就是那個重點**。要這樣用時，把去飽和的範圍明講在環境上
（`saturation down on the environment`），不要寫成全域去飽和。

---

### 色彩硬規則

#### 規則一｜先決定顏色的數量，再決定飽和度

- **做法**：任何色彩指令下筆前先回答「這張圖有幾個色相」。預設 2–3 個，上限 4 個。
  面積依步驟 3 的比例分配，並把每個色相綁到具體表面（`ochre wall`、`navy coat`、`amber lamp`）。
  色相數與承載物件都確定後，才動飽和度旋鈕。
- **不照做會發生什麼**：模型沒拿到色相數，就用先驗補——五、六個互相搶戲的高彩色相，沒有主從、沒有動線，
  得到典型的 AI 廉價感。**高飽和只是把既有關係推到極限的放大器，它放大好關係，也同等放大壞關係。**
  四色畫面加飽和不會變好看，只會變吵。

**色彩禁詞**（沿用 `07-beyond-the-charts.md` 1-4 的表格形式）

| 禁詞 | 模型會做什麼 | 改寫成 |
|---|---|---|
| `colorful` / `vibrant colors` / `rich color palette` | 沒指定色相數，用先驗補成五六個平均分佈的高彩色相，無主從 | 點名色相數與承載物件：`three hues only — olive wall, oxblood chair, off-white shirt` |
| `selective color` / `black and white with one red object` | 命中選擇性上色的濾鏡語料，其餘全部去彩成純灰（包含臉） | `near-neutral grade still holding a trace of colour, one red coat at full saturation as the only fully saturated hue` |
| `moody colors` / `cinematic colors` | 品質形容詞、零可執行資訊，退回模型預設的橘藍 | 直接寫關係與影調段：`amber highlights against teal shadows, neutral white point in the speculars` |
| `no blue` / `avoid green` | 色名是強 token，否定句在多數擴散模型上不可靠，寫了反而更容易出現 | 正面列舉：`every colour in frame drawn from olive, off-white and oxblood` |

#### 規則二｜膚色保護：任何降飽和或強色偏都必須附 `preserve natural skin tone`

- **做法**：只要提示詞裡出現「降飽和」或「全域／大面積色偏」的子句，就在同一段的**該子句之後緊接著**補上
  `preserve natural skin tone`，讓約束跟它要約束的對象黏在一起。
  只寫這一句效果有限，務必再補一句**膚色相對環境的位置**（更暖、更亮、或高一階明度）——
  模型能執行「比 X 亮一階」，「自然」它只能猜。
  一段提示詞寫一次即可；不要放在整段提示詞的最前面，開頭的詞在多數模型上權重最高，容易被當成主體描述而不是色彩約束。
  同軸的替代寫法 `skin kept at natural saturation`（見 `16 高飽和` 提示詞）可與本句並用，兩者互補。
- **不照做會發生什麼**：膚色的脆弱不是因為它的色相特別（HSV 色相角約 20–30°），
  而是因為**它的起始飽和度本來就只有 10–30%，離中性軸最近**。
  同樣一個「全域飽和 −50%」，高彩的紅牆掉完還是紅牆，膚色卻直接跨過「還讀得出是血肉」的門檻掉成中性灰——
  **不是它掉得比較多，是它離灰最近**。臉一到灰，唇色與臉頰的紅色層次一起消失，臉看起來平掉（真正的立體感仍由明度負責，
  被拿走的是次表面散射那層紅）。往藍推變屍青；往綠推最致命，見規則八。

**正確與錯誤對照**

| 意圖 | 錯誤寫法 | 會發生什麼 | 正確寫法 |
|---|---|---|---|
| `45 低飽和` | `desaturated, muted colors` | 膚色與環境一起掉到中性灰，臉變灰屍 | `saturation down about fifty percent across the environment, preserve natural skin tone with its warm undertone intact` |
| `38 冷色調` | `cool blue tone, blue color grade` | 全域藍偏，黑位浮起，膚色變屍青 | `cool blue grade pushed into the shadows, highlights held at a neutral white point, preserve natural skin tone so faces still read as living flesh` |
| 綠調環境 | `sickly green color grade` | 膚色轉黃綠，牙齒眼白發綠 | `green cast carried by the fluorescent tubes and the wall paint, preserve natural skin tone, faces held warm and one stop brighter than the green field` |
| 沙塵橙調（人物是主體時） | `everything orange, sand colored` | 膚色與背景同色相同明度，臉融進背景 | `sodium-orange dust haze filling the air, preserve natural skin tone kept one step cooler and lighter than the haze so the face separates` |
| 重點色 | `black and white with one red umbrella` | 粗糙的選擇性上色，其餘全灰包含臉 | `near-neutral grade still holding a trace of colour, preserve natural skin tone, one red umbrella at full saturation as the only fully saturated hue` |
| `圖二 11 三色印片` | `super saturated technicolor look` | 膚色被推成橘紅塑膠 | `three-strip Technicolor dye-transfer rendering, saturated reds, greens and blues that stay clear of one another, preserve natural skin tone at natural saturation against the saturated set` |

（沙塵那一列的前提是「人臉必須讀得出來」。若照 `圖二 15 沙塵單色` 把人縮成佔畫面 3% 的剪影，膚色不存在也不需要保護，
改走單色條的「明講吃掉」。）

- **例外清單**：以下五個風格包的賣點就是膚色被風格本身吃掉（來源不只色光——也可能是光譜響應或美術設定），
  此時**不可**寫保護句，改成反向明講：
  `圖二 02 義式驚悚紅綠光`（色光吃掉：`skin hue entirely replaced by the gel colours`）、
  `圖二 03 北歐冷冽`（白粉底 + 平光：`chalk-pale skin at the same value as the wall`）、
  `圖二 13 港片霓虹`（色光不校正：`coloured light contaminating the skin uncorrected`）、
  `圖二 16 黑白默片`（正色片光譜響應：膚色偏暗、紅唇渲染成黑，本來就壓深）、
  `圖二 24 宇宙恐怖`（`ash-grey skin`）。
- **最容易搞錯的一組對照**：`圖二 13 港片霓虹` 與 `圖二 21 賽博龐克街景` 看起來都是霓虹夜景，膚色規則卻**相反**——
  13 要求有色光直接污染膚色不校正（在例外清單），21 明文要求「膚色維持接近中性以免整張變色片」（要寫保護句）。
  兩者不可互抄。

  規則是：**膚色只有兩種合法狀態——明講保留，或明講被吃掉。留白等於把結果交給模型擲骰子。**

#### 規則三｜主體與背景的分離，優先序是 明度差 > 色相差 > 景深虛化

- **做法**：先給明度差，寫成可執行的句子：`the subject held two stops brighter than the wall behind`，
  或反過來 `dark figure against a bright field`。明度差不足時才追加色相差（`warm subject against a cool field`）。
  景深虛化是最後一手，且不能單獨使用。
  **自檢法：把畫面想成灰階縮圖。主體如果在灰階下消失，色相差與虛化都救不回來。**
- **順序的原因**：人類視覺系統的亮度通道空間解析度高於色度通道，影像／視訊壓縮據此丟的也是色度（4:2:0 色度次取樣），
  所以縮圖、手機小圖、黑白轉檔下明度差都還在；
  色相差會被你自己下的 `45 低飽和`、`43 低對比度` 抹平，也在色弱觀者與單色系統下失效；
  景深虛化只是把背景弄糊，糊掉的背景若與主體同明度，兩者照樣黏在一起，而且模型常把虛化做成貼圖式的假背景。
- **不照做會發生什麼**：只靠 `25 淺景深` 做分離，會得到「主體浮在一團糊裡但輪廓仍與背景同亮度」的圖，
  縮圖一看主體就不見了；只靠色相差，一旦要求低飽和，分離會整個消失。
- **補救順位**：明度差不夠 → 加 `10 髮絲光` 或 `14 輪廓光` 描邊，或換深色背景配 `42 暗色調`。
- **例外要知道**：`圖二 03 北歐冷冽` 刻意違反這條（人與牆同明度同平面），那是風格的目的而非失誤。
  違反這條之前，先確認你是在做這種風格，而不是忘了。

#### 規則四｜色彩負責情緒歸屬，影調負責注意力引導，兩者不互相代勞

- **分工定義**：**色彩回答「這是什麼情緒、哪個世界、什麼年代」；影調（`42 暗色調`／`44 亮調`／`46 高對比`／`43 低對比度`）回答「先看哪裡、第二看哪裡」。**
- **做法**：視線動線一律交給明度——一塊亮、其餘壓暗；色彩只維持一種關係、不承擔引導功能。
  情緒一律交給色溫方向（`01 暖色調`／`38 冷色調`）與配色關係，不靠加大明暗反差來製造。
- **唯一的例外是重點色**：它是刻意讓色彩接管一次引導，代價是全畫面只准用一次（見重點色三條件）。用第二次就回到下面的失敗模式。
- **色彩代勞引導會發生什麼**：畫面裡出現三、四個高飽和色點，每一點都在喊「看我」，動線斷裂，整張變花。
  這正是「顏色很多但不知道要看哪」的成因。
- **影調代勞情緒會發生什麼**：得到一張反差很大、很有戲但說不出溫度的圖——觀眾能感覺到緊張，卻分不出是懷舊、疏離還是危險。
  情緒歸屬缺席，畫面只剩形式。

#### 規則五｜色偏必須指定作用在哪個影調段，不可全域

- **做法**：所有色彩指令都要標明落在 shadows／midtones／highlights 哪一段，例如
  `teal pushed into the shadows, highlights kept at a neutral white point`。至少保住一個中性參考點（通常是最亮的鏡面高光或白點）。
- **不照做會發生什麼**：全域色偏＝在整張圖上蒙一層色紙。黑位被抬起、白點被染色，反差看起來變糊變髒，
  而且畫面失去中性參考，人眼無從判斷偏色是刻意還是失誤，直接讀成「調色失敗」而非「風格」。
  若畫面是 `41 雙性照明`，全域色偏還會吃掉對側色，把冷暖對照整個抹平（同 `01 暖色調`／`38 冷色調` 的常見錯誤）。
- **與規則七的分工**：規則五管「色偏落在哪個亮度層」，規則七管「顏色落在哪個物件」。兩者要同時給。

#### 規則六｜「高級感」的可靠配方：低飽和 + 窄色域 + 高明度層次

- **配方（三者必須同時滿足）**：
  1. **低飽和**：環境整體飽和降 30–50%，重點色除外。
  2. **窄色域**：色相數 ≤3，且集中在色輪的一段窄弧內（類比色或限制調色盤）。
  3. **高明度層次**：同一色相內有清楚可分的多個明度階（實務目標抓五階），黑位不死、白位不爆。
- **提示詞**：`restricted three-hue palette held inside a narrow arc of the wheel, saturation kept low throughout, five clearly separated luminance steps running from deep shadow to highlight, blacks resting just above zero and highlights rolling off just below pure white, preserve natural skin tone`
  （「五階」模型不會真的去數，這句話的作用是把畫面往「保留階調分離」推；可靠的是它旁邊的黑位／白位相對描述。）
- **為什麼堆飽和常常得到反效果**（機制要講準）：
  1. **通道削頂**：拉飽和是把主導通道往上推，該色相的高光區先撞到上限，那個色相內部的階調分離**真的被壓掉**，畫面變平。
     這才是「層次不見了」的物理成因。
  2. **Helmholtz–Kohlrausch 效應**：高彩色塊看起來比它的實際亮度更亮，主體與背景的明度秩序被視覺攪亂，主從關係失效。
  3. **模型端連帶效應**：`vibrant` 這類詞常連帶拉高對比與銳度（見 `16 高飽和` 常見錯誤），三者疊起來就是「廉價」的完整配方——
     **色相多 + 每個都飽和 + 明度全擠在中間段**。
- **這不是唯一一條路**：高飽和本身不等於廉價，`圖二 11 三色印片` 就是高飽和的高完成度案例。
  它成立的條件是**色相數同樣受限**（紅、綠、藍三色不互相污染）**且用大量補光撐出明度層次**（光比 2:1、臉上沒有純黑）。
  換句話說，兩條路的共通條件都是「色相少 + 明度有階」，差別只在飽和度旋鈕轉到哪。
- **不照做會發生什麼**：想要質感卻只加 `vivid`、`rich colors`，得到的是彩度飽滿但層次全無的塑膠圖；
  高級感不在顏色的濃度，而在「顏色少、但每個顏色都有很多階明度可走」。

#### 規則七｜顏色必須綁在具體表面上，不可只寫抽象色名

- **做法**：寫 `oxblood velvet curtain`、`olive tiled wall`、`amber sodium streetlamp`，
  而不是 `red, green, orange palette`。每個色相至少指定一個承載物件。
- **不照做會發生什麼**：抽象色名沒有告訴模型顏色該落在哪，最省力的解法就是整張蒙一層色——
  你要的是配色關係，拿到的是色偏。這也是規則五的另一個面向：規則五定「哪個亮度層」，規則七定「哪個物件」，
  兩個座標都不給，模型只能全域套用。

#### 規則八｜綠—洋紅軸是膚色最脆弱的方向，動它要額外補償

- **做法**：需要綠調環境（醫院日光燈、地下室、末日場景）時，把綠色鎖在**光源與牆面**上，
  同句補 `preserve natural skin tone` 並加一條分離指令（膚色維持暖、且比環境亮一級）。
  需要洋紅／紫調時同理，把色相鎖在 practical 燈具上。
- **為什麼是這一軸**：人的白平衡適應能力在藍—黃（色溫）軸上很強，因為自然光源（日光、黑體輻射、燭火）本來就沿這一軸變動，
  觀眾看到整體偏藍或偏橘會自動解讀成「時間／光源不同」。綠—洋紅（tint）軸上幾乎沒有自然光源會這樣偏，
  所以同樣幅度的偏移不會被解讀成光源，只會被解讀成**設備出錯或人生病了**。
  這也是為什麼 `圖二 24 宇宙恐怖` 特別交代色溫軸與 tint 軸要分開下指令——紫與黃綠做不出來就是因為只動了色溫。
- **不照做會發生什麼**：綠色偏移會同時汙染牙齒、眼白與淺色衣物，這三處是觀者判斷「這張圖有沒有調壞」的基準點
  （它們接近中性又落在高明度，任何 tint 偏移在上面最明顯）。一旦轉綠，整張圖會被讀成白平衡失誤而非風格選擇。
  冷藍偏移只會讓臉變冷，綠偏會讓臉變病。
