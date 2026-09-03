# 光線篇｜光位、光質、光源

本檔涵蓋 21 項與「光」有關的技法，分成三條**互相正交**的軸：

- **光位**（光從哪個方向來）：`03 側光` `04 側逆光` `05 背光` `07 頂光` `10 髮絲光` `13 底光` `14 輪廓光` `27 正面光`
- **光質與強度**（光硬還是軟、強還是弱）：`09 柔光` `15 舞台光` `18 丁達爾光` `37 弱光` `40 強光` `47 硬光` `48 閃光燈`
- **光源與色溫**（光從什麼東西發出來、什麼顏色）：`06 暖光源` `08 窗光` `11 自發光` `12 火光` `36 冷光源` `41 雙性照明`

三條軸各取一項組成完整的打光描述。同一條軸內的項目通常互斥。

For a scoped visual-look subcontract, include numeric lighting values only when the user provided them. Otherwise
export qualitative source color, direction, hierarchy, shadow, and surface response rather than copying K values,
ratios, stops, exposure, or distance from the examples below.

---

## 一、光位與光形

### 03 側光｜Side Light

- **英文關鍵詞**：`side lighting` / `split lighting` / `raking light`
- **原理**：主光位於被攝體與相機連線的水平方位角 90°、仰角 0–15°，光線幾乎平行掠過臉部平面。因為光來自側面而非上方，鼻影是**橫向**投向暗側、直接併入暗側陰影連成一整片，不會像 30–45° 光那樣在亮側臉頰上留下獨立的 loop 或 Rembrandt 三角；皮膚毛孔、鬍渣與布料織紋被掠射（raking）拉出微浮雕。三個關鍵詞不是同義詞：`side lighting` 講的是光位、`split lighting` 是「臉正對相機時被 90° 光切成對半」的人像 pattern、`raking light` 是強調表面紋理的掠射用法，依需求擇一寫進提示詞。亮暗比從 4:1（2 stop）起跳，暗側完全不補光時可到 8:1（3 stop）以上。要留住這層微浮雕，靠的是掠射角與合焦，與焦段無關：光圈收到 f/5.6–f/8 讓整個臉部平面落進景深，比開到 f/2.8（景深只夠一隻眼睛，紋理反而糊掉）可靠得多。
- **情緒**：果決、疏離、內在分裂、被審視、雕塑感
- **提示詞**：`hard key light at 90 degrees camera-left, eye level, splitting the face into a lit half and a shadow half, the nose shadow running sideways into the dark side instead of dropping down the cheek, light raking across skin texture and fabric weave, shadow side left unfilled and falling to near black`
- **強化**：`47 硬光`、`46 高對比`、`42 暗色調`、`32 特寫`
- **衝突**：`27 正面光`、`44 亮調`、`43 低對比度`
- **常見錯誤**：只寫 `side light` 就收工，模型會退回 30–45° 的 loop／Rembrandt；必須明寫 "90 degrees"、"eye level"、"split the face into lit and shadow halves"、"shadow side unfilled"，否則暗側會被自動補亮成一般側前光。第二個常錯是同時要求 `split lighting` 與四分之三側臉：臉一轉開，90° 光就變成 short／broad lighting，對半的 split 不成立。

### 04 側逆光｜Three-Quarter Backlight

- **英文關鍵詞**：`three-quarter backlight` / `kicker light` / `side rim light`
- **原理**：光源在被攝體後方、偏離正後方 45°（水平方位角 135° 或 225°），仰角 20–45°。高光沿**靠光源那一側**的顴骨—下顎—肩線描出一條亮邊，寬度隨臉的轉向而變，通常不超過臉寬的 1/4。注意：主光在背後，臉的正面整片落在陰影裡，沒有被照亮的區域可以承接鼻影，所以看不到獨立的鼻影 —— 這正是它和側前光在提示詞上最容易被寫混的地方。正面五官要保持可辨識，得另外用反光板或環境光把暗部拉到亮邊以下約 3 stop（8:1）以內。與 `05 背光` 的分野就在這裡：側逆光仍有正面資訊，背光沒有。
- **情緒**：眷戀、回望、餘溫、將要離去、詩意距離
- **提示詞**：`key light behind the subject at 135 degrees rear-left, 30 degrees elevation, carving a bright edge along the cheekbone jawline and shoulder on the light side, the front of the face entirely in shadow yet still readable, sitting three stops under the rim, lifted only by a weak bounce card, dark background`
- **強化**：`14 輪廓光`、`18 丁達爾光`、`25 淺景深`、`圖二 05 煙霧體積光`
- **衝突**：`27 正面光`、`48 閃光燈`、`44 亮調`
- **常見錯誤**：寫成 silhouette 或 full backlight，把正面資訊全丟掉；正確做法是同一句裡同時交代「後方 135° 的邊緣高光」與「暗部仍可辨識的五官＋微量 fill」，兩者缺一就會滑向 `05 背光`。

### 05 背光｜Backlight

