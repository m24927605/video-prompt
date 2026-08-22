# Seedance 2.5 未來受控評測計畫

> **本文件只設計實驗。** 本研究 goal 未獲付費生成授權；不得以此文件啟動 API／UI 生成、消耗額度或把預期結果寫成實測結論。  
> Version gate 基準：2026-08-22（Asia/Taipei）。正式執行前必須重新核對模型、平台、model ID、參數、價格、quota、政策與文件更新日。

## 1. 研究問題與可反證假設

### RQ1：官方導出的 prompt schema 是否改善可控性？

- **H1**：明確 asset mapping + one-sentence intent + global invariants + contiguous timeline + audio rules，相較最小自然語言 baseline，提高 prompt adherence 與 first-pass approval。
- **反證**：paired 結果無優勢、只提升美感但降低動作／story fidelity，或收益只出現在某一 task／risk tier。

### RQ2：reference 數量與資訊密度是否存在甜蜜點？

- **H2**：經挑選、分責、品質合格的少量 references，會比接近平台上限但冗餘／互相衝突的 references 有更好 fidelity／cost。
- **反證**：增加 references 在控制品質後仍單調改善，或少量組在多視角／多角色 task 系統性失敗。

### RQ3：外部 continuity system 是否改善長距離一致性？

- **H3**：canonical passport + per-shot entity schedule + fidelity-gated approved memory + local handoff，優於只傳最近生成幀或只重複文字描述。
- **反證**：長距離 identity／prop／location consistency 沒改善，或增加 constraints 顯著降低 prompt adherence、motion、aesthetic／throughput。

### RQ4：extension chain 與獨立 shots 哪個在長片更有效？

- **H4**：短相鄰 continuation 的 extension 可能有較好接縫，但長 chain 的 drift／waste 可能高於 canonical-reference + hard-cut shots。
- **反證**：在相同故事、品質 floor 與 cost ceiling 下，extension 在所有 recurrence distances 都不差且更快／便宜。

### RQ5：品質最大化、速度守門檻、混合流程的 Pareto 關係？

- **H5**：三者至少形成兩個非支配點；混合流程在 hero quality floor 下提高 usable seconds/hour 或降低 cost per approved second。
- **反證**：某流程在 quality、time、cost 皆支配其他流程，或混合流程的 coordination overhead 抵消分級收益。

## 2. 證據與方法邊界

