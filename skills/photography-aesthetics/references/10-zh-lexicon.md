# 中文視覺標籤對照表

華語圈使用者說出口的視覺需求，八成不是「側逆光」或「低飽和」，而是「氛圍感」「高級感」「膠片感」「純欲」。
這些標籤在英文裡**沒有對應詞**，直譯必錯：`atmosphere`、`luxury`、`pure desire` 分別會把模型拉到風景霧景、金光珠寶、內衣廣告——三個方向都不是使用者要的。

本檔是**輸入層的翻譯表**，不是第 73 項技法。每一列的右半邊仍必須送進 `05-recipes.md` 的 11 槽固定組裝順序才成為完整提示詞；
本檔給的是「這個中文詞等於哪幾個軸的哪幾個值」，不是可以直接貼上去的成品。

**與 `06-analysis.md`〈使用者常說的話 → 他其實要的技法〉的分工**：
那張表處理**泛用形容詞**（要質感、要專業、不要太假、要有力量、要復古），本檔處理**有社群語境的專有標籤**（有出處、有流行週期、有明確視覺原型的那種詞）。
兩表重疊的項目（日系、韓系、高級、暗黑、ins 風、氛圍感、故事感、質感）**一律以本檔為準**，本檔的拆解更細且包含誤譯陷阱。
「復古」不在本檔——它是未定義的年代詞，走 `06-analysis.md` 該列的「先問年代再選載體」流程。

引用格式：`TNN` = 圖一攝影技法 48 項，`SNN` = 圖二影視風格 24 項（同 `05-recipes.md`）。

---

## 零、使用本檔的七條規則

1. **標籤不是提示詞，是查表的 key。** 使用者說「要有高級感」時，不要把 `high-end` 寫進提示詞，要查出這一列對應的軸值，再照組裝順序寫。中文標籤本身**永遠不出現在英文提示詞裡**（包含拼音，`gao ji gan` 對模型是雜訊）。

2. **一次只接受一個主導標籤。** 使用者丟兩個以上時走〈一之五〉的仲裁規則，不要把兩列的英文片語直接相加。

3. **兩級追問記號，不要混用。**
   - **【必問】**＝標籤內部有兩條**互斥且各佔一半**的視覺原型，沒有多數用法可當預設。**沒得到答案就不動工**，只回問題。目前有：膠片感、港風、學院風、國風／新中式。
   - **【問一句】**＝有分岔但存在多數用法。問一句，**使用者不答就走 A 支**並在輸出時標明。目前有：氛圍感、高級感、日系、原相機直出、街拍感。
   問法與 A／B 支的完整配方見〈四〉。

4. **人物年齡一律明寫成年。** 純欲、甜妹／元氣感、少年感、學院風、通透感這幾個標籤在中文語境天然帶年輕化描述，不寫年齡模型會往低齡漂。固定寫法：`a woman in her mid-twenties` / `a man in his late twenties`，寫在第 1 槽主體的最前面。若使用者同時要求未成年設定或校園制服元素，直接改為成年設定並說明，不照做。

5. **本檔所有 K 值指的是「光源色溫」，不是白平衡設定，兩者方向相反。** 白平衡數字調高畫面會變**暖**；決定畫面冷暖的是「光源色溫 ÷ 拍攝白平衡」的相對關係（見 `01-lighting.md` 36 冷光源、`02-tone-color.md` 01/38）。所以要冷就寫**高色溫光源配較低的白平衡**（`an overcast sky around 7000K shot on a 5600K daylight balance`），不要寫 `cool 6500K white balance`——那句話字面上要的是暖。凡表中出現冷／暖判斷，一律用「光源 K 值 + 白平衡 K 值」兩個數字表達。

6. **凡出現 T45 低飽和或強色偏的列，句尾補 `skin kept at natural saturation`**（SKILL.md 硬規則 9；`02-tone-color.md` 用語）。表中已寫進去的不用重複，表中沒寫的自己補。

7. **本檔片語只涵蓋第 4–11 槽，不含主體、動作、手、畫幅。** 直接貼上去會是一段沒有主體的形容詞堆。輸出前一定要補齊 SKILL.md〈輸出閘門〉的每一項，並補上畫幅（畫幅是必填的）。

---

## 一、中文視覺標籤 → 技法 → 英文片語

### 1-1 氣質與狀態類

