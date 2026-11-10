# RSS Filtering Options \[2.8.92\]

These options specify which items to return from the retrieved feed with [`\![execute,rss-get/rss-post]`](bang-execute-rss-get-URL.md).<br />
The syntax is the same as for the [iCal filtering options](bang-execute-ical-post-URL.note.md), but the behavior when omitted is different. --expand is ignored.

If none are specified, all items are returned.

- **Period (--from and --to)**: --from=yyyymmdd returns items with an update date and time at or after 00:00:00 on that date, and --to=yyyymmdd returns items with an update date and time up to the end of that date (inclusive). Dates are evaluated using the local date in the execution environment.<br />
  An omitted bound is unrestricted (unlike iCal, it does not default to the current day). A nonexistent date is treated the same as an omitted value. If --to is earlier than --from, no items are returned.<br />
  If either --from or --to is specified, items without an update date and time (or whose date and time cannot be interpreted) are not returned.
- **Maximum number of items (--limit)**: Only when specified, stop once that number of items has been reached. --limit=0 means unlimited.<br />
  Unlike iCal, there is no default limit of 200 items, and specifying only --limit does not filter by period.<br />
  Items are sorted by update date and time, newest first, so --limit=5 returns the latest 5 items (if no items in the feed have an update date and time, it returns the first 5 in the order listed in the feed).
