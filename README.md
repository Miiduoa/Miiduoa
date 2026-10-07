# 顧晉瑋 · Miiduoa

靜宜大學資訊管理學系。跨端產品、資料分析與可靠性工程。

[作品集](https://miiduoa.github.io) · [Campus One 案例介紹](https://miiduoa.github.io/case-studies/campus-one/) · [專案導覽](REPOSITORY_GUIDE.md) · [Kaggle](https://www.kaggle.com/kuchinwei) · [Email](mailto:demohan513@gmail.com)

> 第一次審查這個帳號：先看 **Campus One**，再看精選作品。未列在這裡的 repository 可能是技術研究、早期課堂重做或已被取代的歷史版本，不代表目前主線品質。

## 精選作品

<a href="https://miiduoa.github.io/switchback/"><img src="https://raw.githubusercontent.com/Miiduoa/switchback/main/docs/screenshot.png" width="49%" alt="Switchback 路線與海拔分析" /></a>
<a href="https://miiduoa.github.io/roomtone/"><img src="https://raw.githubusercontent.com/Miiduoa/roomtone/main/docs/screenshot.png" width="49%" alt="Roomtone 波形剪輯與音訊處理" /></a>

| 作品 | 用途 | 技術重點 |
| --- | --- | --- |
| **[Campus One](https://github.com/Miiduoa/graduation)** · [案例介紹](https://miiduoa.github.io/case-studies/campus-one/) | **旗艦專案**：把課程、訊息、地圖、交通與角色資料流接成同一套跨端校園產品 | Expo · Next.js · Firebase · shared contracts · rules tests · CI / E2E |
| **[Switchback](https://github.com/Miiduoa/switchback)** · [開啟工具](https://miiduoa.github.io/switchback/) | 讀取 GPX 路線，在路線圖與海拔剖面間查看分段紀錄 | TypeScript · 地理計算 · SVG 連動檢視 |
| **[Roomtone](https://github.com/Miiduoa/roomtone)** · [開啟工具](https://miiduoa.github.io/roomtone/) | 剪取音訊、調整淡入淡出與音量，匯出 WAV | Web Audio · 波形選段 · PCM 編碼 |
| **[Stillroom](https://github.com/Miiduoa/stillroom)** · [開啟工具](https://miiduoa.github.io/stillroom/) | 在瀏覽器整理圖片尺寸、格式與交付檔案 | TypeScript · Canvas · 批次處理 · ZIP 匯出 |
| **[Cuework](https://github.com/Miiduoa/cuework)** · [開啟工具](https://miiduoa.github.io/cuework/) | 編修 SRT / VTT 字幕、校正時間並檢查重疊 | TypeScript · Node.js · SQLite · 版本與衝突處理 |
| **[Tracefold](https://github.com/Miiduoa/tracefold)** · [開啟工具](https://miiduoa.github.io/tracefold/) | 從 HAR 找出慢請求、傳輸量與網路錯誤 | 時間軸 · 本機分析 · 實際網站案例 |
| **[Patchday](https://github.com/Miiduoa/patchday)** · [範例報告](https://miiduoa.github.io/patchday/) | 在獨立快照預演 SQLite migration | 交易回滾 · Schema 差異 · 資料損失警示 |
| **[Retail Ops DSS](https://github.com/Miiduoa/retail-ops-dss)** | 銷量預測接到補貨與人力規劃 | Python · 時間切分 · Baseline 比較 |

<a href="https://miiduoa.github.io/stillroom/"><img src="https://raw.githubusercontent.com/Miiduoa/stillroom/main/docs/screenshot.jpg" width="49%" alt="Stillroom 圖片交付工作台" /></a>
<a href="https://miiduoa.github.io/cuework/"><img src="https://raw.githubusercontent.com/Miiduoa/cuework/main/docs/screenshot.jpg" width="49%" alt="Cuework 字幕編輯工作台" /></a>

Switchback、Roomtone 與 Stillroom 在瀏覽器處理匯入檔案。Cuework 的線上版本使用瀏覽器儲存；SQLite 版本服務可依 repo 說明在本機啟動。

## 其他作品

- [nowrite](https://github.com/Miiduoa/nowrite) — 文字轉手寫圖片與 PDF，Vue / FastAPI / Electron。
- [Reliable LINE Webhook](https://github.com/Miiduoa/line-bot) — SQLite inbox / outbox、去重與失敗重試。
- [Byline](https://github.com/Miiduoa/byline) — 可放進版本控制的 CSV dataset contract。
- [Product Analytics Lab](https://github.com/Miiduoa/mymis) — A/B test、資料品質與 cohort 分析。

執行方式、測試與已知限制放在各專案的 README。

<details>
<summary>工程實驗</summary>

- [Tracepath](https://miiduoa.github.io/labs/tracepath/) — Distributed tracing
- [Flagrail](https://miiduoa.github.io/labs/flagrail/) — Feature flags
- [LineageGuard](https://miiduoa.github.io/labs/lineageguard/) — Schema evolution
- [TxnScope](https://miiduoa.github.io/labs/txnscope/) — Optimistic concurrency
- [SessionSentry](https://miiduoa.github.io/labs/sessionsentry/) — Session lifecycle
- [Eventlane](https://miiduoa.github.io/labs/eventlane/) — Event delivery
- [Syncbench](https://miiduoa.github.io/labs/syncbench/) — Offline synchronization
- [Rampwatch](https://miiduoa.github.io/labs/rampwatch/) — Release guardrails

[實驗原始碼](https://github.com/Miiduoa/Miiduoa.github.io/tree/main/labs)

</details>
