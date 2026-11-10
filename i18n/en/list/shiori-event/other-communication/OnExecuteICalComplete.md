# OnExecuteICalComplete

**カテゴリ:** Other communication events

Occurs when [`\![execute,ical-get/ical-post]`](../../sakura-script/misc/bang-execute-ical-get-URL.md) successfully completes retrieval and parsing.

Reference0 contains information about the calendar as a whole; Reference1 onward contain one event each. Values within each Reference are separated by byte value 1 (hereafter \[`\1`\]).<br />
The number and order of events depends on the [iCal filtering options](../../sakura-script/misc/bang-execute-ical-post-URL.note.md).

- **Reference0**: Calendar name (X-WR-CALNAME) \[`\1`\] time zone (X-WR-TIMEZONE) \[`\1`\] calendar scale (CALSCALE; usually GREGORIAN) \[`\1`\] number of events returned by this event \[`\1`\] total number of events in the file \[`\1`\] start date of the filtering period \[`\1`\] end date of the filtering period<br />
  The start and end dates of the period use the format "year,month,day,,,", and are empty if none of --from, --to, --expand, or --limit was specified.
- **Reference1～**: UID \[`\1`\] start date and time \[`\1`\] end date and time \[`\1`\] title (SUMMARY) \[`\1`\] description (DESCRIPTION) \[`\1`\] location (LOCATION) \[`\1`\] URL \[`\1`\] status (STATUS) \[`\1`\] categories (CATEGORIES) \[`\1`\] recurrence rule (original RRULE text) \[`\1`\] all-day flag \[`\1`\] occurrence date<br />
  References continue as Reference1, 2, 3, etc., for each event.<br />
  Start date and time, end date and time, and occurrence date use the same comma-separated format as RSS: "year,month,day,hour,minute,second". For all-day events, hour, minute, and second are empty, as in "2026,9,10,,,".<br />
  The end date and time is the final day of the event (since the DTEND date value is exclusive, the returned value is one day earlier). For events that specify a duration with DURATION instead of DTEND, the duration is added to the start date and time (for all-day events, the returned value is likewise one day earlier).<br />
  If there are multiple categories, they are comma-separated. Commas in category names are not distinguished from separator commas.<br />
  The all-day flag is 1 for all-day events and 0 for events with a time.<br />
  The occurrence date is included only when one of --from, --to, or --expand is specified. With --expand, it is the occurrence date for the expanded instance; without --expand, it is the first occurrence date within the period. It is empty if none is specified.<br />
  RRULE is passed through unchanged, so you can interpret it yourself without using SSP's expansion.<br />
  Titles, descriptions, locations, URLs, categories, and calendar names are escaped so they are not interpreted as Sakura Script (\\→\\\\、%→\\%、newlines and tabs→half-width spaces).

**対応:** SSP 2.8.90