| 中文標籤 | ≈ 技法編號 | 英文提示詞片語 | 常見誤解 |
|---|---|---|---|
| 氛圍感 **【問一句】** | T18 丁達爾光 + T05 背光 + T47 硬光 + T37 弱光 + T42 暗色調 + S05 煙霧體積光 | `low ambient level with haze thick enough to shape the beam but not to fog the subject, a hard backlight high and just outside the frame edge raking through it into defined shafts, dust motes drifting in the beam, subject turned away mid-action, an out-of-focus foreground object cutting into the frame edge, lit area held under a fifth of the frame` | 翻成 `atmospheric` 會拿到大霧風景與 HDR 天空；氛圍感的載體是**空氣中的介質**與被藏起來的資訊，不是色調。光質必須是 T47 硬光——柔光打進煙霧只會得到一片均勻霧，光束不成形（`05-recipes.md` 表 B） |
| 高級感 **【問一句】** | T09 柔光 + T45 低飽和 + T43 低對比度 + T35 居中構圖 + S03 北歐冷冽 | `a single directional source with no second fill and no second shadow, palette held to three neighbouring hues at roughly 20% saturation, matte surfaces with no sparkle and no polished metal, empty space filling more than 40% of the frame, highlights rolled off well below clipping and shadows still holding detail, skin kept at natural saturation` | 翻成 `luxury` 會得到金色、大理石、水晶、鏡面——那是「貴」；高級感是**資訊減量**，貴是資訊堆疊 |
| 電影感 | T04 側逆光 + T11 自發光 + T42 暗色調 + T46 高對比 + T25 淺景深 + S06 單光源夜戲 | `motivated practical sources visible inside the shot as the only key, the far side of the face falling three stops under, desaturated shadows that still hold detail, subject placed off-centre, 85mm at f/2 with an anamorphic-like oval falloff, skin kept at natural saturation, 2.39:1` | 誤解為「加上下黑邊 + 藍橙調色」；黑邊是結果不是原因，真正的來源是**畫面裡看得到光是從哪個燈來的**。畫幅寫在句尾，不要寫在句首（順序即權重） |
| 清冷感 | T08 窗光 + T38 冷色調 + T45 低飽和 + T43 低對比度 + T35 居中構圖 + S03 北歐冷冽 | `north-facing window light only, an overcast sky around 7000K shot on a 5600K daylight balance so the whole frame sits blue-grey, desaturated palette, low contrast with the blacks lifted, subject centred with empty space on all sides, not one warm accent anywhere in frame, skin kept at natural saturation` | 誤加暖色點綴「平衡畫面」；清冷的定義就是**畫面裡一個暖色都沒有**，加一個就破功。另：別寫 `cool 6500K white balance`，白平衡數字調高是變暖（見〈零〉第 5 條） |
| 鬆弛感 | T08 窗光 + T26 斜側視角 + T43 低對比度 + T24 動態模糊（微量） + S23 生活寫實 | `available window light only, subject off-centre with her weight on one hip and one shoulder dropped, gaze away from camera, one hand occupied with a cup, creased unironed linen, uneven headroom, slight motion blur on the near hand while the face stays sharp` | 翻成 `relaxed` 會得到「躺著微笑的圖庫模特」；鬆弛感是**姿態的不對稱與不完成**，不是表情 |
| 通透感 | T09 柔光 + T27 正面光 + T44 亮調 + T43 低對比度 + T19 近景 | `a soft source at least three head-widths across placed close and frontal, a white bounce lifting the shadow side to within one stop for a 2:1 key-to-fill ratio, one low-powered backlight behind the head so the earlobe and the outer rim of the ear glow red with subsurface light, a neutral-to-slightly-cool white point, the specular spread as a broad patch across the cheek rather than a hard point, background half a stop brighter than the face` | 翻成 `transparent` / `translucent` 會做出玻璃人或半透明材質；通透是**光比極小 + 次表面透光**。注意次表面透光需要光從耳後穿過來，純正面光的耳朵不會發紅——所以一定要補一盞弱背光，只寫柔正面光是做不出來的 |
| 氧氣感 | T05 背光 + T02 過度曝光 + T44 亮調 + T43 低對比度 + T25 淺景深 | `backlit haze wrapping the subject and lifting the front shadows two stops, background blown to near-white, minimal contrast, pale palette, loose strands of hair catching the rim, wide aperture with no hard shadow edge anywhere in frame` | 常與氛圍感混用；兩者相反——氧氣感是**亮、空、乾淨**，氛圍感是**暗、有介質、有缺口**。另：背光天生是最高對比，要低對比就**必須**明寫霧氣把暗部抬起來，否則會拿到剪影（`05-recipes.md` 表 B） |
| 故事感 | T20 中景 + T28 背面視角 + T34 封閉構圖 + T08 窗光 + S23 生活寫實 | `mid shot with the room readable behind, subject caught mid-action looking away from camera, framed through a doorway so the frame edges belong to the room, one object out of place in the foreground, available light only, no vignette and no colour grade` | 誤加濾鏡與暗角；故事感來自**資訊留白與可讀的環境**，調色一點都幫不上忙 |
| 高質感 | T03 側光 + T47 硬光 + T45 低飽和 + T25 淺景深 | `a hard side key raking across the surface at a 10 to 20 degree grazing angle so every ridge throws its own shadow, texture rendered by shadow rather than by resolution, restrained palette, matte materials with one controlled specular, 85mm at f/2.8, skin kept at natural saturation` | 誤加解析度堆砌詞；質感來自**光的入射角**，解析度只會讓塑膠感更清楚 |
| 治癒系 | T08 窗光 + T09 柔光 + T01 暖色調 + T43 低對比度 + T19 近景 + S23 生活寫實 | `late-afternoon window light through a cream curtain, the source warmed to roughly 3800K against a 5600K balance, a large white bounce opening the shadows, low contrast with the blacks lifted, pale warm palette, close framing on hands doing something small and ordinary, 50mm at f/2, skin kept at natural saturation` | 誤加高飽和明亮色；飽和一拉高就變成兒童節目。另：暖必須有物理來源（夕陽、米色窗簾、燈罩），只下 T01 暖色調而不指定光源，模型會整張蒙一層黃、膚色變髒橘 |
| 少年感 | T27 正面光 + T38 冷色調 + T44 亮調 + T43 低對比度 + T20 中景 | `flat bright overcast daylight straight on, cool-neutral balance, high-key with the blacks lifted and almost no modelling on the face, loose cotton clothing, mid shot with generous headroom, an unposed stance with the weight on one leg` | 誤用硬光雕輪廓；少年感的臉必須**幾乎沒有立體感**，一打側光就變成成熟男性肖像 |
| 甜妹／元氣感 | T27 正面光 + T44 亮調 + T01 暖色調 + T19 近景 + T24 動態模糊（微量） | `bright frontal daylight, warm high-key exposure, pastel palette with exactly one saturated accent, large round catchlights, close framing, caught mid-laugh with slight motion blur on the hair while the eyes stay sharp` | 誤走全高飽和；甜是**大面積粉調 + 單一重色**，全飽和會變成廣告傳單 |
| 御姐感 | T03 側光 + T47 硬光 + T46 高對比 + T39 低角度視角 + T32 特寫 | `a hard key high and 90 degrees to camera left leaving the far eye socket in shadow, an overcast-cool source around 6500K against a 5600K balance, dark saturated wardrobe, camera slightly below eye level, high contrast with the shadow side three stops under, tight medium close-up` | 誤翻成 `mature woman`（會把年齡拉高一到兩個級距）；御姐是**光與機位造成的權力關係**，不是年齡。另：5000K 是中性日光，不是冷色，別拿它當「冷」的數字 |
| 破碎感 | T37 弱光 + T42 暗色調 + T38 冷色調 + T25 淺景深 + T30 四分之三側面 | `underexposed by a stop and a half with half the face in shadow, cool desaturated palette, subject looking down and away, hair falling across one eye, the focal plane landing a centimetre behind the near eye, shadow noise left in place rather than cleaned up` | 誤加眼淚與誇張表情；破碎感靠**曝光不足與失焦**製造，表情越平越有效 |
| 頹喪／喪系 | T15 舞台光 + T37 弱光 + T42 暗色調 + T16 高飽和 + T24 動態模糊 | `a single overhead practical in a dim room, dense shadows, saturated colour crushed into the dark, subject slumped and sitting outside the light pool, slight motion blur, cluttered surfaces left exactly as they are` | 把畫面調乾淨；乾淨的光會讓頹廢變成時尚大片，**雜物與失焦是必要條件** |

> **S03 北歐冷冽的鎖定提醒**：高級感、清冷感、侘寂、ins 冷淡風、高級灰這五列都掛 S03，而 S03 本身鎖死 **T22 深景深（24mm / f/8）+ 近無影柔光 + 居中全身**，且與 `T25 淺景深`、`T47 硬光`、`T46 高對比`、`T03 側光`、`T01 暖色調` 直接衝突（`04-film-styles.md` 該條「衝突」欄）。要在這五列裡加淺景深或側光，就得先把 S03 拿掉，改從十軸自己組。

### 1-2 地域與文化風格類

