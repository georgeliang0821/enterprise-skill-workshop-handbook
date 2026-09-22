# 參考骨架(沒做完 M12 的人用)

這份 `app/` 對應 `m12-openapi-fastapi-scaffold/openapi/meeting-portal-api.yaml`,結構與 openapi-to-fastapi-scaffold Skill 的輸出慣例一致:
`app/models/schemas.py`(Pydantic model)、`app/routers/<tag>.py`、`app/main.py`。

> 注意:這份 `schemas.py` 是依規格手動對齊 datamodel-codegen 的輸出寫的。如果你已經用 Skill 產過,請用你自己的——那份才是 byte-level 可重現的版本。

複製 `app/` 到 repo 根目錄,在有 `(.venv)` 的終端機執行 `python -m uvicorn app.main:app --reload` 確認能啟動,commit、push,然後回到 M14 的步驟 1。
