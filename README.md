# 顧晉瑋 / Miiduoa

靜宜大學資訊管理學系｜跨端應用、資料分析、系統可靠性

我喜歡從一個明確的使用情境開始做軟體：畫面要能操作，核心規則要能測，遇到錯誤時也要知道系統會怎麼處理。這裡放的是目前還在維護、能看到實作與設計取捨的作品。

**[個人作品集](https://miiduoa.github.io/)** · [Campus One 案例](https://miiduoa.github.io/case-studies/campus-one/) · [完整專案索引](REPOSITORY_GUIDE.md) · [Kaggle](https://www.kaggle.com/kuchinwei) · [聯絡我](mailto:demohan513@gmail.com)

## 從這幾個專案開始

### 01 — [Campus One](https://github.com/Miiduoa/graduation) · 校園跨端系統

課表、訊息、地圖和校園服務不應該是彼此孤立的入口。Campus One 把 Mobile、Web 與後端接成同一套資料流程，處理共用型別、角色權限、安全導頁與服務不可用時的替代路徑。

**Expo / React Native · Next.js · Firebase · TypeScript**

[查看實際畫面與案例](https://miiduoa.github.io/case-studies/campus-one/) · [兩分鐘程式審查路徑](https://github.com/Miiduoa/graduation/blob/main/docs/REVIEW_IN_2_MINUTES.md) · [測試紀錄](https://github.com/Miiduoa/graduation/blob/main/docs/TESTING_EVIDENCE.md)

### 02 — [Contractscope](https://github.com/Miiduoa/contractscope) · API 合約比較

比較兩個 OpenAPI 版本時，新增欄位不一定就是安全變更，請求與回應的相容方向也不同。這個工具會標出變更、對應規則與可能受影響的操作；規則沒涵蓋的部分不會被誤報成「沒有問題」。

**TypeScript · OpenAPI · Browser + CLI**

[操作工具](https://miiduoa.github.io/contractscope/) · [規則與限制](https://github.com/Miiduoa/contractscope/blob/main/docs/rules.md)

### 03 — [Relaylab](https://github.com/Miiduoa/relaylab) · 訊息投遞模擬器

讓 ACK 遺失、租約過期和重試在時間軸上看得見。相同亂數種子可以重播執行過程，對照冪等寫入如何避免重複副作用；瀏覽器介面與 CLI 共用一套離散事件核心。

**TypeScript · Deterministic simulation · CLI**

[操作模擬器](https://miiduoa.github.io/relaylab/) · [模型與假設](https://github.com/Miiduoa/relaylab/blob/main/docs/model.md)

### 04 — [Retail Ops DSS](https://github.com/Miiduoa/retail-ops-dss) · 零售決策支援原型

從銷量預測延伸到補貨和人力建議，另外實作門市範圍、角色授權、敏感操作再驗證與稽核。資料是**固定種子的合成資料**，適合展示模型與操作流程，不冒充真實營運成效。

**Python · Streamlit · scikit-learn · SQLite**

[執行與驗證](https://github.com/Miiduoa/retail-ops-dss#如何執行) · [介面截圖](https://github.com/Miiduoa/retail-ops-dss/tree/main/docs/screenshots)

### 05 — [Foldpress](https://github.com/Miiduoa/foldpress) · PDF 小冊拼版

把普通 PDF 重新安排成可對折裝訂的小冊子。先在瀏覽器核對紙張正反面與頁序，再產生列印檔；測試會重新讀回輸出 PDF，檢查頁面尺寸、排列與旋轉。

**TypeScript · PDF processing · Browser-only**

[操作工具](https://miiduoa.github.io/foldpress/) · [設計取捨](https://github.com/Miiduoa/foldpress/blob/main/docs/decisions.md)

<a href="https://miiduoa.github.io/relaylab/"><img src="https://raw.githubusercontent.com/Miiduoa/relaylab/main/docs/screenshot.png" width="49%" alt="Relaylab 的投遞時間軸及 worker 狀態" /></a>
<a href="https://miiduoa.github.io/foldpress/"><img src="https://raw.githubusercontent.com/Miiduoa/foldpress/main/docs/screenshot.png" width="49%" alt="Foldpress 的紙張與頁序工作台" /></a>

## 其他值得打開的工具

- **網路與資料庫**：[Tracefold](https://github.com/Miiduoa/tracefold)（HAR 分析）、[Patchday](https://github.com/Miiduoa/patchday)（SQLite migration 預演）
- **互動與媒體**：[Motionbench](https://github.com/Miiduoa/motionbench)（動畫曲線）、[Switchback](https://github.com/Miiduoa/switchback)（GPX 路線）、[Roomtone](https://github.com/Miiduoa/roomtone)（音訊剪輯）
- **分析與實驗**：[Competition Lab](https://github.com/Miiduoa/competition-lab)（競賽紀錄與可重現程式）、[Carry / Capacity](https://miiduoa.github.io/)（現金流與排隊量能模型）

如果要深入看程式，不妨先跑專案提供的範例與測試，再對照 README 寫出的支援範圍和已知限制。競賽的本地驗證與官方成績、原型資料與真實資料，會分開標示。

[更多專案、工程實驗與歷史版本 →](REPOSITORY_GUIDE.md)
