# 影視風格篇｜24 項技術配方

> 原表註記：「以下為攝影技法歸納，括號內為風格參照，非指涉特定作品。」

每一項都是**九軸的預設組合包**：選了風格包，等於一次選定光、鏡頭、色彩、質感、構圖多個軸，
之後只需覆寫想調整的個別軸。

## 使用紀律（重要）

1. **提示詞中不可寫導演姓名或電影片名**，一律展開成具體技術描述。
   理由：生成模型對「具體技術描述」的反應遠比對「導演名」精確而穩定；
   而且原表本身就是技法歸納的立場。
2. **技術與載體名詞可以保留**：`Technicolor`、`Kodachrome`、`VHS`、`16mm`、`Super 8`、`DV`、
   `anamorphic` 這些是真實存在的成像介質與器材，模型有明確對應。
3. **一次只用一個風格包**。兩個風格包疊加＝十幾條互相矛盾的指令。
4. 每項的「可組合」欄位列的是**圖一 48 項中可再疊加強化的項目**，選 1–2 個即可，不要全上。

---

## 一、風格 01–08

### 01 德國表現主義｜Expressionist Hard-Shadow Chiaroscuro

> 風格參照：Fritz Lang（僅標示視覺傳統，非指涉特定作品）

- **技法核心**：單一硬光 + 遮光片投出的幾何斜影 + 原生黑白極高反差，讓「陰影」本身成為畫面的主角，人物退居為剪影。
- **光**：只有一盞硬光（裸燈泡或菲涅爾聚光，不加擴散）；水平角 60°–90°（正側光，光必須斜掠過牆面才有投影可看），垂直角只比頭頂高 10°–30° —— 光越低影子拉得越長，巨大斜影來自低光位，不是高頂光。光源與主體之間放 cookie／gobo（百葉窗、樓梯欄杆、鏤空板）切出斜影；人物剛好站在投影的暗條紋裡、或站得夠遠只吃到微量溢光，因此自身壓成剪影，亮的是牆。完全不補光，明暗比 16:1（4 級）以上，暗部直接黑位截止（black clipping）。黑白之下色溫不影響畫面，真正要管的是被攝物本身的明度與反差（正色片 orthochromatic 對紅不敏感，紅色物件會壓成近黑）。
- **鏡頭**：24–35mm 廣角，機位貼近主體與前景結構以放大透視變形；f/5.6–f/8 深景深讓影子與人同樣銳利；機位低於腰位仰拍或高處俯視，可加 5°–15° 傾斜（Dutch angle）；固定機位，或極慢的推軌。
- **色彩與質感**：原生黑白（不是去飽和的彩色），反差曲線中段極陡、亮暗兩端反而截平 —— 中間調被推向兩極，畫面只剩亮部與暗部；中等銀鹽顆粒，亮部允許輕微 halation 暈開；牆面粗糙質地在硬光斜掠下被強化。
- **構圖**：1.33:1（默片時期畫幅）等較窄畫幅；人物剪影小，置於畫面深處、下方或樓梯頂端；斜影佔畫面面積 50% 以上；封閉構圖，用門框、扶手、拱門把人夾死在幾何結構裡。
- **提示詞**：`True monochrome frame, one hard undiffused key from a low side angle just above head height, thrown through a slatted gobo so long diagonal shadow bars stretch across the wall behind; the figure in hat and long coat standing inside one of the dark bars, reduced to a small silhouette against the lit wall, 28mm, f/8 deep focus, slight Dutch tilt, crushed inky blacks, no fill light, 1.33:1 academy frame.`
- **可組合**：`47 硬光`、`46 高對比`、`42 暗色調`、`34 封閉構圖`、`39 低角度視角`
- **衝突**：`09 柔光`、`43 低對比度`、`44 亮調`、`27 正面光`、`16 高飽和`
- **常見錯誤**：把黑白當成「去飽和」處理而留下一堆灰中間調 —— 這個風格要求暗部真的死黑、影子邊緣硬到可以量角度；另一個是把燈架成高頂光，影子一縮短就沒有那道爬滿牆的斜影了。

### 02 義式驚悚紅綠光｜Saturated Red-Green Cross-Light

> 風格參照：Dario Argento（僅標示視覺傳統，非指涉特定作品）

- **技法核心**：左右兩盞互補色硬光分邊夾擊（cross light），色彩取代寫實光源動機，膚色的固有色被色光完全吃掉。
- **光**：雙光源，左右各一，水平角 ±90°–120°（側光到側逆光之間），皆為硬光不加擴散；一側貼原色紅（Lee 106 Primary Red），另一側貼原色綠（Lee 139 Primary Green）。兩束光用遮光扇（barn doors）或旗板切開，在人臉中線交會成一條硬邊界；紅光與綠光是加法混色，重疊處會變黃、不會變中性白，所以重疊帶要壓到最窄，或乾脆讓兩束完全不重疊。完全不加白光補光，環境光壓到近乎全黑，讓色片吃滿。此時色溫概念失效（色片透射不是黑體輻射），改用主波長思考（紅 ≈630nm、綠 ≈525nm）。
- **鏡頭**：40–58mm 標準焦段，避免廣角變形帶來的喜劇感；f/2–f/2.8；機位眼平或略低；固定機位，或極慢的橫向平移；主體貼牆，人與牆落在同一焦平面上一起清楚，走廊縱深自然散開。
- **色彩與質感**：飽和度推到單一通道接近過曝（channel clipping）的邊緣；紅光區只有紅通道有訊號、綠光區只有綠通道有訊號，兩區之間不做漸層；膚色的色相被色光取代，只剩明度層次；暗部不是純黑，而是深紅與深綠；細顆粒加輕微鏡頭光暈，色塊邊界保持硬邊。
- **構圖**：1.85:1 或 4:5；人物側身貼牆，身體壓在兩色交界線上，佔畫面寬度約 1/3；大面積平塗色牆當負空間；常用走廊、門框做封閉夾擊。
- **提示詞**：`Two hard undiffused lamps cross-lighting from ninety degrees left and right, one gelled primary red, one gelled primary green, barn-doored so the beams meet in a hard vertical line down the centre of the face with no soft gradient and no yellow blend; a woman pressed side-on against a corridor wall, her skin hue entirely replaced by the gel colours, deeply saturated single-hue fields, 50mm at f/2, no white fill, shadows falling into dark red and dark green.`
- **可組合**：`41 雙性照明`、`16 高飽和`、`47 硬光`、`03 側光`、`34 封閉構圖`
- **衝突**：`09 柔光`、`45 低飽和`、`27 正面光`、`43 低對比度`
- **常見錯誤**：只在畫面上薄薄鋪一層紅綠氛圍 —— 這個風格要的是色片吃滿、兩色之間有明確硬邊界；也不要讓紅綠大面積重疊，加法混色只會給你一片髒黃。

### 03 北歐冷冽｜Nordic Deadpan Flat Daylight

> 風格參照：Roy Andersson（僅標示視覺傳統，非指涉特定作品）

- **技法核心**：單一大面積冷調柔光 + 廣角深景深 + 完全靜止的正面全景，讓人與空間一樣蒼白、一樣無戲劇性。
- **光**：唯一光源是大面積柔光（整面窗或整片天花柔光罩），方向近乎正面偏上，水平角 0°–20°，接近無影；主暗比 1.5:1，且這個比值是光源夠大自然包覆出來的，不是靠補光燈；陰影邊緣過渡極寬。光源本身 5600–6500K，但白平衡刻意設得比光源低（≈5000K），畫面才會整體偏冷偏綠 —— 若把白平衡校準到光源，只會得到一張中性的白圖。室內燈具即使亮著也不製造暖點；不打人物補光，也刻意不打背景分離光，讓人融進牆面。
- **鏡頭**：18–28mm 廣角，f/8–f/11 深景深，從前景家具到窗外天際線全部清晰；機位固定在略低於眼平（120–140cm），水平垂直都用水平儀校準；全程不搖不推，單鏡到底。
- **色彩與質感**：低飽和（-25 至 -40），色相集中在灰綠、米白、灰藍；對比曲線平坦，黑位抬高成深灰、白位壓在 90% 不到頂；畫面乾淨幾乎無顆粒，帶一點刻意未校正的偏綠白平衡；人物膚色刻意慘白（實拍是白粉底），與牆面落在同一個明度層。
- **構圖**：1.85:1 橫幅或 4:5；人物全身站在畫面中軸上，佔畫面高度不到 1/2；牆、地、天花三個平面都交代清楚，留大量空曠負空間；牆上小畫框、暖氣片等細節左右對稱擺放。
- **提示詞**：`Wide static frame of a pale institutional room, one enormous soft source filling an entire wall as the only light, near shadowless, cool 6000K daylight with a deliberately uncorrected green-grey white balance; no fill and no separation light; a man in a grey suit with chalk-pale skin stands motionless dead centre, full body, small in frame, 24mm at f/8 deep focus, flat low-contrast grading, desaturated grey-green walls, 1.85:1.`
- **可組合**：`09 柔光`、`43 低對比度`、`45 低飽和`、`22 深景深`、`35 居中構圖`
- **衝突**：`47 硬光`、`46 高對比`、`03 側光`、`25 淺景深`、`01 暖色調`
- **常見錯誤**：加側光或分離光想把人「從背景拉出來」—— 這個風格的力量正來自人與牆同亮度、同平面的乏味感。