- **英文關鍵詞**：`backlight` / `contre-jour` / `silhouette lighting`
- **原理**：光源位於被攝體正後方水平方位角 180°、仰角 0–20°，相機直對光源；主體正面只剩環境反射，主體與背景的照度差可達 5–8 stop，以背景測光即成剪影，以臉部測光則背景整片 blow out。這裡有兩層對比要分開講：全域動態範圍極大（近黑剪影對上爆掉的天空），但鏡頭同時產生 veiling flare 抬升黑位，畫面中段的局部微對比反而下降、發灰 —— 強化欄的 `46 高對比` 指的是前者。髮際的光暈主要來自細髮絲的前向散射；底片會再疊一層由片基反射造成的紅橙色 halation，數位感光元件則表現為 bloom。
- **情緒**：神秘、不可知、崇高、身分隱匿、宿命感
- **提示詞**：`sun directly behind the subject at 180 degrees, low on the horizon, face rendered as a near-black silhouette against a blown-out sky, hair fringed with a glowing halo of scattered light, veiling flare washing across the frame and lifting the blacks`
- **強化**：`18 丁達爾光`、`02 過度曝光`、`46 高對比`、`21 遠景`
- **衝突**：`27 正面光`、`43 低對比度`、`48 閃光燈`
- **常見錯誤**：同時要求 `backlight` 又要求臉部清楚打亮 —— 物理上那等於補了正面光、已經不是背光；要嘛承認畫面是 silhouette、把敘事交給輪廓，要嘛直接改用 `04 側逆光`。

### 07 頂光｜Top Light

- **英文關鍵詞**：`top light` / `overhead light` / `downlight`
- **原理**：光源在被攝體正上方、仰角 75–90°；越接近 90°，水平方位角的影響越小（要到 90° 才真的完全失去意義）。照度集中在額頭、鼻樑、顴骨頂與肩線，眼窩、鼻下、下巴下緣與頸部落入深陷陰影，鼻影垂直下墜到人中或上唇；硬光且不補光時亮暗比可達 8:1 以上，腳下留一圈明顯的 pool。與 `13 底光` 是同一垂直軸的兩個極端、陰影方向完全相反，一個是審訊／神性，一個是恐怖。
- **情緒**：壓迫、被審問、罪疚、神性降臨、無處可逃
- **提示詞**：`single hard source mounted directly overhead at 90 degrees elevation, pooling light on forehead nose bridge and shoulders, eye sockets sunk into black, vertical nose shadow dropping onto the upper lip, floor pool beneath the feet, no fill light and nothing bouncing back into the eyes`
- **強化**：`47 硬光`、`46 高對比`、`42 暗色調`、`15 舞台光`
- **衝突**：`13 底光`、`27 正面光`、`44 亮調`
- **常見錯誤**：寫成「明亮的天花板燈」而失去壓迫感；必須指定單一硬光源、正上方、眼窩全黑、鼻下垂直陰影，並在同一句裡明寫 "no fill"，否則模型會回吐一張均勻的室內照明。

### 10 髮絲光｜Hair Light

- **英文關鍵詞**：`hair light` / `top backlight` / `gridded hair light`
- **原理**：位於被攝體後上方、仰角 45–60°、水平偏離正後方 30–45° 的小面積聚光（加 snoot 或 grid 收束），只落在頭頂與髮絲的鏡面高光上，不照到臉頰。出力要看髮色：深髮吸光多，可比主光高 1–1.5 stop；淺髮／金髮反射率高，通常要壓到與主光相當甚至更低，否則髮絲直接過曝糊成一片白。它的功能是把頭部從**暗背景**分離，本身不製造任何可見的臉部陰影 —— 所以它是可疊加的補充光、不是光位，任何主光位（含 `27 正面光`，那正是三點打光與美妝打光的標準組合）都能配。與 `14 輪廓光` 的差別是覆蓋範圍：髮絲光只管頭髮的局部亮邊，輪廓光描的是全身。
- **情緒**：精緻、被珍視、柔軟、廣告質感、可親近
- **提示詞**：`tight gridded hair light from behind and above, 45 degrees elevation and slightly off the rear axis, brighter than the key so the hairline is the brightest thing in frame, a crisp specular ribbon confined to the crown and loose flyaway strands, cheeks and forehead lit only by the key light, subject separated from a dark background`
- **強化**：`04 側逆光`、`42 暗色調`、`32 特寫`、`25 淺景深`
- **衝突**：`05 背光`、`44 亮調`、`43 低對比度`
- **常見錯誤**：寫成 `backlight` 或 `strong light from behind`，模型給的是後方一整片大光源 —— 不是臉沉成剪影，就是整個身體外緣都發亮、變成 `14 輪廓光`，那條只屬於頭頂的高光反而不見。要強調光源面積小、加 grid、高光只限頭頂與飛散髮絲、臉交給主光。

### 13 底光｜Underlighting

