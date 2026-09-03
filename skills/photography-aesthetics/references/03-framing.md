# 構圖篇｜景別、景深、動態、視角

本檔涵蓋 18 項技法，分成四條軸：

- **景別**（主體在畫面中多大）：`31 極端特寫` → `32 特寫` → `19 近景` → `20 中景` → `23 全身照` → `21 遠景`
- **景深與動態**：`22 深景深` ↔ `25 淺景深`、`24 動態模糊`
- **相機高度**：`33 鳥瞰` → `17 高角度拍攝` → 眼平（無編號，但要用就明寫） → `39 低角度視角`
- **主體朝向**：正面 0°（預設，無編號）→ `30 四分之三側面` → `26 斜側視角` → `29 側面視角` → `28 背面視角`
- **構圖類型**：`34 封閉構圖`、`35 居中構圖`

相機高度與主體朝向是**兩條可自由交叉組合的獨立軸**，寫提示詞時要同時指定，缺一模型會自己填預設值。

---

## 一、景別、景深與動態

### 19 近景｜Medium Close-Up

- **英文關鍵詞**：`medium close-up` / `MCU` / `chest-up shot`
- **原理**：切點落在胸線／腋下上方（襯衫第一顆鈕扣一帶），頭頂留 5–8% headroom，臉佔畫幅高度約 1/3–2/5、肩寬約佔畫幅寬一半；等效 85–105mm、機位距被攝者 1.8–2.5m（全片幅 3:2 基準）。要注意透視只由「機位到被攝者的距離」決定，與焦段無關——退到 2m 外，鼻與耳的相對比例才接近肉眼所見、鼻子不會被放大；85mm 的作用只是讓你站在這個距離還切得到胸線。敘事上它同時保住可讀的微表情與肩線姿態，是對白戲、訪談與 reaction shot 的預設景別。
- **情緒**：親近但不侵犯、專注、可信任、對話感、被傾聽
- **提示詞**：`medium close-up framed at the chest line, 85mm equivalent, camera two meters away, slight headroom above the head, both shoulders fully inside the frame with the bottom edge crossing the chest, micro-expressions readable, background gently separated, natural eye-level perspective`
- **強化**：`30 四分之三側面`、`09 柔光`、`25 淺景深`、`10 髮絲光`
- **衝突**：`31 極端特寫`、`21 遠景`、`23 全身照`
- **常見錯誤**：agent 常把它寫成 "portrait"，模型就在頭肩與半身之間亂飄；正確做法是明寫切點 "framed at the chest line" 加上焦段與拍攝距離，把構圖釘死。

### 20 中景｜Medium Shot

- **英文關鍵詞**：`medium shot` / `waist-up shot` / `MS`
- **原理**：切在腰線（皮帶上緣）或略高，頭頂到切點的可見身體填滿畫幅高度九成，臉只佔畫幅高度約 1/4–1/3（比近景明顯小一級），雙手與手勢完整入鏡；等效 40–65mm、距離 1.5–2.2m（全片幅 3:2 基準：50mm 站 1.6m 剛好切在腰線；同一支 50mm 退到 3m 就變成切到膝蓋的美式景了）。這個焦段接近人眼視角、透視自然，環境開始有存在感但仍從屬於人。敘事功能是承載「人與人、人與道具的互動」，也是雙人對話 two-shot 的標準寬度。
- **情緒**：敘事中性、社交距離、觀察、平衡、事情正在發生
- **提示詞**：`medium shot cut at the waistline, 50mm equivalent, camera about one and a half meters away, hands and gestures fully visible inside the frame, environment readable but subordinate, natural human-eye perspective, moderate background separation`
- **強化**：`26 斜側視角`、`22 深景深`、`08 窗光`、`圖二 23 生活寫實`
- **衝突**：`31 極端特寫`、`21 遠景`
- **常見錯誤**：只寫 "medium shot" 時模型多半只給到胸線，等於退化成近景；必須補 "cut at the waistline, hands visible in frame" 才守得住腰線與手勢。

### 21 遠景｜Long Shot / Wide Shot

- **英文關鍵詞**：`wide shot` / `long shot` / `establishing shot`（更寬的一級寫 `extreme long shot`）
- **原理**：人物全身佔畫幅高度不到 1/3，extreme long shot 可低到 1/10 以下，地平線、建築、天空等環境元素佔去絕大部分面積；等效 16–35mm、距離 10m 以上（全片幅 3:2 基準：24mm 站 10m，1.7m 的人約佔畫幅高度 1/6；同一支鏡頭退到 30m 就掉到 1/18，那已經是 extreme long shot）。廣角一次把天地與環境收進來，並拉開近前景與遠方的距離感，天地比例與人物落點成為構圖主軸。敘事功能是交代地點、規模，以及人物在世界中的孤立與渺小，通常作為 establishing shot 使用。
- **情緒**：渺小、孤獨、壯闊、疏離、宿命感、地理感
- **提示詞**：`wide establishing shot, 24mm equivalent from about ten meters, a lone figure standing roughly one sixth of the frame height, vast terrain rolling back to the horizon, the horizon sitting low so the sky fills the upper two thirds, detail holding from foreground to distance`
- **強化**：`22 深景深`、`39 低角度視角`、`18 丁達爾光`、`圖二 09 固定長鏡頭`
- **衝突**：`31 極端特寫`、`32 特寫`、`25 淺景深`
- **常見錯誤**：一邊寫 wide shot 一邊要求 "detailed facial expression"，兩者物理上互斥；遠景的敘事要交給剪影、姿態、行進方向與人／環境的面積比。

### 22 深景深｜Deep Focus

- **英文關鍵詞**：`deep focus` / `deep depth of field` / `hyperfocal distance`
- **原理**：f/8–f/16 搭配 18–35mm 廣角。以 28mm f/11 為例，超焦距約 2.4m，對在 2.4m 時 1.2m 到無限遠同時落在景深內。小光圈吃光：晴天 ISO 100、f/11 的正確快門是 1/250s（Sunny 16 的等值曝光），室內就得靠大功率燈具、拉高 ISO 或上腳架延長曝光把照度補回來，否則只能開大光圈而失去深景深——這是「照度」問題，跟燈的色溫無關（若日光與燈光混用，色溫要另外統一）。再縮到 f/22 以上，繞射反而會吃掉整體解析度。它讓前景道具、中景主體、背景人物三層同時清晰，觀眾自行選擇看哪裡，建立的是「人物與環境的關係」。
- **情緒**：客觀、資訊密集、寫實、無處可躲、多線並置
- **提示詞**：`deep focus, 28mm equivalent at f/11 focused at the hyperfocal distance, three staged planes — a bottle and an ashtray on the table edge in the foreground, the seated subject in the mid-ground, a second figure standing in a lit doorway far behind — every plane rendered equally sharp, crisp texture from the nearest object to the back wall`
- **強化**：`21 遠景`、`40 強光`、`46 高對比`、`圖二 07 單點透視對稱`
- **衝突**：`25 淺景深`、`37 弱光`、`31 極端特寫`
- **常見錯誤**：只寫 "everything in focus" 卻沒安排三層內容，模型回傳一個清晰但空曠的背景；要逐層指名前／中／後各放什麼物件與人。

### 23 全身照｜Full Shot

- **英文關鍵詞**：`full shot` / `full body shot` / `full-length portrait`
- **原理**：完整人形入鏡，頭頂與腳底各留 5–10% 餘白，人物佔畫幅高度 80–90%；等效 35–50mm、距離 3–4.2m（全片幅 3:2 基準：50mm 站 4m 剛好，退到 6m 人就只剩畫幅高度的六成），時尚全身則常用 85–135mm 退到 7–11m，用更長的工作距離消掉近距離廣角的比例畸變。敘事功能是交代體態、服裝全貌與整體肢體語言，是舞蹈、動作、時尚與角色定裝 character sheet 的標準景別。
- **情緒**：完整、展示性、姿態語言、劇場感、身份可辨識
- **提示詞**：`full shot, entire body inside the frame with feet visible and a small margin above the head, 50mm equivalent from four meters, upright posture and silhouette clearly readable, shoes and hemline sharp, even light across the whole figure`
- **強化**：`35 居中構圖`、`15 舞台光`、`27 正面光`、`圖二 08 平面正面構圖`
- **衝突**：`31 極端特寫`、`32 特寫`
- **常見錯誤**：漏寫 "feet visible / entire body inside the frame"，模型習慣裁到腳踝；另外別用 24mm 拍全身——那要站進 2m 內，近距離廣角會誇大「最靠近鏡頭的部位」：機位在頭高就頭大腳小，機位放低就下肢被異常拉長。

### 24 動態模糊｜Motion Blur

- **英文關鍵詞**：`motion blur` / `panning shot` / `slow shutter speed`
- **原理**：三種必須分開寫。(a) 主體移動 subject motion blur：機身固定（腳架），快門 1/15–1/4s，背景銳利、只有移動的四肢與衣料拖影；(b) 相機搖攝 panning：快門 1/30–1/8s，鏡頭以與主體相同角速度橫搖，主體軀幹清晰、背景被拉成水平線條；(c) 整體晃動 camera shake：手持 1/4–1s，全畫面同方向拖曳、無一處銳利。動態模糊與景深是兩條獨立的軸——為了壓住曝光，慢快門通常反而縮到 f/8–f/16，糊的是「動作」不是景深。日光下光靠縮光圈救不回來（ISO 100、f/16 的正確快門本來就是 1/100s 上下），要掛住 1/15s 以下必須加 ND8–ND32 減光鏡。
- **情緒**：速度、失控、混亂、時間流逝、暈眩、急迫
- **提示詞**：`panning shot at 1/15 second, camera swinging laterally at the same angular speed as the runner, torso and face sharp while the background stretches into horizontal streaks, trailing limbs smeared into arcs, ND filter holding f/11`
- **強化**：`48 閃光燈`、`37 弱光`、`圖二 13 港片霓虹`、`圖二 10 手持跟拍`
- **衝突**：`31 極端特寫`、`圖二 20 定格動畫質感`
- **常見錯誤**：只寫 "motion blur" 模型會把整張糊成一團；一定要指定「誰糊、誰清楚」加上具體秒數，panning 尤其要同時寫 subject sharp 與 background streaks，而且同一段裡不能再補 "smear throughout / everything blurred"，那句會把主體一起糊掉。

### 25 淺景深｜Shallow Depth of Field

