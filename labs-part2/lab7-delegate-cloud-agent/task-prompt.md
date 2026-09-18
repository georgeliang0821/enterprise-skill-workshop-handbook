把 app/routers/ 底下所有 raise NotImplementedError 的函式實作成回傳符合 response_model 的假資料 stub;
為每個 router 建立 tests/test_<tag>.py(FastAPI TestClient,涵蓋 200 與至少一個 4xx);
不要修改 app/models/schemas.py;遵守 repo 內 AGENTS.md 與 .github/instructions/fastapi.instructions.md。
完成後在 PR 描述列出你套用了哪些 instructions 檔案。
