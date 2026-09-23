# AI Meeting Intelligence Portal Workshop — 上半場 Lab 素材(M0–M8)

對應講義 `Handbook_Part1_v5.html`。Workshop「從 Prompt 到團隊資產」上半場主題:**從 Prompt 到 Skill**——同一句 prompt 為什麼每個人不一樣,以及三個 Skill 怎麼收斂它。資料夾編號 = 講義模組編號。

| 資料夾 | 模組 | 你會做出 / 經歷什麼 | 主要素材 |
|---|---|---|---|
| `m00-portal-demo/` | M0 | 講師 live demo 用;M2 示範也用它 | `prompt.md` |
| `m02-context-demo/` | M2 | 兩個症狀的講師 demo 腳本 + 七層組裝 / `#` 引用速查(講義附錄 A 的來源) | `README.md` |
| `m03-drift-experiment/` | M3 / M5 / M6 | 偏離預期實驗三輪的記錄表(全班鎖同一模型) | `README.md`、`worksheet.md` |
| `m04-agents-md-and-prompt-file/` | M4 | `/init` → AGENTS.md、Prompt File 兩個完成版 | `AGENTS.md`、`.github/prompts/` |
| `m06-meeting-summary-skill/` | M3 / M6 | 全班共用逐字稿;第一個 Skill,把 M3 / M5 兩輪還沒收斂的偏離預期收掉 | `sample-transcript.txt`、`skills/meeting-summary/SKILL.md` |
| `m07-wbs-and-followup-planner/` | M7 | Lab 7A WBS Excel(code execution)+ Lab 7B Weekly Follow-up Planner(MCP,三條路徑) | `skills/…`、`data/`、`mcp/` |
| `m08-mistrigger-test/` | M8 | 三個 Skill + 一個 prompt file:誤觸發實測 | `README.md` |

> Custom Agent / Subagent / Handoff 的素材在 `labs-part2/m09-meeting-ops-agent/`(下半場開頭);`applyTo` instructions 在 `labs-part2/m12-openapi-fastapi-scaffold/instructions/`。

## 環境需求

- VS Code + GitHub Copilot,Agent mode 可用;模型選單**至少有一個可指定的模型**(M3 / M5 / M6 三輪全班鎖同一個講師指定的模型,不用 Auto)
- Python 3.10+(Lab 7A)。**本資料夾與 `labs-part2` 共用同一個 venv**:請把兩包解壓到課前建好的上課資料夾裡、與 `.venv` 並排(例如 `C:\ghcp-workshop\` 底下同時有 `labs-part1\`、`labs-part2\`、`.venv\`),接著的**第一件事**就是在本資料夾執行:

  ```powershell
  ..\.venv\Scripts\python.exe -m pip install -r requirements.txt
  ```

  兩包的 `requirements.txt` 內容相同,只需在其中一邊裝一次,全天不再需要 `pip install`。
- 請用 VS Code **開啟本資料夾本身**(不要開父資料夾),`.vscode/settings.json` 才會把直譯器指到共用 venv,新終端機提示字元會出現 `(.venv)`。
- Lab 7B:MCP 三路徑擇一(CalendarTools / GitHub MCP / Microsoft Learn MCP),見該 Lab README 的 B0
- 下半場會用到 GitHub repo + Copilot CLI + 雲端 coding agent:**請在上半場結束前把你的 workshop 專案 push 到一個你有寫入權限的 GitHub repo**,並把 `AGENTS.md` 與 `.github/` 一起 commit。

## 使用方式提醒

每個 Lab 的完成版都是「先自己寫、再對照」用的,不要一開始就複製——寫的過程本身就是在練 Scope / IO 的設計判斷。

## 這幾段如何串成一條線

```
M0   講師 demo Portal 終點(m00)+ 一個關鍵提問
M1   五種資產地圖 + .github 檔案結構(講義)
M2   Context 兩個症狀 → #file / 新開 session(講師 demo,m02)
M3   翻車① 第一輪:乾淨環境、同一個模型,同一句 prompt N 種輸出(m06 逐字稿 + m03 worksheet)
M4   Lab:/init → AGENTS.md + Prompt File(m04)
M5   翻車① 第二輪:有 AGENTS.md 仍偏離預期的部分 → 為什麼需要 Skill
M6   Lab 6:meeting-summary 收掉剩下的偏離預期(第三輪)
M7   Lab 7A wbs-generator(code exec)+ Lab 7B weekly-followup-planner(MCP)
M8   翻車②:三個 Skill + 一個 prompt file 的誤觸發實測(m08)
收尾  三輪紀錄 + 翻車③ 預告(編排失控)→ 下半場 M9 解
```