- **英文關鍵詞**：`shallow depth of field` / `bokeh` / `f/1.4`
- **原理**：景深厚度只由光圈、焦段、對焦距離三者決定——f/1.2–f/2 配 85–135mm、拍攝距離 1.5–3m 時，景深只剩約 2–5cm，僅睫毛或虹膜落在焦平面上，耳朵已經脫焦。背景離主體多遠「不影響景深厚度」，只決定散景有多大顆：背景退到 5m 以外，點光源才會散成大顆圓形 bokeh ball；全開光圈時畫面邊緣還會出現 cat's eye 口徑蝕。它的功能是把人物從環境裡「切下來」，觀眾判讀不出地點，只能盯著主體。
- **情緒**：私密、抽離、夢境感、聚焦、柔軟、被凝視
- **提示詞**：`shallow depth of field at f/1.4, 85mm equivalent, focus plane on the near eye with lashes crisp while the ear already goes soft, background dissolved into large round bokeh balls from distant point lights, those balls squeezing into cat's eye shapes toward the frame edges`
- **強化**：`32 特寫`、`19 近景`、`11 自發光`、`圖二 13 港片霓虹`
- **衝突**：`22 深景深`、`21 遠景`、`圖二 07 單點透視對稱`
- **常見錯誤**：寫 "blurry background" 力道太弱，模型只給輕微虛化；要給出 f 值、對焦點（near eye）、背景光點形狀，並指明從哪個部位開始脫焦。

### 31 極端特寫｜Extreme Close-Up

- **英文關鍵詞**：`extreme close-up` / `ECU` / `macro detail shot`
- **原理**：只取五官或身體局部（單眼、雙唇、指尖、喉結），臉的輪廓被切出畫外，主體填滿 90–100% 畫幅；等效 100–135mm 微距、鏡頭距被攝體 0.2–0.4m、放大率約 1:3–1:1（0.33×–1×），此時即使收到 f/4 景深也只有數 mm，睫毛清晰而眼瞼已散。要讓一隻眼睛真的填滿畫面需要接近 1:1（100mm 微距約在 0.2m），退到 0.4m 只有 0.33×，畫面會連眉毛和鼻梁一起收進來。敘事功能是強迫觀眾盯著平常不會細看的細節，製造生理性的親密或不適，多用於情緒轉折與懸疑段落。
- **情緒**：侵入、緊張、脆弱、生理感、心理放大、無處迴避
- **提示詞**：`extreme close-up of a single eye filling the frame, 100mm macro at twenty centimeters, close to 1:1 magnification, iris fibres and individual lashes razor sharp, skin pores and moisture visible, eyelid already out of focus, face outline cropped away`
- **強化**：`25 淺景深`、`03 側光`、`09 柔光`、`46 高對比`
- **衝突**：`21 遠景`、`23 全身照`、`22 深景深`
- **常見錯誤**：寫 "close-up of the face" 只會得到頭肩照；ECU 必須指名「哪一個器官填滿畫面」並明說臉的邊界被裁掉，同時要求 macro 級的表面質感。

### 32 特寫｜Close-Up

- **英文關鍵詞**：`close-up` / `CU` / `head and shoulders shot`
- **原理**：切在鎖骨或肩線，頭頂只留 2–5% headroom（也可刻意切掉髮頂），臉佔畫幅高度 60–75%；等效 85–135mm、距離 1.2–1.9m（全片幅 3:2 基準：105mm 站 1.5m 臉剛好佔 2/3；同一支鏡頭壓到 1.2m 臉會漲到八成以上，變成大特寫）。讓臉不變形的是這個 1.2m 以上的工作距離而不是鏡頭本身——距離拉開，耳朵才不外擴、下顎線才收得乾淨，中長焦只是讓你在這個距離仍能切到鎖骨。敘事上它是電影裡情緒的預設容器，觀眾在這個距離讀微表情、視線方向與呼吸節奏，剪接上通常擔任一場戲的情緒句點。
- **情緒**：情緒直給、共感、專注、緊密、內心獨白
- **提示詞**：`close-up framed at the collarbone, 105mm equivalent from 1.5 meters, face occupying two thirds of the frame height, minimal headroom, eyes on the upper third line, skin texture retained, background reduced to a soft tone`
- **強化**：`25 淺景深`、`30 四分之三側面`、`09 柔光`、`35 居中構圖`
- **衝突**：`21 遠景`、`23 全身照`、`31 極端特寫`
- **常見錯誤**：headroom 留太多就退化成近景；要寫死 "minimal headroom, face fills two thirds of the frame"，並把眼睛放在上三分線，臉才會有特寫該有的壓迫感。

---

## 二、視角與構圖

**本組為兩條互相獨立、可自由交叉組合的軸：相機高度（軸 A）與被攝體朝向（軸 B）。寫提示詞時必須同時指定兩者，缺一模型就會自行漂移。同一軸內各檔本身就互斥（只能選一項），所以以下每條的「衝突」欄不重複列出同軸全部檔位，只列最容易誤配的鄰檔與跨軸的真衝突；不同軸的項目原則上可以自由疊加。**

**軸 A｜相機高度（決定權力關係）**：`33 鳥瞰`（向下 75–90°，近垂直）→ `17 高角度拍攝`（向下 15–45°）→ 眼平（0°，中性、平等、無立場）→ `39 低角度視角`（向上 15–45°）。向下 45–75° 與向上 45–75° 是兩檔之間的過渡帶，72 項中沒有對應編號，寫提示詞時直接寫死度數即可。俯視＝弱化／客體化／被觀察／渺小；平視＝平等對話；仰視＝英雄化／威嚴／壓迫／支配 —— 這是敘事慣例而非光學結果，可以刻意反用。`33 鳥瞰` 與 `17 高角度拍攝` 是同一軸的兩檔，不可並列使用（也不能互相「強化」）：前者近乎垂直、垂直維度塌陷、人物去人格化為色塊；後者只是略高於眼平，仍保留人物五官與環境透視。

**這一軸沒有安全的預設值。** 眼平不是「不寫就會拿到」的檔位——軸 A 沒有被指定，就是沒有被約束，模型會依畫面內容自行決定機位高低。要眼平就把兩件事一起寫死：高度基準（鏡頭對齊誰的視線）與光軸傾角（0°），並把最容易漂過去的相鄰檔位一併關掉，例如：`lens positioned at the subject's eye height, optical axis horizontal, zero downward or upward tilt`。`17 高角度拍攝`、`33 鳥瞰`，以及任何高於人身高的機位，都是**要用才寫**的選擇，不是省略時的落點。

**軸 B｜被攝體朝向（決定心理距離）**：正面 0°（正對鏡頭、全部溝通；72 項中沒有對應編號，是不寫就會得到的預設值）→ `30 四分之三側面` 30–45°（人像預設值）→ `26 斜側視角` 45–70°（開始疏離）→ `29 側面視角` 90°（完全失去眼神接觸）→ `28 背面視角` 180°（臉部消失、觀眾代入其視線）。角度越大，眼神接觸越少、心理距離越遠、觀眾從「被注視」轉為「注視者」。**朝向與光位是兩條不同的軸**：`27 正面光` 是光位（光從鏡頭方向來），不是朝向，不能拿來當這條軸的 0° 檔位，也不與側面／背面視角互斥 —— 它只會讓輪廓失去分離，那是打光品質問題，不是矛盾指令。

### 17 高角度拍攝｜High Angle Shot

- **英文關鍵詞**：`high angle shot` / `shot from above` / `downward camera angle`
- **原理**：相機置於被攝體眼平之上、鏡頭軸線向下傾 15–45°，透視使頭頂與肩線放大、下半身與腿部前縮（foreshortening）；傾角一旦大於鏡頭的垂直半視角（35mm 全片幅約 18°），地平線就被推出畫面上緣，地面取代天空成為背景 —— 傾角小於半視角時地平線仍留在畫面上部，這是同一技法的兩種樣貌。35–50mm 保留人物與環境的關係；85mm 以上壓縮透視，把人物壓成貼在地面上的塊面。
- **情緒**：弱化、被審視、無助、憐憫、客體化
- **提示詞**：`high angle shot, camera 30 degrees above the subject's eye level and tilted down, subject looking up into the lens, head and shoulders enlarged, legs foreshortened, ground filling the entire background, horizon above the top edge of the frame, 35mm`
- **強化**：`07 頂光`、`23 全身照`、`34 封閉構圖`、`22 深景深`
- **衝突**：`33 鳥瞰`、`39 低角度視角`
- **常見錯誤**：只寫 "from above"，模型會直接跳到接近垂直的俯拍。必須寫死 15–45° 的傾角、保留背景地面與人物向上的視線，才不會滑進 `33 鳥瞰`。另外別把 `13 底光` 當禁忌 —— 光位與相機高度是不同軸，俯拍配底光完全可行（恐怖片標準組合），只是情緒會從「弱化」翻成「威脅」，那是選擇不是錯誤。

### 26 斜側視角｜Oblique Side View

- **英文關鍵詞**：`oblique side view` / `near-profile view` / `subject turned 60 degrees off the lens axis`
- **原理**：臉部離鏡頭軸線旋轉 45–70°，遠側眼睛開始被鼻樑壓縮、可見面積變小但仍在；鼻尖逐步逼近遠側臉頰輪廓線，約 65–70° 會切上或越過它 —— 越過之後讀作「近側面（broken profile）」，那仍然不是 `29 側面視角` 的 90° 正側面。此區間兩眼還在，但眼神接觸已經破裂。近端五官離鏡頭較近而放大，建議 85mm 以上避免鼻部變形。
- **情緒**：疏離、若有所思、內省、非對抗、旁觀
- **提示詞**：`subject turned 60 degrees off the camera axis, far eye compressed by the nose bridge but still visible, nose tip almost touching the far cheek contour, gaze directed off-frame, shoulders turned further from the lens than the head, generous negative space on the side the face is turned toward, 85mm`
- **強化**：`03 側光`、`04 側逆光`、`25 淺景深`、`20 中景`
- **衝突**：`30 四分之三側面`、`35 居中構圖`、`圖二 08 平面正面構圖`
- **常見錯誤**：把 45–70° 寫成籠統的 "side angle"，模型多半退回安全的 30° 四分之三臉。也不要在關鍵詞裡寫 "45 degrees" —— 45° 正好是 `30 四分之三側面` 的上界，模型會直接給你 3/4 臉；寫 55–65° 最穩。要指定旋轉度數、描述遠眼被鼻樑壓掉的程度，並在朝向側預留 look room。

### 28 背面視角｜Rear View

- **英文關鍵詞**：`rear view` / `shot from behind` / `back turned to camera`
- **原理**：被攝體旋轉 180°，臉部完全不可見，觀眾失去表情資訊後改讀肩線、頸部角度與步態；人物的視線方向成為畫面的主要向量，背景升格為真正的敘事主體。後腦與背景的明度極易糊成一團，需要 `10 髮絲光`、`14 輪廓光` 這類來自後方的分離光把邊緣拉開。
- **情緒**：離去、孤獨、懸念、代入、拒絕溝通
- **提示詞**：`figure seen entirely from behind, only the back of the head and shoulders presented to the lens, face never visible, subject occupying the lower half of the frame with the environment opening out beyond, subject facing deep into the scene toward a distinct point, viewer eyeline following theirs, rim light separating head and shoulders from the darker background`
- **強化**：`05 背光`、`14 輪廓光`、`10 髮絲光`、`21 遠景`
- **衝突**：`30 四分之三側面`、`圖二 08 平面正面構圖`
- **常見錯誤**：只寫 "from behind"，模型會偷偷把頭轉回四分之三側臉露出下巴。必須正反兩面都寫 —— "only the back of the head presented to the lens, face never visible, head not turned toward camera" —— 並指定人物視線深入場景的方向與所望之物；沒有指定對象，模型會把背影擺在空無一物的背景前，敘事向量整個消失。

