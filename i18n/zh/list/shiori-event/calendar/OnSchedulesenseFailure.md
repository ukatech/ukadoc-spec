# OnSchedulesenseFailure

**カテゴリ:** Calendar event

Occurs when schedule sensor processing fails.<br />
This is sent to all running ghosts, not a specific ghost.

Unlike Begin/Complete, this [also occurs during periodic checks](caption_schedulesensetiming.md).

- **Reference0**: [Reason for failure](../headline-rss/caption_headlinesenseresult.md) (shared with headline sensors). If the data could not be retrieved, the reason is can't download; if it was retrieved but could not be parsed as iCal, the reason is can't analyze.
- **Reference1**: Schedule sensor name. Since there is no Begin event during periodic checks, this is needed to identify which sensor failed.

**対応:** SSP