### 04 魔幻時刻｜Magic Hour Backlight

> 風格參照：Terrence Malick（僅標示視覺傳統，非指涉特定作品）

- **技法核心**：太陽貼著地平線的那 20–30 分鐘，太陽當唯一背光、天空當唯一冷色補光，冷暖分離全部由自然光完成。
- **光**：唯一光源是太陽，仰角 0°–6°、位在主體正後或後側 150°–170°；此時陽光穿過最厚的大氣層被散射，變暗、變暖、由硬轉半柔，陰影邊緣柔但仍有明確方向；直射光色溫 2000–3200K 且逐分鐘改變。暗面只靠天空補光 —— 天光約 10000K，所以暗面自然偏藍，需要時再加白色反光板提一點細節；不使用任何人工燈具。
- **鏡頭**：35–85mm；f/1.8–f/2.8 淺景深，把背景草地與逆光點化成光斑；要 flare 就讓太陽直接擦過鏡頭邊緣或被主體邊緣半遮（flare 來自光源進鏡頭，與景深無關）；機位略低於眼平仰拍，把地平線壓到畫面下方、拉高天空佔比；手持跟走或緩慢環繞，允許輕微晃動。
- **色彩與質感**：暖色高光（橘金）配冷藍陰影的天然 split-tone；飽和度中高但不濃豔；高光柔和滾降不硬切；逆光漫射造成整體對比下降與輕微 haze；髮絲、草穗、空氣中的塵埃被邊緣光描出輪廓。
- **構圖**：2.39:1 或 16:9；人物取近景至中景、偏畫面一側，臉呈四分之三側面朝鏡頭而背對太陽；地平線壓在下三分之一，太陽在頭側形成光暈；大量帶空氣感的負空間。
- **提示詞**：`Low sun sitting right on the horizon directly behind a young woman in a summer field, used as the only key so it rims her flying hair and the grass edges; open sky as the sole fill, leaving her shadow side clearly blue against warm 2800K highlights; 85mm at f/2, handheld, shallow focus, gentle flare where the sun grazes the lens, lowered contrast and soft rolled-off highlights, horizon on the lower third, 2.39:1.`
- **可組合**：`04 側逆光`、`10 髮絲光`、`01 暖色調`、`25 淺景深`、`30 四分之三側面`
- **衝突**：`27 正面光`、`07 頂光`、`36 冷光源`、`22 深景深`
- **常見錯誤**：把它理解成「加一層橘色濾鏡」—— 沒有真正的低角度逆光與冷藍陰影，只會得到一張髒黃的平光照。另一個是把 golden hour 與 magic hour 混為一談：這個配方用的是太陽還在地平線上的最後一段；太陽一旦落到地平線以下（嚴格定義的 magic hour／twilight），就沒有方向性背光可用，只剩無影的冷藍天光，那要換成另一套打法。

### 05 煙霧體積光｜Volumetric Light Shafts in Haze

> 風格參照：Ridley Scott（僅標示視覺傳統，非指涉特定作品）

- **技法核心**：極強的遠距硬光從逆側方向斜射進帶懸浮粒子的空氣，讓光束本身變成畫面裡看得見的立體物件。
- **光**：單一超強硬光從遠距離打入（模擬太陽或大型窗），方向必須偏逆光 —— 水平角 110°–150°、垂直角 40°–60°，光朝著鏡頭方向斜射。煙霧顆粒的散射以前向散射為主，光源越接近逆光，光柱越亮越立體；若改從 30°–45° 的順側光打，煙只會變成一片沒有形狀的灰紗。光先被窗框、百葉或柱列切成數道分離光柱；用造霧機（hazer）打薄到中等的油霧讓光柱顯形，濃度寧可不足也不要過量。主體不站進光柱裡，只吃到旁邊的溢光，臉部曝光比光柱打亮的地面低約 3 級；背景不另外打光，靠煙霧散射自然形成灰階漸層。全場單一色溫，5600K 冷白或 3200K 暖白擇一，不混色。
- **鏡頭**：35–50mm；f/2.8–f/4；機位略低於胸位以強調光柱高度；緩慢推軌或升降讓光束隨視差移動；中等景深，縱深層次靠空氣透視提供 —— 愈遠的物件之間累積的霧愈厚，對比愈低、黑位被抬得愈高。
- **色彩與質感**：接近單色，冷灰藍或琥珀二選一；飽和度低（約 -30），只留光束與陰影的明度戲；高對比但暗部因散射被抬起，形成「發亮的黑」；中等顆粒，光束邊緣有輕微擴散暈。
- **構圖**：2.39:1 寬幅；人物半剪影側身，站在兩道光束之間的暗區或剛好切進一道光；高聳的縱向建築線條（長窗、列柱）製造壓迫感；人物佔畫面高度不超過 1/3。
- **提示詞**：`Thin drifting haze in a tall dark hall, one very hard distant source raking in from behind and above through tall window bars, angled back toward the lens so it carves separate hard-edged light shafts with clear dark gaps between them; a cloaked figure stands in the gap between two shafts, lit only by spill, three stops under; 40mm at f/2.8, near-monochrome cool grey palette, lifted milky blacks, slow dolly, 2.39:1.`
- **可組合**：`18 丁達爾光`、`47 硬光`、`37 弱光`、`42 暗色調`、`21 遠景`
- **衝突**：`09 柔光`、`27 正面光`、`16 高飽和`、`44 亮調`
- **常見錯誤**：煙給太滿變成均勻的霧 —— 光柱必須有清楚的邊界與間隔，煙只是介質，不是主體；另一個是把燈架在鏡頭同側，順光打進煙裡只會得到一層灰紗，光柱完全立不起來。

### 06 單光源夜戲｜Single-Practical Digital Night

> 風格參照：Michael Mann（僅標示視覺傳統，非指涉特定作品）

- **技法核心**：只用場景裡真實存在、且可見於畫面內的一盞燈當主光，其餘暗部交給高感光度數位機身把城市餘光撿回來。
- **光**：唯一主光是入鏡的路燈／霓虹／車燈，位於主體側後方 120°–150°、高度高於頭頂，形成單邊亮臉與整片落下的暗面；完全不補光，暗面只靠遠處城市燈火的環境光，比主光低 3–4 級；色溫刻意不校正，讓各光源的偏差原樣留在畫面上 —— 鈉氣路燈約 2000K、暖白 LED 約 2700–3000K 的橘，對上遠景城市的 4000–5000K 青白。
- **鏡頭**：50–85mm；f/1.4–f/2，讓遠景燈火散成大顆圓形散景（要圓就得全開，收光圈會露出多邊形葉片）；機位眼平或略低仰拍；固定或極輕微手持；淺景深，主體與背景之間留 30 公尺以上實距。
- **色彩與質感**：陰影推向 teal、高光留在橘黃，形成冷暖分離；中低飽和；暗部保留 ISO 3200–6400 的細數位噪點（不是底片顆粒）；對比高但黑位不壓死，遠處燈點的細節必須留住。
- **構圖**：2.39:1；人物中景，置於左右三分之一線上，側面或四分之三側面望向畫外；背景是大面積失焦的城市光點；上方留天空負空間強調孤立。
- **提示詞**：`Night rooftop, the only key is a practical street lamp visible in frame behind the man's shoulder, undiffused sodium orange around 2000K, placed high and behind so his shadow side falls three stops down with no fill; distant city lights thrown into large round bokeh, 85mm at f/1.4, subject standing thirty metres clear of the background, teal shadows against amber highlights, visible high-ISO digital noise rather than film grain, blacks lifted just enough to keep the far light points, 2.39:1.`
- **可組合**：`11 自發光`、`04 側逆光`、`37 弱光`、`25 淺景深`、`38 冷色調`
- **衝突**：`27 正面光`、`22 深景深`、`44 亮調`、`48 閃光燈`
- **常見錯誤**：補一盞沒有畫面內動機的燈把暗面救回來 —— 這個風格的張力來自臉的另一半真的沉進黑裡。

