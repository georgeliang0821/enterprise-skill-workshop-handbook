# CHANGELOG — meeting-ops(Custom Agent)

> `.agent.md` 也是要治理的資產。SemVer 一樣套用:新增一個可路由 Skill(對外行為相容)算 Minor;改變路由/邊界的對外行為算 Major。其中「**把一個寫入型 Skill 加進允許清單**」是最該被記錄、也最該被 review 的變更——它等於悄悄擴大了這個角色能造成的副作用範圍。

## v0.2.0 — 2026-07-08
### 變更
- tools 允許清單明確**排除** `skill:action-item-to-jira`(寫入型),並在指示中加入「建票交還使用者手動處理」的邊界規則。
### 原因(對應到的真實案例)
- M5 撞牆④:寫入型 Skill 的三連撞(重複建票、姓名硬塞、語意誤觸發)證明「整理會議」的角色不該有能力在使用者沒明講時動 Jira。兩層防線的 Agent 層。

## v0.1.0 — 2026-07-08
- 初版建立(上半場 M3d):編排型 agent,路由 meeting-summary / wbs-generator / weekly-followup-planner 三個 Skill。
