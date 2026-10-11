# 顧晉瑋

靜宜大學資訊管理學系。開發跨端應用與資料工具，關注角色權限、API 相容性，以及服務中斷後的資料處理。

[作品集](https://miiduoa.github.io/) · [專案索引](REPOSITORY_GUIDE.md) · [Email](mailto:demohan513@gmail.com) · [Kaggle](https://www.kaggle.com/kuchinwei)

## Campus One

校園服務原型，整合課表、訊息、地圖與校園入口。行動端使用 Expo / React Native，Web 使用 Next.js，搭配 Firebase 後端與共用 TypeScript 型別。

學生、教師與管理者使用不同的資料範圍與操作權限；專案也包含登入失敗、安全導頁和外部服務無法連線時的處理。

<p align="center">
  <a href="https://github.com/Miiduoa/graduation">
    <img src="https://raw.githubusercontent.com/Miiduoa/graduation/51205ceb9f4b2b5940da64559bbdd2aabc8beac7/docs/mobile-screenshots/m_student_03_campus.png" alt="Campus One 原型的行動端校園服務入口" width="200">
  </a>
</p>

[程式碼](https://github.com/Miiduoa/graduation) · [架構與畫面](https://miiduoa.github.io/case-studies/campus-one/) · [測試與限制](https://github.com/Miiduoa/graduation/blob/main/docs/TESTING_EVIDENCE.md)

## Contractscope

比較兩份 OpenAPI 規格，列出變更位置、前後值與相容性判定。瀏覽器工作台與 CLI 共用 TypeScript 核心，未支援的規則會在報告中標示。

<a href="https://miiduoa.github.io/contractscope/">
  <img src="https://raw.githubusercontent.com/Miiduoa/contractscope/bdc544e10e649f0392c7a97e0379aa5fd4603157/docs/screenshot.png" alt="Contractscope 工作台：使用範例合約比較 API 變更" width="840">
</a>

[開啟工具](https://miiduoa.github.io/contractscope/) · [程式碼](https://github.com/Miiduoa/contractscope) · [規則範圍](https://github.com/Miiduoa/contractscope/blob/main/docs/rules.md)

## Relaylab

可重播的訊息佇列模擬器。透過 ACK 遺失、租約到期與重試情境，觀察重複投遞和冪等寫入；瀏覽器與 CLI 共用模擬核心。

[開啟模擬器](https://miiduoa.github.io/relaylab/) · [程式碼](https://github.com/Miiduoa/relaylab) · [模型假設](https://github.com/Miiduoa/relaylab/blob/main/docs/model.md)

## Retail Ops DSS

使用合成銷量資料的零售決策支援原型，包含預測、補貨建議、門市資料授權與操作稽核。以 Python、Streamlit、scikit-learn 和 SQLite 實作。

[程式與執行方式](https://github.com/Miiduoa/retail-ops-dss) · [存取控制](https://github.com/Miiduoa/retail-ops-dss/blob/main/src/access/policy.py)

## 其他工具

[Foldpress](https://github.com/Miiduoa/foldpress) 提供 PDF 小冊子拼版。其他音訊、圖片、字幕工具與實驗整理在[專案索引](REPOSITORY_GUIDE.md)。
