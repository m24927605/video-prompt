已讀完所需參考，直接交付。說明一點：這個工作階段沒有 Write 工具，無法建立計畫檔，所以完整方案直接呈現在這裡。

## 1. 輸入基礎

- **任務**：純文字生成（text-to-video）、單一鏡頭、8 秒、無任何參考圖／影片／音訊。
- **平台／模型**：未定 → prompt 寫成**平台中立**版本；Seedance 2.0、UI 標籤「Seedance 2」、Seedance 2.5、第三方平台的行為不互通，本稿不預設任何一方的參數。知識存檔日期 2026-08-22，實際可用時長、比例、音訊、首幀功能以你選定平台的當下文件為準。
- **已驗證的執行參數**：無（尚未選平台）。
- **假設**（可直接用，不需回覆）：無對白；16:9 橫式；「有人拿走」用遠景背影＋紅傘遠去呈現；不含品牌與可辨識文字；中文為主稿、附英文同義版。
- **未知**：8 秒是否為該平台可選檔位、是否原生生成音訊、prompt 長度上限、是否支援首幀圖。

## 2. 最終 Prompt（中文版，直接貼上）

```text
生成一段 8 秒、單一連續鏡頭、真人實拍質感的電影畫面。沒有對白、沒有字幕、沒有配樂。

場景：深夜下雨的便利店門口。鏡頭位於人行道上，以約 3/4 的斜角對著店面：發著冷白光的自動玻璃門在畫面右側中景，門上方有一道窄雨遮，雨遮邊緣滴著一道細細的水簾。門的左側靠牆放著一個金屬傘架，裡面只有兩把傘：一把收起的黑色長傘、一把透明傘，傘架裡沒有紅色的傘。畫面左側是濕亮的人行道往景深深處延伸，路面反射著暖色街燈與霓虹的散景，雨絲在逆光中清楚可見。玻璃門後只看得到貨架和燈光，沒有店員或顧客。店招與燈箱只是白色或淡藍色的光面，沒有任何可辨識的文字或品牌標誌。

人物：全片只有兩個人。（1）主角：二十出頭的女生，黑色及肩直髮，米白色針織外套、深色牛仔褲、白色帆布鞋，左手提著一個小小的半透明塑膠購物袋。（2）畫面左側遠處人行道上的一個路人：深色雨衣、背對鏡頭、全程看不到臉，撐著全片唯一的紅色物件——一把撐開的紅色長柄傘。這個路人一直往遠處走，從頭到尾不回頭、不停步、不靠近。

鏡頭：中景、略低於視線高度、35mm 鏡頭感、淺景深，焦點全程在女生臉上。唯一的運鏡是極慢的向前推進，從中景推到中近景，最後兩秒停住不動。

第一格畫面：自動門正「叮」一聲滑開，女生已經站在門口跨出第一步，左手提著袋子。傘架（黑傘＋透明傘）在畫面左下；紅傘已經在畫面左側遠景的人行道上。

0–2 秒：她走出來停在雨遮下，抬眼看了一下雨，右手憑習慣往畫面左下方的傘架伸過去，眼睛還沒看傘架。
2–4 秒：右手在傘架邊緣撲了個空，手指停住。她的視線這時才落到傘架上：只有黑傘和透明傘。她微微彎腰，用手把兩把傘撥開確認一次，呼吸停了一拍。門在她身後滑上。
4–6 秒：她直起身，從鼻子緩緩呼出一口氣。目光從傘架慢慢抬起、轉向畫面左側的雨中——遠處人行道上，那把紅傘正在走遠，被雨和散景暈成一團柔和的紅色。
6–8 秒：她站在雨遮邊緣不動，雨水在她面前一掌寬的地方落下。左手握緊袋子提把、薄塑膠袋輕微皺響；右手垂在身側、掌心微張。嘴唇微微張開但沒有說話。紅傘縮成遠處一個小紅點，人影始終背對。鏡頭停在她的中近景。

光線：主光是店內透過玻璃門灑出的冷白光，從她右後方打來；畫面左側的街燈與霓虹在她左臉勾出一層暖橘色邊光，形成左暖右冷的臉部分光。濕地面同時反射這兩種光。門關上後冷光略減，其他光線不變，沒有閃電、沒有燈光閃爍。

質感：細微膠片顆粒、深沉的黑、高對比，寫實，不是卡通或動畫。

聲音：持續的雨聲、雨遮滴水聲、遠處濕路面的車流聲；開頭自動門的提示音和滑門聲；店內嗡鳴隨門關上而變小；第 4–5 秒一聲清楚的呼氣。沒有對白、沒有音樂、沒有字幕。

結尾畫面：女生在畫面中央偏右的中近景，目光鎖定畫面左側的雨中；左下角傘架裡仍是兩把傘；紅傘仍在左側遠景持續遠去；門已關上；鏡頭靜止。
```

