# OnExecuteScheduleGetComplete

**カテゴリ:** Other communication events

Occurs when the ghost's schedule is read via [`\![execute,schedule-get]`](../../sakura-script/misc/bang-execute-schedule-get.md).

If an ID starting with On is specified with --event, that ID becomes the event name.

- **Reference0～**: [Same as OnExecuteICalComplete](OnExecuteICalComplete.md).<br />
  Only the ghost's schedule is included; user-registered schedules and schedule sensor entries are not included.

**対応:** SSP 2.8.91
