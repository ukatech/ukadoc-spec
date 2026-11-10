# OnScheduleTodayNotify

**カテゴリ:** Calendar event

Occurs when the contents of “Today's schedule” in the built-in calendar change. *\[NOTIFY\]*<br />
For example, when the date changes, a schedule is added or deleted, or the results from the schedule sensor change. It does not occur if there is no change.<br />
This is sent to all running ghosts, not to a specific ghost.

Reference0 onward each contain one item from the updated “Today's schedule.” The contents of each Reference are separated by byte value 1 (hereafter \[`\1`\]).<br />
If there are no remaining schedule items, the event occurs with no References.

- **Reference0～**: Event [type](caption_scheduletype.md) \[`\1`\] Event content (caption) \[`\1`\] Additional data (subtitle) \[`\1`\] Script (script) \[`\1`\] Start date and time \[`\1`\] End date and time \[`\1`\]<br />
  References continue as Reference0, 1, 2, and so on, for the number of schedules. Note that a delimiter \[`\1`\] is also appended at the end.<br />
  Start and end dates and times use the comma-separated format “year,month,day,hour,minute,second.” For schedules with no time set, hour, minute, and second are empty, as in “2026,9,10,,,.”<br />
  The end date and time are included only for schedules with an end time set. Otherwise, they are empty.<br />
  caption, subtitle, and script are the strings registered in the built-in calendar, unchanged; no escaping for Sakura Script is performed.

**対応:** SSP 2.8.90