### 29 側面視角｜Profile View

- **英文關鍵詞**：`profile view` / `side profile` / `90-degree side view`
- **原理**：臉部旋轉 90°，只剩單眼可見，額頭、鼻樑、人中、雙唇、下巴連成一條抵著背景的連續輪廓線，因此背景的明度與雜訊決定成敗；眼神接觸歸零，臉從「表情」轉為「圖形」。此角度臉部平面幾乎與感光面平行，透視變形本來就最小 —— 85–135mm 的作用不在修正鼻形（正側面本來就不會被短鏡頭撐大），而在壓縮背景、讓輪廓線落在乾淨且明度分離的底子上。
- **情緒**：決絕、紀念碑感、儀式性、拒絕交流、標本化
- **提示詞**：`strict 90-degree profile, the nose pointing straight across the frame, single eye visible, forehead-nose-lips-chin forming one clean outline against an uncluttered background of contrasting brightness, ear fully visible, head not turned toward the lens, 100mm, separation light skimming the jawline`
- **強化**：`03 側光`、`14 輪廓光`、`05 背光`、`42 暗色調`
- **衝突**：`30 四分之三側面`、`35 居中構圖`、`圖二 08 平面正面構圖`
- **常見錯誤**：寫了 profile 卻沒處理輪廓線後面的背景，臉的邊緣與雜亂背景糊成一團。務必指定與膚色明度拉開的乾淨背景，或沿下顎的分離光，並註明「不要回頭看鏡頭」以免模型折衷成 70°。

### 30 四分之三側面｜Three-Quarter View

- **英文關鍵詞**：`three-quarter view` / `3/4 portrait angle` / `head turned 35 degrees from the lens`
- **原理**：臉部旋轉 30–45°，兩眼都完整可見（遠眼尚未被鼻樑吃掉），近鏡頭的廣邊頰與轉開的短邊頰形成明暗交界而產生體積感。把主光放在臉轉過去的那一側（短邊，即 short lighting）、水平 45°、仰角 45°，鼻影會與頰影接合，在**近鏡頭側的陰影頰**上圍出一塊寬不過眼、長不過鼻的倒三角亮區 —— 這才是 Rembrandt 三角（它永遠出現在陰影側，不是被打亮的遠頰）；主光若改放廣邊就成了 broad lighting，臉會被拉寬、體積感下降。這是最省事地同時保有立體感與眼神接觸的角度（0° 正面也有眼神接觸，只是少了兩頰明暗差容易扁平），因此成為人像預設值；85mm、f/1.8–2.8、鏡頭到人 1.5–2.5m 為標準組合。
- **情緒**：親近但不侵略、可信、立體、經典肖像感
- **提示詞**：`three-quarter view, head turned 35 degrees from the lens with both eyes fully visible, key light 45 degrees horizontally and 45 degrees above on the side the face is turned toward, a small triangle of light on the shadowed near cheek no wider than the eye, shoulders turned 15 degrees further from the lens than the head, 85mm at f/2`
- **強化**：`03 側光`、`09 柔光`、`25 淺景深`、`32 特寫`
- **衝突**：`29 側面視角`、`26 斜側視角`、`33 鳥瞰`、`圖二 08 平面正面構圖`
- **常見錯誤**：只寫 "three-quarter view" 而不鎖角度，模型常漂到 55–65°、遠眼被鼻子吃掉，實際上掉進 `26 斜側視角`，體積感反而下降。要寫死 30–45°（35° 最安全）並明確要求 "both eyes fully visible"；肩線可比臉再多轉 10–15° 增加縱深。

### 33 鳥瞰｜Bird's-Eye View

- **英文關鍵詞**：`bird's-eye view` / `top-down overhead shot` / `directly overhead`
- **原理**：相機拉高到向下 75–90°，真正 90° 時垂直維度完全塌陷，人物只剩頭頂與肩膀的塊狀剪影，地面紋理升格為平面圖案；世界中的垂直線此時平行於鏡頭軸，透視收斂到鏡頭正下方的單一消失點（天底點），畫面內不存在地平線。地面與感光面平行、面上各點到鏡頭幾乎等距，景深因此失去分離主體的能力，光圈只剩曝光作用。廣角 16–24mm 用於涵蓋範圍，長焦自高處拍則壓縮成純圖形。
- **情緒**：抽離、神視角、命運感、渺小、幾何秩序、去人格
- **提示詞**：`bird's-eye view, camera directly overhead at 90 degrees with the lens perpendicular to the floor, figures reduced to heads and shoulders, ground pattern reading as flat graphic geometry, floor filling the entire frame with no horizon anywhere, 24mm`
- **強化**：`07 頂光`、`21 遠景`、`35 居中構圖`、`22 深景深`
- **衝突**：`17 高角度拍攝`、`39 低角度視角`、`30 四分之三側面`、`25 淺景深`
- **常見錯誤**：把 bird's-eye 當成「高一點的俯拍」，結果只得到 30° 的 `17 高角度拍攝`。必須寫 "directly overhead, 90 degrees, lens perpendicular to the floor, no horizon in frame" 並描述地面圖案，模型才會真的把鏡頭拉到垂直。另外注意：影子長短由**光源仰角**決定，跟相機在哪無關 —— 想要腳下那圈短影子，得另外指定 `07 頂光`；只寫 "shadows directly beneath" 而不給光位，模型只會隨機挑一個時間。

### 34 封閉構圖｜Closed Framing

- **英文關鍵詞**：`closed framing` / `closed form composition` / `frame within a frame`
- **原理**：所有敘事資訊都被容納在畫框內，主體完整不被邊緣切割，畫外空間不被暗示。注意 closed framing（電影理論的 closed form）是**概念**，frame within a frame（門框、窗框、拱門、鏡框、走廊在畫面內再造一層二次框）是執行它最常用的**手法**，兩者不是同義詞：只餵概念模型不會執行，必須寫出實體的二次框。前景暗部通常吃掉外緣 20–40%，配合鎖死的固定機位與 f/8–f/16 深景深，讓整個被封閉的空間都清楚可讀。相對的開放構圖（open framing / open form）讓主體被邊緣切斷、視線與動作指向畫外，暗示一個比畫框更大的世界；封閉構圖則宣告「這裡就是全部」，因而產生禁錮與窺視感。
- **情緒**：禁錮、窺視、宿命、秩序、被觀察、劇場感
- **提示詞**：`subject fully enclosed inside a doorway acting as a second frame, dark foreground architecture masking the outer 30 percent of the edges, every frame edge closed off by wall or architecture, the whole body inside the opening with margin on all four sides, static locked-off camera, 35mm at f/11 deep focus`
- **強化**：`35 居中構圖`、`22 深景深`、`42 暗色調`、`圖二 07 單點透視對稱`
- **衝突**：`31 極端特寫`、`圖二 10 手持跟拍`、`圖二 19 偽紀錄片`
- **常見錯誤**：只寫 "closed composition" 這種抽象術語，模型無從執行。必須指名做二次框的實體物件（doorway / window frame / archway / mirror）、它壓住畫面邊緣的比例，以及主體四周留白這一條。「主體不被切割」要用正面敘述寫（"the whole body inside the opening with margin on all four sides"），只寫 "nothing cropped" 這類否定句，模型常常直接忽略。

### 35 居中構圖｜Centered Composition

- **英文關鍵詞**：`centered composition` / `symmetrical framing` / `subject dead center`
- **原理**：主體垂直軸壓在畫面中線上，刻意違反三分法；三分法讓視線在畫面內遊走，居中則讓視線停住，於是產生正式感、對稱感與正面直視的對峙感。與單點透視（消失點落在畫面正中）及對稱背景疊加時效果最強。缺點是消滅了 lead room／nose room（視線前方的留白），因此人物明顯側轉、行進或視線離軸時不該用 —— 那會讓畫面像撞牆。分界在旋轉約 45°：`30 四分之三側面`（30–45°）只要眼睛回看鏡頭仍可居中，`26 斜側視角`、`29 側面視角` 就必須改成偏置並留 look room；動態場面、追蹤鏡頭、以及需要暗示畫外的敘事同樣應改用偏置構圖。
- **情緒**：正式、對峙、莊嚴、直視、儀式、不安的秩序
- **提示詞**：`subject dead center on the vertical axis, symmetrical background aligned to the frame edges, vanishing point at the exact center of the frame, subject facing the lens straight on, equal negative space on the left and the right`
- **強化**：`圖二 07 單點透視對稱`、`圖二 08 平面正面構圖`、`34 封閉構圖`、`33 鳥瞰`
- **衝突**：`26 斜側視角`、`29 側面視角`、`24 動態模糊`
- **常見錯誤**：把居中當成萬用預設，套在明顯側身或移動中的人物上，導致朝向側沒有空間、構圖窒息。居中只用於靜止、正對鏡頭或背景本身對稱的場景；一旦人物旋轉超過 45°，改把主體推離中線並留出 look room。

### 39 低角度視角｜Low Angle Shot

- **英文關鍵詞**：`low angle shot` / `shot from below` / `camera below eye level tilted up`
- **原理**：相機降到眼平之下、向上傾 15–45°（極端者鏡頭離地 20–40cm），垂直線因透視向畫面上方收斂，下顎與胸廓因為離鏡頭最近而被放大、頭頂相對縮小，天空或天花板成為主體背後的乾淨負空間；24–35mm 廣角會把收斂與體積放大效果推到最強。再往上推到接近垂直（向上 75–90°）是 worm's-eye view —— 那是這條軸的極端檔位、與 `33 鳥瞰` 對稱，不是 low angle 的同義詞。
- **情緒**：威嚴、壓迫、英雄化、支配、崇拜、不安
- **提示詞**：`low angle shot, lens 40cm above the floor tilted 30 degrees upward, verticals converging toward the top of the frame, jaw and chest enlarged by perspective with the crown of the head smaller, ceiling or open sky as a clean backdrop, subject towering over the viewer, 24mm`
- **強化**：`13 底光`、`15 舞台光`、`46 高對比`、`22 深景深`
- **衝突**：`17 高角度拍攝`、`33 鳥瞰`
- **常見錯誤**：只寫 "low angle"，模型往往只把鏡頭降到胸口高度，壓迫感完全不成立。要同時給出鏡頭離地高度、向上傾角，並明確要求 "converging verticals" 與背後的天空／天花板，才會真的仰視。反過來，隨手寫 "worm's-eye view" 會讓模型直接跳到近乎垂直的極端仰角 —— 那是另一檔，不要拿它當 low angle 的同義詞。

---

## 第 10 軸：鏡頭（焦距、畫幅比例、鏡頭瑕疵）

