# OnSchedulesenseComplete

**カテゴリ:** Calendar event

Occurs when a schedule sensor finishes processing.<br />
This event is sent to all running ghosts, not to a specific ghost.

**Occurs only during a manual update.** As [described below](caption_schedulesensetiming.md), it does not occur during periodic checks.<br />
This event also occurs on success when data was retrieved but nothing changed (for example, 304 Not Modified or identical content).

- **Reference0**: Schedule sensor name
- **Reference1**: Number of schedule entries returned by the schedule sensor

**対応:** SSP
