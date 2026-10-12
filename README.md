# 顧晉瑋

靜宜大學資訊管理學系。開發行動端與 Web 應用，也用 Python 做資料分析。

目前主要維護 **Campus One**。我關注的不只是畫面能不能操作，還包括不同角色能存取哪些資料，以及登入、連線或寫入失敗後，使用者能否繼續完成事情。

[作品集](https://miiduoa.github.io/) · [專案索引](REPOSITORY_GUIDE.md) · [Email](mailto:demohan513@gmail.com) · [Kaggle](https://www.kaggle.com/kuchinwei)

## Campus One

**校園資訊分散在不同系統，學生每天卻需要一起使用。** 這個專案把課表、訊息、地圖與校園服務整理到同一個介面，並提供學生、教師與管理者各自的操作入口。

<p align="center">
  <a href="https://miiduoa.github.io/case-studies/campus-one/">
    <img src="https://raw.githubusercontent.com/Miiduoa/graduation/51205ceb9f4b2b5940da64559bbdd2aabc8beac7/docs/mobile-screenshots/m_student_03_campus.png" alt="Campus One 開發版本：學生端的校園服務入口" width="240">
  </a>
</p>

行動端使用 Expo / React Native，Web 使用 Next.js，後端是 Firebase。共用 TypeScript 型別與角色規則，讓權限檢查不只停留在按鈕是否顯示。

這是開發中的校園服務原型，不是正式校務系統；部分畫面使用示範資料，外部服務串接仍依環境與憑證而定。

[畫面與實作](https://miiduoa.github.io/case-studies/campus-one/) · [原始碼](https://github.com/Miiduoa/graduation) · [架構](https://github.com/Miiduoa/graduation/blob/main/docs/ARCHITECTURE_OVERVIEW.md) · [測試與限制](https://github.com/Miiduoa/graduation/blob/main/docs/TESTING_EVIDENCE.md)

## 其他代表作

| 專案 | 解決的問題 | 閱讀入口 |
| --- | --- | --- |
| **[Contractscope](https://github.com/Miiduoa/contractscope)** | 比較兩版 OpenAPI，區分破壞性變更與尚未涵蓋的規則。瀏覽器與 CLI 共用比較核心。 | [開啟工具](https://miiduoa.github.io/contractscope/) · [比較規則](https://github.com/Miiduoa/contractscope/blob/main/docs/rules.md) |
| **[Relaylab](https://github.com/Miiduoa/relaylab)** | 用可重播的佇列模擬，觀察確認訊息遺失、租約到期與重複寫入。 | [操作模擬器](https://miiduoa.github.io/relaylab/) · [模型邊界](https://github.com/Miiduoa/relaylab/blob/main/docs/model.md) |
| **[Retail Ops DSS](https://github.com/Miiduoa/retail-ops-dss)** | 以合成銷量資料串起預測、補貨建議、門市授權與操作稽核。 | [執行方式](https://github.com/Miiduoa/retail-ops-dss#如何執行) · [權限程式](https://github.com/Miiduoa/retail-ops-dss/blob/main/src/access/policy.py) |
| **[Foldpress](https://github.com/Miiduoa/foldpress)** | 將 PDF 排成可雙面列印、對折裝訂的小冊子。 | [開啟工具](https://miiduoa.github.io/foldpress/) · [列印限制](https://github.com/Miiduoa/foldpress/blob/main/docs/decisions.md) |
| **[Competition Lab](https://github.com/Miiduoa/competition-lab)** | 競賽的訓練程式、實驗筆記與成績紀錄；本地驗證與官方成績分開記錄。 | [程式與紀錄](https://github.com/Miiduoa/competition-lab) |

## 從程式看實作

跨端資料與權限可以從 Campus One 的架構文件開始；API 相容性看 Contractscope 的規則與測試；重試和重複寫入看 Relaylab 的事件模型。每個專案的執行方式與限制都放在各自的 README。

音訊、圖片、字幕工具，以及較早期的課程練習，整理在[專案索引](REPOSITORY_GUIDE.md)。
