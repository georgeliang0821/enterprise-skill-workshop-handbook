# Lab 4:OpenAPI → FastAPI Scaffolding + 撞牆④:純手刻漂移

這個 Lab 對應企業導入 Copilot 最常見的具體需求:「從 API Spec 產生 Controller 骨架」。`openapi/meeting-portal-api.yaml` 這份規格**就是 M0 demo 那個 Portal 前端所需要的後端 API**——做完這一步,故事線閉環。

跟前兩個 Lab 結構不同:**不要求你從頭手寫 SKILL.md**(今天已經寫過三份,第四份邊際學習有限),而是把時間花在「先看純手刻怎麼翻車,再看包工具為什麼穩」。這裡的翻車是**機率性**的——單看一份純手刻輸出常常「看起來還不錯」,所以我們的比法不是比對錯,而是比**兩次跑得一不一樣**:同一份規格、同一句指令,跑兩次長得不一樣,就代表你不能把它當可靠的工程步驟。

> 📌 **一件刻意的事**:第一輪請**先不要**複製 `skills/` 裡的 SKILL.md、也不要裝 requirements——先讓 Copilot 在沒有任何工具與規則的情況下純手刻,你才有對照組。

## 環境需求

- Python 3.10+
- PowerShell(Windows)
- git(diff 用)

## 第一輪:純手刻,跑兩次

1. 開一個新的 Agent mode session,提供 `openapi/meeting-portal-api.yaml`,下指令(為了時間,只做兩個 endpoint):

   ```text
   依照這份 OpenAPI 規格,不要使用任何 code generation 工具,直接手寫
   getMeetingSummary 和 getActionItems 這兩個 endpoint 的 FastAPI router
   跟對應的 Pydantic model,輸出到 app_llm_run1/ 目錄下。
   ```

2. **開一個全新的 chat session**(關鍵——同一個 session 重跑,它會參考自己剛剛的輸出,漂移會被遮住),同一份規格、同一句指令原封不動再下一次,只把輸出目錄改成 `app_llm_run2/`。

3. (選做)分別啟動兩份輸出驗證能不能跑——**module path 要對到資料夾名稱,兩個不能同時佔用同一個 port**:

   ```powershell
   python -m uvicorn app_llm_run1.main:app --reload
   ```
   ```powershell
   python -m uvicorn app_llm_run2.main:app --reload --port 8001
   ```

   噴 `ModuleNotFoundError` 通常是資料夾缺 `__init__.py`,補一個空檔案即可——這步可省略,重點在下一步的 diff。

4. 兩次輸出互 diff(加 `--no-pager` 避免 PowerShell 丟進 `less` 卡住):

   ```powershell
   git --no-pager diff --no-index app_llm_run1 app_llm_run2
   ```

   看到 `__pycache__` 的 binary diff 不用管,那是跑過 uvicorn 留下的快取。想聚焦型別合約,直接只看 model 檔(通常叫 `models.py`):

   ```powershell
   git --no-pager diff --no-index app_llm_run1/models.py app_llm_run2/models.py
   ```

   為什麼挑 model 檔看?因為 `main.py`/`routers.py` 的差異多半是措辭、命名習慣;只有 model 檔承載**型別合約**本身。

5. 對答案——**保證會出現**的是命名層級不一致:類別名一次叫 `SentimentEnum` 一次叫 `Sentiment`,enum member 一次小寫 `positive` 一次大寫 `POSITIVE`。這不只是風格問題——**如果呼叫端程式碼寫了 `Sentiment.positive`,換到另一次產出就直接 `AttributeError`**,兩份「看起來都對」的 model 彼此兜不起來。

   規格裡還埋了幾顆型別地雷,運氣不好會直接踩到(不保證每次都踩,但至少有機率):

   | 地雷 | spec 位置 | 常見漂移 |
   | --- | --- | --- |
   | nullable | `ActionItem.dueDate`、`Risk.detail` | `Optional[date]` / `date \| None` / 直接漏掉 |
   | enum | `MeetingSummary.sentiment`、`ActionItem.priority` | 一次 `Enum` class、一次裸 `str` |
   | date-time | `MeetingSummary.generatedAt` | 一次 `datetime`、一次 `str` |
   | camelCase | `meetingId`、`dueDate`、`generatedAt` | 一次有 `alias`、一次沒有 |
   | 其它 | — | 欄位順序、model 命名、檔案切法每次都不同 |

