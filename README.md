# 顧晉瑋 · Miiduoa

**Information Management · Product Analytics · Decision Support · Applied ML**

靜宜大學資訊管理學系。  
我比較在意的不是「模型用了什麼」，而是資料能不能一路走到**可驗證的決策、介面與產品**。

[作品集網站](https://miiduoa.github.io) · [Kaggle](https://www.kaggle.com/kuchinwei) · [Email](mailto:demohan513@gmail.com)

---

## Selected work

| 專案 | 我解決的問題 | 做法與證據 |
|---|---|---|
| **[Retail Ops DSS](https://github.com/Miiduoa/retail-ops-dss)** | 門市補貨與排班容易只靠經驗 | 4 門市 × 4 品類 × 約 730 日合成資料；時間切分、MA-7 baseline、Random Forest、MAE/MAPE、Streamlit 決策介面 |
| **[Campus One](https://github.com/Miiduoa/graduation)** | 校園資訊分散，學生要在多個系統間找下一步 | Expo + Next.js + Firebase；把課程、訊息、地圖、交通、學習風險與行動建議整合成跨端原型 |
| **[nowrite](https://github.com/Miiduoa/nowrite)** | 文字轉手寫工具多停在單次腳本，缺少完整操作流程 | Vue + FastAPI + Electron；支援圖片 / PDF、多語介面、自訂字型與 macOS / Windows 桌面封裝 |
| **[competition-lab](https://github.com/Miiduoa/competition-lab)** | 競賽容易只留下分數，沒有可重現的思考過程 | 整理 Kaggle、DrivenData、AI CUP 與鐵道資料企劃的程式、驗證紀錄與提交結果，明確區分本地驗證與官方成績 |
| **[Tired](https://github.com/Miiduoa/tired)** | 多重身份下的任務、課程與時間容易互相衝突 | SwiftUI + Firebase iOS App；另抽出純 Swift PlanningCore，測試 priority、deadline、busy block、locked task 與 daily capacity |
| **[Nolu](https://github.com/Miiduoa/web)** | 登入、主要 region 或網路出問題時，學生資料與身份邊界仍要保持正確 | PWA + Supabase；hot standby、durable outbox、Ed25519 replication、guest privacy、provider mesh，以及大量 auth / failover / resilience contract tests |
| **[Byline](https://github.com/Miiduoa/byline)** | 上游 CSV 改欄位或型別時，分析流程常到最後才壞 | Python CLI 建立可 review 的 dataset contract；檢查欄位、型別、null rate、row count 與 SHA-256，breaking change 可直接擋 CI |
| **[Aortal](https://github.com/Miiduoa/aortal)** | API payload 的小改動可能直接破壞既有 consumer | Node.js 零 runtime dependency；從 JSON sample 推導 contract，遞迴檢查 required field、型別、nullable 與新增欄位，內建測試與 CI |
| **[anyone](https://github.com/Miiduoa/anyone)** | 匿名回饋服務要同時處理重複送出、審核與隱私邊界 | Express 後端；Idempotency-Key、防濫刷 rate limit、pending moderation、append-only audit trail、管理員 session 邊界與 Node built-in tests |
| **[line-bot](https://github.com/Miiduoa/line-bot)** | Webhook 已接收，但外部 Reply API 暫時失敗時不能直接丟資料 | Python + Flask + SQLite durable inbox/outbox；persistent event dedup、lease、exponential backoff、dead-letter metadata、worker CLI 與 restart tests |
| **[air](https://github.com/Miiduoa/air)** | IoT ingestion 遇到壞 row 時，不該讓整批資料一起失敗 | Row-level quarantine、freshness / duplicate / range checks、accepted ratio、healthy station ratio、latest lag、pipeline health 與 privacy-minimized quarantine |

### Systems & analytics labs

- **[mymis · Product Analytics Lab](https://github.com/Miiduoa/mymis)** — A/B test、sample ratio mismatch、funnel 與 event contract；先確認資料與分流可信，再解讀 lift。
- **[stock · Walk-forward Backtest Lab](https://github.com/Miiduoa/stock)** — 把 look-ahead bias、交易成本、benchmark 與 walk-forward 驗證放進同一套可測試回測流程。
- **[ERP · Inventory Event Ledger](https://github.com/Miiduoa/ERP)** — 用 append-only inventory events 重建庫存，檢查重複事件、負庫存與資料一致性。
- **[Gesture · Motion Lab](https://github.com/Miiduoa/Gesture)** — Android accelerometer → magnitude → RMS / peak → Steady / Moving / Shake；分類邏輯獨立測試。
- **[learnpy · Python Practice Judge](https://github.com/Miiduoa/learnpy)** — 用 Python AST 與 rubric 檢查函式、參數、迴圈、條件、禁止 API 等結構要求；明確區分 structural feedback 與語意正確性。
- **[CS Notes Reader](https://github.com/Miiduoa/cs-textbook-site)** — Offline-first 靜態閱讀器；加權全文搜尋、Service Worker、localStorage 閱讀進度，以及 CI 內容完整性檢查，不為了作品集硬塞 framework。
- **[n8n / Render SLO Guard](https://github.com/Miiduoa/n8n-render-deploy)** — Synthetic HTTP probes + append-only history；計算 availability、error budget、burn rate、p95 latency 與雙時間窗 alert severity，不把 deployment success 當成 reliability。
- **[0925SQL · SQL Analytics Mart](https://github.com/Miiduoa/0925SQL)** — SQLite schema、foreign key、index、window function、分析查詢與完整性測試；合成資料可重建。
- **[math · Double-entry Personal Finance Ledger](https://github.com/Miiduoa/math)** — 以 integer minor units、借貸平衡、duplicate transaction guard、trial balance 與月度損益維持帳務一致性。
- **[llm · Fine-tuning Pipeline Lab](https://github.com/Miiduoa/llm)** — LoRA training / JSONL data contract / infer-eval config / W&B-TensorBoard tracking；CI 驗證 YAML、DeepSpeed JSON 與資料契約，不宣稱未提供的 benchmark。
- **[PUClass](https://github.com/Miiduoa/puclass)** — 課程時段衝突、每週負荷與作業壓力檢查；核心邏輯以 Node.js 寫成可測試函式。
- **[Demand Sensing Lite](https://github.com/Miiduoa/demand-sensing-lite)** — 多 SKU 需求預測接到 `(s,S)` 補貨模擬，觀察預測誤差如何影響服務水準與庫存。
- **[Rail Ops Briefing DSS](https://github.com/Miiduoa/rail-ops-briefing-dss)** — 用營運 KPI、What-if 槓桿與規則建議做鐵道營運簡報原型。

---

## How I build

**先定義問題，再決定模型。**  
每個分析專案至少保留 baseline、驗證方式與限制，不把模型分數當成結論。

**把結果做成可以操作的東西。**  
比起只交 notebook，我更常把結果接成 Web、Mobile、Dashboard、CLI 或桌面工具。

**留下可檢查的證據。**  
README、測試、執行方式、資料來源與已知限制都放在 repo 裡，讓別人能快速判斷作品做到哪裡。較早期的課堂練習保留作為學習紀錄，不列入精選作品。

---

## Stack I actually use

`Python` · `scikit-learn` · `Pandas` · `Streamlit`  
`JavaScript / TypeScript` · `React / Next.js` · `React Native / Expo`  
`Swift / SwiftUI` · `Kotlin / Jetpack Compose` · `Vue` · `FastAPI` · `Firebase` · `GitHub Actions`
