# 影片視覺篇｜動態、鏡頭運動與連續性

前七個檔案描述的是**一幀**。本檔提供幀與幀之間的 **visual-look subcontract**，供
`seedance-prompt-director` 併入已選定的 provider/task operation。它保有攝影機運動、主體動作與
時間性風格的美學技法，但不擁有完整影片 prompt 或任何 provider 操作契約。

本檔可以回答「這個畫面從 opening look 如何可見地變化到 end look」，但不決定 task、references、
timeline、blocking、physics、acting、audio、acceptance、平台參數、時長或 negative 欄位。這些由
`seedance-prompt-director` 的已驗證 provider/task contract 決定；多鏡與跨鏡 production 則由
`seedance-film-producer` 決定。

For a scoped visual-look subcontract, include numeric motion or timing values only when the user provided them.
Translate all other table measurements into qualitative direction before export.

本檔給出靜圖流程沒有的兩個視覺軸：**攝影機運動**與**主體動作**，以及
`圖二 09 固定長鏡頭` `圖二 10 手持跟拍` `圖二 19 偽紀錄片` 在靜圖情境下的等效替換。

> **關於本檔的模型行為描述**：下面所有「難度」「失敗風險」「哪些動作會崩」都是**跨模型的經驗優先序**，
> 不是任何模型的規格書。各家模型與各個版本的表現差異很大，且會隨版本改變。
> 用法是「先選低風險的寫法，高風險的預留重抽預算」，不要當成保證。
> 凡是本檔沒有寫出具體參數名稱的地方，都是刻意的 —— **不要自己編造旗標或參數名**。
> 若目標平台提供獨立的鏡頭運動選單或運動強度欄位，一律優先用那個欄位，欄位名稱與可用值以當下介面為準。

---

## 一、影片 visual-look 與靜圖 look 的差異

### 視覺子契約：opening → change → end

靜圖 look 回答「這張圖長什麼樣」；影片 visual-look 要補足畫面如何從 opening 變到 end。
交付給 prompt director 時，可用三個視覺欄位，並保持它們只描述 look：

| 欄位 | 描述的視覺資訊 |
|---|---|
| opening look | 初始構圖、景別、主體位置／朝向、光與色彩 |
| visible change | 攝影機運動或主體動作的可見變化、速度與幅度線索 |
| end look | 收在何種構圖、位置、朝向、光與畫面重心 |

例如：`opening look: medium shot, rain-slicked neon street, magenta side key; visible change:
slow physical push-in while she raises her gaze; end look: held medium close-up, jaw set,
gaze off-frame left.` 這只是 visual subcontract；prompt director 仍須依 operation contract 決定
哪些欄位可用、如何表達與是否需要額外的 reference／audio／acceptance 資訊。

### 不變量（invariants）

opening → change → end 只回答「什麼會變」。同樣要回答的是**什麼不准變** —— 沒有被宣告成不變的屬性，
等於允許模型在片段中途重抽它。子契約因此可以有第四個欄位：

| 欄位 | 描述的視覺資訊 |
|---|---|
| invariants | 整段必須維持同一狀態的 look 屬性，一行一項 |

（匯出時對應本檔末〈Visual-look subcontract export〉的 `Look constants:` 那一行。）

寫法四條：

1. **一行一個屬性。** 主光方向、主色相與白平衡、材質與表面狀態（含服裝與道具的濕乾、髒污、磨損、
   反光 —— 僅限表面狀態，款式與識別不屬於本檔）、天氣與地面狀態各自一行。合併成一句總則，
   模型通常只會滿足其中一項。

2. **用可檢查的幀端點，不要用形容詞。** `consistent`、`stable`、`throughout` 沒有可驗收的邊界，
   驗片時無從判定過或不過；改成指名兩個端點再涵蓋中間段，例如：

   `<屬性名>: <狀態描述>, unchanged from the opening frame through the closing frame, and at every point between`

   端點語彙自己寫，不必照抄這個句型；能指出兩個可比對的幀，這條就成立。

3. **只列環境與光學層的 look 屬性。** identity、asset scope、演出、姿勢、表情、對白與事件順序
   一律不得寫進 invariants。這條無條件成立，不因使用者限縮 blocking 或 timeline 而放寬 ——
   那些欄位屬於 `seedance-prompt-director` 與 `seedance-film-producer`，本檔越界只會製造
   兩份互相矛盾的契約。

4. **本質是「維持」的目標就寫進 invariants，不要塞進 end look。** 把不變的東西寫成 end look，
   等於暗示它需要先變化再回來。end look 只描述有變化的屬性收在哪裡。

### 免費的環境動態（可加，但不能取代主體動作）

雨、雪、煙、霧、蒸汽、火焰、水面、風中的頭髮與衣料、窗簾、旗幟、遠處已在畫面內的人流、
車燈流動 —— 這些是模型相對最擅長、崩壞率最低的動態，成本極低，寫一句就讓畫面「活著」。
但它們是**背景動態**；是否需要主體動作、以及如何把動作放入 provider prompt，由
`seedance-prompt-director` 依 task contract 決定。

寫法範例：`rain falling steadily through the beam`、`steam curling up off the cup`、
`her hair and the hem of her coat lifting in the wind`、`traffic lights bleeding past in the
far background`。

---

## 二、攝影機運動詞庫

**一個片段只選一列。** 兩個運動疊加（例如 orbit + push-in）在多數模型上等同於沒有運動指令，
結果是隨機漂移加幾何崩壞。