### 07 單點透視對稱｜One-Point Perspective Symmetry

> 風格參照：Kubrick（僅標示視覺傳統，非指涉特定作品）

- **技法核心**：鏡頭光軸與空間中軸完全重合，畫面內所有直線收斂到正中央的單一消失點。
- **光**：光源配置本身也對稱 —— 走廊兩側等距的吸頂燈或壁燈作為入鏡光源，形成隨透視規律遞減的亮點序列；燈具是小面積硬光源、只被燈罩略微擴散，所以人物走到燈下時頭頂亮、眼窩暗（換成大面積柔光，這個垂直落影就不見了）；垂直角 80°–90°；不使用側光以免破壞左右平衡；全場單一色溫（3200K 暖白或 4300K 冷白擇一），不混色。
- **鏡頭**：18–28mm（超廣角到廣角，誇張的透視收斂是重點），且必須是直線畸變修正良好的鏡頭 —— 一有桶狀變形，本該筆直的收斂線就會彎掉，單點透視立刻失效；相機零傾斜、零旋轉、零橫移，水平垂直都以水平儀校準；f/5.6–f/11 深景深，從最近的門框到最遠的消失點全清晰；機位固定在較低的胸位（100–120cm）；運動只允許沿光軸的直線推進（dolly-in），絕不橫搖或橫移。
- **色彩與質感**：中高對比，色盤收斂到一到兩個主色（地毯的橘紅、牆面的米白），飽和度中等；畫面乾淨、四角無明顯暗角（廣角大光圈的邊角失光要修掉）；地毯花紋與壁紙紋理保持銳利 —— 它們就是透視的刻度尺。
- **構圖**：1.85:1 或 1.33:1；嚴格左右鏡像，中軸兩側元素的數量與間距一致；人物極小，站在正中央的消失點上，佔畫面高度不到 1/5；地板與天花板各佔畫面上下約 1/4，形成強烈的縱深隧道。
- **提示詞**：`Long hotel corridor shot dead on the centre axis, camera perfectly level with zero tilt and no roll, every straight line converging to a single vanishing point in the exact middle of the frame, no barrel distortion; matching ceiling lamps recede in symmetrical pairs as small hard pools of warm tungsten light, patterned carpet as a depth scale, one tiny figure standing far away at the vanishing point, 21mm at f/8 deep focus, restricted orange-and-cream palette, 1.85:1.`
- **可組合**：`35 居中構圖`、`22 深景深`、`07 頂光`、`34 封閉構圖`、`21 遠景`
- **衝突**：`26 斜側視角`、`33 鳥瞰`、`25 淺景深`、`03 側光`
- **常見錯誤**：機位偏了幾公分或鏡頭稍微上仰 —— 消失點一離開畫面正中心，效果立刻垮成一張普通的走廊快照。

### 08 平面正面構圖｜Planimetric Frontal Tableau

> 風格參照：Wes Anderson（僅標示視覺傳統，非指涉特定作品）

- **技法核心**：把三維空間壓成一個與感光面完全平行的平面，人與道具像立面圖一樣正面陳列。
- **光**：極柔、極平的正面光（大型柔光箱或天花反射），水平角 0°、垂直角僅高於鏡頭 10°–15°，主暗比 2:1 以內，幾乎不留可見陰影；牆面另打一層均勻背景光，讓整面牆讀成一塊乾淨飽滿的平色；場景內的檯燈作為左右對稱、亮度相同的裝飾性自發光；全場色溫統一 3200–4000K。
- **鏡頭**：等效 27–40mm；平面感來自光軸與背景牆呈 90° 垂直加上正面平光，不是靠焦段換來的 —— 焦段只要不出現明顯的廣角變形（直線必須筆直）即可；f/5.6–f/8 讓前後景一樣清楚；機位必須落在主體臉部高度的正中央；運動只用純水平橫移（tracking）、垂直升降（pedestal），或 90° 的快速甩鏡（whip pan），絕不斜向或弧形移動。
- **色彩與質感**：高度受控的有限色盤（3–4 個主色，如粉紅、芥末黃、木紋褐）；明度高、飽和度中等偏低的粉彩調（pastel 本身就是「高明度＋不濃」，不要同時要求高飽和）；對比中等、黑位微微抬高；質感乾淨平滑，帶輕微底片顆粒與幾乎不可見的暗角。
- **構圖**：1.85:1；主體置中、正面直視鏡頭，左右對稱、上下留白刻意等量；左右陳設鏡像對稱（兩盞燈、兩個櫃子）；人物坐姿佔畫面高度約 1/2；背景牆填滿整個畫面，幾乎沒有縱深，負空間由色塊而非空氣構成。
- **提示詞**：`Subject seated centred and facing the lens straight on, camera axis exactly perpendicular to a flush background wall so the whole scene flattens into a single plane with no depth cues; symmetrical matching table lamps left and right, broad soft frontal light with almost no visible shadow, evenly washed wall reading as one flat colour field, pastel pink and mustard palette at moderate saturation, 35mm at f/5.6, eye level, 1.85:1.`
- **可組合**：`27 正面光`、`35 居中構圖`、`09 柔光`、`22 深景深`、`20 中景`
- **衝突**：`26 斜側視角`、`25 淺景深`、`03 側光`、`47 硬光`
- **常見錯誤**：加斜側視角或淺景深想「增加層次」—— 這個風格的效果完全來自平面性，一旦出現縱深就變成普通的室內照。

---

## 二、風格 09–16

### 09 固定長鏡頭｜Static Long Take

> 風格參照：（侯孝賢）

- **技法核心**：機位完全鎖死的三腳架 + 標準焦段 + 深景深 + 純現場光，把「剪接」與「運鏡」兩個變數同時歸零，讓敘事完全交給人物在框內的走位與時間流逝。
- **光**：只用現場既有光源，通常是 1 個主導光（窗光，或天花板的家用鎢絲燈泡）加上牆面自然反彈當唯一補光；窗外日光約 5000–5600K、家用鎢絲燈泡約 2700–3000K，兩種色溫同場並存且完全不做白平衡校正，畫面裡冷區暖區各據一方；不打電影燈、不放反光板、不加髮絲光；曝光以人物受光面為基準，房間角落自然掉到接近純黑，主光與牆面反彈的光比約 4:1 至 6:1。
- **鏡頭**：35–50mm；Super35 的畫幅對角約 28.6mm，標準視角落在 32–35mm，50mm 已經是輕度長焦、帶一點壓縮，兩端各有用途但不是同一件事。f/4–f/5.6 求前後全清；機位鎖在三腳架上完全不動，無搖攝、無俯仰、無變焦；高度取坐姿眼平 110–120cm（比站立視線低），景深涵蓋前景桌面到後景門廊。
- **色彩與質感**：低飽和（比正常降 15–20%）；鎢絲燈的偏黃與窗光的偏藍同框並存、色偏一律不修（只有場景裡真的有日光燈時才會出現偏綠）；對比中等，暗部順其自然沉下去，既不抬黑位也不刻意壓死；35mm 細顆粒；膚色維持真實偏黃的樣子，不美膚、不把人從環境色裡單獨提亮。
- **構圖**：1.85:1 或 1.66:1；大量使用門框、窗框、樑柱形成畫中畫的封閉構圖；人物只佔畫面高度的 1/4–1/3 且偏離中心；前景常有物件部分遮擋；留白給空蕩的房間本身。
- **提示詞**：`Locked-off tripod frame, 40mm lens at f/5.6, deep focus from the foreground table all the way to the far doorway, camera at seated eye level, 115cm off the floor. Interior lit only by one household tungsten bulb and daylight spilling in through a window, the two colour temperatures left mixed and uncorrected, warm pool against cool pool, no film lighting and no bounce boards, corners allowed to fall away to near black. Muted desaturated palette, skin left its real sallow yellow, fine 35mm grain, 1.85:1. Figure small in the frame at a quarter of the picture height, off centre, seen past a door jamb, wide empty negative space, one unbroken static take.`
- **可組合**：`22 深景深`、`08 窗光`、`34 封閉構圖`、`45 低飽和`、`21 遠景`
- **常見錯誤**：把「固定」誤解成「空鏡」——鏡頭不動不等於畫面不動，必須讓人物在框內進出走位、留下可被時間填滿的空間，否則只是一張放大的靜照。

