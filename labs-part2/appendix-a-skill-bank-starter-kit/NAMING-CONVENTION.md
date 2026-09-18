# Skill 命名規範

> **附錄。** 命名的兩條硬性治理規則(不要用人名/團隊名當前綴、不要把版本號塞進名稱)已成為 `skills/INDEX.md` 的**登記 gate**。這份文件是完整參考;實際把關以 INDEX 的檢查清單為準。

## 基本規則

- 全小寫,單字之間用連字號(`-`)分隔,不用底線或駝峰式。
- 資料夾名稱與 `name:` frontmatter 欄位保持一致。
- 名稱長度控制在 2-4 個字詞以內——太長代表 Scope 可能太大,該考慮拆分(回顧 M2 的 Scope 判準:工具/寫入權限邊界是否不同、是否永遠強依賴共同觸發、未來會不會被單獨呼叫)。

## 依 Skill 的性質選對應的命名模式

今天做出來的五個 Skill,剛好對應到三種常見模式,之後團隊新增 Skill 時可以直接比照:

| 命名模式 | 意涵 | 今天的範例 |
|---|---|---|
| `<領域>-<動作>` | 對某個領域資料做萃取/處理 | `meeting-summary`、`weekly-followup-planner` |
| `<物件>-generator` | 從既有內容產生結構化檔案或產物 | `wbs-generator` |
| `<來源>-to-<目標>` | 把一種格式/系統轉換或同步到另一種 | `openapi-to-fastapi-scaffold`、`action-item-to-jira` |

## 避免的命名方式

- ❌ 用人名或團隊名當前綴(例如 `david-meeting-tool`)——Skill 是團隊資產,不是個人工具。
- ❌ 用版本號當名稱的一部分(例如 `meeting-summary-v2`)——版本資訊放在 `version:` frontmatter 和 `CHANGELOG.md`,不要放進名稱,否則新版上線時,舊的引用路徑全部要跟著改。
- ❌ 名稱過度技術化、脫離業務語意(例如 `llm-json-transform-01`)——名稱應該讓不寫程式的同事也看得懂這個 Skill 在做什麼。

## Owner 規範

每個 Skill 都要有一個明確的 Owner(可以是個人或小組),寫在 `INDEX.md` 裡。Owner 的責任是:

1. 負責審核這個 Skill 的變更(見 M6 討論的品質治理流程)。
2. 收到「這個 Skill 輸出怪怪的」回報時,是第一個該被通知的人。
3. 決定這個 Skill 要不要升版、要不要棄用。

沒有 Owner 的 Skill,狀態應該保持 `Draft`,不建議標示成 `Active` 讓其他人依賴。
