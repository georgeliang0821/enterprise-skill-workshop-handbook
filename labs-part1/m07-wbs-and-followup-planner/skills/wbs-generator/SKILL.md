---
name: wbs-generator
description: 依會議逐字稿或使用者描述的專案範圍,產生結構化 WBS(Work Breakdown Structure),輸出為 Excel 檔案(.xlsx),包含任務階層大綱群組、負責人、狀態欄位,並套用篩選與凍結窗格。是「專案範圍分解成 Excel 檔案」,不是會議摘要(那是 meeting-summary),也不是本週跟進規劃(那是 weekly-followup-planner)。關鍵詞:WBS、work breakdown structure、任務分解、專案分解、拆解、排程。
disable-model-invocation: false
user-invocable: true
version: 0.1.0
---
# WBS 產生 Skill(WBS Generator)

## ① 適用範圍 / 不適用時改用
- 適用:使用者提供專案範圍描述、逐字稿內容,或已整理好的待辦事項,並要求拆解成 WBS、產生任務分解結構。
- 不適用:例行進度會議,內容裡沒有範圍界定或任務分解的討論依據——不要勉強套用,先反問使用者要拆解的範圍是什麼。
- 不適用:使用者要的是會議摘要或待辦清單 → 改用 `meeting-summary`。
- 不適用:使用者要的是看本週空檔、安排跟進未結事項 → 改用 `weekly-followup-planner`。

## ② 需要的輸入
1. 專案範圍描述,或已有的逐字稿/待辦事項清單(必要)——可以直接沿用 `meeting-summary` 產出的 Action Items 當作輸入的一部分。
2. 階層深度期望(選,預設拆到第二層,即「工作包 → 子任務」)。
3. 輸出檔名(選,沒指定則用專案名稱 + 日期命名)。

> 輸入內容不足以判斷任務邊界時(例如只有一句話帶過的範圍),先反問使用者要拆解到多細,不要自己腦補出一堆工作包。

## ③ 步驟
1. 通讀輸入,辨識主要工作包(Work Package)。
2. 依 MECE 原則(彼此獨立、互無遺漏)分解到②指定的深度,預設不超過三層。
3. 每個末端任務標註負責人(若輸入裡有明確指派)與狀態;沒有依據的欄位留空或標記「未定」,不能自己捏造。
4. **明確排除的項目不要塞進 WBS**——如果輸入裡有「這個先不排進本階段範圍,之後再討論」這類明確排除的內容,不要因為它被提到就列成工作項。
5. 依下方固定範本寫一份 Python 腳本(不要自行改變這個結構),用檔案編輯工具建立腳本檔案。
6. 在終端機執行腳本,產出 .xlsx。若執行報錯,讀取錯誤訊息修正腳本後重跑,不要略過失敗直接回報完成。
7. 依 ⑤ 品質自檢逐項確認。

### 固定參考腳本(openpyxl)

```python
import openpyxl
from openpyxl.styles import Alignment
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "WBS"

headers = ["WBS編號", "任務名稱", "負責人", "狀態", "備註/來源"]
ws.append(headers)

# rows: list of (wbs_no, name, owner, status, note, level)
# level 從 0 開始,對應大綱群組層數
for row in rows:
    wbs_no, name, owner, status, note, level = row
    r = ws.max_row + 1
    ws.cell(row=r, column=1, value=wbs_no)
    cell = ws.cell(row=r, column=2, value=name)
    cell.alignment = Alignment(indent=level)
    ws.cell(row=r, column=3, value=owner or "未定")
    ws.cell(row=r, column=4, value=status or "未開始")
    ws.cell(row=r, column=5, value=note or "")
    if level > 0:
        ws.row_dimensions[r].outline_level = level

last_col = get_column_letter(len(headers))
ws.auto_filter.ref = f"A1:{last_col}{ws.max_row}"
ws.freeze_panes = "A2"

for i, h in enumerate(headers, start=1):
    ws.column_dimensions[get_column_letter(i)].width = 30 if i == 2 else 16

wb.save("wbs_output.xlsx")
```

## ④ 輸出格式
一個 .xlsx 檔案,單一工作表「WBS」,欄位:WBS編號 / 任務名稱(依階層縮排)/ 負責人 / 狀態 / 備註來源。標題列凍結、套用篩選,子項的大綱層級(outline_level)要對應 WBS 編號的階層深度(例如 1.1.1 的 outline_level 是 2)。

## ⑤ 品質自檢(產出後逐項確認,沒過就修再交)
- [ ] 每個末端任務都能對應到輸入內容裡的具體描述,沒有無中生有的工作包。
- [ ] 輸入裡明確排除、延後討論的項目,沒有被誤列進 WBS。
- [ ] WBS 編號的階層深度,跟 Excel 的 outline_level 一致。
- [ ] AutoFilter 涵蓋所有欄位、所有資料列(標題列到最後一列)。
- [ ] 標題列有凍結窗格。
- [ ] 沒有依據的負責人/狀態,標記「未定」/「未開始」,沒有自己捏造。
- [ ] 腳本執行後有確認檔案實際產出且可開啟,不是只看到終端機顯示「執行完成」就回報成功。
