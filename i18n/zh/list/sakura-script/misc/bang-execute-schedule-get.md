# `\![execute,schedule-get,オプション,オプション,オプション...]`

**カテゴリ:** Unclassified commands

Read events registered in the ghost calendar and report them through [OnExecuteScheduleGetComplete](../../shiori-event/other-communication/OnExecuteScheduleGetComplete.md). The Reference format is the same as for [OnExecuteICalComplete](../../shiori-event/other-communication/OnExecuteICalComplete.md).<br />
Only events in the ghost calendar are included; events in the user's calendar and schedule sensor are excluded.<br />
The [iCal filtering options](bang-execute-ical-post-URL.note.md) (--from, --to, --expand, --limit) specify which events to return and how many. The --event=event ID option is also available.

**対応:** SSP 2.8.91

## 記述例

```sakurascript
\![execute,schedule-get,--expand=7,--event=OnMySchedule]今日から7日ぶんのゴースト用の予定を「発生」単位で展開し、OnMyScheduleで受け取る。
```
