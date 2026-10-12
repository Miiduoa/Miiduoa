# 專案索引

[GitHub 首頁](README.md) · [作品集網站](https://miiduoa.github.io/)

先看主要專案的畫面與用途，再依興趣往下讀程式。瀏覽器工具、模擬實驗和課程練習分開整理，不把小型實驗當成正式服務。

## 主要專案

### Campus One｜跨端校園服務

整合課表、訊息、地圖與角色入口。行動端、Web、後端與資料授權分層實作；仍是開發中的原型，部分流程使用示範資料，外部串接須有對應環境。

[畫面與實作](https://miiduoa.github.io/case-studies/campus-one/) → [架構](https://github.com/Miiduoa/graduation/blob/main/docs/ARCHITECTURE_OVERVIEW.md) → [角色與資料邊界](https://github.com/Miiduoa/graduation/blob/main/docs/APP_ROLE_DATA_FLOW_ARCHITECTURE.md) → [測試與限制](https://github.com/Miiduoa/graduation/blob/main/docs/TESTING_EVIDENCE.md)

[原始碼](https://github.com/Miiduoa/graduation) · [CI 執行紀錄](https://github.com/Miiduoa/graduation/actions/workflows/ci.yml)

### Contractscope｜OpenAPI 變更比較

比較同一支 API 的前後版本，列出受影響的操作、判斷規則與相容性。未支援的規則會回報涵蓋不完整，不當成「沒有問題」。

先在[工作台](https://miiduoa.github.io/contractscope/)載入範例、比較兩份規格，再交換前後版本重新比較，觀察輸入與輸出方向如何影響結果。接著看[規則文件](https://github.com/Miiduoa/contractscope/blob/main/docs/rules.md)與[比較核心](https://github.com/Miiduoa/contractscope/blob/main/src/core/index.ts)。

[原始碼與 CLI](https://github.com/Miiduoa/contractscope) · [實作紀錄](https://miiduoa.github.io/case-studies/contractscope/)

### Relaylab｜訊息投遞與重試

以固定種子重播確認訊息遺失、重試與租約競態。這是離散事件模擬，不是實際訊息代理服務，也不是壓力測試。

在[模擬器](https://miiduoa.github.io/relaylab/)播放預設情境，再開啟「冪等寫入」並套用設定。要觀察的是：重複投遞仍然發生，但第二次寫入是否被抑制。對照[模擬核心](https://github.com/Miiduoa/relaylab/blob/main/src/core/engine.ts)與[測試](https://github.com/Miiduoa/relaylab/blob/main/tests/engine.test.ts)。

[原始碼與 CLI](https://github.com/Miiduoa/relaylab) · [模型假設](https://github.com/Miiduoa/relaylab/blob/main/docs/model.md) · [實作紀錄](https://miiduoa.github.io/case-studies/relaylab/)

### Retail Ops DSS｜零售決策支援

以合成銷量資料展示預測、補貨、門市範圍與操作稽核。模型結果是實驗資料上的評估，不是店家實際營運成效。

依[執行方式](https://github.com/Miiduoa/retail-ops-dss#如何執行)啟動後，用不同示範帳號比較可見門市與操作權限。程式閱讀從[權限表](https://github.com/Miiduoa/retail-ops-dss/blob/main/src/access/policy.py)和[授權測試](https://github.com/Miiduoa/retail-ops-dss/blob/main/tests/test_access_control.py)開始。

[原始碼](https://github.com/Miiduoa/retail-ops-dss) · [操作畫面](https://github.com/Miiduoa/retail-ops-dss/tree/main/docs/screenshots)

### Foldpress｜PDF 小冊子拼版

調整雙面列印頁序，產生可對折裝訂的 PDF。[開啟工具](https://miiduoa.github.io/foldpress/)前可先讀[列印限制](https://github.com/Miiduoa/foldpress/blob/main/docs/decisions.md)；實際翻面方向仍須依印表機設定確認。

[原始碼與執行方式](https://github.com/Miiduoa/foldpress)

### Competition Lab｜競賽與實驗紀錄

收錄訓練程式、參賽筆記與成績來源。本地驗證分數與官方榜單分開記錄，企劃案與完成的系統也分開標示。

[程式與紀錄](https://github.com/Miiduoa/competition-lab) · [成績表](https://github.com/Miiduoa/competition-lab/blob/main/SCORES.md)

## 其他工具與應用

| 專案 | 用途 |
| --- | --- |
| [Nolu](https://github.com/Miiduoa/web) | 學生規劃 PWA；課表與日常安排 |
| [nowrite](https://github.com/Miiduoa/nowrite) | 文字轉手寫圖片與 PDF |
| [Roomtone](https://github.com/Miiduoa/roomtone) | 音訊剪輯、淡入淡出與 WAV 匯出 |
| [Stillroom](https://github.com/Miiduoa/stillroom) | 圖片尺寸、格式與批次匯出 |
| [Cuework](https://github.com/Miiduoa/cuework) | 字幕文字與時間編輯 |
| [Switchback](https://github.com/Miiduoa/switchback) | GPX 路線分析 |
| [Motionbench](https://github.com/Miiduoa/motionbench) | 動畫曲線預覽與程式碼匯出 |
| [Tracefold](https://github.com/Miiduoa/tracefold) | HAR 網路紀錄分析 |

## 資料與後端實作

| 專案 | 閱讀方向 |
| --- | --- |
| [mymis](https://github.com/Miiduoa/mymis) | 產品分析與資料品質 |
| [byline](https://github.com/Miiduoa/byline) | CSV 資料契約 |
| [bitest](https://github.com/Miiduoa/bitest) | BI 驗證 |
| [stock](https://github.com/Miiduoa/stock) | 回測實驗 |
| [Patchday](https://github.com/Miiduoa/patchday) | SQLite migration 預演 |
| [line-bot](https://github.com/Miiduoa/line-bot) | Webhook inbox / outbox、去重與重試 |

<details>
<summary>系統機制與數學模型實驗</summary>

以下是觀察特定機制的小型實驗，不等同於完成的分散式系統或營運服務。

| 主題 | 實驗 |
| --- | --- |
| 請求與發布 | [Tracepath](https://miiduoa.github.io/labs/tracepath/) · [Flagrail](https://miiduoa.github.io/labs/flagrail/) · [Rampwatch](https://miiduoa.github.io/labs/rampwatch/) |
| 資料與同步 | [LineageGuard](https://miiduoa.github.io/labs/lineageguard/) · [TxnScope](https://miiduoa.github.io/labs/txnscope/) · [Syncbench](https://miiduoa.github.io/labs/syncbench/) |
| 工作階段與投遞 | [SessionSentry](https://miiduoa.github.io/labs/sessionsentry/) · [Eventlane](https://miiduoa.github.io/labs/eventlane/) |
| 復原與稽核 | [Recovergrid](https://miiduoa.github.io/labs/recovergrid/) · [Proofline](https://miiduoa.github.io/labs/proofline/) |
| 數學模型 | [Carry](https://miiduoa.github.io/tools/carry/) 現金流比較 · [Capacity](https://miiduoa.github.io/tools/capacity/) 排隊量能估算 |

[實驗測試執行紀錄](https://github.com/Miiduoa/Miiduoa.github.io/actions/workflows/lab-tests.yml)

</details>

<details>
<summary>課程與早期練習</summary>

[ERP](https://github.com/Miiduoa/ERP) · [Gesture](https://github.com/Miiduoa/Gesture) · [Game2D.2](https://github.com/Miiduoa/Game2D.2) · [0925SQL](https://github.com/Miiduoa/0925SQL) · [learnpy](https://github.com/Miiduoa/learnpy)

保留學習過程，不列為主要作品，也不因為年代較早就移除原始碼。

</details>

---

[所有公開儲存庫](https://github.com/Miiduoa?tab=repositories) · [回到 GitHub 首頁](README.md)