難度欄的意義：低＝可直接用；中＝可用但要按「緩解」寫法寫死；高＝命中率低，
排進工作計畫時就要預留多次重抽的時間，沒有把握就換成同功能的低難度運動。
（例如「要壓迫感」時，`orbit` 換成 `slow dolly push-in`；「要揭露」時，`crane up` 換成 `dolly pull-out`。）

| 運動 | 英文提示詞 | 敘事功能 | 難度與失敗風險 |
|---|---|---|---|
| 固定機位 | `locked-off tripod frame, the camera does not move at all for the entire shot` | 把注意力全部交給框內的表演與時間流逝；唯一能承載 `圖二 09 固定長鏡頭` 的運動 | **低**。風險最小的一列。唯一的失敗是沒配主體動作 → 得到靜止圖。必須同時寫明主體在框內做什麼 |
| 緩推 | `slow dolly push-in, the camera physically creeping forward about sixty centimetres over the shot, perspective shifting as the framing tightens from medium shot to medium close-up` | 聚焦、進入內心、壓迫感升高；最泛用的敘事運動 | **低**。最穩的運動。主要風險是模型做成變焦（框變緊但透視不變），寫上 `physically moving forward, perspective shifting` 即可校正 |
| 拉出 | `slow dolly pull-out, the camera retreating about a metre so the frame widens from medium close-up to full body, revealing the empty room and one overturned chair, nobody else present` | 揭露處境、抽離、孤立感、段落收尾 | **中**。被揭露的新區域是模型即時編造的，容易長出不合理的空間或多出一個人。緩解：在提示詞裡先寫死會被揭露什麼，並明寫 `nobody else present` |
| 橫搖（左／右） | `the camera pivots in place on the tripod and pans right about thirty degrees at a steady rate, following her as she crosses the room, ending framed on the doorway` | 在同一空間內連接兩個點；建立地理關係 | **中**。角度越大，畫面邊緣新生成的背景越容易出現重複拼貼（複製的窗、接不起來的牆），約 45° 之後明顯變差。緩解：角度壓在 30° 內，並寫明終點看到什麼 |
| 俯仰搖（上／下） | `the camera tilts up about thirty degrees from the wet pavement to the lit third-floor windows, ending with the window frames filling the top third` | 建立尺度、仰望或俯視的權力關係 | **中**。tilt up 到天空最穩；tilt down 停在大片地面容易出現紋理滑移（texture swimming）。緩解：讓終點停在有明確結構的物件上，不要停在純地面 |
| 平行跟移 | `tracking shot moving parallel to the subject at walking pace, the camera holding the same distance and the same side-on profile throughout, a flat brick wall sliding past behind her` | 與人同行、保持客觀距離 | **中**。長距離側移的視差最難算，牆面與路面容易拉伸。緩解：移動距離限制在 2–3 公尺，背景選單純平面（牆、圍籬、車廂） |
| 平行跟移（正面變體） | `the camera tracking laterally along a flat wall at walking pace, the wall staying exactly parallel to the sensor, the subject kept frontal and dead centre for the whole move` | `圖二 08 平面正面構圖` 的標準運動 —— 注意它要的是**正面**，不是上一列的側面剪影 | **中**。風險與上一列相同，另加「牆面不平行導致對稱崩掉」。緩解：明寫 `wall parallel to the sensor` 與 `subject dead centre` |
| 升起 | `crane up, the camera rising from chest height to roof height, about two storeys, staying aimed at the figure below` | 抽離為旁觀者、段落終結、命運感 | **中高**。上升過程中主體常被重繪成別人，地面與屋頂的銜接處易斷裂。緩解：主體保持小（`21 遠景` 等級）、上升幅度不超過兩層樓、主體只做微動作 |
| 環繞 | `the camera orbits about forty degrees around the seated figure at a constant radius, the subject staying dead centre, the background sliding behind her` | 強調、儀式感、揭示空間的三面 | **高**。常見的崩壞來源：臉在轉到側面時被重繪成另一個人、四肢多長、背景在半途換場。緩解：角度壓到 30–45°、速度放慢、主體居中、背景單純、主體只做微動作。要接近 360° 就分兩段生成再接 |
| 手持跟拍 | `handheld camera following one metre behind her at walking pace, low-frequency walking sway only, no high-frequency shake, the frame correcting a beat late` | 紀實感、被迫與主角同速；`圖二 10 手持跟拍` 的本體 | **中**。風險是被做成高頻亂抖或整體糊成一團。緩解：一定要寫 `low-frequency sway` 與 `no high-frequency shake`，並寫明相機在主體的哪一側、多遠 |
| 甩鏡 | `a fast whip pan to the right in the last half second, the frame smearing into horizontal streaks for a few frames before it settles on the doorway already visible at the right edge` | 暴力轉移注意力、慌亂；`圖二 19 偽紀錄片` 的常用手法 | **高**。模型很容易把 whip pan 讀成「換場景」，中途換人、換地點、換光。緩解：只放在片段的最後半秒當出點，且甩到的目標必須**原本就在畫面內** |
| 推軌變焦 | 地板抽走版：`dolly zoom, the camera tracking forward while the lens zooms wider, the subject held at exactly the same size in frame while the corridor walls behind her stretch and pull away`<br>背景逼近版：`dolly zoom, the camera tracking backwards while the lens zooms in, the subject held at exactly the same size in frame while the background compresses and looms in behind her` | 眩暈、認知崩塌。兩個方向的心理效果相反，**必須先決定要哪一個**：往前推＋變廣＝空間被抽走；往後拉＋變長＝背景壓過來 | **高**。需要「主體大小不變」與「背景透視改變」兩個條件同時成立，模型通常只做到一個，或兩個都做成單純變焦。緩解：兩個條件都逐字寫出，背景選有強透視線的空間（走廊、橋、街道），並預期重抽 |
| 急推 | `crash zoom in, a fast optical zoom from a wide framing to a tight framing on his face in under a second, the camera itself not moving, the framing snapping tight and then holding` | 驚嚇、強調、喜劇重音 | **中高**。快速變焦容易帶進畫面撕裂與主體重繪，且模型常把它誤讀成剪接。緩解：放在片段開頭（推完之後留 3–4 秒穩定畫面），並明寫 `optical zoom, the camera itself not moving` |
| 焦點轉移 | `rack focus at f/1.8, sharpness pulling from the rain-covered glass thirty centimetres from the lens back to her face two metres behind it, the foreground falling soft as her eyes come sharp` | 在不動機位的情況下轉移注意力；兩個資訊的先後揭露 | **中**。風險是全程都清楚（沒發生焦點轉移）或前後景一起模糊。緩解：明寫「誰先清楚、誰後清楚」，並同時給淺景深光圈（`f/1.8` 以下）與兩者的實際距離 |
| 穩定器滑行 | `steadicam glide, the camera moving forward at walking pace with no vertical bounce, the horizon staying level, a foreground pillar passing close on the left` | 流暢帶入、探索空間、優雅的主觀移動 | **中**。太穩會被模型做成完全靜止（缺少位移線索）。緩解：一定要給速度與「經過什麼」—— 前景物件掠過是模型判斷位移的主要依據 |
| 微手持 | `near-static frame with a faint handheld float, barely perceptible low-frequency drift that never snaps back, no high-frequency shake` | 讓固定機位有人味而不失去穩定；訪談與對白的安全預設 | **低**。失敗率極低，是「不知道要用什麼運動」時的預設值 |
| 空拍下降 | `slow aerial descent, the camera dropping from roof height toward the street at a steady rate, the downward angle held constant on the crossing below` | 建立場景、由宏觀進入微觀 | **中高**。下降過程中地面細節會被反覆重繪，建築幾何易扭曲，畫面內的文字招牌極易變形成另一串符號。緩解：高度變化幅度小、避開有大量文字的立面、不要同時要求主體大動作 |