| 中文標籤 | ≈ 技法編號 | 英文提示詞片語 | 常見誤解 |
|---|---|---|---|
| 日系 **【問一句】** | T08 窗光 + T09 柔光 + T44 亮調 + T43 低對比度 + T45 低飽和 + S23 生活寫實 | `soft diffused window light, high-key exposure with the blacks lifted so no true black appears anywhere, low contrast, pale palette with a faint cyan-green cast in the midtones, natural unretouched skin with visible pores, skin kept at natural saturation` | 誤加暖橘調色（那是台式婚紗）；日系的偏色是**青綠**，而且黑位必須抬起來 |
| 韓系 | T27 正面光 + T09 柔光 + T44 亮調 + T36 冷光源 + T25 淺景深 | `a large soft frontal source close to the lens and near shadowless, daylight-balanced with no warm bounce anywhere so the white point reads clean and cool, high-key skin with a dewy uneven sheen, one saturated accent colour against an otherwise neutral set, 85mm at f/2` | 誤把整體拉高飽和；韓系是**整體低飽和 + 單點重色**，且陰影幾乎為零。它的「冷」來自完全沒有暖補光，不是藍色調色 |
| 港風（霓虹夜街）**【必問】** | T41 雙性照明 + T16 高飽和 + T42 暗色調 + T25 淺景深 + S13 港片霓虹 | `rain-wet street at night lit only by shop practicals and neon tubes, magenta raking one side of the face and jade green the other at an even 1:1 with a dark band down the centre line of the nose, blacks crushed but tinted rather than neutral, 100mm at f/1.8 from across the road, framing partly blocked by a foreground grille, wet asphalt reflections stretching every light into a vertical smear` | 與人像港風是兩套完全不同的參數，不問就做必錯其一。另：**掛 S13 就不能再加 T45 低飽和**，會把風格包整個抵銷（`05-recipes.md` 表 B） |
| 港風（復古人像）**【必問】** | T41 雙性照明 + T03 側光 + T47 硬光 + T16 高飽和 + T32 特寫（**24 個風格包裡沒有對應項，不要掛 S13**） | `a hard 3200K tungsten key high and 45 degrees to camera left, a 6000K cyan-gelled fill on the shadow side sitting one and a half stops under the key with the two temperatures meeting along the bridge of the nose, a deep blue-red lip and a strongly defined straight brow, glossy black hair with one hard highlight band, seamless dark studio background, medium close-up at 105mm` | 誤用柔光美肌；港式人像的骨架是**硬光 + 濃妝 + 暖冷雙色**，柔光一上就變成現代韓系。另：S13 的定義整條都是夜街自發光（`04-film-styles.md`），套在棚拍人像上會把背景換成街景 |
| 新中式 **【必問，與國風二選一】** | T08 窗光 + T09 柔光 + T45 低飽和 + T35 居中構圖 + T34 封閉構圖 | `a palette of ink black, off-white and one muted vermilion accent held below 25% saturation, soft window light through a wooden lattice screen casting a geometric shadow across a plaster wall, dark elm and raw silk surfaces, symmetrical centred composition, more than half the frame left empty` | 誤堆金龍、鳳凰、紅燈籠——那是觀光紀念品；新中式是**留白 + 器物質感 + 一個克制的紅** |
| 國風 **【必問，與新中式二選一】** | T27 正面光 + T16 高飽和 + T43 低對比度 + T22 深景深 + S08 平面正面構圖 | `a saturated mineral-pigment palette of malachite green, azurite blue and cinnabar red, flat frontal light with almost no modelling and no cast shadow, layered silk garments with visible outlined edges, everything in focus, spatial depth compressed flat like a hanging scroll` | 與新中式常被混為一談，方向相反：國風是**高飽和工筆設色**，新中式是**低飽和留白** |
| 侘寂 | T08 窗光 + T09 柔光 + T45 低飽和 + T43 低對比度 + S03 北歐冷冽 | `raw unglazed clay, oxidised iron and lime-plaster walls, flat cool north daylight with no direct sun, the materials reading warm-grey while the light itself stays cool, visible chipping, water staining and asymmetry, matte with almost no specular anywhere` | 誤做成「米色極簡樣品屋」；沒有**磨損與不對稱**就只是無印風。注意「暖」只能寫在材質上，不能下 T01 暖色調——S03 與暖色調直接衝突 |
| 森系 | T09 柔光 + T45 低飽和 + T43 低對比度 + T21 遠景 + T22 深景深 + S23 生活寫實 | `overcast forest light filtered through leaves with no direct sun anywhere, green-leaning low-saturation palette, soft even contrast, linen and cotton clothing, the subject small within the foliage, deep focus so the forest stays readable` | 誤加陽光穿透與高飽和綠；森系必須是**陰天**，出太陽就變成旅遊照。也不要配淺景深——遠景 + 淺景深功能自相抵銷 |
| 民國風 | T03 側光 + T06 暖光源 + T45 低飽和 + T46 高對比 + S18 十六毫米顆粒 | `a hard warm tungsten key around 3000K through a window grille laying a barred shadow across the wall, sepia-leaning desaturated palette, dark wood and patterned cement floor tile, medium shot at 50mm, high contrast with the shadow side three stops under, skin kept at natural saturation` | 誤等同旗袍服裝；服裝只是道具，成立的關鍵是**顆粒 + 硬側光 + 去飽和的暖調**。顆粒與 halation 由 S18 自帶，**不要再另外寫一次**，會疊成兩倍粗（`07-beyond-the-charts.md` 排他規則） |

### 1-3 年代、載體與次文化類

