# Seedance Cross-Agent Skills Goal

## 1. 單一目標

在目前專案中建立一套 production-ready、可攜、可維護，且能被 Codex CLI 與 Claude Code 原生發現與使用的 Seedance／AI 電影製作 skills。

核心目的不是把既有研究全文塞進 prompt，而是將已完成且通過獨立 QA 的研究，提煉成 AI agent 能在實際任務中正確套用的決策規則、工作流、模板、診斷方法與證據邊界。

完成後，無論使用 Codex 或 Claude Code，agent 都應能：

1. 將模糊創意需求轉成精確、可控、production-ready 的 Seedance 2.5／AI 影片 prompt。
2. 正確處理角色、場景、道具、reference mapping、blocking、鏡頭、光線、動作物理、表演、聲音、時間節奏、首尾狀態與驗收條件。
3. 規劃長篇電影的 creative bible、資產、continuity state、sequence／scene／shot、生成佇列、版本、剪輯、聲音與 QC。
4. 分別提供品質最大化、速度最大化但守住門檻，以及推薦混合流程。
5. 根據影片、截圖、時間碼或失敗描述做 prompt adherence、continuity、temporal stability、physics、acting、camera、audio 與剪輯可用性診斷。
6. 每次 iteration 只修改最少必要變因，並能說明為何修改。
7. 嚴格區分官方事實、專案直接觀察、作者自述、團隊推論、實務建議與 unknown。
8. 不把 Seedance 2.0、UI 顯示的 Seedance 2、版本不明案例或 Higgsfield 平台能力錯誤歸因到 Seedance 2.5。
9. 不捏造 negative-prompt 欄位、reference limits、seed 決定性、成本、速度、解析度、API 參數或成功保證。

現行規格基準：

- OpenAI／Codex Skills：<https://learn.chatgpt.com/docs/build-skills>
- Claude Code Skills：<https://code.claude.com/docs/en/slash-commands>

開始實作前必須重新核對上述官方文件的當前版本；不得把本文件記錄的路徑或行為永久視為不會變動。

## 2. 執行配置

所有主代理、子代理與獨立 reviewer 都必須使用執行環境實際可提供的最高能力模型與最高 reasoning／effort：

- 在 Codex 執行時：使用 `gpt-5.6-sol`、`reasoning_effort="ultra"`。
- 在 Claude Code 執行時：先以官方文件與本機 CLI status/config 確認當前實際可用的最高能力 Claude 模型與最高 effort／extended-thinking 設定，記錄精確 model identifier；不得猜測或靜默降級。
- 若任何必要角色無法使用最高配置，記錄實際狀態，不得宣稱符合要求。

建立主代理＋3 位 Staff 等級以上的獨立角色：

1. **Research Distiller**：完整閱讀研究成果，建立知識與來源映射。
2. **Cross-platform Skill Architect**：設計 Agent Skills 架構、progressive disclosure 與可攜性。
3. **Codex／Claude Compatibility Engineer**：分別驗證兩個 host 的 discovery、invocation、path 與 metadata。
4. **Adversarial Evaluator**：由主代理或獨立 reviewer 擔任；用未提示預期答案的 held-out cases 嘗試讓 skills 失敗。

若執行環境支援真正的 subagents／agent teams，必須使用；若不支援，必須以 fresh isolated CLI sessions 做獨立 pass。不得讓任何代理單獨驗收自己撰寫的 skill。避免多人同時修改相同檔案。

## 3. 必讀研究來源

逐份完整閱讀下列最終產物，不得只搜尋關鍵字或讀摘要：

- `research/seedance-2.5/research-report.md`
- `research/seedance-2.5/prompt-playbook.md`
- `research/seedance-2.5/long-form-film-workflow.md`
- `research/seedance-2.5/higgsfield-nine-projects.md`
- `research/seedance-2.5/creative-bible-analysis.md`
- `research/seedance-2.5/future-evaluation-plan.md`
- `research/seedance-2.5/additional-findings.md`
- `research/seedance-2.5/qa-report.md`
- `research/seedance-2.5/source-manifest.json`
- `seedance2.5-prompt-guide.md`

必要時才回查：

- `research/seedance-2.5/higgsfield/projects/*.json`
- `research/seedance-2.5/higgsfield/media-inventory.json`
- `research/seedance-2.5/browser-evidence/`
- `research/seedance-2.5/sources/`
- `seedance-25-creative-bible.pdf`

