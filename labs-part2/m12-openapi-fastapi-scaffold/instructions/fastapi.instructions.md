---
applyTo: "**/app/**,**/tests/**"
---
# FastAPI 慣例(處理 app/ 與 tests/ 底下檔案時套用)

## 骨架階段
- 每個 OpenAPI tag 一個 router 檔:app/routers/<tag>.py;每個 operationId 一個函式。
- Pydantic model 只放在 app/models/schemas.py,router 不得自行定義 model。
- 函式體只能是 `raise NotImplementedError("<operationId>")`,不得補上猜測的商業邏輯。

## 實作階段
- 每個 router 必須有對應的 tests/test_<tag>.py,用 FastAPI TestClient。
- 每個測試檔至少涵蓋一個成功狀態碼(200 或 201)與一個 4xx;
  spec 沒有定義 4xx 的 endpoint,用 FastAPI 的 422 驗證錯誤(例如 /search 不帶 q)。
- stub 只回傳符合 response_model 的假資料,不得自行補上規格沒有的商業邏輯。

## 兩個階段都適用
- 不要修改 app/models/schemas.py——它是由 datamodel-codegen 產生的,改規格請改 openapi/*.yaml 後重跑。