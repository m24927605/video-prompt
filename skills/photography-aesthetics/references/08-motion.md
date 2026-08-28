# 影片篇｜時間軸、鏡頭運動、片長

前七個檔案描述的是**一幀**。這個檔案處理的是**幀與幀之間**。

靜圖提示詞回答「這張圖長什麼樣」；影片提示詞必須回答「這一秒怎麼變成下一秒」。
把 `05-recipes.md` 的靜圖組裝結果原封不動餵給影片模型，得到的是一段幾乎不動的素材 ——
這是本 skill 用在影片上最常見、也最容易被誤判成「模型不行」的失敗。

本檔給出四樣靜圖流程沒有的東西：**攝影機運動軸**、**主體動作軸**、**片長與轉場的硬規則**、
以及 `圖二 09 固定長鏡頭` `圖二 10 手持跟拍` `圖二 19 偽紀錄片` 三項在靜圖情境下的等效替換。

> **關於本檔的模型行為描述**：下面所有「難度」「失敗風險」「哪些動作會崩」都是**跨模型的經驗優先序**，
> 不是任何模型的規格書。各家模型與各個版本的表現差異很大，且會隨版本改變。
> 用法是「先選低風險的寫法，高風險的預留重抽預算」，不要當成保證。
> 凡是本檔沒有寫出具體參數名稱的地方，都是刻意的 —— **不要自己編造旗標或參數名**。
> 若目標平台提供獨立的鏡頭運動選單或運動強度欄位，一律優先用那個欄位，欄位名稱與可用值以當下介面為準。

---

## 一、影片提示詞與靜圖提示詞的根本差異

### 影片提示詞的最小結構是三段，不是一段

| 段 | 回答什麼 | 缺了會怎樣 |
|---|---|---|
| 起始狀態 | 第 1 幀的構圖、主體位置、朝向、景別 | 模型自行決定開場，命中率低；接不上前一個鏡頭 |
| 過程中的變化 | 攝影機怎麼移動、主體做了什麼、速度多快 | **整段靜止**，只剩雲飄、髮絲抖、噪點浮動 |
| 結束狀態 | 最後 1 幀的構圖、主體位置、朝向、景別 | 動作做到一半停住，或在片長內來回做完好幾遍 |

三段之中最常被漏掉的是第三段。只寫 `she turns her head` 而不寫
`ends held on her face looking off-frame left`，模型不知道動作該在哪裡收，常見結果是轉回去再轉一次。

### 反例（把靜圖提示詞直接餵給影片模型）

```
A Taiwanese woman in her early thirties in a red wool coat, standing on a rain-slicked neon
street at night, medium shot at eye level, magenta shop sign as key from camera left, 50mm at
f/2, saturated magenta and green, crushed blacks, 2.39:1
```

這段話在生圖上是好提示詞，在影片上是壞提示詞。它沒有任何一個字描述變化，
模型只能把同一個狀態重複整段，你會拿到一張會下雨的照片。

### 正例（同一個畫面改寫成影片提示詞）

```
Opens on a Taiwanese woman in her early thirties in a red wool coat, rain flattening her short
hair to her forehead, both hands buried in her pockets, standing still under a shop awning on a
rain-slicked street, medium shot at eye level; over the full five seconds the camera pushes in
slowly on a dolly, physically moving forward about sixty centimetres so the perspective shifts
and the framing tightens to a medium close-up, while she lifts her head and turns to look
off-frame left; ends held on her face at chest height, jaw set, gaze off-frame; magenta shop
sign as the only key from camera left, the far side of her face two stops under, rain streaking
through the beam and reflections sliding across the wet asphalt behind her, 50mm at f/2, 24fps
with a 180 degree shutter, saturated magenta and green, crushed blacks, preserve natural skin
tone, 2.39:1
```

差異只有那三個結構句：`Opens on…` / `over the full five seconds… while…` / `ends held on…`。
光、色、鏡頭、畫幅這些槽位一個字都沒改 —— 靜圖那套技法在影片裡完全照用，
**只是需要在外面再包一層時間軸**。

注意這個正例同時通過了 `SKILL.md` 的〈輸出閘門〉：主體是具體名詞、有族裔、有頭髮狀態、
有手的明確狀態、有視線方向。**影片提示詞不能因為多了時間軸就放鬆主體描述** ——
主體寫得越糊，模型在後面幾秒把他重繪成別人的機率越高。

