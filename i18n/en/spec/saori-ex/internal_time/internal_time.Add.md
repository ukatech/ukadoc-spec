# Add

**カテゴリ:** internal_time

Returns the date-time obtained by adding an amount to a date-time, in epoch seconds. The amount may be negative.<br />
`second` / `minute` / `hour` are added as elapsed time. `day` and larger units are added using the calendar in the `--tz=` zone (so the time remains the same even when crossing a daylight saving transition).<br />
Dates are clamped to the end of the month (January 31 + 1 month = February 28 or 29).<br />
If the result is a nonexistent time during a daylight saving transition (a time skipped when the clock moves forward), it becomes the time after the transition. If the result is a time that occurs twice, the earlier one is used (see [Before and after daylight saving transitions](zone-tz.md#夏時間の切り替えの前後)).

- **Argument1**: Date-time
- **Argument2**: Amount (integer)
- **Argument3**: Unit: `second` `minute` `hour` `day` `week` `month` `year` (plural forms such as `days` are also allowed)
- **Options**: `--tz=`

**対応:** SSP 2.9.13