| 中文標籤 | ≈ 技法編號 | 英文提示詞片語 | 常見誤解 |
|---|---|---|---|
| 膠片感 **【必問】** | 先選載體：S12 柯達克羅姆／S18 十六毫米顆粒／S17 VHS 錄影帶。**影調、對比、顆粒、色偏全部由選定的載體決定，不另外指定** | `shot on film rather than digitally — grain, highlight response and colour cast all come from the stock` ＋ 三選一：S18 → `soft negative highlight shoulder, shadows blocking up early and tinted slightly green, boiling midtone grain, red-orange halation around every highlight`；S12 → `dominant saturated reds and oranges, olive greens, dense blue-cyan blacks, highlights clipping abruptly with no roll-off, grain almost invisible`；S17 → `4:3, red chroma bleed smearing sideways, milky lifted blacks, clipped chalky highlights` | 直接套暖黃濾鏡 + 暗角＝手機 app 的假膠片。更危險的是**把三種底片的特徵混寫成一句**：「Kodachrome + 低對比 + 粗顆粒 + 柔和高光滾降 + 偏綠中間調」是四種互相矛盾的底片——Kodachrome 是高飽和高反差、亮部硬切、**幾乎無顆粒**（加顆粒等於換成別種底片），柔高光肩部 + halation + 偏綠陰影那一套是 S18（見 `04-film-styles.md` 12 與 18） |
| 原相機直出 **【問一句】** | 日間 T27 正面光 + T22 深景深 + T43 低對比度；夜間改掛 T48 閃光燈 + T46 高對比。**不掛任何載體風格包** | `a phone main camera at roughly 26mm equivalent, everything from foreground to background in focus, HDR pulling the shadows up so the blacks sit grey while local contrast stays high, over-sharpened contours with thin bright halos, mild luminance noise with smeared shadow detail, auto white balance settling slightly off neutral, framing casual with the horizon a degree or two off` | 翻成 `raw photo` / `unedited` 對模型沒有語意，而且 RAW 檔的視覺特徵剛好相反（平淡、低反差、高寬容度）。另外兩個常錯：**（a）不要掛 S14 數位早期**——S14 是 2000 年代 MiniDV 的 4:3 隔行標清、色度糊邊、日期字幕，與現代手機的計算攝影是兩套完全不同的成像；**（b）HDR 提亮暗部等於降低全域對比**，所以日間支要寫 T43 低對比度，寫 T46 高對比是把成因講反了 |
| 街拍感 | T20 中景 + T29 側面視角 + T24 動態模糊 + T22 深景深 + S23 生活寫實 | `available light only, 35mm zone-focused at f/8 with the whole street in focus, shot from chest height inside the crowd, subject unaware and mid-stride, cluttered background left uncleaned, slight motion blur on the near hand while the face stays sharp, one blown highlight left uncorrected` | 誤做成擺拍的時尚外景；街拍的可信度來自**沒對到眼神 + 背景沒整理 + 曝光沒修正**。另：**S10 手持跟拍在靜態圖上幾乎無效**（SKILL.md 明列），生圖時改用上面那兩句成像瑕疵片語替代；長焦 + 深景深也是互相打架的組合，要深景深就用廣角區域對焦 |
| INS 風 | T04 側逆光 + T10 髮絲光 + T01 暖色調 + T25 淺景深 + S04 魔幻時刻 | `the sun 5 to 15 degrees above the horizon directly behind the subject, a warm rim along the hair, hazy lifted highlights with veiling flare washing one corner, creamy out-of-focus background at 85mm f/1.8, close framing` | 誤加高飽和藍天；INS 風的天空必須是**過曝發白**的，藍天會把它變成旅遊廣告 |
| ins 冷淡風 | T09 柔光 + T36 冷光源 + T45 低飽和 + T43 低對比度 + T35 居中構圖 + S03 北歐冷冽 | `flat overcast light around 7000K on a 5600K balance, a near-monochrome off-white and grey palette, camera perpendicular to the back wall with the vanishing point dead centre, low contrast with no shadow drama, a single object centred with heavy empty space around it, skin kept at natural saturation` | 與 INS 風只差一個字但完全相反：一個是**暖逆光淺景深**，一個是**冷平光深空間**。另：不要同時掛 S03 與 S08——一列只能有一個風格包，平貼構圖改用 T35 居中構圖這個軸值表達 |
| 老錢風（quiet luxury） | T09 柔光 + T08 窗光 + T45 低飽和 + T43 低對比度 + T20 中景 | `overcast north light through a large window, palette limited to navy, camel and cream, no logos and no visible branding anywhere, cashmere and worn leather with the weave readable, wide framing inside a large plain room, muted contrast with no pure black and no pure white in frame, skin kept at natural saturation` | 寫 `luxury` / `rich` / `expensive` 會得到金錶跑車；老錢風的定義是**看不出價格**，所以必須明寫 no logos。「色彩控制在兩級以內」是**影調**的說法不是配色的說法（藏青與奶油本身就差三四級），要壓的是對比不是色相亮度 |
| 千禧辣妹（Y2K） | T48 閃光燈 + T27 正面光 + T16 高飽和 + T42 暗色調 + S14 數位早期 | `direct on-camera flash at night, the nearest surface blown and the background falling to black a metre behind, saturated magenta and chrome accents, early small-CCD colour with the reds clipping and bleeding sideways, in-camera oversharpening halos, harsh specular on the skin, centred snapshot framing` | 誤做成乾淨的復古時尚棚拍；Y2K 的核心是**直閃 + 低階數位成像**，燈打漂亮就不成立。掛 S14 時只取它的**感光元件與編碼特徵**，隔行梳狀邊緣、日期字幕那類錄影專屬瑕疵要刪掉——那是攝影機不是相機 |
| 賽博 | T41 雙性照明 + T16 高飽和 + T42 暗色調 + T37 弱光 + T39 低角度視角 + S21 賽博龐克街景 | `rain-slick night street, layered neon signage in cyan and magenta, volumetric haze, wet asphalt reflections stretching every light into a vertical smear, a 3200K sodium pool warming the near pavement against a 6500K cyan ambient with the two meeting at the kerb, camera below eye level, blacks dense but tinted` | 誤加大量機械義肢與 UI 疊層；賽博感的來源是**濕地面 + 體積霧 + 雙色霓虹**，不是道具 |
| 學院風（暗黑學院）**【必問】** | T41 雙性照明 + T42 暗色調 + T46 高對比 + T34 封閉構圖 + S06 單光源夜戲 | `a single tall window as the key at 5600K with the room falling off deep behind it, one 2700K desk lamp as the only other source sitting two stops under, the two temperatures meeting at the near edge of the desk, oxblood and forest-green tweed, aged paper and dark oak, low-key with the shadows still holding texture` | 與美式預科完全相反（一暗一亮），不問就做必錯其一。另：原本「窗是唯一光源，然後桌燈是第二個實用光源」是自相矛盾的寫法——要兩個色溫就得走 T41 並明寫哪一側、交界在哪、差幾級（`05-recipes.md` T41 例外條款三條件） |
| 學院風（美式預科）**【必問】** | T27 正面光 + T09 柔光 + T44 亮調 + T22 深景深 + T20 中景 | `bright overcast daylight on a brick and ivy facade, navy and cream palette, crisp mid contrast with accurate colour and no cast, everything in focus, mid shot at 50mm` | 同上 |
| 廢土 | T40 強光 + T47 硬光 + T02 過度曝光 + T21 遠景 + S15 沙塵單色 | `dust-laden air under a hard midday sun almost overhead, sand and rust as the only two hues so the frame reads near-monochrome, blown highlights left uncorrected, cracked concrete and oxidised metal, wide shot with the figure occupying under a tenth of the frame height, coarse grain` | 誤用日落美光；廢土必須是**正午硬光，無處可躲**。另：掛 S15 就把整個色彩槽讓給它，不要再另外下飽和度指令，改寫 `tonal separation` 這類明度描述（`05-recipes.md` 表 B）。也不要同時要 T02 過度曝光與 T46 高對比——兩者對高光的處理直接矛盾 |
| 暗黑系 | T42 暗色調 + T46 高對比 + T04 側逆光 + T14 輪廓光 + T36 冷光源 + S06 單光源夜戲 | `low-key with small pools of light on a mostly dark frame, a cool 6500K rim separating the silhouette from the background, a hard undiffused key with the shadow side four stops under, shadows retaining texture and noise, no lifted blacks` | 誤解為「整張壓暗」；壓曝光只會糊成一團，正解是**縮小亮部面積**並保留暗部細節 |
| 蒸汽波 | T15 舞台光 + T41 雙性照明 + T16 高飽和 + T35 居中構圖 + S17 VHS 錄影帶 | `a magenta and cyan gel wash split left and right meeting at the centre line of the frame, chrome and pastel plaster surfaces, flat frontal composition with rigid symmetry, VHS-era chroma bleed smearing to the right and visible scan lines, one hard shadow thrown by a low source` | 誤與賽博混用；蒸汽波是**平面、對稱、粉調、室內**，賽博是**縱深、濕、暗、街道** |
| 多巴胺風 | T27 正面光 + T16 高飽和 + T44 亮調 + T23 全身照 + S08 平面正面構圖 | `flat bright light with no shadow drama, saturated complementary blocks of colour against a plain seamless background, crisp edges with no gradients anywhere, centred full-length framing, skin kept at natural saturation` | 誤加漸層與光暈；多巴胺的邏輯是**色塊相撞**，任何柔化都會削弱它 |
| 美拉德風 | T04 側逆光 + T01 暖色調 + T45 低飽和 + T43 低對比度 | `a low late-afternoon back-side light skimming the shoulder, a warm brown-to-caramel palette held inside a 30 degree hue range, matte suede and wool with the weave raking, saturation low with the midtones warm, medium contrast, skin kept at natural saturation` | 誤拉高飽和變成橘色；美拉德是**窄色域的棕階**，飽和一高就變成秋季促銷。另：技法選了 T04 側逆光，英文就不能只寫 `side light`——那是 T03，兩者陰影落點不同 |
| 高級灰 | T09 柔光 + T45 低飽和 + T43 低對比度 + T35 居中構圖 + S03 北歐冷冽 | `overcast light, a palette of five closely spaced desaturated greys plus one much darker anchor tone, matte plaster and brushed metal, low contrast, camera square to the wall with the subject centred` | 誤做成全灰無層次；高級灰的關鍵是**灰階之間必須有明度差**，且要有一個最深的錨點。同 ins 冷淡風：一列只掛一個風格包 |
| 黑金風 | T47 硬光 + T42 暗色調 + T46 高對比 + T06 暖光源 + T39 低角度視角 | `a single hard 3000K source in a dark room, warm amber specular running as thin lines along brushed brass and black stone, gold occupying under a tenth of the frame area, dense blacks with no lifted shadows, camera below eye level` | 誤加大量金色面積；黑金的比例是**九黑一金**，金只能是高光線條 |
| 工業風 | T41 雙性照明 + T22 深景深 + T46 高對比 + T34 封閉構圖 | `bare tungsten bulb practicals at 2800K hanging against a 7000K north skylight, the two temperatures split along the line of the roof truss with the warm side one stop under the daylight, exposed concrete, brick and oxidised steel, deep focus at f/8, a high ceiling closing the frame at the top` | 誤把色溫統一；工業風的真實感正來自**冷天光與暖燈泡混色**。但混色一旦成立就**不能再加 T45 低飽和或 T43 低對比度**——那兩者會把好不容易分開的兩個色溫壓回同一團灰（`05-recipes.md` T41 例外條款結尾） |
| 硬照／大片感 | T47 硬光 + T46 高對比 + T27 正面光 + T35 居中構圖 + S08 平面正面構圖 | `a hard undiffused key straight on with a crisp shadow edge on the wall behind, background raked into deep falloff, high contrast with the highlight held just under clipping, a static frontal pose with the weight even on both feet, 135mm for flat perspective` | 誤加淺景深與柔光；硬照的語言是**硬光 + 靜止姿態 + 壓縮透視**，柔化就變成沙龍照 |

