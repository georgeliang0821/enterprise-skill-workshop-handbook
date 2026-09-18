# 我的決策表(離場前填完)

團隊:＿＿＿＿　填表人:＿＿＿＿　日期:＿＿＿＿

> 每一題都沒有 workshop 的標準答案,只有你們 repo 的答案。**理由欄要能指出今天哪一次事故讓你這樣選**;填不出來的寫「回去問誰」。

| # | 決策點 | 選項 | 我們團隊的選擇 | 理由 / 對應的事故 |
|---|---|---|---|---|
| ① | API 是 spec-first 還是 code-first?(M4) | 包工具 Skill / code-first / 純手刻 | | |
| ② | 會議助手能不能開單?(M5) | A 放進路由 / B 完全排除 / C handoff 按鈕 | | |
| ③ | 寫入型 Skill 上線前誰看過?(M5) | 不用 / PR review / Owner + 狀態欄 | | |
| ④ | 哪類工作放哪個執行面?(M6') | VS Code / CLI / 雲端 agent | | |
| ⑤ | 第一個派給雲端 agent 的任務?(M7') | — | | |
| ⑥ | 第一組資產怎麼分享?(M8') | commit 進 repo / gh skill / Enterprise Plugins | | |
| ⑦ | 日常用 Auto 還是鎖模型?團隊資產鎖不鎖?(M2a) | Auto / 鎖 / 資產用 `model:` 鎖 | | |

## 回去第一個 Skill 的 description 草稿(Transfer 練習)

- 痛點(重複發生、做法已成熟):
- description(做什麼 / 何時用 / 不是什麼 / 關鍵詞):
- 跟今天哪個 Skill 最容易混淆?什麼指令會選錯?
- 唯讀 or 寫入型?寫入型 → `disable-model-invocation: true` + 決策點 ③ 的選擇
