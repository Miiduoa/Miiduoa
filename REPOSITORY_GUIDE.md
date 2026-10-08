# 專案導覽

這份清單按「審查時能回答什麼問題」排序，不按建立日期、commit 數量或程式碼行數。想快速了解目前的實作能力，從前五個作品開始；課堂作業、早期原型和單點實驗不應跟它們放在同一層比較。

## 先看五個有完整脈絡的作品

| 想評估的能力 | 專案 | 從哪裡開始 |
| --- | --- | --- |
| 跨端架構、角色流程與測試 | **[Campus One](https://github.com/Miiduoa/graduation)** | [案例介紹](https://miiduoa.github.io/case-studies/campus-one/) → [兩分鐘審查](https://github.com/Miiduoa/graduation/blob/main/docs/REVIEW_IN_2_MINUTES.md) → [測試紀錄](https://github.com/Miiduoa/graduation/blob/main/docs/TESTING_EVIDENCE.md) |
| API 版本相容性與不完整資訊的處理 | **[Contractscope](https://github.com/Miiduoa/contractscope)** | [工程案例](https://miiduoa.github.io/case-studies/contractscope/) → [線上操作](https://miiduoa.github.io/contractscope/) → [規則定義](https://github.com/Miiduoa/contractscope/blob/main/docs/rules.md) |
| 重試、租約、冪等與可重現模擬 | **[Relaylab](https://github.com/Miiduoa/relaylab)** | [工程案例](https://miiduoa.github.io/case-studies/relaylab/) → [線上操作](https://miiduoa.github.io/relaylab/) → [模型假設](https://github.com/Miiduoa/relaylab/blob/main/docs/model.md) |
| 從預測到可授權、可稽核的決策流程 | **[Retail Ops DSS](https://github.com/Miiduoa/retail-ops-dss)** | [操作流程與截圖](https://github.com/Miiduoa/retail-ops-dss#30-秒-demo-路徑) → [權限程式](https://github.com/Miiduoa/retail-ops-dss/blob/main/src/access/policy.py) |
| 檔案處理、可檢查輸出與邊界測試 | **[Foldpress](https://github.com/Miiduoa/foldpress)** | [線上操作](https://miiduoa.github.io/foldpress/) → [拼版與列印限制](https://github.com/Miiduoa/foldpress/blob/main/docs/decisions.md) |

Campus One 是整合型系統；其餘四個作品各自處理一個能被測試的問題。讀 README 時可以特別注意範例輸入、失敗案例、測試與明確寫出的限制。

## 依主題延伸

**產品與瀏覽器工具**：[Motionbench](https://github.com/Miiduoa/motionbench)（動畫模型與匯出）、[Switchback](https://github.com/Miiduoa/switchback)（GPX 路線分析）、[Roomtone](https://github.com/Miiduoa/roomtone)（WAV 音訊剪輯）、[Tracefold](https://github.com/Miiduoa/tracefold)（HAR 效能記錄）、[Stillroom](https://github.com/Miiduoa/stillroom)（圖片交付）、[Cuework](https://github.com/Miiduoa/cuework)（字幕時間軸）。

**資料工程與決策**：[Competition Lab](https://github.com/Miiduoa/competition-lab)（競賽紀錄與程式）、[mymis](https://github.com/Miiduoa/mymis)（產品分析）、[byline](https://github.com/Miiduoa/byline)（CSV 契約）、[bitest](https://github.com/Miiduoa/bitest)（BI 驗證）、[stock](https://github.com/Miiduoa/stock)（回測）、[Capacity](https://miiduoa.github.io/tools/capacity/) / [Carry](https://miiduoa.github.io/tools/carry/)（排隊與現金流模型）。

**服務與可靠性**：[Patchday](https://github.com/Miiduoa/patchday)（SQLite migration 預演）、[line-bot](https://github.com/Miiduoa/line-bot)（Webhook inbox / outbox）、[web](https://github.com/Miiduoa/web)（學生規劃 PWA）、[nowrite](https://github.com/Miiduoa/nowrite)（文字轉手寫圖與 PDF）。

## 工程實驗

作品集網站的 Labs 區收錄 [Tracepath](https://miiduoa.github.io/labs/tracepath/)（追蹤）、[Flagrail](https://miiduoa.github.io/labs/flagrail/)（功能旗標）、[LineageGuard](https://miiduoa.github.io/labs/lineageguard/)（結構沿革）、[TxnScope](https://miiduoa.github.io/labs/txnscope/)（樂觀鎖）、[SessionSentry](https://miiduoa.github.io/labs/sessionsentry/)（工作階段）、[Eventlane](https://miiduoa.github.io/labs/eventlane/)（事件投遞）、[Syncbench](https://miiduoa.github.io/labs/syncbench/)（離線同步）與 [Rampwatch](https://miiduoa.github.io/labs/rampwatch/)（漸進發布）與 [Recovergrid](https://miiduoa.github.io/labs/recovergrid/)（災難復原情境）。

這些是刻意縮小範圍的模型或互動示範，**不是完整 SaaS 產品**。另外還有 [ERP](https://github.com/Miiduoa/ERP)、[learnpy](https://github.com/Miiduoa/learnpy)、[Game2D.2](https://github.com/Miiduoa/Game2D.2) 等題目，保留作為技術練習紀錄。

## 歷史版本與展示範圍

Campus One 早期架構、設計原型與測試部署環境保留在私人儲存庫，不列入公開作品；公開導覽不連到需要權限才能開啟的頁面。

[ERP](https://github.com/Miiduoa/ERP)、[learnpy](https://github.com/Miiduoa/learnpy)、[Game2D.2](https://github.com/Miiduoa/Game2D.2) 等是練習與歷史紀錄，不和上面的精選專案混作已交付產品。完整公開清單可從 [Repositories](https://github.com/Miiduoa?tab=repositories) 查看。

## 檢查一個專案的方式

先確認輸入與預期輸出，再自己重現其中一個錯誤情境。接著看核心邏輯是否獨立於 UI、測試是否真的覆蓋邊界，以及文件有沒有區分原型、合成資料、已驗證結果和待完成工作。作品的價值不在 commit 次數，而在能不能被別人讀懂、執行和質疑。

[回到 GitHub 首頁](README.md) · [開啟完整網站](https://miiduoa.github.io/)
