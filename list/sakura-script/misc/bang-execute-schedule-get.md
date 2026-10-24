# `\![execute,schedule-get,オプション,オプション,オプション...]`

**カテゴリ:** 未分類コマンド

ゴースト用の予定表に登録されている予定を読み出し、[OnExecuteScheduleGetComplete](../../shiori-event/other-communication/OnExecuteScheduleGetComplete.md)で通知する。Referenceの形式は[OnExecuteICalComplete](../../shiori-event/other-communication/OnExecuteICalComplete.md)と同じ。<br />
対象はゴースト用の予定表だけで、ユーザーの予定・スケジュールセンサの予定は含まれない。<br />
どの予定をいくつ返すかは[iCal絞り込みオプション](notes_executeical.md)（--from・--to・--expand・--limit）で指定する。ほかに --event=イベントID が使える。

**対応:** SSP 2.8.91

## 記述例

```sakurascript
\![execute,schedule-get,--expand=7,--event=OnMySchedule]今日から7日ぶんのゴースト用の予定を「発生」単位で展開し、OnMyScheduleで受け取る。
```