- **英文關鍵詞**：`underlighting` / `uplight` / `under-chin key light`
- **原理**：光源低於下巴、由下往上以 -30°～-45° 仰角照射，所有陰影方向反轉：鼻子在額頭上拉出一道往上爬的長影、眉弓陰影上翻進額頭、下巴下緣與顴骨下緣反而成為最亮的面，形成與「太陽在上」的日常經驗相反的違和感。色溫決定調性：1800–2200K 的火光偏戲劇、說書感；5600K 以上的冷白裸燈更臨床、更非人。與 `07 頂光` 是同一垂直軸的兩個極端。
- **情緒**：詭異、失控、原始恐懼、不祥、非人感
- **提示詞**：`bare cold white 5600K source placed below chin level, aimed upward at 45 degrees, every shadow inverted — nose shadow climbing the forehead, brow ridges throwing arcs upward, undersides of the chin and cheekbones the brightest planes, a huge distorted shadow of the head thrown up the wall behind, no fill`
- **強化**：`12 火光`、`47 硬光`、`39 低角度視角`、`圖二 01 德國表現主義`
- **衝突**：`07 頂光`、`44 亮調`、`27 正面光`
- **常見錯誤**：只寫 `creepy lighting` 或 `horror lighting`，模型只會把畫面調暗；必須明說光源在下巴以下、陰影往上投、鼻影落在額頭，才會真的翻轉陰影方向。另外別只丟 K 值 —— 模型對 "5600K" 的反應遠不如對 "cold white" / "firelight orange" 這類色彩形容詞，兩者要一起寫。

### 14 輪廓光｜Rim Light

- **英文關鍵詞**：`rim light` / `edge light` / `separation light`
- **原理**：兩盞（或環繞多盞）位於被攝體後方水平方位角 120°–240°、仰角 15–45° 的光，把整個身體外緣描成一條連續不斷的亮線。定義性的條件不是燈的絕對出力，而是**輪廓比正面亮 2–3 stop**：正面必須刻意壓低，觀眾才會先讀形狀、再讀細節。這也是它和三點打光裡那盞順手加的分離光的差別 —— 那盞只求把人從背景剝開，可以配任何主光；這裡的輪廓光主導整個畫面。與 `10 髮絲光` 的差別在於這是全身完整描邊，不是頭髮上的局部高光。
- **情緒**：英雄氣、危險、儀式感、距離、劇場性
- **提示詞**：`two rim lights at 135 and 225 degrees behind the subject, slightly above shoulder height, tracing an unbroken bright outline around the whole body, the front of the body held two to three stops down so only its shape reads, near-black set behind`
- **強化**：`05 背光`、`42 暗色調`、`23 全身照`、`18 丁達爾光`
- **衝突**：`48 閃光燈`、`44 亮調`、`43 低對比度`
- **常見錯誤**：只寫 `rim light` 卻沒壓低正面曝光，結果變成一張打亮的普通人像；要同時指定後方雙燈位置、輪廓線連續不中斷、以及主體正面比輪廓暗 2–3 stop。也不要在同一句寫 `silhouette`：正面只壓 2–3 stop 還讀得到細節，用了那個字模型會把整個人推成全黑，變成 `05 背光`。

### 27 正面光｜Frontal Light

- **英文關鍵詞**：`frontal lighting` / `on-axis light` / `flat front light`
- **原理**：光源與相機同軸（水平方位角 0°、仰角 0–10°，越接近 0° 陰影藏得越乾淨；超過 15° 投影就會從主體側後方露出來），投影被主體自身遮蔽而落在正後方，畫面上幾乎看不到陰影，鼻影短到只剩鼻孔下方一小塊；立體感本來由陰影提供，陰影消失＝體積消失，臉被壓平，亮暗比接近 1:1（實務 1:1–2:1）。它抹平的是**立體紋理**：毛孔、細紋、疤痕因為失去投影而變不明顯；但色斑、紅血絲、膚色不均這類**顏色**上的瑕疵不會被抹掉，在這種均勻照明下反而更顯眼。注意這是「方位」參數，與 `09 柔光` 的「光質」是兩條互不相干的軸。
- **情緒**：直白、坦率、清潔、天真、無防備、公事公辦
- **提示詞**：`light mounted on the camera axis at 0 degrees, level with the eyes, shadows falling directly behind the subject and hidden by the body, minimal nose shadow, skin texture flattened as pores and fine lines lose their shadows, even luminance from cheek to cheek`
- **強化**：`48 閃光燈`、`44 亮調`、`35 居中構圖`、`圖二 08 平面正面構圖`
- **衝突**：`03 側光`、`05 背光`、`07 頂光`
- **常見錯誤**：把「正面光」直接寫成「柔光」；正面光指的是 0° 方位，它可以是硬的 direct flash，也可以是柔的 beauty dish —— 寫提示詞時先鎖定方位與「陰影藏在主體後面」，再獨立決定硬柔。

---

## 二、光質與強度

**軸向說明**：本組七項描述的是光的**物理性質與能量**（光源角直徑、照度 lux、空氣介質、衰減曲線、陰影邊緣寬度），與 `03 側光`／`04 側逆光`／`05 背光`／`07 頂光`／`13 底光`／`27 正面光` 等「光位」項目是**互為正交的兩個軸**——任何一個光位都可以是柔的或硬的、強的或弱的。組裝提示詞時兩軸各取一項：先定方向（光從哪來），再定光質（09/47）與強度（37/40），兩者不可互相替代，也不會互相包含。

再往下還有第三個獨立軸：**影調與對比**（`42 暗色調`／`44 亮調`／`43 低對比度`／`46 高對比`）是「畫面的階調分布與明暗比」，由補光量與背景亮度決定，不由光質決定。柔光＋無補光＋暗背景會得到「柔邊但高對比」，明亮陰天則是「強光＋柔光＋低對比」——所以光質與對比不能互相推導，也不該互相排除。

