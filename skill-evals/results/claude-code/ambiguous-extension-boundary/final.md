I checked the skill's references before drafting. One thing blocks writing the final prompt, and the skill explicitly requires stopping on it rather than guessing.

**The blocker: "向前續寫" 的邊界方向是歧義的。** The prompt-schema reference (`skills/seedance-prompt-director/references/prompt-schema.md:128-136`) states that phrases like 「向前續寫」/「往前延長」 are ambiguous direction labels — they don't establish which boundary of the source video the new material attaches to — and that a "只要最終提示詞" request does not override this: the direction question must be asked once before any draft. Your described action fits both readings equally well:

- **接在 Video 1 結尾之後（append）**：新的 5 秒從 Video 1 的最後一格接續，人物在後續走進房間。
- **加在 Video 1 開頭之前（prepend）**：新的 5 秒是前傳，人物走進房間，最後一格必須無縫接上 Video 1 的第一格。

這兩種寫法的提示詞結構完全不同（各自要重建的邊界狀態是相反的一端），所以無法先寫再改。

Everything else is ready and doesn't need input from you: no local video file exists (「@Video 1」會作為平台上傳標籤處理)，所以提示詞會以引用 @Video 1 邊界幀的方式鎖定人物身份、場景、機位、光線與環境聲的連續性，而不是虛構具體場景細節；平台/模型未指定，會交付平台中立的提示詞；依你的要求只回最終提示詞，不附說明。

**請確認一項：新的 5 秒要接在 Video 1 的「結尾之後」，還是「開頭之前」？** 回覆後我會直接給出最終提示詞。
