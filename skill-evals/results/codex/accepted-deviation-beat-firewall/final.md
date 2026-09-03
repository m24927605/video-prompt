依 accepted-state firewall，已接受的 shot 1 是「可採納偏差」：它提前完成原 beat 2 與 beat 3 的閱讀段落。後續不得重演開信或讀信；被拒絕的撕信版本完全不推進故事狀態。

### Beat 狀態重算

| 狀態 | Beat | 可見事實 |
|---|---|---|
| `completed` | 原 beat 2 | 角色已打開信封 |
| `completed` | beat 3A（自原 beat 3 拆出） | 角色已讀完信 |
| `current` | beat 3B | 把信折起來，且不得撕破 |
| `reserved` | 下一個劇本 beat | 尚未提供，不得由模型自行預演 |

原 beat 2 從 queue 移除；原 beat 3 改成只剩「折信」這個 delta。

### 三鏡頭接續

| Shot | 接續關係 | 起始狀態 | 唯一主要 delta | 結束狀態 |
|---|---|---|---|---|
| Shot 1 | 已接受來源 | 原始狀態 | 已打開並讀完信 | 信已讀完、信封已開；信是否完整須由畫面確認 |
| Shot 2 | 優先為 `same-shot seamless` | Shot 1 的 approved cutoff／local handoff | 將完整、攤開的信折起來 | 信完整且已折、仍由角色持有；不自動新增收納或放桌動作 |
| Shot 3 | `intentional next shot` | Shot 2 通過後的 folded-letter state | 下一個經劇本定義的新 beat | 未定義前保持 reserved，不生成 |

Shot 2 的提示只描述新 delta，例如：「從既有姿勢繼續，角色平靜地把完整信紙折起來。」不要再描述打開信封、閱讀內容或「讀完後」，以免模型重演已完成事件。

Shot 3 應刻意切換構圖或景別，承接下一個正式故事行為；它不是 Shot 2 的無限延伸。若下一 beat 尚未定義，Shot 3 保留在 queue，不用反應鏡頭或放信動作自行填空。

### 橋接與漂移處理

Shot 1→2 可用無縫同鏡續接，但必須先確認 approved 尾端具備：

- 信紙可見且完整；
- 角色、手別、持有關係、畫面方向與動作尾勢清楚；
- 沒有撕裂、複製信紙、手部崩壞或不可剪的尾端瑕疵。

若只是最後幾幀的局部抖動或短暫手部瑕疵，走 `repair tail`：由 Shot 1 的 accepted parent 製作有界尾端修復，再經 QC 後成為新的 approved derivative。

若身份、信紙幾何、完整性、持有手或空間方向已漂移，走 `reanchor drift`：回到 Shot 1 較早的乾淨 approved frame，加上 canonical 角色／信件資產，將 Shot 2 改為可剪接的新鏡頭。不得拿撕信版本的尾幀來「修」連續性。

橋接只攜帶已知狀態。若 Shot 1 畫面不能證明信紙完整，完整性應標為 `unknown`；此時不能直接做無縫延伸，應用 canonical intact-letter 資產重新錨定。

### Accepted／canon 防火牆

可以進 accepted state：

- 已由人確認的 Shot 1，以及其可見的「已開信、已讀完」事實。
- Shot 1 的乾淨影格或尾段：通過身份、道具與鄰鏡相容 QC 後，才可升為 approved memory/local handoff。
- Shot 2：只有在信保持完整、折信動作清楚且沒有重演完成 beats 時才能接受。
- 尾端修復或重新錨定輸出：必須另存新版本、保留 Shot 1 parent lineage，重新審核後才可 accepted。
- Shot 2 通過後，才建立新的 continuity checkpoint：`letter=folded_intact`。

不得 canon：

- 被拒絕的撕信版本及其任何影格、尾幀、prop 狀態或動作結果。
- 未審核的 extension、tail repair、reanchor 或 Shot 2 候選。
- 模型自行加入的重新閱讀、重新開信、撕信、揉信、放桌、收入信封等事件。
- 從 rejected 版本推導出的「角色生氣」或「信已毀損」等故事含義。

撕信版本只留在 rejected ledger，標記缺陷 `unauthorized prop-state transition: intact → torn`，可供診斷，但不能作 reference、handoff、select 或 approved memory。

### 生產控制

採 hybrid 模式：Shot 2 是高風險手部／道具接續，走較嚴格 QC；Shot 3 在新 beat 鎖定前不投入生成。Shot 2 失敗時先改用更乾淨的信件資產、較短動作或折信 insert；不以 rejected 版本補洞。回滾點固定在 accepted Shot 1。

目前 ledger 能確認：2 個已審版本、1 accepted、1 rejected、1 次 accepted deviation、1 次撕裂缺陷。首輪通過率、重試數、成本、耗時與可用秒數均未知，不應臆造。平台、模型版本與 extension 能力也未提供；因此 `same-shot seamless` 是剪輯／接續意圖，不代表任何特定 Seedance 介面保證具備此能力。