另外注意：本組的 `15 舞台光`、`18 丁達爾光`、`48 閃光燈` 不是單純的光質或強度參數，而是**已經把光位＋光質＋介質綁死的複合場景條目**（例如 48 已內含正面光＋硬光＋近距離衰減）。它們不與 09/47、37/40 平行並列，而是取代其中數項；同時疊用時要檢查有沒有把方向或光質寫矛盾。

### 09 柔光｜Soft Light

- **英文關鍵詞**：`soft diffused light` / `large softbox lighting` / `overcast diffused light`
- **原理**：柔硬取決於光源相對被攝體的**視角大小（apparent source size）**，不是取決於亮度；當光源直徑接近或大於被攝體且距離近時角直徑大（>20°，例如 1.2m 八角柔光箱置於 1m 處約 62°〔2·arctan(0.6/1)〕、陰天整片天空近 180°），半影 penumbra 寬，陰影邊緣過渡帶可達數公分至數十公分。實務上明暗比常壓在 2:1–3:1（約 1–1.6 stop），暗部仍保有細節——但這個比值是**補光量決定的，不是柔度決定的**，柔光一樣可以打到 8:1。色溫由**光源本身**決定，柔光箱、反射傘等柔光配件幾乎不改變色溫：日光平衡燈頭或日光配柔光箱約 5500K，鎢絲燈頭配柔光箱仍是 3200K，陰天散射光偏藍約 6500–7500K。
- **情緒**：溫柔、親近、安全、體面、乾淨、無威脅
- **提示詞**：`lit by a large softbox placed close to the subject, shadow edges spreading softly over several centimetres, light wrapping around the jaw into the shadow side, open shadows keeping full detail, smooth gradation across the cheek, broad soft speculars instead of hard pinpoints, gentle two-to-one lighting ratio`
- **強化**：`08 窗光`、`44 亮調`、`43 低對比度`、`45 低飽和`
- **衝突**：`47 硬光`、`48 閃光燈`、`15 舞台光`
- **常見錯誤**：只寫 "soft lighting" 或 "soft light" 幾乎不會改變模型輸出，正確做法是明確給出光源尺寸／距離關係與陰影邊緣的過渡寬度（"large source close to subject, shadow edges spreading over centimetres"），讓柔度變成可執行的幾何條件。另一個常見誤解是把柔光等同於低對比：柔光只保證陰影邊緣是漸變的，畫面對比要靠 `43 低對比度` 或 `46 高對比` 另外指定。

### 15 舞台光｜Stage Lighting

- **英文關鍵詞**：`theatrical stage lighting` / `follow spot` / `hard-edged spotlight pool`
- **原理**：硬切邊來自 **ellipsoidal / profile 聚光燈（ERS、Leko）**——它有成像光學與四片 shutter，可以把光束切成明確的幾何邊緣，也能加 gobo；Fresnel 打出的是柔邊 wash，通常負責補光、背光與整場基調，不負責切邊。燈位自高位前側（俯角約 45°，McCandless 前側光的標準角度，追光與高位燈可到 60°）加上側翼 side boom，地面上形成一圈 light pool。背景之所以沉黑，主因**不是平方反比**，而是聚光燈的光束根本沒涵蓋到背景（beam 之外幾乎無直射光），再加上距離衰減，落差常在 4 stops 以上，主體因此被「從黑暗中挖出來」。鎢絲燈基底 3200K，常疊彩色 gel（congo blue、steel blue、amber 等效果片；CTB 屬色溫校正片，用途不同）做 rim 或背景，煙霧機讓光束本體可見。
- **情緒**：被注視、孤立、莊嚴、表演性、榮耀、緊繃
- **提示詞**：`a hard-edged follow spot from high front-left carves the performer out of a black void, a bright circular pool of light on the stage floor, the beam's cut edge clearly visible in theatrical haze, everything outside the beam falling away to pure black, warm tungsten key at 3200K with a saturated blue gel rim from a side boom`
- **強化**：`18 丁達爾光`、`42 暗色調`、`46 高對比`、`圖二 05 煙霧體積光`
- **衝突**：`44 亮調`、`43 低對比度`、`09 柔光`
- **常見錯誤**：寫成普通的 "spotlight" 卻讓模型把背景也照亮，舞台光的成立條件是**光束切邊 + 背景急速衰減到全黑**，必須把 "pool of light"、"beam edge"、"background falls off into black" 一起寫進去。

### 18 丁達爾光｜Crepuscular Rays / God Rays

