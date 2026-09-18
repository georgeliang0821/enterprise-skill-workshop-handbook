# PR review checklist(雲端 coding agent 的產出)

| # | 檢查 | 通過? | 沒過怎麼辦 |
|---|---|---|---|
| a | `app/models/schemas.py` **沒有**被修改 | ☐ | 留言 `@copilot 請 revert schemas.py 的變更,model 由 codegen 產生` |
| b | 每個 router 有對應 `tests/test_<tag>.py`;每個檔案至少一個 200、一個 4xx | ☐ | 留言指出缺哪個 |
| c | 沒有「順手」補上規格沒有的商業邏輯(stub 只回傳符合 response_model 的假資料) | ☐ | 留言請它移除 |
| d | PR 描述列出套用的 instructions 檔案(至少 `AGENTS.md` 與 `fastapi.instructions.md`) | ☐ | 看 session 紀錄確認它有沒有讀;沒讀 → 查 glob / push |
| e | 測試在 CI 或本機 `pytest` 通過 | ☐ | 留言貼失敗訊息 |
| f | 沒有新增的相依套件(除了 pytest / httpx) | ☐ | 留言請它移除 |

只有 a–d 全過才 merge;e、f 視你們專案而定。
