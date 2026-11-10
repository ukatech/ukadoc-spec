# OnSchedulesenseComplete

**カテゴリ:** Calendar event

Occurs when the schedule sensor finishes processing.<br />
This is sent to all running ghosts, not a specific ghost.

**Occurs only during a manual update.** It does not occur during periodic checks, as [described below](caption_schedulesensetiming.md).<br />
This event also occurs as a success when the data was retrieved but there were no updates (304 Not Modified or the contents were identical).

- **Reference0**: Schedule sensor name
- **Reference1**: Number of schedule items returned by the schedule sensor

**対応:** SSP