### 免費的環境動態（可加，但不能取代主體動作）

雨、雪、煙、霧、蒸汽、火焰、水面、風中的頭髮與衣料、窗簾、旗幟、遠處已在畫面內的人流、
車燈流動 —— 這些是模型相對最擅長、崩壞率最低的動態，成本極低，寫一句就讓畫面「活著」。
但它們是**背景動態**，不能當成第二段的「變化」：一段只有雨在下、人完全不動的片段，
觀眾讀到的仍然是靜止畫面。環境動態的用途是墊底，主體動作的用途是敘事，兩者都要有。

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
| 微手持 | `near-static frame with a faint handheld float, the framing drifting by about one percent of the frame width and never correcting` | 讓固定機位有人味而不失去穩定；訪談與對白的安全預設 | **低**。失敗率極低，是「不知道要用什麼運動」時的預設值 |
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

## 四、硬規則

1. **一個生成片段 ＝ 至多 1 個攝影機運動 ＋ 至多 1 個主體動作。**
   任一項超過一個就會失控：兩個相機運動 → 隨機漂移；兩個主體動作 → 兩個動作各做一半，
   或在片長內來回抽動。要兩個動作就分成兩個片段。
   **降級條款**：選了難度「高」或「中高」的相機運動（orbit、crane、dolly zoom、whip pan、
   crash zoom、空拍下降）時，主體動作降級成呼吸、眨眼、髮絲飄動這類微動作 ——
   算力要留給幾何，不要同時要求表演。

2. **單一片段內禁止出現剪接語彙。**
   禁用詞：`cut to`、`then the camera cuts`、`next shot`、`transition to`、`dissolve to`、
   `meanwhile`、`montage`、`intercut`、`split screen`、`flashback`，以及中文的「然後切到」「接著鏡頭轉向」。
   後果很具體：模型不會剪接，它只會在同一個連續空間裡「變形」過去 ——
   你會得到畫面撕裂、主體融解、場景在中途被重繪。
   **多鏡頭一律分次生成，剪接留給後製。**

3. **片長預算。** 常見的可選片長是 5s 與 10s，但**各平台與各版本提供的長度不同**
   （也有 4s、6s、8s，以及把片段接續延長的功能），下筆前先確認當下模型實際能選什麼，不要假設。

   | 片長 | 裝得下什麼 | 不要嘗試 |
   |---|---|---|
   | 5s | 1 個相機運動 + 1 個主體動作。分鏡時用「1s 安定 + 3s 動作 + 1s 收尾」當心理模型去配秒數（這是規劃用的切法，不是模型的內部行為） | 走完一整條走廊、完成一段對白、任何有起承轉合的事 |
   | 10s | 同一個動作放慢，或「1 個動作 + 該動作的餘韻」（走到定位後站定並轉頭） | 兩個獨立事件。片段越長，越後段的臉、服裝、場景越容易漂移 —— 這是連續性成本，沒有固定的秒數門檻，但方向是單調的：能用短的就用短的 |

   一個 30 秒的段落 = 6 個各負責一件事的 5 秒鏡頭，不是一段 30 秒生成。
   先寫分鏡表，再逐格寫提示詞。

4. **同段落的所有片段共用同一份「主體外觀 ／ 光 ／ 色 ／ 載體」文字，逐字複製貼上。**
   只更換運動、動作、景別與焦段光圈四個部分。
   主體外觀也必須逐字複製 —— 跨片段換臉、換衣服是影片工作流的頭號問題，
   而不同措辭的同義描述就足以觸發它。不這樣做的話，每個片段的色調與光位也會漂移，
   剪在一起會像好幾個不同的場景。

