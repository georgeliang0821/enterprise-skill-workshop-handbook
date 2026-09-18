# Skill Bank Index

團隊所有 Skill 的中央清單。**每新增或修改一個 Skill,都要同步更新這張表**——這張表本身就是團隊查找「有沒有現成 Skill 可以用」的第一入口,避免同事重複造輪子或不小心做出兩個功能重疊的 Skill。它也是**登記 gate**:一個 Skill 要標成 `Active` 讓大家依賴之前,命名、Owner、寫入型審核、scope 都在這裡把關(見下方檢查清單)。

| Skill 名稱 | 版本 | Owner | 狀態 | Scope | 寫入型? | 依賴的外部工具/MCP server | 用途一句話 |
|---|---|---|---|---|---|---|---|
| `meeting-summary` | 0.1.0 | (填團隊成員) | Active | project | 否 | 無 | 從逐字稿產生摘要/決議/風險/待辦四區塊 |
| `wbs-generator` | 0.1.0 | (填團隊成員) | Active | project | 否 | 無(本地 Python + openpyxl) | 從專案範圍描述或逐字稿產生 WBS Excel 檔案 |
| `weekly-followup-planner` | 0.3.0 | (填團隊成員) | Active | project | 否 | CalendarTools(MCP,Agent365,需租戶開通) | 依本週行事曆空檔與未結 Action Item 產生跟進規劃 |
| `openapi-to-fastapi-scaffold` | 0.2.0 | (填團隊成員) | Active | project | 否 | 無(本地 CLI 工具 `datamodel-codegen`) | 從 OpenAPI 規格產生 FastAPI router 骨架 + Pydantic model |
| `action-item-to-jira` | 0.2.0 | (填團隊成員) | Active | project | **是(需 Owner review)** | Jira REST API(直接呼叫,非 MCP) | 把結構化待辦同步建立成 Jira 票 |

## Agents(.agent.md 也要登記)

| Agent 名稱 | 版本 | Owner | 狀態 | 路由到哪些 Skill | 刻意排除哪些 Skill |
|---|---|---|---|---|---|
| `meeting-ops` | 0.2.0 | (填團隊成員) | Active | meeting-summary / wbs-generator / weekly-followup-planner | **action-item-to-jira(寫入型,M5 護欄)** |

> 「依賴欄」對 agent 比對 Skill 更關鍵:它是分發時的檢查依據——agent + 它路由的 Skill 是**一組 bundle**,不能單獨搬一個 `.agent.md`(hands-on 動手 4 會親眼驗證)。「刻意排除」欄同樣重要:把一個寫入型 Skill **加進**某個 agent 的允許清單,屬於 Major 級變更、需 Owner review。

## 狀態欄位定義

- **Draft**:個人測試中,還沒經過任何人 review,不建議其他人依賴。
- **Active**:已有明確 Owner、經過至少一次 review,團隊可以放心使用。**寫入型 Skill(「寫入型?」欄為「是」)標成 Active 前,一定要有明確 Owner 過目一次**——這是 M5 `action-item-to-jira` 那種「有寫入副作用」的 Skill 的硬性要求,唯讀型沒有。
- **Deprecated**:不建議再用,通常會註明「請改用 <新 Skill 名稱>」。

## Scope 欄位定義

- **project**:團隊資產,跟著 repo 走、大家一起 `git pull` / `gh skill install` 就有。今天五個 Skill 都是 project。
- **user**:個人習慣用的 Skill,裝在自己 home 目錄、不進團隊版控。判斷 project 還是 user,其實就是在回答「這個 Skill 的 Owner 是團隊還是個人」。

## 新增一個 Skill 到這張表時,順便檢查(登記 gate)

- [ ] **命名 gate**:名稱符合 `NAMING-CONVENTION.md`;特別是**不要用人名/團隊名當前綴**(Skill 是團隊資產,不是個人工具),**不要把版本號塞進名稱**(`meeting-summary-v2` 這種——版本放 `version:` 欄位和 `CHANGELOG.md`,否則新版上線時所有引用路徑都要跟著改)。就算 Skill 是用 generator 產出來的,也要用這兩條擋一下。
- [ ] 是否已經有功能重疊的既有 Skill(先查這張表,不要先動手寫)
- [ ] `SKILL.md` 旁邊有沒有對應的 `CHANGELOG.md`
- [ ] Owner 欄位是否填了真實負責人,不是留空
- [ ] **寫入型審核 gate**:這個 Skill 會不會**寫入外部系統**?如果會(「寫入型?」欄標「是」),標成 `Active` 前一定要有明確 Owner 過目一次(一個 PR / MR review 就能做到),不能寫完直接讓全 team 依賴。
- [ ] **Scope**:這個 Skill 是團隊資產(project)還是個人習慣(user)?填進 Scope 欄。
- [ ] 如果這個 Skill 依賴 MCP server 或其他外部工具,「依賴的外部工具/MCP server」欄位是否填寫清楚——尤其是像 CalendarTools 這種不是每個租戶都已開通的功能,要讓接手的人第一時間就知道要先檢查什麼
