# M7 · Lab 7A / 7B:WBS Generator + Tech Grounding Checker

這個 Lab 一次帶兩個 Skill,刻意選了兩種**失敗方式完全不同**的任務:7A 的風險是「範圍失控」,7B 的風險是「依據造假」。兩支 Skill 合起來才是一件完整的事——

> 一份可交付的 WBS,每一列**往回**要指得到需求,**往前**要指得到依據。
> 7A 做了往回,7B 補上往前。

## 目標

1. 動手寫(或對照完成版理解)`wbs-generator`:今天第一個真正**產出檔案**的 Skill,靠 Agent mode 內建的檔案編輯 + 終端機執行完成,重點在**每個工作包都要能對應輸入依據,格式要用固定範本釘死**。
2. 動手寫(或對照完成版理解)`tech-grounding-checker`:今天第一個接上外部工具(MCP)的 Skill,重點在**每一條依據都要能點開驗證,查不到就誠實說查不到**。

> 📌 **為什麼 Search 沒有自己的 SKILL.md**:對逐字稿做關鍵字搜尋,不需要外部工具、輸出格式 LLM 零樣本就做得對、「沒有就誠實說沒有」也不是這個任務特有的規則——這三點都不成立時,不值得包成一個獨立 Skill,直接讓 Agent/Prompt 處理就好。Portal 上的 Search 面板本身還在,只是不用一份 SKILL.md 去管它。詳細說明見講義 M7 開場。

## 事前準備

完成版 SKILL.md 放在 `skills/` 底下,**這個路徑不會生效**,是給你對照用的。你要自己建立的是 `.github/skills/<skill-name>/SKILL.md`——那裡現在是空的,這是刻意的:如果完成版直接躺在生效路徑上,B1 就變成覆蓋別人的檔案,M8 的誤觸發測試也會失去意義(大家跑的都是同一份完成版)。

---

## Lab 7A:WBS Generator

這個練習延續 Lab 6 的逐字稿——會議決議「下週開始進行 PoC」,David/Mary/George 各自有一筆待辦事項,今天把這個 PoC 階段拆解成一份 Excel WBS。

1. 建立 `.github/skills/wbs-generator/SKILL.md`,對照 `skills/wbs-generator/SKILL.md` 完成版,自己動手寫一版(至少 description 跟 ③ 步驟自己重新表達)。
2. 用 Agent mode,把 `sample-transcript.txt` 內容(或 Lab 6 產出的 Action Items)提供給 Copilot,下指令:「幫我把這場會議決議的 PoC 階段拆成一份 WBS,輸出成 Excel」。
3. 觀察 Copilot 是否會先寫一段 Python 腳本(用 openpyxl),再呼叫終端機執行——**每個終端機指令執行前都需要你按 Run 核准**,注意這一步不會自動跳過。
4. 打開產出的 `.xlsx`,檢查:左側是否有大綱群組(`+`/`-` 摺疊按鈕)、標題列是否有篩選按鈕、捲動時標題列是否保持凍結。
5. 刻意檢查一件事:逐字稿裡有一句「這個 PoC 之後如果驗證順利,中期評估要不要跟 SAP 系統整合……這個目前先不排進 PoC 範圍」——確認產出的 WBS **沒有**把 SAP 整合列成工作項,這是測試「① 不適用範圍」有沒有生效的關鍵。
6. 對照 ⑤ 品質自檢逐項打勾。

> 📌 產出的 Excel 備註欄會看到「民國115年7月10日」這種日期格式——那不是 Skill 寫的,是 `AGENTS.md` 裡的規範在生效。這正好示範了 SKILL.md 與 AGENTS.md 的分工:任務怎麼做歸 SKILL.md 管,跨任務的共通規範歸 AGENTS.md 管。

**7A 的產出就是 7B 的輸入,請留著不要刪。**

---

## Lab 7B:Tech Grounding Checker

### 故事線

David 在 7A 交出了 WBS。現在 George 要拿它去跟資安、採購過,最後上長官會議。

問題是——表上寫著「規劃 Azure OpenAI 資源配置」「確認資料落地地區設定」,這些是**會議室裡憑印象講出來的**,還是真的查過官方文件?長官會議上只要有人問一句「資料落地,Azure OpenAI 在台灣到底有沒有?」而現場答不出來,PoC 就要延一週。

所以 7B 做的事是:**把這份 WBS 從「我們開會決定的」升級成「有官方依據的」**。逐項去 Microsoft Learn 查官方文件、去 GitHub 找有沒有人真的這樣做過;查得到的附上可點的連結,查不到的老實標查無依據,本來就不該有文件的標不適用。

### B0. 設定兩個唯讀 MCP

在專案根目錄建立 `.vscode/mcp.json`,內容見本資料夾的同名檔案(已經寫好,對照著看一遍再用):

```jsonc
{
  "servers": {
    "microsoft-learn": {
      "type": "http",
      "url": "https://learn.microsoft.com/api/mcp"
    },
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/readonly"
    }
  }
}
```

1. 存檔後,`microsoft-learn` 立刻可用——**免登入、免 OAuth**。
2. `github` 第一次呼叫會跳瀏覽器 OAuth,同意授權後即可使用。
3. Copilot Chat 輸入 `/mcp` 或查看 MCP 工具清單,確認兩個 server 的工具都出現。

