---
name: hello-test
description: 一個最小可安裝的測試 Skill,用來體驗 gh skill preview / install / list 的分發流程。被明確叫用時,回覆一段固定的問候並說明自己是分發測試用。
user-invocable: true
version: 0.1.0
---

## ① 適用範圍
- 適用:課堂上驗證 `gh skill install` 分發流程是否成功。
- 不適用:任何真實工作場景——這只是分發測試樣本。

## ③ 步驟
1. 回覆:「hello from hello-test skill —— 分發流程正常。」
2. 說明目前是用哪個 scope 安裝的(project / user),提醒使用者用 `gh skill list` 查 path。

## ⑤ 品質自檢
- [ ] 只在被明確叫用時回覆,不做任何寫入或外部呼叫。
- [ ] 不讀取、不執行任何外部內容。

> 注意:檔名必須是全大寫 `SKILL.md`。用 PowerShell 建檔時容易變成小寫 `skill.md`,
> 本機看似正常但推上 GitHub 後 `gh skill preview` 會回 `no skills found`。
> 修法:`git mv skills/hello-test/skill.md skills/hello-test/SKILL.md` → commit → push。
