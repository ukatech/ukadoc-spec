# `\![execute,schedule-delete,UID,オプション...]`

**カテゴリ:** 未分類コマンド

ゴースト用の予定表から、指定したUIDの予定を削除する。ユーザーの予定・スケジュールセンサの予定は削除できない。<br />
結果は[OnExecuteScheduleComplete](../../shiori-event/other-communication/OnExecuteScheduleComplete.md)、失敗時（該当する予定が無い場合を含む）は[OnExecuteScheduleFailure](../../shiori-event/other-communication/OnExecuteScheduleFailure.md)で通知される。SSTPなど外部から送られたスクリプトでは実行できない。<br />
オプションは --event=イベントID のみ。[schedule-add](bang-execute-schedule-add.md)と同じ。

**対応:** SSP 2.8.91
