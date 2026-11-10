# `\![execute,ical-get,URL,オプション,オプション,オプション...]`

**カテゴリ:** 未分類命令

使用[※選項](bang-execute-http-options-URL.note.md)執行 HTTP GET 請求，並將回應解析為 iCalendar（RFC 5545）行事曆，再將解析結果作為事件通知。<br />
參數群組的指定方式與 http-post 相同。

取得的事件會透過[OnExecuteICalComplete](../../shiori-event/other-communication/OnExecuteICalComplete.md)通知，失敗時則透過[OnExecuteICalFailure](../../shiori-event/other-communication/OnExecuteICalFailure.md)通知。

要回傳哪些事件及其數量，可透過[iCal 篩選選項](bang-execute-ical-post-URL.note.md)（--from・--to・--expand・--limit）指定。若未指定，則從檔案開頭依序回傳所有 VEVENT。

解析對象為 VCALENDAR 直屬的 X-WR-CALNAME・X-WR-TIMEZONE・CALSCALE，以及 VEVENT（及其中的 VALARM）。不含 SUMMARY 的 VEVENT 會視為無效並排除。<br />
另外，即使指定 --nofile，仍會建立解析用的暫存檔（此指定會被忽略）。

**対応:** SSP 2.8.90

## 記述例

```sakurascript
\![execute,ical-get,https://example.com/calendar.ics,--async=OnMyCalendar,--expand=7]今日から7日ぶんの予定を「発生」単位で展開し、OnMyCalendarで受け取る。
```

```sakurascript
\![execute,ical-get,https://example.com/calendar.ics,--async=OnMyCalendar,--from=20261201,--to=20261231,--limit=50]2026年12月に発生する予定を最大50件、VEVENT単位で受け取る。
```
