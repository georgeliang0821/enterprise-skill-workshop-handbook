# CHANGELOG — weekly-followup-planner

## v0.3.0 — 2026-07-29
- 由 `meeting-prep-brief` 重新命名為 `weekly-followup-planner`,並改寫故事線。
- 原「依某場會議產生會前提要」需要行事曆事件與內部 Action Item 依與會者對齊,無法用真實個人行事曆練習;改為「查本週空檔 + 列未結 Action Item」——空檔與未結事項兩個來源各自獨立、不需對齊,真 CalendarTools 可直接查使用者自己的行事曆當主線。
- 沒有 Agent365 / CalendarTools 存取權時,改用 `data/sample-calendar-week.json` 或口頭「假設本週某些時段都有空」;未結事項那一端兩條路完全一致。
- 邊界測試由「查無此會議」改為「本週排滿 → 誠實回報無空檔」。

## v0.1.0 — 2026-07-08
- 初版建立(Workshop 課堂產出,原名 `meeting-prep-brief`)。
