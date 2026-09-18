# AI Meeting Intelligence Portal Workshop — 上半場 Lab 素材(M0-M4,重構版)

這個資料夾對應重構版講義上半場的實作段落。跟前一版最大的差別:Lab 1 改為講師 demo、新增兩個「撞牆實驗」(M2a 漂移實驗、M3c 誤觸發實測)、Lab 4 改為「用 → 撞 → 修」三輪。

| 資料夾 | 對應模組 | 你會做出 / 經歷什麼 | 主要素材 |
|---|---|---|---|
| `lab1-portal-scaffold/` | M0 | 講師 live demo 用;學員可課後自行重現 Portal 前端 | `prompt.md` |
| `lab2-meeting-summary-skill/` | M2a + Lab 2 | 先做漂移實驗(baseline),再寫第一個 Skill 收斂它 | `skills/meeting-summary/SKILL.md`、`sample-transcript.txt` |
| `lab3-wbs-and-prep-brief-skill/` | Lab 3 | 兩種技術路徑:WBS Excel(code execution)+ Weekly Follow-up Planner(MCP) | `skills/wbs-generator/`、`skills/weekly-followup-planner/`、`data/`、`mcp/` |
| `m3c-mistrigger-test/` | M3c | 三個 Skill 並存時的誤觸發實測與修復 | `README.md`(指令清單與觀察表) |
| `lab4-openapi-fastapi-scaffold/` | M4 | scaffold 後端骨架 → 親手撞一次覆蓋事故 → 加保護修復 | `openapi/meeting-portal-api.yaml`、`skills/openapi-to-fastapi-scaffold/` |

## 環境需求總覽

- **共通**:VS Code + GitHub Copilot,Agent mode 可用
- **Lab 3A / Lab 4**:Python 3.10+;Lab 4 課前先 `pip install -r lab4-openapi-fastapi-scaffold/requirements.txt`
- **Lab 3B**:MCP 三路徑擇一(CalendarTools / GitHub MCP / fallback 資料),詳見該 Lab README
- **Lab 1(選做)**:Node.js 18+,只有想自己重現 Portal 前端的人需要

## 使用方式提醒

每個 Lab 資料夾裡都有:
- `README.md`:操作步驟與完成檢核
- `skills/<name>/SKILL.md`(如適用):**講師完成版**,建議先自己動手寫過一版再對照,不要一開始就直接複製——寫的過程本身就是在練習 Scope / IO / 品質規則的設計判斷。唯一例外是 Lab 4:那個 Lab 的重點是「用 → 撞 → 修」,完成版是直接拿來用的(而且它刻意留了一個洞,詳見 Lab 4 README)。

## 這幾段如何串成一條線

```
M0:講師 demo Portal 終點畫面(lab1 素材)
   ↓
M2a:漂移實驗——同一句 prompt,全班輸出長得不一樣(用 lab2 逐字稿)
   ↓
Lab2:寫 meeting-summary,把 M2a 的漂移收斂掉,做出 before/after
   ↓
Lab3:再做兩種技術路徑不同的 Skill —— WBS Excel(code exec)+ Weekly Follow-up Planner(MCP)
   ↓
M3c:三個 Skill 並存 → 用模糊指令實測誤觸發 → 改 description 修復
   ↓
Lab4:scaffold 後端骨架 → spec 改版重跑蓋掉手寫實作(撞牆)→ 加重跑保護(修復)
```

下半場(M5-M8)會延續這條線:Action Item 串接 Jira(第一個有寫入副作用的 Skill)、把今天三次撞牆的結果做成品質治理與版本升級、建立團隊 Skill Bank。
