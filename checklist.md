# GitHub Copilot 工作坊：學員環境自我檢查表

> **請在開課前一天完成。** 本清單對應 `Handbook_Part1_v4.06.html` 與 `Handbook_Part2_v4.html`，目的是將帳號、網路、Proxy、套件安裝及權限問題提前排除。
>
> 環境假設：**Windows + VS Code + PowerShell**。命令以 PowerShell 與 `curl.exe` 為主。
>



---

## ① Copilot 與工作區

### 1. 帳號與授權

- [ ] 能以**公司 GitHub 帳號**登入 `https://github.com`。
- [ ] 已被指派有效的 GitHub Copilot seat（Business 或 Enterprise）。
  - 驗證：GitHub 右上頭像 → **Your Copilot**，確認方案為啟用中。
  - 未指派 seat 時，請找公司 GitHub 組織管理員處理。

### 2. VS Code 與基本工具

PowerShell 執行下列命令；每一行都應顯示版本，而非 `not recognized`：

```powershell
code --version
git --version
```

- [ ] VS Code 與 Git 均可使用。

> 工作坊會使用 commit、push 與 PR，因此完整課程必須安裝 Git。

### 3. VS Code 擴充、模型與工作區

- [ ] 已安裝並登入 **GitHub Copilot**，且可開啟 Copilot Chat。
- [ ] 建立或開啟一個本機可寫入的工作資料夾。
- [ ] VS Code 沒有顯示 Restricted Mode；若有，請按 **Trust** 信任此工作區。
- [ ] Chat 模式下拉選單可看到並切換至 **Agent**。
- [ ] Chat 模型選單看得到 **Auto**，以及至少一個可明確指定的模型。

> 工作坊需要 Agent 建立檔案、執行 Python 與啟動本機服務，因此必須能提出並核准終端機命令。

### 4. 實機驗證：Chat、Agent 與終端機

- [ ] **Chat**：開啟 Copilot Chat，問「`what is 1+1`」，能收到回應。
- [ ] **Agent**：切到 Agent mode，要求它在工作區建立 `preflight.txt`，確認可提出檔案修改。
- [ ] **終端機核准**：要求 Agent 執行 `python --version`，確認學員能看到並按 **Run** 核准命令。

> Chat 正常但 Agent 不能寫檔或不能提出/執行終端機命令時，實作練習仍可能卡關，請先處理工作區信任或組織政策。

---

## ② 本機執行環境與套件

工作坊會使用 Python 產生檔案、建立 API 服務並執行本機服務。**Lab 素材壓縮檔於上課當天提供**，課程套件也是當天由素材附的腳本一次裝好；**課前只需建好上課用的資料夾與共用 venv**。

### Node.js 與 npm（選配）

Node.js 並非主要課程的必要條件；只有需要執行選配前端內容時才需安裝。

```powershell
node --version
npm --version
npm ping
```

- [ ] （選配）`npm ping` 成功，或至少取得 registry 回應而非逾時、Proxy/SSL 錯誤。
- [ ] （選配）Node.js 為 18+（建議 20 LTS）。
- [ ] （選配）本機可開啟瀏覽器並存取本機開發伺服器。

### Python

```powershell
python --version
```