前九軸決定「畫面裡有什麼、被怎麼照亮」，第 10 軸決定「這些東西被什麼光學系統看見、裝進什麼形狀的容器」。

**先釐清一件會讓人誤讀的事：編號與排序不是同一回事。** 鏡頭是第 10 個被加進技法庫的軸（所以叫第 10 軸），但在組裝順序上它拆成**第 2 位**與**最尾端**兩個位置 —— 以 SKILL.md 與 `05-recipes.md` 的固定順序為準：

```
主體 → 景別 → 鏡頭焦距 → 視角/朝向 → 光位 → 光質 → 光源與色溫
     → 影調與對比 → 色彩 → 景深（光圈） → 質感/載體 → 風格總結 → 畫幅
```

兩個**必填**槽位：

- **焦距＋拍攝距離**：緊接景別寫，格式固定為「焦距 + 機位距離」（例：`85mm equivalent from two meters`）。**光圈不寫在這裡**，光圈留在第 9 槽景深。缺焦距，模型會自己挑，且在特寫時系統性地挑錯。
- **畫幅比例**：寫在整句最尾端（風格總結之後），或直接填平台的比例參數欄位。缺畫幅就是吃平台預設值（多數圖像模型是 1:1，多數影片模型是 16:9），「電影感」再怎麼堆都不會出現 —— 見 SKILL.md 硬規則 8。

第三個槽位（**鏡頭瑕疵**）是選配，掛在第 10 槽質感/載體，並與 `07-beyond-the-charts.md`〈1-3 成像瑕疵組〉**共用同一份「全篇瑕疵片語上限 3 個」的額度**。

**這三者都不佔技法上限 8 項的名額**（硬規則 4）：焦距與畫幅是必填參數而不是技法，鏡頭瑕疵受它自己的片語上限管。

要電影感的優先順序（與 SKILL.md 硬規則 11 一致）：**先服從使用者或交付版位指定的畫幅；未指定時才預設 2.39:1 → 再給一個時段＋一個天氣 → 才輪到鏡頭瑕疵 → 最後才考慮風格包。**

---

### 焦距對照表

以下皆為**全片幅（135 格式）等效焦距**。

| 等效焦距 | 英文提示詞片語 | 透視特性（畸變行為／背景壓縮） | 建議搭配景別（含機位距離） | 典型用途 |
|---|---|---|---|---|
| 14–24mm | `18mm ultra wide angle lens, exaggerated near-to-far scale difference, whatever sits nearest the lens rendered much larger, objects near the corners stretched outward, background small and far back` | 畸變最強，但成因是「必須靠得很近」：離鏡頭最近的物體被放大、遠處急速縮小。直線在直線校正鏡下仍是直的（邊緣只有輕微桶狀彎曲），真正被扯的是**立體體積**——落在四角的臉會沿對角方向被拉長。同樣主體大小下，背景相對放大率最低，看起來最小最遠 | `21 遠景`（機位 10m 以上） | establishing shot、建築內部、風景、把環境當主角、`39 低角度視角`（收斂垂直線由仰角造成，廣角只是讓它明顯） |
| 24–35mm | `28mm wide angle lens, natural separation between foreground and background, mild corner stretching, the environment reading large around the subject` | 廣角但可控：機位 1m 內仍明顯撐大最靠近鏡頭的部位，退到 2m 外接近自然。同樣主體大小下背景比 50mm 更小更遠 | `21 遠景`、`23 全身照`（3m 以上）、`20 中景`（環境敘事） | 環境人像、紀實手持、`22 深景深`、`34 封閉構圖`、`33 鳥瞰`（求涵蓋範圍） |
| 35mm | `35mm reportage lens from two meters, near-natural facial proportions, background still legible with readable detail` | 略寬於 50mm 標準視角；機位 2m 外五官比例正常，1m 內鼻子仍會被撐大。背景相對放大率略低於 50mm，背景保有可讀細節 | `20 中景`（1.5–2.2m）、`23 全身照`（3m 以上） | 街拍、紀錄片、雙人 two-shot、需要同時看清人與地點時 |
| 50mm | `50mm standard lens from two meters, neutral perspective with neither noticeable compression nor stretching` | 中性基準線。在 1.5m 以上的正常拍攝距離下，前後景關係最接近肉眼所見。注意它**不是「和人眼視野一樣寬」**（人眼實際視野遠寬於此），接近的是**透視關係**，不是視角大小 | `20 中景`（1.6m）、`23 全身照`（4m） | 不確定時的預設值 —— 但只在 `20 中景`／`23 全身照` 成立；景別一旦進到 `32 特寫` 就必須換掉（見硬規則） |
| 85mm | `85mm portrait lens from two meters, compressed background, undistorted facial proportions` | 開始壓縮：**在同樣主體大小的前提下**，背景元素的成像放大率約為 50mm 的 1.7 倍（85÷50），背景看起來更近更大、納進來的範圍更窄。機位 2m 時鼻與耳的成像放大率只差約 6%，臉頰不外擴、下顎線收得乾淨 | `32 特寫`（1.2–1.5m）、`19 近景`（1.8–2.5m） | 人像預設焦段、`30 四分之三側面`、`25 淺景深` |
| 100mm macro | `100mm macro lens at twenty centimeters, close to 1:1 magnification, depth of field only a few millimetres even stopped down` | 高放大率下景深塌縮到公釐級（1:1、f/8 約 1mm）。**這個距離的透視其實極強而不是消失**：主體看起來扁平，是因為焦平面外的一切立刻糊掉，不是因為前後差異變小。同一個原因也讓 20cm 這種距離絕對不能拿來拍整張臉 | `31 極端特寫`（0.2–0.4m） | 眼睛、指尖、水珠、食物、材質表面、商品細節 |
| 135mm | `135mm telephoto lens, strong background compression, only a narrow slice of background inside the frame` | 強壓縮：背景元素被放大、納進畫面的範圍變窄。**背景「沒有細節」是大光圈造成的，不是壓縮造成的**——壓縮只讓背景變大變近，要化成一片色牆仍得靠 f/2 以下。臉部零畸變 | `32 特寫`（1.9m）、`19 近景`（2.5–3m）、`23 全身照`（10m 以上） | 時尚全身、舞台、隔著距離拍的情緒特寫 |
| 200mm | `200mm long telephoto lens, distant planes stacked flat against one another, the subject lifted out of the crowd by compression` | 極端壓縮：前中後景層層貼平、縱深感消失。對角視角只剩約 12°，機身角度只要動一點點構圖就整個換掉，手震也被同比例放大 | `32 特寫`、`21 遠景`（僅限刻意的壓縮式遠景，見下方硬規則第 2 條） | 體育、野生動物、街頭遠距離抓拍、把單一人物從人群裡壓出來 |

**為什麼廣角近攝會讓臉變形 —— 成因是拍攝距離，不是焦距本身。**

透視只由「相機到被攝體各點的距離比」決定。人臉的鼻尖比耳朵約近 12cm：機位在 0.5m 時，鼻在 0.5m、耳在 0.62m，比值 1:1.24 —— 鼻子的成像比耳朵大 24%，於是鼻子放大、臉頰往內縮、耳朵縮小、下巴後退，這就是使用者說的「臉怪怪的」。退到 2m，比值變成 1:1.06，只差 6%，肉眼判讀為正常。這與 `32 特寫`、`29 側面視角` 兩條的原理段講的是同一件事。

焦距在這裡的角色只是**決定你要切到某個景別必須站多遠**：24mm 想切到頭肩就得貼到 0.4m（必然變形），85mm 站在 1.2–1.5m 外就能切到鎖骨（不變形）。所以修正變形的動作不是「換一支不會變形的鏡頭」，而是**退後，再用長鏡頭把景別切回來**。

實務上還有一條：生成模型不做光學運算，它是在「被標成這個 token 的影像」分布裡取樣。`85mm` 之所以有效，是因為訓練資料裡標成 85mm 的照片多半本來就是 1.5–2m 外拍的。因此**焦距與距離必須互相一致**——同時寫 `85mm` 和 `camera very close to the face`，模型多半跟著距離走而不是跟著焦距走，你還是會拿到變形臉。

**景深由光圈、焦距、對焦距離三者共同決定，缺一不可推。** 下列數字以全片幅、彌散圓 0.03mm 計；換一套判準絕對值會變，但倍數關係不變：

- 同樣 f/1.4、同樣對焦在 2m：85mm 的景深約 4.5cm（只有睫毛在焦內），35mm 約 27cm（整顆頭連衣領都清楚）—— 差約六倍。
- 反過來，85mm 收到 f/11、仍對在 2m，景深也只有約 35cm，根本構不成 deep focus；deep focus 只能靠廣角換來（見硬規則第 7 條）。
- 背景離主體多遠**不改變景深厚度**，只決定散景顆粒有多大（見 `25 淺景深`）。

---

### 焦距硬規則

1. **`31 極端特寫` 一律 100mm macro（機位 0.2–0.4m）；`32 特寫` 一律 85–135mm（機位 1.2–1.9m）。** 不照做：模型預設用廣角近攝，交出鼻子放大、臉頰內縮、耳朵縮小的變形臉，而使用者只會回報「臉怪怪的」，說不出哪裡錯。
2. **`21 遠景` 配 16–35mm，預設 24mm、機位 10m 以上。** 唯一例外是刻意的壓縮式遠景（層疊山脊、熱浪中的城市天際線），那要明寫 `200mm` 並放棄前景細節。不照做：用長焦拍一般遠景會把天、地、人壓成貼在一起的平面，空間感與規模感全部消失，看起來像望遠鏡截圖而不是 establishing shot。
3. **`23 全身照` 配 35–50mm（機位 3–4.2m）或 85–135mm（機位 7–11m），絕不配 24mm。** 不照做：24mm 拍全身要站進 2m 內，機位在頭高就頭大腳小，機位放低就下肢被異常拉長。
4. **`25 淺景深` 必須同時給焦距與光圈**，寫成 `85mm at f/1.8 focused at two meters`。不照做：只寫 `f/1.8`，模型可能配上 35mm —— 35mm f/1.8 對在 2m 的景深有 30cm 以上，背景照樣讀得出來，使用者回報「散不開」。
5. **廣角＋人像特寫是錯誤組合，不要寫。** `24mm close-up portrait`、`wide angle beauty shot` 這類寫法模型會忠實照做，直接產出變形臉。真的要變形（喜劇、恐怖、自拍質感）就明寫 `deliberate wide-angle facial distortion, lens thirty centimetres from the nose`，把它變成刻意的選擇而不是意外。
6. **焦距與拍攝距離一起寫，不要只給焦距。** 不照做：只寫 `85mm`，模型仍可能把機位貼到 0.6m，變形照樣發生——描述距離的詞權重高於焦距標籤。
7. **`22 深景深` 配 18–35mm + f/8–f/11 + 對在超焦距**（28mm f/11 的超焦距約 2.4m，對在那裡則 1.2m 到無限遠都清楚）。不照做：85mm 就算收到 f/11，2m 處景深也只有約 35cm，前中後三層同時清晰不可能成立。
8. **`39 低角度視角` 配 24–35mm。** 成因要搞清楚：收斂垂直線是**仰角**造成的，不是廣角造成的；廣角的作用是讓收斂在畫面裡佔滿而看得見。不照做：改用 85mm 仰拍，你必須退到很遠，垂直線的收斂在窄視角裡小到看不出來，下顎與胸廓也不會被放大，壓迫感與英雄化效果歸零，只剩「從下面拍的一張普通照片」。
9. **`33 鳥瞰` 只有兩個檔位：24mm 以下（求涵蓋、保留空間感）或 135mm 以上（從高處拍成純平面圖案）。** 不照做：50mm 俯拍兩頭不到岸——既涵蓋不夠廣，也壓縮不成圖形。
10. **每張圖只給一個焦距值**（同 `05-recipes.md`「每個槽只寫一個值」）。不照做：同槽出現兩個焦距（`35mm, 85mm portrait`）互相抵銷，模型會取一個中間的隨機值，構圖與畸變都不受控。

