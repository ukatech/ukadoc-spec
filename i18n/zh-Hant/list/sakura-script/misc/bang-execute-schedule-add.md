# `\![execute,schedule-add,オプション,オプション,オプション...]`

**カテゴリ:** Uncategorized commands

Add one event to the ghost calendar. The event is displayed in the SSP calendar and, like the user's events, is included in today's schedule and in [OnSchedule5MinutesToGo](../../shiori-event/calendar/OnSchedule5MinutesToGo.md).<br />
The ghost calendar is stored in a separate file (data/schedule/ghost/schedule.ics) from the user's events and the schedule sensor, and is shared by all ghosts. Events added by other ghosts can also be overwritten or deleted.<br />
Users can view the events in the calendar but cannot edit them. They can delete all of them at once from the calendar menu: "Delete all" → "Events added by ghosts".<br />
Results are reported through [OnExecuteScheduleComplete](../../shiori-event/other-communication/OnExecuteScheduleComplete.md), or [OnExecuteScheduleFailure](../../shiori-event/other-communication/OnExecuteScheduleFailure.md) on failure. This command cannot be run from scripts sent externally, such as via SSTP.

Options (--summary and --start are required)<br />
--summary=title: Event title (SUMMARY).<br />
--start=date and time: Start date and time. yyyymmdd indicates an all-day event; yyyymmddThhmm or yyyymmddThhmmss indicates an event with a time (local time). The - and : separators are ignored.<br />
--end=date and time: End date and time. The format is the same as for --start. If omitted, the event lasts only for the start date.<br />
--uid=UID: Event identifier. Only single-byte alphanumeric characters and symbols, excluding spaces, are allowed. Replaces any event with the same UID. If omitted, SSP assigns one and returns it in OnExecuteScheduleComplete.<br />
--description=description: DESCRIPTION.<br />
--location=location: LOCATION.<br />
--url=URL: URL.<br />
--categories=categories: CATEGORIES. Separate multiple values with commas (they are stored as-is as the value of iCal's CATEGORIES).<br />
--status=status: STATUS (CONFIRMED / TENTATIVE / CANCELLED).<br />
--type=type: Event type. Used as Reference0 for [OnSchedule5MinutesToGo](../../shiori-event/calendar/OnSchedule5MinutesToGo.md) and other events.<br />
--rrule=rule: Recurrence rule (the value portion of RRULE; for example, FREQ=WEEKLY;BYDAY=MO).<br />
--exdate=date: Date to exclude from the recurrence (yyyymmdd). Separate multiple dates with commas.<br />
--notify=minutes: How many minutes in advance to notify. If omitted, the SSP setting is used.<br />
--script=script: Sakura Script to attach to the event. It is run when notifying the user and when reading the event.<br />
--event=event ID: If an ID beginning with On is specified, the result event name is set to that ID (on failure, the name has Failure appended to the ID).<br />
When specifying a value that contains commas (such as --rrule, --exdate, or --categories), enclose the entire argument in " ".

**対応:** SSP 2.8.91

## 記述例

```sakurascript
\![execute,schedule-add,--uid=myghost-meeting,--summary=打ち合わせ,--start=20261001T1000,--end=20261001T1100,"--rrule=FREQ=WEEKLY;BYDAY=TH",--notify=10,--event=OnMyScheduleAdded]2026年10月1日から毎週木曜10時の予定を登録し、10分前に通知させる。
```

```sakurascript
\![execute,schedule-add,--summary=記念日,--start=20261224,--rrule=FREQ=YEARLY]毎年12月24日の終日予定を登録する。
```
