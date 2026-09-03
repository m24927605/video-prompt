# Video Prompt cross-agent skills

本專案提供五個共用 canonical skills；Codex 與 Claude Code 透過各自的 project-local symlink 讀取同一份內容。

| Skill | 用途 | Codex | Claude Code |
|---|---|---|---|
| `screenplay-writer` | 開發、規劃、撰寫、續寫、審查或重寫短片／長片電影劇本，支援 Fountain、角色聲紋、觀眾知識與連戲追蹤 | `$screenplay-writer` | `/screenplay-writer` |
| `photography-aesthetics` | 為圖片 prompt 或影片 visual-look／motion 子契約設計光線、鏡頭、構圖、色彩與質感，並可逆向分析照片；不擁有完整影片 prompt | `$photography-aesthetics` | `/photography-aesthetics` |
| `seedance-prompt-director` | 撰寫、審核或修復單鏡／單 clip 的完整 production-ready Seedance／AI 影片 prompt contract，包含 task、reference、blocking、物理、表演、聲音與 end state | `$seedance-prompt-director` | `/seedance-prompt-director` |
| `seedance-film-producer` | 規劃多鏡、短片、系列或長片的資產、continuity、佇列、版本、剪輯與完成流程 | `$seedance-film-producer` | `/seedance-film-producer` |
| `seedance-video-qc` | 依影片、截圖、時間碼或失敗紀錄檢查 adherence、continuity、物理、表演、影音與剪輯可用性 | `$seedance-video-qc` | `/seedance-video-qc` |

五個 skills 都支援 description-based automatic invocation。

最短範例：

```text
$screenplay-writer 把這個台灣家庭劇 premise 發展成 sequence map，先不要寫正文。
$photography-aesthetics 只把這個雨夜片段整理成可嵌入影片 prompt 的 visual-look 子契約。
$seedance-prompt-director 把這個 8 秒雨夜單鏡 brief 寫成含 reference、動作、聲音與驗收條件的完整 prompt。
/seedance-film-producer 為這部 12 分鐘短片建立 continuity 與 shot queue。
$seedance-video-qc 依 00:00、00:04、00:08 的證據診斷這支失敗影片。
```

Skills 會以使用者語言回答。`screenplay-writer` 不承諾 AI detector 分數，改以原創性、可拍性、可演性、角色聲音與作者意圖保真作為驗收標準。`photography-aesthetics` 的圖片提示詞預設使用英文、說明使用繁體中文；影片 visual-look 只作為交給 `seedance-prompt-director` 的子契約。未指定的畫幅、時長、解析度、格式或 provider 欄位不得由美學 skill 補預設值。若詢問「目前／最新」模型能力或參數，應先核對實際平台的現行官方文件。Seedance 研究知識封存日為 2026-08-22。
