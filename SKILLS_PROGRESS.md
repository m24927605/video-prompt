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
