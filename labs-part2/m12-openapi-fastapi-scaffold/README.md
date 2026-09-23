# M12 · Lab 12:applyTo instructions + OpenAPI → FastAPI Scaffolding

> 這個 Lab 是一個對照實驗,**兩輪都由學員自己執行**:第一輪純手刻兩次、diff;第二輪換上包工具的 Skill 再跑兩次、diff。做完 **commit + push**——M14 的雲端 coding agent 會從這份骨架接手。
>
> 講師課前的兩份手刻輸出改為**備案**(見 `instructor-demo/README.md`),只在人數太少或現場環境卡住時投影。

## 前置(5 分):先建 applyTo instructions

1. 建立 `.github/instructions/fastapi.instructions.md`,frontmatter 用 `applyTo: "app/**,tests/**"`(完成版在 `instructions/fastapi.instructions.md`,可直接複製)。
2. 驗證它「平常不在、碰到才在」:先問一個跟 `app/` 無關的問題,references 裡不應該有它;再把 `openapi/meeting-portal-api.yaml` 拖進來問「依這份規格幫我在 app/routers/ 下寫 summaries router 的骨架」——這次 references 裡就要有它。

兩個細節值得多看三秒:

- **glob 要蓋到「規則管的所有路徑」。** 測試那條規則管的是 `tests/`,所以 glob 不能只寫 `app/**`——否則 agent 在建 `tests/test_meetings.py` 時,這份檔案不會被注入。規則寫給誰看,glob 就要蓋到誰。
- **這份檔案有一半的規則你今天用不到。** 「實作階段」那一段是寫給 **M14 的雲端 agent** 看的。同一份 instructions 可以分階段寫,由讀它的 agent 判斷現在在哪一階段。

## 開始前的兩個前提

- 確認終端機提示字元有 `(.venv)`;沒有的話回到 `labs-part2/README.md` 的環境檢查。套件已由共用 venv 裝好(含 `datamodel-code-generator`),**不需要 `pip install`**;這裡的 `requirements.txt` 只是「這個 Lab 用到什麼」的對照。
- 以下所有步驟的工作目錄都是**你自己的 Portal 專案 repo 根目錄**,`app_manual_1/`、`app_manual_2/`、`app/`、`app_verify/` 都產在那裡。

## 第一輪(6 分):純手刻兩次,先用眼睛看,再用 diff 看

1. 新開一個乾淨 session,把 `openapi/meeting-portal-api.yaml` 拖進來,下:
   > 依照這份 OpenAPI 規格,不要使用任何 code generation 工具,直接手寫 MeetingSummary 和 ActionItem 這兩個 Pydantic model,輸出到 app_manual_1/models.py。只要 model,不要 router、不要 main.py。
2. **另外開一個新 session**(同一個 session 重跑會參考自己上一次的輸出,漂移會被遮住),同一句指令,輸出目錄改成 `app_manual_2/`。
3. **先用眼睛看**:兩份並排打開,花 30 秒掃過去,心裡回答「這兩份一樣嗎?」
4. **再用 diff 看**:
   ```powershell
   git --no-pager diff --no-index app_manual_1/models.py app_manual_2/models.py
   ```

要盯的不是「哪份對」,是「兩份都看起來對,但兜不起來」。這份 spec 埋的幾個點:

| spec 裡長這樣 | 常見分歧 | 踩到會怎樣 |
|---|---|---|
| `sentiment: [positive, neutral, negative]` | 類別名 `Sentiment` / `SentimentEnum`;member 大小寫不一 | 呼叫端 `Sentiment.positive` 換一份就 `AttributeError` |
| `priority: [High, Medium, Low]` | 同檔跟 sentiment 大小寫慣例相反,LLM 容易「順手統一」 | 同上,而且更難發現 |
| `dueDate`:`format: date` + `nullable: true` | `Optional[date]` / `date \| None` / `Optional[str]` / 漏掉 nullable | 塞 `null` 直接 ValidationError |
| `generatedAt`:`format: date-time` | `datetime` 還是 `str` | 序列化格式不同,前端解析失敗 |
| camelCase 欄位名 | 有沒有 alias、有沒有 `populate_by_name` | JSON 欄位名對不上 |

連類別排列順序、有沒有 `__init__.py` 都可能不同。沒全踩到也沒關係——**「這次剛好對」不等於「下次也對」,只要有機率漂,就不該是可信的工程步驟。**

> **為什麼輸出到 `app_manual_*/` 而不是 `app/`**
> 因為 `app/**` 已經被你剛建的 `fastapi.instructions.md` 蓋住了,那份規則會壓掉一部分漂移,第一輪就看不出問題。刻意避開它,順便證明你寫的規則真的在生效。

## 第二輪(12 分):換上包工具的 Skill,同樣跑兩次、同樣 diff

1. 把 `skills/openapi-to-fastapi-scaffold/SKILL.md` 複製到 `.github/skills/openapi-to-fastapi-scaffold/SKILL.md`,讀一遍 ③ 步驟——model 那段是呼叫 `datamodel-codegen --disable-timestamp`,不是叫 LLM 手寫。
2. 新開一個乾淨 session:「依照這份 OpenAPI 規格,幫我產生 FastAPI 的 router 骨架跟 Pydantic model,輸出到 app/ 目錄下。」
   - 看 references:應出現你剛建的 `fastapi.instructions.md`(因為輸出在 `app/**`)。
3. `python -m uvicorn app.main:app --reload` → 開 http://127.0.0.1:8000/docs,所有 endpoint 都在,呼叫得到 `NotImplementedError`(預期)。
4. **再開一個新 session,同一句指令,輸出目錄改成 `app_verify/`**——跟第一輪完全一樣的做法,只是換了一個 Skill。
5. 第二次 diff:
   ```powershell
   git --no-pager diff --no-index app/models/schemas.py app_verify/models/schemas.py
   ```
6. 對一下全班的 hash:
   ```powershell
   certutil -hashfile app\models\schemas.py SHA256
   ```
   三十台機器、三十個獨立 session,同一個 hash——因為型別轉換那一段根本不是 LLM 在做。
7. **commit 並 push,`.github/` 要一起帶上**:
   ```powershell
   git add app .github
   git commit -m "scaffold: FastAPI skeleton from OpenAPI"
   git push
   ```
   M14 的雲端 agent 讀不到你本機的檔案,它只看得到 repo 上的——`.github/` 沒 push,M14 就會卡在「它沒讀到 instructions」那個翻車。

## 完成檢核

- [ ] 能說出兩次 diff 分別印出了什麼——第一次有幾處差異、差在哪;第二次是空的
- [ ] 能說出「哪些交給決定性工具、哪些交給 LLM、為什麼」
- [ ] `fastapi.instructions.md` 在不相干的問題裡不出現、在涉及 `app/` 的問題裡出現
- [ ] references 有 `fastapi.instructions.md`
- [ ] Swagger UI 看得到所有 endpoint;函式體都是 `NotImplementedError`
- [ ] 你的 `schemas.py` hash 跟鄰座一樣
- [ ] 骨架**與 `.github/`** 都已 push

## 帶走的一個問題

你們的 API 是 spec-first(包工具 Skill)、code-first(FastAPI 自產 spec)、還是一次性 PoC(純手刻)?包工具的做法假設 spec 已經定案——如果你們的 spec 還在動,先回頭解決的是治理流程,不是 scaffolding 工具。