# M4 · Lab 4:AGENTS.md 與 Prompt File

兩個檔案,兩種「何時被讀」:

| 檔案 | 何時被讀 | 所以 |
|---|---|---|
| `AGENTS.md`(repo 根目錄) | 每一次請求;VS Code、Copilot CLI、雲端 coding agent 都讀 | 由 `/init` 起稿 → 精簡 → 補團隊意志 |
| `.github/prompts/meeting-quickcheck.prompt.md`(`${input:…}`) | 你打 `/meeting-quickcheck` 時 | 可以帶參數;不會被自動觸發 |

> 第三種「碰到符合檔案才注入」的 Custom Instructions(`applyTo`)留到下半場 M12 產 FastAPI 骨架時再建,完成版在 `labs-part2/m12-openapi-fastapi-scaffold/instructions/`。

## 步驟

> 注意:`labs-part1/AGENTS.md`(素材資料夾根目錄那份)只是告訴 Agent「跟 Python 相關的事情要走共用 venv」的環境註記,不是本 Lab 的教材。本 Lab 要你寫的是**你自己 Portal 專案 repo 根目錄**的 `AGENTS.md`;完成版對照範本在本資料夾內。

### A · AGENTS.md:/init 產草稿,再由你決定留什麼
1. **A1 產草稿**:在 Portal 專案的 chat 輸入 `/init`。展開 references 看它讀了哪些檔案。完成後 repo 根目錄出現 `AGENTS.md`。若它順帶建議產生 skills / custom agents,**今天只保留 AGENTS.md**。
2. **A2 精簡**:逐段問「這一段是不是每一次請求都需要?」不是的就刪或改成一行連結。這份檔案每次請求都會送出去。
3. **A3 補團隊意志**:`/init` 抓得到客觀事實(build / test / 框架),抓不到團隊規則。加上完成版末段那五條。注意只放「風格與紅線」——「什麼算決議」是判斷邏輯,不屬於這裡。
4. **A4 檢核**:隨便問一句,references 裡要看到 `AGENTS.md`。

> **AGENTS.md vs `.github/copilot-instructions.md`**:兩者都是 always-on,VS Code 兩個都注入,同時存在就是重複付費。本課用 AGENTS.md(跨工具,CLI 與雲端 agent 原生讀取);既有 repo 若已有 copilot-instructions.md,沿用即可。`alternatives/copilot-instructions.md` 是等價內容,供對照。

### B · Prompt File
建立 `.github/prompts/meeting-quickcheck.prompt.md`。拖入逐字稿,輸入 `/meeting-quickcheck`,填會議日期,送出。

## 完成檢核

- [ ] 任意 chat 的 references 都有 `AGENTS.md`;你能指出草稿裡被刪掉的至少一段並說出原因
- [ ] `/meeting-quickcheck` 出現在 `/` 選單、會跳輸入框、輸出只有「決議」「未訂期限的承諾」兩個小標題
- [ ] 你說得出:為什麼「什麼算決議」不該寫進 AGENTS.md

完成版:`AGENTS.md`、`.github/prompts/…`;先自己做再對照。
