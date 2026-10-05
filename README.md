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

### Systems & analytics labs

- **[mymis · Product Analytics Lab](https://github.com/Miiduoa/mymis)** — A/B test、sample ratio mismatch、funnel 與 event contract；先確認資料與分流可信，再解讀 lift。
- **[bitest · BI regression checks](https://github.com/Miiduoa/bitest)** — 對 baseline / current CSV 做 schema、row count、null rate、主鍵重複與指標漂移檢查，可直接放進 CI。
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
README、測試、執行方式、資料來源與已知限制都放在 repo 裡，讓別人能快速判斷作品做到哪裡。

---

## Stack I actually use

`Python` · `scikit-learn` · `Pandas` · `Streamlit`  
`JavaScript / TypeScript` · `React / Next.js` · `React Native / Expo`  
`Vue` · `FastAPI` · `Firebase` · `GitHub Actions`