---

### 畫幅比例（必填）

| 比例 | 何時用 | 觀感 | 常見平台 |
|---|---|---|---|
| 1:1 | 商品主圖、頭像、不確定會被怎麼裁切而必須四邊都安全時 | 靜止、置中、無方向性；橫向空間被切光，天生帶目錄感。**做不出電影感** | 電商主圖、IG 網格縮圖、Podcast／專輯封面、大頭貼 |
| 4:5 | 直式社群人像，要把人放到最大 | 把主體放大、把左右環境切掉，親近、雜誌內頁感 | IG 直式貼文（feed 最大直式版位）、Facebook 直式廣告 |
| 3:2 | 一般攝影輸出，沒有特殊戲劇訴求時的中性選擇 | 中性「照片感」，不做任何風格宣示 | 135 相機原生比例、圖庫、部落格首圖、4×6 沖印 |
| 16:9 | 影片預設、網頁 hero、簡報 | 橫向、資訊性、螢幕感；寬，但讀起來是電視不是電影 | YouTube、簡報、網站 banner、多數影片模型的預設值 |
| 2.39:1 | 目標有「電影感」且使用者未指定其他畫幅或交付版位 | 最強電影訊號；強制橫向構圖與大量負空間 | 劇情長片、廣告、電影感短片、視覺 key art |
| 9:16 | 手機全螢幕、短影音 | 沉浸、貼身、當下感；橫向資訊全部被犧牲 | Reels、Stories、TikTok、Shorts |
| 1.85:1 | 要電影感、但主體必須站直入鏡（`23 全身照`、高聳建築、直立人物） | 電影感但保留縱向呼吸空間，比 2.39:1 溫和；橫向負空間少一半 | 院線片與串流影集的另一個標準寬幅；需要人物站滿畫面高度的固定機位長鏡頭（`圖二 09 固定長鏡頭`） |
| 1.66:1 / 1.78:1 | Super 16 紀錄片質感 | 介於方正與當代寬幅之間，保留環境又不像電視畫面 | `圖二 18 十六毫米顆粒`（1.66:1 原生，或裁成 1.78:1） |
| 4:3 | 復古、標準 16mm、家庭錄影帶質感，或中片幅人像 | 方正、懷舊、非當代；縱向空間充足，人像不擁擠 | `圖二 14 數位早期`、`圖二 17 VHS 錄影帶`、`圖二 16 黑白默片`（默片時代的 1.33:1）、標準 16mm、中片幅時尚、舊電視素材 |

**使用者明確指定的畫幅或交付版位永遠優先。未指定時，2.39:1 才是最便宜的電影感來源，並優先於任何風格包。**

先給畫幅，再考慮要不要加 `圖二 01`–`圖二 24` 的任何一包。原因是：風格包換的是顏色、顆粒與影調，它**換不掉構圖幾何**；而「電影感」被辨識出來的機制主要就是構圖幾何。

同樣寬度下，2.39:1 的畫面高度只有 16:9 的 74%（1.778 ÷ 2.39）。這個約束會**自動**收窄構圖的可能性，不需要你再多寫任何一個形容詞：

1. 站立的人一旦填滿畫面高度，左右就空出大量寬度必須交代 —— 環境非進來不可；反之若讓環境退場，人就只能縮小。兩條路都通向「人比 16:9 小、環境比 16:9 多」。
2. 主體無法同時填滿寬與高，橫向必然出現大片負空間：置中是兩側對稱的大留白，偏置是單側留白 —— 兩者都是電影構圖的常見語彙，都不是社群貼文的樣子。
3. 地平線放在正中會把畫面切成兩條扁帶，視覺上幾乎無法成立，因此實務上一律壓到上或下三分之一。
4. 兩個人並置時左右間距被拉開，自動形成對峙或疏離的關係，不必另外寫。

這四件事就是觀眾在辨認的「電影感」。反過來說，在 1:1 或 4:5 裡堆再多 `cinematic`、再精緻的調色，觀眾第一眼讀到的仍然是社群貼文 —— 因為幾何不對。

**警告：2.39:1 不等於在 16:9 上加黑邊。** 不要寫 `black bars top and bottom` 或 `letterbox`，模型會把黑條當成畫面內容畫進去，主體仍然按 16:9 構圖，你得到的是一張中間縮水的假寬幅，上面四件幾何約束一件都沒發生（這也是 `06-analysis.md`〈要有電影感〉那條列出的常見誤解）。要改的是輸出比例本身。

**唯一例外：比例已經確認、但輸出容器表達不了它時，遮幅可以寫成畫面內容。** 在既有容器內要求上下（或左右）遮幅，並寫明遮幅是**畫進畫面的東西**：`the image letterboxed inside the frame with solid black bars top and bottom, the picture area filling the central band`。三個前提，缺一不可：

1. 該比例是使用者或已選定 surface **確認過的**，不是為了「電影感」自行決定的——`SKILL.md` 硬規則 8 不變，上一段的警告在所有其他情況下照常成立。
2. 說明裡要講清楚這是**畫面內容而不是輸出參數**：交付、後製裁切與再利用的處理方式完全不同，把它當成參數會在下游出錯。
3. 遮幅會吃掉可用畫幅，**構圖要按遮幅後的畫面配置**，不是按容器配置；景別與切點跟著遮幅後的高度重算——上一段講的假寬幅，失敗點正是在這裡。

**畫幅寫在哪：句尾或參數區，絕不塞在中間。**

- **有比例參數的平台一律走參數。** Higgsfield 的 `generate_image` / `generate_video` 走 `params.aspect_ratio`（各模型支援的比例值不同，先用 `models_explore` 查該模型的 `aspect_ratios` 清單）；Midjourney 走 `--ar`（`--ar 21:9` ≈ 2.33:1 最穩；能否精確吃到 `--ar 239:100` 依版本而異，不確定就用 `21:9`）。**走參數時提示詞裡不要再重複寫比例數字**，重複只會讓模型把它當畫面內容處理。各平台的實際欄位名與寫法以 `09-model-dialects.md` 為準，且會隨版本改動 —— 送出前先確認當前文件，不要憑記憶填欄位名。
- **只有沒有比例參數的純文字輸入框才寫進句子**，放在整句最後一個逗號之後、後面不再接任何畫面內容：`2.39:1 widescreen framing`、`vertical 9:16 framing`。
- **為什麼不能寫中間**：畫幅是容器不是內容。夾在主體與光線描述之間，模型會把它當成畫面裡的一個物件去詮釋 —— 常見結果是憑空生出一台寬螢幕電視、一條被畫進去的黑邊，或一個寬幅的畫框道具（同 SKILL.md 步驟 0：把 Midjourney 參數餵給純文字模型會被當成字面文字畫進圖裡）。

---

### 鏡頭瑕疵詞庫

- `anamorphic lens flare, a horizontal blue streak stretching out from the brightest point source` — 畫面裡有實體點光源（車頭燈、霓虹、練習燈、路燈）、而且已經給了寬幅比例時用。會從光源橫拉一條藍色水平光條。畫面裡沒有點光源時不要寫，模型會硬生出一條浮在空中、沒有來源的藍線。
- `halation blooming around the brightest highlights` — 高光落在暗背景上時用（夜間霓虹、暗室裡的窗光、燭火、`11 自發光`）。亮部邊緣暈開一圈紅橘光暈，這是「底片感」最主要的來源，比顆粒有效。畫面裡沒有接近過曝的亮點時寫了無效。與 `07-beyond-the-charts.md` 的 `slight halation on highlights` 是同一項，兩句只能擇一。
- `natural vignetting, the corners falling about half a stop darker` — 想把視線壓回中心，或要老鏡頭／偷拍／檔案影像感時用。**一定要寫級數**（半級是預設值，要更明顯就寫 `one stop`）；只寫 `vignetting` 會拿到後製硬黑框那種重口暗角，把構圖吃掉。與 07-beyond 的 `corner vignetting about half a stop down` 是同一項。
- `corner illumination matching the centre, no darkening toward the frame edges` — 明確**不要**暗角時用。四角與中心的亮度關係是要裁決的一項，兩個方向都要寫得出來：不明講，這個落差就是一個未指定的值，會隨每次重生變動。寫法上**先正面陳述目標狀態，再補否定**——只寫 `no vignette` 是純否定，模型沒有拿到要收斂到哪裡；把「四角與中心等亮」講出來，才是把這個關係從未指定變成被指定（同 `SKILL.md` 硬規則 15）。與上一條 `natural vignetting` 是同一項的兩個方向，只能擇一；也不要與下面的 `soft corners falling off from a critically sharp centre` 同寫，那一項本身就預設四角會掉。載體型風格包若已指定四角行為，照風格包走（見 `04-film-styles.md`），不要在外面再補一句。這一條是**取消**瑕疵而不是加入瑕疵，不佔下面「一次最多 2 個」的名額。
- `cat's eye bokeh toward the frame edges, swirly background rendering` — 只在同時有 `25 淺景深`、光圈接近全開、且背景有點光源時用。畫面邊緣的圓形散景被口徑蝕擠成貓眼形，整片背景因此讀起來像在旋轉（漩渦感是貓眼散景沿邊緣排列的結果，不是另一種獨立現象）。深景深或背景乾淨無點光源時寫了完全不會出現。
- `mild chromatic aberration at the frame edges` — 高反差邊界（逆光樹枝、金屬邊緣、`05 背光`、`04 側逆光`）想去掉數位太乾淨的塑膠感時用。畫面**邊緣**出現細細的紫綠色邊（橫向色差只發生在邊緣，寫在中央不成立）。**必須保留 `mild`**，不加限定詞模型會把整張圖所有邊緣都染上彩虹邊，看起來像壞掉的螢幕。
- `soft corners falling off from a critically sharp centre` — 復古鏡頭、大光圈開放質感、`圖二 18 十六毫米顆粒`／`圖二 14 數位早期` 時用。中心銳利、四角解析度下降，畫面有實體鏡頭的性格。**不要與 `22 深景深` 同寫**：嚴格說兩者不是同一件事（景深講的是縱深範圍，邊角鬆講的是離軸解像力），但同時餵進去模型只會取平均，交出一張整體偏軟的圖，deep focus 要的三層清晰就毀了。
- `slight lens breathing as focus shifts` — **只用於影片**，尤其是有跟焦或變焦的鏡頭、`圖二 10 手持跟拍`、`圖二 19 偽紀錄片`。對焦變化時視角微幅縮放，讓焦點移動看起來像真的機械鏡頭而不是數位裁切。放進靜態圖是空詞，只浪費 token（影片專屬項目見 `08-motion.md`）。
- `veiling flare lifting the blacks in the lower left corner where the source clips the barrel` — 光源在畫面內或剛好在畫框外時用（`05 背光`、`04 側逆光`、`12 火光`）。**要指定是哪一角或哪一側，不要寫成全畫面 flare。** 靠近光源那一側的黑位被整體抬起、對比下降，是最像「真的有光打進鏡頭」的訊號。它會直接摧毀黑位，別跟 `46 高對比`、`42 暗色調` 同寫。
- `dust and hairline scratches on the front element catching the light` — 要「這支鏡頭被用了很多年」的紀錄片、檔案、末世感時用。強逆光下前玉的灰塵與細刮痕會亮起來成為一層細絲。**只在有強逆光時才成立**，順光或柔光場景寫了等於沒寫。注意這一項髒的是**鏡頭**，與 07-beyond 的 `a hair and two dust specks on the negative`（髒在**底片**上、數位載體不可用）是兩件事，不要同寫。

