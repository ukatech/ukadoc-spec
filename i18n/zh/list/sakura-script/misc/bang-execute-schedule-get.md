# `\![execute,schedule-get,オプション,オプション,オプション...]`

**カテゴリ:** 未分类命令

读取 ghost 专用日历中的日程，并通过[OnExecuteScheduleGetComplete](../../shiori-event/other-communication/OnExecuteScheduleGetComplete.md)通知。Reference 的格式与[OnExecuteICalComplete](../../shiori-event/other-communication/OnExecuteICalComplete.md)相同。<br />
读取范围仅限 ghost 专用日历，不包含用户的日程或计划传感器的日程。<br />
要返回哪些日程以及返回多少项，可通过[iCal筛选选项](bang-execute-ical-post-URL.note.md)（--from・--to・--expand・--limit）指定。还可使用 --event=事件ID。

**対応:** SSP 2.8.91

## 記述例

```sakurascript
\![execute,schedule-get,--expand=7,--event=OnMySchedule]今日から7日ぶんのゴースト用の予定を「発生」単位で展開し、OnMyScheduleで受け取る。
```
