# AI Meeting Intelligence Portal Workshop — 上半場 Lab 素材(M0–M3)

對應講義 `Handbook_Part1_v4.html`。

| 資料夾 | 對應模組 | 你會做出 / 經歷什麼 | 主要素材 |
|---|---|---|---|
| `lab1-portal-scaffold/` | M0 | 講師 live demo 用;M1b 示範也用它 | `prompt.md` |
| `m1b-context-demo/` | M1b | 兩個症狀的講師 demo 腳本、七層組裝、# 手術刀、新舊命名對照 | `README.md` |
| `m2a-drift-experiment/` | M2a 第一輪 / 第二輪 | 漂移實驗兩輪 + 模型分組記錄 | `README.md`、`worksheet.md` |
| `lab1b-custom-instructions-and-prompts/` | Lab 1B | `/init` → AGENTS.md、Custom Instructions(applyTo)、Prompt File 三個完成版 | `AGENTS.md`、`.github/…` |
| `lab2-meeting-summary-skill/` | Lab 2 | 第一個 Skill,把 M2a 兩輪還沒收斂的漂移收掉 | `skills/meeting-summary/SKILL.md`、`sample-transcript.txt` |
| `lab3-wbs-and-prep-brief-skill/` | Lab 3A / 3B / M3c | WBS Excel(code execution)+ Weekly Follow-up Planner(MCP)+ 誤觸發實測 | `skills/…`、`data/`、`mcp/`、`m3c-mistrigger-test/` |
| `lab3d-meeting-ops-agent/` | M3d | 編排型 Custom Agent + Subagent(wbs-builder)+ Handoff(followup-planner)+ tool set 注意事項 | `agents/*.agent.md` 三份 |

## 環境需求

- VS Code + GitHub Copilot,Agent mode 可用;模型選單看得到 **Auto** 與至少一個可指定模型(M2a 分組用)
- Python 3.10+（Lab 3A）。**本資料夾與 `labs-part2` 共用同一個 venv**：請把兩包解壓到課前建好的上課資料夾裡、與 `.venv` 並排（例如 `C:\ghcp-workshop\` 底下同時有 `labs-part1\`、`labs-part2\`、`.venv\`），接著的**第一件事**就是在本資料夾執行：

  ```powershell
  ..\.venv\Scripts\Activate.ps1
  python -m pip install -r requirements.txt
  ```

  兩包的 `requirements.txt` 內容相同，只需在其中一邊裝一次，全天不再需要 `pip install`。
- 請用 VS Code **開啟本資料夾本身**(不要開父資料夾),`.vscode/settings.json` 才會把直譯器指到共用 venv,新終端機提示字元會出現 `(.venv)`。
- Lab 3B:MCP 三路徑擇一(CalendarTools / GitHub MCP / Microsoft Learn MCP),見該 Lab README
- 下半場會用到 GitHub repo + Copilot CLI + 雲端 coding agent:**請在上半場結束前把你的 workshop 專案 push 到一個你有寫入權限的 GitHub repo**,並把 `AGENTS.md` 與 `.github/` 一起 commit。

## 使用方式提醒

每個 Lab 的完成版都是「先自己寫、再對照」用的,不要一開始就複製——寫的過程本身就是在練 Scope / IO 的設計判斷。唯一例外是 Lab 1B 的 `fastapi.instructions.md`:它是給下半場 M4 / M7' 用的,直接複製即可。

## 這幾段如何串成一條線

```
M0   講師 demo Portal 終點(lab1)
M1b  Context Engineering:兩個症狀(找錯檔案、credit 燒太快)→ 七層組裝 → # 手術刀
M2a① 乾淨環境的漂移(lab2 逐字稿;半班 Auto、半班鎖模型)
Lab1.5 寫 copilot-instructions / applyTo instructions / prompt file
M2a② 有 instructions 之後仍漂移的部分 → 所以需要 Skill;模型選擇與用量
Lab2 meeting-summary 收掉剩下的漂移(第三輪)
Lab3 wbs-generator(code exec)+ weekly-followup-planner(MCP)
M3c  三個 Skill + 一個 prompt file:誤觸發實測
M3d  @meeting-ops(路由 + tools 白名單)+ subagent wbs-builder(下放 runCommands)+ handoff → @followup-planner
```
