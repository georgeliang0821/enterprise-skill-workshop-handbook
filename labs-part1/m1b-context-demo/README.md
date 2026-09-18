# M1b · Context Engineering:先看兩個症狀,再拿手術刀(講師 demo 腳本 + 速查)

## 講師 demo 腳本(約 5 分)

**準備**:Portal 專案(`lab1-portal-scaffold/` 完成版)開在 VS Code;確認裡面有一個做日期換算的工具函式(例如 `src/utils/date.js`),以及至少一個跟日期無關的元件檔。

### 症狀一:agent 找錯檔案
1. 開著一個跟日期無關的檔案(例如 `App.jsx`)。Agent 模式問:「這個專案哪裡在做日期換算?」
2. 不看答案,展開回應底下的 **references**。預期:讀了兩三個不相干的元件、漏掉真正的工具函式,或只看了開著的檔案就回答。
3. 指向 chat 輸入框上方:開著的檔案只以「建議附件」chip 出現,沒點就沒進這次請求;搜到什麼是它在迴圈中自行決定的。
4. 一句話:「它拿到的請求裡沒有任何東西告訴它去哪裡找,所以它猜。」

### 症狀二:credit 燒得比想像快
1. 新開 session。什麼都不附,hover chat 輸入框的 **context window 使用量指示器**,念出 token 總數。
2. 把整個 `src/` 拖進 chat,再 hover——念出跳到多少、referenced files 佔多少。
3. 清掉,只 `#file` 那個工具函式——再念一次。
4. 一句話:「這個差距就是『讓它自己探索』和『告訴它看哪裡』每一次請求的成本差。」

### 收尾
「兩個症狀同一個根因:模型只能對這次請求裡有的東西推理。找錯檔案是缺了該有的;credit 燒太快是塞了不該有的。解法不在換個說法再問,而在控制組裝。」→ 進七層表。

## 七層組裝(依 VS Code 官方文件)

System instructions → Customizations(instructions / skills / agents)→ User message → Conversation history(接近上限自動 compact)→ Implicit context(Agent 模式下 active file 只是建議附件)→ Explicit references(`#`)→ Tool outputs(agent 自行決定搜不搜、讀幾個)。

症狀一出在第 5、7 層;症狀二出在第 2、4、7 層;手術刀是第 6 層。

## 兩個先更正的誤解

- **點開檔案 ≠ 這次 session 的參考資料。** Agent 模式下 active file 只是建議附件;附件是 per-request,只透過 history 留存,compact 後可能被摘要掉。
- **不加 `#codebase` ≠ 預設整個 codebase。** 語意索引幫 agent 定位片段,不會把整個 workspace 放進每一次請求。

## 手術刀:四個問題對回症狀

| 問題 | 機制差別 | 對哪個症狀 | 什麼時候用 |
|---|---|---|---|
| 點開檔案 vs `#file` | 隱性(Agent 模式不帶內容、只有 active 那一個、切 tab 就變) vs 顯性(完整內容、可多個、不必開著、釘在該次請求、context chips 看得到) | 一 | 多個非前景檔案;要確保一定被納入;寫進 Prompt File |
| `#file` vs `#codebase` | 相反方向:`#file` = 知道在哪、釘住、省掉搜尋;`#codebase` = 不知道在哪、強制一次 workspace 語意搜尋 | `#file` → 二;`#codebase` → 一 | `#codebase`:Ask 模式;Agent 只憑當前檔案就回答;探索型問題 |
| `#terminalLastCommand` | agent 自己跑的指令它看得到;**你手動跑的**它看不到 | 一 | 手動 build / test / az / terraform 噴錯時;只要一段用 `#terminalSelection`;需 shell integration |
| `#fetch` vs 貼 URL | 貼 URL 是「希望模型決定呼叫 fetch」;`#fetch` 宣告意圖並把工具帶進請求;`web` 工具集被關閉時貼 URL 不會抓、也不會告訴你 | 一 | 不帶 URL 的用法;Ask / inline chat;要確保真的抓。會先要求確認外部 URL,且短時間快取 |

對症狀二的另外兩刀:`/compact`、換任務就新開 session。

## 怎麼證明它看到了什麼

context chips(你加了什麼;建議附件有沒有點進去)→ references(它讀了什麼)→ context window 指示器(這次請求多大、哪類佔最多)。之後每個 Lab 的檢核都會用 references。

## 命名更新(功能未取消)

| 舊 | 現行 |
|---|---|
| `#codebase` | `#search/codebase` |
| `#usages` | `#search/usages` |
| `#terminalLastCommand` / `#terminalSelection` | `#read/terminalLastCommand` / `#read/terminalSelection` |
| `#problems` | `#read/problems` |
| `#testFailure` | `#execute/testFailure` |
| `#fetch` | `#web/fetch` |
| `#extensions` / `#runCommand` | `#vscode/extensions` / `#vscode/runCommand` |
| `@workspace` → `#workspace` | 已移除,由 `#codebase` 取代;內建參與者剩 `@github` `@terminal` `@vscode` |
| `#file` | 不變(不是工具,是 `#<file|folder|symbol>` 直接引用) |

短寫法仍以別名出現;輸入 `#` 時以選單顯示為準。
