# M11 · Lab 11:寫入型 Skill —— 先翻車,再把護欄蓋到 Skill 自己身上(Action Item → Jira)

這個 Lab 不需要真實 Jira 帳號。`mock_jira_server.py` 模擬 Jira 的查詢/建票 API——**它是假的,正因為是假的,才是踩「寫入事故」的完美沙箱**:重複建票,在這裡零成本,在真 Jira 上是團隊工作流程的實際混亂,而且不一定會被立刻發現。

> **定位**:M9、M10 蓋的牆都在 agent 身上(tools 白名單、subagent、handoff)。這個 Lab 把牆再往下蓋一層,蓋到 Skill 自己身上——「**用 → 踩 → 修**」跟上半場的翻車實驗同構,但這次踩的是全天副作用最大的一種。你會先用一個「刻意天真版」Skill 連踩兩次,再自己把它防呆,最後對照完成版。

## 素材

| 檔案 | 用途 |
|---|---|
| `mock_jira_server.py` | 假 Jira(查詢 / 建票 / `debug/issues` / `debug/reset`) |
| `skills/action-item-to-jira/SKILL-naive.md` | **翻車用的刻意天真版(v0.1.0-naive)**——第一輪直接用它 |
| `skills/action-item-to-jira/SKILL.md` | 防呆完成版——**第三輪做完前不要偷看** |
| `action-items-sample.md` | 結構化待辦清單(模擬上半場產出) |

## 第零步:啟動 Mock Jira Server

套件已由共用 venv 裝好,**不需要 `pip install`**。在本資料夾開一個終端機(VS Code 外的 PowerShell 也可以),確認提示字元有 `(.venv)`,然後:

```powershell
python -m uvicorn mock_jira_server:app --reload --port 9000
```

開 `http://127.0.0.1:9000/docs` 確認 Swagger UI 正常。

> Mock Jira 不驗 token,所以今天沒有認證這一步。真實 Jira 要 token 時,放使用者層級環境變數或 secret store,**不要寫進 SKILL.md**——M13 / M14 會把整個 `.github/` 推上 GitHub。

## 第一輪:用(naive 版跑起來,看似正常)

1. 把 `SKILL-naive.md` 的內容複製到你的專案 `.github/skills/action-item-to-jira/SKILL.md`。
2. 用 Agent mode 提供 `action-items-sample.md`、專案代碼 `MIP`、Mock Server 位置 `http://127.0.0.1:9000`,下指令:「幫我把這些待辦事項同步到 Jira,專案代碼是 MIP」。
3. 驗證:`curl.exe http://127.0.0.1:9000/debug/issues` ——三筆票建立成功,票號正確回報。**看起來一切正常,這正是天真版最危險的地方:它能動。**

## 第二輪:踩(連踩兩次)

### 踩 A:重複建票

對**同一份** `action-items-sample.md` 再觸發一次,然後:

```powershell
curl.exe http://127.0.0.1:9000/debug/issues
```

六筆票,三筆是重複的。真 Jira 上,這代表 David 的 dashboard 上同一個任務出現兩次,團隊開始搞不清楚哪張才是真的。

### 踩 B:語意誤觸發

開新對話,附上待辦清單,**只隨口說一句**:「這些待辦事項要記得追蹤」——不明確要求建票。觀察 Copilot 會不會因為 naive 版的 `disable-model-invocation: false` + description 裡的「追蹤」關鍵詞,**自己跑去建票**。

> 這是你第一次親眼看到「語意誤觸發」——上半場 M6 講過 selection 是機率性語意匹配,現在看到它的另一面:**觸發是機率性的**,這次沒觸發不代表下次不會。對唯讀 Skill 你可以賭這個機率,對會寫入外部系統的 Skill,你敢賭嗎?M9 ⑤ 與 M10 已經給了你這個欄位——`disable-model-invocation: true`;這一踩給你的是非鎖不可的理由:它是架構層防呆,不是選配。

踩完清場,準備防呆:

```powershell
curl.exe -X POST http://127.0.0.1:9000/debug/reset
```

## 第三輪:修(自己防呆)

針對兩個踩點,**用自己的話**修改你的 SKILL.md:

1. **去重**(對踩 A):③ 步驟加上「建票前先呼叫 `GET /rest/api/2/search` 用 summary 關鍵字查詢是否已存在;已存在則略過並註明」。
2. **鎖自動觸發**(對踩 B):frontmatter 改 `disable-model-invocation: true`,version 升為 `0.2.0`(這次變更本身就是 M6 要收割的一筆)。
3. 順手補 ⑤ 品質自檢:去重、每筆都有明確狀態。

然後驗收(三項,都是你自己的防呆成果):

