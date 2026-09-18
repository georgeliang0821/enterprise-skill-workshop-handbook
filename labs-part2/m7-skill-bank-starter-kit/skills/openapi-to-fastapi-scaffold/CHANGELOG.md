# CHANGELOG — openapi-to-fastapi-scaffold

## v0.2.0 — 2026-07-08
### 變更
- ③ 步驟與 ⑤ 品質自檢新增**重跑保護**:目標檔案已存在時,已有實作(非 TODO/NotImplementedError 骨架)的 function 跳過不覆蓋,完成回報列出被跳過清單。
### 原因(對應到的真實案例)
- Workshop M4 撞牆③:`MeetingSummary` schema 加入 `sentiment` 欄位後重跑 scaffold,`getMeetingSummary` 的手寫實作被靜默蓋回 `NotImplementedError`。規則由事故長出,非憑空想像。


## v0.1.0 — 2026-07-08
- 初版建立(Workshop 課堂產出)。
