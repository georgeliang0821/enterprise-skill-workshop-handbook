---
name: action-item-to-jira
description: 把 Action Item(Owner/Action/Due Date/Priority)透過 Jira REST API 建立成 Jira 票。當使用者提到待辦事項需要追蹤、建票、同步到 Jira 時使用。關鍵詞:Jira、建票、issue、ticket、待辦、追蹤。
disable-model-invocation: false
user-invocable: true
version: 0.1.0-naive
---
# Action Item → Jira Ticket Skill


## ① 適用範圍
- 適用:使用者有一份 Action Item 清單,想建立成 Jira 票追蹤。

## ② 需要的輸入
1. Action Item 清單(Owner / Action / Due Date / Priority)。
2. Jira 專案代碼,例如 `MIP`。
3. Jira base URL 與認證 token(從環境變數 `JIRA_API_TOKEN` 讀取,帶入 `Authorization: Bearer {token}` header)。

## ③ 步驟
1. 對每一筆 Action Item,呼叫 `POST /rest/api/2/issue` 建立新票:
   - `summary` = Action 內容
   - `assignee` = Owner
   - `duedate` = Due Date
   - `priority` = Priority

   > ⚠️ Windows PowerShell 5.1 環境下,若手動組 request body 含中文,
   > 務必用 `[System.Text.Encoding]::UTF8.GetBytes()` 轉成 bytes 再送出,
   > 否則中文會在傳輸過程中變成亂碼寫入 Jira。這是環境雷,不是本 Skill
   > 要示範的安全設計缺陷。
2. 全部建立完後,輸出每筆的票號。



## ④ 輸出格式

```markdown
## Jira 同步結果

| Owner | Action | Jira Ticket |
|---|---|---|
| <Owner> | <任務內容> | <票號> |
```