- **英文關鍵詞**：`crepuscular rays` / `god rays` / `volumetric light shafts`
- **原理**：光束本身要「看得見」需同時滿足三個條件：(1) 空氣中有介質——塵埃、霧、水氣、煙——產生 Mie 散射；(2) 有遮擋物（窗框、樹冠、門縫、雲隙）切出光束幾何；(3) 相機朝向光源側拍攝，即以被攝體為頂點時，相機方向與光源方向的夾角大於 90°（逆光或側逆光位），因前向散射最強。第四個實務條件是**光柱要有較暗的背景才讀得出來**，打在亮牆或亮天空上的光柱等於不存在。太陽仰角約 10–20° 時光線斜穿介質的路徑長、光柱拉得最長最明顯。收小光圈至 f/11–f/16 可得到星芒（sunstar），但要注意小光圈同時會讓鏡頭鬼影 ghosting 更明確，並不會「壓住溢光」。
- **情緒**：神聖、崇高、寧靜、超自然、懷舊、渺小
- **提示詞**：`low sun about fifteen degrees above the horizon raking through gaps in the foliage, dust and mist scattering it into separate volumetric shafts, camera shooting back into the light, each shaft brightest right at the gap and fading as it travels, the shafts read against a dark shaded background, haze lifting the blacks, small-aperture sunstar where the sun clears the branches`
- **強化**：`05 背光`、`04 側逆光`、`08 窗光`、`42 暗色調`
- **衝突**：`09 柔光`、`27 正面光`、`44 亮調`
- **常見錯誤**：只丟 "god rays" 會得到憑空浮現、沒有來源也沒有介質的假光斑；必須把**介質**（dust / haze / mist / smoke）、**遮擋物**（gaps, window frame, doorway）與**逆光方向**（shooting into the light）三者同時寫出來。

### 37 弱光｜Low Light

- **英文關鍵詞**：`low-light available light` / `high-ISO night interior` / `low-key ambient`
- **原理**：必須先分辨兩種東西——**low-key ambient**是「暗場景的正確曝光」，主體臉部仍落在可讀的中間調上，只有環境沉入暗部；**underexposed**是整張影像往下拉，連高光都灰掉、色彩劣化，那是失誤不是風格。低照度場景約 1–10 lux（EV100 約 −1 至 2）。以 3 lux 的室內為例，要 f/1.4、1/50s、ISO 6400 才勉強站上正確曝光；再暗就只能靠更慢的快門（1/30–1/15，已逼近手持極限）或 ISO 12800，因此必然帶明顯 luminance noise、色彩噪點與動態範圍壓縮。
- **情緒**：私密、孤獨、疲憊、危險、真實、夜行
- **提示詞**：`a night interior lit only by one practical lamp, around three lux, exposed for the face so the skin keeps readable mid-tones while the rest of the room sinks to near black, visible ISO 6400 luminance grain in the shadows, f/1.4 shallow focus, no fill light, the lamp's own highlight still clean and not smeared`
- **強化**：`42 暗色調`、`11 自發光`、`25 淺景深`、`圖二 06 單光源夜戲`
- **衝突**：`40 強光`、`02 過度曝光`、`44 亮調`
- **常見錯誤**：寫 "dark, underexposed" 會換來一張糊掉的死黑圖；正確做法是指定「主體正確曝光、環境自然衰減」並主動要求高 ISO 顆粒（"exposed for the face…, visible ISO 6400 grain"），把弱光寫成曝光策略而不是把亮度調低。

### 40 強光｜High-Intensity Light

- **英文關鍵詞**：`high-intensity light` / `blinding bright sunlight` / `blown-out clipped highlights` / `100,000 lux daylight`
- **原理**：講的是**能量與照度**，不是光源尺寸。正午直射日光約 100,000 lux（EV 15–16；Sunny 16：f/16 1/125 ISO 100 ≈ EV 15），specular highlight 超過感光元件上限而 clipping 成純白無細節，直射時明暗比常在 8:1（3 stop）以上，伴隨眩光、鏡頭 flare、汗光、熱浪扭曲與被攝者眯眼的生理反應。與 47 硬光正交：強光可以被雲層漫射而仍然很柔（明亮陰天約 10,000–20,000 lux，依然是強光，但柔、且低對比），硬光也可以來自一支低功率裸燈。
- **情緒**：灼熱、壓迫、暴露、亢奮、乾渴、無處可躲
- **提示詞**：`blinding noon sun, around 100,000 lux, speculars clipping to pure white on skin and chrome, shadows dropping three stops below, glare and veiling flare washing across the frame, heat shimmer rising off the ground, the subject squinting hard against the light`
- **強化**：`47 硬光`、`02 過度曝光`、`46 高對比`、`圖二 15 沙塵單色`
- **衝突**：`37 弱光`、`42 暗色調`、`圖二 06 單光源夜戲`
- **常見錯誤**：把「強光」當成「硬光」的同義詞而只寫 harsh；強光要寫的是亮度、高光 clipping 與眩光生理反應，若同時要銳利落影必須另外疊上 `47 硬光` 的陰影邊緣描述。反過來也別以為強光就一定高對比——明亮陰天是強光配柔光配低對比，對比要另外指定。

### 47 硬光｜Hard Light

