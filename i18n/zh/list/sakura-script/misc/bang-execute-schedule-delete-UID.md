# `\![execute,schedule-delete,UID,オプション...]`

**カテゴリ:** Unclassified commands

Delete the event with the specified UID from the ghost calendar. Events in the user's calendar and schedule sensor cannot be deleted.<br />
Results are reported through [OnExecuteScheduleComplete](../../shiori-event/other-communication/OnExecuteScheduleComplete.md), and failures through [OnExecuteScheduleFailure](../../shiori-event/other-communication/OnExecuteScheduleFailure.md) (including when the specified event does not exist). This cannot be executed from scripts sent externally, such as via SSTP.<br />
The only option is --event=event ID. It works the same way as in [schedule-add](bang-execute-schedule-add.md).

**対応:** SSP 2.8.91
