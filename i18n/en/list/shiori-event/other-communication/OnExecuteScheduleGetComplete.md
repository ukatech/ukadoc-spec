# OnExecuteScheduleGetComplete

**カテゴリ:** Other communication events

Occurs when the ghost's schedule is read using [`\![execute,schedule-get]`](../../sakura-script/misc/bang-execute-schedule-get.md).

If an ID beginning with On is specified with --event, that ID becomes the event name.

- **Reference0～**: [Same as OnExecuteICalComplete](OnExecuteICalComplete.md).<br />
  Only the ghost's schedule is included; user-added entries and entries from the schedule sensor are not included.

**対応:** SSP 2.8.91