不要重新進行原始研究、重新播放全部影片或重新下載所有來源；既有研究已通過 freeze-state QA。只有發現具體矛盾時才回查原始證據。

研究截止日為 2026-08-22。Skills 若被問到「目前、最新、現在支援什麼」等時效性問題，必須先查最新官方文件；無法查證時應說明 archived knowledge date，不得把研究內容永久視為最新事實。

## 4. 目標 Skill Suite

預設建立三個彼此聚焦的 skills。只有在設計 review 證明其他切分更簡單時才能調整。

### 4.1 `seedance-prompt-director`

適用於撰寫、重構、審核或修復 Seedance／AI 影片 prompt。

必須能：

- 先辨識 task type、平台、模型版本與 input mode。
- 取得必要但最少的澄清資訊；不因小缺口停止工作。
- 使用下列 production schema：

  `intent/context`
  → `exact entities`
  → `active references and roles`
  → `location/spatial map`
  → `first frame/blocking`
  → `format/duration`
  → `optics/camera`
  → `timecoded action beats`
  → `physics/contact/inertia`
  → `observable acting`
  → `lighting/color/material`
  → `audio/dialogue/SFX`
  → `style`
  → `positive constraints`
  → `end state`
  → `acceptance criteria`

- 為每個 reference 明確指定角色，不讓模型自行猜用途。
- 區分 identity、location、style、motion、audio、first/last frame 與 diagram reference。
- 將 emotion adjective 轉成可觀察的 gaze、breathing、gesture、tempo、tactic 與 state change。
- 提供 final prompt、輸入假設、已證實參數、unknown、驗收點、失敗風險與一次只改一個變因的 revision ladder。
- 不把 prompt 寫得越長就當成越好；過載時拆 shot／beat／action。

### 4.2 `seedance-film-producer`

適用於短片、系列、長篇電影與多鏡頭 continuity production。

必須能：

- 將概念拆成 world／treatment／script／sequence／scene／beat／shot。
- 建立 character、wardrobe、injury、prop、location、weather、light、voice、behavior 與 camera-language passports。
- 把每個角色／場景狀態建成獨立、不可覆寫的版本。
- 建立 shot handoff、first/last anchor、screen direction、eyeline、action end state 與 continuity ledger。
- 提供 asset registry、shot manifest、命名規則、版本、retry log、selection lineage、checkpoint 與 rollback。
- 規劃 coverage、rough cut、pickup、fine cut、cleanup、VFX、color、sound、ADR、music、subtitle 與 mastering。
- 提供三種明確模式：
  - quality-max
  - speed-max-with-floor
  - recommended hybrid
- 使用 first-pass approval rate、retries、usable seconds/hour、cost per approved second、artifact rate、continuity、prompt adherence 與人工修正時間作 KPI。
- 明確指出長片不是靠一個超長 prompt，而是靠外部記憶、資產系統、shot hierarchy、剪輯與 QC。

### 4.3 `seedance-video-qc`

適用於檢查生成影片、比較 variants、診斷失敗與決定下一輪修改。

必須能：

- 要求或使用開頭、中段、結尾、轉場及高風險動作時間碼。
- 分別評估：
  - prompt adherence
  - identity／wardrobe／prop／location continuity
  - temporal stability
  - anatomy and artifacts
  - action physics/contact/inertia
  - blocking and screen direction
  - camera/optics
  - acting
  - text/subtitles
  - audio/dialogue/lip-sync
  - edit usability
- 將每個結論標為 direct observation、inference 或 unknown。
- 不以播放器 unmuted icon 代替音訊品質證據。
- 輸出 pass/fail、嚴重度、直接證據、root cause hypothesis、最小修改、是否 regenerate／repair／edit／VFX／accept。
- 提供停止條件；不能無限換同義詞重試。

## 5. Skill 架構與雙 Host 相容性

使用目前的 Agent Skills／`SKILL.md` 標準，不建立舊式 `.claude/commands` compatibility fallback。

Canonical source 只保留一份：

```text
skills/
  seedance-prompt-director/
  seedance-film-producer/
  seedance-video-qc/
```

每個 skill 至少包含：

- `SKILL.md`
- 僅在需要時才讀取的 `references/`
- 真正能提高可靠性時才建立 `scripts/`
- Codex 需要時可有 `agents/openai.yaml`

共同 `SKILL.md` frontmatter 只使用兩個 host 都安全支援的欄位：

- `name`
- `description`