### 10 手持跟拍｜Handheld Follow-Cam

> 風格參照：（Dardenne brothers）

- **技法核心**：肩扛攝影機貼在人物背後 1 公尺內持續行走，用「操作者的身體」取代雲台，配上純現場光與反應式跟焦，讓觀眾被迫與主角同速移動。
- **光**：100% available light，不帶燈具；同一場常同時存在 5600K 日光與 4000K 走廊日光燈而不做白平衡統一；曝光壓在臉上，背景窗戶直接過曝溢出；完全無補光、無反光板，人物轉身背向光源時臉可以整個掉進暗部（比臉部基準低 2–3 級，1 級以內只是「稍暗」，撐不起這個風格）。
- **鏡頭**：25–35mm 廣角略帶變形，f/2.8–f/4；機位在主體肩後、高度約 150–165cm（肩扛的自然高度），距離 0.8–1.5m；持續的行走低頻起伏 + 重新構圖的細微修正 + 偶爾追不上的甩鏡；跟焦是人手反應式的，合焦永遠慢半拍——先軟一下再追實，而不是全程死鎖；1/48 快門（24fps、180° 快門角）保留自然拖影。
- **色彩與質感**：中性偏冷的紀錄片調（混合色溫留在光源裡，不在調色上做風格化色彩分離）；不加銳化；暗部保留原生噪點；動態中的輕微殘影而非清晰凍結；膚色略偏灰白不做修飾。
- **構圖**：1.66:1 或 1.85:1；主體後腦或側頸佔據左右三分之一，頭頂常被上緣切掉；地平線隨步伐傾斜數度；主體前方幾乎不留視線空間，鏡頭永遠慢半拍、人物幾乎要走出畫面。
- **提示詞**：`Shoulder-mounted handheld camera trailing one metre behind a walking figure, 28mm at f/2.8, shoulder height, slow low-frequency walking sway rather than shake, the frame lagging and correcting a beat late, focus landing soft for a moment before it settles. Available light only, mixed daylight and green corridor fluorescent left uncorrected, exposed for the face, the window behind blown out, no bounce or fill, the face dropping two to three stops under as she turns away. Desaturated neutral documentary grade, no sharpening, native shadow noise, mild motion blur at a 1/48 shutter. Back of the head filling a third of the frame and cropped hard against the top edge, horizon tilted a few degrees, almost no space ahead of her, 1.66:1.`
- **可組合**：`28 背面視角`、`24 動態模糊`、`20 中景`、`45 低飽和`、`08 窗光`
- **常見錯誤**：把手持做成劇烈抖動——真實跟拍是「行走的低頻起伏 + 構圖的細微追補」，高頻亂晃只會被讀成業餘素材而非紀實感。

### 11 三色印片｜Three-Strip Technicolor

> 風格參照：（Technicolor）

- **技法核心**：分光稜鏡三片式感光 + 染料轉印（dye-transfer）出片；三條片同時曝光使有效感光度只有 ASA 5–10，必須用巨量弧光燈照明，於是「超高照度 + 高補光 + 純淨原色 + 幾乎沒有純黑」成為這個載體無可迴避的視覺後果。
- **光**：棚內多燈；主光是碳弧燈（日光色溫，約 5500K，不是 3200K 鎢絲燈——選它正是為了那個照度）置於 30–45° 水平角、20–30° 仰角；即使把棚內堆到 800–1000 呎燭光（約 8,600–10,800 lux），工作光圈也只開得到 f/2.3–f/3.5；補光極強，光比壓到 2:1 甚至 1.5:1，臉上幾乎不存在純黑；每個主要人物必加一盞硬質髮絲光把頭髮從背景剝離；背景另有獨立的均勻鋪光。
- **鏡頭**：35–50mm（1.37:1 Academy 上的標準到輕長焦；75mm 在這個畫幅已是長焦，拍不了全身舞台化調度），f/2.3–f/3.5；三腳架固定或緩慢升降，機位眼平或略低於眼平以拉出人物高度；景深其實只是中等——前景到繪景背景一起清楚，靠的是廣角焦段、人物退遠、以及背景本身就是一張平面繪景，不是靠縮光圈。
- **色彩與質感**：攝影端把畫面分成紅、綠、藍三條分離片，印片端用青、洋紅、黃三種染料轉印；成像上的辨識點是紅、綠、藍三色極度飽和且不互相污染；暗部偏青、亮部偏暖奶油色；高飽和但對比平順、不壓黑；顆粒極細（染料影像沒有銀鹽顆粒結構）；高反差邊緣有輕微的套準偏移彩邊（registration fringing）。
- **構圖**：1.37:1 Academy 畫幅；劇場式正面舞台化調度，人物取全身或七分身並保留充足頭頂空間；前景與背景以互補色塊分區；服裝本身就是主要色彩重點。
- **提示詞**：`Three-strip Technicolor dye-transfer rendering: vividly saturated reds, greens and blues that never contaminate one another, cyan-tinted shadows, creamy warm highlights, faint colour fringing from imperfect registration on high-contrast edges. Lit like a 1930s sound stage with daylight-balanced carbon arcs, a hard key 40 degrees off axis and 25 degrees up, a 2:1 key-to-fill ratio so nothing on the face reaches black, a hard hair light on every figure, the background separately and evenly lit. 40mm at f/2.8, locked tripod, Academy 1.37:1, centred full-figure theatrical staging, costume carrying the colour against complementary background blocks.`
- **可組合**：`16 高飽和`、`40 強光`、`10 髮絲光`、`44 亮調`、`35 居中構圖`
- **常見錯誤**：只把飽和度拉滿卻保留現代的深黑陰影——三色印片的辨識點是「高飽和 + 高照度 + 幾乎沒有純黑」，少了大量補光就只是一層廉價濾鏡。

### 12 柯達克羅姆｜Kodachrome Reversal

> 風格參照：（1970s Kodachrome）

- **技法核心**：ISO 25 或 ISO 64 的正片（反轉片）在直射陽光下按亮部曝光；場景寬容度只有約 5 級，於是「濃黑暗部 + 紅橙偏強的高飽和 + 極細顆粒」是化學結構直接決定的結果。
- **光**：單一光源＝太陽本身，5000–5500K；不補光、不用反光板；順光或 45° 側前光；暗部只靠開闊天空的藍色散射填充，因而偏冷偏濃；曝光鎖在亮部（sunny 16 紀律），陰影直接堵死。
- **鏡頭**：135 片幅上的 35mm 或 50mm 定焦；ISO 64 在直射陽光下的 sunny 16 等效組合就是 f/11、1/125 秒（薄雲或側逆光才開到 f/8）；手持、眼平高度；中等偏深的景深，人物與環境同時交代清楚。
- **色彩與質感**：紅與橙最先飽和且最強勢、藍偏深、綠被壓成偏橄欖的黃綠；亮部完全沒有滾降空間，一到就切斷；顆粒細到幾乎看不見；深暗部又濃又偏藍青；老鏡頭邊角有輕微暗角；掃描後留有少量灰塵與細微刮痕。
- **構圖**：3:2 橫幅；隨手紀實式取景，主體置於中景距離、佔畫面高度約一半；環境資訊留得很足；地平線偏高或偏低，少見置中。
- **提示詞**：`Kodachrome 64 reversal stock in direct afternoon sun, 5400K, no fill and no reflector, shadows filled only by open blue sky so they read cool and block up dense. Exposed for the highlights at f/11 and 1/125, 50mm prime, handheld at eye level, 3:2 frame. Saturated dominant reds and oranges, restrained olive greens, deep blue-cyan blacks, highlights clipping abruptly with no roll-off at all, extremely fine grain that is almost invisible, faint corner vignetting, a little scan dust and one hairline scratch.`
- **可組合**：`27 正面光`、`46 高對比`、`01 暖色調`、`22 深景深`、`20 中景`
- **常見錯誤**：加上粗顆粒——Kodachrome 的辨識特徵正是「幾乎無顆粒 + 極濃的黑」，加了顆粒等於換成了另一種底片。