## 第二輪:包工具的 Skill,也跑兩次

6. 安裝工具:

   ```powershell
   pip install -r requirements.txt
   ```

7. 把 `skills/openapi-to-fastapi-scaffold/SKILL.md` 複製到專案 `.github/skills/openapi-to-fastapi-scaffold/SKILL.md`,快速讀一遍 ③ 步驟:model 那段不是「請產生 Pydantic model」,而是明確呼叫 `datamodel-codegen`(注意 `--disable-timestamp`——沒有它,檔頭時間戳會讓等下的 diff 不乾淨)。

8. 開新 session,下指令(這次做完整規格):

   ```text
   依照這份 OpenAPI 規格,幫我產生 FastAPI 的 router 骨架跟 Pydantic model,輸出到 app/ 目錄下。
   ```

9. 驗證:

   ```powershell
   python -m uvicorn app.main:app --reload
   ```

   開 `http://127.0.0.1:8000/docs`,確認 spec 裡所有 endpoint 都在;呼叫任一 endpoint 得到 `NotImplementedError`(預期行為——骨架正確、邏輯留白)。

10. 再開一個新 session,同一句指令重跑到 `app_verify/`,diff 兩次的 model(注意工具版的 model 檔固定在 `app/models/schemas.py`,不是 `app/models.py`):

   ```powershell
   git --no-pager diff --no-index app/models/schemas.py app_verify/models/schemas.py
   ```

   **指令跑完畫面上什麼都不會印出來——這就是預期結果,不是下錯指令。**——型別轉換根本不是 LLM 在做,是決定性工具在做;LLM 負責流程編排跟 router 慣例,那才是它擅長且風險可控的部分。

11. 回頭抽查地雷:對照 `app/models/schemas.py`,看 `sentiment` enum、`generatedAt` date-time、`dueDate` nullable 在工具版怎麼被正確處理,再看你純手刻兩份各自錯在哪。

12. 最後檢查骨架紀律:有沒有函式被「順手」補上看似合理其實沒根據的邏輯——骨架就該是乾淨的 `NotImplementedError`。

## 完成檢核

- [ ] 第一輪:兩份純手刻輸出的 `models.py` diff 出至少一處**命名不一致**(類別名或 enum member 大小寫);能說出為什麼這種差異換到呼叫端會直接 `AttributeError`
- [ ] 第一輪(加分,不強求):有踩到 nullable / enum 型別 / date-time / camelCase alias 其中一類**型別合約**差異——沒踩到代表這次運氣好,不代表下次也會好
- [ ] 第二輪:Swagger UI 看得到所有 endpoint;所有函式是乾淨骨架;uvicorn 正常啟動
- [ ] 兩次工具版 `schemas.py` 的 diff 為**空**(指令跑完無輸出)
- [ ] 能一句話回答:「這個 Skill 裡,哪些交給決定性工具、哪些交給 LLM,為什麼這樣切?」

> 帶走的觀念:**Skill 不是把 prompt 寫長,而是把「不該生成的部分」從生成裡拿掉。** 純手刻不需要「每次都錯」才算不可靠——只要存在「這次跟下次長得不一樣」的機率,就不該是你信任的工程步驟。另外注意 SKILL.md ③-6 的「重跑保護」——它防的是另一種事故(spec 改版重跑,把同事手寫的實作靜默蓋回骨架),今天用講的、不實測,但這條規則的來歷正是 M6 要講的:**最有價值的品質規則,往往來自事故,不是來自想像。**