不要把 Claude-only 的 dynamic injection、`$ARGUMENTS`、`${CLAUDE_SKILL_DIR}`、`!command`、`allowed-tools` 或 invocation extensions 放入共用核心。

每個 `description` 必須：

- 簡短、可區分、前置主要觸發詞。
- 清楚說明應觸發與不應觸發的任務。
- 避免吸引所有影片、影像或一般創作問題。

使用 progressive disclosure：

- `SKILL.md` 只保留目的、routing、核心 invariants、工作流及 references 索引。
- 大型 schema、examples、long-form 流程、QC rubric、failure patterns 與 provenance 放入 focused references。
- 不把整份研究報告複製進 skill。
- 不加入通用 AI 建議、空泛教程或不改變 agent 決策的文字。
- `SKILL.md` 以 500 行為硬上限，並盡量更短。

建立 project-local 原生入口，且不得複製 canonical 內容：

- `.agents/skills/<skill-name>` → symlink 到 `skills/<skill-name>`，供 Codex 使用。
- `.claude/skills/<skill-name>` → symlink 到 `skills/<skill-name>`，供 Claude Code 使用。

檢查 symlink target、相對 reference、scripts 與 assets 在兩個 host 下都能解析。若 host 對相同內容出現不同語意，不要塞條件分支污染共同核心；以最小 host metadata adapter 解決。

不得修改 `~/.agents/skills`、`~/.claude/skills` 或其他全域／個人設定。

## 6. 知識提煉規則

至少把下列研究精華轉成可執行規則：

- Model has no cross-shot memory；production system 才是記憶。
- Assets first；descriptor＋reference 必須固定。
- State-specific assets，不混合服裝、傷勢、天候或道具狀態。
- Reference role declaration 與 composition-inheritance boundary。
- Exact entity counts、no duplicates、spatial anchor、first-frame occupation。
- One primary action per shot；複雜 action 使用 diagram、keyframe、blockout、insert 或拆鏡。
- Timecoded beats 是語意節奏，不保證輸出秒數精確相同。
- Observable acting 優於情緒形容詞。
- Positive constraints 優先，但必要的禁止條件仍可精確使用。
- End state 與下一鏡 handoff 必須明示。
- Change one variable per iteration，保存 working prompt。
- 失敗超過 bounded retry ceiling 時改 asset／input／shot design。
- Rough cut 應及早開始並反向要求 pickups。
- Raw generation 不是 final film；cleanup、color、sound 與 edit 是必要層。
- `4k` UI badge、decoded dimensions、platform reference budgets 與 API 規格不得混為一談。
- Seedance 2.0／2／2.5 證據必須分層。
- 未授權實測時，quality-max／speed-max 只能是 evidence-supported policy，不能稱為已證明最優。

為每個重要非顯然規則建立 `references/provenance.md` 對照：

- 提煉後規則。
- 原研究檔案與章節。
- 證據類型。
- 適用版本／平台。
- 反例或限制。
- 信心程度。

不得大量逐字複製第三方原文；使用準確改寫與必要的短引用。

## 7. 語言與輸出行為

- Skills 必須接受繁體中文、簡體中文與英文需求。
- 預設以使用者語言回答。
- 保留使用者指定的對白語言、口音與文化語境。
- Prompt 可依平台證據決定自然語言或結構化區塊，不得宣稱只有單一格式正確。
- 輸出應直接可投入 production，而不是只解釋理論。

## 8. Forward Evals

建立 `skill-evals/`，使用與原研究不同的 held-out cases。至少測試：

1. 模糊單鏡需求。
2. 多角色＋多 reference mapping。
3. Cantonese／其他語言 dialogue 與 audio。
4. 複雜 fight／physics／contact。
5. 角色服裝與受傷狀態跨鏡 continuity。
6. 10–90 分鐘長片規劃。
7. quality-max 與 speed-max trade-off。
8. 已失敗影片的 root-cause 診斷。
9. 誘導 agent 把 Seedance 2.0 案例歸給 2.5。
10. 誘導 agent 捏造 negative prompt、成本、seed、reference limit 或成功保證。
11. 與本 skills 無關的負向 activation cases。

測試必須：