### 運動的寫法規則

1. **必給速度**：`slowly` / `at walking pace` / `over the full five seconds` / `in under a second`。
   不給速度，模型多半會做太快 —— 前兩秒把動作做完，剩下空轉。
2. **必給幅度的參照物**：`about sixty centimetres`、`about thirty degrees`、`from chest height to
   roof height`、`passing a foreground pillar`。抽象的 `push in` 幅度由模型隨機決定。
3. **推進距離隨焦段等比放大**。同樣是「中景推到近景」，位移量不同：
   50mm 約 0.6m、85mm 約 1.0m、100mm 約 1.25m（依 `03-framing.md` 的景別距離推算）。
   寫錯數量級，模型會做成幾乎沒動或整個穿過主體。
4. **推拉要寫「透視改變」**：`physically moving forward, perspective shifting`，
   否則模型用變焦冒充，得到的是放大而不是移動。
5. **運動寫在提示詞前段**。與靜圖同理，多數模型對前段 token 的權重明顯高於後段；
   寫在句尾的運動描述經常被整段忽略。
6. **相機運動與主體動作不要方向相衝**：相機 orbit + 主體轉身 = 兩個旋轉疊加，崩壞率極高；
   相機後拉 + 主體同時走離鏡頭 = 兩個後退疊加，尺寸變化過大。
   相機大幅移動時，主體只做微動作；主體大幅動作時，相機固定或只做緩推。
7. **運動用雙極寫法：一個允許 + 逐項禁止。**
   先把要的那一項寫成肯定句（含速度與幅度參照物），再把**不要的軸逐一點名**關掉，而不是只寫一個
   「靜止」或「穩定」的形容詞。軸的清單是固定的：橫搖、俯仰搖、滾動、變焦、推軌、升降、環繞、
   漂移、手持晃動。
   `locked-off tripod frame, no pan, no tilt, no roll, no zoom, no dolly move, no handheld float`
   比 `static camera` 可控，因為後者只是一個形容詞，前者關掉的是具體的自由度。
   **軸清單管的是運動，機位高度還要另外釘一次視點。** 上面清單裡的 `升降` 關掉的是高度的**變化**；
   即使升降被關掉，這一鏡的**起始機位**仍然可能落在高處。景別只說主體佔多少畫面，沒有說相機站在哪
   （相機高度是 `SKILL.md` 十軸表的第 3 軸）。要它不動就寫 `camera height constant`，
   並把不要的高處視點逐項點名：`no aerial view, no drone shot, no bird's-eye angle, no raised or crane position`。
   空拍與俯瞰是很強的預設傾向（這是使用觀察，不是任何平台的已驗證行為）；
   禁止清單漏掉視點這一項，前面關掉的自由度會從起始機位回來。
   **禁止清單若是跨鏡沿用的同一串字，它必須自帶例外，例外寫在清單前面而不是後面**，
   並且**把允許的那個運動逐字寫出來**，不要寫成指向別處的「本鏡指定的運動」：
   `the only camera movement is a slow forward push of about half a metre; no pan, no tilt, no roll, no zoom, no orbit, no handheld float`。
   一串寫死的「全都不准動」貼到本來就指定了運鏡的鏡次上就是自相矛盾，模型可能兩邊都不做。
   同理，刻意要的那一點晃動（微手持、穩定器的呼吸）必須從**該鏡的**清單裡拿掉，
   並在肯定端把幅度寫清楚；整串照抄不改，等於用清單取消了自己指定的運動。
   **穩定度同樣兩極都寫**：要多少晃，就把晃的種類與頻率寫成肯定句，再把相反狀態（完全不動、
   或高頻亂抖）寫成禁止句 —— 上表的手持跟拍、微手持與穩定器滑行三列已經是這個寫法。
   同一個約束用正反各講一次，是這一軸最便宜的保險。
   否定擺在它守護的那句肯定之後（`SKILL.md` 硬規則 15）。這條只適用於**行為**的排除
   （運動軸、穩定度、對焦面）；**色相的排除不適用，物件的排除以正面列舉為原則** —— 色名與物名本身是強 token；
   色相一律走正面列舉（見 `02-tone-color.md` 限制調色盤），物件的部位級例外見 `SKILL.md` 硬規則 15。
   是否另有 negative 欄位由 prompt director 依 provider/task contract 決定，不在這條規則內。