### 1-4 人物膚感與妝容類

| 中文標籤 | ≈ 技法編號 | 英文提示詞片語 | 常見誤解 |
|---|---|---|---|
| 純欲 | T27 正面光 + T09 柔光 + T10 髮絲光 + T44 亮調 + T45 低飽和 + T32 特寫 | `an adult woman in her mid-twenties, a large soft frontal source with a faint backlight edge falling only along the shoulder line and the jaw, high-key skin with pores open across the nose and inner cheeks and an uneven dewy sheen, bare makeup with a glossy neutral lip and soft unshaped brows, white and skin-tone fabrics, close framing on the collarbone and jaw, direct gaze with a blank unsmiling expression, skin kept at natural saturation` | 翻成 `sexy` / `seductive` 會抽樣到內衣廣告的濃妝與誇張姿態，方向完全相反；純欲的張力來自**妝素、光亮、料薄**三者並存 |
| 冷白皮 | T09 柔光 + T36 冷光源 + T38 冷色調 + T44 亮調 | `a 6500K source on a 5600K balance so the skin sits blue-leaning, pale skin with visible capillaries at the nostril crease and a cool grey-blue in the shadow side, soft frontal light, no warm bounce anywhere in frame` | 寫 `white skin` 會改變模型對族裔的判定、寫 `porcelain` 會做出無毛孔陶瓷；冷白皮是**光源與白平衡的相對關係 + 陰影色相**的事，不是膚色詞 |
| 素顏感／偽素顏 | T08 窗光 + T09 柔光 + T43 低對比度 + T19 近景 + S23 生活寫實 | `bare skin with pores open across the nose and inner cheeks, uneven pigmentation and slight redness around the nose and ears, tinted lip balm only, brows left unshaped, soft window light` ＋ 依模型分流的 `no skin smoothing, no beauty retouching` | 誤寫成無妝＝乾燥暗沉；偽素顏是**有修飾但看不出修飾**，關鍵是保留毛孔與不均勻，而不是拿掉光澤。那兩句否定的擺放位置照 `07-beyond-the-charts.md` 皮膚組的分流規則，不要夾在提示詞中段 |

### 1-5 多標籤同時出現時的仲裁規則

使用者一次丟兩三個標籤是常態（「日系一點但要有高級感」「港風但要通透」）。不要把兩列的英文片語相加——那會產生互相抵銷的指令。照這個順序處理：

1. **先看影調是否衝突。** 兩個標籤如果一個屬亮調群、一個屬暗群，**必須先問**，不得自行折衷；折衷的結果是中灰無個性。
   - 亮調群（T44 亮調）：日系、韓系、通透感、氧氣感、少年感、甜妹／元氣感、純欲、學院風（美式預科）、多巴胺風、冷白皮
   - 暗群（T42 暗色調）：氛圍感、電影感、港風（霓虹夜街）、破碎感、頹喪／喪系、賽博、學院風（暗黑學院）、暗黑系、黑金風、千禧辣妹
2. **影調不衝突時，取「先說的那個」為主導標籤**，鎖定它的全部軸值。
3. **第二個標籤只允許貢獻色彩軸或質感層**，最多改寫 2 個軸（同 SKILL.md 風格包覆寫上限）。例：「日系 + 高級感」＝日系鎖定光位光質影調，高級感只貢獻「色域收窄到三色 + 材質改啞光」。
4. **第三個以上的標籤一律丟棄**，並在回覆中明講丟了哪一個、為什麼。
5. **兩個標籤各自帶風格包時，只留主導標籤的那一個。** 一列一個 S，多的那個展開成軸值寫。

常見組合的既定裁決：

| 使用者說 | 裁決 |
|---|---|
| 日系 + 膠片感 | 相容。日系鎖光與影調，膠片感只掛 S18 的顆粒與 halation，不動色彩 |
| 韓系 + 高級感 | 相容。韓系鎖正面柔光，高級感把「單點重色」降為無彩色 |
| 高級感 + 老錢風 | 高度重疊，不要疊。統一走老錢風（它多了服裝與材質的具體規定），並在回覆中說明兩者只差在有沒有指定衣料 |
| 高級感 + 淺景深 | **不相容於 S03 路線**。S03 鎖 f/8 深景深。要淺景深就把 S03 拿掉，改從 T09 + T45 + T43 自己組 |
| 原相機直出 + 電影感 / 淺景深 | **衝突**（小感光元件全景深 vs 大光圈虛化）。直接告知互斥並請使用者二選一，不要折衷 |
| 工業風 + 高級感 | **衝突**（雙色溫分離 vs 低飽和低對比）。低飽和會吃掉混色，必問 |
| 氛圍感 + 通透感 | **衝突**（暗 vs 亮、有介質 vs 無介質）。必問 |
| 港風 + 清冷感 | **衝突**（高飽和暖冷雙色 vs 全冷低飽和）。必問 |
| 賽博 + 高級感 | **衝突**（高飽和堆疊 vs 資訊減量）。必問；使用者通常要的是「冷色調的高級感」而非賽博 |

---

## 二、六個最容易翻錯的標籤：深度拆解

### 2-1 氛圍感

**真正所指**：畫面裡有「沒說完的話」。華語圈用這個詞時，指的其實是兩件事的疊加——**空氣是可見的**（光有形狀），以及**資訊是不完整的**（主體沒看鏡頭、動作在中途、有東西擋住）。它描述的是觀看者的心理狀態，不是畫面的色調。

**拆成技術參數**：
- 介質：`haze` / `dust motes` / `steam`，濃度寫成「光束邊緣可辨但主體不糊」。沒有介質，逆光只會拍出剪影，拍不出氛圍。
- 光位：T05 背光或 T04 側逆光，光源必須高於主體且靠近畫面邊緣，光束才有斜度。
- **光質：必須是 T47 硬光。** 丁達爾光需要接近平行的光束打進介質才會成形；柔光在煙霧裡只會變成一片均勻霧，光束根本不出現。這一條是最常被漏掉的，因為「氛圍」聽起來很軟。
- 環境照度：T37 弱光。氛圍感的亮部面積上限約全畫面 20%。
- 主體朝向：T28 背面視角或 T26 斜側視角，**禁止與鏡頭對視**——對視會把注意力從空氣拉回臉上。
- 前景：畫面邊緣要有一個失焦遮擋物（門框、樹葉、人的肩膀）。

