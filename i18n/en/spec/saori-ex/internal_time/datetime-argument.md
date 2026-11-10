# Date-time arguments

A date-time argument must be written in one of the following forms. If it cannot be parsed as any of them, the result is 400 (`invalid parameter`). Nonexistent dates (such as February 30) also result in 400.

- **Integer**: Epoch seconds. Negative values (before 1970) are allowed.
- **now**: The current time.
- **ISO 8601**: Examples: `2026-10-11`, `2026-10-11T21:00:00+09:00`, `2026-10-11 21:00`, and `20261011T210000Z`. Fractional seconds are discarded.<br />
  Values without a zone (`Z` or `+09:00`) are interpreted as times in the `--tz=` zone. For how times during daylight saving transitions—times that occur twice or do not exist—are handled, see [Zones](zone-tz.md#夏時間の切り替えの前後).
- **HTTP date**: Examples: `Sun, 11 Oct 2026 12:00:00 GMT`.

The supported range is 0001-01-01 to 9999-12-31 in UTC (from 1601 onward when `--tz=local`). Values outside this range result in 400 (`out of range`).<br />
However, ISO 8601 and HTTP date strings can only represent dates from 1601 onward (earlier dates result in 400 `invalid parameter`; they can be specified as integer epoch seconds).<br />
The range is determined in UTC, so formatting dates near 9999-12-31 in an eastern zone (such as `+09:00`) may produce a five-digit year, 10000.
