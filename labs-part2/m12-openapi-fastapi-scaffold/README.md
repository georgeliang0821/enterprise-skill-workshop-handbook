# M12 · Lab 12:applyTo instructions + OpenAPI → FastAPI Scaffolding

> 純手刻兩輪由**講師課前準備、現場投影 diff**(見 `instructor-demo/README.md`);學員只做包工具那一輪,做完 **commit + push**——M14 的雲端 coding agent 會從這份骨架接手。

## 前置(5 分):先建 applyTo instructions

1. 建立 `.github/instructions/fastapi.instructions.md`,frontmatter 用 `applyTo: "app/**"`(完成版在 `instructions/fastapi.instructions.md`,可直接複製)。
2. 驗證它「平常不在、碰到才在」:先問一個跟 `app/` 無關的問題,references 裡不應該有它;再把 `openapi/meeting-portal-api.yaml` 拖進來問「依這份規格幫我在 app/routers/ 下寫 summaries router 的骨架」——這次 references 裡就要有它。

## 學員步驟

> 套件已由共用 venv 裝好(含 `datamodel-code-generator`),**不需要 `pip install`**;下面步驟 3–6 的工作目錄是**你自己的 Portal 專案 repo 根目錄**,`app/` 與 `app_verify/` 都產在那裡。`requirements.txt` 只是「這個 Lab 用到什麼」的對照。

1. 確認終端機提示字元有 `(.venv)`;沒有的話回到 `labs-part2/README.md` 的環境檢查。
2. 把 `skills/openapi-to-fastapi-scaffold/SKILL.md` 複製到 `.github/skills/openapi-to-fastapi-scaffold/SKILL.md`,讀一遍 ③ 步驟——model 那段是呼叫 `datamodel-codegen --disable-timestamp`,不是叫 LLM 手寫。
3. 新開 session:「依照這份 OpenAPI 規格,幫我產生 FastAPI 的 router 骨架跟 Pydantic model,輸出到 app/ 目錄下。」
   - 看 references:應出現你剛建的 `.github/instructions/fastapi.instructions.md`(因為輸出在 `app/**`)。
4. `python -m uvicorn app.main:app --reload` → 開 http://127.0.0.1:8000/docs,所有 endpoint 都在,呼叫得到 `NotImplementedError`(預期)。
5. (選)新 session 重跑到 `app_verify/`,`git --no-pager diff --no-index app/models/schemas.py app_verify/models/schemas.py` 應為空。
6. **`git add app && git commit -m "scaffold: FastAPI skeleton from OpenAPI" && git push`**

## 完成檢核

- [ ] Swagger UI 看得到所有 endpoint;函式體都是 `NotImplementedError`
- [ ] `fastapi.instructions.md` 在不相干的問題裡不出現、在涉及 `app/` 的問題裡出現
- [ ] references 有 `fastapi.instructions.md`
- [ ] 能說出「哪些交給決定性工具、哪些交給 LLM、為什麼」
- [ ] 骨架已 push

## 帶走的一個問題
你們的 API 是 spec-first(包工具 Skill)、code-first(FastAPI 自產 spec)、還是一次性 PoC(純手刻)?包工具的做法假設 spec 已經定案。