**為什麼直譯失敗**：`atmosphere` / `atmospheric` 在英文攝影語境裡幾乎都繫在風景攝影（山霧、湖面、日出），寫進人像提示詞很容易把背景換成山谷。`moody` 則傾向只拉低整體曝光而不加介質，得到一張「單純很暗」的圖。

### 2-2 高級感

**真正所指**：**控制**。看得出畫面裡的每一個元素都是被允許存在的，其餘都被拿掉了。華語圈說「高級」時，反義詞不是「便宜」，是「用力」——金色、漸層、光暈、多光源、滿版都屬於用力。

**拆成技術參數**：
- 色彩：色相數 ≤ 3 且相鄰，飽和度（以 HSB 的 S 為準）壓在 20% 上下。這是最關鍵的一條，違反了其他全部做對也沒用。
- 光源：只有一個方向明確的光源，禁止第二個補光造出第二組陰影。
- 材質：全部啞光（`matte`），禁止鏡面、亮片、水晶、拋光金屬。
- 影調：對比可以高，但高光必須壓在破點之下（`highlights rolled off well below clipping`），暗部要留細節。
- 構圖：留白佔比 ≥ 40%，T35 居中構圖或嚴格對稱。
- 景深：走 S03 路線時鎖 f/8 深景深；要淺景深就別掛 S03。

**為什麼直譯失敗**：`luxury` / `high-end` / `premium` 在圖像語料裡被電商與廣告圖佔滿，指向的是「昂貴物件的視覺清單」——金箔、大理石、香檳、水晶吊燈、絲絨、反光。模型照做的結果是暴發戶感，與使用者要的**減法**恰好相反。若使用者要的真的是「貴」而不是「高級」，那要走黑金風那一列。

### 2-3 通透感

**真正所指**：皮膚看起來**是有厚度而且會透光的**，畫面裡沒有髒的暗部。這個詞幾乎只用在人像與美妝，核心是**光比**而不是修圖。

**拆成技術參數**：
- 光比：主光與補光差距壓到 1 級以內，也就是 2:1，比一般人像的 3:1（約 1.6 級）更平；追求極致時到 1.5:1。
- 光源尺寸：光源直徑 ≥ 主體頭部三倍，且距離近；這樣高光才是「一片」而不是「一點」。
- **次表面散射需要一盞背光才成立。** 光從耳廓與鼻翼透過來才會發紅，而透過來的前提是光在**後面**。只寫大面積正面柔光，耳朵不會亮。正確寫法是「正面柔光為主 + 一盞低功率背光」：`one low-powered backlight behind the head so the earlobe and the outer rim of the ear glow red with subsurface light`。直接描述透光的部位，比任何抽象詞有效。
- 白平衡：中性偏冷。偏暖會變成「油」，那是通透感的反面。
- 背景：比臉亮 0.5 級，且無雜色。背景一暗，臉再亮也不通透。

**為什麼直譯失敗**：`transparent` / `translucent` 是**材質詞**，模型會照做——把皮膚渲染成半透明樹脂，或直接生出玻璃人像。`clear skin` 則容易抽樣到痘痘藥廣告的修圖語料，抹掉毛孔，變成塑膠。

### 2-4 鬆弛感

**真正所指**：**沒有在配合鏡頭**。這是一個關於「姿態與時機」的詞，跟光完全無關——把一張擺拍照片調成任何色調都不會產生鬆弛感。

**拆成技術參數**：
- 重心：`weight on one hip` / `leaning on the door frame`——身體必須有一邊在承重，站得正就是緊繃。
- 四肢：不對稱，且手要有事做（拿杯子、撥頭髮、插口袋）。空著的手是擺拍的最大破綻，也是模型畫壞手的主要場合。
- 視線：離開鏡頭。
- 服裝：`creased linen` / `an unironed shirt collar turned up on one side`。燙平的衣服會摧毀鬆弛感。
- 快門：微量動態模糊，用 `07-beyond-the-charts.md` 成像瑕疵組的完整片語 `slight motion blur on the near hand while the face stays sharp`（後半句不可省，省掉會整張糊）。
- 構圖：T26 斜側視角、主體偏離中心、頭上留白不均。

**為什麼直譯失敗**：`relaxed` 在圖像語料裡對應的是「躺著、閉眼、微笑、spa」，得到的是一張圖庫式的放鬆照片；`effortless` 則傾向被當成時尚術語，拉出擺拍過的街拍時尚圖——外表隨意但每個關節都在鏡頭上。

### 2-5 原相機直出

**真正所指**：**手機內建相機、沒開濾鏡、沒修圖**的那一整套成像特徵。使用者說這句話時要的不是「真實」，而是一組非常具體的技術缺陷。

**拆成技術參數**：
- 焦段與景深：約 26mm 等效、小感光元件 → **深景深**（T22），畫面幾乎全焦。
- 動態範圍：手機 HDR 會把暗部大幅提亮 → `HDR-lifted shadows`，暗部發灰而不是死黑。**注意方向**：暗部被抬起等於**全域對比下降**（同時局部對比很強），所以日間支要下 T43 低對比度，不是 T46 高對比。
- 銳化：過度銳化，輪廓有白邊 → `slightly over-sharpened edges with thin halos along contours`。
- 抹噪：暗部細節被塗抹但仍留亮度雜訊 → `mild luminance noise with smeared shadow detail`。
- 白平衡：略偏離中性。各廠牌的自動白平衡傾向不同，且逐代在變，**不要寫死是偏冷還是偏暖**；寫 `auto white balance settling slightly off neutral` 就足以產生那個味道。
- 夜間：直閃（T48），近處過曝、背景全黑，此時才是 T46 高對比。
- 構圖：隨手，地平線微歪，主體位置不講究。

**為什麼直譯失敗**：`raw photo` 會被理解為 RAW 檔（高寬容度、平淡低對比的專業素材），與手機直出正好相反；`unedited` / `no filter` 是後製語彙，對模型沒有可執行的畫面語意。

**兩條互斥警告**：
- 原相機直出與 T25 淺景深、85mm、f/1.4 完全互斥——一旦同時出現，模型會生出一張「用單眼拍的假直出」，中文使用者一眼就看得出來。
- **不要掛 S14 數位早期。** S14 是 2000 年代 MiniDV：4:3 隔行、720×480、色度水平糊邊、角落日期字幕、鏡頭廣角端一點都不廣。那是攝影機的胎記，跟現代手機的計算攝影完全不同一套。24 個風格包裡沒有對應項，這一列只能從軸值直接寫。

### 2-6 純欲

**真正所指**：**「純」與「欲」兩組相反訊號同時出現**。純來自妝容與色彩（素、白、亮、乾淨），欲來自身體線條與光的邊緣（鎖骨、頸肩、薄料、逆光輪廓）。少了任何一邊都不成立：只有純＝清水照，只有欲＝內衣廣告。

**拆成技術參數**：
- 主光：T27 正面光 + T09 柔光，大面積、高位、近距離，把臉打平打亮。
- 邊緣光：T10 髮絲光或一道微弱的側逆光，**只落在肩線與下顎緣**，不打亮身體正面。
- 影調與色彩：T44 亮調 + T45 低飽和，畫面主色是白、裸、淺灰，句尾補 `skin kept at natural saturation`。
- 妝：`bare makeup with a glossy neutral lip, brows left soft`——禁止煙燻、深唇、假睫。
- 質感：皮膚要有毛孔與不均勻的水光（用 `07-beyond-the-charts.md` 皮膚組的 `pores open across the nose and inner cheeks`），完美無瑕會倒退回廣告修圖。
- 表情：直視鏡頭但**表情放空**。微笑會轉成甜妹，挑眉會轉成御姐。
- 景別：T32 特寫或 T19 近景，取鎖骨與下顎，不取全身。

