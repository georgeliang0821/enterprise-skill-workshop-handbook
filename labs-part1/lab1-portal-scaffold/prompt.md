# Lab 1 用 Prompt:建立 AI Meeting Intelligence Portal 雛型

> 用法:開一個新的空資料夾,VS Code 開啟後,在 Copilot **Agent mode**(不是單純 Chat)貼上下面整段 prompt。
> 這一步的目的不是產出完美的 UI,而是讓學員在 45 分鐘內看到「東西真的動起來」——這是整堂課故事線的起點。

```text
請幫我用 React + Vite 建立一個網頁專案,專案名稱叫 meeting-intelligence-portal。

這是一個「AI Meeting Intelligence Portal」的前端雛型,畫面由上到下依序是這幾個區塊(先用假資料/mock data,不用真的接後端 API,後端我們後面課程才會做):

1. 頁首標題:AI Meeting Intelligence Portal
2. Upload Transcript 區塊:一個檔案上傳按鈕 + 一個多行文字框,讓使用者可以貼上會議逐字稿文字(先不用真的處理上傳邏輯,按下按鈕後只要把文字框內容存進 React state 即可)
3. Meeting Summary 區塊:顯示一段摘要文字,先放假資料「專案進度正常」
4. Decisions 區塊:顯示一個編號清單,先放假資料:
   1. 採用 Azure OpenAI
   2. 下週進行 PoC
5. Action Items 區塊:顯示一個表格,欄位是 Owner / Action Item,先放假資料:
   - David -> PoC 架構設計
   - Mary -> 成本評估
   - George -> 資安需求確認
6. Risks 區塊:顯示一個清單,先放假資料:
   - Token Cost
   - Data Residency
7. Search 區塊:一個搜尋輸入框 + 搜尋按鈕,先放一個 placeholder「關鍵字:SAP」,按下搜尋後先不用真的查,只要把輸入的關鍵字印在畫面上即可

視覺風格要求:
- 使用 Fluent UI React（@fluentui/react-components）的元件來做卡片、按鈕、輸入框,不要用純 HTML 原生元件
- 每個區塊都用一張 Card 包起來,區塊之間要有清楚的視覺分隔(可以參考一般企業內部工具、微軟 M365 風格的簡潔配色)
- Responsive:手機寬度也要能正常閱讀,區塊改成上下堆疊
- 所有假資料都集中放在一個 mockData.js 檔案裡,不要寫死在元件裡面,方便我們之後替換成真的 API 回傳值

請把每個區塊拆成獨立的 React component(例如 UploadTranscript.jsx、MeetingSummary.jsx、DecisionsPanel.jsx、ActionItemsPanel.jsx、RisksPanel.jsx、SearchPanel.jsx),在 App.jsx 裡組裝起來,並且在結尾附上啟動專案的指令。
```

## 這一步之後你應該會拿到什麼

- 一個可以 `npm run dev` 跑起來的 React 專案
- 畫面長得跟你們的 mockup 手繪稿一致(六個區塊都在,資料是假的)
- 六個獨立元件檔案 + 一個 `mockData.js`

## 觀察重點(講師帶學員一起看)

跑起來之後,故意問學員兩個問題,銜接到 M1 的白話定義:

1. 「你剛剛下的這個指令,是 Prompt、Skill,還是 Agent?」——答案是 **Agent**:因為 Copilot 自己規劃了拆檔案、寫多個 component、串起 App.jsx 這一連串步驟,不是單一次問答就結束。
2. 「如果明天你的同事也要做一個一模一樣結構的 Portal,你要怎麼確保他做出來的六個區塊命名、風格、假資料格式都跟你一致?」——這個問題答不出來,就是這堂課接下來要解決的:**把「怎麼做」這件事封裝成 Skill**,而不是每次都重新下一次落落長的 prompt。
