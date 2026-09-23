把 app/routers/ 底下所有 raise NotImplementedError 的函式實作成回傳符合 response_model 的假資料 stub;
為每個 router 建立 tests/test_<tag>.py(FastAPI TestClient),每個測試檔涵蓋一個成功狀態碼(200 或 201)
與一個 4xx;spec 沒有定義 4xx 的 endpoint,用 FastAPI 的 422 驗證錯誤(例如 /search 不帶 q);
不要修改 app/models/schemas.py;遵守 repo 內 AGENTS.md 與 .github/instructions/fastapi.instructions.md。
完成後在 PR 描述列出你套用了哪些 instructions 檔案。