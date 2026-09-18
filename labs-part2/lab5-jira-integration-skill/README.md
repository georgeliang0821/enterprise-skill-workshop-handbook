# Lab 5:寫入型 Skill —— 先撞事故,再自己硬化(Action Item → Jira)

這個 Lab 不需要真實 Jira 帳號。`mock_jira_server.py` 模擬 Jira 的查詢/建票 API——**它是假的,正因為是假的,才是撞「寫入事故」的完美沙箱**:重複建票、指派錯人,在這裡零成本,在真 Jira 上是團隊工作流程的實際混亂,而且不一定會被立刻發現。

> **重構版定位變更**:這一段從「講師 Demo 四個安全設計」改為學員動手的「**用 → 撞 → 修**」——跟 Lab 4 同構,但這次撞的是全天副作用最大的一種。你會先用一個「刻意天真版」Skill 三連撞,再自己把它硬化,最後對照完成版。

## 素材

| 檔案 | 用途 |
|---|---|
| `mock_jira_server.py` | 假 Jira(查詢 / 建票 / `debug/issues` / `debug/reset`) |
| `skills/action-item-to-jira/SKILL-naive.md` | **撞牆輪用的刻意天真版(v0.1.0-naive)**——第一輪直接用它 |
| `skills/action-item-to-jira/SKILL.md` | 硬化完成版——**第三輪做完前不要偷看** |
| `action-items-from-lab3.md` | 結構化待辦清單(模擬上半場產出) |
| `owner-jira-mapping.json` | Owner 姓名 → Jira 帳號對照表(第三輪才用得到) |

## 第零步:啟動 Mock Jira Server

套件已由共用 venv 裝好,**不需要 `pip install`**。在本資料夾開一個終端機,確認提示字元有 `(.venv)`,然後:

```powershell
$env:JIRA_API_TOKEN = "mock-jira-token-classroom-only"
python -m uvicorn mock_jira_server:app --reload --port 9000
```

開 `http://127.0.0.1:9000/docs` 確認 Swagger UI 正常。token 之後由 Skill 從環境變數讀,不寫死在任何檔案裡。

> 環境變數只在這個終端機視窗有效——之後要在別的視窗跑 Skill 的話,那個視窗也要設一次。

## 第一輪:用(naive 版跑起來,看似正常)

1. 把 `SKILL-naive.md` 的內容複製到你的專案 `.github/skills/action-item-to-jira/SKILL.md`。
2. 用 Agent mode 提供 `action-items-from-lab3.md`、專案代碼 `MIP`、Mock Server 位置 `http://127.0.0.1:9000`,下指令:「幫我把這些待辦事項同步到 Jira,專案代碼是 MIP」。
3. 驗證:`curl.exe http://127.0.0.1:9000/debug/issues` ——三筆票建立成功,票號正確回報。**看起來一切正常,這正是天真版最危險的地方:它能動。**

## 第二輪:撞(三連撞)

### 撞 A:重複建票

對**同一份** `action-items-from-lab3.md` 再觸發一次,然後:

```powershell
curl.exe http://127.0.0.1:9000/debug/issues
```

六筆票,三筆是重複的。真 Jira 上,這代表 David 的 dashboard 上同一個任務出現兩次,團隊開始搞不清楚哪張才是真的。

### 撞 B:姓名硬塞

看 debug 輸出的 `assignee` 欄——是 `"David"`、`"Mary"` 這種**姓名字串**,不是 Jira 帳號。Mock Server 照單全收,這很寫實:**寬鬆的 API 不會幫你擋,錯的資料就是靜靜地進去了**。真 Jira 上這筆指派會失效或掛到錯的人身上。

### 撞 C:語意誤觸發

開新對話,附上待辦清單,**只隨口說一句**:「這些待辦事項要記得追蹤」——不明確要求建票。觀察 Copilot 會不會因為 naive 版的 `disable-model-invocation: false` + description 裡的「追蹤」關鍵詞,**自己跑去建票**。

> 這裡跟上半場 M3c 是同一課:**觸發是機率性的**——這次沒觸發不代表下次不會。對唯讀 Skill 你可以賭這個機率,對會寫入外部系統的 Skill,你敢賭嗎?這一撞直接推導出 `disable-model-invocation: true` 為什麼是架構層防呆,不是選配。

撞完清場,準備硬化:

```powershell
curl.exe -X POST http://127.0.0.1:9000/debug/reset
```

## 第三輪:修(自己硬化)

針對三個撞點,**用自己的話**修改你的 SKILL.md:

1. **去重**(對撞 A):③ 步驟加上「建票前先呼叫 `GET /rest/api/2/search` 用 summary 關鍵字查詢是否已存在;已存在則略過並註明」。
2. **Owner 對照**(對撞 B):② 輸入加上 `owner-jira-mapping.json` 為必要輸入;③ 步驟改為「assignee 用對照表查到的帳號,**查不到就標記失敗,不用姓名硬塞**」。
3. **鎖自動觸發**(對撞 C):frontmatter 改 `disable-model-invocation: true`,version 升為 `0.2.0`(這次變更本身就是 M6 要收割的一筆)。
4. 順手補 ⑤ 品質自檢:去重、對照失敗誠實回報、token 不出現在輸出/log、每筆都有明確狀態。

