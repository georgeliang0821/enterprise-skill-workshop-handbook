---
name: action-item-to-jira
description: 把已經結構化的 Action Item(Owner/Action/Due Date/Priority)透過 Jira REST API 建立對應的 Jira 票,並避免對同一個 Action Item 重複建票。是「把待辦事項寫入 Jira」,不是從逐字稿整理會議摘要與待辦事項(那是 meeting-summary)。當使用者已經有結構化的 Action Item 清單,並要求「建 Jira 票」「同步到 Jira」「開票追蹤這些待辦」時使用。關鍵詞:Jira、建票、issue、ticket、同步待辦。
disable-model-invocation: true   # 只能手動 /action-item-to-jira 呼叫,不會被自動語意觸發——
                                  # 這是有寫入副作用的 Skill 的標準做法,不只靠 description 防呆
user-invocable: true
version: 0.2.0
---
# Action Item → Jira Ticket Skill(Wrap Existing Tools 範例)

## ① 適用範圍 / 不適用時改用
- 適用:使用者已經有結構化的 Action Item 清單(表格或清單形式),並要求把這些項目建立成 Jira 票。
- 不適用:Action Item 還沒被整理成結構化資料 → 先用 `meeting-summary` 把逐字稿整理成含 Action Items 的會議紀錄,這個 Skill 只負責「已經結構化的資料 → Jira」這一段。
- 不適用:使用者只是想「看看」逐字稿中的待辦事項有哪些,沒有明確要求寫入 Jira → 改用 `meeting-summary`,不要自作主張連建票都做了。
- 不適用:Jira 端點設定缺漏時,不要自己猜,誠實回報設定缺漏。

> 這個界線本身就是 M2 教過的 Scope 拆分原則:「一句話講不完的事,拆成多個 Skill」。「從逐字稿抽取待辦,而且順便建 Jira 票」一句話講不完,而且兩者的工具/寫入權限邊界完全不同——抽取只讀逐字稿,建票要寫入外部系統——所以拆成兩個 Skill,各自的輸入輸出邊界清楚。

## ② 需要的輸入
1. 結構化 Action Item 清單(必要):Owner / Action / Due Date / Priority。
2. Jira 專案代碼(必要),例如 `MIP`。
3. Jira base URL(必要),例如 `http://127.0.0.1:9000`。

## ③ 步驟(優先包既有工具/API,不要純手寫邏輯)

> base URL 取自 ②-3,本區塊只處理呼叫順序與參數邏輯。

1. 對每一筆 Action Item,先呼叫 Jira 的搜尋 API(`GET /rest/api/2/search?jql=...`),用 summary 關鍵字比對是否已經存在相同任務的票——**避免重複建票**。
2. 若不存在,呼叫 `POST /rest/api/2/issue` 建立新票:
   - `summary` = Action 內容
   - `assignee` = Owner
   - `duedate` = Due Date(若「未訂」則不帶這個欄位,不要塞假日期)
   - `priority` = 依 Priority 對照 Jira 的 priority scheme

   > ⚠️ Windows PowerShell 5.1 環境下,若手動組 request body 含中文,
   > 務必用 `[System.Text.Encoding]::UTF8.GetBytes()` 轉成 bytes 再送出,
   > 否則中文會在傳輸過程中變成亂碼寫入 Jira。這是環境雷,不是本 Skill
   > 要示範的安全設計缺陷。   

3. 若已存在,略過並在輸出裡註明「已存在,略過」。
4. 全部處理完後,依 ④ 的格式輸出結果表。

## ④ 輸出格式

```markdown
## Jira 同步結果

| Owner | Action | Jira Ticket | 狀態 |
|---|---|---|---|
| <姓名> | <任務內容> | <MIP-101 或「—」> | <新建 / 已存在,略過 / 失敗:原因> |
```
