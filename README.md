# 顧晉瑋 · Miiduoa

靜宜大學資訊管理學系。跨端產品、資料分析與可靠性工程。

[作品集](https://miiduoa.github.io) · [Campus One 案例介紹](https://miiduoa.github.io/case-studies/campus-one/) · [專案導覽](REPOSITORY_GUIDE.md) · [Kaggle](https://www.kaggle.com/kuchinwei) · [Email](mailto:demohan513@gmail.com)

從 **Campus One** 的案例介紹開始，或直接開啟下面的工具。各專案附有執行方式、測試與設計限制。

## 精選作品

<a href="https://miiduoa.github.io/foldpress/"><img src="https://raw.githubusercontent.com/Miiduoa/foldpress/main/docs/screenshot.png" width="49%" alt="Foldpress 的 PDF 頁序、紙張與拼版預覽" /></a>
<a href="https://miiduoa.github.io/relaylab/"><img src="https://raw.githubusercontent.com/Miiduoa/relaylab/main/docs/screenshot.png" width="49%" alt="Relaylab 的 worker 投遞時間軸、訊息狀態與事件紀錄" /></a>

| 作品 | 用途 | 技術重點 |
| --- | --- | --- |
| **[Campus One](https://github.com/Miiduoa/graduation)** · [案例介紹](https://miiduoa.github.io/case-studies/campus-one/) | **旗艦專案**：把課程、訊息、地圖、交通與角色資料流接成同一套跨端校園產品 | Expo · Next.js · Firebase · shared contracts · rules tests · CI / E2E |
| **[Foldpress](https://github.com/Miiduoa/foldpress)** · [開啟工具](https://miiduoa.github.io/foldpress/) | 把 PDF 排成可對折裝訂的小冊子，先確認頁序，再匯出列印檔 | TypeScript · PDF 拼版 · 檔案在瀏覽器處理 |
| **[Relaylab](https://github.com/Miiduoa/relaylab)** · [開啟模擬器](https://miiduoa.github.io/relaylab/) | 沿著投遞時間軸查看重試與租約過期，比較冪等寫入前後的結果 | TypeScript · 離散事件模擬 · 種子重播 · CLI |
| **[Contractscope](https://github.com/Miiduoa/contractscope)** · [開啟工具](https://miiduoa.github.io/contractscope/) | 比較兩版 OpenAPI 合約，檢查呼叫端可能受到的影響 | TypeScript · 相容性規則 · CLI · [設計說明](https://github.com/Miiduoa/contractscope/blob/main/docs/design.zh-TW.md) |
| **[Motionbench](https://github.com/Miiduoa/motionbench)** · [開啟工具](https://miiduoa.github.io/motionbench/) | 調整彈簧與 Bézier 動畫，查看曲線並匯出程式碼 | TypeScript · 數值模型 · CSS easing · [設計說明](https://github.com/Miiduoa/motionbench/blob/main/docs/design.zh-TW.md) |
| **[Retail Ops DSS](https://github.com/Miiduoa/retail-ops-dss)** | 銷量預測接到補貨與人力規劃 | Python · 時間切分 · Baseline 比較 |
| **[Carry](https://miiduoa.github.io/tools/carry/)** · [計算模型](https://github.com/Miiduoa/Miiduoa.github.io/tree/main/tools/carry) | 貸款與現金購買的期末淨資產比較；納入剩餘債務與四種投資情境 | JavaScript · 現金流模型 · 數學測試 |
| **[Capacity](https://miiduoa.github.io/tools/capacity/)** · [計算模型](https://github.com/Miiduoa/Miiduoa.github.io/tree/main/tools/capacity) | 服務席次的排隊機率、尖峰負載及目標等待時間比較 | Erlang C · 排隊理論 · SVG · 測試 |

## 更多工具

- **[Switchback](https://github.com/Miiduoa/switchback)** · [開啟工具](https://miiduoa.github.io/switchback/) — 讀取 GPX 路線，在路線圖與海拔剖面間查看分段紀錄。
- **[Roomtone](https://github.com/Miiduoa/roomtone)** · [開啟工具](https://miiduoa.github.io/roomtone/) — 剪取音訊、調整淡入淡出與音量，匯出 WAV。
- **[Stillroom](https://github.com/Miiduoa/stillroom)** · [開啟工具](https://miiduoa.github.io/stillroom/) — 整理圖片尺寸、格式與交付檔案。
- **[Cuework](https://github.com/Miiduoa/cuework)** · [開啟工具](https://miiduoa.github.io/cuework/) — 編修 SRT / VTT 字幕、校正時間並檢查重疊。
- **[Tracefold](https://github.com/Miiduoa/tracefold)** · [開啟工具](https://miiduoa.github.io/tracefold/) — 從 HAR 找出慢請求、傳輸量與網路錯誤。
- **[Patchday](https://github.com/Miiduoa/patchday)** · [範例報告](https://miiduoa.github.io/patchday/) — 在獨立快照預演 SQLite migration，檢查結構差異與資料損失。

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