- 重新提供待辦清單,明確打 `/action-item-to-jira` 觸發 → `debug/issues` 三筆票。
- 同一份清單再觸發一次 → 輸出標註「已存在,略過」,沒有重複票。
- 隨口說「這些待辦要記得追蹤」→ **不會**自動觸發,只有明確打 `/action-item-to-jira` 才執行。

最後對照完成版 `SKILL.md`,比較你的寫法差異——特別看它 ① 裡「不要自作主張連建票都做了」。

## 第四輪:決策點——誰有權觸發 Jira 開單?(接上 M10 的 handoff)

> 這一輪是**應用 M10 v3 的 handoff,不是新機制**:按鈕、`send: false`、label 要有英數字元都做過了;新的只有接完之後「三道東西各自擋什麼」那張疊層表(見講義)。

現在 `action-item-to-jira` 已經把去重與自動觸發鎖好。Skill 內部安全了,下一個風險不在 Skill 裡,而在**誰可以啟動這個寫入副作用**。把它接回 M9 的編排型 `@meeting-ops` 時,觸發權要交給模型,還是留在人手上?

比較下面三種整合方式——**它們都合法,差別在誰握有觸發權**:

| 選項 | 做法 | 方便 | 風險 | 誰決定 |
|---|---|---|---|---|
| A 放進路由 | body 加「要開單用 action-item-to-jira」,Skill 不鎖 | 最方便 | 踩 B 看過:隨口一句就可能開單;開單靠終端機打 REST,`@meeting-ops` 若還留著整類 `execute`(沒做 M10),tools 牆完全攔不住 | 模型 |
| B 完全排除 | Skill `disable-model-invocation: true`;body 排除;使用者自己 `/action-item-to-jira` | 最不方便 | 最低 | 人,但沒人提醒 |
| C handoff 按鈕 | Skill 同 B 硬鎖;另建只有 Jira 工具的 `@jira-clerk`;`@meeting-ops` 用 `handoffs:` 給一顆「Create-Jira (建立 Jira 工單)」按鈕,`send: false` | 整理完就看到按鈕 | 低:沒人按不會發生;按了也在最小工具邊界內 | 人,而且在對的時機被提醒 |

今天做 **C**。完成版在 `agents/`:

- `agents/jira-clerk.agent.md`:只做開單、tools 只有 `read` + `runInTerminal`(同 wbs-builder 削到只剩跑指令)、不給 edit、`disable-model-invocation: true`(不讓別的 agent 把它當 subagent)。
- `agents/meeting-ops.agent.md`:在 M10 v3 上新增第二個 handoff「Create-Jira (建立 Jira 工單)」;tools 與第一顆按鈕都跟 M10 v3 一樣。

操作:

1. 確認 `action-item-to-jira/SKILL.md` 的 `disable-model-invocation: true`(第三輪加的)在。
2. 建 `.github/agents/jira-clerk.agent.md`(對照完成版自己寫;tools 用工具選單勾)。
3. 改 `.github/agents/meeting-ops.agent.md`:加第二個 handoff(label 至少要有一個英數字元,純中文會被擋——M10 踩過);body 的排除語句照留;確認 tools 跟 M10 v3 一樣(`read`、`edit`、`agent`、`microsoft-learn/*`,沒有 `execute`)、`agents:` 只有 `wbs-builder`(jira-clerk 不在裡面)。
4. 踩線:`@meeting-ops`「幫我把這些 Action Item 整理好,順便開成 Jira 工單」→ 整理照做、開單明講交還、**出現「Create-Jira」按鈕**;它沒有終端機(M10),也不該把開單包成任務丟給 wbs-builder。
5. 按下去 → `@jira-clerk` 先列「將建立 / 已存在略過」兩個清單 → 你說「確認」→ `curl.exe http://127.0.0.1:9000/debug/issues` 驗證。
6. 對照組:同一句丟預設 Agent Mode——硬鎖仍在所以不會自動開單,但沒有按鈕、沒有排除語句。

## 決策點:寫入型 Skill 上線前誰要看過?
不用 / PR review 順便看 / 指定 Owner + 狀態欄(團隊自己維護一張 Skill 登記表)。第二個選項成本幾乎是零,而它擋掉的是「別人的 Jira 裡多了你沒要的工單」。

## 完成檢核

- [ ] 踩 A 親眼看過(重複票出現在 `debug/issues` 裡)
- [ ] 踩 B 測過語意觸發(能說出「為什麼寫入型不能賭這個機率」)
- [ ] 防呆後三項驗收全過;version 已升 0.2.0
- [ ] `@meeting-ops` 踩線測試:整理照做、開單明講交還、出現按鈕;`@jira-clerk` 先列清單再等確認
- [ ] 能對「誰有權觸發 Jira 開單」說出 A/B/C 各自的觸發者與代價
