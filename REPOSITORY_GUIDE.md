# Repository Guide

這份索引是給第一次瀏覽 Miiduoa 帳號的人。GitHub 上保留了一些早期課堂、原型與重做前的 repository；如果要評估目前的能力，請優先看下面的 maintained work，而不是只依 repo 名稱或建立時間判斷。

## Start here

### 1. Flagship system

**[Campus One](https://github.com/Miiduoa/graduation)**  
Mobile + Web + Backend 的校園產品 monorepo。  
重點：Expo、Next.js、Firebase、shared contracts、角色權限、rules tests、CI / E2E、degraded path。

- [Case study](https://miiduoa.github.io/case-studies/campus-one/)
- [2-minute reviewer path](https://github.com/Miiduoa/graduation/blob/main/docs/REVIEW_IN_2_MINUTES.md)

## Tools

這些專案有明確使用情境、可操作介面與可檢查限制：

| Repo | Focus |
|---|---|
| [Contractscope](https://github.com/Miiduoa/contractscope) | OpenAPI 合約比較、變更風險與 CLI；[設計與規則範圍](https://github.com/Miiduoa/contractscope/blob/main/docs/design.zh-TW.md) |
| [Motionbench](https://github.com/Miiduoa/motionbench) | 彈簧與 Bézier 動畫工作台；[模型與驗證](https://github.com/Miiduoa/motionbench/blob/main/docs/design.zh-TW.md) |
| [Switchback](https://github.com/Miiduoa/switchback) | 本機 GPX 路線與海拔分析，支援繁中／英文 |
| [Roomtone](https://github.com/Miiduoa/roomtone) | 本機音訊剪輯、淡入淡出與 WAV 匯出，支援繁中／英文 |
| [Stillroom](https://github.com/Miiduoa/stillroom) | browser image delivery workbench |
| [Cuework](https://github.com/Miiduoa/cuework) | subtitle timing / overlap editor |
| [Tracefold](https://github.com/Miiduoa/tracefold) | HAR / network trace analysis |
| [Patchday](https://github.com/Miiduoa/patchday) | SQLite migration rehearsal |
| [nowrite](https://github.com/Miiduoa/nowrite) | handwriting/PDF workflow |
| [web](https://github.com/Miiduoa/web) | resilient student planner PWA |

## Data / analytics / decision systems

| Repo | Focus |
|---|---|
| [Retail Ops DSS](https://github.com/Miiduoa/retail-ops-dss) | forecasting → replenishment / staffing decisions |
| [Demand Sensing Lite](https://github.com/Miiduoa/demand-sensing-lite) | demand-sensing baseline |
| [Rail Ops Briefing DSS](https://github.com/Miiduoa/rail-ops-briefing-dss) | operational briefing / decision support |
| [Competition Lab](https://github.com/Miiduoa/competition-lab) | reproducible competition workflow |
| [mymis](https://github.com/Miiduoa/mymis) | product analytics / experimentation |
| [bitest](https://github.com/Miiduoa/bitest) | BI regression / data-quality gate |
| [byline](https://github.com/Miiduoa/byline) | dataset contract |
| [0925SQL](https://github.com/Miiduoa/0925SQL) | SQLite analytics mart |
| [stock](https://github.com/Miiduoa/stock) | walk-forward backtest discipline |

## Engineering studies

這些 repo / labs 刻意把一個技術問題縮小，讓規則與失敗情境可以直接測：

- [Tracepath](https://miiduoa.github.io/labs/tracepath/) — distributed trace structure / exclusive time
- [Flagrail](https://miiduoa.github.io/labs/flagrail/) — deterministic feature flags
- [LineageGuard](https://miiduoa.github.io/labs/lineageguard/) — schema evolution / column lineage
- [TxnScope](https://miiduoa.github.io/labs/txnscope/) — optimistic concurrency
- [SessionSentry](https://miiduoa.github.io/labs/sessionsentry/) — session lifecycle
- [Eventlane](https://miiduoa.github.io/labs/eventlane/) — at-least-once delivery / DLQ
- [Syncbench](https://miiduoa.github.io/labs/syncbench/) — offline synchronization
- [Rampwatch](https://miiduoa.github.io/labs/rampwatch/) — canary guardrails
- [Gesture](https://github.com/Miiduoa/Gesture) — accelerometer feature pipeline
- [Game2D.2](https://github.com/Miiduoa/Game2D.2) — deterministic fixed-step simulation
- [ERP](https://github.com/Miiduoa/ERP) — append-only inventory ledger
- [learnpy](https://github.com/Miiduoa/learnpy) — AST-based structural code checks
- [anyone](https://github.com/Miiduoa/anyone) — moderation / idempotency / audit boundaries
- [aortal](https://github.com/Miiduoa/aortal) — JSON contract regression guard
- [llm](https://github.com/Miiduoa/llm) — LoRA training pipeline validation

## Superseded / historical repositories

下面這些不是目前作品集主線；保留主要是歷史與遷移參考：

| Repo | Status |
|---|---|
| [campus-one-v2](https://github.com/Miiduoa/campus-one-v2) | superseded by Campus One |
| [campus-one-v12-prototypes](https://github.com/Miiduoa/campus-one-v12-prototypes) | superseded design prototypes |
| [nuni-prod](https://github.com/Miiduoa/nuni-prod) | archived |
| [-](https://github.com/Miiduoa/-) | legacy account-history marker |

它們不應被拿來代表目前的程式品質；對應 README 也會指向 maintained successor。

## Review principle

我希望 repository 本身能回答四個問題：

1. 這個專案真正解什麼問題？
2. 哪些規則可以被測試或重現？
3. 失敗、權限與資料邊界怎麼處理？
4. 哪些事情沒有被假裝成已完成？

快速審查可以先看 Campus One 的跨端整合，再依主題選擇：Contractscope 的介面變更規則、Retail Ops DSS 的決策分析，或 Motionbench 的互動模型。每個專案都可以從範例、核心實作與測試交叉檢查。