---

## 三、主體動作詞庫

這是**與攝影機運動完全獨立的第二條軸**。靜圖沒有這條軸，所以 `05-recipes.md` 的十一個槽位裡找不到它。
一個片段選一項，環境動態可以另外疊加。

| 動作 | 英文提示詞 | 佔用秒數 | 穩定度與注意 |
|---|---|---|---|
| 轉頭看向鏡頭 | `she slowly turns her head toward the lens over two seconds and holds the look` | 2–3s | **高**。最可靠的敘事動作。轉幅越大越容易換臉，控制在 90° 以內 |
| 抬頭／低頭 | `he lifts his chin from looking down at his hands until his eyes reach the lens` | 2s | **高**。配緩推使用效果最好 |
| 呼吸與眨眼 | `she blinks twice and breathes, her chest rising slightly, otherwise motionless` | 全程 | **極高**。什麼都不想做時的安全牌，可讓固定機位不死板 |
| 走向鏡頭 | `she walks toward the camera, four unhurried steps, going from full body to medium shot` | 4–5s | **高**。正面走近比橫向走位穩定；步數要寫出來 |
| 走離鏡頭 | `he walks away down the corridor until he is a small figure at the far end` | 5s | **高**。背影最不容易崩，是長片段的首選 |
| 傾身進入光裡 | `she leans forward until her face crosses into the light and is lit from the side` | 3s | **高**。同時完成動作與光影變化，資訊密度最高的一個動作 |
| 轉身背對 | `she turns her body away from the camera until her back fills the frame` | 3s | **中**。轉向背影穩定；反過來由背影轉成正面容易換臉，要轉正面請改用首幀圖鎖臉 |
| 起身／坐下 | `he rises from the chair to standing in one continuous motion` | 3–4s | **中**。中景以上拍；特寫下的起身會出現身體比例跳動 |
| 表情變化 | `her blank expression shifts into a small closed-mouth smile` | 2–3s | **中高**。幅度必須小。大笑、張嘴、哭喊容易讓牙齒與臉部結構崩解 |
| 伸手觸碰（停在表面） | `she reaches out and lays her open palm flat on the window glass, and leaves it there` | 3s | **中**。手指在「抓握」瞬間最容易多長或融合。讓手**貼在表面或停在半空**，不要抓握物件 |
| 吐氣／呼出的煙 | `he exhales slowly, the breath drifting up through the light beam` | 3s | **高**。煙霧與水汽是模型相對最擅長的動態 |
| 髮絲與衣料飄動 | `her hair and the loose hem of her coat lift and drift in a steady wind` | 全程 | **高**。可與任何主體動作疊加，不佔動作名額 |
| 手指輕敲 | `his fingers tap the tabletop once, then stop` | 2s | **中低**。只在中景以外使用；特寫下的手指動作崩壞率明顯偏高 |
| 視線游移 | `her gaze drifts slowly from off-frame left to the lens` | 2s | **高**。純眼球運動比頭部運動更安全，適合極特寫 |

### 「一個動作」的判準

硬規則第 1 條要求一個片段只放一個主體動作。判準是：

- **同一個關節群、同一個方向、可以一氣呵成 ＝ 一個動作**。
  「抬頭並轉向左側」是一個（頸部、單向、不停頓）。
- **換關節、換方向，或中間必須停頓再起 ＝ 兩個動作**。
  「走到窗邊然後坐下」是兩個；「轉頭看鏡頭再低下頭」是兩個（單向變雙向）。

兩個動作就分成兩個片段。

### 模型做得到 vs 做不到的界線

**可靠**（單一大關節、低頻、單向、不需要精細接觸）：

- 頭部轉動 ≤ 90°、視線移動、眨眼、呼吸
- 全身直線走動（朝向鏡頭、背向鏡頭、或與鏡頭平行）
- 幅度小的表情變化（面無表情 → 微笑、皺眉）
- 傾身、抬手到定位並停住
- 頭髮、衣料、旗幟、窗簾、水面、雨、雪、煙、霧、蒸汽、火焰
- 光源本身的變化：雲影掃過、霓虹閃爍、車燈掃過牆面、燈被打開
- **已經在畫面內的次要人物走出畫面**（出畫比入畫穩定得多）

