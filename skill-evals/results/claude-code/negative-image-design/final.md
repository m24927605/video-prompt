完成。這是平面設計海報而非攝影場景,所以我沒有套用光位、景深等攝影軸,而是以「平面正面構圖 + 亮調」的邏輯組裝:平塗、無陰影、無縱深,讓白底讀成一整塊乾淨色面。

## Prompt(直接可用)

```
A minimalist Swiss-design graphic poster, square format, on a pure flat white
background. A single solid orange circle, flat color with no gradient, no
shadow and no outline, placed slightly above the center of the composition.
Below the circle, the word "MONDAY" in black, set in a bold geometric
sans-serif typeface, all uppercase, wide even letter-spacing, horizontally
centered. Strict grid alignment, generous white negative space, only two
colors on white: vivid orange and pure black. Flat vector-style rendering
with crisp clean edges, International Typographic Style, print poster
aesthetic, no texture, no depth, no additional elements.
```

## 各段在控制什麼

- **開頭三句**先鎖定主體與版面:方形、白底、橘圓在中心偏上、標題在下方置中。生成模型對排版的服從度靠這種明確的相對位置描述,不靠風格詞。
- **字體描述**用 `bold geometric sans-serif, all uppercase, wide even letter-spacing` 展開「無襯線標題」,比只寫 sans-serif 更接近瑞士風格的 Helvetica/Akzidenz 氣質(依本 skill 規則,不寫特定字體或設計師名,展開成技術描述)。英文單字 MONDAY 入畫的成功率不錯,但字距與筆畫偶爾仍會歪,多抽幾張挑字最正的。
- **`flat color / no gradient / no shadow / no texture / no depth`** 是這張圖的關鍵防線:模型很容易自作主張幫圓形加漸層、投影或紙張紋理,必須在正文裡明講排除,才能得到真正的平塗色面。
- **`International Typographic Style` + `print poster aesthetic`** 收尾當風格總結,把前面的具體指令歸攏到瑞士國際主義排版傳統。

## 可調的旋鈕(一次只改一項)

- 想要更典型的瑞士不對稱版面:把 `horizontally centered` 改成 `left-aligned on the grid, in the lower third`,圓形改 `in the upper right quadrant`。
- 想指定橘色色感:把 `vivid orange` 換成 `warm red-orange` 或 `bright tangerine orange`。
- 想加一行小字副標:在 MONDAY 句後加一句描述其位置與相對大小,但極簡風格下建議維持單一元素層級。
