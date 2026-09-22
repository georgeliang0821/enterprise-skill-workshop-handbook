# 講師課前準備:兩份純手刻輸出(學員不用做)

「純手刻漂移」由講師示範。請在課前用同一句指令、兩個乾淨 session 各跑一次,把輸出留在這個資料夾旁邊(`app_llm_run1/`、`app_llm_run2/`),現場只投影 diff。

## 步驟

1. 不放任何 SKILL.md、不裝工具。新開 Agent mode session,提供 `openapi/meeting-portal-api.yaml`,下:
   > 依照這份 OpenAPI 規格,不要使用任何 code generation 工具,直接手寫 getMeetingSummary 和 getActionItems 這兩個 endpoint 的 FastAPI router 跟對應的 Pydantic model,輸出到 app_llm_run1/ 目錄下。
2. **新開一個 session**(同一 session 重跑會參考自己的輸出,漂移會被遮住),同一句,輸出目錄改 `app_llm_run2/`。
3. 現場投影:
   ```powershell
   git --no-pager diff --no-index app_llm_run1/models.py app_llm_run2/models.py
   ```
   (檔名依 LLM 這次怎麼命名而定——連檔名不同,本身就是一種漂移,可以順便講。)

## 現場要指的東西

- 幾乎必中:enum 類別名 / member 大小寫不一致 → 呼叫端 `Sentiment.positive` 換一份就 `AttributeError`。
- 看運氣:`dueDate` nullable 寫法、`generatedAt` 是 `datetime` 還是 `str`、camelCase 欄位有沒有 alias、有沒有 `__init__.py`。
- 沒踩到也沒關係——「這次剛好對」不等於「下次也對」,只要有機率漂,就不該是可信的工程步驤。

## 如果課前來不及跑

用 `datamodel-codegen` 產出的 `schemas.py`(學員等一下自己會產)跟任何一份純手刻比,也能講到重點;但兩份純手刻互比的說服力最強。
