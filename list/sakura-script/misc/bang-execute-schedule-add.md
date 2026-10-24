# `\![execute,schedule-add,オプション,オプション,オプション...]`

**カテゴリ:** 未分類コマンド

ゴースト用の予定表に予定を1件登録する。登録した予定はSSPのカレンダーに表示され、ユーザーの予定と同じく今日の予定や[OnSchedule5MinutesToGo](../../shiori-event/calendar/OnSchedule5MinutesToGo.md)の対象になる。<br />
ゴースト用の予定表は、ユーザーの予定・スケジュールセンサとは別のファイル（data/schedule/ghost/schedule.ics）に保存され、すべてのゴーストで共有される。他のゴーストが登録した予定も上書き・削除できる。<br />
ユーザーはカレンダー上で閲覧できるが編集はできない。カレンダーのメニュー「すべて削除」→「ゴーストが登録した予定」で一括削除できる。<br />
結果は[OnExecuteScheduleComplete](../../shiori-event/other-communication/OnExecuteScheduleComplete.md)、失敗時は[OnExecuteScheduleFailure](../../shiori-event/other-communication/OnExecuteScheduleFailure.md)で通知される。SSTPなど外部から送られたスクリプトでは実行できない。

オプション（--summary と --start は必須）<br />
--summary=タイトル : 予定のタイトル(SUMMARY)。<br />
--start=日時 : 開始日時。yyyymmdd なら終日予定、yyyymmddThhmm または yyyymmddThhmmss なら時刻付き（ローカル時刻）。区切りの - と : は無視される。<br />
--end=日時 : 終了日時。書式は --start と同じ。省略時は開始日の1日だけの予定になる。<br />
--uid=UID : 予定の識別子。空白を含まない半角英数記号のみ。同じUIDの予定があれば置き換える。省略時はSSPが割り当て、OnExecuteScheduleCompleteで返す。<br />
--description=説明 : DESCRIPTION。<br />
--location=場所 : LOCATION。<br />
--url=URL : URL。<br />
--categories=分類 : CATEGORIES。複数ある場合はカンマ区切り（iCalのCATEGORIESの値としてそのまま保存される）。<br />
--status=状態 : STATUS（CONFIRMED / TENTATIVE / CANCELLED）。<br />
--type=種類 : 予定の種類。[OnSchedule5MinutesToGo](../../shiori-event/calendar/OnSchedule5MinutesToGo.md)等のReference0に入る。<br />
--rrule=規則 : 繰り返し規則（RRULEの値部分。例 FREQ=WEEKLY;BYDAY=MO）。<br />
--exdate=日付 : 繰り返しから除外する日（yyyymmdd）。複数ある場合はカンマ区切り。<br />
--notify=分 : 何分前に通知するか。省略時はSSPの設定に従う。<br />
--script=スクリプト : 予定に添えるさくらスクリプト。通知時・予定を読むときに実行される。<br />
--event=イベントID : Onから始まるIDを指定すると、結果のイベント名がそのIDになる（失敗時はIDの後ろにFailureをつけた名前）。<br />
カンマを含む値（--rrule・--exdate・--categories など）を指定する場合は、引数全体を " " で囲むこと。

**対応:** SSP 2.8.91

## 記述例

```sakurascript
\![execute,schedule-add,--uid=myghost-meeting,--summary=打ち合わせ,--start=20261001T1000,--end=20261001T1100,"--rrule=FREQ=WEEKLY;BYDAY=TH",--notify=10,--event=OnMyScheduleAdded]2026年10月1日から毎週木曜10時の予定を登録し、10分前に通知させる。
```

```sakurascript
\![execute,schedule-add,--summary=記念日,--start=20261224,--rrule=FREQ=YEARLY]毎年12月24日の終日予定を登録する。
```
