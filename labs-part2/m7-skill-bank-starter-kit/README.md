# M7 團隊共用與 Skill Bank 建置 —— 討論素材 + 動手

M7 是【講解+討論+動手】模組。這個資料夾就是一個**可以直接帶回去用的 Skill Bank 起手式**——`skills/` 底下已經歸檔了今天做出的五個 Skill，每個都配好 `SKILL.md` + `CHANGELOG.md`，外加命名規範、Fork 檢查清單、索引表;`hands-on/` 底下則是三段動手實作的素材。

## 資料夾內容

| 檔案/資料夾 | 用途 |
|---|---|
| `skills/INDEX.md` | Skill Bank 的中央索引,團隊查找/新增 Skill 前都先看這張表 |
| `skills/<name>/SKILL.md` + `CHANGELOG.md` | 今天五個 Skill 的正式歸檔格式(範例) |
| `NAMING-CONVENTION.md` | 命名規則(附錄;權威的兩條登記 gate 在 `skills/INDEX.md`) |
| `FORK-CHECKLIST.md` | 引用社群 Skill、Fork 成團隊版時的檢查清單(附錄) |
| `hands-on/README.md` | **四段動手**:`gh skill install`、填 INDEX 登記、撞牆⑤a(preview 抓注入 + 實際觸發看它服從)、撞牆⑤b(拆散的 bundle 當場失效) |
| `hands-on/hello-test/` | `gh skill install` 的最小可安裝範例 Skill |
| `hands-on/community-skill-sample/` | 社群 Skill 範例(故意留了品質與注入破口)+ `sample-page-with-injection.md`(含注入的假網頁內容,實際觸發用) |
| `hands-on/INDEX-EXERCISE.md` | INDEX 登記的填空練習版 |
| `agents/meeting-ops/` | `@meeting-ops` 的正式歸檔(`.agent.md` + CHANGELOG)——bundle 撞牆測試與分發示範用 |

## 建議的討論 + 動手流程

1. **Skill Bank 結構與 INDEX 治理**:看 `skills/INDEX.md` 怎麼當登記 gate——命名(不用人名前綴、不塞版本號)、Owner、**寫入型 Skill 標 Active 前需審核**(像 `action-item-to-jira`)、Scope(project vs user)。
2. **分發方法比較**:討論手動 copy-paste / raw download / `gh skill install` 在保真度、版本追蹤、更新、供應鏈安全、版本鎖定上的差別(見講義 M7 比較表)。
3. **四段動手**:照 `hands-on/README.md` 跑——`gh skill install` 裝 `hello-test`(講師提供當天 repo)、填 `INDEX-EXERCISE.md`、撞牆⑤a(preview 找出注入破口 → 實際觸發親眼看它服從 → fork 硬化)、撞牆⑤b(只裝 `.agent.md` 不裝 Skill,看 `@meeting-ops` 當場失效)。
4. 討論:回去之後這個 Skill Bank 要放在公司的哪裡(內部 repo、還是接 EAA 既有的 Skill 管理機制)、Owner 要怎麼分配。

## 什麼時候一個 Skill 需要「有人先看過才能上線」

這是延續 M6 尾聲提到的問題:一個 Skill 只是「個人測試用」,不需要任何審核,自己改自己用;但一旦它變成**團隊共用的資產**——尤其是像 `action-item-to-jira` 這種**會寫入外部系統**的 Skill——建議至少要有明確的 Owner 過目一次再發布,而不是寫完就直接讓所有人使用。

具體怎麼做因團隊規模而異,常見的最小可行做法是:

```
個人草稿 Skill
     ↓
提交給 Owner / 指定的人審核(看 SKILL.md 的內容跟一次實際觸發的輸出)
     ↓
確認沒問題 → 合併進團隊 Skill Bank,更新 INDEX.md,狀態改成 Active
```

這一步不需要额外的工具或系統支撐,一個 PR / MR 的 review 流程就能做到——重點是**「有沒有一個人在正式生效前看過一次」這個習慣有沒有被建立起來**,而不是流程本身要多複雜。