### 英文同義版（平台對英文較穩時使用）

```text
Generate an 8-second, single continuous shot, photoreal live-action cinematic clip. No dialogue, no subtitles, no background music.

Scene: the entrance of a convenience store late at night in the rain. The camera sits on the sidewalk at roughly a 3/4 angle to the storefront: the automatic glass door, glowing cold white from inside, is on frame-right in the mid-ground, with a narrow eave above it; a thin curtain of water drips off the eave's edge. A metal umbrella stand sits against the wall just left of the door, holding only two umbrellas: one folded black long umbrella and one clear umbrella — no red umbrella in it. On frame-left the wet sidewalk runs away into depth, reflecting warm street lights and neon bokeh; rain streaks are clearly visible against the backlight. Through the glass only shelves and light are visible — no staff or customers. The signage and lightbox are plain white or pale-blue light panels with no readable text or brand logos.

People: exactly two people in the entire shot. (1) The protagonist: a woman in her early twenties, straight black shoulder-length hair, cream knit cardigan, dark jeans, white canvas sneakers, a small translucent plastic shopping bag in her left hand. (2) A passer-by far down the sidewalk on frame-left, in a dark raincoat, back to camera, face never visible, holding the only red object in the shot: an open red long-handled umbrella. The passer-by keeps walking away into the distance and never turns, stops, or approaches.

Camera: medium shot, slightly below eye level, 35mm lens feel, shallow depth of field, focus stays on the woman's face throughout. The only camera move is a very slow push-in from medium shot to medium close-up, settling and holding still for the last two seconds.

First frame: the automatic door is sliding open with a soft chime; the woman is already in the doorway taking her first step out, bag in her left hand. The umbrella stand (black + clear umbrella) is in lower frame-left; the red umbrella is already far down the sidewalk in the background on frame-left.

0–2 s: she steps out under the eave and stops, glances up at the rain, and out of habit her right hand reaches down toward the umbrella stand on frame-left without her looking at it.
2–4 s: her hand closes on empty air at the rim of the stand and her fingers stop. Only now does her gaze drop to the stand: the black umbrella and the clear one. She leans down slightly and parts the two umbrellas with her hand once to check; she holds her breath for a beat. Behind her, the door slides shut.
4–6 s: she straightens up and slowly exhales through her nose. Her eyes lift from the stand and turn toward frame-left, into the rain — far down the sidewalk, the red umbrella is walking away, blurred by rain and bokeh into a soft red shape.
6–8 s: she stands still at the edge of the eave; rain falls a hand's width in front of her. Her left hand tightens on the bag handles and the thin plastic crinkles; her right hand hangs at her side, palm slightly open. Her lips part slightly but she says nothing. The red umbrella shrinks to a small red dot; the figure never turns. The camera holds on her medium close-up.

Light: the key light is the cold white store light spilling through the glass door from her right-rear. Warm orange street light and neon from frame-left rim her left cheek, giving a warm-left / cool-right split on her face. The wet pavement reflects both. After the door closes the cold spill dims slightly; no other light change, no lightning, no flicker.

Look: fine film grain, deep blacks, high contrast, realistic, not cartoon or anime.

Sound: steady rain, water dripping from the eave, distant tire hiss on the wet road; the automatic door chime and sliding sound at the start; the store's interior hum fades as the door closes; one clear exhale around 4–5 s. No dialogue, no music, no subtitles.

End frame: the woman in medium close-up, center-right, gaze locked on frame-left into the rain; the umbrella stand in lower frame-left still holding two umbrellas; the red umbrella still receding in the far background on frame-left; the door closed; the camera static.
```

### 到平台上要另外設定的參數（不在 prompt 文字裡）

- 時長：8 秒。若平台沒有 8 秒檔位，選最接近的；prompt 裡的秒數是**語意節拍**，不是精準時長鎖定。
- 比例：16:9（若平台提供 21:9 且你想要更電影的寬幅，可選，但未驗證）。
- 解析度、音訊開關、seed：依平台，未知；不要假設有獨立的負面提示欄位。
- 若平台沒有原生音訊，直接刪掉「聲音」整段，後期再補雨聲與配樂。
- 若有字數上限，刪減順序：質感 → 聲音 → 光線細節；**不要刪**人數／紅傘唯一性／空間方位／結尾畫面。