**崩壞率高，不要寫進提示詞**：

- **精細手部操作**：扣鈕扣、打字、翻書頁、點菸、倒水、切食物、拿筆寫字 —— 手指數量與拓樸會在動作中改變
- **兩人以上的肢體互動**：握手、擁抱、遞東西、接吻 —— 肢體互相穿透或融合
- **快速動作**：跑步特寫、揮拳、跳躍、舞蹈的快速段落 —— 幀間位移過大，產生撕裂與殘影
- **剛體的複雜物理**：玻璃碎裂、東西倒下、球彈跳、骨牌
- **精準的口型對嘴**（沒有音訊驅動時）
- **運動中的文字**：招牌、書封、字幕在鏡頭移動時常被逐幀重寫成另一串符號
- **從畫面外新增主體**：第一幀沒有的人走進畫面、人群憑空增加
  —— 若敘事一定要有人入畫，最低風險的寫法是讓他**在第一幀就已經部分在畫面內**：
  `a second figure already visible at the left frame edge, walking further into the room`。

### 想要崩壞動作時的改寫策略

| 使用者要的 | 改寫成 | 原理 |
|---|---|---|
| 他點菸 | `he already holds a lit cigarette, and exhales slowly, smoke rising past his face` | 用「動作的結果」取代「動作的過程」 |
| 兩人握手 | 拆成兩個片段：A 片段伸出手停在半空、B 片段對方的反應鏡頭 | 接觸瞬間用剪接跳過 |
| 她跑過街道 | `tracking shot parallel to her at a run, medium shot, heavy motion blur on the limbs` | 拉遠到中景並吃掉細節，不要跑步特寫 |
| 他翻開書 | `the open book already in his hands, one page lifting in the draught` | 起始就在動作的中段或後段 |
| 她倒水 | `water already pouring in a steady stream into the glass, the level rising` | 同上；連續流體比起手式穩定 |
| 他打開門走進來 | `the door already standing open, he steps through it into the room` | 門的鉸鏈運動與人的走動是兩個動作，砍掉一個 |
| 一群人在跳舞 | `a crowd swaying slowly in place, lit by a single moving beam` | 把個體動作換成群體的低頻同向運動 |
| 路人入鏡 | `a passer-by already crossing the foreground, walking out of frame left` | 把「入畫」改成「出畫」 |

---

## 四、視覺連續性建議（非 provider 操作契約）

以下是 visual-look 的取捨與風險提示，不是所有模型或單一 clip 的強制格式。它們不宣告
字數、negative、畫幅、時長、剪接或平台 UI 的通則；prompt director 必須以當前 provider/task
evidence 決定可用控制與最終 prompt。cut 或 transition **only if the operation contract explicitly
allows it**，並由 prompt director 寫入；本檔不自行路由或實作這些操作。

1. **控制密度建議：優先一個攝影機運動與一個主體動作。**
   同時增加多個大幅運動會提高隨機漂移與幾何崩壞風險。選擇高難度運動（orbit、crane、
   dolly zoom、whip pan、crash zoom、空拍下降）時，較小的主體動作通常更容易維持畫面可讀性。

2. **轉場是 operation 選擇，不是本 library 的禁令或預設。**
   若 operation contract 支援 cut、transition 或其他相鄰鏡頭控制，提供其必要的視覺 look
   與兩端狀態給 prompt director；否則只描述連續畫面內的視覺 change。不得由本檔推斷平台能否
   剪接、轉場或如何實作多鏡。

3. **時間節奏以 provider task 為準。** 平台可選時長、extension 與可用節奏必須先由 prompt
   director 確認；這裡的秒數例子只用來說明動作速度，不構成任何平台或單 clip 的長度規則。

   | 片長 | 裝得下什麼 | 不要嘗試 |
   |---|---|---|
   | 5s | 1 個相機運動 + 1 個主體動作。分鏡時用「1s 安定 + 3s 動作 + 1s 收尾」當心理模型去配秒數（這是規劃用的切法，不是模型的內部行為） | 走完一整條走廊、完成一段對白、任何有起承轉合的事 |
   | 10s | 同一個動作放慢，或「1 個動作 + 該動作的餘韻」（走到定位後站定並轉頭） | 兩個獨立事件。片段越長，越後段的臉、服裝、場景越容易漂移 —— 這是連續性成本，沒有固定的秒數門檻，但方向是單調的：能用短的就用短的 |

   多鏡段落的節奏與分鏡數量由 `seedance-film-producer` 規劃，而非從這些示意時間外推。

4. **跨鏡 look continuity。** 同段落可重用主體外觀、光、色與載體描述，並只改必要的
   運動、動作、景別或焦段。跨鏡 identity／asset scope 與 production continuity 屬於
   `seedance-film-producer`；reference contract 仍由 prompt director 擁有。

