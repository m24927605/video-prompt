# Seedance skills execution progress

執行契約：`SEEDANCE_CROSS_AGENT_SKILLS_GOAL.md`。研究封存日：2026-08-22（Asia/Taipei）。

## Completed

- 開始前完整讀取 362 行執行契約。
- 主代理與 Research Distiller 各自完整讀取十份必讀研究，共 6,899 行／437,948 bytes；未重跑原始研究。
- 核對當前 OpenAI 與 Claude Code 官方 skills 規格。
- 驗證本機最高 host 配置：Codex `gpt-5.6-sol`／`ultra`；Claude Code `claude-fable-5`／`max`。
- 建立三個 canonical skills、focused references、53 條 provenance rules 與 `agents/openai.yaml`。
- 建立 `.agents/skills` 與 `.claude/skills` 的三組相對 symlinks；沒有 legacy `.claude/commands`。
- 建立 14 個 held-out cases、共同 behavioral rubric、evaluator-only criteria、隔離 runner、aggregate/manifest/secret-scan scripts。
- `skill-creator` `quick_validate.py`：3/3 PASS。
- 結構驗證已通過 frontmatter、line limit、host-safe core、links、symlinks、metadata、case coverage 與 provenance ID coverage。
- Codex 14/14 behavioral cases：100.00%，critical=0，negative activation failures=0。
- Claude Code 14/14 behavioral cases：98.14%，critical=0，negative activation failures=0。
- 獨立 Staff-level adversarial review：PASS，blocking findings=0。
- 初次 fabricated-parameter routing failure 已保存 lineage，完成窄修並在雙 host 重測通過。
- 所有 Claude/Codex persisted results 已套用最終 session/private-path sanitizer。
- 完整 deterministic suite：35/35 PASS。
- SHA-256 public-artifact manifest：322 entries；`--check` PASS。
- Post-manifest staged-index credential/signed-query scan與 gitleaks：0 findings／0 leaks。
- `SKILLS_QA.md` 與第 12 節逐項 completion audit 已完成。

## Fixed constraints

下列限制適用於原 skill 建置與雙 host 驗收 goal；不包含使用者後續另行明確授權的 public GitHub release：

- 未呼叫任何付費影片、圖片或音訊生成。
- 未修改、remix、share 或 publish Higgsfield project。
- 未建立或保存 API key、OAuth、credential、cookie、session 或 signed media URL。
- 原 goal 執行期間未 commit、push、upload 或發布。
- 不因時間或 host 延遲降低雙 host 90%／critical=0 完成門檻。

## 2026-09-01 clean-room integration checkpoint — active

- 固定研究 `liyue-aigc/seedance-2-5-video-director` 的 `main` commit `ad0e68ba6ce24fb9ae9c67c9276061cef37663f1`；只採抽象操作政策，未複製上游例文、onboarding、template 或 provider-derived 長文。
- 維持純 AI agent skills suite；未新增應用程式、API client、生成服務、資料庫、runtime compiler、ShotContract engine 或媒體 pipeline。
- 完成 Prompt Director 的 deliverable／operation／extension／asset／example／edit／transition／blockout／storyboard 契約，以及 Photography visual-look ownership 收斂。
- 新增五-skill isolated staging、expected／forbidden activation 與 fail-closed case contract；個人 `.agents/skills`、`.codex/skills` 不參與 Codex 評測。
- Codex 29/29 independent grades：**PASS，2886/2900（99.52%）**，critical=0，negative／forbidden activation failures=0，paid-media events=0。
- 第一輪 Codex finding 已按單一 root cause 修復：`ambiguous-single-shot` 由 83 FAIL 提升為 100 PASS；明確 `only` 的 prompt-only 與 extension boundary 輸出未被擴張。
- 五個 packaged skills 的 quick validation 全通過；70項 deterministic tests中69通過，唯一未通過項是刻意延後的manifest hash；pre-seal signed-query scan 534 files／0 findings，gitleaks 0 findings。
- Claude Code 五-skill discovery smoke 已成功，但七日配額於 2026-09-01 觸頂；官方事件記錄的重置時間為 **2026-09-02 07:00 Asia/Taipei**。在 Claude 29-case review、跨 host aggregation、final manifest 與 post-manifest scans 完成前，本 checkpoint 不宣稱 goal complete。
- 追加完整研讀 `Emily2040/seedance-2.0` commit `44b514992963a2570beee71aaf2a8720785f7ec2`：269 tracked files／23,767,844 bytes，全數由 core、engineering/eval、provenance/version lanes 覆蓋；10 PNG逐張視檢、兩個TTF依OFL盤點。
- 所有2.0 findings均先分類 `GENERIC`／`SEEDANCE_FAMILY_CONDITIONAL`／`SEEDANCE_2_0_ONLY`／`UNKNOWN_UNPROVEN`；2.0 limits、model IDs、API/UI、tag/mode、固定word/retry/seed與legacy/filter workaround全部隔離。
- 只吸收通用缺口：reference dimension authority、inspection honesty、accepted-source delta、continuation relation、beat firewall與version isolation；未引入upstream compiler/schema/state engine/installer/media tooling。
- Seedance 2.0追加的4個Codex held-out cases均通過；初次 `accepted-deviation-beat-firewall` 暴露agent內部numeric ceiling洩入deliverable，已從87 FAIL修為100 PASS，且未新增任何固定generation retry／chain數字。

## 2026-09-02 Claude review cycle checkpoint — active

- Claude Code 額度重置後完成 29/29 原生五-skill isolated runs；model／provider、workspace digest、expected／forbidden activation、research isolation、case／rubric digest 與 paid-media gates 全部通過。
- 第一輪 fresh-context adversarial review 為 **22/29 PASS、2603/2900（89.76%）、critical=0**；完整結果保存於 `skill-evals/results/reviews/claude-upstream-integration-adversarial-review.md`，不得把 host exit success 誤報為 semantic PASS。
- 七個 findings 已按根因處理：Claude runner 由 `permission-mode=plan` 改為 read-only tools 下的 `dontAsk`；Prompt Director 的 prompt-only 改為裸單一 artifact；Photography 的 unknown-provider、visual-look scope 與 numeric example leakage 已在 canonical skill／references 收斂；兩個 negative fixtures 消除題意或評分隱含條件。
- 修後七個 focused cases 均重新取得正常 host evidence；plan-only 三案已直接交付 artifact，prompt-only 無包裝，live-action visibility 已修正，visual-look 無 blocking／timeline 且只保留使用者提供的 `35mm`，靜態圖不再輸出具名模型、相容性、negative 欄位或平台參數建議。
- 本 work slice 於 90 分鐘上限停止。尚未完成：第二輪且最後一次 29-case 雙 host behavioral review、cross-host aggregate、語意凍結後單次 manifest／security seal 與 final commit；在這些 gates 全綠前不得宣稱 goal complete。
