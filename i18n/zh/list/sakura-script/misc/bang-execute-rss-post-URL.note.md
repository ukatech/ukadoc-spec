# RSS filtering options \[2.8.92\]

Options that specify which items to return from a retrieved feed using [`\![execute,rss-get/rss-post]`](bang-execute-rss-get-URL.md).<br />
The syntax is the same as for [iCal filtering options](bang-execute-ical-post-URL.note.md), but the behavior when omitted is different. --expand is ignored.

If none are specified, all items are returned.

- **Date range (--from, --to)**: --from=yyyymmdd returns items with an update timestamp at or after midnight (00:00:00) on that date; --to=yyyymmdd returns items with an update timestamp up to the end of that date (inclusive). Dates are evaluated using the local date of the execution environment.<br />
  The omitted side has no limit (unlike iCal, the range does not start from the current date). A nonexistent date is treated the same as an omitted option. If --to is earlier than --from, no items are returned.<br />
  If either --from or --to is specified, items without an update timestamp (or with an unparseable timestamp) are not returned.
- **Maximum number of items (--limit)**: When specified, processing stops once that number of items has been reached. --limit=0 means unlimited.<br />
  Unlike iCal, there is no default limit (200 items), and specifying only --limit does not filter by date range.<br />
  Items are sorted by newest update timestamp first, so --limit=5 returns the latest five items (if no items in the feed have an update timestamp, it returns the first five in feed order).
