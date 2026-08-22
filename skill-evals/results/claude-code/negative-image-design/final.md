目錄裡只有三個 Seedance **影片** skill，沒有靜態圖的範本。你的需求明確是靜態海報、排除運鏡/聲音/時間軸，所以我不套用那些 skill（它們會硬塞 camera、blocking、audio、end state 等影片欄位），直接給你圖片生成 prompt。

## 主 Prompt（英文，適用 Midjourney / Flux / SD / Ideogram / DALL·E）

```
Minimalist Swiss International Typographic Style poster, square 1:1 format.
Pure flat white background (#FFFFFF).
One single large solid orange circle (#FF5A1F), perfectly round, flat color, no gradient, no shadow, no outline, positioned off-center in the upper-right area on a strict modular grid.
The word "MONDAY" in bold black Helvetica-style grotesque sans-serif, all uppercase, tight letter-spacing, flush-left aligned in the lower-left of the grid, crisp vector edges.
Generous negative space, asymmetric balance, exactly three colors: white, black, orange.
Clean, precise, geometric, print-quality flat graphic design, vector illustration look.
No other text, no textures, no gradients, no shadows, no 3D, no noise, no watermark.
```

## Negative Prompt（支援的模型用）

```
gradient, shadow, 3D, texture, paper grain, photo, photorealistic, extra text, misspelled text, watermark, logo, border, frame, multiple circles, extra shapes, decorative elements, noise, blur, low quality
```

## 參數建議

- **比例**：`1:1`（例如 1024×1024 或 2048×2048）
- **Midjourney**：結尾加 `--ar 1:1 --style raw --stylize 50 --no gradient shadow texture`
- **Ideogram / Flux**：文字渲染較穩，保留 `"MONDAY"` 的雙引號並加 `text: MONDAY`；若字拼錯，加一句 `the only text in the image is the word MONDAY`
- **SD / Flux**：CFG 5–7，避免過度風格化把圓形畫出立體感

## 可調的地方

- **佈局**：把「upper-right / lower-left」換成 `circle centered, title below` 就變成對稱置中版
- **橘色**：`#FF5A1F` 偏暖；想要更 Swiss 經典感可用 `#FF6600`
- **字體**：`Helvetica-style` 可改成 `Akzidenz-Grotesk-style` 或 `Neue Haas Grotesk-style`

---

**小結**：我檢查過目錄，只有影片用的 Seedance skill，跟靜態海報無關，所以沒套用。上面是一組完整可直接貼用的靜態圖 prompt：主 prompt + negative prompt + 1:1 參數與各模型微調建議。如果你告訴我要用哪個模型，我可以幫你把 prompt 收斂成該模型的最佳長度與語法。
