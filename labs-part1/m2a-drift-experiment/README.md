# M2a · 翻車①:漂移實驗(兩輪)

同一份逐字稿(`../lab2-meeting-summary-skill/sample-transcript.txt`)、同一句指令「幫我整理這場會議的紀錄」,跑兩輪:

1. **第一輪(乾淨環境)**:repo 根目錄沒有 `AGENTS.md`,`.github/` 底下沒有任何 instructions / prompts / skills。
2. **Lab 1B** 之後 → **第二輪**:多了 `AGENTS.md`,新開 session 再跑同一句。
3. Lab 2 之後會有 **第三輪**(有 Skill),同樣記在 worksheet 上。

## 分組:半班 Auto、半班鎖模型

講師依座位分兩半:左半邊模型選單選 **Auto**;右半邊全部鎖同一個講師指定的模型。每一輪都在 worksheet 記下「這次實際用的模型」(Auto 會在回應中顯示它選了誰)。

## 每輪都要做到的三件事

- 新開 session(不要在上一輪對話裡續問)
- 一字不改的同一句指令
- 跑完不修、不重跑,保留第一次輸出

## 比對四個檢查點

| 檢查點 | 看什麼 |
|---|---|
| 輸出結構 | 四區塊?流水帳?自創區塊? |
| Due Date | 「這週五」「下週三」有沒有換算成 YYYY-MM-DD |
| Decisions 判定 | 「SAP 整合先不排進 PoC」有沒有被誤列 |
| Owner 欄位 | 姓名還是職稱 |

第二輪的預期:Owner 與日期格式多半收斂,判斷邏輯與結構仍漂——這是 instructions 的邊界,也是 Lab 2 存在的理由。
