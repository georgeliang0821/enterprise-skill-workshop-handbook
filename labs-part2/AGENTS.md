# Lab 素材資料夾 — Agent 環境約定

> 這份檔案只描述**執行環境**。你自己 Portal 專案 repo 裡那份 `AGENTS.md`(上半場 Lab 1B 寫的)才是課程資產,跟這份無關。

## Python 環境:共用 venv

`labs-part1` 與 `labs-part2` **共用同一個 venv**,位置在兩個資料夾的共同父資料夾下:`../.venv`。

- 所有 Python / pip 指令一律走這個 venv,**不要使用全域直譯器**。
- VS Code 已透過 `.vscode/settings.json` 指定直譯器,新開的終端機會自動啟用;執行任何 Python 指令前,先確認提示字元有 `(.venv)`。
- **禁止執行全域 `pip install`**。各 Lab 資料夾下的 `requirements.txt` 只是對照用，套件已由本資料夾根目錄的 `requirements.txt` 一次裝好。若發現缺套件，先回報缺哪一個，由使用者決定是否加進該清單。
- venv 尚未建立時，請回報使用者，不要自行 `python -m venv`。

常用啟動指令(都用 `python -m`,確保走的是 venv 而非 PATH 上的 exe):

```powershell
python -m uvicorn app.main:app --reload
python -m uvicorn mock_jira_server:app --reload --port 9000
```
