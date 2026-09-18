# AI Meeting Intelligence Portal Workshop — 下半場素材(M4–M9)

對應講義 `Handbook_Part2_v4.html`。主題:**把資產帶到每個地方(可攜)**;每一段結束在一個決策點。

| 資料夾 | 模組 | 性質 |
|---|---|---|
| `lab4-openapi-fastapi-scaffold/` | M4 | 講師 diff 示範(`instructor-demo/`)+ 學員跑包工具版 → commit/push |
| `lab5-jira-integration-skill/` | M5 | **動手**:naive 三連踩 → 防呆 → 決策點 ②(做選項 C:handoff → `@jira-clerk`) |
| `lab6-copilot-cli/` | M6' | **動手**:同一組 `.github/` 在 CLI 跑;`/agent` `/model` `/usage` |
| `lab7-delegate-cloud-agent/` | M7' | **動手**:`/delegate` 給雲端 coding agent 實作 M4 骨架 → review PR;含參考骨架 |
| `m8-share-and-boundaries/` | M8' | **動手**:拆散的 bundle、注入 preview;分發取捨表 |
| `m9-transfer/` | M9 | 決策表 + description 草稿 |
| `appendix-a-skill-bank-starter-kit/` | 附錄 A | Skill Bank / INDEX 登記 / gh skill,給團隊資產 Owner |

## 環境檢查(下半場開始前,每個人)

- [ ] workshop 專案是 git repo,已 push 到你有寫入權限的 GitHub repo;`.github/` 已 commit
- [ ] 組織已開通 Copilot CLI 與 Copilot coding agent(本梯次已確認)
- [ ] Copilot CLI 已安裝並 `/login`(見 `lab6-copilot-cli/README.md`)
- [ ] `gh auth status` 正常
- [ ] 共用 venv 就緒：本資料夾與 `labs-part1` 共用同一個 venv（就是課前在上課資料夾建的 `.venv`，與兩個 Lab 資料夾並排）。上半場已在 `labs-part1` 裝過套件的人這裡不用再做；沒裝過的在本資料夾執行 `..\.venv\Scripts\Activate.ps1`，再執行 `python -m pip install -r requirements.txt`。**下半場不需要其他 `pip install`。**
- [ ] 請用 VS Code **開啟本資料夾本身**(不要開父資料夾);新開終端機提示字元有 `(.venv)`

## 端到端路徑

```
M4   骨架(包工具)→ commit/push
M5   naive 三連踩 → 防呆 0.2.0 → 決策點②:handoff → @jira-clerk
M6'  CLI:/agent meeting-ops 同一份輸出;/usage 檢視用量
M7'  /delegate → 雲端 agent 實作骨架 → PR → review → @copilot 補
M8'  拆散 bundle / 注入 / 分發取捨
M9   決策表 ①–⑦ + 第一個 Skill 的 description 草稿
```
