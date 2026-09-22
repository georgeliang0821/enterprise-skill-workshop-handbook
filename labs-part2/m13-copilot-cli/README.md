# M13 · Copilot CLI:同一組 .github/ 資產,在終端機執行一次

## 安裝與登入(課前)

- Windows:`winget install GitHub.Copilot`
- macOS / Linux:`brew install copilot-cli` 或 `curl -fsSL https://gh.io/copilot-install | bash`
- 任一平台:`npm install -g @github/copilot`

進 repo 根目錄執行 `copilot`,第一次用 `/login`。組織要開通 Copilot CLI 政策(本梯次已開通)。

## 15 分鐘步驟

1. `copilot` → `/agent`:清單裡應有 `meeting-ops`、`wbs-builder`、`followup-planner`、`jira-clerk`——它讀的是 `.github/agents/`,跟 VS Code 同一份;repo 根目錄的 `AGENTS.md` 也會自動載入。選 `meeting-ops`。
2. 「幫我整理這場會議的紀錄,逐字稿在 labs-part1/m06-meeting-summary-skill/sample-transcript.txt,會議日期 2026-07-08」→ 比對 VS Code 的輸出(四區塊、日期、Owner)。
3. `/usage` → 記下這一輪的用量。`/model` 切到 Auto → `/clear` → 再跑一次 → `/usage` 再看一次。
4. 試「順便開成 Jira 工單」:CLI 沒有 VS Code 的按鈕 UI(handoff 在 CLI 的呈現以當天版本為準),但拒絕與交還的行為應一致——因為硬鎖在 Skill、排除語句在 body,兩者走到哪都在。
5. (選)`/mcp`:CLI 的 MCP 設定跟 `.vscode/mcp.json` 分開;用 `/mcp add` 把 Microsoft Learn MCP(`https://learn.microsoft.com/api/mcp`)加一次。
6. (選)`Shift+Tab` 切到 autopilot 看一眼它的權限提示——不要在這裡開,M14 會用到雲端那條路。

## 觀察記錄

| | VS Code | CLI(鎖模型) | CLI(Auto) |
|---|---|---|---|
| 四區塊一致? | | | |
| Due Date 一致? | | | |
| /usage 數字 | — | | |
| 對「開單」的反應 | 按鈕 + 交還 | | |

## 可攜性通則(帶走)

- **repo 內的檔案**(AGENTS.md、agents / skills / instructions):可攜性最高——三個執行面都讀。
- **UI 機制與使用者層級設定**(handoff 按鈕、工具勾選清單、tool set):最低——換執行面或換人就要重新確認。
- **連線設定**(MCP):要各自做一次。

## 決策點:三個執行面
哪類工作放 VS Code、哪類放 CLI、哪類派給雲端 agent?(講義 M13 的比較表)
