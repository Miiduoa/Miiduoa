# 顧晉瑋 / Miiduoa

靜宜大學資訊管理學系。目前主要維護 Campus One，整理校園服務在行動端與 Web 之間的資料、登入和角色權限。

[作品集](https://miiduoa.github.io/) · [專案索引](REPOSITORY_GUIDE.md) · [Kaggle](https://www.kaggle.com/kuchinwei) · [Email](mailto:demohan513@gmail.com)

## Campus One

[程式碼](https://github.com/Miiduoa/graduation) · [畫面與實作](https://miiduoa.github.io/case-studies/campus-one/) · [程式導讀](https://github.com/Miiduoa/graduation/blob/main/docs/REVIEW_IN_2_MINUTES.md)

把課表、訊息、地圖與校園服務整合在同一個 App，並提供 Web 介面。行動端使用 Expo / React Native，Web 使用 Next.js，後端包含 Firebase，兩端共用 TypeScript 型別。

這個專案的重點不只是畫面：學生、教師與管理員能操作的資料不同，登入失敗、權限變更和服務無法連線，也需要有對應的處理流程。

主線程式放在 `graduation`。開發中的改動、測試結果與發布進度分開看：[待合併修改](https://github.com/Miiduoa/graduation/pulls) · [自動化檢查](https://github.com/Miiduoa/graduation/actions) · [測試與限制](https://github.com/Miiduoa/graduation/blob/main/docs/TESTING_EVIDENCE.md)。

## 其他作品

### [Contractscope](https://github.com/Miiduoa/contractscope)

比較兩份 OpenAPI 規格，逐項列出變更位置、前後值與相容性判定。瀏覽器介面與 CLI 共用 TypeScript 比較核心；未涵蓋的規則另列，不把「沒有偵測到」當成「一定相容」。

[開啟工具](https://miiduoa.github.io/contractscope/) · [實作說明](https://miiduoa.github.io/case-studies/contractscope/) · [規則範圍](https://github.com/Miiduoa/contractscope/blob/main/docs/rules.md)

### [Retail Ops DSS](https://github.com/Miiduoa/retail-ops-dss)

用銷量預測推算補貨與人力需求，另實作門市授權和稽核紀錄。使用 Python、Streamlit、scikit-learn 與 SQLite；這是使用固定種子合成資料的原型，不是實際門市的營運成果。

[程式與執行方式](https://github.com/Miiduoa/retail-ops-dss) · [介面截圖](https://github.com/Miiduoa/retail-ops-dss/tree/main/docs/screenshots) · [權限邏輯](https://github.com/Miiduoa/retail-ops-dss/blob/main/src/access/policy.py)

### 工具與模擬

- [Foldpress](https://github.com/Miiduoa/foldpress)：把 PDF 排成可雙面列印、對折裝訂的小冊子。[開啟工具](https://miiduoa.github.io/foldpress/)
- [Relaylab](https://github.com/Miiduoa/relaylab)：模擬佇列投遞，觀察 ACK 遺失、租約到期與重複寫入。[開啟模擬器](https://miiduoa.github.io/relaylab/)

音訊、圖片、字幕工具與其他實驗放在[專案索引](REPOSITORY_GUIDE.md)。