## 3. 驗收檢查（逐項是／否）

1. 全片恰好 2 人：女生＋遠景背影；無其他行人、無店員。
2. 全片恰好 1 把紅傘，只在遠景路人手上；傘架裡只有黑傘＋透明傘，沒有紅色。
3. 紅色只出現在紅傘上（衣著、招牌皆無紅）。
4. 空間：門在右、傘架在左下、人行道往左側景深延伸；她右手伸向畫面左下；視線先向下（傘架）再抬向畫面左遠景——同一軸線。
5. 因果鏈可見：伸手 → 撲空 → 低頭確認 → 直身呼氣 → 抬眼看見遠處紅傘 → 定住。
6. 表演可見：手指停住、撥傘確認一次、一次鼻呼氣、左手握緊袋子、唇微張但無話。
7. 鏡頭：單一緩慢推進、最後兩秒靜止；焦點在臉；無環繞、無變焦跳動。
8. 光：左暖右冷分光；雨絲逆光可見；無閃電、無閃爍。
9. 門：開頭滑開、中段關上、之後保持關閉。
10. 音訊（若有）：雨聲持續、門音、一次呼氣；無對白、無 BGM、無字幕——要實際聽過，播放圖示不算證據。
11. 結尾：她中近景、目光向左、紅傘仍在遠處、鏡頭靜止，可直接接下一鏡。
12. 畫面中沒有可辨識文字或 logo。

## 4. 失敗風險（無成功保證）

- **紅傘重複**：傘架裡同時出現紅傘，或女生手上憑空多一把傘（最高風險）。
- 遠景路人轉身、走向鏡頭、或膨脹成第二主角；人數增加。
- 店招生成亂碼文字或品牌 logo。
- 手與傘架接觸處穿模、傘數量在撥動時變動。
- 自動門異常（不關、反覆開關）。
- 推進鏡頭變成環繞或變焦。
- 雨被畫成雪、雨量大到遮臉、水簾位置錯。
- 節拍漂移：8 秒內事件多，後段可能被壓縮或提前。
- 女生身分／衣著在推進中漂移（淺景深＋雨偶發）。

## 5. 修改階梯（每次只動一個變數；未經實測，為預先規劃）

1. **紅傘重複** → 只改「人物」段：刪掉遠景路人，改為「紅傘不在畫面中，傘架有一個空位」；其餘不動。仍失敗 → 拆成兩鏡（本鏡＋紅傘遠去的插入鏡）。
2. **路人轉身／靠近** → 只改路人描述：「已在景深最深處，只剩模糊的紅色色塊，人形幾乎不可辨」。
3. **手部／傘架穿模** → 只改鏡頭為「固定機位、不推進」。仍失敗 → 只刪「撥開兩把傘確認」這一個動作。
4. **文字／logo 亂碼** → 只改場景：「店招在畫面外，只見燈光溢出；玻璃門上沒有貼紙」。
5. **鏡頭變環繞／變焦** → 只改運鏡句為「固定機位」，推進感改由後期裁切模擬。
6. **表演平淡** → 只加一個延遲：「撲空後停兩拍才低頭」；仍平 → 拆出反應特寫第二鏡。
7. **雨型錯** → 只改雨的描述：「細密的雨，逆光呈銀色細線；雨遮邊緣一條連續的水線」。

**停止／改道條件**：同一硬缺陷在對應的單變數修改後仍重現，就停止重試，改為拆鏡，或（若平台支援首幀圖）先生成一張「第一格畫面」的靜圖鎖定版面，再做圖生影片。

---

**回顧**：依 seedance-prompt-director 規範產出一支平台中立、8 秒單鏡頭的可用 prompt（中文主稿＋英文同義版），核心設計是「伸手撲空 → 低頭確認 → 抬眼看見紅傘遠去」單一因果事件，配合左暖右冷分光與單一緩慢推進營造電影感；紅傘唯一性、人數、方位軸線與結尾畫面都已明確鎖定。附上平台參數清單、12 項驗收、風險與單變數修改階梯。你選定平台後，只需設定時長／比例／音訊，貼上 prompt 即可生成；若產出有缺陷，可把影片或截圖交給 seedance-video-qc 診斷後再回來做有界修改。
