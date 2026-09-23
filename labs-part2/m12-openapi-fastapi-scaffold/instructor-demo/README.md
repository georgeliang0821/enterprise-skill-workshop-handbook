# 講師課前準備:兩份純手刻輸出(**備案**,學員不用做)

**純手刻漂移改由學員自己跑**(見上層 `README.md` 第一輪)。這份輸出降級為備案,只在下列情況投影:

- 現場人數太少(< 8 人),學員自己兩次剛好沒漂,樣本不足以說明問題。
- 環境卡住(網路、額度、session 開不起來),第一輪跑不完。
- 有學員兩次輸出幾乎一致,追問「是不是其實很穩」——這時拿講師這兩份出來,證明它只是這次運氣好。

## 步驟(課前做)

1. 不放任何 SKILL.md、不裝工具。新開 Agent mode session,提供 `openapi/meeting-portal-api.yaml`,下:
   > 依照這份 OpenAPI 規格,不要使用任何 code generation 工具,直接手寫 MeetingSummary 和 ActionItem 這兩個 Pydantic model,輸出到 app_llm_run1/ 目錄下。只要 model,不要 router、不要 main.py。
2. **新開一個 session**(同一 session 重跑會參考自己的輸出,漂移會被遮住),同一句,輸出目錄改 `app_llm_run2/`。
3. 輸出留在這個資料夾旁邊(`app_llm_run1/`、`app_llm_run2/`),現場只投影 diff:
   ```powershell
   git --no-pager diff --no-index app_llm_run1/models.py app_llm_run2/models.py
   ```
   (檔名依 LLM 這次怎麼命名而定——**連檔名不同,本身就是一種漂移**,投影時可以順便講。)

## 現場要指的東西

- 幾乎必中:enum 類別名 / member 大小寫不一致 → 呼叫端 `Sentiment.positive` 換一份就 `AttributeError`。
- 這份 spec 的隱藏陷阱:`sentiment` 是全小寫、`priority` 是首字大寫,同一個檔案裡兩套慣例——LLM 很容易「順手統一」成其中一種。
- 看運氣:`dueDate` nullable 寫法、`generatedAt` 是 `datetime` 還是 `str`、camelCase 欄位有沒有 alias、有沒有 `__init__.py`。
- 沒踩到也沒關係——「這次剛好對」不等於「下次也對」,只要有機率漂,就不該是可信的工程步驟。

## 這一段的講法(學員已經自己跑過第一輪)

不要重複講一次漂移是什麼。講師這兩份的作用只有一個:**加大樣本**。台詞大致是「你們剛才各自跑了兩次,我課前也跑了兩次——連我自己跟自己都對不起來」。三十個人 × 兩次,加上講師兩次,沒有任何一組是可重現的。