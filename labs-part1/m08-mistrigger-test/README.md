# M8 · 翻車②:誤觸發實測——三個 Skill 互相干擾

**前置條件**:你的 `.github/skills/` 裡同時存在 `meeting-summary`、`wbs-generator`、`weekly-followup-planner` 三個 Skill(Lab 6 + Lab 7 的產出)。沒寫完自己版本的,暫時把三份完成版 SKILL.md 放進去即可參加。

GitHub Copilot 的 Skill selection 是**機率性語意匹配**——description 不夠具體、沒有清楚的對比詞,多個 Skill 之間就會互相干擾、選錯或選不到。這 15 分鐘直接測。

## 素材路徑

- 📄 `../m07-wbs-and-followup-planner/data/past-action-items.json`
- 📄 `../m06-meeting-summary-skill/sample-transcript.txt`

## 操作(每一句都開新對話,避免上下文污染)

### 模糊指令一:三方共用關鍵詞

附上 `past-action-items.json`,只說:

> 幫我看一下這些 action item

三個 Skill 的 description 裡都有 "action item" 這個詞。觀察:選中了誰?還是誰都沒選、直接回答?

### 模糊指令二:一句話沾到三個 Skill

附上 `sample-transcript.txt`,說:

> 幫我把會議裡的待辦整理一下,排個計畫

「整理待辦」指向 meeting-summary,「排個計畫」同時沾到 wbs-generator(拆解)跟 weekly-followup-planner(排程)。

### 模糊指令三:零關鍵詞命中

不附任何檔案,說:

> 我下週要跟進這個專案,幫我準備一下

沒有任何 Skill 的關鍵詞被直接命中——看它會硬選一個,還是不觸發。

### 觀察記錄表

| 指令 | 你的機器選中的 Skill | 隔壁同學選中的 | 一致嗎? |
|---|---|---|---|
| 一 |  |  |  |
| 二 |  |  |  |
| 三 |  |  |  |

講師收集現場結果——**同一句指令,不同人的機器選中的 Skill 很可能不一樣**。這本身就是最重要的觀察:selection 是機率性的,description 的工作是把機率分佈收窄,不是給出保證。

### 修復回合

挑一句你這邊選錯(或該觸發卻不觸發)的指令,回頭改對應 Skill 的 description——加對比句、加關鍵詞、或把容易誤導的詞拿掉——**開新對話**再測一次,確認行為改變。

## 帶得走的兩個習慣

- description 用對比句法,不是只堆關鍵詞:「是逐字稿產出的結構化紀錄,不是排程規劃」,而不是單純寫「摘要、逐字稿、summary」。
- 新增 Skill 時,把新舊 description 一起丟給 Copilot,問「這兩個會不會混淆、什麼情況下會選錯」——不需要自動化互斥檢查,但至少人工過一次這道關。

## 完成檢核

- [ ] 三句模糊指令都測過,記錄了各自選中(或未選中)的 Skill
- [ ] 至少跟一位同學比對過結果,理解「機率性」的實際意涵
- [ ] 完成至少一次 description 修改 → 重測 → 行為改變的迴圈

> 📌 **跟下半場的關係**:企業內部很快會累積 5-10 個以上相似的 Skill,誤觸發從偶發變日常。M6 的品質治理會把這 15 分鐘的手動測試,升級成有版本紀錄、有回歸測試觀念的治理流程——你剛做的,就是那套流程的最小可行版。


## 對照組——Prompt File 為什麼永遠不會誤觸發

三句模糊指令跑完後,再做一件事:附上逐字稿、打 `/meeting-quickcheck`(M4 建的)。它每次都準確執行、每次都只做它那兩件事——因為它根本沒有參與 selection,是你喊它才出現。

所以當一個能力「一定要人明確叫、不能被語意猜中」時,你有兩個選擇:寫成 prompt file,或寫成 Skill 但設 `disable-model-invocation: true`。差別只在要不要帶附件與腳本。下半場的寫入型 Skill 會用到後者。