然後驗收(這就是原本講師 demo 的四個驗證,現在是你自己的硬化成果):

- 重新提供對照表 + 待辦清單,明確打 `/action-item-to-jira` 觸發 → `debug/issues` 三筆票、assignee 是 email。
- 同一份清單再觸發一次 → 輸出標註「已存在,略過」,沒有重複票。
- 把 `owner-jira-mapping.json` 其中一筆刪掉再觸發 → 該筆誠實回報「失敗:找不到 Jira 帳號」。
- 把 `$env:JIRA_API_TOKEN` 設錯再觸發 → 誠實回報「認證失敗」,輸出/log 完全看不到 token 值。
- 隨口說「這些待辦要記得追蹤」→ **不會**自動觸發,只有明確打 `/action-item-to-jira` 才執行。

最後對照完成版 `SKILL.md`,比較你的寫法差異——特別看它 ① 裡「不要自作主張連建票都做了」跟 ② 裡 401 的處理方式。

## 第四輪:回頭幫 @meeting-ops 加護欄

現在你手上有:上半場 M3d 的編排型 `@meeting-ops`,跟一個剛硬化完、**會真的寫入**的 Skill。設計題:要不要讓 `@meeting-ops` 叫得動它?

這題有三個選項——**它們都合法,差別在你們願意讓誰決定「開不開」**:

| 選項 | 做法 | 方便 | 風險 | 誰決定 |
|---|---|---|---|---|
| A 放進路由 | body 加「要開單用 action-item-to-jira」,Skill 不鎖 | 最方便 | 踩 C 看過:隨口一句就可能開單;開單靠終端機打 REST,`@meeting-ops` 若還留著 `runCommands`(沒做 M3d 05b),tools 牆完全攔不住 | 模型 |
| B 完全排除 | Skill `disable-model-invocation: true`;body 排除;使用者自己 `/action-item-to-jira` | 最不方便 | 最低 | 人,但沒人提醒 |
| C handoff 按鈕 | Skill 同 B 硬鎖;另建只有 Jira 工具的 `@jira-clerk`;`@meeting-ops` 用 `handoffs:` 給一顆「建立 Jira 工單」按鈕,`send: false` | 整理完就看到按鈕 | 低:沒人按不會發生;按了也在最小工具邊界內 | 人,而且在對的時機被提醒 |

今天做 **C**。完成版在 `agents/`:

- `agents/jira-clerk.agent.md`:只做開單、tools 只有 `runCommands` + 讀檔、不給 edit、`disable-model-invocation: true`(不讓別的 agent 把它當 subagent)。
- `agents/meeting-ops.agent.md`:新增第二個 handoff。

操作:

1. 確認 `action-item-to-jira/SKILL.md` 的 `disable-model-invocation: true`(第三輪加的)在。
2. 建 `.github/agents/jira-clerk.agent.md`(對照完成版自己寫;tools 用工具選單勾)。
3. 改 `.github/agents/meeting-ops.agent.md`:加第二個 handoff;body 的排除語句照留;確認 tools 沒有 `runCommands`、`agents:` 只有 `wbs-builder`(jira-clerk 不在裡面)。
4. 踩線:`@meeting-ops`「幫我把這些 Action Item 整理好,順便開成 Jira 工單」→ 整理照做、開單明講交還、**出現「建立 Jira 工單」按鈕**;它沒有終端機(05b),也不該把開單包成任務丟給 wbs-builder。
5. 按下去 → `@jira-clerk` 先列「將建立 / 已存在略過 / 無法對照 owner」三個清單 → 你說「確認」→ `curl.exe http://127.0.0.1:9000/debug/issues` 驗證。
6. 對照組:同一句丟預設 Agent Mode——硬鎖仍在所以不會自動開單,但沒有按鈕、沒有排除語句。

## 決策點 ③(填進 M9 決策表)
寫入型 Skill 上線前誰要看過?不用 / PR review 順便看 / 指定 Owner + 狀態欄(附錄 A)。

## 完成檢核

- [ ] 撞 A/B 都親眼看過(重複票、姓名 assignee 都出現在 `debug/issues` 裡)
- [ ] 撞 C 測過語意觸發(能說出「為什麼寫入型不能賭這個機率」)
- [ ] 硬化後五項驗收全過;version 已升 0.2.0
- [ ] `@meeting-ops` 踩線測試:整理照做、開單明講交還、出現按鈕;`@jira-clerk` 先列清單再等確認
- [ ] 能對「會議助手能不能開單」說出 A/B/C 各自的代價