- [ ] Python 為 3.10+。
- [ ] 不是 Microsoft Store 版（`(Get-Command python).Source` 的路徑**不應包含** `WindowsApps`）。若是，請改裝 [python.org](https://www.python.org/downloads/windows/) 版本，或到「設定 → 應用程式 → 應用程式執行別名」關閉 `python.exe` 的別名。
- [ ] Agent mode 可在工作區建立 Python 檔，且學員可核准終端機執行。

### 建立上課用資料夾與共用 venv

請自行建立一個上課用的資料夾（路徑請避免中文與空白，例如 `C:\ghcp-workshop`，位置與名稱可自訂），當天的 Lab 素材會解壓到這裡。接著在該資料夾中開啟 PowerShell，建立共用 `.venv`：

```powershell
cd C:\ghcp-workshop        # 換成你自己建立的資料夾
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --no-cache-dir --force-reinstall pip
python -m pip --version
```

- [ ] 上課用資料夾已建立。
- [ ] `python -m venv .venv` 成功，資料夾中出現 `.venv`（沒有被防毒軟體或資料夾權限擋住）。
- [ ] PowerShell 提示字元出現 `(.venv)`，代表共用 venv 已啟用。
- [ ] 出現 `Successfully installed pip-…`，代表能連到 PyPI 下載並安裝（沒有逾時、Proxy 或 SSL 憑證錯誤）。
- [ ] `pip --version` 顯示的路徑落在該資料夾的 `.venv` 裡，代表裝進 venv 而非全域。
- [ ] **不要刪掉這個 `.venv`**，上課當天會直接沿用它，不會重建。

> 第三行 `--no-cache-dir --force-reinstall` 是刻意的：強迫真的去 PyPI 下載一次，否則 pip 已是最新時只會印「Requirement already satisfied」，就驗不到網路。
>
> 課前**不需要、也請不要安裝任何課程套件**（FastAPI、openpyxl 那些當天由素材附的腳本一次裝好）。
>
> 若出現 SSL 憑證錯誤或逾時，通常是公司 Proxy 或 TLS 檢查所致，請先與 IT 確認 `pypi.org` 與 `files.pythonhosted.org` 可通行——**這是課前最需要提早排除的一項**。

### localhost 服務

這項測試是確認電腦允許 Python 在 localhost 啟動服務，且另一個程式可以連線。工作坊會用本機 Mock API 模擬企業系統（例如 Jira）；Agent 會啟動這個 API，再透過 HTTP 呼叫它。若公司端點防護或防火牆阻擋本機服務，相關實作就無法進行。

請同時開啟**兩個彼此獨立的 PowerShell 視窗**，不要在同一個視窗依序執行。

**PowerShell 視窗 1：啟動測試服務**

執行下列命令後，視窗會持續停在服務執行狀態，這是正常現象；請保持此視窗開啟。

```powershell
python -m http.server 9000 --bind 127.0.0.1
```

**PowerShell 視窗 2：測試連線**

保持視窗 1 的服務運作，切換到另一個 PowerShell 視窗執行：

```powershell
curl.exe -I http://127.0.0.1:9000
```

- [ ] 視窗 2 能收到 `HTTP/1.0 200 OK` 或其他 HTTP 回應。
- [ ] 驗證完成後，回到視窗 1 按 `Ctrl+C` 停止測試服務。

> 若公司端點防護或防火牆阻擋 Python 監聽 localhost port `9000`，請先與 IT 確認。

---

## ③ GitHub repository、CLI 與雲端 coding agent

### GitHub repository 權限

- [ ] 擁有一個自己可寫入的 GitHub repository，或有權限建立新 repository。
- [ ] 能在任一測試 repository 完成 clone、commit 與 push。
- [ ] 所屬組織已開通 **GitHub Copilot coding agent**；若未開通，請先請組織管理員確認政策。

```powershell
git status
git remote -v
```

> 上述命令請在自己現有的測試 repository 內執行，不需要工作坊教材。

### Copilot CLI

```powershell
winget install GitHub.Copilot    # 尚未安裝時；也可用 npm install -g @github/copilot
copilot --version
copilot                          # 進入 CLI 後執行 /login，再用 /exit 離開
```

- [ ] `copilot --version` 有正常輸出。
- [ ] 已在 Copilot CLI 完成 `/login`。
- [ ] 所屬組織已開通 **Copilot CLI** 政策。

### GitHub CLI

```powershell
winget install GitHub.cli    # 尚未安裝時
gh --version
gh auth status              # 未登入請執行 gh auth login
```

- [ ] `gh auth status` 顯示已登入預計上課使用的 GitHub 帳號。

> 請確認登入的帳號對預計使用的 repository 有寫入權限。

---

## ④ MCP 連線前置

### MCP 真實設定體驗（三選一）

工作坊會使用 MCP；CalendarTools 不可用時，可改走 GitHub remote MCP 或免登入的 Microsoft Learn MCP。課前不需建立設定檔，只需確認至少一條路徑可行：

- [ ] **路徑一：CalendarTools**。已有 M365 Copilot 授權，並已提前查好 Entra ID 租戶 ID（`tenant_id`）：

  ```powershell
  # 用公司網域換取租戶 ID，不需登入或任何權限
  (Invoke-RestMethod "https://login.microsoftonline.com/<你的公司網域>/v2.0/.well-known/openid-configuration").issuer
  ```

  回傳的 `issuer` 格式為 `https://login.microsoftonline.com/<tenant_id>/v2.0`，中間的 GUID 即為 `tenant_id`。

- [ ] **路徑二：GitHub remote MCP**。沒有 CalendarTools 授權，但可用 GitHub 帳號完成 OAuth；server URL 為 `https://api.githubcopilot.com/mcp/`。
- [ ] **路徑三：Microsoft Learn MCP**。不方便使用前兩者時，採免登入、免 OAuth 路徑；server URL 為 `https://learn.microsoft.com/api/mcp`。

> 不需要在課前建立 MCP 設定檔或準備任何範例資料。

---

## 網路 / Proxy / 防火牆

### A. 快速連線測試

在 PowerShell 執行：

```powershell
# Copilot 與 GitHub 基本 HTTPS 連通性
Test-NetConnection api.github.com -Port 443

# 回傳任意 HTTP 狀態碼代表可連到目標服務；逾時、拒絕或 SSL 錯誤才是異常
curl.exe -s -o NUL -w "github=%{http_code}`n" https://api.github.com
curl.exe -s -o NUL -w "copilot-proxy=%{http_code}`n" https://copilot-proxy.githubusercontent.com
curl.exe -s -o NUL -w "copilot-api=%{http_code}`n" https://api.githubcopilot.com

# 選配前端內容會使用的套件來源
npm ping

# Python 套件來源（任意 HTTP 狀態碼代表已連到服務）
curl.exe -s -o NUL -w "pypi=%{http_code}`n" https://pypi.org/simple/
curl.exe -s -o NUL -w "pythonhosted=%{http_code}`n" https://files.pythonhosted.org

# MCP 路徑二、三（選用哪條就測哪條；任意 HTTP 狀態碼代表已連到服務）
curl.exe -s -o NUL -w "github-mcp=%{http_code}`n" https://api.githubcopilot.com/mcp/
curl.exe -s -o NUL -w "learn-mcp=%{http_code}`n" https://learn.microsoft.com/api/mcp
```

> Node.js 為選配，因此不執行前端內容時可略過 `npm ping`。

---


## 參考資料

- [GitHub Copilot allowlist reference](https://docs.github.com/en/copilot/reference/copilot-allowlist-reference)
- [GitHub Copilot network settings](https://docs.github.com/en/copilot/concepts/network-settings)
- [VS Code network connections](https://code.visualstudio.com/docs/setup/network)
