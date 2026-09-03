Prompt 已完成。這張是平面向量式海報而非攝影，所以攝影軸大多不適用；我採用「有限色盤正面列舉＋逐句封口」的寫法，並把每個否定句貼在它守護的肯定句後面（例如圓形最容易被模型畫成有陰影的 3D 球體，就在描述圓形的那句直接關掉）。

## 可直接使用的 Prompt

```
A minimalist Swiss-style graphic design poster in a square composition, flat vector
artwork on a plain solid white background. One large solid orange circle, perfectly
round with a crisp sharp edge, placed above the center line and offset toward the
right; the circle is a single flat uniform orange fill, not a gradient and not a
shaded 3D sphere, and it casts no shadow on the white background. The single word
MONDAY, spelled exactly M-O-N-D-A-Y in bold black grotesque sans-serif capitals,
set on one straight horizontal baseline in the lower left of the poster, letters
evenly spaced, edges sharply rendered like printed type, not hand-drawn lettering.
The poster contains exactly three elements — the white background, the orange
circle, and the black MONDAY headline — and nothing else anywhere in the frame.
Clean flat print finish, perfectly even illumination across the whole poster with
no vignette, no paper texture, and no border line around the edge.
```

## 設計說明與可調的槽位

- **版面**：我做了一個具體決定 —— 圓形置於中線上方偏右、標題落在左下，這是瑞士國際主義風格典型的非對稱網格配置。只寫「minimal Swiss design」而不給位置，模型會自己亂擺。若你偏好**正中對稱**的莊嚴感，把位置句改成 `the circle dead center on the vertical axis, the word MONDAY centered directly below it`。
- **文字**：拼字逐字母寫死（`spelled exactly M-O-N-D-A-Y`）是為了壓低生成文字時多字母、缺字母的機率；英文單一短詞成功率高，但仍建議多抽幾張挑字最乾淨的。
- **封口句**：「exactly three elements … and nothing else anywhere in the frame」是正面列舉後當場封口，防止模型自己加裝飾線條、副標或雜訊。
- **橘色深淺**：目前留給模型決定。想鎖定色相可在 orange 前加形容，例如 `warm red-orange` 或 `bright tangerine orange`；若有品牌色票，直接寫十六進位色碼（如 `orange (#F25C05)`）多數模型也能大致貼近。
- **圓形大小比例**：想更精確可加一句 `the circle's diameter spanning about half the width of the poster`。

要改動時一次只改一個槽位再重生，才能判斷差異來自哪裡。