### 13 港片霓虹｜Neon Street Nocturne

> 風格參照：（王家衛）

- **技法核心**：不另架白光電影燈（要加也只用同色系的實用光源），讓招牌霓虹與店鋪燈泡本身當主光；再用長焦從街對面穿過前景雜物壓縮空間，配大光圈與慢快門把光源化成色塊。
- **光**：自發光為唯一光源——霓虹管、2700K 鎢絲店燈、4200K 偏綠日光燈同時存在；有色光直接污染膚色，不做任何校正，也不補白光。臉的處理**二擇一，不要混用**：(a) 兩種對立色（洋紅／青、紅／綠）各照半邊臉、兩側光比約 1:1，鼻梁中線留一道兩邊都照不到的暗帶；(b) 只有單側被招牌照到，另外半邊整個沉進有色暗部（低 3 級以上）。
- **鏡頭**：85–135mm 長焦壓縮，f/1.4–f/2 全開；機位胸部高度或更低，手持帶輕微漂移；極淺景深，前景隔著玻璃、鐵窗花、路人的身體拍攝；情緒段落用「低格率 + 每格 1/12–1/24 秒長曝」拍攝，再以重複印格（step printing）放慢，得到「拖影」與「頓挫」並存的動態——這與單純的慢快門不是同一件事，慢快門只給平順的模糊。
- **色彩與質感**：洋紅、青、翡翠綠、琥珀黃四色極度飽和；黑位壓死但被有色光污染而不純；每個光源周圍有明顯光暈（halation）與溢光；暗部可見 35mm 顆粒；濕地面把光源複製成第二層。
- **構圖**：1.85:1；主體被擠到畫面邊緣或被前景遮蔽超過三分之一；透過門洞、鏡子、招牌縫隙取景；頭頂空間切掉；輕微傾斜數度；深處負空間填滿失焦的霓虹散景。
- **提示詞**：`Night street lit only by neon tubes and shop practicals, no white film light anywhere: magenta raking one side of the face, jade green raking the other, an even 1:1 between the two coloured sources, a dark band down the centre line where neither reaches. 100mm at f/1.4, chest height, shot from across the road through a foreground grille. Coloured light contaminating the skin uncorrected, crushed blacks tinted rather than neutral, heavy halation bloom around every source, wet asphalt doubling the signage, dense vertical neon bokeh behind, smeared stuttering motion trails on anything that moves, 35mm grain, 1.85:1.`
- **可組合**：`41 雙性照明`、`11 自發光`、`25 淺景深`、`16 高飽和`、`24 動態模糊`
- **常見錯誤**：把霓虹當成背景裝飾、另外打一盞柔光在臉上——霓虹必須是唯一主光，臉上的顏色要來自招牌本身；一補白光就退化成商業廣告的打光。

### 14 數位早期｜Early Digital Video

> 風格參照：（2000s DV）

- **技法核心**：1/4 吋 CCD、隔行掃描的標清錄影 + 全自動曝光與白平衡；小感光元件造成全景深，視訊 gamma 造成亮部硬切，4:1:1 色度取樣造成彩色邊緣糊開。
- **光**：現場光或機頂燈；自動曝光持續呼吸（人一走近整個畫面就變暗）；自動白平衡在 3200K 室內與 5600K 室外之間漂移、常偏綠；亮部沒有膠片式的滾降，窗戶直接切成一片死白；暗部被電子增益抬起成灰並帶噪點；機頂燈在最近的人身上留下明顯熱點與硬邊影子。
- **鏡頭**：內建 4.5–45mm 10× 變焦；1/4 吋 CCD 的裁切係數約 10.8×，換算 135 等效約 48–480mm——**廣角端一點都不廣**，這個「退無可退還是拍不進去」正是 DV 的視覺胎記；標稱 f/1.8 但因感光元件小而景深極深、幾乎沒有焦外；手持胸口至眼平高度；數位變焦推拉時畫質階梯式劣化；沒有可用的散景。
- **色彩與質感**：720×480 隔行掃描，運動邊緣出現梳狀交錯（combing）；4:1:1 讓紅與藍的色度邊界水平糊開；機內銳化造成的白邊光暈，加上幀內 DCT 壓縮在細節區的塊狀瑕疵；暗部帶薄薄的青綠色偏；中間調對比偏低、黑位抬起，卻同時有硬切的亮部。
- **構圖**：4:3；偶爾是機內裁切、上下加黑邊的假 16:9（不是變形擠壓的真寬銀幕）；隨手置中構圖、缺乏設計；主體在中景距離；地平線晃動；角落有機內烙印的日期時間字幕。
- **提示詞**：`Standard-definition MiniDV capture, 4:3 interlaced 720x480, 4:1:1 chroma bleeding sideways off saturated reds, combing artifacts on anything that moves, in-camera oversharpening halos and DCT block noise in fine detail. Auto-exposure breathing, auto white balance drifting green, windows clipped to flat paper white with no roll-off, blacks lifted grey and noisy from electronic gain. Tiny quarter-inch CCD keeps everything from foreground to background in focus with no bokeh at all, on-camera light burning a hotspot into the nearest face, handheld at chest height, casual centered framing, a date and time stamp burned into the corner.`
- **可組合**：`02 過度曝光`、`22 深景深`、`43 低對比度`、`27 正面光`、`37 弱光`
- **常見錯誤**：用高畫質素材再套一層「復古濾鏡」——DV 的辨識點是感光元件與編碼造成的「全景深 + 亮部硬切 + 色度糊邊」，不是顏色偏移。

### 15 沙塵單色｜Dust-Field Monochrome

> 風格參照：（Denis Villeneuve）

- **技法核心**：讓空氣中的懸浮介質（沙、塵、霧、霾）成為真正的擴散器，把一顆巨大的背光或頂光散射成單一色場，整個場景收斂成近乎單色；再用極小的人影交代尺度。
- **光**：唯一光源是被介質包住的巨型漫射光——沙暴中的低角度太陽（透過厚塵後只剩約 2000–2500K 的琥珀色）或全陰天穹頂（約 6500K 平白）；不架補光，補光完全由粒子散射自然完成；沒有硬質輪廓光——背光被介質打散之後只會留下柔化的剪影邊緣，不會出現銳利的髮絲光；介質把光比壓到 2:1 以內，黑位被霧抬起發灰。
- **鏡頭**：21–40mm 變形寬銀幕鏡，f/4–f/5.6；機位極低（貼地）或極高（俯視地貌）；運動只有極慢的推軌或升降，慢到定睛看一秒幾乎察覺不到鏡頭在動；深景深，前後分離交給空氣透視而非景深。
- **色彩與質感**：近乎單色——整幅畫面只剩一個色相（琥珀橙，或石板藍灰），所有物體都在這個色相的明暗之間分佈，次要色相被完全抽掉；飽和度本身不高，但色相高度統一；濃厚的空氣霾使遠景幾乎消失；細顆粒；剪影邊緣柔化不銳利。
- **構圖**：2.39:1；人物只佔畫面高度的 3–8%；上方三分之二留給空無；巨大的單體幾何剪影；對稱或只有一條強烈的地平線。
- **提示詞**：`Dense airborne dust collapsing the whole scene into a single amber hue, a 2200K low sun burning through the haze as one enormous diffused backlight, no added fill — the particulate itself does the filling, contrast flattened to about 2:1, blacks lifted milky by the haze, silhouette edges softened with no hard rim anywhere. 28mm anamorphic at f/5.6, camera almost on the ground, glacially slow push-in. 2.39:1, a human silhouette three percent of frame height, vast empty sky above, the distance dissolving into haze, atmospheric perspective doing all the separation.`
- **可組合**：`21 遠景`、`05 背光`、`45 低飽和`、`39 低角度視角`、`43 低對比度`
- **常見錯誤**：只把色調調成橘色卻沒有空氣中的懸浮粒子——這個風格的物理基礎是「介質」，沒有霧塵散射與被抬起的黑位，就只是蓋了一張色片。

