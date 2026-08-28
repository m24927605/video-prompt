# Video Prompt cross-agent skills

本專案提供四個共用 canonical skills；Codex 與 Claude Code 透過各自的 project-local symlink 讀取同一份內容。

| Skill | 用途 | Codex | Claude Code |
|---|---|---|---|
| `photography-aesthetics` | 把模糊的視覺需求翻譯成可控的攝影／電影美學提示詞，或逆向分析既有照片的光線、鏡頭、構圖、色彩與質感 | `$photography-aesthetics` | `/photography-aesthetics` |
| `seedance-prompt-director` | 撰寫、審核或修復單鏡／單 clip 的 production-ready Seedance／AI 影片 prompt | `$seedance-prompt-director` | `/seedance-prompt-director` |
| `seedance-film-producer` | 規劃多鏡、短片、系列或長片的資產、continuity、佇列、版本、剪輯與完成流程 | `$seedance-film-producer` | `/seedance-film-producer` |
| `seedance-video-qc` | 依影片、截圖、時間碼或失敗紀錄檢查 adherence、continuity、物理、表演、影音與剪輯可用性 | `$seedance-video-qc` | `/seedance-video-qc` |

四個 skills 都支援 description-based automatic invocation。

最短範例：

```text
$photography-aesthetics 把這個雨夜人像構想整理成適合 GPT Image 2 的電影感提示詞。
$seedance-prompt-director 把這個 8 秒雨夜單鏡 brief 寫成可驗收 prompt。
/seedance-film-producer 為這部 12 分鐘短片建立 continuity 與 shot queue。
$seedance-video-qc 依 00:00、00:04、00:08 的證據診斷這支失敗影片。
```

Skills 會以使用者語言回答。`photography-aesthetics` 的提示詞預設使用英文、說明使用繁體中文；若詢問「目前／最新」模型能力或參數，應先核對實際平台的現行官方文件。Seedance 研究知識封存日為 2026-08-22。
