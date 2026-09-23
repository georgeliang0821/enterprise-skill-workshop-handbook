# PR review checklist(雲端 coding agent 的產出)

> 這份 checklist 是 M14 的重點。M12 的可信度來自「跑兩次一樣」;這裡的工作不可能重現(派兩次一定得到兩份不同的 PR),可信度只能來自「這一次過得了下面這幾項」。

| # | 檢查 | 通過? | 沒過怎麼辦 |
|---|---|---|---|
| a | `app/models/schemas.py` **沒有**被修改 | ☐ | 留言 `@copilot 請 revert schemas.py 的變更,model 由 codegen 產生` |
| b | 每個 router 有對應 `tests/test_<tag>.py`;每個檔案至少一個成功狀態碼(200 或 201)與一個 4xx<br>※ `transcripts` 是 **201**;`search` 與 `transcripts` 規格沒有 4xx,用 FastAPI 的 **422**(例如 `/search` 不帶 `q`)算過 | ☐ | 留言指出缺哪個 |
| c | 沒有「順手」補上規格沒有的商業邏輯(stub 只回傳符合 response_model 的假資料) | ☐ | 留言請它移除 |
| d1 | **session 紀錄裡看得到它讀了 `fastapi.instructions.md`**(主證據) | ☐ | 沒讀 → 查 `.github/` 有沒有 push、`applyTo` glob 對不對(含 `tests/**`) |
| d2 | PR 描述列出套用的 instructions 檔案(次要:這是 agent 的自我申報,寫了不代表真讀) | ☐ | 留言請它補;但判斷「有沒有生效」以 d1 為準 |
| e | 測試在 CI 或本機 `pytest` 通過 | ☐ | 留言貼失敗訊息 |
| f | 沒有新增的相依套件(除了 pytest / httpx) | ☐ | 留言請它移除 |

只有 a、b、c、d1 全過才 merge;d2、e、f 視你們專案而定。

## review 時的心法

M12 的型別漂移和這裡的 agent 越界,失敗模式是同一種:**都是「看起來對」**。幾百行 diff 裡夾一段規格沒有的商業邏輯,掃過去不會發現。所以 review 的順序建議是:

1. 先看**檔案清單**(有沒有動到不該動的 `schemas.py`) — 對應 a
2. 再看**新增了什麼**(有沒有多出來的邏輯、多出來的套件) — 對應 c、f
3. 最後才看**寫得好不好** — 對應 b、e

前兩步是「牆」,第三步才是品味。牆沒守住,寫得再好也不能 merge。