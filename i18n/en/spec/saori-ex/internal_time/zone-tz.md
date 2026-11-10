# Zone (--tz=)

- **local**: (default) The OS time zone. Applies daylight saving time for the given date and time.
- **UTC / Z**: UTC.
- **+09:00 / +0900 / +09**: Offset from UTC (up to ±18:00).
- **Named zones**: An IANA time zone name (such as `Asia/Tokyo` or `America/New_York`) or a Windows time zone name (such as `Tokyo Standard Time`). Case-insensitive. Applies daylight saving time for the given date and time.<br />
  Zone rules use the OS (Windows) time zone information. IANA names are mapped to Windows names using the Unicode CLDR mapping table. A name not available on the OS returns 400 (`invalid parameter`). It is not treated as UTC.

Rules for named zones are limited to the scope of the OS time zone information. For historical rules not included in the OS information (often those from before the 2000s), the rules for the earliest year available on the OS are used instead.

## Before and after daylight saving time transitions

When converting a zoned date and time (wall-clock time) to UTC (when reading a zone-less ISO 8601 date and time, or when calculating the result of adding `day` or a larger unit in [Add](internal_time.Add.md)), times around daylight saving time transitions can be ambiguous. For both `local` and named zones, regardless of whether the zone is west (negative offset) or east (positive offset), the following rules apply. \[SSP 2.9.27\]

- **A time that occurs twice** (the day the clock goes back at the end of daylight saving time): Use the earlier occurrence, that is, the time still in daylight saving time. For example, `2026-11-01T01:30` in `America/New_York` is `2026-11-01T01:30:00-04:00`.
- **A nonexistent time** (the day the clock moves forward at the start of daylight saving time): Interpret it using the pre-transition offset, resulting in a time after the transition. For example, `2026-03-08T02:30` in `America/New_York` is `2026-03-08T03:30:00-04:00`, and `2026-03-29T02:30` in `Europe/Berlin` is `2026-03-29T03:30:00+02:00`.

Before \[SSP 2.9.26\], in zones with a negative offset, a nonexistent time was moved back by one hour (`02:30` in `America/New_York` became `01:30-05:00`). The choice of occurrence for times that happened twice was also reversed between zones east and west of UTC.