- **英文關鍵詞**：`hard light` / `bare-bulb direct light` / `sharp-edged shadows`
- **原理**：光源相對被攝體的角直徑極小（<5°；正午太陽僅 0.53°，遠距裸燈、Fresnel 聚光同理），半影 penumbra 幾乎為零，陰影邊緣在數毫米內從全亮切到全暗，接近一條刀鋒線。斜射時把皮膚毛孔、布料織紋、牆面粗糙度全部拉出微影浮凸；無補光時明暗比可達 4:1–8:1（2–3 stop），只靠環境反射填暗部時還會更高。光源離被攝體越遠，角直徑越小、光質越硬。
- **情緒**：銳利、殘酷、緊張、陽剛、審問感、不留情面
- **提示詞**：`a single undiffused point source, no fill at all, shadow edges terminating in a knife-thin line within a millimetre or two, a crisp cast shadow stamped on the wall behind, pores and fabric weave raked into relief, hot speculars on cheekbones and brow, eight-to-one lighting ratio`
- **強化**：`40 強光`、`46 高對比`、`03 側光`、`圖二 01 德國表現主義`
- **衝突**：`09 柔光`、`43 低對比度`、`44 亮調`
- **常見錯誤**：只寫 "harsh lighting" 模型多半只是加對比曲線而陰影邊緣依然糊；必須描述**陰影邊緣寬度**（knife-thin / razor-sharp shadow edge）、**紋理浮凸**與明確 **no fill light**，硬度才會真的出現。

### 48 閃光燈｜Direct On-Camera Flash

- **英文關鍵詞**：`direct on-camera flash` / `harsh flash snapshot` / `paparazzi flash`
- **原理**：閃光管位於鏡頭光軸上、口徑極小、不加柔光罩，色溫約 5500–6000K，全出力閃光持續時間約 1/1000s（小出力更短）足以凍結動作。因為同軸且點狀，會同時出現五個特徵：主體正後方牆面被壓出**硬邊落影**、鼻尖與額頭的油光 hotspot 與最靠近的前景**過曝 clipping**、背景依平方反比急墜（距離加倍掉 2 stops：主體 1.5m、背景 6m 就差 4 stops，房間深處直接沉黑）、視網膜反射造成**紅眼**（同軸＋暗環境下瞳孔放大）、以及正面無立體感、相對環境鎢絲燈偏冷的 snapshot 質地。這是直打美學，與棚拍柔光箱是相反方向的東西。
- **情緒**：突兀、當下、粗糙、真實、狼狽、被抓拍
- **提示詞**：`direct undiffused on-camera flash at 5600K, flat frontal light with no modelling, greasy hotspots on nose and forehead, a hard-edged shadow stamped on the wall right behind the subject, the nearest foreground clipping while the depth of the room falls away to black, faint red-eye, snapshot feel`
- **強化**：`27 正面光`、`47 硬光`、`42 暗色調`、`圖二 14 數位早期`
- **衝突**：`09 柔光`、`05 背光`、`43 低對比度`
- **常見錯誤**：寫成 "studio flash / softbox flash" 會得到乾淨的棚拍柔光，完全不是這一項要的東西；必須寫死 **on-camera、direct、undiffused**，並補上背後硬邊落影與背景急速衰減，snapshot 感才會成立。

---

## 三、光源與色溫

### 06 暖光源｜Warm Light Source

- **英文關鍵詞**：`warm practical light` / `tungsten light source` / `incandescent glow`
- **原理**：光源本身色溫落在 2700–3200K（家用鎢絲燈泡約 2700K、鹵素與影視鎢絲燈 3000–3200K、暖白 LED 2700–3000K；高壓鈉氣路燈更低，約 2000K，低壓鈉燈近乎單色橘黃，嚴格說沒有可用的色溫值）。光譜紅橘分量高、藍光稀薄，以 5600K daylight 白平衡拍攝時整體偏 amber。實體燈具多為小面積光源，可近似點光源、遵守平方反比：距離加倍光量剩四分之一，被攝體距燈 1m 與 2m 相差約 2 級曝光，因此臉亮、背景快速掉入暗部，陰影邊緣也偏銳——除非加燈罩或紙燈籠把它擴成面光源，那才是柔的。典型參數 f/1.8–f/2.8、ISO 800–1600、1/50s。
- **情緒**：溫暖、親密、懷舊、安全感、慵懶、私密
- **提示詞**：`warm tungsten table lamp just outside the frame, camera left, a small amber pool falling visibly from the lit face into a much darker background, skin rendered honey-gold, one restrained patch of cool blue-grey ambient kept behind for contrast`
- **強化**：`01 暖色調`、`37 弱光`、`42 暗色調`、`46 高對比`
- **衝突**：`36 冷光源`、`38 冷色調`、`48 閃光燈`
- **常見錯誤**：只寫 "warm lighting" 而不指定色溫與燈具實體，模型會回一張平均的橘色濾鏡照；正確做法是指名光源物件（table lamp / bare bulb / sodium street lamp）、給出 K 值與拍攝白平衡、寫出衰減級數，並保留一小塊冷色環境光作對照，暖才成立。兩點界線要記住：那塊冷色只是次要環境對照，主光仍是暖的，所以不牴觸與 `36 冷光源` 的衝突（衝突指的是誰當主光）；另外本條的燈具可以不入鏡，一旦要求「發光物件必須在畫面裡看得見」，那是 `11 自發光`。

### 08 窗光｜Window Light

