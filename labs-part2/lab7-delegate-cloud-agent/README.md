# M7' · /delegate:把 M4 的骨架派給雲端 coding agent,review 它的 PR

## 前置(每個人)

- [ ] 骨架已 commit 並 push;`git status` 乾淨
- [ ] `AGENTS.md` 與 `.github/`(含 `instructions/fastapi.instructions.md`)已在 GitHub 上
- [ ] `gh auth status` 正常;組織已開通 Copilot coding agent
- [ ] 沒做完 M4 的人:把 `app-skeleton/app/` 複製成 repo 根目錄的 `app/`,commit、push

## 步驤

1. 在 Copilot CLI 切回預設 agent(不要用 `@meeting-ops` 派程式任務)。
2. 貼 `task-prompt.md` 的內容,前面加 `/delegate`(或用 `&` 前綴)。CLI 會問要不要把未提交變更 commit 成 checkpoint,然後給你 PR 連結 + agent session 連結。
3. 打開 session 連結看它工作(5–10 分):
   - 它讀了哪些檔案?**找 `AGENTS.md` 和 `fastapi.instructions.md`**
   - 它跑測試了沒?掛了有沒有自己修?
4. 用 `review-checklist.md` review PR。
5. 挑一個沒過的項目,在 PR 留言 `@copilot …` 請它補,看它在同一個 PR 上加 commit。
6. (選)VS Code chat 的「Delegate to cloud agent」、GitHub 上把 issue assign 給 Copilot——三個入口同一個後端。

## 兩個常見翻車

- **沒讀到 instructions**:`.github/` 沒 push、或 `applyTo` glob 跟路徑對不上(`app/**` vs `src/app/**`)。看 session 紀錄。
- **改了 `schemas.py`**:instructions 是路標不是牆——所以才有 review checklist。

## 決策點 ⑤(填進 M9 決策表)
你們回去第一個派出去的任務是什麼?挑「驗收標準寫得出來、有測試能驗、可以等、影響範圍被 instructions 跟 review 圈住」的。
