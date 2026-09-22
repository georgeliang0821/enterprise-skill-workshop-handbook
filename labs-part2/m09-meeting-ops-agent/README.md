# M9 / M10 · Custom Agent:@meeting-ops(M9)+ Subagent wbs-builder、Handoff → @followup-planner(M10)

三份完成版 `.agent.md`,放到 `.github/agents/`:

| 檔案 | 角色 | 被叫的方式 | tools |
|---|---|---|---|
| `agents/meeting-ops.agent.md` | 編排型 coordinator。薄路由、handoff 按鈕、派 subagent | 使用者 `@meeting-ops` | `edit`、`search`、`CalendarTools/*`(**沒有** runCommands) |
| `agents/wbs-builder.agent.md` | subagent:只做 WBS | 由 @meeting-ops 透過 `agents:` 白名單呼叫(模型決定) | `edit`、`runCommands` |
| `agents/followup-planner.agent.md` | handoff 目標:只排本週跟進 | 使用者按「排進本週跟進」按鈕(人決定);`disable-model-invocation: true` | `search`、`CalendarTools/*` |

## 注意

- `tools` 的名稱**用 VS Code 的工具勾選清單產生**;填錯會被靜默忽略。
- `tools` 沒有 Skill 白名單欄位;`skill:xxx` 會被忽略。
- `model:` 填講師當天指定的模型。
- **Tool set**:`Chat: Configure Tool Sets` 可定義 `meeting-tools` 一次、多個 agent 引用。但 tool set 是使用者層級設定、不進 repo——交付的 `.agent.md` 請展開成明確工具名(本資料夾的完成版就是展開後的)。
- `handoffs` 的 `send: false` 表示按下按鈕後 prompt 只是預填。
- subagent 以 custom agent 執行在部分版本標為 experimental;不支援時 M10 的 subagent 改為講師示範,`@meeting-ops` 保留 `runCommands`。

## 操作順序(對照講義 M9 ⑤、M10)

1. **M9 先撞**:預設 Agent Mode 下複合指令「這是這場會議的逐字稿,幫我把該做的都做一做」,記下它做了哪些事。
2. **M9 建 `@meeting-ops`**(此時 tools 可先含 `runCommands`),同一句再跑,比對。
3. **M10 subagent**:下「整理這場會議,並把 PoC 拆成 WBS」,看 context window 指示器。建 `wbs-builder`;`@meeting-ops` 加 `agents: [wbs-builder]`、tools 拿掉 `runCommands`、body 的 WBS 路由改為「交給 wbs-builder」。再跑同一句:WBS 段落變成 subagent 呼叫、主對話只收摘要、指示器數字下降。邊界:「順便幫我跑 pytest」→ 它沒有終端機,應明講做不到、不繞去叫 wbs-builder。
4. **M10 handoff**:建 `@followup-planner`,`@meeting-ops` 加 handoff,刪掉 body 裡「先整理再交給 weekly-followup-planner」的自動路由。整理完 → 按鈕 → 切到 `@followup-planner`,prompt 預填未送出。
5. 邊界:「順便幫我把這些 Action Item 開成 Jira 票」→ 明講超出範圍、交還。M11 會給這件事一顆按鈕。
