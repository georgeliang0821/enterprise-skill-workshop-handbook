---
applyTo: "app/**"
---
# FastAPI 慣例(只在處理 app/ 底下檔案時套用)

- 每個 OpenAPI tag 一個 router 檔:app/routers/<tag>.py;每個 operationId 一個函式。
- Pydantic model 只放在 app/models/schemas.py,router 不得自行定義 model。
- 骨架階段的函式體只能是 `raise NotImplementedError("<operationId>")`,不得補上猜測的商業邏輯。
- 實作階段:每個 router 必須有對應的 tests/test_<tag>.py,用 FastAPI TestClient;測試要涵蓋 200 與至少一個 4xx。
- 不要修改 app/models/schemas.py——它是由 datamodel-codegen 產生的,改規格請改 openapi/*.yaml 後重跑。
