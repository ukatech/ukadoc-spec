# OnExecuteICalComplete

**カテゴリ:** Other communication events

Occurs when retrieval and parsing complete successfully with [`\![execute,ical-get/ical-post]`](../../sakura-script/misc/bang-execute-ical-get-URL.md).

Reference0 contains information for the entire calendar, and Reference1 onward contain one event each. The fields within each Reference are separated by byte value 1 (hereafter \[`\1`\]).<br />
The number of events and which ones are included are determined by the [iCal filtering options](../../sakura-script/misc/bang-execute-ical-post-URL.note.md).

- **Reference0**: Calendar name (X-WR-CALNAME) \[`\1`\] Time zone (X-WR-TIMEZONE) \[`\1`\] Calendar scale (CALSCALE; usually GREGORIAN) \[`\1`\] Number of events returned by this event \[`\1`\] Total number of events in the file \[`\1`\] Start date of filtering period \[`\1`\] End date of filtering period<br />
  The start and end dates of the period use the format "year,month,day,,, ". If none of --from, --to, --expand, or --limit are specified, these fields are empty.
- **Reference1～**: UID \[`\1`\] Start date and time \[`\1`\] End date and time \[`\1`\] Title (SUMMARY) \[`\1`\] Description (DESCRIPTION) \[`\1`\] Location (LOCATION) \[`\1`\] URL \[`\1`\] Status (STATUS) \[`\1`\] Categories (CATEGORIES) \[`\1`\] Recurrence rule (original RRULE text) \[`\1`\] All-day flag \[`\1`\] Occurrence date<br />
  Reference1, 2, 3, etc. continue for each event.<br />
  Start date and time, end date and time, and occurrence date use the same comma-separated format as RSS: "year,month,day,hour,minute,second". For all-day events, hour, minute, and second are empty, so the value looks like "2026,9,10,,, ".<br />
  The end date and time is the final date of the event (since the DTEND date value is exclusive, the value is one day earlier). For events that specify duration with DURATION instead of DTEND, the duration is added to the start date and time (for all-day events, the value is likewise one day earlier).<br />
  If there are multiple categories, they are comma-separated. Commas within category names are not distinguished from separator commas.<br />
  The all-day flag is 1 for all-day events and 0 for events with a time.<br />
  The occurrence date is included only when one of --from, --to, or --expand is specified. With --expand, it is the occurrence date for the expanded instance; without --expand, it is the first occurrence within the period. If none is specified, the field is empty.<br />
  RRULE is passed through as-is, so you can interpret it yourself without using SSP's expansion.<br />
  Titles, descriptions, locations, URLs, categories, and calendar names are escaped so they are not interpreted as Sakura Script (\\→\\\\, %→\\%, newlines and tabs→half-width spaces).

**対応:** SSP 2.8.90
