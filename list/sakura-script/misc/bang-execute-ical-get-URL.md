# `\![execute,ical-get,URL,オプション,オプション,オプション...]`

**カテゴリ:** 未分類コマンド

[※オプション](notes_executehttp.md)付きでhttp get リクエストを行い、レスポンスをiCalendar(RFC 5545)のカレンダーとして解析したのち、解析結果をイベントとして通知する。<br />
パラメータ群の指定はhttp-postと同じ。

取得したイベントは[OnExecuteICalComplete](../../shiori-event/other-communication/OnExecuteICalComplete.md)、失敗時は[OnExecuteICalFailure](../../shiori-event/other-communication/OnExecuteICalFailure.md)で通知される。

どのイベントをいくつ返すかは[iCal絞り込みオプション](notes_executeical.md)（--from・--to・--expand・--limit）で指定する。無指定の場合はファイルに書かれたVEVENTを先頭から全件返す。

解析対象はVCALENDAR直下のX-WR-CALNAME・X-WR-TIMEZONE・CALSCALEと、VEVENT（およびその中のVALARM）。SUMMARYを持たないVEVENTは無効とみなして除外される。<br />
なお、--nofileを指定しても解析用の一時ファイルは作成される（指定は無視される）。

**対応:** SSP 2.8.90

## 記述例

```sakurascript
\![execute,ical-get,https://example.com/calendar.ics,--async=OnMyCalendar,--expand=7]今日から7日ぶんの予定を「発生」単位で展開し、OnMyCalendarで受け取る。
```

```sakurascript
\![execute,ical-get,https://example.com/calendar.ics,--async=OnMyCalendar,--from=20261201,--to=20261231,--limit=50]2026年12月に発生する予定を最大50件、VEVENT単位で受け取る。
```