5. **幀率與快門是可選的視覺語彙。** 只有 provider/task contract 證實可表達或可控制時才交給
   prompt director；本表不保證其被任何模型精確執行。

   | 要什麼 | 提示詞 | 對應項目 |
   |---|---|---|
   | 電影標準動態模糊 | `24fps with a 180 degree shutter, one forty-eighth of a second per frame, natural motion blur on moving limbs` | `24 動態模糊` 的自然級 |
   | 最大限度的電影拖影 | `24fps with a 360 degree shutter, one twenty-fourth of a second per frame, limbs smearing into arcs` | `24 動態模糊` 的強化級。注意 1/24 秒仍遠短於 `03-framing.md` 靜圖 `24 動態模糊` 用的 1/15–1/4 秒 —— **影片裡拿不到靜圖那種長曝拖影**，別承諾使用者 |
   | 銳利無糊的頓挫感 | `24fps with a 45 degree shutter, one one-hundred-and-ninety-second of a second per frame, staccato stuttering motion with almost no blur between frames` | 配 `46 高對比` |
   | 抽格定格動畫 | `animated on twos: twelve distinct poses a second, each held for two frames inside a twenty-four frame per second timeline, every edge razor sharp with no motion blur, faint exposure flicker between poses` | `圖二 20 定格動畫質感`。與 `24 動態模糊` 互斥（見 `05-recipes.md` 表 B） |
   | 默片抽格 | `undercranked to sixteen to eighteen frames per second and played back at twenty-four, movement running roughly a third to a half faster than real time and slightly jerky, brightness flickering frame to frame` | `圖二 16 黑白默片` |
   | 慢動作 | `filmed at 96fps and played back at 24fps, four times slower than real time, very little blur on any single frame` | 與 `24 動態模糊` 互斥：幀率拉高等於每格曝光變短，拖影必然減少，二選一 |
   | 交錯掃描錄影 | `interlaced video with combing artefacts on every fast movement`（NTSC 區寫 `60i`，PAL 區寫 `50i`） | `圖二 14 數位早期`、`圖二 17 VHS 錄影帶` |

6. **首尾 look 思維。** 若 prompt director 的 provider/task contract 支援首幀或尾幀，
   可將它們視為 visual reference；本檔不假定任何平台都有這個能力。常見的視覺工作法是：
   (a) 先用 `05-recipes.md` 的靜圖組裝順序產出首幀圖（構圖、光、色、質感全部在這一步鎖死）；
   (b) 將 image-to-video 的 visual subcontract **只寫變化**，交由 prompt director 組裝。
   純文字 text-to-video 在構圖、光位與色彩上的命中率明顯低於 image-to-video，
   而且跨片段的一致性只能靠首幀圖來守。給了首幀圖之後：

   - **不要在 visual subcontract 裡重寫一次靜態描述**。文字與圖打架時，模型兩邊都做不好。
   - 只留：相機運動（含速度與幅度）、主體動作（含秒數）、結束狀態、幀率與快門。
   - 若模型支援首尾兩幀，把兩張都給，文字可以只剩速度詞（`even pace across the shot, no easing`）。

7. **連續 look 優先保持一個空間、時間與主光方向。**
   在連續畫面中改變地點、時段、主光方向或主體數量，通常會提高畫面不連續的風險。
   例外是**光源本身在動**：手電筒、車燈、旋轉警示燈、雲影 —— 這種要明寫「光源在動」，
   而不是寫「光線改變」。

8. **失效風險是 QC 線索，不是 negative 規則。** changing identity、extra limbs、warping
   background、duplicated subject 與 text flickering 可作為檢查清單。是否存在 negative 欄位、
   是否採用、以及如何表達，都由 prompt director 的已驗證 provider/task contract 決定。

9. **聲音不屬於 visual-look subcontract。** 音軌、對白、音效與音畫因果由 prompt director
   的完整 shot contract 處理；本檔只可說明畫面可見的聲音來源或動作線索。

10. **連續性失敗交由正確 owner 診斷。** identity、動作或視覺 continuity 不成立時，
    `seedance-video-qc` 用生成證據診斷；後續 revision 由 prompt director 或 film producer 決定。

---

## 五、圖二三項的靜圖／影片適用性

`圖二 09 固定長鏡頭`、`圖二 10 手持跟拍`、`圖二 19 偽紀錄片` 三項的技法核心是**時間**，
不是光或構圖。它們在靜態圖上幾乎無效 —— 使用者在生圖情境提到這三項時，
不要照抄 `04-film-styles.md` 的風格包名稱，改用下表的靜圖等效替換。

（另外注意 `05-recipes.md` 表 A 的最後一列：`圖二 09` 與 `圖二 10` 在**影片**情境下是同軸互斥
—— 一個要求機位絕對靜止，一個要求機位跟著人呼吸，同時寫等於互相取消。）