**警告：鏡頭瑕疵一次最多用 2 個**，而且與 `07-beyond-the-charts.md`〈1-3 成像瑕疵組〉**共用「全篇瑕疵片語上限 3 個」的額度** —— 本節挑滿 2 個，成像瑕疵組最多再補 1 個。每個瑕疵詞都在搶同一批像素（高光、邊緣、四角），三個以上疊在一起，模型會把它們同時全開，交出一張又霧、又髒、又有彩邊、又橫著一條藍線的圖 —— 那讀起來不是電影，是壞掉的截圖。

挑法固定為 **一個全域的 ＋ 一個局部的**：

- **全域**（改變整張圖的亮度分布或對比）：`natural vignetting`、`veiling flare`、`soft corners`
- **局部**（只作用在特定元素上）：`anamorphic lens flare`、`halation`、`cat's eye bokeh`、`mild chromatic aberration`、`dust and hairline scratches`

不要兩個全域（整張圖一起變糊變霧）或兩個局部（同一批高光與邊緣被兩種效果互搶）。

另外，選了 `圖二 11 三色印片`、`圖二 12 柯達克羅姆`、`圖二 14 數位早期`、`圖二 17 VHS 錄影帶`、`圖二 18 十六毫米顆粒`、`圖二 20 定格動畫質感` 這六個載體風格包時，顆粒與成像特徵已內含在風格包裡，本節只保留風格包沒有指定的項目（同 07-beyond 的排他規則）。

---

## 構圖補充 10 項

以下十項是疊在九軸之上的**構圖層**：九軸決定「拍到什麼」，這一層決定「東西擺在畫框的哪裡」。它不新增軸位，因此**不另佔 `SKILL.md` 硬規則 4 的 8 項名額**（它描述的是既有景別／視角軸在畫框內的落點）；但**同一張圖最多用 3 項**，超過就開始與主體描述搶指令權重。

寫入位置：接在 `07-beyond-the-charts.md`〈零〉的擴充順序中「視角/朝向」之後、「天氣」之前。以下每條的**提示詞**都是**片語**，不是完整提示詞——畫幅仍照硬規則 8 另外寫在句尾（唯一例外是多人構圖的 two-shot，那裡畫幅直接決定切點，見下一節）。

**本層真正的硬互斥（其餘各項可自由疊加）**

| 互斥對 | 原因 |
|---|---|
| 三分法 ↔ `35 居中構圖` | 同一個主體位置只能選一個 |
| 三分法 ↔ `圖二 07 單點透視對稱`、`圖二 08 平面正面構圖` | 這兩個風格包鎖死居中對稱，三分法自動失效 |
| 傾斜畫框（Dutch roll）↔ `圖二 07`、`圖二 08` | 兩者的條目都明文要求零旋轉、機位與牆面垂直 |
| 三層景深 ↔ `33 鳥瞰` | 地面與感光面平行，縱深維度塌陷，沒有三層可分 |
| 地平線高度 ↔ `33 鳥瞰` | 該條目明文「畫面內不存在地平線」 |
| 引導線 ↔ `32 特寫`、`31 極端特寫` | 畫框內容不下足夠長度的線 |
| 負空間 ↔ `07-beyond-the-charts.md` 3-1 三個物件規則 | 一個要空、一個要三件道具；選了負空間就把環境物件降到 0–1 個 |

---

#### 三層景深｜Three-Plane Staging　**（在構圖層裡優先於任何風格包）**

- **是什麼**：在畫框裡明確安排前景／中景（主體）／背景三個可辨識的縱深層，前景元素通常刻意失焦並壓住畫框一角或一側。
- **為什麼一個失焦前景就能製造電影感**：它一次宣告兩件事——**鏡頭有實體位置**（有東西比主體更靠近鏡頭且已落在景深之外，鏡頭因此不再是無形的觀察點，而是空間裡的一個具體座標），以及**空間往前後真實延伸**（背景不是一張貼在主體後面的圖）。使用者說「要電影感」時，缺的往往是縱深而不是色調。
- **它在既有規則裡的位置**（不要與硬規則打架）：硬規則 8 的 `2.39:1` 屬畫幅層、硬規則 11 的「時段＋天氣」屬光線層、本項屬構圖層，三者不同層，可同時用且互相加成。照 `07-beyond-the-charts.md` 2-4 的程序，仍是先加時段＋天氣重生；本項與它同批加入，而**兩者都排在任何 `圖二` 風格包之前**——先把縱深與光的成因做出來，再考慮要不要花掉一個風格包名額。
- **提示詞**：`three distinct depth planes — an out-of-focus foreground element crossing the lower left corner and covering about one fifth of the frame, the subject sharp in the mid-ground, a separately lit background receding behind them, the foreground element reading as a soft dark mass`
- **讓前景真的糊掉的物理條件**（不寫死就會三層全清晰）：把前景元素放在**對焦距離的一半以內**。淺景深版本 `50mm equivalent at f/2 focused on the subject at two metres, the foreground object one metre from the lens`；深景深版本照 `22 深景深` 的數字（28mm、f/11、對在超焦距約 2.4m），此時 1.2m 以外的前景仍然清晰，得到的是「三層皆實」而不是失焦前景。
- **前景放什麼（挑一個寫死）**：門框側柱、前排人物的肩與後腦、桌緣的杯子、垂下的枝葉、欄杆、雨棚、路過的車頭、一盞近處的燈（順便給出散景光點）。
- **何時用 / 何時不用**：預設全開；只有 `33 鳥瞰` 與純色棚拍去背需求時不用。
- **搭配**：`25 淺景深` 與 `22 深景深` **二擇一**（`05-recipes.md` 已列為互斥，同時寫模型會兩邊都做不到）、`21 遠景`、`圖二 21 賽博龐克街景`、`圖二 05 煙霧體積光`

#### 引導線｜Leading Lines

- **是什麼**：畫面裡的實體線條（道路、走廊、欄杆、屋脊、光帶、陰影邊界、河岸）從畫框邊緣延伸並終止於主體，把視線沿線押到主體上。
- **提示詞**：`a wet road receding from the bottom right corner and converging on the standing figure, the kerb line and the reflected light streak both pointing at the subject, the lines starting at the frame edge and ending exactly where the subject stands`
- **何時用 / 何時不用**：主體佔畫幅高度不到 1/3、環境佔大部分面積時用（`21 遠景`、街景、風景、走廊）；`32 特寫` 與 `31 極端特寫` 不用——畫框內裝不下一條從邊緣走到主體的線。
- **搭配**：`21 遠景`、`22 深景深`、`39 低角度視角`、`圖二 07 單點透視對稱`

#### 框中框｜Frame Within a Frame

- **是什麼**：用畫面內的實體開口（門框、窗、拱門、後視鏡、樹枝間隙、人群縫隙）在主體周圍再造一層邊界。它是 `34 封閉構圖` 條目裡點名的**執行手法**（該條目已說明 closed framing 是概念、frame within a frame 是手法）；但可單獨使用：只框住而不封死四邊，就只有聚焦與遮醜的作用，不帶禁錮感。
- **提示詞**：`the subject seen through a doorway two metres in front of the camera, the dark jamb and lintel occupying the outer 30 percent of the frame on three sides, the opening bright and the surrounding frame two stops darker`
- **何時用 / 何時不用**：要窺視感、隔離感，或背景太亂需要遮掉三面時用；敘事需要暗示畫外世界（人物即將走出去、畫外有威脅）時不用——二次框的作用正是宣告「這裡就是全部」，會把畫外空間關掉。
- **搭配**：`34 封閉構圖`、`42 暗色調`、`22 深景深`、`圖二 09 固定長鏡頭`

#### 負空間｜Negative Space

- **是什麼**：主體以外大面積、低資訊量的連續空白區（天空、素牆、霧、水面、暗部）。孤立感由**面積比**產生，不由表情產生——這是「拍不出情緒」時最省事的補救。操作門檻：空白區佔畫面 60% 以上才讀得出來，要明確就推到 80%。
- **提示詞**：`the figure occupying less than one fifth of the frame in the lower left, the rest of the picture a single uninterrupted expanse of pale grey sky with no texture or object in it, a wide empty margin above and to the right of the subject`
- **何時用 / 何時不用**：要孤獨、留白、或要留出標題／字幕位置時用；要熱鬧、資訊密度、環境敘事時不用。**用了就必須把 `07-beyond-the-charts.md` 3-1 的環境物件從 3 個降到 0–1 個**，否則兩條規則會互相抵銷。
- **搭配**：`21 遠景`、`44 亮調`、`45 低飽和`、`圖二 03 北歐冷冽`

#### 三分法｜Rule of Thirds

- **是什麼**：以兩橫兩縱把畫面切成九宮格，主體垂直軸落在左或右三分線、眼睛落在上三分線、地平線壓在上或下三分線，四個交點是視覺重心。
- **提示詞**：`subject placed on the right vertical third line and facing toward the open left side, eyes sitting on the upper horizontal third, horizon on the lower third, the left two thirds of the frame left open`（**朝向必須與留白同側**——只寫「主體在右、左邊留白」而不寫朝向，模型有一半機率讓人臉朝右貼著畫框，直接違反下面的視線空間）
- **何時用 / 何時不用**：主體側轉、移動、或視線離軸時一律用；背景本身對稱、或要正面對峙時改 `35 居中構圖`。
- **搭配**：`26 斜側視角`、`20 中景`、`圖二 23 生活寫實`

