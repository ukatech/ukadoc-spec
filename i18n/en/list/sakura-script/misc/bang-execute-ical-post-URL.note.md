# iCal filtering options \[2.8.90\]

In [`\![execute,ical-get/ical-post]`](bang-execute-ical-get-URL.md), options for specifying which events to return from the retrieved calendar.<br />
\[2.8.92\] The same options can also be used with rss-get/rss-post, but their behavior when omitted differs (see [RSS filtering options](bang-execute-rss-post-URL.note.md)). They are ignored for other requests.

Writing any of --from, --to, --expand, or --limit enables “date range mode”, which returns only events that occur within the date range. If only --limit is specified, date range mode starts from the current day.<br />
If none are specified, all VEVENTs in the file are returned as-is, in order from the first (with no date-range filtering or event-count limit).

- **Date range**: The start date is the date specified by --from, or the current day if omitted.<br />
  The end date is the date specified by --to (inclusive). If --to is omitted, the range is the number of days specified by --expand, if it has a number of days; 30 days if --expand is specified without a number of days; or 1830 days if --expand is not specified.<br />
  The range is limited to a maximum of 1830 days (if longer, it is truncated to 1830 days). If --to is earlier than --from, the range is empty and no events are returned.
- **With --expand (per occurrence)**: Expand RRULE recurrences one at a time and return one Reference per occurrence. Results are sorted by date in ascending order.<br />
  If the same event occurs multiple times within the date range, a Reference is returned for each occurrence.
- **Without --expand (per VEVENT)**: Return one item per VEVENT for each event that occurs at least once within the date range. Results are sorted by the date of the first occurrence within the range (for the same date, by start time).<br />
  In this case, each Reference's “occurrence date” is the date of the first occurrence within the date range.
- **Event-count limit**: Stop once the number of items specified by --limit is reached. The default in date range mode is 200; --limit=0 means no limit.<br />
  There is no limit outside date range mode (when no options are specified).
- **Determining occurrence dates**: RRULE (FREQ, INTERVAL, COUNT, UNTIL, BYDAY, BYMONTHDAY, BYMONTH) and EXDATE are interpreted to determine occurrences.<br />
  An event spanning multiple days from DTSTART through DTEND (or, if DTEND is absent, through the end specified by DURATION) is considered to occur on every day in that span.<br />
  Dates listed in EXDATE are treated as non-occurrences, regardless of whether the event recurs.
