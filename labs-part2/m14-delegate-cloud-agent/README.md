# M14 · /delegate:把 M12 的骨架派給雲端 coding agent,review 它的 PR

> **這一段的重點是 review,不是派任務。** M12 的可信度來自「可重現」(跑兩次 byte-level 一樣);這裡的工作本質上不可重現——派兩次一定得到兩份不同的 PR。可信度換了來源:**可驗收**。
>
> 一句話:**instructions 是路標,不是牆。** 事前的規則只提高機率,事後的 review checklist 才是牆。

## 前置(每個人)

- [ ] 骨架已 commit 並 push;`git status` 乾淨
- [ ] `AGENTS.md` 與 `.github/`(含 `instructions/fastapi.instructions.md`)**已在 GitHub 上**——雲端 agent 讀不到你本機的檔案
- [ ] `gh auth status` 正常
- [ ] 沒做完 M12 的人:把 `app-skeleton/app/` 複製成 repo 根目錄的 `app/`,commit、push

### 組織沒開通 Copilot coding agent 怎麼辦

不影響你學到這一段的重點。兩個 Plan B:

- **跟鄰座併機**:兩個人看同一個 PR,各自獨立跑一次 checklist,再對答案(比自己跑更有收穫——你會發現兩個人抓到的項目不一樣)。
- **用講師的 PR 連結**做 review,步驟 4 之後完全一樣。

## 步驟

1. 在 Copilot CLI 切回預設 agent(不要用 M13 選的 `@meeting-ops` 派程式任務——它的 tools 邊界是為會議紀錄設的)。
2. 貼 `task-prompt.md` 的內容,前面加 `/delegate`(或用 `&` 前綴)。CLI 會問要不要把未提交變更 commit 成 checkpoint,然後給你 PR 連結 + agent session 連結。
3. 打開 session 連結看它工作(10–20 分,視佇列而定):
   - 它讀了哪些檔案?**找 `AGENTS.md` 和 `fastapi.instructions.md`**
   - 它跑測試了沒?掛了有沒有自己修?
4. 用 `review-checklist.md` review PR。六項裡 a、b、c、d1 是必過的。
5. 挑一個沒過的項目,在 PR 留言 `@copilot …` 請它補,看它在同一個 PR 上加 commit。**這是迭代迴圈,不是重派**——重派會得到另一份不相干的 PR,你剛才 review 的功夫就白費了。
6. (選)VS Code chat 的「Delegate to cloud agent」、GitHub 上把 issue assign 給 Copilot——三個入口同一個後端,就是 M13 那張表最右欄。

## 兩個你現在應該認得出來的設計

- **「agent 填了 stub,不是違反 instructions 嗎?」** 不是。M12 那份 instructions 分「骨架階段」和「實作階段」兩段,同一份檔案管兩個階段,由讀它的 agent 判斷現在在哪一階段。你寫的時候用不到的那一半,今天兌現了。
- **「不要修改 `schemas.py`」為什麼寫了兩次?** 一次在 instructions(context,會不會被讀是機率),一次在 task prompt(這次一定看得到)。**重要的約束值得寫兩次**,這是對「路標不是牆」的務實回應。

## 兩個常見翻車

- **沒讀到 instructions**:`.github/` 沒 push、或 `applyTo` glob 跟路徑對不上(`app/**` vs `src/app/**`,或忘了把 `tests/**` 納進來)。**看 session 紀錄,不要猜。**
- **改了 `schemas.py`**:instructions 是路標不是牆——所以才有 review checklist。也是為什麼 M12 那條「重跑不覆蓋已有實作」在雲端 agent 時代更重要:會來改你檔案的,已經不只你自己了。

## 決策點:什麼該派出去、什麼留在本機?

M13 那張表比的是「三個執行面讀得到哪些資產」;這張表回答下一個問題:**手上這個任務,該不該進最右邊那一欄。**

| 派給雲端 agent | 留在本機(VS Code / CLI) |
|---|---|
| 驗收標準寫得出來、有測試能驗 | 還在探索、需要來回討論的 |
| 可以等 10–30 分鐘的 | 要立刻看到結果的 |
| 影響範圍被 instructions 跟 review 圈住的 | 會碰到秘密、生產設定、或沒有測試保護的 |
| 你願意用 PR review 當最後一道牆的 | 你需要每一步都同意的 |

左欄四條是同一句話的四種說法:**你能不能把「做對了」定義成一組別人可以檢查的條件。** 定義得出來就能派,定義不出來就留著自己做。

今天的任務刻意選了左欄全中的:骨架 → stub + 測試。你們回去第一個派出去的任務,建議也是這種。

## 完成檢核

- [ ] 雲端 agent 開了 draft PR;**session 紀錄裡看得到它讀了 `fastapi.instructions.md`**(主證據)
- [ ] PR 通過 checklist 的 a、b、c、d1;沒過的那項你用 `@copilot` 留言請它補,它在同一個 PR 上補了 commit
- [ ] `app/models/schemas.py` 沒被動到(或被動到了,而你抓到了——兩種都算學到)
- [ ] 能說出:「同一組 `.github/`,VS Code、CLI、雲端 agent 三個地方都讀得到;不同的是 UI 機制跟連線設定」
- [ ] 能說出 M12 和 M14 的可信度分別建立在什麼上面:**一個是可重現,一個是可驗收**