# M3 / M5 / M6 · 翻車①:偏離預期實驗(三輪)

同一份逐字稿(`../m06-meeting-summary-skill/sample-transcript.txt`)、同一句指令「幫我整理這場會議的紀錄」、**同一個模型**,跑三輪:

1. **M3 第一輪(乾淨環境)**:repo 根目錄沒有 `AGENTS.md`,`.github/` 底下沒有任何 instructions / prompts / skills。
2. **M4** 之後 → **M5 第二輪**:多了 `AGENTS.md`,新開 session 再跑同一句。
3. **M6** 之後 → **第三輪**:多了 `meeting-summary` Skill,同樣記在 worksheet 上——這是今天第一次完整的 before / after。

## 全班鎖同一個模型,不用 Auto

模型選單全班鎖同一個講師指定的模型(當天可用的 1x 等級即可),三輪都用同一個,並在 worksheet 記下模型名稱。這樣三輪之間唯一的變因就是「有沒有 instructions / 有沒有 Skill」;Auto 會在不同時間路由到不同模型,那是另一個變因,今天刻意不混進來(Auto 怎麼運作、什麼情境該鎖模型,見講義附錄 B)。

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

第二輪的預期:Owner 與日期格式多半收斂,判斷邏輯與結構仍偏離——這是 instructions 的邊界,也是 M6 Lab 存在的理由。第三輪的預期:四項都收斂。