**三分法 vs 居中的選擇規則**

| 選居中 `35 居中構圖` | 選三分 |
|---|---|
| 要**權威／對稱／疏離**：主體被「展示」給觀眾 | 要**自然／敘事／呼吸感**：主體活在一個更大的空間裡 |
| 主體靜止、朝向 0°–45° 且眼睛回看鏡頭 | 主體側轉超過 45°、或正在移動 |
| 背景本身對稱、消失點在正中 | 背景不對稱、需要環境參與敘事 |
| 儀式、對峙、肖像、標本化 | 對白、行走、觀看、暗示畫外 |

**硬性判準**：主體朝向一旦超過 45°（進入 `26 斜側視角`、`29 側面視角`）或人物正在移動，**強制改三分並在朝向／行進側留空間**；此時居中會消滅視線空間，畫面像撞牆。`28 背面視角` 是特例：純 180° 背對時畫面上沒有左右的「朝向側」，要留的是**縱深方向的空間**（人物前方要有一條路或一個明確的目標物，見該條目）；只有人物同時側轉或橫向行進時才回到留左右空間的規則。反過來，一旦下了 `圖二 07 單點透視對稱` 或 `圖二 08 平面正面構圖`，三分法自動失效，別再寫。

#### 頭部空間｜Headroom

- **是什麼**：頭頂到畫框上緣的距離，以佔畫幅高度的百分比計。**景別越緊，headroom 越小**：`20 中景` 約 10%（可見身體填滿九成畫幅高度）→ `19 近景` 5–8% → `32 特寫` 2–5%，特寫可刻意切掉髮頂（headroom 為負）；到 `31 極端特寫` 這個量已不存在（臉的邊界整個在畫外）。兩個例外：`23 全身照` 的上下餘白是為了塞進全身而**一起**決定的（各 5–10%），不在這條遞減曲線上；`21 遠景` 的主體只佔畫幅高度不到 1/3，畫面由地平線高度與人物落點決定，headroom 不是控制量。
- **提示詞**：緊 `tight headroom, the top of the head just below the upper frame edge with only a sliver of space above it, eyes on the upper third line`；鬆 `generous headroom, a wide band of empty sky above the head, the figure pushed toward the bottom of the frame`
- **何時用 / 何時不用**：現行主流模型的預設 headroom 偏鬆（會隨版本改變，但方向一致），`19 近景` 及更緊的景別**每次都主動寫緊**；只有刻意要壓迫主體、或要留標題空間時才寫鬆。
- **搭配**：`32 特寫`、`19 近景`、`17 高角度拍攝`（鬆 headroom 會加深弱化感）

#### 視線空間｜Looking Room / Nose Room（移動時稱 Lead Room）

- **是什麼**：主體看向或走向的那一側，留白必須多於背後，比例 2:1 起跳。違反它（空間全堆在腦後、臉貼著畫框）會立刻產生擠壓與不安——這是可以刻意使用的表現手法，不是純粹的錯誤。
- **提示詞**：正常 `subject on the left third looking toward the right, the space in front of the face twice as wide as the space behind the head, nothing blocking the direction of the gaze`；刻意壓迫 `subject pushed hard against the right frame edge while still facing right, almost no space in front of the face, the entire empty area piled up behind the back of the head`
- **何時用 / 何時不用**：只要主體不是正對鏡頭就必寫；主體正面 0°、或已鎖 `35 居中構圖` 時不寫（該條目已說明居中會消滅 lead room／nose room，這是它只能用在靜止正面主體的原因）。
- **搭配**：`26 斜側視角`、`29 側面視角`、`30 四分之三側面`、`24 動態模糊`（行進方向前方必須留空間，否則速度感消失）

#### 地平線高度｜Horizon Placement

- **是什麼**：地平線在畫框中的高度，決定天／地面積比與觀者的立足感。壓到下三分＝天空主導、開闊、人渺小；抬到上三分＝地面主導、封閉、壓迫；壓在正中＝靜止、對稱、刻意的沉悶。
- **關鍵區分（兩個常被混為一談的量）**：
  - **真正的地平線**（無限遠處的水平線）在畫框內的高度**只由鏡頭的俯仰角決定**——相機水平無傾角時，它永遠落在畫框正中，把相機從 0.5m 抬到 5m 也不會移動；相機高度改變的是地平線**橫切過畫面內人物身上的哪個位置**（它永遠切在與鏡頭等高處）。
  - **牆與地板的交線、近處的山稜線**不是無限遠的地平線，它們離鏡頭有限，**位置同時受相機高度與俯仰角影響**。要下這兩種指令得分開寫。
  - 代價：靠俯仰角把地平線壓低，垂直線就會收斂（仰拍時向上收斂）。要地平線低**又**要垂直線筆直，只有升高機位＋水平機身＋事後裁切上半，或用移軸／垂直修正——提示詞裡要明說 `verticals kept parallel`。
- **提示詞**：`horizon pressed down to the lower third with sky filling the upper two thirds, camera tilted about ten degrees upward, horizon dead level with no roll`；要壓低地平線又不歪垂直線 `horizon on the lower third, camera perfectly level with zero tilt, all verticals kept parallel to the frame edges`
- **何時用 / 何時不用**：戶外、或室內有明確牆地交線時必指定；室內特寫與 `33 鳥瞰`（該條目明文畫面內不存在地平線）不用。
- **搭配**：`21 遠景`、`39 低角度視角`、`圖二 04 魔幻時刻`、`圖二 22 太空歌劇`

#### 對角線構圖｜Diagonal Composition

- **是什麼**：主體、動線或主要結構線沿畫框對角走向，取代水平／垂直的穩定軸，產生動勢與不安定感。**「畫面內容走對角」與「整個畫框傾斜（Dutch angle）」是兩件事**：前者是構圖，機身水平；後者是相機滾轉，屬於機位而非構圖。混寫模型只會把整張圖歪掉。
- **提示詞**：內容走對角 `the subject's body and the staircase both running along the diagonal from the lower left corner to the upper right, no major line parallel to the frame edges, camera level with verticals kept upright`；傾斜畫框 `the whole image rotated about 15 degrees so the horizon runs from the lower left to the upper right, the standing figure leaning with it, everything in the world tilting together`（**不要寫 "the subject stays upright within the tilted frame"**——相機滾轉時世界裡的垂直物一律跟著傾斜，這句是物理上不可能的指令，模型只能二選一亂猜）
- **何時用 / 何時不用**：要動勢、速度、心理失衡時用。真正的互斥只有兩個半：`圖二 08 平面正面構圖`（該風格要求一切與畫框平行，任何對角都會破功）、`圖二 07 單點透視對稱` 只排斥**傾斜畫框與不對稱的對角**（它條目裡明文零旋轉；它自己的透視收斂線本來就是對稱的對角，那不衝突）；`35 居中構圖` 只鎖主體的左右位置，畫面裡有對角結構完全可以，不要誤當互斥。
- **搭配**：`24 動態模糊`、`39 低角度視角`、`46 高對比`、`圖二 01 德國表現主義`

#### 主體與背景分離｜Subject–Background Separation

- **是什麼**：讓主體輪廓能從背景讀出來的手段。這是「圖看起來很糊很平」最常見的真正病因，且三種手段有明確效力排序。
- **優先序：明度差 > 色相差 > 景深虛化。**
  - **明度差最可靠**，兩個理由。(a) 感知面：人眼定位邊緣主要靠亮度通道，色度通道的空間解析度明顯較低，等亮度的純色相邊界人眼定位得很差。(b) 適用面：色相差會被低飽和、單色系統（`圖二 16 黑白默片`、`圖二 15 沙塵單色`）、`37 弱光` 下的色彩退化以及任何後製調色抹平；景深虛化只在特定光圈／焦段／距離同時成立時才有，一旦改用 `21 遠景` 或 `22 深景深` 就整個失效。只有明度差在**任何景別、任何色彩系統、任何景深**下都成立，而且它是一句就能寫死、也能一眼驗收的指令（「背景比受光面暗兩級」）。
  - 執行順序：① 明度差——把主體背後那塊背景壓暗 1.5–2 級，或用 `10 髮絲光`、`14 輪廓光`、`05 背光` 把主體邊緣打亮；② 色相差——主體與背景放在色輪對側（暖膚色對冷藍背景）；③ 景深——`25 淺景深`。三者可疊加，但缺了①的話另外兩個都撐不住。
- **提示詞**：`the subject's outline separated from the background by luminance alone — the wall behind falling two stops darker than the lit side of the face, a hard rim light along the shoulder and jawline exactly where the head crosses the darkest part of the background`
- **何時用 / 何時不用**：主體與背景明度接近時必寫（黑髮對暗牆、白衣對白牆、`28 背面視角` 的後腦對夜景——該條目已把這件事列為必處理項）；主體本身就是剪影、或刻意要 `42 暗色調` 的「融進暗部」時不用。
- **搭配**：`14 輪廓光`、`10 髮絲光`、`46 高對比`、`28 背面視角`

---

## 單幀多格版面

一張生成可以是一個**版面**，而不是一格畫面。多格出自同一次取樣，因此天生共用同一組光、色與質感——這是分別生成拿不到的一致性。代價是解析度：每一格只分到畫幅的一小塊，格數越多，單格能承載的細節越少（換算方式見下一節〈實務警告：多人必崩臉〉的像素高度表）。

先分清楚兩種用途，寫法不同：

- **比較型版面**——同一個主體的多個景別或視角並列，目的是讓格與格可互相比對。底色寫成乾淨的中性無縫，環境會把可比較性吃掉。
- **敘事型版面**——一段連續動作的數個節拍並列，每一格都是完整場景。這一種**不要**清空底色，環境本身就是內容。

四件事，缺一不可：

1. **先宣告格數與版面幾何**。幾格、幾欄或幾列、由左到右還是由上到下。需要時連每一格內部的畫幅比例與黑邊一起寫死——版面有兩個畫幅（容器的、單格的），`SKILL.md` 硬規則 8 要套兩次，只寫一個會得到不受控的切分。不宣告版面，模型會自己決定格數與切法，而且每次不同。
2. **每一格只給自己刻意要變的那一軸**（景別、視角、節拍、狀態，擇一），**其餘各軸明寫維持同一組值**。差異必須落在刻意的那一軸上；其他軸跟著一起漂，就變成幾張無關的圖拼在一起。
3. **例外寫在它所約束的那幾格上，不要寫成全域規則。** 寫成全域，其他格也會照做——這是多格版面最常見的失敗。例外不限一格，重點是把適用範圍指名到格。
4. **每一格的臉單獨結算**。格數直接等於臉數，而且每張臉只分到畫幅的一小塊，`SKILL.md` 硬規則 13 在這裡最容易踩到。若某幾格看的是輪廓、服裝、姿態或動作而不是長相，就對那幾格明寫臉不可辨——背對、低頭、脫焦或被前景遮住——把像素預算集中到真正需要長相的那一兩格。這同時把「臉在格與格之間漂移」的問題移出畫面。