### 16 黑白默片｜Orthochromatic Silent Film

> 風格參照：（Murnau）

- **技法核心**：正色片（orthochromatic）的光譜響應錯位 + 單一硬質弧光 + 完全無補光燈 + 手搖 16–18fps 拍攝；四者疊加出高反差、深黑背景、被雕刻出來的臉。
- **光**：1 盞硬質碳弧燈置於 45–60° 仰角、無擴散，投出邊緣銳利、可辨形狀的影子；再加 1 盞硬邊輪廓光把人從黑背景剝出；沒有任何補光燈，暗面全靠地板牆面的微弱反彈，光比因此落在 8:1 以上；畫面可有大面積純黑；手搖速度不勻（加上弧光本身的不穩）造成約 ±1/3 級的曝光跳動。
- **鏡頭**：35–50mm，f/4–f/5.6；三腳架鎖定，眼平或略低機位，偶爾緩慢平移推軌；深景深；拍攝 16–18fps 而以 24fps 放映，動作略微加速（約 1.3 倍）且帶輕微跳格。
- **色彩與質感**：正色片響應——藍天渲染成白（雲層完全分不出來）、紅唇渲染成黑、膚色偏暗且質地明顯；S 曲線陡峭，純黑與過曝白同時存在；粗顆粒；片門抖動（gate weave）、垂直刮痕、局部霉斑；可選整場做印片染色（tinting，染的是拷貝不是原始底片），染成琥珀或藍的單色調。
- **構圖**：1.33:1 默片全片幅（silent aperture；1.37:1 Academy 是 1932 年有聲之後才定的規格，兩者不能混稱）；舞台化正面調度，人物取全身或七分身居中，背景以建築斜線與樓梯製造動勢；影子本身當作構圖量體使用；頭頂空間充足。
- **提示詞**：`Orthochromatic black-and-white rendering: blue sky goes white with no cloud separation, red lips go black, skin dark and textured. One hard undiffused carbon-arc key 55 degrees above, razor-edged cast shadows, no fill lamp at all so the ratio runs 8:1 or steeper into pure black backgrounds, plus a hard rim separating the shoulder. Staged frontal blocking against steep architectural diagonals and a staircase, the cast shadow itself used as a compositional mass. 1.33:1 silent-era full frame, locked 50mm at f/4, coarse grain, gate weave, vertical scratches and a faint exposure flicker.`
- **可組合**：`47 硬光`、`46 高對比`、`14 輪廓光`、`42 暗色調`、`34 封閉構圖`
- **常見錯誤**：直接把彩色影像去飽和——正色片的關鍵是「光譜響應錯位」（紅變黑、藍變白），單純去色會保留現代的膚色明度關係，一眼就假。

---

## 三、風格 17–24

### 17 VHS 錄影帶｜VHS Home Video

> 風格參照：1980s home video

- **技法核心**：家用攝影機的「機頂單燈正面直打」加上磁帶記錄的物理劣化（4:3、水平解析度僅約 240 線、色度以 color-under 方式降頻另存，頻寬約 0.4MHz 對亮度的 3MHz，只剩約六分之一），兩層疊加才成立。
- **光**：單一光源——機身頂部的鎢絲鹵素攝影燈（約 3200K）從鏡頭軸線正面直打，完全沒有補光；近端主體立刻過曝到剪裁，背景因平方反比在 2 公尺外掉進全黑。現場另有 2700K 白熾燈與帶綠尖峰的螢光燈混色，自動白平衡在暖橘與偏綠之間來回漂移（綠偏來自螢光燈的不連續光譜，白熾燈本身只會更橘），臉頰高光呈無血色的白。
- **鏡頭**：機身內建 6 倍變焦，1/2 吋成像面（裁切係數約 5.4，等效約 45–270mm——廣角端其實不夠廣，這是家用機的典型限制），f/1.4–2.0；1/2 吋攝像管或小型 CCD 使景深天然很深，2 公尺外幾乎全清晰；全尺寸機種肩扛托機，持機高度在胸口到肩之間左右晃動，自動對焦來回搜尋（focus hunting），常有一次目的不明的推鏡變焦。
- **色彩與質感**：紅色與洋紅嚴重色度滲流（chroma bleed），色邊沿掃描方向向右拖尾；交錯掃描的線結構可見，磁帶 dropout 呈白色短橫線，畫面底部約 2% 高度有 head-switching 撕裂雜訊帶；黑位被訊噪比與多代轉錄抬起，呈灰霧狀（NTSC 本來就有 7.5 IRE 的 setup 黑階，但灰霧不是 setup 造成的，是雜訊底），高光硬性剪裁；右下或右上有橘黃色日期字幕。
- **構圖**：4:3（1.33:1），主體隨手擺中間、頭上留白過多、水平線微傾；沒有三分法意識，靠變焦而不是走位改變景別，畫面邊緣常切到無關的人。
- **提示詞**：`1980s consumer camcorder frame, 4:3 interlaced video, soft 240-line VHS resolution with smeared low-bandwidth colour, on-camera tungsten lamp blasting the subject frontally, background falling to black two metres behind, clipped chalky skin highlights, milky lifted blacks, red chroma bleed smearing to the right, visible scan lines, white tape dropout streaks, head-switching tear band along the bottom edge, orange date stamp in the corner, shoulder-braced handheld tilt, deep focus throughout`
- **可組合**：`27 正面光`、`02 過度曝光`、`22 深景深`、`06 暖光源`、`37 弱光`
- **常見錯誤**：把 VHS 當成「加一層雜訊濾鏡」——真正的辨識點是 4:3 畫幅、色度滲流與底部 head-switching 雜訊帶，缺這三樣時加再多顆粒都只是數位偽舊。

---

### 18 十六毫米顆粒｜16mm Documentary Grain

> 風格參照：16mm documentary

- **技法核心**：肩扛手持 + 全現場光欠曝推感光 + Super 16 小片幅大顆粒，三者共構出「攝影師真的站在那裡」的在場感。
- **光**：只用現場既有光，不打電影燈。主光是未加色溫紙的窗（約 5600K，帶天空光時更冷），室內家用鎢絲實用光（2800–3000K，不是攝影棚的 3200K）直接混進畫面；整體以日光為基準平衡而不強行統一，於是臉部接近中性、背景牆與燈泡偏橘、窗外遠景偏青藍。反差靠一塊白牆或反光板做弱補光，暗面約為主光的四分之一（1:4），窗戶允許過曝 2–3 級並帶柔性 rolloff。
- **鏡頭**：9.5mm／12mm／25mm 定焦裝在 Super 16 機身（Super 16 對全片幅的換算係數約 2.9，視角約等於全片幅的 28／35／72mm），T2–T2.8 接近全開；機位在肩高、略低於眼平；24fps 配 180° 快門（1/48s）產生自然動態拖影；手持隨呼吸微幅浮動，跟焦是手動而且看得見一點點失誤。
- **色彩與質感**：負片寬容度帶來柔和的高光肩部；顆粒在中間調與被提亮的暗部最明顯且會蠕動（grain boil）；高光邊緣有輕微紅橘 halation 暈（來自紅感層與片基背面的反射）；陰影微微偏綠；飽和度自然不做加強；片門抖動（gate weave）與偶爾的毛髮、灰塵點。
- **構圖**：1.66:1（Super 16 原生）或裁 1.78:1；主體偏離中心，中景為主並刻意帶進環境；重新構圖是拍攝當下即時完成的，所以有短暫的重新找人、重新框；常有前景遮擋（門框、路人肩膀）。
- **提示詞**：`Shot on grainy Super 16mm colour negative pushed one stop, 25mm prime wide open at T2, shoulder-height handheld with breathing micro-movement, lit only by an uncorrected window against warm interior practicals, face sitting two stops below the blown-out window, dense visible grain through the midtones and lifted shadows, red halation blooming around highlights, gate weave, dust specks and a stray hair in the gate, 1.66:1 frame, hand-pulled focus that drifts`
- **可組合**：`08 窗光`、`41 雙性照明`、`20 中景`、`09 柔光`、`24 動態模糊`
- **常見錯誤**：一邊要 16mm 顆粒、一邊又要「打足光、乾淨無噪點」的畫面——窗光本身確實是大面積柔光（所以 `09 柔光` 可以疊），衝突的是光量：顆粒感來自照度不足與推感光，一旦補足照度、把感光度降下來，那個質地就消失了。散景也不會奶油化，Super 16 片幅小，T2 的背景仍然相對收斂。