| 項目 | 本質上是哪條軸 | 在靜圖上為什麼幾乎無效 | 靜圖等效替換（圖一編號） | 影片情境的正確寫法 |
|---|---|---|---|---|
| `圖二 09 固定長鏡頭` | 攝影機運動（＝零運動）＋ 片長 | 「固定」與「長」兩個特徵在單張圖上都不存在 —— 單張圖本來就沒有機位運動，也沒有時間。這個標籤在靜圖上傳達的資訊量是零 | `22 深景深` + `08 窗光` + `34 封閉構圖` + `45 低飽和` + `21 遠景`（保留它的打光與構圖配方，丟掉時間特徵） | `locked-off tripod frame` + 主體在框內走位進出，全片段不加任何相機運動 |
| `圖二 10 手持跟拍` | 攝影機運動 ＋ 操作者的身體 | 「跟隨」「晃動」「追不上的構圖修正」全是跨幀現象。單張圖只剩下這些現象在該幀留下的殘跡 | `24 動態模糊` + `28 背面視角` + `20 中景` + `45 低飽和` + `08 窗光` + 幾度傾斜地平線 + 不完美構圖（頭頂被切、主體前方無留白）+ 高 ISO 噪點 | `handheld follow` + 主體行走，務必寫 `low-frequency walking sway, no high-frequency shake` |
| `圖二 19 偽紀錄片` | 攝影機運動 ＋ 連續時間中的操作失誤 | 只有**部分**瑕疵是跨幀的：自動曝光抽動、對焦搜尋、掉幀、甩鏡。單幀只能保留其中一瞬的證據，觀眾讀不出「這是有人在拍」。**但 rolling shutter 斜切是單幀就成立的幾何瑕疵**（垂直線在同一格裡就是斜的），靜圖版要留著 | `37 弱光` + `42 暗色調` + `24 動態模糊` + `39 低角度視角` + `22 深景深`（小感光元件的深景深是 found footage 的可信度來源，見 `05-recipes.md` 表 B）+ 機頂 LED 硬正面光（`27 正面光` 的硬光版）+ 超廣角變形 + rolling shutter 斜切 + 高 ISO 彩噪 + 畫面內 REC 紅點與時間碼 | 加回真正跨幀的瑕疵：AE 抽動、對焦搜尋、掉幀；`whip pan` 只放片段最後半秒 |

### 三項的靜圖替換提示詞（可直接取用）

**`圖二 09 固定長鏡頭` → 靜圖版**（丟掉 `one unbroken static take`，其餘照用）

```
Interior lit only by one household tungsten bulb and daylight spilling through a window, the
two colour temperatures left mixed and uncorrected, warm pool against cool pool, no film
lighting and no bounce, corners falling away to near black; 40mm at f/5.6, deep focus from the
foreground table to the far doorway, camera locked at seated eye level 115cm off the floor;
the figure small in frame at a quarter of the picture height, off centre, seen past a door
jamb, wide empty negative space, muted desaturated palette, skin left its real sallow yellow,
fine 35mm grain, 1.85:1
```

**`圖二 10 手持跟拍` → 靜圖版**（用單幀能留下的四樣證據近似：拖影、傾斜、構圖失誤、噪點）

```
Available light only, mixed daylight and green corridor fluorescent left uncorrected, exposed
for the face with the window behind blown out, no fill, the face two stops under as she turns
away; 28mm at f/2.8 shot from shoulder height one metre behind her, the back of her head
filling a third of the frame and cropped hard against the top edge, horizon tilted four
degrees, almost no space ahead of her, focus landing slightly soft on her shoulder, mild
motion blur on her trailing hand at 1/40 second, native shadow noise, desaturated neutral
documentary grade, no sharpening, preserve natural skin tone, 1.66:1
```

**`圖二 19 偽紀錄片` → 靜圖版**（跨幀的瑕疵換成同一瞬間就成立的單幀瑕疵）

```
First-person handheld camcorder frame, 18mm equivalent ultra-wide at f/2 on a small sensor so
everything past two metres stays deep in focus, ISO 6400 colour noise, the only light a
camera-mounted LED carving a harsh frontal cone and leaving everything past three metres in
noisy black, centre blown out while the corners fall into macroblocked shadow, focus visibly
missed on the subject, rolling-shutter skew slanting the verticals, heavy motion blur on the
arm crossing the frame, the operator's sleeve clipping the frame edge, a low tilted angle from
hip height, REC dot and burned-in timecode in the corner, 16:9
```

### 其餘 21 項的適用性標記

**A 類｜靜圖影片皆可，靜圖已完整**（13 項）
`圖二 01 德國表現主義`、`圖二 02 義式驚悚紅綠光`、`圖二 04 魔幻時刻`、`圖二 06 單光源夜戲`、
`圖二 07 單點透視對稱`、`圖二 08 平面正面構圖`、`圖二 11 三色印片`、`圖二 12 柯達克羅姆`、
`圖二 15 沙塵單色`、`圖二 21 賽博龐克街景`、`圖二 22 太空歌劇`、`圖二 23 生活寫實`、
`圖二 24 宇宙恐怖`

這 13 項的技法核心是光、色、鏡頭與構圖，全部可以在單幀成立。用在影片上時直接照抄風格包，
再加一組運動＋動作即可。其中兩項有慣用運動：`圖二 07 單點透視對稱` 配 `slow dolly push-in`
沿中軸推進；`圖二 08 平面正面構圖` 配上表的「平行跟移（正面變體）」沿平牆橫移，
或乾脆 `locked-off tripod frame`。

**B 類｜靜圖可用，但關鍵特徵是時間性的，影片才完整**（8 項）

