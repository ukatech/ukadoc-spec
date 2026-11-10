# `\![execute,schedule-delete,UID,オプション...]`

**カテゴリ:** Unclassified command

Delete the event with the specified UID from the ghost calendar. Events in the user's calendar or the schedule sensor cannot be deleted.<br />
The result is reported through [OnExecuteScheduleComplete](../../shiori-event/other-communication/OnExecuteScheduleComplete.md), and failures (including when no matching event exists) through [OnExecuteScheduleFailure](../../shiori-event/other-communication/OnExecuteScheduleFailure.md). This command cannot be run from scripts sent externally, such as via SSTP.<br />
The only option is --event=event ID. See [schedule-add](bang-execute-schedule-add.md).

**対応:** SSP 2.8.91