---

### 19 偽紀錄片｜Found Footage

> 風格參照：found footage

- **技法核心**：攝影機是劇中人手上的道具，因此所有光源、機位與失誤都必須在故事世界內部說得通；技術缺陷不是瑕疵，是敘事證據。
- **光**：完全 diegetic。主光是機頂 LED（5500–6500K）或角色手上的手電筒，光軸隨機身擺動，陰影跟著甩；沒有任何補光，3 公尺外只剩噪點黑。手機螢幕作為近距自發光補一層青白色。自動曝光在明暗交界處來回抽動（AE pumping），光源直入鏡頭時整幅畫面被沖白。
- **鏡頭**：14–24mm 等效超廣角，f/1.8–2.8，ISO 推到 6400 以上；持機高度從腰際到臉部劇烈變動；急甩鏡（whip pan）時 CMOS 逐行讀取造成 rolling shutter 斜切變形；自動對焦反覆搜尋，跑動時畫面上下彈跳；小感光元件下景深很深，但畫面四角有解析度崩壞。
- **色彩與質感**：高 ISO 彩色噪點，暗部被壓縮編碼糊成方塊（macroblocking）；畫面中央因機頂燈過曝、邊緣全黑；偶發掉幀與畫面凍結；角落有 REC 紅點、電池格與時間碼；夜視段落切成單色綠加瞳孔反光。
- **構圖**：16:9 或直幅 9:16；主體常被畫框切一半或跑出框外再被追回；握把造成的隨機傾斜；持機者的手臂、袖子、呼吸霧氣入鏡；鏡頭掉落時出現貼地的怪異低角度。
- **提示詞**：`First-person handheld camcorder frame, 18mm ultra-wide at f/2, ISO 6400 colour noise, the only light a camera-mounted LED and a swinging flashlight carving a harsh cone and leaving everything past three metres in noisy black, centre blown out while the corners fall away into macroblocked shadow, focus visibly missed on the subject, rolling-shutter skew slanting the verticals during a whip pan, heavy motion blur from running, the operator's sleeve clipping the frame edge, REC dot and burned-in timecode in the corner, 16:9`
- **可組合**：`27 正面光`、`37 弱光`、`42 暗色調`、`24 動態模糊`、`39 低角度視角`
- **常見錯誤**：讓畫面出現「這台攝影機不可能拍到的東西」——第三人稱運鏡、正反打、沒有來源的臉部補光，只要出現一個，偽紀錄片的前提就整個垮掉。

---

### 20 定格動畫質感｜Stop-Motion Tactility

> 風格參照：stop-motion

- **技法核心**：微縮實體場景 + 微距小光圈爭取景深 + 逐格單張曝光帶來的細微閃爍與輪廓抖動，關鍵是讓人看出「這是被拍攝的實物」而不是被算圖的模型。
- **光**：小尺寸高精度燈具在微縮尺度上模擬大尺度光線——光纖點光源或迷你 LED 做單一硬主光，配一張小白卡做 1:4 補光；場景內的迷你燈泡（2700K）作為 practical 入鏡。縮尺最容易露餡的地方是衰減梯度：燈到物只有數十公分時，平方反比會讓前後幾公分之間就出現明顯的亮度落差，而真實大空間裡同樣的深度幾乎不衰減；所以燈要盡量拉遠、或用聚光與光纖束逼近平行光，讓照度在整個場景深度上盡量均勻。逐格曝光造成幀與幀之間 1–2% 的亮度跳動。
- **鏡頭**：24–50mm 微距或探針鏡頭，距離 1:6 比例的偶約 20–40 公分。注意焦段不要做「等效換算」：用 35mm 在 30 公分拍 1:6 的偶，透視關係等同於用 35mm 在 1.8 公尺拍真人，按比例縮短距離時透視完全不變；縮尺真正改變的是景深——同樣的構圖下景深急遽變淺，這才是必須收到 f/8–f/16、必要時同一格拍多張不同焦點再合成（focus stacking）的原因。機位壓到偶的眼睛高度；三腳架完全鎖死或用電腦控制的緩慢移動；小光圈帶來輕微繞射柔化。
- **色彩與質感**：材質必須看得出手工——毛氈纖維、黏土指紋、矽膠的半透光澤、木紋、接縫裡的灰塵、替換頭的分模線；飽和度中上但陰影略降；輪廓有逐格微抖（boil）；沒有動態模糊，邊緣一律銳利；每格之間有極輕微的曝光閃爍。
- **構圖**：1.85:1 或 1.78:1；舞台式的正面、居中演出；場景明確分成前景剪影、中景表演區與繪製背景幕三層；角色約佔畫面高度三分之一以露出整個微縮場景；留較多頭頂空間展示布景細節。另一種同樣關鍵的鏡頭是反過來貼到極近的材質特寫——只有在纖維、指紋、分模線被放大時，「實物」的證據才成立，所以 `32 特寫` 與這個寬鏡頭staging 是交替使用而非互斥。
- **提示詞**：`Miniature handmade set photographed frame by frame, 35mm macro lens 30cm from a sixth-scale puppet, f/11 focus-stacked so the felt fibres, plasticine thumbprints and dusty seams all stay crisp, one hard fibre-optic pinspot as key with a small white bounce card, locked-off tripod, warm practical bulbs inside the set, visible replacement-face seam line and armature joints, every edge razor sharp with no motion blur`
- **可組合**：`22 深景深`、`47 硬光`、`35 居中構圖`、`06 暖光源`、`32 特寫`
- **常見錯誤**：只寫 stop-motion style 會得到光滑的 3D 動畫塑膠感——必須指名具體材質與微縮比例，模型才知道要做「實物被拍攝」而不是「被渲染」。

---

### 21 賽博龐克街景｜Neon Cyberpunk Street

> 風格參照：Blade Runner lineage

- **技法核心**：夜景完全沒有天光，靠自發光招牌當主光、雨霧做體積散射、濕地面做鏡面反射，把有限的幾支光源在視覺上放大成整條街的照明。
- **光**：主光是畫面內的霓虹與 LED 廣告（2000K 琥珀對 9000K 青藍並置），從側上方灑在人物髮際與肩線；背後有穿過雨幕與煙霧的強力背光，形成實體感的體積光柱；臉部正面幾乎不打燈，只靠濕地反彈的一點下方補光，主副光比約 8:1，暗部保留可辨識的彩色訊息而非死黑。
- **鏡頭**：40–100mm 變形寬銀幕鏡頭（2x anamorphic）裝在 35mm 機身，T2.8；機位低到胸口或膝蓋、略仰拍讓招牌壓下來；緩慢推軌或升降，避免手持；中淺景深，散景呈直立的橢圓形，點光源拉出水平藍色條狀耀光。
- **色彩與質感**：青與洋紅的分離調色（陰影推青、高光推洋紅）；黑位壓低但帶色相；高光溢出產生 bloom；雨絲被背光打亮成細線；遠景因霧氣抬起黑位形成空氣透視；高飽和只保留給實用光本身，膚色維持接近中性以免整張變色片。
- **構圖**：2.39:1；垂直招牌密集堆疊填滿畫面上半；人在龐大結構與前景遮擋物之間顯得很小；主體偏離中心，另一側負空間交給一盞明亮實用光；前景（雨棚、人群、蒸氣）／中景（主體）／背景（樓體招牌）三層明確分離。
- **提示詞**：`Rain-soaked night street, no daylight at all, lit entirely by towering neon and LED signage, 2000K amber against 9000K cyan, backlit haze building solid volumetric shafts, rain streaks picked out by the backlight, faces held only by rim light and bounce off the wet asphalt, 75mm 2x anamorphic at T2.8, knee-height camera tilted up, oval bokeh, horizontal blue streak flares, neutral skin against saturated signage, crushed blacks that still hold cyan and magenta, 2.39:1`
- **可組合**：`11 自發光`、`36 冷光源`、`18 丁達爾光`、`05 背光`、`16 高飽和`
- **常見錯誤**：只給霓虹顏色卻忘了雨、霧與濕地面——霓虹的戲劇性來自被大氣散射與鏡面反射二次放大，乾燥清澈的空氣會讓同一組顏色變成廉價色片。

