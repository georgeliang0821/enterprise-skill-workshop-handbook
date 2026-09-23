# AI Meeting Intelligence Portal Workshop — 下半場素材(M9–M14)

對應講義 `Handbook_Part2_v5.html`。Workshop「從 Prompt 到團隊資產」下半場主題:**從 Skill 到 Agent**——M9–M11 是「誰決定、誰能碰什麼」(Custom Agent、Subagent、Handoff、寫入型 Skill);M12–M14 是「可攜」(applyTo instructions、OpenAPI 骨架、CLI、雲端 agent)。資料夾編號 = 講義模組編號。

| 資料夾 | 模組 | 性質 |
|---|---|---|
| `m09-meeting-ops-agent/` | M9 / M10 | **動手**:翻車③ 編排失控 → `@meeting-ops`(薄路由 + tools 白名單)→ subagent `wbs-builder` → handoff `@followup-planner`;三份完成版 `.agent.md` |
| `m11-jira-integration-skill/` | M11 | **動手**:naive 三連踩 → 防呆 → 決策點「誰有權觸發 Jira 開單?」(實作人工確認 handoff → `@jira-clerk`) |
| `m12-openapi-fastapi-scaffold/` | M12 | applyTo instructions 完成版 + 講師 diff 示範(`instructor-demo/`)+ 學員跑包工具版 → commit/push |
| `m13-copilot-cli/` | M13 | **動手**:同一組 `.github/` 在 CLI 跑;`/agent` `/model` `/usage` |
| `m14-delegate-cloud-agent/` | M14 | **動手**:`/delegate` 給雲端 coding agent 實作 M12 骨架 → review PR;含參考骨架 |

## 環境檢查(下半場開始前,每個人)

- [ ] workshop 專案是 git repo,已 push 到你有寫入權限的 GitHub repo;`AGENTS.md` 與 `.github/` 已 commit
- [ ] 組織已開通 Copilot CLI 與 Copilot coding agent(本梯次已確認)
- [ ] Copilot CLI 已安裝並 `/login`(見 `m13-copilot-cli/README.md`)
- [ ] `gh auth status` 正常
- [ ] 共用 venv 就緒:本資料夾與 `labs-part1` 共用同一個 venv(就是課前在上課資料夾建的 `.venv`,與兩個 Lab 資料夾並排)。上半場已在 `labs-part1` 裝過套件的人這裡不用再做;沒裝過的在本資料夾執行 `..\.venv\Scripts\python.exe -m pip install -r requirements.txt`。**下半場不需要其他 `pip install`。**
- [ ] 請用 VS Code **開啟本資料夾本身**(不要開父資料夾);新開終端機提示字元有 `(.venv)`

## 端到端路徑

```
M9   翻車③:預設 Agent Mode 編排失控 → @meeting-ops(人設 + 薄路由 + tools 白名單)
M10  subagent wbs-builder(下放 runCommands)+ handoff → @followup-planner(send: false)
M11  naive 三連踩 → 防呆 0.2.0 → 決策點:誰有權觸發 Jira 開單 → 人工確認 handoff → @jira-clerk
M12  applyTo instructions → OpenAPI 骨架(包工具)→ commit/push
M13  CLI:/agent meeting-ops 同一份輸出;/usage 檢視用量
M14  /delegate → 雲端 agent 實作骨架 → PR → review → @copilot 補
總回顧 四個決策點 + 回去第一個 Skill 的 description 草稿
```