- `官方事實`：Seedance 2.5 prompt／task／parameter 能力只以 [BytePlus prompt guide](https://docs.byteplus.com/en/docs/ModelArk/2607689)、[tutorial](https://docs.byteplus.com/en/docs/ModelArk/2607688)、[API](https://docs.byteplus.com/en/docs/ModelArk/1520757)及實際執行平台版本為準。
- `一手方法證據`：MovieBench 的 movie／scene／shot hierarchy、VBench-2.0 的 intrinsic faithfulness、StoryMem／EntityBench 的 memory／fidelity gate 啟發評測結構；它們不是 Seedance 2.5 實測。本機來源 [archive: `sources/supplemental/cvf-cvpr2025-moviebench.pdf`]、VBench-2.0 [archive: `sources/supplemental/arxiv-2503.21755-vbench-2.0.pdf`]、StoryMem [archive: `sources/supplemental/arxiv-2512.19539-storymem.pdf`]、EntityBench [archive: `sources/supplemental/arxiv-2605.15199-entitybench.pdf`]。
- `未知／待驗證`：效果大小、成本、速度、重試、平台穩定性、同 seed 變異與所有 production thresholds。

## 3. 執行前 preregistration

在任何付費 call 前鎖定一份不可回寫的 preregistration：

```yaml
experiment_id:
date_timezone:
platform_region_account_tier:
model_ids_and_document_versions:
task_and_parameter_matrix:
shot_suite_hash:
input_asset_hashes_and_rights:
prompt_condition_hashes:
seed_schedule:
replicate_count:
randomization_plan:
blinding_plan:
hard_gates_and_scales:
primary_secondary_endpoints:
sample_size_or_budget_rule:
stopping_rule:
analysis_code_hash:
exclusions_and_missing-data_policy:
```

變更只能新增 amendment，記錄時間、原因與受影響分析；不能看結果後偷偷改 primary endpoint。

## 4. 測試素材集

### 4.1 Pilot suite（低成本校準）

12 個 shot contracts，每個 task archetype 1 個：

| ID | Task | 主要風險 | Primary checks |
|---|---|---|---|
| P01 | T2V 單主體單動作 | 四肢／接觸 | order、motion、temporal stability |
| P02 | T2V 30s 多段故事 | 過載／cut | plot coverage、order、identity |
| P03 | T2V 產品微距 | 物理／材質 | contact→result、object count |
| P04 | T2V 雙人對白 | speaker／lip | line attribution、sync、subtitle absence |
| P05 | R2V 角色＋場景 | mapping | appearance／background separation |
| P06 | R2V 三角色＋聲音 | 多 identity | presence、face／voice mapping |
| P07 | Motion reference | 屬性洩漏 | action／camera transfer only |
| P08 | Storyboard | panel order | high-level sequence、style leakage |
| P09 | Independent keyframes | strict layout | keyframe alignment、transitions |
| P10 | First+last frame | 拓撲／物理 | start/end fidelity、causal bridge |
| P11 | Video edit | edit spill | A→B、time range、preservation |
| P12 | Extension | seam／drift | AV seam、end state、identity |

Pilot 目的只為：檢查 task 可執行、校準 rubric、估變異／成本／時間、做 power／budget update；不能從 pilot 挑「最好看」的 shots 再稱 main confirmation。

### 4.2 Main single-shot suite

24 個 shot contracts：上述 12 archetypes 各兩個內容實例，平衡：

- realistic／stylized。
- 1／2–3 characters。
- static／camera movement。
- low／medium／high motion。
- no dialogue／one speaker／two speakers。
- 8–12 秒一般 shot；另保留 30 秒 narrative stress shots。
- A／B／C risk tiers 各 8 個。

每個 shot 預先定義 required entities、forbidden entities、action order、start/end state、camera、sound、hard defects 與相鄰 cut needs。

### 4.3 Long-form suite

三個不同風格故事，共 32 shots：

- `L1`：8-shot 寫實雙人室內戲；重點為 eyeline、wardrobe、prop transfer、dialogue。
- `L2`：8-shot stylized journey；重點為 character／location／palette 與 hard-cut geography。
- `L3`：16-shot action-drama stress sequence；2–4 角色、2 locations、3 persistent props，刻意安排角色／物件在 gaps 1–2、3–5、6–10、11–15 shots 後重現。

每個 story 有 story overview、scene cards、character／voice／location／prop passports、entity schedules、cut／continuation labels、shot prompts、neighbor acceptance。不得用知名受版權保護角色或無授權真人素材。

## 5. Condition matrix

### 5.1 Prompt ablation

| Condition | 內容 | 用途 |
|---|---|---|
| `PR-MIN` | 最小但完整的一段自然語言；不故意寫壞 | 實務 baseline |
| `PR-OFFICIAL` | 官方公式 + asset mapping + summary + timeline／shots + notes | 測官方導出 schema |
| `PR-CONTRACT` | `PR-OFFICIAL` + global invariants + start/end state + explicit preserve／forbidden items | 測 production contract 增量 |
| `PR-OVERLOAD` | 相同意圖但塞入過多同時 beat／camera／style constraints | stress／失敗邊界；不是推薦做法 |

Primary comparison：`PR-OFFICIAL vs PR-MIN`。Secondary：`PR-CONTRACT vs PR-OFFICIAL`；`PR-OVERLOAD` 只用 pilot／stress subset，避免無謂消耗。

### 5.2 Reference ablation

| Condition | 素材 |
|---|---|
| `REF-1` | 每 entity 一個乾淨 canonical single-view／audio；逐項 mapping |
| `REF-CURATED` | 官方建議甜蜜點內的核准 multi-view／audio，去冗餘且分責 |
| `REF-REDUNDANT` | 接近上限但合法、包含重複與近似視角；仍不故意放錯 identity |
| `REF-CONFLICT` | 一個可明確定位的屬性衝突（例如光色或服裝），只在 pilot 診斷 |

Primary comparison：`REF-CURATED vs REF-1`；`REF-REDUNDANT` 測邊際收益／退化，`REF-CONFLICT` 測 prompt priority 是否足夠。

### 5.3 Storyboard／keyframe／clay

- `CTRL-SB`：≤15 格乾淨 line-art storyboard，高層結構 reference。
- `CTRL-KF`：同樣 story beats 拆成 independent keyframes，明示順序。
- `CTRL-CLAY`：簡單 previz video + canonical visual refs，控制 blocking／camera。

比較時只選三種皆合理的 shots；不能拿不適合 clay 的情緒特寫扭曲結果。

### 5.4 Long-form memory conditions

| Condition | 下一鏡取得的 continuity context |
|---|---|
| `MEM-TEXT` | 重複必要文字描述，不傳任何生成幀；canonical 只在第一鏡 |
| `MEM-RECENT` | 只用最近生成／末幀，不做 quality promotion |
| `MEM-CANON` | 每次都用 canonical passport；不傳歷史生成幀 |
| `MEM-GATED` | canonical + per-shot entity schedule + 通過 fidelity gate 的少量 approved memory + continuation 的 local handoff |

Primary：`MEM-GATED vs MEM-RECENT`。若 `MEM-RECENT` 失敗輸出造成安全／權利問題立即停止，不為實驗目的繼續污染。

### 5.5 Workflow modes

- `WF-Q`：品質最大化，完整 previz／anchors、較高 review 與 post budget。
- `WF-S`：速度守 gate，一次 blocking，簡化 coverage，hard defect 才 retry／route。
- `WF-H`：推薦混合，A shots 用 Q、B standard、C 用 S。

三者使用同一 locked script 與交付品質 floors；允許不同 coverage／route，但要記錄所有人時、費用與失敗秒數。

## 6. Model／platform／parameter matrix

### 6.1 Primary arm

| 欄位 | 設定 |
|---|---|
| Platform | BytePlus ModelArk，實際 region／account tier 記錄 |
| Model | `dreamina-seedance-2-5-260628` |
| Resolution | 720p 作 primary common setting；1080p 只作 ModelArk hero confirmatory subset |
| Ratio | 16:9 一般 tests；edit／extend／first-frame 類按官方 gate 用 `adaptive` |
| Duration | 每個 shot contract 固定；edit 用 `-1`；其他 4–30 秒 |
| Format | mp4 一般；edit／extend 用 mov，另記 playback／conform time |
| Audio | 依 task 固定；畫面-only ablation 用 false，audio tests 用 true |
| Seed | 預先登記整數；範圍 `[-1,2147483647]`，主實驗不用 `-1` |
| Watermark | 固定一值且所有 conditions 相同；合規另測不混主效果 |
| Draft | 不用；2.5 官方 API 不支援 draft |

### 6.2 Optional control arms

- **Model control**：ModelArk `dreamina-seedance-2-0-260128`，只比較兩版共同 task／resolution／prompt 能力；2.0 不支援 timestamps 的項目改用 shot numbers，並單獨報告，不能當 2.5 prompt ablation。
- **Platform portability**：LAS `dreamina-seedance-2-5-260628` 只在 720p common subset；平台差異與模型差異分開，不把 LAS 480／720 能力跟 ModelArk 1080 混成同 cell。
- Higgsfield 只在其官方／UI model gate、參數、成本與權利完整確認後另建 arm；不套用 BytePlus JSON。

## 7. Repetitions、seed 與 sample size

### 7.1 Seed design

`官方事實`：ModelArk 2.5 支援 `seed`；同 request + 同 seed 產生相似結果，但不保證完全一致。[API 文件](https://docs.byteplus.com/en/docs/ModelArk/1520757)。因此：

1. **Fixed-seed paired block**：同一 shot、兩 prompt／workflow conditions 使用相同 seed，降低隨機差。
2. **Between-seed distribution**：至少使用多個預先登記 seeds，估計模型輸出分布與 tail failure。
3. **Same-seed reproducibility audit**：從 pilot 每個 risk tier 選 2 shots，同 request + 同 seed 重送 3 次，量測非決定性；這是 audit，不併入主要效果樣本。

### 7.2 暫定重複數

- Pilot：每 condition × shot 使用 3 個 seeds；同-seed audit 如上。
- Main：初始 5 個 seeds／cell；用 pilot 的 paired variance 和可用預算做正式 power／precision 更新。
- Long-form：每 memory condition 至少 3 個完整 story realizations；不能把每個 shot 當完全獨立樣本，analysis 以 story／shot nested model 處理。

這些數字是 `實務建議／待 power 校準`，不是事後看到顯著性才增減。若預算不足，縮小 secondary cells 或 shot suite，不降低 primary cell 的重複而假裝有把握。

## 8. Run procedure

1. 驗證 inputs、rights、hash、task constraints；建立不可變 shot packet。
2. 由非 reviewer 依 seed schedule 建 tasks；保存 request／response、queue／generation time、實際費用與失敗碼。
3. 輸出 URL 在有效期內合法下載；移除 signed query，不寫入 manifest；核對 bytes／duration／codec／hash。
4. 正規化 review copy 的 container、播放響度與標籤，但不得改動被評畫面／時序；保留原檔。
5. 盲碼為隨機 ID；condition、prompt、seed、cost、生成順序不提供給 reviewer。
6. Reviewer 先獨立看完整片，再按 timecode 記 defect、硬 gate、分項分數與 pairwise preference；允許 tie。
7. 20% 樣本重複插入測 intra-rater consistency；不同 reviewer 的順序各自隨機。
8. 解盲、鎖資料、執行預登記分析；secondary exploratory results 明標。

## 9. 評分與 fidelity gate

### 9.1 Layer 1：Intra-shot quality

- Structural／human fidelity。
- Temporal flicker、texture crawl、motion smoothness、dynamic adequacy。
- Imaging／aesthetic、material、lighting、compression。
- Audio technical quality（若適用）。

### 9.2 Layer 2：Prompt／story fidelity

- Required character／object／location presence；forbidden absence。
- Identity、服裝、道具狀態、場景與 reference fidelity。
- Action depicted、order、direction、interaction、causal result。
- Camera、timeline、dialogue、speaker、language、sound／subtitle rules。

### 9.3 Layer 3：Cross-shot consistency

只有 Layer 2 identity／location／object fidelity 達預登記 threshold 的 appearances 進 consistency 比較；未過 gate 的 scheduled appearance 對 corrected metric 記為失敗／零貢獻，不能被靜默略過。

- Character：face、hair、build、clothing、voice。
- Object：shape、color／texture、proportion、details、state／owner。
- Location：layout、landmarks、color mood、perspective-aware identity。
- Transition：cut／continuation、screen direction、eyeline、action、camera velocity、AV seam。
- Gap-decay：依同 entity 兩次出現間隔 shots 分 bin，畫 fidelity／consistency vs recurrence gap。

這沿用 EntityBench「先正確，再比較一致」的概念；threshold 要用 pilot 人工標註校準，不能直接搬其模型 metric 值。

## 10. Human evaluation

### 10.1 Reviewer panel

- 暫定至少 5 位獨立 reviewer：director／editor／continuity／VFX or DP／sound；各自評自己專長與共同項。
- Reviewer 不能評自己生成／修正的 take；衝突需第三方 adjudication。
- 先用 calibration clips 對 severity／scale 達成共識；不把 calibration clips 放主測試。

### 10.2 Pairwise + absolute

- **Pairwise**：A／B 順序隨機，選 A、tie、B；每一比較只問一個 primary dimension，避免「整體感覺」吞掉細節。
- **Absolute**：1–5 rubric，另有硬 gate pass/fail 與 timecode defects。
- 先 absolute 後 pairwise 或跨 reviewer counterbalance，避免先看到另一版造成 anchoring。

### 10.3 Reviewer QA

- 20% hidden duplicates；未達預登記一致性標準的 reviewer 先 retrain，再按規則決定是否排除。
- 報 Krippendorff's alpha／weighted kappa（ordinal）或 ICC（連續彙總）；不能只報百分比同意。
- 所有 exclusions、播放錯誤、缺失 rating 及原因保留。

## 11. Automated／instrumented metrics（secondary）

自動量測只作診斷，不能單獨核准成片：

- Frame／shot：duration、fps、resolution、duplicate／dropped frames、black／freeze、loudness、clipping。
- Temporal：optical-flow discontinuity、flicker、track survival、artifact time ratio。
- Prompt：entity detection／count、action／caption alignment，必須人工抽查 false positive／negative。
- Identity：face／body／object embeddings + human identity judgment；不能把「相似但錯的人」當一致。
- Audio：ASR WER／台詞 exactness、speaker attribution、AV offset、room-tone／level jump。
- Editorial：approved in/out、usable handles、neighbor-cut pass、manual fix minutes。

VBench／VBench-2.0 類 metrics 可作 secondary；其模型／版本／threshold、失敗、未評項與 human-alignment calibration 全部記錄。

## 12. KPI、時間與成本紀錄

每個 shot／run 收集：

```text
prompt adherence; character/location continuity; temporal stability;
motion naturalness; cinematography; sound; artifact rate; editorial usability;
first-pass approval; retries; queue time; generation time; review time;
asset prep time; correction/VFX/sound time; generated seconds; approved seconds;
billed amount; cost per approved second; usable seconds/hour; waste rate.
```

成本以帳單為準；0-cost failed task 仍記 wall-clock／人工成本。跨平台比較要分幣別、稅、discount／resource pack 與日期，不能只用 nominal token price。

## 13. Statistics

### 13.1 Primary analysis

- Experimental unit：single-shot study 以 shot-seed pair；long-form 以 story realization，shots nested within story。
- Pairwise preference：paired Bradley–Terry／mixed logistic model，或預登記的 exact paired permutation；tie 明確建模。
- 1–5 ordinal：cumulative-link mixed model；若樣本不足，paired Wilcoxon + cluster bootstrap。
- Pass／approval：mixed logistic；報 absolute difference、risk ratio／odds ratio 與 95% CI。
- Time／cost：報 median、IQR、P90、cluster bootstrap CI；長尾不只用 mean。
- Inter-rater：alpha／kappa／ICC；effect size 與 CI 優先於單一 p-value。
- 多重比較：primary comparison 少而預登記；secondary 用 Holm correction 或 false-discovery policy。

### 13.2 Missing／failed outputs

- API failure、moderation、timeout、corrupt file、無 required entity 分開記錄。
- 不把無可評輸出靜默刪除；primary intention-to-produce analysis 中按預登記規則計失敗。
- 同時報 conditional-on-evaluable score，清楚顯示分母；避免 failure-heavy condition 因只留下最好樣本而看似更強。

### 13.3 Non-inferiority／production relevance

速度流程只有在所有 hard gates pass，且 primary quality 下限不劣於預登記 margin，才能稱「守住品質」。Margin 由 pilot + stakeholder 決定，例如 1–5 scale 的差值、approval-rate drop 或 continuity floor；本文不先假定 universal margin。

## 14. Pareto analysis

每個 workflow 以一個 vector 表示：

```text
Q = [adherence, continuity, stability, motion, cinematography, sound,
     1-artifact_rate, editorial_usability]
E = [first_pass, -retries, -time/approved_shot, usable_seconds/hour,
     -cost/approved_second, -human_fix_time, -waste_rate]
```

先套 quality floors，再計 non-dominated frontier；不先用任意權重壓成單一總分。

可驗證結論格式：

- 「在本 suite、model ID、平台、日期、預算與品質 floor 下，WF-H 相對 WF-Q 的 usable seconds/hour 提升 X（95% CI），continuity 差 Y（95% CI）；兩者是否非支配。」
- 禁止：「WF-H 是最快又最好」或「Seedance 2.5 的最佳流程」除非跨 suite、重複、reviewer 與版本都支持。

Frontier robustness：以 bootstrap 重抽 shot／story／reviewer；報每 workflow 落在 frontier 的比例。

## 15. 通過、停止與安全規則

### 15.1 Production gate（暫定、待 pilot 校準）

- 所有 rights／safety／delivery／required beat／identity／continuity hard gates pass。
- Blocking artifact 為 0；critical dimension 不低於 project floor。
- 至少兩位非生成者核准 hero／continuity-critical shots。
- Rough-cut neighbor test、audio、subtitle 與 final technical QC 通過。

### 15.2 Experiment stopping

- 達預登記 sample／budget；不因「已顯著」任意提前停。
- 安全／權利、平台異常收費、資料洩漏、模型／文件重大版本變更立即暫停，重新 gate。
- 某 condition 連續觸發相同 hard failure 到預登記 futility boundary 時停止該 cell，保留失敗為結果。
- 若成本預估（由 pilot 實際帳單推得）超使用者授權，縮 secondary scope 或請求新授權；不得自行加值。

## 16. 預期產物

- Immutable preregistration、shot suite／asset hashes、randomization seed、analysis plan。
- 每 run 完整 ledger；原始／review copies、blind mapping、ratings、timecode defects。
- Pilot calibration／power update；main results；per-task／risk-tier／gap-decay slices。
- Pareto frontier + bootstrap stability；workflow decision record。
- Versioned production policy：哪些 prompt／references／memory／routes 被資料支持、哪些被反證。
- Negative results、failures、unknowns、平台差異與不可泛化條件。

## 17. 本 goal 內的禁止事項

- 不啟動任何付費或免費但會消耗配額的影片生成。
- 不建立 API key、不讀取／保存憑證、不保存 signed output URL。
- 不修改、重跑、刪除、分享或發布 Higgsfield projects。
- 不把官方展示、搜尋摘要、學術預印本或本文件預期值冒充本專案實測。
