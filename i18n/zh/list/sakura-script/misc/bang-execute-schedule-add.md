# `\![execute,schedule-add,オプション,オプション,オプション...]`

**カテゴリ:** Unclassified commands

Add one event to the ghost calendar. The event is displayed in the SSP calendar and, like a user's event, is included in today's events and in the scope of [OnSchedule5MinutesToGo](../../shiori-event/calendar/OnSchedule5MinutesToGo.md).<br />
The ghost calendar is saved to a separate file (data/schedule/ghost/schedule.ics) from the user's events and the schedule sensor, and is shared by all ghosts. Events added by other ghosts can also be overwritten or deleted.<br />
Users can view the calendar but cannot edit it. Use the calendar menu's "Delete all" → "Events added by ghosts" to delete all events at once.<br />
Results are reported through [OnExecuteScheduleComplete](../../shiori-event/other-communication/OnExecuteScheduleComplete.md), and failures through [OnExecuteScheduleFailure](../../shiori-event/other-communication/OnExecuteScheduleFailure.md). This cannot be executed from scripts sent externally, such as via SSTP.

Options (--summary and --start are required)<br />
--summary=title : Event title (SUMMARY).<br />
--start=datetime : Start date and time. yyyymmdd specifies an all-day event; yyyymmddThhmm or yyyymmddThhmmss specifies a time-specific event (local time). The - and : separators are ignored.<br />
--end=datetime : End date and time. The format is the same as --start. If omitted, the event lasts for one day, starting on the start date.<br />
--uid=UID : Event identifier. Only single-byte alphanumeric characters and symbols, with no spaces. Replaces any event with the same UID. If omitted, SSP assigns one and returns it in OnExecuteScheduleComplete.<br />
--description=description : DESCRIPTION.<br />
--location=location : LOCATION.<br />
--url=URL : URL.<br />
--categories=categories : CATEGORIES. Separate multiple values with commas (they are saved as-is as the value of iCal's CATEGORIES).<br />
--status=status : STATUS (CONFIRMED / TENTATIVE / CANCELLED).<br />
--type=type : Event type. Included in Reference0 of [OnSchedule5MinutesToGo](../../shiori-event/calendar/OnSchedule5MinutesToGo.md) and similar events.<br />
--rrule=rule : Recurrence rule (the value part of RRULE. For example, FREQ=WEEKLY;BYDAY=MO).<br />
--exdate=date : Date to exclude from the recurrence (yyyymmdd). Separate multiple dates with commas.<br />
--notify=minutes : How many minutes in advance to notify. If omitted, the SSP setting is used.<br />
--script=script : Sakura Script to attach to the event. Executed when notifying or reading the event.<br />
--event=event ID : If an ID starting with On is specified, that ID becomes the name of the result event (on failure, Failure is appended to the ID).<br />
If a value containing commas (such as --rrule, --exdate, or --categories) is specified, enclose the entire argument in " ".

**対応:** SSP 2.8.91

## 記述例

```sakurascript
\![execute,schedule-add,--uid=myghost-meeting,--summary=打ち合わせ,--start=20261001T1000,--end=20261001T1100,"--rrule=FREQ=WEEKLY;BYDAY=TH",--notify=10,--event=OnMyScheduleAdded]2026年10月1日から毎週木曜10時の予定を登録し、10分前に通知させる。
```

```sakurascript
\![execute,schedule-add,--summary=記念日,--start=20261224,--rrule=FREQ=YEARLY]毎年12月24日の終日予定を登録する。
```
