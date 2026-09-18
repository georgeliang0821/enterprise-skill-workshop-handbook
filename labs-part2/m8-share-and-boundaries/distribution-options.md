# 三種分發方式的取捨

| 維度 | 直接 copy / git clone | `gh skill install --pin`(Public Preview) | Enterprise-Managed Plugins(Public Preview) |
|---|---|---|---|
| 誰動手 | 使用者自己搬 | 使用者自己拉(一行指令) | 管理員設定,使用者登入時自動套用 |
| 版本 | 快照,靠 commit hash 手動記 | frontmatter 注入來源 metadata;`--pin` 鎖 tag/SHA;`gh skill update` 偵測漂移 | 由 marketplace 設定決定 |
| 安全檢查點 | 無 | `gh skill preview` 安裝前看內容 | 管理員審 plugin 內容 |
| bundle 完整性 | 靠人記得 agent + subagents + skills 一起搬;tool set 不會跟著走 | 以 skill 為單位;agent 要另外處理 | plugin 本來就是 agents + skills + MCP 設定一包 |
| 需要什麼 | — | gh CLI ≥ 2.90;來源 repo 可讀 | 企業層級設定;目前為 preview,細節請查當時文件 |
| 對應今天的事故 | ⑥a 拆散的 bundle | ⑥b 注入 | ⑥a(plugin 天然是 bundle) |

## 什麼時候用哪個

- **兩三個 Skill、一個團隊、同一個 repo** → 直接 commit 進 repo。不需要 Skill Bank。
- **跨 repo 共用、開始有人問「這版跟上版差在哪」** → `gh skill` 的 preview 與 pin 開始有價值(附錄 A.3)。
- **全公司要有基準線、不能靠每個人記得裝** → 管理員的事:Enterprise-Managed Plugins。
