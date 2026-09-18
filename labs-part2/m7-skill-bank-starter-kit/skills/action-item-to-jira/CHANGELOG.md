# CHANGELOG — action-item-to-jira

## v0.2.0 — 2026-07-08
### 變更(M5 撞牆④三連撞後的硬化)
- ③ 步驟新增**去重**:建票前先 `GET /rest/api/2/search` 比對是否已存在,已存在則略過並註明。
- ② 輸入新增 **Owner 對照表為必要輸入**;assignee 一律用對照表帳號,查不到標記失敗,不用姓名硬塞。
- frontmatter 改 `disable-model-invocation: true`,鎖住自動語意觸發,只能明確 `/action-item-to-jira` 執行。
- ② 與 ⑤ 補上認證處理:token 走環境變數、401 誠實回報、token 值不出現在輸出/log。
### 原因(對應到的真實案例)
- 撞 A:同一份清單觸發兩次,`debug/issues` 出現六筆票(三筆重複)。
- 撞 B:assignee 被塞入 "David" 姓名字串,寬鬆 API 照單全收。
- 撞 C:隨口一句「這些待辦要記得追蹤」有機率被語意觸發直接建票——寫入型不能賭這個機率。

## v0.1.0-naive — 2026-07-08
- 初版(刻意天真版,Workshop 撞牆用):能動,但無去重、姓名直塞 assignee、允許自動觸發。