**為什麼直譯失敗**：`sexy` / `sensual` / `seductive` 傾向抽樣到內衣與泳裝廣告——濃妝、高飽和、暖光、誇張姿態，六項參數全部反向。`innocent` 則會把年齡拉低，是必須避免的方向。

**硬規則**：這一列必須明寫成年（`an adult woman in her mid-twenties`），且不寫任何暗示未成年的詞（school uniform、schoolgirl、childlike、petite、校園場景一律不用）。使用者若堅持要未成年設定，改為成年設定並說明，不照做。

---

## 三、中文使用者的兩條硬規則

### 3-1 亞洲主體必須明寫具體族裔描述

**問題**：多數國際主流影像模型的訓練分佈以歐美影像為主，提示詞未指定族裔時就落到那個預設，生出白人臉；只寫 `Asian` 時則生出一張「泛亞平均臉」——常混入東南亞、東亞與白人特徵，中文母語觀眾一眼看出「不是我們」。這不是模型的美學問題，是機率分佈問題，只能用**具體描述**壓過去。

> **模型差異**：以中文語料為主訓練的模型（Seedream 一類）預設分佈本來就偏東亞，未指定時未必生出白人臉。但**規則不變**：不指定就是把臉交給預設分佈，換一個模型、換一個版本結果就變。這一段的預設行為會隨模型版本改變，跨模型時請以實測為準。

**錯誤寫法**

| ✗ 寫法 | 模型會給你什麼 |
|---|---|
| `a young woman with long dark hair, soft window light` | 白人臉配黑髮。未指定＝走預設分佈 |
| `an Asian woman` | 泛亞平均臉，五官比例與髮質都不特定，換一次 seed 就換一個族群 |
| `a girl with mixed features, exotic look` | 直接得到混血臉；`exotic` 另外會抽樣到獵奇與物化語料 |
| `almond-shaped eyes, oriental beauty, porcelain skin` | 刻板詞三連。`oriental` 抽樣到殖民時期語料，`porcelain` 生出無毛孔陶瓷皮膚 |
| `a woman in Taipei` | **地點不等於人種**。模型會生出一個白人站在亞洲街景裡。這是最高頻的錯誤 |

**正確寫法：五段結構，寫在第 1 槽主體的最前面**

`國別／地區 + 年齡 → 髮（長度、剪法、質地）→ 骨相（挑 2–3 個具體特徵）→ 膚色與妝 → 服裝`

女性範例：

`a Taiwanese woman in her early thirties, straight black hair cut blunt at the collarbone with a centre parting, a low nose bridge with a rounded tip and broad flat cheekbones, warm olive skin with slight redness at the nostril crease, bare-skin makeup with a matte coral lip, an oversized ecru linen shirt`

男性範例：

`a Korean man in his late twenties, black hair in a grown-out undercut falling over the ears, a straight brow line, flat cheekbones and a squared jaw, neutral fair skin with a faint stubble shadow along the jaw, a charcoal crew-neck knit`

> 這兩段只是第 1 槽的**身分描述**，還不是完整的主體。後面必須接上動作、姿態重心、手的狀態、視線與表情，才通得過 SKILL.md 的〈輸出閘門〉。

**四條執行規則**

1. **族裔詞用具體國別／地區**（`Taiwanese` / `Japanese` / `Korean` / `Hong Kong Chinese` / `northern Chinese`），不要只寫 `Asian`。`East Asian` 是可接受的下限，用在明確不想指定國別時。
2. **骨相特徵一次只挑 2–3 個。** 把所有東亞特徵一次寫滿會製造刻板臉。挑選原則：寫「這一個人長什麼樣」，不是寫「這個族群長什麼樣」。可用的具體詞：`low nose bridge`、`broad flat cheekbones`、`monolid eyes` / `a shallow double eyelid crease`、`a rounded jaw`、`a short philtrum`、`fine straight hair with a strong shine`。（避免寫 `malar cheekbones`——malar 本身就是顴骨，那是贅詞。）
3. **禁用刻板詞**：`oriental`、`exotic`、`almond eyes`、`porcelain skin`、`doll-like`、`China doll`、`geisha-like`。另外 `K-pop idol` 會把臉推向風格化的均值臉，也不要用。替代方式一律是**具體五官描述 + 具體妝容 + 具體服裝**。
4. **不要用否定式**。`not white`、`no Caucasian features` 對多數模型無效；模型不擅長處理否定，反而會被 `Caucasian` 這個 token 影響。要排除只能靠正面描述壓過去。

**三個容易漏掉的場合**

- **多人畫面：每一個人都要單獨寫。** 只寫第一個人的族裔，第二、三個人會回到預設分佈。寫法：`three East Asian colleagues — a Taiwanese woman in her forties with short permed hair, a Japanese man in his twenties with round wire glasses, and a Korean woman in her thirties with a low bun`。注意同時受 SKILL.md 硬規則 13 限制：**超過 3 張正臉模型會崩臉**，第四人以上改側臉、背影或推進失焦區。
- **背景路人也要寫一句**：`the passers-by in the background are also East Asian`。否則街景會出現一群白人。
- **image-to-image 與參考臉**：即使掛了參考圖或 Soul 角色，文字裡仍要重述族裔與 2–3 個骨相特徵。二次生成與高重繪強度會讓臉往預設分佈漂白。

### 3-2 中文字入畫：預設不生成

**問題**：影像模型生成漢字的錯誤率仍然很高——缺筆畫、偏旁錯置、左右結構顛倒、生出似字非字的符號。主要成因是漢字的字形空間遠大於拉丁字母，而文字細節在生成過程的低解析度中間表示裡最先被壓掉；筆畫多、結構複雜的字（含多數繁體字）錯得更明顯。

> **這是本檔時效性最短的一段。** 各家模型的中文渲染能力逐版在變，部分模型已能穩定生出短字串。**不要把任何一家模型的當前表現寫死在提示詞策略裡**；下面的規則是「在不知道目標模型當前實測表現時的安全預設」。若已知目標模型且已實測過，以實測為準。

**預設規則：提示詞不要求生成任何漢字，改為在畫面預留乾淨區塊，文字用後製加上。**

三種預留寫法：

| 情境 | 英文提示詞片語 |
|---|---|
| 招牌／看板 | `a plain matte signboard above the door, the surface left completely blank, evenly lit with an unbroken painted finish` |
| 包裝／產品 | `a matte off-white carton with a clean unprinted front panel, soft even light across the panel, the label area left empty` |
| 海報／書封／首圖 | `a poster on the wall with a solid flat colour field occupying the upper third, clean straight edges, even illumination across the empty area` |

**否定句的分流**（照 `07-beyond-the-charts.md` 皮膚組同一套規則）：`no lettering` / `no glyphs` / `no text of any kind` 這類否定，對 GPT Image 2、Nano Banana 這類指令遵循型模型有效，直接寫在該物件之後；對 Midjourney 用 `--no text, --no lettering`；對有 negative prompt 欄位的模型移進去。**若目標端點根本沒有 negative prompt 欄位（Flux 的多數官方端點就沒有），就只能靠正面描述**——`an unprinted blank panel`、`a solid colour field`、`an unbroken painted surface`。各模型的實際欄位以 `09-model-dialects.md` 為準。

**次佳解：讓字不可辨**（成本最低、成功率最高，街景與夜景一律優先用這個）

