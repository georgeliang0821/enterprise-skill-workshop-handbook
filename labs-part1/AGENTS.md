# Lab 素材資料夾 — Agent 環境約定

> 這份檔案只描述**執行環境**,不是 Lab 1B 的教材。Lab 1B 要你動手寫的 `AGENTS.md` 是在你自己的 Portal 專案 repo 根目錄,跟這份無關;完成版在 `lab1b-custom-instructions-and-prompts/AGENTS.md`。

## Python 環境:共用 venv

`labs-part1` 與 `labs-part2` **共用同一個 venv**,位置在兩個資料夾的共同父資料夾下:`../.venv`。

- 所有 Python / pip 指令一律走這個 venv,**不要使用全域直譯器**。
- VS Code 已透過 `.vscode/settings.json` 指定直譯器,新開的終端機會自動啟用;執行任何 Python 指令前,先確認提示字元有 `(.venv)`。
- **禁止執行全域 `pip install`**。若發現缺套件，先回報缺哪一個，由使用者決定是否加進本資料夾的 `requirements.txt`。
- venv 尚未建立時，請回報使用者，不要自行 `python -m venv`。

工作坊需要的套件(openpyxl、fastapi、uvicorn、pydantic、requests、datamodel-code-generator、pytest、httpx)在共用 venv 裡已經裝好,正常情況下不需要安裝任何東西。
