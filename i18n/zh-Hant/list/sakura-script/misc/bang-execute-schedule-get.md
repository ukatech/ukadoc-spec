# `\![execute,schedule-get,オプション,オプション,オプション...]`

**カテゴリ:** 未分類コマンド

讀取 ghost 專用行事曆中的行程，並透過[OnExecuteScheduleGetComplete](../../shiori-event/other-communication/OnExecuteScheduleGetComplete.md)通知。Reference 的格式與[OnExecuteICalComplete](../../shiori-event/other-communication/OnExecuteICalComplete.md)相同。<br />
僅會讀取 ghost 專用行事曆，不包含使用者行程或排程感測器的行程。<br />
要回傳哪些行程以及回傳幾個行程，可使用[iCal 篩選選項](bang-execute-ical-post-URL.note.md)（--from・--to・--expand・--limit）指定。也可以使用 --event=事件 ID。

**対応:** SSP 2.8.91

## 記述例

```sakurascript
\![execute,schedule-get,--expand=7,--event=OnMySchedule]今日から7日ぶんのゴースト用の予定を「発生」単位で展開し、OnMyScheduleで受け取る。
```