- `neon signage reduced to unreadable glowing strokes by defocus, bokeh discs forming along the sign edge`
- `signage cropped by the frame edge so that only part of one character enters the shot`
- `signage seen at a steep oblique angle, the strokes compressed until unreadable`

**風格包警告**：`S13 港片霓虹`、`S21 賽博龐克街景`，以及任何夜街場景，**幾乎一定會自動長出招牌**，即使提示詞沒提到——因為招牌是這兩個風格包視覺定義的一部分。用到它們時必須主動補上失焦、裁切或留白指令，否則畫面裡就會出現似字非字的符號。（`S14 數位早期` 本身不含街景，只有在你自己把場景設在街上時才需要注意。）

**非要生成漢字時的六條規則**

1. **控制在 2–4 字。** 字數越多錯誤率越高，且是陡升不是線性；超過四字基本上不值得嘗試。
2. **選常見、筆畫少的字**（山、日、月、大、小、中、口、早、安、門、店）。避開多筆畫繁體字（豐、聲、灣、藝、鑫）。同一組字盡量不要混用筆畫數差距很大的字。
3. **逐字列出並要求精確**：`large signage reading exactly the two characters 早 安, rendered as flat solid strokes`。
4. **字要大、要正、要平**：佔畫面寬度 1/3 以上，`shot straight on with the sign parallel to the sensor plane, even frontal light, high contrast between the characters and the background, no perspective distortion, no handwriting or decorative serifs`。小字、斜角、手寫體、反光面全部會大幅提高錯誤率。
5. **排除多餘文字**：句尾加 `no additional characters anywhere else in the frame`（否定句照上面的分流規則擺放）——模型常在畫面其他地方自行補上亂碼。
6. **預期要重生多次逐張挑選**，不要相信第一張；實際需要幾次隨模型與字數變動很大，先跑三、五張評估命中率再決定要不要繼續。agent 若無法檢視生成結果，**必須主動在回覆中提醒使用者人工逐筆核對漢字**，並附上預期的正確字形。

---

## 四、模糊中文標籤 → 一題收斂

**提問三原則**

1. **只問一題，且必須是封閉二選一。** 中文標籤的問題不是資訊不足，而是**標籤內部有兩條互斥路線**；問題要切在那條分岔線上，不要問「你想要什麼感覺」。
2. **兩個選項都用「畫面會長什麼樣」描述，不用技術詞。** 使用者不知道什麼叫低對比，但知道「臉一半在暗處」。
3. **【問一句】的標籤，使用者不答就走 A 支**（A 一律設為該標籤的多數用法），並在輸出時標明走了哪一支、怎麼改到 B。**【必問】的標籤沒有 A 支預設**（膠片感、港風、學院風、國風／新中式）——兩條路線各佔一半，猜錯是整張重做，沒得到答案就只回問題不動工。

---

**實例 1｜氛圍感【問一句】**

> 使用者：幫我生一張有氛圍感的照片。
> Agent：氛圍你要「看得見的光」還是「看不見的臉」？**A** 空氣裡有霧、逆光打出光束、輪廓在發亮；**B** 整體很暗很安靜，臉有一半在陰影裡，只有一小塊亮。

- A（不答走這支）→ `T18 丁達爾光 + T05 背光 + T47 硬光 + T37 弱光 + S05 煙霧體積光`，接 `haze with hard defined light shafts, dust motes in the beam, subject turned away, foreground occlusion`
- B → `T03 側光 + T47 硬光 + T42 暗色調 + T46 高對比 + S06 單光源夜戲`，接 `single practical, half the face falling three stops under`
- **分岔線**：氛圍感內部真正的變數是**亮部面積**，不是色調。問色調（暖／冷）等於白問。
- **兩支共用的硬條件**：光質都是 T47 硬光。A 支若用柔光，煙霧裡不會出現光束；B 支若用柔光，臉不會被切成一半。

---

**實例 2｜高級感【問一句】**

> 使用者：這張要有高級感。
> Agent：你要的是「拿掉東西」還是「加上重量」？**A** 畫面很空、只有兩三個接近的顏色、材質全是啞面；**B** 大面積深黑底、一道暖光掃過金屬邊緣、很重很沉。

- A（不答走這支）→ `T09 柔光 + T45 低飽和 + T43 低對比度 + T35 居中構圖 + S03 北歐冷冽`（〈2-2〉的減法路線；注意 S03 鎖 f/8 深景深）
- B → `T47 硬光 + T42 暗色調 + T46 高對比 + T06 暖光源 + T39 低角度視角`（黑金風那一列）
- **分岔線**：中文的「高級」同時涵蓋**極簡的高級**與**厚重的貴氣**，這兩者的參數全部相反。不問就做，有一半機率整張重來。

---

**實例 3｜日系【問一句】**

> 使用者：想要日系那種感覺。
> Agent：日系有兩種，你要哪一種？**A** 白天窗邊、很亮、幾乎沒有影子、顏色很淡；**B** 顆粒很明顯、顏色偏綠、亮的地方會暈開，像底片拍的。

- A（不答走這支）→ `T08 窗光 + T09 柔光 + T44 亮調 + T43 低對比度 + T45 低飽和 + S23 生活寫實`
- B → A 的全部，把 S23 換成 `S18 十六毫米顆粒`（一列只能有一個風格包），由 S18 自帶顆粒、halation 與偏綠陰影，光與影調維持 A 支不動（依〈1-5〉規則，膠片感只貢獻質感層）
- **分岔線**：日系的分岔在**載體**（數位 vs 底片），不在光——兩支的打光完全一樣。

---

**實例 4｜港風【必問，無預設】**

> 使用者：幫我拍出港風。
> Agent：是 **A** 下雨的夜街、霓虹反射在濕地上、人很小；還是 **B** 人像特寫、硬光、紅唇濃眉、暗背景？

- A → `T41 雙性照明 + T16 高飽和 + T42 暗色調 + T25 淺景深 + S13 港片霓虹`，且**必須**補上招牌失焦指令（見〈3-2〉）
- B → `T41 雙性照明 + T03 側光 + T47 硬光 + T16 高飽和 + T32 特寫`，**不掛 S13**（S13 整條定義都是夜街自發光，套在棚拍上會把背景換成街景）
- **分岔線**：港風在中文語境裡是**兩個不同年代、不同題材的視覺原型**共用一個詞（夜街／人像），沒有中間值。這一題沒有 A 支預設，使用者不答就只回問題。

---

**實例 5｜原相機直出【問一句】**

> 使用者：不要修圖感，要像原相機直出。
> Agent：白天還是晚上？**A** 白天窗邊或戶外，全部都對焦、暗處有點灰；**B** 晚上、手機閃燈直打，近的地方很亮、背景全黑。

- A（不答走這支）→ `T27 正面光 + T22 深景深 + T43 低對比度`，接 `roughly 26mm equivalent, HDR-lifted shadows sitting grey, over-sharpened contours with thin halos, auto white balance slightly off neutral`
- B → A 的全部，把影調換成 `T46 高對比`，並在光質槽加 `T48 閃光燈`，接 `direct on-camera flash, hot falloff into black a metre behind, harsh specular on the skin`
- **分岔線**：手機直出的成像特徵在日夜之間差異極大（HDR 提亮 → 全域低對比 vs 直閃 → 極高對比），且兩支都**必須排除淺景深**——這是本標籤唯一的互斥硬規則。兩支都**不掛 S14 數位早期**，那是 MiniDV 不是手機。
