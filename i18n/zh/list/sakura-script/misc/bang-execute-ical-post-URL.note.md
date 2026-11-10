# iCal filtering options \[2.8.90\]

Options for specifying which events to return from the retrieved calendar with [`\![execute,ical-get/ical-post]`](bang-execute-ical-get-URL.md).<br />
\[2.8.92\] Options with the same names can also be used with rss-get/rss-post, but their behavior when omitted differs (see [RSS filtering options](bang-execute-rss-post-URL.note.md)). They are ignored for other requests.

Writing any of --from, --to, --expand, or --limit enables “period mode”, which returns only events that occur during the period. If only --limit is specified, the period starts from today.<br />
If none are specified, all VEVENTs in the file are returned as-is, in order from the beginning (with no filtering by period and no limit on the number of events).

- **Setting the period**: The start date is the date specified by --from, or today if omitted.<br />
  The end date is the date specified by --to (inclusive). If --to is omitted, the period is the number of days specified by --expand if it has a number of days; otherwise it is 30 days if --expand is present, or 1830 days if --expand is absent.<br />
  The period is capped at 1830 days (if it is longer, it is cut off at 1830 days). If --to is earlier than --from, the period is empty and no events are returned.
- **With --expand (per occurrence)**: Expand RRULE repetitions one occurrence at a time and return one Reference per occurrence. Results are sorted by date in ascending order.<br />
  If the same event occurs multiple times during the period, a Reference is returned for each occurrence.
- **Without --expand (per VEVENT)**: Return one event per VEVENT that occurs at least once during the period. Results are sorted by the date of their first occurrence within the period (and by start date and time when dates are the same).<br />
  In this case, the “occurrence date” in each Reference is the date of the first occurrence within the period.
- **Maximum number of events**: Stop when the number specified by --limit is reached. The default in period mode is 200; --limit=0 means unlimited.<br />
  There is no limit outside period mode (when no options are specified).
- **Determining occurrence dates**: RRULE (FREQ, INTERVAL, COUNT, UNTIL, BYDAY, BYMONTHDAY, BYMONTH) and EXDATE are interpreted to determine occurrence dates.<br />
  For an event that spans multiple days from DTSTART through DTEND (or, if the event specifies its duration with DURATION instead of DTEND, through its end), all those days are considered occurrence dates.<br />
  Dates listed in EXDATE are treated as non-occurrences, regardless of whether the event repeats.
