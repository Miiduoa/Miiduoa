# 顧晉瑋 · Miiduoa

**Information Management · Product Analytics · Decision Support · Systems**

靜宜大學資訊管理學系。  
我比較在意的不是「用了什麼技術」，而是資料與系統能不能一路走到**可驗證的決策、介面與產品**。

[作品集網站](https://miiduoa.github.io) · [Kaggle](https://www.kaggle.com/kuchinwei) · [Email](mailto:demohan513@gmail.com)

---

## Selected work

| 專案 | 我解決的問題 | 做法與證據 |
|---|---|---|
| **[Campus One](https://github.com/Miiduoa/graduation)** | 校園資訊分散，學生要在多個系統間找下一步 | Expo + Next.js + Firebase；整合課程、訊息、地圖、交通、學習風險與行動建議，保留跨端驗證與規則 |
| **[Nolu](https://github.com/Miiduoa/web)** | 登入、主要 region 或網路出問題時，資料與身份邊界仍要保持正確 | PWA + Supabase；hot standby、durable outbox、Ed25519 replication、guest privacy、provider mesh 與 resilience contract tests |
| **[Retail Ops DSS](https://github.com/Miiduoa/retail-ops-dss)** | 門市補貨與排班容易只靠經驗 | 時間切分、MA-7 baseline、Random Forest、MAE/MAPE，加上 Streamlit 決策介面 |
| **[Rail Ops Briefing DSS](https://github.com/Miiduoa/rail-ops-briefing-dss)** | 營運異常發生時，值班資訊很多，但不一定知道哪個區段該先處理 | incident contract、重複事件去重、active window、情境衝擊、priority ranking 與 Markdown briefing；合成情境與真實營運資料明確分開 |
| **[nowrite](https://github.com/Miiduoa/nowrite)** | 文字轉手寫工具常停在單次腳本，缺少完整操作流程 | Vue + FastAPI + Electron；支援圖片 / PDF、多語、自訂字型與 macOS / Windows 封裝 |
| **[Reliable LINE Webhook](https://github.com/Miiduoa/line-bot)** | Webhook 已接收，但外部 Reply API 暫時失敗時不能直接丟資料 | Flask + SQLite durable inbox/outbox、persistent event dedup、lease、retry/backoff、dead-letter 與 restart tests |

### Focused labs

這裡只留有明確問題、可執行程式與驗證方式的實驗。較早期課堂練習保留在 Git 歷史，不當成作品展示。

#### Data & decision quality

- **[competition-lab](https://github.com/Miiduoa/competition-lab)** — 整理 Kaggle、DrivenData、AI CUP 與鐵道資料企劃；明確區分本地驗證、baseline 與官方成績。
- **[mymis · Product Analytics Lab](https://github.com/Miiduoa/mymis)** — A/B test、confidence interval、SRM、MDE、guardrails、funnel 與 timezone-aware cohort retention；把資料品質、實驗有效性與後續留存放在同一條可驗證流程。
- **[stock · Walk-forward Backtest Lab](https://github.com/Miiduoa/stock)** — 把 look-ahead bias、交易成本、benchmark 與 walk-forward 驗證放進同一套回測流程。
- **[Demand Sensing Lite](https://github.com/Miiduoa/demand-sensing-lite)** — 多 SKU 合成需求、嚴格時間切分、HistGradientBoosting forecast，再接 (s,S) / Days-of-Cover 補貨模擬與服務水準／庫存 KPI；end-to-end CI 可重現。
- **[DriveCost Lab](https://github.com/Miiduoa/pucar)** — 把車貸、折舊、油耗、稅費、保險與保養放進同一個持有成本模型；情境可透過 URL 保存，核心計算有單元測試。
- **[Byline](https://github.com/Miiduoa/byline)** — CSV dataset contract；欄位、型別、null rate、row count 與 SHA-256 可被 code review，breaking change 可直接擋 CI。

#### Systems & reliability

- **[IoT Sensor Data Pipeline](https://github.com/Miiduoa/air)** — Row-level quarantine、freshness / duplicate / range checks、accepted ratio、latest lag 與 pipeline health；壞 row 不拖垮整批 ingestion。
- **[anyone](https://github.com/Miiduoa/anyone)** — 匿名回饋服務；Idempotency-Key、rate limit、pending moderation、append-only audit trail 與 Node built-in tests。
- **[Aortal · API Contract Guard](https://github.com/Miiduoa/aortal)** — 從 JSON sample 推導 contract，檢查 required field、型別、nullable 與 breaking change。
- **[ERP · Inventory Event Ledger](https://github.com/Miiduoa/ERP)** — append-only inventory events、replayable balances、duplicate-event 與 negative-inventory checks。
- **[bitest · BI Regression Checks](https://github.com/Miiduoa/bitest)** — 對 baseline / current CSV 做 schema、row count、null rate、主鍵重複與指標漂移檢查，CI 直接阻擋資料品質退化。
- **[math · Double-entry Ledger](https://github.com/Miiduoa/math)** — integer minor units、借貸平衡、duplicate transaction guard、trial balance 與月度損益。
- **[EventOps Console](https://github.com/Miiduoa/misnew)** — 離線活動簽到與容量控制；append-only event log、event id 去重、replay、localStorage 與基本 PWA offline shell。
- **[Policy Gate](https://github.com/Miiduoa/class501)** — 可解釋的授權 policy evaluator；RBAC + attribute conditions、deny-overrides、deterministic rule ordering 與 decision explanation。Repo 保留舊歷史憑證風險說明，不隱藏安全邊界。
- **[Webhook SLO Workbench](https://github.com/Miiduoa/line-bot-app)** — 把 eventual success 與 first-attempt reliability 分開，計算 p95 latency、retry recovery、error budget、burn rate 與 incident windows。

#### Mobile, learning & ML

- **[PUClass · Schedule Feasibility Engine](https://github.com/Miiduoa/puclass)** — 不只抓衝堂，也檢查跨校舍移動、tight / unknown transition、alternative section 搜尋與 timezone-aware ICS 匯出；核心規則無框架依賴並有 Node 測試。
- **[PlanningCore · Swift](https://github.com/Miiduoa/tired/tree/main)** — 純 Swift weekly planner；可測 priority、deadline、busy blocks、locked tasks 與 capacity。只連到已整理的 `main` 實作，不把未驗證的完整 App 當成成果。
- **[Gesture · Motion Lab](https://github.com/Miiduoa/Gesture)** — Android accelerometer → magnitude → RMS / peak → Steady / Moving / Shake；分類邏輯可獨立測試。
- **[Game2D.2 · Deterministic Simulation Lab](https://github.com/Miiduoa/Game2D.2)** — 60 Hz fixed-step、AABB collision、seeded PRNG、replay checksum 與 regression tests；同一 seed + input sequence 必須得到完全相同狀態。
- **[llm · Fine-tuning Pipeline Lab](https://github.com/Miiduoa/llm)** — LoRA training、JSONL contract、infer/eval config、tracking 與 config/data CI；不宣稱未提供的 benchmark。
- **[Grounded Search Lab](https://github.com/Miiduoa/cloudchatbot)** — 先做 BM25 retrieval、來源保留與 abstain，再用 Recall@k / MRR 檢查檢索品質；示範資料與正式規章清楚分開。
- **[CS Notes Reader](https://github.com/Miiduoa/cs-textbook-site)** — Offline-first 閱讀器；加權搜尋、Service Worker、localStorage 進度與內容完整性檢查。

---

## How I build

**先定義問題，再決定技術。**  
分析專案至少保留 baseline、驗證方式與限制；系統專案則把失敗情境、資料邊界與可恢復性一起測。

**把結果做成可以操作的東西。**  
比起只交 notebook，我更常把結果接成 Web、Mobile、Dashboard、CLI 或桌面工具。

**留下可檢查的證據。**  
README、測試、執行方式、資料來源與已知限制都放在 repo 裡，讓別人能快速判斷作品做到哪裡。

---

## Stack I actually use

`Python` · `scikit-learn` · `Pandas` · `Streamlit`  
`JavaScript / TypeScript` · `React / Next.js` · `React Native / Expo`  
`Swift / SwiftUI` · `Kotlin / Jetpack Compose` · `Vue` · `FastAPI` · `Firebase` · `Supabase` · `GitHub Actions`
