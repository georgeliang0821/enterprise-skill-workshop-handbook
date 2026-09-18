---
name: openapi-to-fastapi-scaffold
description: 從 OpenAPI/Swagger 規格產生 FastAPI 的 Pydantic model 與 router 骨架。是「產生程式骨架」,不是設計 API 規格,也不會補上任何商業邏輯。當使用者提供 OpenAPI yaml/json 檔,並要求「產生 FastAPI controller」「依 API spec 產生 router」「幫我 scaffold 後端」時使用。關鍵詞:OpenAPI、Swagger、FastAPI、router、controller、scaffold、Pydantic。
disable-model-invocation: false
user-invocable: true
version: 0.1.0
---
# OpenAPI → FastAPI Scaffolding Skill

## ① 適用範圍 / 不適用時改用
- 適用:使用者提供一份 OpenAPI(或 Swagger)規格檔,並要求依此產生 FastAPI 的程式骨架。
- 不適用:使用者只是想「討論 API 設計」、還沒定案 spec——那個階段還在設計討論,不該急著生成程式碼,直接對話討論就好。
- 不適用:使用者要的是把骨架填成真正能跑的商業邏輯 → 那超出這個 Skill 的範圍,骨架完成後的實作是另一件事,不歸這個 Skill 管。

## ② 需要的輸入
1. OpenAPI spec 檔案路徑(必要),例如 `openapi/meeting-portal-api.yaml`。
2. 輸出目錄(必要或使用預設慣例,例如 `app/`)。
3. (選)既有的專案慣例文件,例如錯誤處理慣例、authentication 中介層寫法——如果專案裡已經有其他 router 檔案可以參考風格,先讀取那些檔案再動手,不要憑空自創一套風格。

## ③ 步驟(優先包既有工具,不要純手寫)
1. 先用 `datamodel-codegen` 從 OpenAPI spec 產生 Pydantic model 初版:
   ```powershell
   datamodel-codegen --input openapi/meeting-portal-api.yaml --input-file-type openapi --output app/models/schemas.py
   ```
2. 讀取 spec 裡每一個 `path` + `method`,依 `tags` 分組,每個 tag 建立一個獨立的 router 檔案(例如 `app/routers/meetings.py`、`app/routers/search.py`)。
3. 每個 `operationId` 對應一個 FastAPI 的 path function,函式內先放 `raise NotImplementedError("TODO: 實作 <operationId>")` 當骨架,**不要自己幻覺一段看起來合理但沒有根據的商業邏輯**——這是這個 Skill 最重要的紀律:scaffolding 的責任是「把介面長對」,不是「把邏輯寫對」。
4. 每個 path function 的 `response_model` 要對應 spec 裡定義的 schema,狀態碼(200/201/404 等)要跟 spec 一致。
5. 在 `app/main.py` 把所有 router 用 `include_router` 組裝起來。
6. 產出後,實際跑一次 `uvicorn app.main:app --reload`,確認服務能正常啟動(即使呼叫 endpoint 會得到 `NotImplementedError`,那是預期行為,不是錯誤)。

## ④ 輸出格式
- `app/models/schemas.py`:datamodel-codegen 產生的 Pydantic model。
- `app/routers/<tag>.py`:每個 tag 一個檔案,內含對應的 path function 骨架。
- `app/main.py`:組裝所有 router 的進入點。
- 結尾附上摘要:列出總共產生了幾個 endpoint、分別對應哪個 router 檔案。

## ⑤ 品質自檢(產出後逐項確認,沒過就修再交)
- [ ] spec 裡的每一個 `path` + `method` 都有對應的 function,沒有遺漏。
- [ ] 每個 function 的 `response_model` 正確對應 spec 定義的 schema,沒有型別對不上。
- [ ] 路徑參數(例如 `{meetingId}`)型別正確,且有從 URL 正確帶入。
- [ ] 狀態碼(200/201/404…)跟 spec 定義一致。
- [ ] 函式內是明確的 `TODO` / `NotImplementedError` 骨架,**沒有夾帶任何看似合理其實是幻覺出來的商業邏輯**。
- [ ] `uvicorn app.main:app --reload` 能成功啟動,沒有 import 或型別錯誤。
- [ ] 命名慣例(檔名、函式名、變數名)跟專案既有風格一致,不是自創一套。
