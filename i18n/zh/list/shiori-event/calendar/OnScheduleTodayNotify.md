# OnScheduleTodayNotify

**カテゴリ:** Calendar event

Occurs when the contents of “Today's schedule” in the baseware calendar change. *\[NOTIFY\]*<br />
For example, when the date changes, a schedule is added or deleted, or the results from a schedule sensor change. It does not occur if there is no change.<br />
This is sent to all running ghosts, not a specific ghost.

Reference0 and onward contain each item in the updated “Today's schedule.” Each Reference's contents are separated by byte value 1 (hereafter \[`\1`\]).<br />
If there are no remaining items, the event occurs with no References.

- **Reference0～**: Event [type](caption_scheduletype.md) \[`\1`\] Event content (caption) \[`\1`\] Additional data (subtitle) \[`\1`\] Script (script) \[`\1`\] Start date and time \[`\1`\] End date and time \[`\1`\]<br />
  References continue as Reference0, 1, 2, and so on, for each schedule. Note that a trailing separator \[`\1`\] is also appended.<br />
  The start and end dates and times use the comma-separated format “year,month,day,hour,minute,second.” For schedules without a time set, hour, minute, and second are empty, as in “2026,9,10,,,”.<br />
  The end date and time are included only for schedules with an end time set. Otherwise, they are empty.<br />
  caption, subtitle, and script are the exact strings registered in the baseware calendar; no escaping for Sakura Script is performed.

**対応:** SSP 2.8.90