---

### 22 太空歌劇｜Space Opera

> 風格參照：space opera

- **技法核心**：真空中的單一平行硬光 + 行星反照的冷色弱補光 + 長焦深景深，用極端光比與比例尺物件把「體積」拍出來。
- **光**：恆星是唯一主光，光線近乎平行，投射陰影的邊緣銳利到幾乎沒有半影，而且沒有大氣散射來填補，陰影裡什麼都不剩。要注意講法：船體曲面上的明暗仍然依表面法線平滑遞減，真正「數公分內斷掉」的是邊緣、凸起與另一塊結構落下的投影。補光只來自行星反照（冷色 7000–9000K 藍），光比約 16:1，暗面只剩主光的十六分之一，僅存勉強可辨的細節。船體上的自發光實用光是第三層：推進器尾焰 1800K 橘、艙窗燈列 4300K 白，在真空中照不亮周圍的空間，只在鄰近的船體表面留下一圈光暈。
- **鏡頭**：大畫幅或 2x 變形寬銀幕；50–200mm 長焦壓縮巨大體積、讓船首與船尾看起來一樣大；T5.6–T11 深景深使全船銳利；機位低於物體下緣仰拍以誇大體量；電腦控制（motion control）的極慢橫移或推進，絕不手持。
- **色彩與質感**：高光接近中性白、陰影推冷藍，橘藍互補只出現在推進器與艙窗；星空因無大氣散射而是純黑、沒有任何漸層；船體表面有 panel line、燒灼污漬與微隕石坑等「使用過」的細節；直射恆星處有輕微鏡頭光暈與光圈葉片造成的星芒。
- **構圖**：2.39:1；用一個人、一架小艇或一扇艙門作為比例尺放在巨物邊緣，是體積感成立的唯一辦法；純黑太空佔畫面 60% 以上的負空間；船體或行星地平線作為低位的橫向切割線；主體常被推到畫面下三分之一或單側。
- **提示詞**：`Colossal vessel in vacuum, a single hard parallel sunlight key throwing razor-edged cast shadows with no atmospheric fill at all, cool 8000K planetary bounce as the only fill at sixteen to one, orange 1800K engine glow and lit window rows as self-illuminating practicals, one tiny suited human figure at an open hatch giving the scale, 135mm 2x anamorphic at T8 for edge-to-edge deep focus, camera below the hull looking up, panel lines, scorch stains and micrometeorite pitting across the plating, pure black gradient-free starfield, 2.39:1`
- **可組合**：`47 硬光`、`46 高對比`、`11 自發光`、`21 遠景`、`22 深景深`
- **常見錯誤**：在真空場景加進大氣霧或柔化的陰影邊緣，巨大感立刻縮水成塑膠模型；忘了放比例尺物件則會讓「巨大」根本無從判讀。

---

### 23 生活寫實｜Domestic Realism

> 風格參照：是枝裕和

- **技法核心**：單一窗光的大面積漫射 + 榻榻米高度的固定機位 + 低對比自然膚色，把攝影降到觀察者的位置。
- **光**：白天全靠自然光從障子（和紙拉門）或側窗進入，經和紙與白牆漫射成一面遠大於主體的柔光（5000–5600K）；補光只來自對側白牆的反彈，光比壓到 1:1.5–1:2，臉上幾乎沒有明顯的暗面。夜戲改用室內既有的頂燈與桌燈自上而下（日本家庭常見的 2700K 電球色到 5000K 晝白色都可能，照現場實際狀況），仍然不加電影燈；窗外允許輕微過曝，不做壓光處理。
- **鏡頭**：35–50mm 全片幅（接近人眼視角）為主，偶爾用 85mm 從房間另一端遠遠觀察；T2.8–T4——因為機位退到中景以上的距離，這個光圈的景深仍足以讓人物與家中陳設同時可辨。機位放低到坐姿或榻榻米高度，離地約 60–90 公分；三腳架固定或極輕微的手持呼吸；以中景到中近景為主，一次長時間不切。
- **色彩與質感**：以膚色自然為第一優先，整體低對比、陰影抬起、高光柔和收尾；輕度降飽和但植物的綠與木頭的黃棕保持真實；質感細膩、無明顯顆粒；白平衡就照現場混色狀態保留，不強行統一成單一色調。
- **構圖**：1.85:1 或 1.78:1；大量使用門框、走廊、窗櫺形成畫中畫；人物常被家具或前景物體遮住一部分；多人同框時各做各的事、視線不交會；畫面刻意留下生活痕跡（碗盤、曬衣、拖鞋、貼在牆上的紙）。
- **提示詞**：`Ordinary family home in the afternoon, the sole key a large paper-screened sliding door diffusing 5400K daylight across the room, fill only from an opposite white wall at a one-to-two ratio, 40mm lens at T4, tripod locked at seated tatami height about 70cm off the floor, natural skin tones, lifted shadows, gentle highlight rolloff, framed through a doorway, everyday clutter left in shot, 1.85:1`
- **可組合**：`08 窗光`、`09 柔光`、`43 低對比度`、`20 中景`、`34 封閉構圖`
- **常見錯誤**：把「自然」誤解成「沒有設計」——低對比與低機位都是刻意的技術選擇，一旦換回眼平機位並用電影燈把臉打亮，就變成普通的家庭劇。

---

### 24 宇宙恐怖｜Cosmic Horror

> 風格參照：cosmic horror

- **技法核心**：極端的比例落差 + 沒有動機的光源 + 欠曝與濃霧，把「看不清楚」本身當成主體來拍。
- **光**：畫面裡只有一團找不到來源的巨大輝光，從框外上方或地平線之下滲出，色溫與色調兩軸都刻意偏離自然——高色溫（8000K 以上）再往洋紅方向偏成紫，或反過來往綠方向偏成病態的黃綠（色溫只管藍↔橘那一軸，紫與黃綠必須靠 tint／magenta–green 軸做出來，兩軸要分開下指令，不能寫成「偏紫的 8000K」）；完全沒有補光，人物只拿得到輪廓光與四分之三背面的邊緣；整體曝光壓在正常值以下 1.5–2 級，讓陰影恰好落在噪點門檻邊緣，觀眾必須主動去辨認暗部裡有什麼。
- **鏡頭**：兩極化選擇——18–24mm 超廣角貼地仰拍讓人與巨物的比例徹底崩壞，或 135–300mm 長焦把遠處的東西壓到人物背後貼著；每秒僅數公分的極慢推軌。光圈跟著這個選擇走，不能兩頭都要：要「淺景深只留眼睛清晰」就開到 T2–T2.8，要「不該被看清的東西也保持清晰」的全景深就收到 T5.6–T8。
- **色彩與質感**：接近單色的低飽和底色，只保留單一非自然色的高飽和光源；黑位壓到剩約 5% 細節；濃霧讓遠景失去對比呈灰白的空氣透視；輕微顆粒與高光 halation；避開暖膚色，把膚色推向青灰。
- **構圖**：2.39:1 或 1.85:1；人物縮到畫面底部十分之一，純粹作為比例尺；巨大的負空間留給不可名狀之物或空無的天空；正面對稱構圖製造儀式感；地平線壓到極低或抬到極高以消除安全的中線。
- **提示詞**：`A lone figure at the bottom tenth of the frame, dwarfed by a vast fog-filled void, lit by a single glow with no visible source bleeding up from beyond the horizon, its colour pushed cold and then hard toward magenta into violet, no fill at all, only a thin rim along the figure's shoulders and the back of the head, underexposed two stops so the shadows sit just above the noise floor, 20mm at T2.8 tilted up from ground level, near-monochrome desaturation with the violet glow as the only saturated colour, ash-grey skin, fine grain, 2.39:1`
- **可組合**：`39 低角度視角`、`05 背光`、`42 暗色調`、`45 低飽和`、`21 遠景`
- **常見錯誤**：把恐怖寄託在怪物本身，寫滿觸手與血——真正的機制是比例、留白與無來源的光；主體越清晰、畫面越滿，恐懼感越低。
