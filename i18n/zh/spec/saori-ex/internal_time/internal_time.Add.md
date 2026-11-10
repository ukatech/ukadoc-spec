# Add

**カテゴリ:** internal_time

Returns the date and time obtained by adding an amount to a date and time, as epoch seconds. The amount may be negative.<br />
`second` / `minute` / `hour` are added as elapsed time. `day` and larger units are added using the calendar in the zone specified by `--tz=` (the local time remains the same across daylight saving time transitions).<br />
Month ends are clamped (January 31 + 1 month = February 28 or 29).<br />
If the result falls at a time that does not exist due to a daylight saving time transition (a time skipped when the clock moves forward), it becomes the next valid time. If the result falls at a time that occurs twice, the earlier occurrence is used (see [Around daylight saving time transitions](zone-tz.md#夏時間の切り替えの前後)).

- **Argument1**: Date and time
- **Argument2**: Amount (integer)
- **Argument3**: Unit: `second` `minute` `hour` `day` `week` `month` `year` (plural forms such as `days` are also accepted)
- **Options**: `--tz=`

**対応:** SSP 2.9.13
