# `\![execute,schedule-delete,UID,オプション...]`

**カテゴリ:** Uncategorized commands

Delete the event with the specified UID from the ghost calendar. Events belonging to the user or the schedule sensor cannot be deleted.<br />
Results are reported through [OnExecuteScheduleComplete](../../shiori-event/other-communication/OnExecuteScheduleComplete.md), or [OnExecuteScheduleFailure](../../shiori-event/other-communication/OnExecuteScheduleFailure.md) on failure (including when no matching event exists). This command cannot be run from scripts sent externally, such as via SSTP.<br />
The only available option is --event=event ID. See [schedule-add](bang-execute-schedule-add.md).

**対応:** SSP 2.8.91
