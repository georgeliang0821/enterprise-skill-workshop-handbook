# Lab 1 素材:Portal 雛型(M0 講師 Demo 用 / 學員選做)

> **重構版定位變更**:這一段不再是學員 Lab。M0 開場時由講師 live demo——先跑完成版 Portal 給大家看終點,再示範把 `prompt.md` 貼進 Agent mode 生成專案的過程(看個開頭即可,不用等跑完)。學員拿到的是完成版專案;想自己重現的,照下面步驟課後十分鐘就能做完。

## 給講師:M0 Demo 流程(15 分鐘)

1. 開完成版專案,`npm run dev`,展示六個區塊(Upload / Summary / Decisions / Action Items / Risks / Search)用假資料動起來——今天所有 Skill 的產出,最終都對應到這個畫面上的某一塊。
2. 開一個空資料夾,把 `prompt.md` 整段貼進 Agent mode 送出,讓大家看拆檔、寫檔的過程開頭,然後切回完成版。
3. 留下今天最重要的提問(中午前 M2a 會回來收):
   > **「一段夠詳細的 prompt 可以生出一整個專案。那——你的同事明天要做出結構一模一樣的東西,靠什麼保證他做出來的跟你一致?」**

## 給學員:課後自行重現(選做)

### 環境需求

- Node.js 18+(建議 20 LTS)
- VS Code + GitHub Copilot,**Agent mode 可用**

### 操作步驟

1. 建立空資料夾(例如 `meeting-intelligence-portal`),VS Code 開啟。
2. Copilot Chat 切到 **Agent mode**(不是 Ask 模式),貼上 `prompt.md` 裡 ```text 區塊的整段 prompt,送出。
3. 等 Copilot 跑完拆檔、寫檔、組裝(通常 1-3 分鐘)。
4. 安裝並啟動:

```powershell
npm install
npm run dev
```

5. 瀏覽器開啟終端機顯示的網址(通常 `http://localhost:5173`),確認六個區塊都出現。

### 常見狀況與排除

| 狀況 | 處理方式 |
|---|---|
| Copilot 沒有裝 `@fluentui/react-components` | 手動 `npm install @fluentui/react-components` 後重新整理 |
| 畫面樣式跑掉、卡片沒有分隔感 | 屬正常現象,重點不是像素級還原,六個區塊都在、資料正確顯示即可 |
| Agent mode 跑到一半卡住 | 直接中斷,檢查已產生的檔案,缺的用 Chat 補問(例如「幫我補上 RisksPanel.jsx」) |

### 完成檢核(自行重現時)

- [ ] `npm run dev` 能啟動
- [ ] 六個區塊都在畫面上
- [ ] 假資料集中在 `mockData.js`,不是寫死在各元件裡
