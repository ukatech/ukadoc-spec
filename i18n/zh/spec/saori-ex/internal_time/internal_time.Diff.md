# Diff

**カテゴリ:** internal_time

Returns the integer difference between date and time 2 and date and time 1, counted in the specified unit. Fractions are truncated toward zero.<br />
`day` and larger units are counted using the calendar in the zone specified by `--tz=`. For example, if date and time 2 is a date only (midnight on that day), the number of days remaining decreases by one at midnight in the `--tz=` zone. `month` / `year` are counted as calendar months, returning the largest number that can be added using [Add](internal_time.Add.md) without exceeding the target (from January 31, one month is the same time on February 28 in a common year, or February 29 in a leap year).

- **Argument1**: Date and time 1
- **Argument2**: Date and time 2
- **Argument3**: Unit (same as [Add](internal_time.Add.md))
- **Options**: `--tz=`

## 記述例

```
Argument0: Diff
Argument1: 2026-12-20T10:00
Argument2: 2026-12-24
Argument3: day

→ Result: 3（3日と14時間なので3）
```

To get the difference between calendar dates (how many days from today), specify date only for date and time 1 as well (you can create today's date using `%Y-%m-%d` in [Format](internal_time.Format.md)).

**対応:** SSP 2.9.13
