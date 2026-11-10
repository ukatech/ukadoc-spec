# OnSchedulesenseFailure

**カテゴリ:** Calendar event

Occurs when a schedule sensor fails to process.<br />
This event is sent to all running ghosts, not to a specific ghost.

Unlike Begin/Complete, this event [also occurs during periodic checks](caption_schedulesensetiming.md).

- **Reference0**: [Reason for failure](../headline-rss/caption_headlinesenseresult.md) (shared with the headline sensor). If data could not be retrieved, the value is can't download; if data was retrieved but could not be parsed as iCal, the value is can't analyze.
- **Reference1**: Schedule sensor name. During periodic checks, Begin does not occur, so without this value it would be impossible to tell which sensor failed.

**対応:** SSP