比較型：

`<N> panels in one frame, left to right: <view 1>, <view 2>, <view 3>; the same subject, the same key direction, the same colour treatment and the same texture in every panel; clean seamless neutral ground behind all of them; the face readable only in <panel>, turned away or shadowed in the others`

敘事型：

`one row of <N> panels read left to right, each panel framed to <ratio> inside the container; panel 1 <shot size + angle>; panel 2 <shot size + angle>; …; the same location, the same wardrobe and the same time of day across all panels`

---

## 多人構圖

畫面裡一旦超過一個人，構圖問題會從「主體擺哪裡」變成「**人與人之間的關係、間距與縱深**」，同時多出一個生成模型獨有的風險：臉會崩（`SKILL.md` 硬規則 13 的展開版，見本節末）。以下六種站位涵蓋絕大多數需求，每一種都必須寫死表格最後一欄，否則模型會退化成「兩個人並排看鏡頭」。

| 構圖 | 英文提示詞片語 | 適用情境 | 必須寫死的一點 |
|---|---|---|---|
| **雙人平衡** two-shot | `two-shot in 2.39:1, both figures framed from just above their heads down to the waistline, 50mm equivalent from about two metres, the two standing roughly eighty centimetres apart and each turned three quarters toward the other, a clear gap of visible background between their shoulders, camera at their shared eye level` | 對話開場、關係建立、要讓觀眾同時看到兩人的反應 | 兩人之間**留出可見的背景縫隙**；並且**畫幅要一起寫死**——這是唯一畫幅直接決定切點的構圖（見表下說明），不寫畫幅就得到別的景別 |
| **縱深雙人** staggered two-shot | `staggered two-shot, 50mm equivalent at f/2.8 focused on the far figure three metres away, the near figure standing one metre closer to the lens, larger in frame and slightly soft, the far figure sharp and smaller, their heads at clearly different heights and never overlapping` | 權力不對等、緊張、暗示、審訊 | 兩人**距鏡頭的距離差**（用公尺寫）＋**對焦在誰身上**＋**頭不重疊**；只寫距離差不寫合焦點，模型會把兩人一起拍清楚，縱深就消失了 |
| **過肩** over-the-shoulder | `over-the-shoulder shot, the near figure's shoulder and the back of their head occupying the left third of the frame as a dark out-of-focus mass with the face never visible, the speaking subject sharp in the mid-ground looking at the near figure's eyes just off the lens axis and not into the lens, 50mm equivalent at f/2.8 focused on the far subject's near eye, camera just behind and slightly above the near shoulder` | 對白正反打、要讓觀眾站進其中一人的位置 | 近端人物**只給肩＋後腦、明說臉不可見**（這是「兩個人在畫面裡但只有一張臉要成立」最便宜的解法，也自帶三層景深）；以及遠端主體的視線**落在近端人物的眼睛、擦過鏡頭而不是看進鏡頭**——寫成 "looking toward the lens" 會得到破第四面牆的直視 |
| **三角形站位** triangular blocking | `three figures arranged as a triangle, two seated closer to the lens forming the base and one standing further back at the apex, their heads at three clearly different heights with no two heads on the same horizontal line, the group reading as one solid shape against the background` | 三人的群戲、家庭照、團隊照，取代「排排站」 | **頭高互不相同**，而且要寫死**高度差是怎麼來的**（坐／站、或站在台階上）。只寫「後面那個人在頂點」在幾何上是矛盾的：等高的人站得越遠，頭在畫面上越低——頂點要嘛比別人高（站 vs 坐），要嘛離鏡頭最近 |
| **群像景深分層** group depth layering | `six people staged across three depth planes — two sharp in the mid-ground as the actual subject, two cropped and out of focus in the foreground, two small and soft near the back wall, facial detail dropping off progressively with distance` | 宴會、辦公室、街頭、市集，任何要「有人氣」但不需要每張臉都成立的場景 | **只有中景那一層要臉**，前後兩層明說失焦／被畫框切掉／背對鏡頭 |
| **環繞式** circular / enveloping | `figures arranged in a ring around a single light source sitting at ground level in the centre of the group, the two nearest people seen from behind as dark silhouettes framing the bottom of the frame, the far side of the ring lit from below by that source with shadows thrown upward onto their faces, camera at the seated ring's eye level` | 營火、圍桌、圍觀、儀式；要把觀眾放進圈子裡 | 最靠鏡頭的一到兩人**只給背影剪影**（同時解決崩臉與縱深）；並寫死**光源高度**——中心光源放在地面才會得到 `13 底光`／`12 火光` 的由下往上照，不寫高度模型會給一盞平光吊燈 |

**為什麼 two-shot 要連畫幅一起寫**：兩人並排需要約 1.25m 的實拍寬度。50mm 站 2m 時畫面寬約 1.44m，剛好塞得下；但在 3:2 底下對應的畫面高度是 0.96m，從髮頂往下算會直接裁到大腿，得到的是全身／美式景而不是腰上。同一個機位改成 2.39:1，畫面高度只剩約 0.6m，切點才落在腰線。**兩人並排的景別是被畫幅決定的，不是被焦段決定的**——要腰上 two-shot 就用 2.39:1 或 1.85:1，用 3:2／1:1 就接受它切在大腿。

**共通執行規則**

- **人數用確切數字寫，並逐一給互斥的辨識特徵**：`three people: a woman in a red coat on the left, a bearded man in a grey jacket in the centre, a teenager with a shaved head on the right`。寫 "a group of people" 模型不受數量控制；寫 "three similar-looking young women" 則極易讓特徵互相混合。超過 5 人就別逐一寫，改成「3 個具名主體 ＋ 其餘作為失焦背景群」。
- **眼線要明寫指向誰**：`the man looking at the woman's face, the woman looking down at the table`。不指定的話模型會讓所有人一起看鏡頭，關係全部消失。
- **正反打要能剪在一起（同一場戲生兩張圖時）**：兩張的**機位要在動作軸的同一側**（180° 規則）。落到提示詞上就是——A 圖 `subject on the left of frame looking toward the right`，B 圖 `subject on the right of frame looking toward the left`。若兩張都把人放在畫面同一側、或都看同一個方向，就是越軸，剪起來會變成兩人望向同一處而不是彼此。
- **群像的光位比單人更難**：`03 側光` 打一群人時，離光遠的那一側與被前排擋住的人會整個掉進暗部（平方反比加遮擋，不只是「後排」）。兩個解法：把大面積光源退遠——距離越遠，前後排的照度比越接近 1，貼太近則前排過曝後排全黑；或改用 `08 窗光`、`09 柔光` 這類大面積光源，或用 `11 自發光`（每人自帶一個實用光動機）。

### 實務警告：多人必崩臉

以目前主流的圖像生成模型（2025–2026）而言，**超過 3 張需要「成立」的正臉時，幾乎必然崩臉**——五官融合（A 的鼻子長到 B 臉上）、眼睛數量或位置錯亂、頭身比例不一致、同一畫面裡出現兩張近乎複製的臉。這不是提示詞寫得不夠好。可驗證的機制是**每張臉分到的解析度不夠**：模型在壓縮過的潛在空間裡作畫，一張只佔畫幅高度 5% 的臉，在 1024px 高的輸出上只有約 50px，換算到潛在空間只剩幾個格點，不足以編碼一組五官結構。臉的張數則是次要放大器——臉越多，模型越容易把某張臉的特徵複製到隔壁。

**真正的主變數是「每張臉在成品上的實際像素高度」＝ 臉佔畫幅高度 × 輸出高度，不是單純人數。**

| 情況 | 每張臉佔畫幅高度 | 換算成 1024px 高輸出 | 風險 |
|---|---|---|---|
| 1–3 人，`32 特寫`／`19 近景`／`20 中景` | 25% 以上 | 250px 以上 | 低——每張臉都分到足夠像素 |
| **4 人以上的群像（畫面寬到塞得下四個人，臉自然變小）** | **5–20%** | **50–200px** | **極高——這是必崩帶** |
| 10 人以上，`21 遠景` | 3% 以下 | 30px 以下 | 低——臉小到只是色塊，觀眾不要求細節 |

單張臉低於約 100px 時五官開始不穩（經驗值，會隨模型版本與輸出解析度變動；新模型的臨界值可能下移，但「臉的像素高度是主變數」這件事不變）。所以 `21 遠景` 裡站十個人不會崩，`19 近景` 裡塞四張正臉一定崩。判斷時先估「成品上每張臉大約多少像素」，再決定要不要動手。

**動手前先做一件事**：確認輸出解析度已經開到工具允許的上限，並考慮改直幅——同樣一張臉，在 1536px 高的畫面上得到的像素是 1024px 的 1.5 倍。這一步不改構圖也不花名額，但可能直接把你從必崩帶推出去。之後再依序試下面四招。

**解法，依序試（前面的成本最低）：**

1. **改用背影／側臉／低頭**，把需要成立的正臉降到 3 張以內。寫 `the two nearest figures seen from behind, only the backs of their heads presented to the lens, faces never visible`（正反兩面都寫，`28 背面視角` 條目已說明只寫否定句模型會偷偷把頭轉回來）、`the third person turned to a strict 90-degree profile`、`one figure looking down with the face shadowed by the hat brim`。過肩構圖是這一招的標準形式。
2. **把遠處的人推進失焦區**：`25 淺景深` 加上**正面敘述**的 `background figures reduced to soft coloured shapes, their heads reading as smooth featureless ovals`。不要寫 "features deliberately not defined" 這類否定句——模型對否定句的服從度低，會照樣把每張臉畫完整。
3. **改用 `21 遠景`**：把臉縮到畫幅高度 3% 以下，讓臉小到不需要細節；敘事改由姿態、間距、行進方向與剪影承擔（作法見該條目的「常見錯誤」——遠景不要同時要求可讀的表情，兩者物理上互斥）。
4. **分次生成後合成**：把畫面拆成前景組與背景組（極端情況每人單獨一張），各自生成後在影像編輯軟體合成；或先生成群像再對每張臉做局部重繪（inpainting，前提是所用工具支援）。若工具支援角色參考圖／identity reference，用同一張參考維持同一人跨圖一致。這是目前最能保住「多張大正臉全部成立」的路線，成本也最高，四人以上的正式合照大多繞不開。

**反面警告**：不要用加強語氣硬解。`perfect faces for everyone`、`each face fully detailed`、`consistent facial features` 這類詞不含任何空間資訊，**不會替任何一張臉多爭取到一個像素**；而且它們就是 `07-beyond-the-charts.md` 1-4 禁詞清單所指的品質形容詞——`perfect` 系列會把模型推向「平均臉」先驗，結果是每張臉更像彼此，正是你要避免的融合。正解永遠是**減少需要成立的臉的數量、或提高每張臉分到的像素**，而不是要求模型畫得更用力。