- **英文關鍵詞**：`window light` / `north-facing window light` / `soft directional daylight`
- **原理**：窗戶把整片天空裁切成一塊有邊界的面光源，相對於人臉尺寸極大，陰影半影帶（penumbra）寬而柔，但方向仍然明確（陰影一律落在背窗側）。衰減方面：大面積光源在近距離掉得比平方反比慢，被攝體從離窗 1m 移到 2m 約掉 1.5–2 級，距離再拉開才逐漸趨近平方反比；室內若是深色、不回光的牆面會掉更快，淺色牆面則會回光補進陰影、把光比拉平。大面積柔光、明確方向性、明顯縱深衰減三者同時成立，這是窗光無法被單純「柔光」取代的原因。古典肖像畫室採 north-facing window（北半球）的傳統，是因為終日不受直射陽光掃過、只吃天空散射光，色溫穩定在 6000–7500K；一旦是直射陽光穿窗，性質立刻轉為硬光加窗框投影圖案，那已經歸 `47 硬光`。
- **情緒**：靜謐、日常、真實、沉思、乾淨、微微感傷
- **提示詞**：`large north-facing window camera left, subject standing one meter from the glass, soft 6500K skylight wrapping one cheek, shadow side about one stop under the lit side, light falling away another stop toward the back of the room, gentle luminance gradient down the wall behind, sheer curtain softening the edge, no direct sunlight`
- **強化**：`09 柔光`、`03 側光`、`43 低對比度`、`圖二 23 生活寫實`
- **衝突**：`48 閃光燈`、`47 硬光`、`15 舞台光`
- **常見錯誤**：寫成 "natural light" 就收手，模型會給無方向的平光；必須指定窗在畫面的哪一側、被攝體離窗多遠、陰影落在哪一邊、亮暗側差幾級、往房間深處再掉幾級。特別注意別把「臉的亮暗側光比」和「離窗的距離衰減」寫成同一個數字——前者是 lighting ratio，後者是 falloff，兩者要分開給；混在一起寫，窗光最值錢的方向性與縱深就全部消失，只剩一張亮亮的室內照。

### 11 自發光｜Practical Light in Frame

- **英文關鍵詞**：`practical light source visible in frame` / `screen glow on face` / `motivated in-frame source`
- **原理**：光源是畫面內可見的發光物件本身——手機、筆電螢幕、燈籠、發光道具——通常手持在胸口高度、距臉 30–50cm，形成由下往上 30–60° 的 underlighting（底光）角度：鼻影與眉骨陰影往額頭上方投射、眼窩由下被填亮、下巴與喉頭出現不自然亮面。色溫依發光內容而定：白底介面的白點多落在 6500–7500K（部分手機的鮮豔模式更高），播放影片時會隨畫面跳色，燈籠或暖色道具則 2000–3000K。要留意 6500K 在日光白平衡下其實接近中性，螢幕之所以「看起來藍」，來自它與暖色室內光的並置以及白光 LED 的藍光尖峰；若場景以 3200K tungsten 平衡，藍味才會被推到極端。光源極近使 falloff 極陡，臉亮而後方牆面近乎全黑，需 f/1.4–f/2、ISO 1600–3200。
- **情緒**：孤獨、著迷、詭祕、疏離、窺看、當代焦慮
- **提示詞**：`phone screen held at chest height as the only light source, the glowing screen itself visible in frame, cool bluish-white 7000K glow raking up the face from below, nose and brow shadows thrown upward onto the forehead, a single rectangular catchlight in each eye, room behind falling to near black, shot at f/1.8`
- **強化**：`13 底光`、`37 弱光`、`42 暗色調`、`圖二 06 單光源夜戲`
- **衝突**：`44 亮調`、`07 頂光`、`40 強光`
- **常見錯誤**：把它寫成一般低調打光而漏掉「發光物件必須留在畫面內、看得見」這個定義性條件；正確做法是描述發光體的形狀、握持高度、與臉的距離，並指定它在眼球上留下的 catchlight 形狀，觀眾要能一眼判讀光是從哪個物件出來的。另外別把「光從下面來」寫成 underexposed 之類的曝光詞——這裡要的是 underlighting／lit from below，是光位，不是曝光。

### 12 火光｜Firelight

- **英文關鍵詞**：`firelight` / `flickering candlelight` / `campfire glow`
- **原理**：燃燒光源色溫大致落在 1700–2000K（燭焰約 1850K，營火隨焰體與燃料在 1700–2100K 之間浮動），紅橘分量壓倒性、藍光近乎缺席，膚色轉 amber 而藍色物件塌成灰黑。火焰是體積會變形的小面積光源，強度以每秒數次的隨機頻率跳動（flicker），光線方向、亮度與陰影邊緣同步抖動；單燭陰影偏硬，營火因焰體較大而稍軟。火在前下方時，在顴骨、眉弓、鼻尖留下的是高光（specular highlight）而不是 rim light——要有 rim 得把火移到人物後方。實拍常用 f/1.4、ISO 3200、1/48s（24fps、180° 快門），讓火光的不穩定被記錄成畫面的呼吸。
- **情緒**：原始、危險、儀式感、催眠、溫暖中的不安
- **提示詞**：`single campfire just below and in front of the subject at 1900K, caught mid-flicker so the orange-red light lands unevenly across the face, one cheek hotter than the other, hard-edged shadows thrown upward, hot speculars on the cheekbones and brow, everything beyond the fire's reach falling into deep blue-black night`
- **強化**：`13 底光`、`06 暖光源`、`46 高對比`、`37 弱光`
- **衝突**：`43 低對比度`、`45 低飽和`、`48 閃光燈`
- **常見錯誤**：只寫 "warm firelight"，得到的是一盞靜態橘燈。靜態圖模型不理解時間，要改用「某一瞬間的不均勻分佈」來描述——caught mid-flicker、一邊臉比另一邊亮、陰影邊緣不規則；flickering / pulsing / shadow edges jittering frame to frame 這類時間性寫法留給影片模型。另外火光照不到的地方要讓它直接沉入黑，不要補環境光，火才會有可讀的「照明半徑」。