5. **幀率與快門必須明寫。**（快門角是否被精確執行依模型而定；但寫了至少不會拿到逐次不同的隨機糊度。）

   | 要什麼 | 提示詞 | 對應項目 |
   |---|---|---|
   | 電影標準動態模糊 | `24fps with a 180 degree shutter, one forty-eighth of a second per frame, natural motion blur on moving limbs` | `24 動態模糊` 的自然級 |
   | 最大限度的電影拖影 | `24fps with a 360 degree shutter, one twenty-fourth of a second per frame, limbs smearing into arcs` | `24 動態模糊` 的強化級。注意 1/24 秒仍遠短於 `03-framing.md` 靜圖 `24 動態模糊` 用的 1/15–1/4 秒 —— **影片裡拿不到靜圖那種長曝拖影**，別承諾使用者 |
   | 銳利無糊的頓挫感 | `24fps with a 45 degree shutter, one one-hundred-and-ninety-second of a second per frame, staccato stuttering motion with almost no blur between frames` | 配 `46 高對比` |
   | 抽格定格動畫 | `animated on twos: twelve distinct poses a second, each held for two frames inside a twenty-four frame per second timeline, every edge razor sharp with no motion blur, faint exposure flicker between poses` | `圖二 20 定格動畫質感`。與 `24 動態模糊` 互斥（見 `05-recipes.md` 表 B） |
   | 默片抽格 | `undercranked to sixteen to eighteen frames per second and played back at twenty-four, movement running roughly a third to a half faster than real time and slightly jerky, brightness flickering frame to frame` | `圖二 16 黑白默片` |
   | 慢動作 | `filmed at 96fps and played back at 24fps, four times slower than real time, very little blur on any single frame` | 與 `24 動態模糊` 互斥：幀率拉高等於每格曝光變短，拖影必然減少，二選一 |
   | 交錯掃描錄影 | `interlaced video with combing artefacts on every fast movement`（NTSC 區寫 `60i`，PAL 區寫 `50i`） | `圖二 14 數位早期`、`圖二 17 VHS 錄影帶` |

6. **首尾幀思維：能給首幀圖就給。**
   標準工作流是兩段式 ——
   (a) 先用 `05-recipes.md` 的靜圖組裝順序產出首幀圖（構圖、光、色、質感全部在這一步鎖死）；
   (b) 用該圖做 image-to-video，影片提示詞**只寫變化**。
   純文字 text-to-video 在構圖、光位與色彩上的命中率明顯低於 image-to-video，
   而且跨片段的一致性只能靠首幀圖來守。給了首幀圖之後：

   - **不要在影片提示詞裡重寫一次靜態描述**。文字與圖打架時，模型兩邊都做不好。
   - 只留：相機運動（含速度與幅度）、主體動作（含秒數）、結束狀態、幀率與快門。
   - 若模型支援首尾兩幀，把兩張都給，文字可以只剩速度詞（`even pace across the shot, no easing`）。

7. **一個片段只有一個空間、一個時間、一個光位。**
   片段內不可以改變地點、改變時段（黃昏變夜晚）、改變主光方向、改變主體數量。
   例外是**光源本身在動**：手電筒、車燈、旋轉警示燈、雲影 —— 這種要明寫「光源在動」，
   而不是寫「光線改變」。

8. **善用負面提示詞（模型支援時）。** 影片專屬的失效模式要指名，這不是堆砌詞：
   `morphing face, changing identity, extra limbs, warping background, sudden scene change,
   duplicated subject, text flickering`。
   模型若沒有負面提示詞欄位，就不要把這些字塞進正向提示詞 —— 那等於在要求它們出現。

9. **不要在畫面提示詞裡寫聲音。** 除非模型明確有音軌欄位，
   `we hear footsteps` 這類句子會被當成畫面內容處理，容易生出多餘的人或物。

10. **接不上就重生，不要靠後製救。** 兩個片段的主體長得不一樣時，
    正確做法是用同一張首幀圖（或前一片段的尾幀）重生，不是在剪接上加轉場遮掩。

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

| 風格 | 只有影片拿得到的特徵 | 影片提示詞補語 |
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

`SKILL.md` 把「攝影機運動 + 主體動作」合稱為影片的第 12 軸；
實際寫提示詞時要當成**兩條獨立的軸**各選一項，不要合併思考。

### 影片版組裝順序

取代 `05-recipes.md` 的靜圖十一槽，改用以下十四槽。
順序一樣是權重問題：時間性指令必須排在前段，排在句尾會被整段忽略。