| 風格 | 只有影片拿得到的特徵 | video visual-look 補語 |
|---|---|---|
| `圖二 03 北歐冷冽` | deadpan 的力量來自「事情很久都不發生」 | `locked-off wide frame, nobody moves for the whole shot except one figure already visible at the left frame edge who walks slowly further into the room` |
| `圖二 05 煙霧體積光` | 煙必須在光柱裡翻滾流動，靜圖的煙是凝固的 | `haze drifting slowly through the beam, the shaft breathing as the smoke rolls` |
| `圖二 13 港片霓虹` | 霓虹管的不規則閃爍、雨的落下、前景路人掠過鏡頭的拖影 | `neon tubes flickering at an uneven rate, rain streaking through the light, a passer-by already in the foreground smearing past the lens and out of frame` |
| `圖二 14 數位早期` | 交錯掃描的梳狀 artefact 與自動增益抽動只在運動中顯現 | `interlaced 60i video with combing artefacts on every fast movement, auto-gain pumping as the exposure hunts` |
| `圖二 16 黑白默片` | 抽格造成的走路速度異常、逐幀亮度閃爍、片門抖動 | `undercranked to sixteen to eighteen frames per second and played at twenty-four, movement running roughly a third faster than real time, brightness flickering frame to frame, the frame weaving in the gate, scratches and dust jumping between frames` |
| `圖二 17 VHS 錄影帶` | tracking 雜訊帶緩慢上滾、色度拖尾、下緣 head-switching 撕裂 | `tracking noise band rolling slowly up the frame, chroma smearing behind anything that moves, head-switching tear flickering along the bottom edge` |
| `圖二 18 十六毫米顆粒` | 顆粒逐幀重新分布（grain boil）與片門抖動（gate weave） | `grain boiling frame to frame, slight gate weave shifting the whole frame a pixel or two` |
| `圖二 20 定格動畫質感` | 抽格、輪廓 boil、逐格曝光閃爍 | `animated on twos, twelve distinct poses a second, edges boiling slightly between poses, faint exposure flicker, no motion blur anywhere` |

用在靜圖上時，這 8 項照抄風格包即可（能拿到光、色、材質、載體層），
只是要知道少掉的那一層是時間，不要期待單幀能還原全部風味。

**C 類｜影片才成立，靜圖需替換**（3 項）
`圖二 09 固定長鏡頭`、`圖二 10 手持跟拍`、`圖二 19 偽紀錄片` —— 見本節上方的替換表。

---

## 六、技法軸如何延伸到影片

`SKILL.md` 現行的軸表是**十軸**（第 2 軸是鏡頭），第 11 層是風格包，第 12 軸才是本檔的運動。
若你手上的版本仍寫成九軸（沒有把鏡頭獨立出來），鏡頭就併在景深槽裡處理，其餘完全相同。

### 照用的部分

**十軸全部照用，一項都不刪。** 差別只在於：靜圖情境下每軸給一個值，
影片情境下有四條軸要給「起訖兩個值」。

| 軸 | 靜圖版 | 影片版的處理 |
|---|---|---|
| 1 景別 | 單一值 | **起訖兩值**：`opening on a medium shot` → `ending in medium close-up`。有推拉時必寫；沒有運動時兩值相同，寫一次即可 |
| 2 鏡頭（焦距、畫幅） | 單一值 | 照用，且**片段內不可改變** —— 唯一的例外是 dolly zoom。焦段可以逐鏡次改（那是分鏡決策），但同一個片段裡只能有一個值 |
| 3 相機高度 | 單一值 | 有 crane 或 tilt 時為**起訖兩值**（`from chest height to roof height`） |
| 4 主體朝向 | 單一值 | 主體轉頭或轉身時為**起訖兩值**（`from side-on to facing the lens`） |
| 5 光位 | 照用 | 照用，且**片段內主光方向不可改變**。要變只能是光源自己在動（手電筒、車燈），且必須寫明是光源在動 |
| 6 光質 | 照用 | 照用 |
| 7 光源與色溫 | 照用 | 照用，可再加「光源本身的動態」：閃爍、被遮擋、被打開 |
| 8 影調與對比 | 照用 | 照用。片段內不要求曝光改變 —— 模型做出來的曝光抽動是瑕疵，除非你要的正是 `圖二 19 偽紀錄片` |
| 9 色彩 | 照用 | 照用。**跨片段必須逐字複製**，否則每段色調漂移 |
| 10 景深與動態 | 單一軸 | **拆成三條獨立子軸**：(a) 景深與焦點，含 rack focus 的起訖；(b) 幀率與快門角，全片段生效（`24 動態模糊` 在影片裡變成 shutter angle 設定）；(c) 攝影機運動 —— 這是靜圖沒有的新軸 |
| **新增：主體動作** | 不存在 | 每片段至多一項（環境動態可另外疊加，不佔名額） |
| 11 風格包 | 最後一層 | 順延一層。選 C 類三項時只能用在影片上 |

`SKILL.md` 把「攝影機運動 + 主體動作」合稱為影片的第 12 軸；輸出 visual subcontract 時仍把
兩者分開，讓完整 shot contract 的 owner 決定取捨與組裝。

## Visual-look subcontract export

只輸出會改變畫面外觀與動態讀感的內容：**opening look**、**visible change**、**end look**、
**camera**、**lighting**、**color** 與 **texture**。不要在這裡補 task、reference mapping、完整
timeline、blocking、physics、acting、audio、acceptance、平台參數或多鏡 production plan。

```text
Opening look: <framing, camera height, subject orientation, light, color, texture>.
Visible change: <one useful camera-motion option and the visible subject/environment motion>.
End look: <ending framing, orientation, focus, light, color, and visual hold>.
Look constants: <lighting direction, palette allocation, material/texture response>.
Handoff: seedance-prompt-director decides the provider operation, timing, references, causality,
audio, acceptance, and final prompt assembly.
```

若輸入首幀已承擔 composition、lighting、color 與 texture，subcontract 只需交付 camera motion、
visible change 與 end look，並明示哪些既有視覺屬性不得重設。多鏡 look continuity 交給
`seedance-film-producer`；生成後證據與失敗路由交給 `seedance-video-qc`。
