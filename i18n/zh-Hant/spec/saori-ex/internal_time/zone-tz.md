# Zone (--tz=)

- **local**: (default) The OS time zone. Daylight saving time for the specified date and time is applied.
- **UTC / Z**: UTC.
- **+09:00 / +0900 / +09**: Offset from UTC (up to ±18:00).
- **Named zones**: An IANA time zone name (such as `Asia/Tokyo` or `America/New_York`) or a Windows time zone name (such as `Tokyo Standard Time`). Case is ignored. Daylight saving time for the specified date and time is applied.<br />
  Zone rules use the OS (Windows) time zone information. IANA names are mapped to Windows names using the Unicode CLDR mapping table. A name not available in the OS results in 400 (`invalid parameter`). It is not treated as UTC.

The rules for named zones are limited to the OS time zone information. For older rules not included in the OS information (often from before the 2000s), the rules for the earliest year available in the OS are used instead.

## Around daylight saving time transitions

When converting a zoned date and time (wall-clock time) to UTC (when reading an ISO 8601 date and time without a zone, or when calculating the result of adding `day` or more in [Add](internal_time.Add.md)), there are ambiguous times around daylight saving time transitions. For both `local` and named zones, the following rules apply regardless of whether the zone is west (negative offset) or east (positive offset). \[SSP 2.9.27\]

- **A time that occurs twice** (the day clocks go back at the end of daylight saving time): Use the earlier occurrence, that is, the time still on daylight saving time. For example, `2026-11-01T01:30` in `America/New_York` is `2026-11-01T01:30:00-04:00`.
- **A nonexistent time** (the day clocks go forward at the start of daylight saving time): Interpret it using the offset before the transition, so the result is the time after the clocks have advanced. For example, `2026-03-08T02:30` in `America/New_York` is `2026-03-08T03:30:00-04:00`, and `2026-03-29T02:30` in `Europe/Berlin` is `2026-03-29T03:30:00+02:00`.

Before \[SSP 2.9.26\], in zones with negative offsets, nonexistent times were shifted back by one hour (`02:30` in `America/New_York` became `01:30-05:00`). The choice of occurrence for times that occurred twice was also reversed between zones east and west of UTC.
