# `\![execute,ical-get,URL,オプション,オプション,オプション...]`

**カテゴリ:** 未分类命令

使用[※选项](bang-execute-http-options-URL.note.md)发送 http get 请求，并将响应解析为 iCalendar（RFC 5545）日历，然后将解析结果作为事件通知。<br />
参数组的指定方式与 http-post 相同。

获取到的事件通过[OnExecuteICalComplete](../../shiori-event/other-communication/OnExecuteICalComplete.md)通知；失败时通过[OnExecuteICalFailure](../../shiori-event/other-communication/OnExecuteICalFailure.md)通知。

通过[iCal 筛选选项](bang-execute-ical-post-URL.note.md)（--from・--to・--expand・--limit）指定返回哪些事件以及返回多少个事件。未指定时，按文件中的顺序返回所有 VEVENT。

解析对象是 VCALENDAR 直接包含的 X-WR-CALNAME・X-WR-TIMEZONE・CALSCALE，以及 VEVENT（及其内部的 VALARM）。不含 SUMMARY 的 VEVENT 将被视为无效并排除。<br />
另外，即使指定了 --nofile，也会创建用于解析的临时文件（该指定会被忽略）。

**対応:** SSP 2.8.90

## 記述例

```sakurascript
\![execute,ical-get,https://example.com/calendar.ics,--async=OnMyCalendar,--expand=7]今日から7日ぶんの予定を「発生」単位で展開し、OnMyCalendarで受け取る。
```

```sakurascript
\![execute,ical-get,https://example.com/calendar.ics,--async=OnMyCalendar,--from=20261201,--to=20261231,--limit=50]2026年12月に発生する予定を最大50件、VEVENT単位で受け取る。
```
