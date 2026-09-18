# AI Meeting Intelligence Portal

## 專案概觀
- 前端:React(Vite),原始碼在 src/;後端:FastAPI,原始碼在 app/(由 OpenAPI 規格 scaffold 而來)。
- 會議相關的 Copilot 資產在 .github/(skills、agents、prompts、instructions)。

## 常用指令
- 前端開發:`npm run dev`;前端測試:`npm test`
- 後端啟動:`python -m uvicorn app.main:app --reload`;後端測試:`pytest`

## 團隊規則(每次請求都適用,保持精簡)
- 一律用繁體中文回覆;程式碼註解與 commit message 用英文。
- 提到人名時使用逐字稿或程式碼中出現的實際姓名,不要用職稱代替,也不要編造名字。
- 所有日期輸出使用 YYYY-MM-DD;無法確定的日期寫「未訂」,不要猜。
- 不要在骨架程式碼裡補上規格沒有的商業邏輯。
- 需要外部系統(Jira、行事曆)的操作時,先說明你要做什麼、再等使用者確認。
