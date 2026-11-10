# Format

**カテゴリ:** internal_time

Formats a date-time in the `--tz=` zone. Weekday and month names are fixed in English (independent of language and regional settings).

- **Argument1**: Date-time
- **Argument2**: Format (defaults to `iso8601` if omitted or empty)
- **Options**: `--tz=`

The format can be one of the following names or a format using `%`. An unknown format name or `%` character results in 400 (`invalid parameter`).

- **iso8601 / rfc3339**: `2026-10-11T21:00:00+09:00`. If the offset is 0, the suffix is `Z`.
- **http**: `Sun, 11 Oct 2026 12:00:00 GMT`. Always uses GMT, regardless of `--tz=`.
- **epoch / epochms**: Epoch seconds / epoch milliseconds.
- **% format**: `%Y` (four-digit year) `%y` (two-digit year) `%m` (month) `%d` (day) `%H` (hour) `%M` (minute) `%S` (second) `%j` (day of year) `%u` (weekday, Monday=1 to Sunday=7) `%w` (weekday, Sunday=0 to Saturday=6) `%a` (Sun) `%A` (Sunday) `%b` (Jan) `%B` (January) `%z` (+0900) `%:z` (+09:00) `%s` (epoch seconds) `%%` (%).<br />
  Characters other than `%` are output as-is.

## 記述例

```
Argument0: Format
Argument1: 0
Argument2: %Y/%m/%d %H:%M (%a)
Argument3: --tz=+09:00

→ Result: 1970/01/01 09:00 (Thu)
```

**対応:** SSP 2.9.13
