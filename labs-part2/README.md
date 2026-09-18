# AI Meeting Intelligence Portal Workshop — 下半場素材(M5-M8)

延續上半場(M0-M4)做出來的 Portal 前端、三個抽取 Skill、以及後端骨架,下半場把這些東西「企業化」:接上既有系統、做品質治理、正式歸檔成團隊資產。

| 資料夾 | 對應模組 | 性質 |
|---|---|---|
| `lab5-jira-integration-skill/` | M5 | **動手(用→撞→修→護欄)**:naive 版三連撞寫入事故 → 自己硬化 → `@meeting-ops` 護欄。Mock Jira Server 是安全沙箱 |
| `m6-quality-hardening-kit/` | M6 | **動手(收割)**:把今天四次事故填進收割表 → 轉寫 CHANGELOG → 判斷版本號 |
| `m7-skill-bank-starter-kit/` | M7 | 講解壓縮 + **四段動手**:Skill Bank 起手式(INDEX 登記治理、含 `agents/meeting-ops/`)、gh skill install、撞牆⑤a(preview 抓注入+實際觸發)、撞牆⑤b(拆散的 bundle) |

M8 改為「transfer 練習 + 總回顧 + Q&A」:每人為自己團隊的一個真實痛點寫 Skill description 草稿、互做混淆檢查、判斷唯讀/寫入型——不需要額外素材,判準都在今天五次撞牆裡。

## 環境需求

- **Lab5(動手)**:Python 3.10+,`pip install -r lab5-jira-integration-skill/requirements.txt`
- **M6 / M7**:討論與文件範本不需額外安裝;M7 動手的 `gh skill install` 需 gh CLI ≥ 2.90.0(見課前環境檢查表)
