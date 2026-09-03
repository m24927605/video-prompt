## 输入依据

- **主操作**：文生视频，生成单个 8 秒动作镜头；无参考素材。
- **平台/模型**：未指定，因此采用平台中立写法。画幅、分辨率、帧率、种子及接口字段均保持未知，不虚构参数。
- **动作归属假设**：A 穿暗黄色雨衣，B 穿深蓝色雨衣；A 用左手抓 B 的右手腕。
- **声音假设**：仅现场雨声、鞋底摩擦、湿衣摆动、撞击和呼吸；无对白、无配乐、无字幕。
- **实践建议——过载处理**：
  - 保留完整的抓腕、挣脱、肩撞、后滑两步和对峙结果。
  - 删除 360° 环绕、快速推近、升至俯拍的组合。
  - 镜头只做约 30° 的平缓侧向弧移，全程保持两人全身可见。
  - “定格”改为人物停住约 1 秒、雨水继续运动。若需要真正静帧，应在后期冻结最后一个合格画面。

## 最终 Prompt

```text
[TASK]
Generate one continuous 8-second action shot on a rain-soaked rooftop. Exactly two adult people are present: A wears a heavy dark-yellow hooded raincoat; B wears a heavy dark-navy hooded raincoat. No other people, reflections shaped like extra people, weapons, punches, or kicks.

[SPACE AND FIRST FRAME]
A stands frame-left and B stands frame-right, facing each other on a clear horizontal action axis. Both full bodies and both pairs of feet remain visible. Leave open wet rooftop space behind A toward frame-left for two recovery steps. Low parapet walls, shallow puddles, steady wind-driven rain, overcast blue-gray daylight.

At the first frame they are already at close range. A’s left hand clearly encloses B’s right wrist. A’s other hand and B’s left hand remain separately visible. Their feet are planted in guarded staggered stances; neither person is already falling or moving backward.

[CAMERA]
A stable medium-wide full-body two-shot from waist-to-chest camera height. The camera performs one slow, smooth lateral arc of about 30 degrees around the pair during the shot, maintaining the same distance and keeping both complete bodies in frame. Track the midpoint between their torsos. No fast push-in, no crane rise, no overhead view, no full 360-degree orbit, no cuts, no slow motion, and no handheld shaking. The camera settles before the final face-off.

[ACTION — semantic pacing]
0.0–1.2 seconds:
Clearly establish A gripping B’s right wrist. B looks first at the grip, then at A’s upper chest. Both brace against the rain. The grip and correct hand ownership must be readable.

1.2–3.2 seconds:
B bends both knees slightly and lowers the center of gravity. B keeps the right elbow close to the right ribs, rotates the captured right hand toward the opening beside A’s thumb, and steps the left foot half a step inward toward A. B turns the hips and torso together toward A, using the hip rotation and elbow retraction to pull the right wrist cleanly out of A’s left hand. The wrist separates before the shoulder impact; no twisted joint, teleporting hand, or fused fingers.

3.2–4.6 seconds:
Continuing the same forward transfer of body weight, B plants the feet and drives the left shoulder once into A’s upper chest and shoulder line. It is one compact shoulder check, not a headbutt or tackle. Show brief raincoat compression at the contact point, then separation. A reacts only after visible shoulder contact.

4.6–6.9 seconds:
The impact sends A backward toward frame-left. A stays upright and recovers through exactly two distinct sliding steps: the rear foot skids through a shallow film of water and regains grip, then the other foot slides back and plants. Small water sprays outward from each sole. A’s knees flex, torso lags behind the hips from inertia, arms spread briefly for balance, then return to guard. A does not fall, kneel, spin, or take a third step. B does not chase or strike again.

6.9–8.0 seconds:
Both people finish upright, separated by roughly one arm’s length plus one step, facing each other with direct eyelines. A is balanced after exactly two backward steps; B remains planted after the shoulder check. They hold the face-off pose until the cut while breathing visibly. Their bodies stop advancing, but rain, dripping sleeves, and settling raincoat hems continue moving naturally.

[PHYSICS AND MATERIAL]
The rooftop is wet and slippery but not frictionless. Rubber soles alternately lose and regain traction; feet do not glide like ice skates. B’s planted foot must visibly support the hip turn and shoulder drive. A’s backward motion begins at the shoulder contact and travels through the torso into the legs.

Both raincoats are saturated and heavy: fabric clings around shoulders and torso, folds compress during the grab and impact, and coat hems lag behind the hip turn before swinging and settling from inertia. Do not make the coats float like thin capes. Rain splashes from shoulders and boots; puddles ripple under steps. Keep wind direction and rainfall direction consistent throughout.

[AUDIO]
Only natural location sound: steady rooftop rain, water striking raincoat fabric, two distinct wet rubber sole scrapes during A’s recovery, one muted cloth-covered shoulder impact, fabric strain, and restrained breathing. No dialogue, no music, no subtitles.

[END STATE]
Exactly two people remain visible. A and B are upright, separated, and facing each other. A has completed exactly two backward sliding steps without falling. B’s right wrist is free. There is no continuing body contact. The camera is steady; only rain, dripping water, breathing, and the last settling motion of the heavy raincoats continue.
```

## 验收检查

- A 左手抓住的是 B 右腕，挣脱前后归属不交换。
- 顺序清楚：先脱腕，后肩部接触，再出现 A 的位移。
- 肩撞只有一次，不变成推掌、头槌、擒抱或连续攻击。
- A 恰好后退两步，每一步都有失去摩擦、滑动、重新着地的过程。
- A 全程没有倒地、跪地、转圈或滑出画面。
- B 的支撑脚、降重心和转髋能解释冲量来源。
- 湿雨衣有重量、压缩、延迟摆动和逐渐停止的表现。
- 镜头只有一次小幅弧移，没有推近、升高、俯拍或 360° 环绕。
- 最后一秒人物对峙停住，但雨水和衣摆不被错误地完全冻结。

## 主要失败风险

- 抓腕处可能出现手指融合、左右手互换或脱腕过程被跳过。
- “湿滑”可能被夸张成无摩擦滑冰，导致 A 连续漂移。
- 肩撞可能被模型改写成双手推搡或头部碰撞。
- 即使只是小幅弧移，也可能与复杂接触动作争夺稳定性。
- 生成式“定格”可能让雨水一起停住；真正冻结画面更适合后期完成。

## 有限修订阶梯

1. **若身体接触或脚步物理失败**：只把相机改为完全固定，其余 prompt、时长和动作不变。若动作因此通过，说明主要冲突来自镜头运动。

2. **若抓腕归属仍错误**：保持固定镜头和全部动作，只增加一张简洁动作几何图或首帧姿势参考——如果所选平台明确支持该输入角色。参考只控制人物位置、左右手和接触点，不继承人物外观。

3. **若动作合格但最终停驻失败**：不重新生成主体动作，直接在后期选取最后一个清晰对峙帧做短暂静帧，并叠接连续雨声。

若在锁定相机和明确接触几何后，仍反复出现同一种手腕或肩部拓扑错误，应停止继续加长 prompt，改为两个镜头或动作预演参考路线。
