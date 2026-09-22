# M3 偏離預期實驗 + M6 Lab 6:建立 Meeting Notes Skill

這個資料夾涵蓋兩段:先做 **M3 翻車實驗**(15 分鐘,在學任何 SKILL.md 語法之前),再進 **Lab 6** 把實驗裡看到的偏離預期收斂掉。順序不要顛倒——先親眼看到問題,再學解法。

## M3 · 翻車① 第一輪:同一句 prompt、同一個模型,N 種輸出

**每個人都做,不要跳過。**

1. 開一個**乾淨環境**——確認 `.github/skills/` 底下沒有任何 Skill、沒有特別的 instructions。
2. 把 `sample-transcript.txt` 內容貼進 Copilot Chat,只下這一句,一字不多、一字不少,全班同一句:

   > 幫我整理這場會議的紀錄

3. 跑完**不要修、不要重跑**,保留第一次輸出(存成 `baseline-output.md` 之類的檔案,等一下 Lab 6 要拿來對比)。
4. 講師抽 3-4 位學員,把輸出投影並排比對,盯這四個點:

| 檢查點 | 你會看到的偏離預期 |
|---|---|
| 輸出結構 | 有人分成摘要/決議/待辦,有人一大段流水帳,有人多了自創區塊 |
| Due Date | David「這週五前」、George「下週三前」——有人換算成實際日期,有人照抄相對用詞,有人沒抓到 |
| Decisions 判定 | SAP 整合明講「先不排進 PoC 範圍」——有人正確排除,有人列成決議或待辦 |
| Owner 欄位 | 有人寫姓名(David / Mary / George),有人寫職稱(架構師 / 財務窗口) |

同一句 prompt、同一份輸入,輸出還是不一樣——這不是 prompt 寫不好,是 sampling variance:沒被固定下來的判斷,每次都會被重新「發明」一次。這就是 Consistency Gap 的長相,也是「把 prompt 傳給同事」為什麼不夠的答案。

> **給講師**:抽樣優先挑「Due Date 換算」跟「SAP 誤列」——最不需要解釋就能看出會出事。現場偏離預期不明顯時,備案是投影事先收集的三份歷史輸出。

## Lab 6:建立 Meeting Notes Skill

### 目標

自己動手寫一份 `SKILL.md`,把 M3 那句「幫我整理這場會議的紀錄」收斂成穩定輸出四個區塊:Meeting Summary / Decisions / Risks / Action Items。

摘要跟待辦合併成同一個 Skill,是因為:權限邊界一樣(都只讀逐字稿、不寫外部系統)、實務上幾乎永遠一起被需要(摘要拿去報告、待辦拿去追蹤)。詳細判斷邏輯見講義 M6「Scope 怎麼抓」。

### 操作步驟

1. 建立 `.github/skills/meeting-summary/SKILL.md`,對照講義的四區塊骨架**自己填寫**(不要直接複製 `skills/meeting-summary/SKILL.md` 完成版——那份是對照用)。寫的時候,把 M3 觀察到的每一種偏離預期對應成一條明確規則:什麼算決議、日期怎麼換算、Owner 用姓名不用職稱、區塊為空也要寫「無」。
2. 存檔後,Chat 輸入 `/skills` 確認被偵測到。
3. **關鍵一步:用跟 M3 一模一樣的方式再跑一次(同一個模型、新開 session)**——同一份逐字稿(開頭已標註會議日期 2026-07-08)、同一句「幫我整理這場會議的紀錄」,**不要點名 Skill 名稱**,觀察有沒有自動選中。
4. 把這次輸出跟你保留的 `baseline-output.md` 並排比對——這是今天第一組 before/after,也是你之後回公司推 Skill 時最有說服力的素材。
5. 檢查 Due Date:David「這週五前」、Mary「下週會議前」、George「下週三前」都換算成 YYYY-MM-DD。
6. 對照完成版,檢查差異——特別是 `description` 的寫法,以及「什麼才算真正的決議」「Due Date 怎麼換算」這兩種容易含糊的判斷怎麼寫清楚。

### 完成檢核

- [ ] `/skills` 看得到 meeting-summary;沒點名 Skill 名稱有自動選用
- [ ] 跟 M3 baseline 並排比對,四種偏離預期(結構/日期/決議判定/Owner)都被收斂
- [ ] Decisions 沒有把「討論中」內容誤判成決議;SAP 整合沒有出現在任何區塊
- [ ] Risks 每一項都能回頭在逐字稿裡指出對應發言
- [ ] Due Date 都是換算後的實際日期,沒有殘留「這週五」「下週三」
- [ ] Owner 都是實際姓名(David / Mary / George),不是職稱

> 📌 **留著這三個 Skill 檔案**:M7 做完後,`.github/skills/` 裡會有三個 Skill 並存——M8 的誤觸發實測要用。