### 36 冷光源｜Cool Light Source

- **英文關鍵詞**：`cool light source` / `overcast skylight` / `cool white fluorescent / HMI`
- **原理**：關鍵是「光源色溫高於拍攝白平衡」這個相對關係，不是絕對 K 值——陰天 6500–8000K、blue hour 天空散射光 9000–12000K、冷白螢光燈 4000–6500K（且帶綠偏，需 minus-green／洋紅 gel 修正）；HMI 與冷白 LED 約 5600–6500K，本身是日光平衡的中性光，只有在 3200K tungsten 平衡下才會極端偏藍。藍色分量高、紅色被壓縮，膚色轉青灰。陰天本質是覆蓋半天球的巨型光源，方向性弱（只剩微弱的由上而下）、陰影淺、對比約 2:1。夜戲的月光模擬（moonlight effect）則相反：常用高位 HMI 打硬光再往藍調，做出冷而銳利的陰影——順帶一提，真實月光是反射的日光，實測約 4100K，銀幕上的藍月是敘事慣例而非物理。至於 day-for-night 是另一件事：白天實拍，靠曝光不足與冷色調偽裝成夜晚，不要跟月光硬光混為一談。
- **情緒**：疏離、清醒、臨床、寒冷、機械、無情
- **提示詞**：`overcast 7500K skylight from a broad grey sky, shot on 5600K daylight white balance so the blue-cyan cast sits in the lit skin and concrete themselves, soft near-shadowless wrap with only a faint top-down direction, flat 2:1 contrast, palette desaturated toward steel and slate`
- **強化**：`38 冷色調`、`45 低飽和`、`43 低對比度`、`圖二 03 北歐冷冽`
- **衝突**：`06 暖光源`、`01 暖色調`、`16 高飽和`
- **常見錯誤**：把「冷光源」寫成後製藍色濾鏡，整張蒙一層藍霧。分辨方法很簡單：冷光源染的是「被光照到的地方」——亮部帶藍，因為那就是光本身的顏色；冷調色染的則是整張、尤其是陰影。正確做法是指名光源本體（overcast sky / blue hour / HMI / fluorescent tube）與 K 值，並同時給出拍攝白平衡當參照，色偏才有依據，否則 "7500K" 對模型只是裝飾字，回給你的仍然是一張藍濾鏡照。

### 41 雙性照明｜Bisexual Lighting

- **英文關鍵詞**：`bisexual lighting` / `cyan and magenta cross lighting` / `dual-gel split lighting`
- **原理**：兩盞上色片的燈從左右夾擊被攝體——一側 cyan／blue，另一側 magenta／pink，兩盞強度接近。水平角度決定成敗：各約 90°（純側光）時，兩色交界剛好落在鼻樑與臉部中線；往後移到 120–150° 就變成兩道只勾邊的 rim light，五官不會被照亮，兩色也不會在臉中央相遇。色片不落在黑體軌跡上，用 K 值描述並不精確（藍綠 gel 頂多粗略說成「比 full CTB 更冷的 8000K 以上冷端」），實務上直接指定 RGB LED 的色相更可靠。另外 cyan 與 magenta 並不是互補色（互補對是 cyan↔red、magenta↔green、yellow↔blue）：兩者加色混合得到偏藍紫的淡白，不會回到中性膚色；真要在重疊區還原中性膚色，得改用 orange／teal（琥珀＋藍）這種互補配置。也因此臉部立體感主要由色相差建立，左右亮度接近，畫面張力來自暗底加兩道高飽和色光；背景另補一盞紫或深藍做分離。這是 2010 年代後 MV、科幻與夜店場景的標誌性打光。
- **情緒**：當代、曖昧、電子感、夜生活、性感、人工亢奮
- **提示詞**：`cyan LED at 90 degrees camera left, magenta LED at 90 degrees camera right, the two colour edges meeting along the nose bridge, where they overlap the skin reads pale lavender-white rather than neutral, no fill light between them, dark violet haze behind, hard specular edges`
- **強化**：`15 舞台光`、`16 高飽和`、`37 弱光`、`圖二 21 賽博龐克街景`
- **衝突**：`45 低飽和`、`27 正面光`、`44 亮調`
- **常見錯誤**：只寫 "pink and blue lighting"，模型會回一團平均混合的紫霧；必須指定兩盞燈各自的左右方位與夾角、兩色交界落在臉上的哪一條線、中央重疊處是什麼顏色，並明說不打補光，雙色夾擊的體積感才出得來。另外 "bisexual lighting" 是網路流行語而不是棚內術語，部分模型對它反應不穩定或直接被安全過濾攔下；提示詞主體請寫 cyan／magenta cross lighting 的物理描述，把這個詞當風格標籤放最後就好。
