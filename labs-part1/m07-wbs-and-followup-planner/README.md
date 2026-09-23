# M7 · Lab 7A / 7B:WBS Generator + Weekly Follow-up Planner

這個 Lab 一次帶兩個 Skill,刻意選了兩種**技術路徑完全不同**的任務,對照出「code execution 產出檔案」跟「MCP 多來源工具整合」在品質規則設計上的差異。

## 目標

1. 動手寫(或對照完成版理解)`wbs-generator`:今天第一個真正**產出檔案**(而不是聊天視窗文字)的 Skill,靠 Agent mode 內建的檔案編輯 + 終端機執行完成,重點在**每個工作包都要能對應輸入依據,格式要用固定範本釘死**。
2. 動手寫(或對照完成版理解)`weekly-followup-planner`:今天第一個接上外部工具(MCP)的 Skill,重點在**每一條內容都要能標明來源**。

> 📌 **為什麼 Search 沒有自己的 SKILL.md**:對逐字稿做關鍵字搜尋,不需要外部工具、輸出格式 LLM 零樣本就做得對、「沒有就誠實說沒有」也不是這個任務特有的規則——這三點都不成立時,不值得包成一個獨立 Skill,直接讓 Agent/Prompt 處理就好。Portal 上的 Search 面板本身還在,只是不用一份 SKILL.md 去管它。詳細說明見講義 M7 開場。

## 操作步驟

### Lab 7A:WBS Generator

這個練習延續 Lab 6 的逐字稿——會議決議「下週開始進行 PoC」,David/Mary/George 各自有一筆待辦事項,今天把這個 PoC 階段拆解成一份 Excel WBS。

1. 建立 `.github/skills/wbs-generator/SKILL.md`,對照 `skills/wbs-generator/SKILL.md` 完成版,自己動手寫一版(至少 description 跟 ③ 步驟自己重新表達)。
2. 用 Agent mode,把 `sample-transcript.txt` 內容(或 Lab 6 產出的 Action Items)提供給 Copilot,下指令:「幫我把這場會議決議的 PoC 階段拆成一份 WBS,輸出成 Excel」。
3. 觀察 Copilot 是否會先寫一段 Python 腳本(用 openpyxl),再呼叫終端機執行——**每個終端機指令執行前都需要你按 Run 核准**,注意這一步不會自動跳過。
4. 打開產出的 `.xlsx`,檢查:左側是否有大綱群組(`+`/`-` 摺疊按鈕)、標題列是否有篩選按鈕、捲動時標題列是否保持凍結。
5. 刻意檢查一件事:逐字稿裡有一句「這個 PoC 之後如果驗證順利,中期評估要不要跟 SAP 系統整合……這個目前先不排進 PoC 範圍」——確認產出的 WBS **沒有**把 SAP 整合列成工作項,這是測試「① 不適用範圍」有沒有生效的關鍵。
6. 對照 ⑤ 品質自檢逐項打勾。

### Lab 7B:Weekly Follow-up Planner

這個 Skill 會用到 MCP。故事線是:**「幫我看本週行事曆哪些時段有空,並把還沒結案的 Action Item 列出來,我想挑個空檔把它們清一清。」** 空檔來自行事曆(CalendarTools),未結事項來自內部 Action Item 記錄——兩個來源各自獨立、不需互相對齊,所以有沒有 Agent365 權限,未結事項那端的練習完全一樣,差別只在空檔是「真查行事曆」還是「用替代資料/假設」。

先完成下面 B0 的其中一條路,三條路都不影響後面 B1-B4 的 Skill 撰寫練習。

#### B0. MCP 路徑選擇(三選一,都不影響 B1 之後的練習)

> 📌 **誠實面對 MCP 的可用性問題**:CalendarTools 是 Agent365 底下的功能,不是每個租戶都已開通。若只是「沒權限就用 fallback 資料」,走 fallback 的人整場沒摸到真的 MCP(mcp.json、OAuth、工具清單)。所以三條路擇一,**至少確保每個人都完成過一次真實的 MCP 設定**;行事曆資料有沒有真的,不影響 B1 之後的練習。

| 路徑 | 條件 | 行事曆資料來源 |
|---|---|---|
| 一 · CalendarTools | 有 M365 Copilot 授權、租戶已開通 Agent365 | 真行事曆 |
| 二 · GitHub remote MCP | 有 GitHub 帳號 | `data/sample-calendar-week.json`(fallback) |
| 三 · Microsoft Learn MCP | 連 GitHub 都不方便用(免登入、免 OAuth) | `data/sample-calendar-week.json`(fallback) |

##### 路徑一:租戶已開通 Agent365 → 設定 CalendarTools,走真行事曆

1. 先查好租戶 ID(用公司網域即可換到,不需登入或任何權限):

   ```powershell
   # PowerShell
   (Invoke-RestMethod "https://login.microsoftonline.com/<你的公司網域>/v2.0/.well-known/openid-configuration").issuer

   # 或 curl.exe
   curl.exe -s "https://login.microsoftonline.com/<你的公司網域>/v2.0/.well-known/openid-configuration"
   ```

   回傳的 `issuer` 格式為 `https://login.microsoftonline.com/<tenant_id>/v2.0`,中間那段 GUID 就是 `tenant_id`。
2. 在專案根目錄建立(或編輯)`.vscode/mcp.json`,內容參考 `mcp/mcp-config-example.jsonc`;VS Code 提示時貼上 tenant_id。
3. 第一次呼叫會跳瀏覽器 OAuth,同意授權後即可使用。
4. Copilot Chat 輸入 `/mcp` 或查看 MCP 工具清單,確認看得到 CalendarTools 的工具。