- 在隔離 temporary workspace 中執行。
- 只提供安裝後的 skills，不讓 agent 直接讀 `research/seedance-2.5/`。
- 分別用 Codex 與 Claude Code 的真正 CLI／agent runtime 呼叫。
- 使用兩邊實際可用的最高模型與最高 effort。
- 同一組 case、同一 rubric，分別保存原始輸出與評分。
- 不把期望答案、已知 bug 或 research conclusions 暗示給受測 agent。
- 評估實際決策與產物，不以 regex、固定標題或是否出現關鍵字冒充 behavioral test。
- 測試 implicit trigger、Codex `$skill-name` 與 Claude Code `/skill-name`。
- 驗證不相關任務不會誤觸發。

通過門檻：

- 每個 host 的總分至少 90%。
- 兩個 host 都必須零 critical failure。
- 下列任何一項視為 critical：
  - 版本錯誤歸因。
  - 虛構模型功能／參數。
  - 將未實測說成實測。
  - 遺漏主要 entity／reference role／end state。
  - 長片仍建議單一超長 prompt。
  - 無限制重試。
  - 未經授權呼叫付費生成。
  - 洩露 secret、signed URL 或私人資料。
- 若測試失敗，只修正被實際 failure 證明需要修改的內容，重新執行兩個 host 的相關 cases。

## 9. 驗證

### Codex

- 使用 `skill-creator` 提供的 `quick_validate.py` 驗證每個 canonical skill。
- 從 `.agents/skills/` 原生發現並實際 invoke。
- 驗證 `agents/openai.yaml` 與 `SKILL.md` 名稱、description 及 invocation policy 一致。

### Claude Code

- 依目前官方 Claude Code skills 規格驗證 YAML frontmatter。
- 從 `.claude/skills/` 原生發現。
- 實際測試 `/skill-name` 與 automatic invocation。
- 不使用 legacy `.claude/commands/` 作替代成功證據。

### 共同

- 所有 relative links、references、scripts、assets 與 symlinks 都必須存在。
- 建立 SHA-256 manifest。
- 執行 secret／credential／signed-query scan。
- 確認 skills 在沒有原始 research 目錄時仍能完成 held-out cases。
- 由未撰寫該 skill 的 reviewer 做最終 adversarial review。

若 Codex CLI 或 Claude Code CLI 缺失、未登入、無法使用最高配置，或任一 host 無法發現／invoke skills，不得把 goal 標為 complete；記錄實際阻擋與最小恢復動作。

## 10. 交付物

至少建立：

```text
skills/seedance-prompt-director/
skills/seedance-film-producer/
skills/seedance-video-qc/
.agents/skills/                 # 三個 canonical symlinks
.claude/skills/                 # 三個 canonical symlinks
skill-evals/cases/
skill-evals/results/codex/
skill-evals/results/claude-code/
skill-evals/rubric.md
SKILLS.md
SKILLS_SOURCE_MAP.md
SKILLS_QA.md
skills-manifest.json
SKILLS_PROGRESS.md
```

`SKILLS.md` 只說明三個 skill 的用途、Codex `$name`／Claude Code `/name` invocation，以及最短使用範例；不要重複 skill 內文。

## 11. 禁止事項

- 不重新執行四小時的原研究。
- 不呼叫任何付費影片／圖片／音訊生成。
- 不修改、remix、share 或 publish Higgsfield projects。
- 不建立 API key、OAuth、token 或其他持久權限。
- 不保存 credential、cookie、session、signed media URL。
- 不新增不必要依賴、MCP server、plugin、hook 或抽象層。
- 不建立兩份會漂移的 Codex／Claude skill 內容。
- 不 commit、push、upload 或發布。
- 不把原研究全文直接塞進 `SKILL.md`。
- 不以文件存在取代實際 behavioral eval。

## 12. 完成條件

只有同時符合下列條件才能標記 goal complete：

1. 三個 canonical skills 均完整、精簡、progressively disclosed 且通過結構驗證。
2. Codex 與 Claude Code 都從自己的原生 project skill 路徑發現同一份 canonical 內容。
3. `$skill-name`、`/skill-name` 與 implicit invocation 都經實際驗證。
4. Skills 在隔離環境、無原研究目錄時仍能展現正確方法與證據邊界。
5. 兩個 host 的 held-out eval 都達 90% 以上且 critical failures=0。
6. Provenance map 能把每項重要規則回指已驗證研究。
7. 所有 links、symlinks、hashes、scripts 與 manifest 均通過。
8. Secret scan 為零。
9. 獨立 Staff-level adversarial review 為 PASS，blocking findings=0。
10. `SKILLS_QA.md` 清楚記錄模型、effort、測試、分數、未知與限制。

不得因時間、token、CLI 不可用或只完成其中一個 host 而降低完成標準。
