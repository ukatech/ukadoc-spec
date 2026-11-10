# OnScheduleTodayNotify

**カテゴリ:** Calendar event

Occurs when the contents of “Today's schedule” in the baseware calendar change. *\[NOTIFY\]*<br />
Examples include when the date changes, a schedule is added or deleted, or the results retrieved by the schedule sensor change. It does not occur if nothing changes.<br />
This event is sent to all running ghosts, not to a specific ghost.

Reference0 and subsequent references each contain one item from the updated “Today's schedule.” Each Reference is delimited by byte value 1 (hereafter \[`\1`\]).<br />
If there are no remaining schedules, the event occurs with no References.

- **Reference0～**: Event [type](caption_scheduletype.md) \[`\1`\] Event content (caption) \[`\1`\] Additional data (subtitle) \[`\1`\] Script (script) \[`\1`\] Start date and time \[`\1`\] End date and time \[`\1`\]<br />
  The references continue as Reference0, 1, 2, and so on, for each schedule. Note that a delimiter \[`\1`\] is also appended at the end.<br />
  The start and end dates and times use the comma-separated format “year,month,day,hour,minute,second.” For schedules without a set time, the hour, minute, and second are empty, as in “2026,9,10,,,.”<br />
  The end date and time are included only for schedules with a set end time. Otherwise, they are empty.<br />
  caption, subtitle, and script are the exact strings registered in the baseware calendar; no escaping for Sakura Script is performed.

**対応:** SSP 2.8.90
