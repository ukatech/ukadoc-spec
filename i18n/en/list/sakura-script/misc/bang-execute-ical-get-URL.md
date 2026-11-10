# `\![execute,ical-get,URL,オプション,オプション,オプション...]`

**カテゴリ:** Uncategorized command

Send an HTTP GET request with [※options](bang-execute-http-options-URL.note.md), parse the response as an iCalendar (RFC 5545) calendar, and then notify the parsed results as events.<br />
The parameter specification is the same as for http-post.

Retrieved events are notified through [OnExecuteICalComplete](../../shiori-event/other-communication/OnExecuteICalComplete.md), and failures through [OnExecuteICalFailure](../../shiori-event/other-communication/OnExecuteICalFailure.md).

Specify which events to return and how many with the [iCal filtering options](bang-execute-ical-post-URL.note.md) (--from, --to, --expand, and --limit). If none are specified, all VEVENTs in the file are returned, starting from the first.

The items parsed are X-WR-CALNAME, X-WR-TIMEZONE, and CALSCALE directly under VCALENDAR, as well as VEVENT (and VALARM within it). VEVENTs without SUMMARY are considered invalid and excluded.<br />
A temporary file for parsing is created even if --nofile is specified (the option is ignored).

**対応:** SSP 2.8.90

## 記述例

```sakurascript
\![execute,ical-get,https://example.com/calendar.ics,--async=OnMyCalendar,--expand=7]今日から7日ぶんの予定を「発生」単位で展開し、OnMyCalendarで受け取る。
```

```sakurascript
\![execute,ical-get,https://example.com/calendar.ics,--async=OnMyCalendar,--from=20261201,--to=20261231,--limit=50]2026年12月に発生する予定を最大50件、VEVENT単位で受け取る。
```
