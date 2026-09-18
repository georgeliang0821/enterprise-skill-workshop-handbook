# M8' · 踩坑⑥:分享與邊界

三件事,兩次踩坑、一張取捨表。

## ⑥a · 拆散的 bundle(5 分)
開一個乾淨資料夾(沒有 `.github/skills/`),只放 `meeting-ops.agent.md`,`@meeting-ops 幫我整理這場會議的紀錄`。它宣稱要用 meeting-summary,但 Skill 不存在 → 不報錯、自由發揮 → M2a 第一輪的漂移。
**agent + 它路由的 Skill + 它派的 subagent + 它 handoff 到的 agent 是一組**,不能單獨搬。另一個不在 `.github/` 底下的成員:**tool set**(使用者層級設定)。`.agent.md` 若寫 `tools: [meeting-tools]`,同事那邊沒有這個 tool set → 名稱被靜默忽略 → agent 照樣能用但沒有工具邊界。交付前展開成明確工具名。

## ⑥b · preview 抓到注入(10 分)
`community-skill-sample/web-notes-summarizer/SKILL.md` 是一個典型社群 Skill(故意留了破口);`sample-page-with-injection.md` 是含注入的「網頁內容」。
1. 找:⑤ 品質自檢哪裡不合格?③ 步驤哪一行是破口?
2. 踩:裝進 `.github/skills/`,餵 `sample-page-with-injection.md` 請它整理筆記 → 大概率多一句你沒要求的推銷文字。沒中?服從注入也是機率性的。
3. 修:照 `FORK-CHECKLIST.md` fork,重測。

## ⑥c · 三種分發方式的取捨(講解)
見 `distribution-options.md`。**不是只有一種對**:兩三個 Skill、同一個 repo → 直接 commit;跨 repo 共用、要鎖版 → `gh skill preview / install --pin`;全公司基準線 → Enterprise-Managed Plugins(管理員)。完整操作在 `../appendix-a-skill-bank-starter-kit/`。

## 決策點 ⑥(填進 M9 決策表)
你們的第一組資產,用哪一條路分享?