> ⚠️ **注意 github 那一條結尾的 `/readonly`。** 少了它,這個 Agent 就有能力幫你開 issue、改 branch protection、關 PR。同一個 server,端點差一個後綴,治理上天差地別——這是企業導入 MCP 時通常要做的第一個決策。`/readonly` 可以接在任何 toolset 端點後面(例如 `/mcp/x/issues/readonly`),也可以改用 `X-MCP-Readonly: true` 這個 header。

> ⚠️ 企業租戶的 Copilot policy 可能擋掉 GitHub MCP。**被擋不影響你做完 Lab 7B**——只用 `microsoft-learn` 一樣走得完,差別只在「實作佐證」那一欄會是空的,而 Skill 的 ② 已經要求這種情況要在輸出結尾註明。這正是這個 Lab 想示範的 graceful degradation:少一個來源就少一欄,誠實講出來,而不是拿別的東西填上去。

#### 🛠️ OAuth 卡住時的排障

授權流程失敗或想換帳號重來時:

1. 按 `Ctrl+Shift+P` 開啟 **Command Palette**
2. 輸入並執行:`Authentication: Remove Dynamic Authentication Providers`
3. 重新執行 MCP 工具、重新走一次 OAuth

### B1. 建立 Skill

建立 `.github/skills/tech-grounding-checker/SKILL.md`,對照 `skills/tech-grounding-checker/SKILL.md` 完成版,自己動手寫一版。

description 記得寫成對比句:不是逐字稿摘要(那是 `meeting-summary`),也不是專案範圍分解(那是 `wbs-generator`)——**這個 Skill 的輸入本身就已經是拆好的項目,它只負責補依據**。這兩句對比句等一下 M8 會被實際拿來考驗,現在寫得越含糊,等一下誤觸發越精彩。

### B2. 觸發 Skill

**這一步要手動把 Excel 附進 context,Copilot 不會自己去找檔案。**

在 Copilot Chat 輸入框打 `#file`,選擇 7A 產出的 `AI-Meeting-Intelligence-Portal-PoC-WBS-*.xlsx`(或把檔案從總管直接拖進聊天視窗),然後下指令:

> 幫我逐項查證這份 WBS 的技術依據

7A 沒跑成功、或檔案不見了的人,用 `sample/AI-Meeting-Intelligence-Portal-PoC-WBS-2026-07-08.xlsx` 這份備援檔案,內容一樣。

觀察三件事:

- Copilot 有沒有先寫一段 Python(openpyxl)把 Excel 讀出來——**又是一次終端機 Run 核准**,但這次是讀檔不是寫檔。
- 它先呼叫哪一個 MCP?對同一個項目呼叫了幾次?
- 它有沒有**先分類**(技術項 / 不適用)再開始查,還是每一項都硬查一輪。

### B3. 驗證來源——請真的去點

隨機點兩條 Learn 連結、一條 GitHub 連結。不是確認「開得起來」就好,要確認:

**這篇文章講的,是不是這個工作包的那一件事?**

連結能開、內容也沒錯,但講的是別的服務——這是這個 Lab 最想讓你抓到的錯誤。它通過了所有表面檢查。

### B4. 邊界測試:看它怎麼處理 1.2 和 4.1

7A 產出的 WBS 裡,有兩項 Microsoft Learn 不可能有文件:

| WBS | 項目 | 為什麼查不到 |
|---|---|---|
| 1.2 | 規劃與現有 Portal 前端的串接方式 | 客戶自家系統,官方文件不可能涵蓋別人家的架構 |
| 4.1 | 在資安確認通過後開啟 PoC 環境 | 這是專案管理流程,不是技術設定 |

正確答案是**「—— 不適用」**,不是「查無依據」,更不是掛一篇相近的文件上去。

Agent 最想做的事是**把表格每一格都填滿**。所以面對 1.2,它八成不會說查不到,而是去搜「前端整合」然後掛一篇 Azure App Service 或 Static Web Apps 的文件——那個連結是真的、點得開、內容也沒錯,只是跟這個工作包毫無關係。

**加碼**(時間夠再做):在 WBS 手動加一列「設定 Azure OpenAI 的文件層級存取權限(document-level ACL)」。document-level ACL 是 Azure AI Search 的功能,不是 Azure OpenAI 的。看它會不會把一篇**真的** AI Search 文件掛到 Azure OpenAI 的項目上。

---

## 完成檢核

- [ ] WBS 的 Excel 檔案有大綱群組、篩選按鈕、凍結窗格,且沒有把逐字稿裡明確排除的項目(SAP 整合)列進去
- [ ] `/mcp` 看得到 `microsoft-learn` 與 `github` 兩個 server 的工具清單,而且 github 走的是 `/readonly` 端點
- [ ] `/skills` 或 Copilot 能偵測到 `tech-grounding-checker`,description 有清楚的對比句
- [ ] 對照表裡每一個連結都點得開,**而且講的是該項目本身的那個服務**
- [ ] 1.2 與 4.1 標的是「不適用」,不是「查無依據」,也沒有被掛上相近主題的文件
- [ ] 表格下方有三類統計,數字加總等於項目總數
- [ ] 原始 WBS Excel 沒有被修改

> 📌 **做完這個 Lab,你的 `.github/skills/` 裡有三個 Skill 了**——接下來進 `../m08-mistrigger-test/`(M8),實測它們互相干擾時會發生什麼事。B1 那兩句對比句寫得越含糊,等一下誤觸發越精彩。