##### 路徑二:沒開通 Agent365,但有 GitHub 帳號 → 設定 GitHub remote MCP server

體驗跟路徑一完全同構(mcp.json → OAuth → `/mcp` 看工具清單)。設定內容見 `mcp/mcp-config-github-example.jsonc`,或直接在 `.vscode/mcp.json` 加入:

```jsonc
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}
```

設定完成後隨口試一句「用 GitHub MCP 幫我列出我最近的 repo」,確認工具真的被呼叫——**這 5 分鐘的目的只是讓「MCP 設定」在你手上真實發生過一次**。行事曆資料走 fallback(見下方)。

> ⚠️ 企業租戶的 Copilot policy 可能擋掉這個 server;被擋就走路徑三。

##### 路徑三:連 GitHub 帳號都不方便用 → 設定 Microsoft Learn MCP server

完全免登入、免 OAuth,是門檻最低的真 MCP。在 `.vscode/mcp.json` 加入:

```jsonc
{
  "servers": {
    "microsoft-learn": {
      "type": "http",
      "url": "https://learn.microsoft.com/api/mcp"
    }
  }
}
```

設定完成後試一句「用 Microsoft Learn MCP 查一下 Azure Container Apps 的 ingress 怎麼設定」,確認 `/mcp` 看得到工具、工具真的被呼叫。行事曆資料同樣走 fallback。

##### Fallback 行事曆資料(路徑二 / 三共用)

兩種做法擇一:

- **給替代資料**:把 `data/sample-calendar-week.json` 提供給 Copilot,下指令時加一句「這是 CalendarTools 查到的本週行事曆」,讓它當作 MCP 查詢結果算空檔。這份資料刻意把週三排滿一整天,方便 B4 的邊界測試。
- **直接假設**:告訴 Copilot「假設我本週下午都有空」,把這句當作行事曆來源。

不管走哪條路,② 未結 Action Item 那一端跟有 MCP 的人完全一樣,練習重點——整合多來源、各自標明來源——完全不受影響。

##### 🛠️ OAuth 卡住時的排障(路徑一 / 二共用)

授權流程失敗或想換帳號重來時:

1. 按 `Ctrl+Shift+P` 開啟 **Command Palette**
2. 輸入並執行:`Authentication: Remove Dynamic Authentication Providers`
3. 重新執行 MCP 工具、重新走一次 OAuth

#### B1. 建立 Skill

建立 `.github/skills/weekly-followup-planner/SKILL.md`,對照 `skills/weekly-followup-planner/SKILL.md` 完成版,自己動手寫一版。description 記得寫成對比句:不是逐字稿摘要(那是 meeting-summary),也不是專案範圍分解(那是 wbs-generator)。

#### B2. 觸發 Skill

把 `data/past-action-items.json` 提供給 Copilot(當作內部 Action Item 記錄的資料來源),再視你 B0 走的路:

- **有 MCP**:直接下指令「幫我看本週哪些時段有空,並把還沒結案的 Action Item 列出來,我想挑空檔跟進」,觀察 Agent 有沒有先呼叫 CalendarTools 查你的真實行事曆。
- **走 Fallback**:把 `data/sample-calendar-week.json` 一起提供(或改說「假設我本週下午都有空」),下指令「這是 CalendarTools 查到的本週行事曆,幫我看哪些時段有空,並把未結的 Action Item 列出來排進去跟進」。

#### B3. 檢查來源標註

檢查輸出的「待跟進的未結事項」是不是列出了 `data/past-action-items.json` 裡**所有** `status: "open"` 的項目、每一筆都標了來源 id,而且**沒有**把已經 `done` 的 `AI-2026-06-20-01` 也列進去。再看「可用空檔」有沒有標明來源是 calendar,而不是憑空生出的時段。

#### B4. 刻意測試一次「本週排滿、沒有空檔」的情境

用 `data/sample-calendar-week.json` 走一次,問「週三幫我排時間跟進」——週三被刻意排滿一整天,確認 Copilot 有誠實回報「週三無可用空檔」而不是硬生一個時段——這是檢視品質規則有沒有生效的關鍵測試。這裡的幻覺風險比 Lab 7A 更隱蔽:錯誤可能藏在 MCP 查詢、內部資料查詢,或 LLM 整合多來源時自己腦補,任何一個環節沒把關,都會排出一個根本不存在的空檔。

## 完成檢核

- [ ] WBS 的 Excel 檔案有大綱群組、篩選按鈕、凍結窗格,且沒有把逐字稿裡明確排除的項目(SAP 整合)列進去
- [ ] `/skills` 或 Copilot 能偵測到 `weekly-followup-planner`,description 有清楚的對比句(不是摘要、不是任務分解)
- [ ] weekly-followup-planner 能正確帶出 CalendarTools(或 fallback 資料)算出的本週空檔
- [ ] 「待跟進的未結事項」列出所有 `status: open` 的項目、每筆標來源 id,`done` 的項目沒有被誤列
- [ ] 每一條輸出都能回頭指出來源(calendar 或 Action Item 記錄 id)
- [ ] 本週排滿的情境有誠實回報「無可用空檔」,沒有硬生時段

> 📌 **做完這個 Lab,你的 `.github/skills/` 裡有三個 Skill 了**——接下來進 `../m08-mistrigger-test/`(M8),實測它們互相干擾時會發生什麼事。B1 那兩句對比句寫得越含糊,等一下誤觸發越精彩。