```
1  主體與場景（起始狀態）
2  起始景別 + 相機高度 + 主體朝向
3  攝影機運動（1 個，含速度與幅度）
4  主體動作（1 個，含秒數）
5  結束狀態（結束景別 / 朝向 / 位置）
6  光位（含暗部落在哪）
7  光質
8  光源與色溫（＋光源本身的動態）
9  影調與對比
10 色彩
11 鏡頭焦距 + 光圈 + 焦點變化
12 幀率與快門角
13 質感 / 載體
14 風格總結 + 畫幅
```

槽 3–5 是影片專屬的三槽，也是唯一決定「會不會動」的三槽。它們必須連在一起寫成一個句群，
中間不要插入光線描述 —— 插入之後模型常把運動描述當成靜態場景的一部分。

### image-to-video 的縮短版（建議路徑）

給了首幀圖之後，槽 1、2、6–11、13、14 全部由圖承擔，文字只留四槽：

```
3  攝影機運動（含速度與幅度）
4  主體動作（含秒數）
5  結束狀態
12 幀率與快門角
```

範例：

```
Slow dolly push-in, the camera physically moving forward about sixty centimetres over the full
five seconds, perspective shifting as the framing tightens to a medium close-up; she lifts her
head and turns to look off-frame left over two seconds; ends held on her face, gaze off-frame,
rain still falling behind her; 24fps with a 180 degree shutter
```

### 完整範例：一段 20 秒的分鏡

**需求**：「夜裡的城市，一個人站在便利商店外，要港片的感覺，大概 20 秒。」

**共用技法（4 項）**：`圖二 13 港片霓虹`（風格包）+ `11 自發光` + `41 雙性照明` + `24 動態模糊`（180° shutter）
**逐鏡指定**：景別、焦段與光圈（近的兩鏡走 `25 淺景深`，遠的兩鏡收到中等景深，
避開 `05-recipes.md` 表 B 的「遠景 ↔ 淺景深」互相抵銷）

**共用文字**（四個片段逐字複製，一個字都不要改）：

```
A Cantonese man in his forties in a soaked grey nylon jacket, hair flattened to his forehead,
one hand closed around a cooling can of coffee, standing outside a convenience store on a wet
night street. Lit only by neon tubes and shop practicals, no white film light anywhere:
magenta raking one side of his face, jade green raking the other, an even 1:1 between the two
coloured sources, a dark band down the centre line where neither reaches. Coloured light
contaminating the skin uncorrected, preserve natural skin tone underneath, crushed blacks
tinted rather than neutral, heavy halation around every source, wet asphalt doubling the
signage, rain falling steadily, 35mm grain, 24fps with a 180 degree shutter, 1.85:1
```

（`41 雙性照明` 的三個條件在這段裡全部滿足：哪一側是哪個顏色、兩色交界在哪、兩者的強度關係
`an even 1:1` —— 這是 `圖二 13` 覆寫 `05-recipes.md` T41 例外條款預設值的地方，
港片霓虹要的是兩色等亮 + 中線暗帶，不是一側壓暗。）

| 鏡次 | 秒數 | 景別（起 → 訖） | 鏡頭 | 攝影機運動 | 主體動作 |
|---|---|---|---|---|---|
| 1 | 5s | `23 全身照` → `23 全身照` | `85mm at f/2.8, shot from across the road` | `locked-off tripod frame` | `he stands motionless under the awning, breathing, a passer-by already crossing the foreground and walking out of frame left` |
| 2 | 5s | `20 中景` → `19 近景` | `85mm at f/2` | `slow dolly push-in, about one metre, perspective shifting` | `he lifts his head and turns to look off-frame left over two seconds` |
| 3 | 5s | `32 特寫` → `32 特寫` | `100mm at f/1.4` | `rack focus from the rain on the glass thirty centimetres away back to his eyes` | `he blinks twice and exhales, the breath drifting up` |
| 4 | 5s | `23 全身照` → `21 遠景` | `85mm at f/2.8` | `locked-off tripod frame` | `he walks away from camera down the street until he is a small figure at the far end` |

**為什麼第 4 鏡不用 `dolly pull-out`**：那會讓相機後退與主體後退疊加成同方向的兩段位移，
尺寸變化過大、崩壞率高（見第二節寫法規則 6）。要收尾的「抽離感」，
讓主體自己走遠、機位不動，是同樣效果的低風險寫法。

四個片段分四次生成，剪接在後製完成。**沒有任何一個片段的提示詞裡出現 `cut` 或「然後」。**
