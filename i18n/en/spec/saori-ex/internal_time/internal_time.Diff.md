# Diff

**カテゴリ:** internal_time

Returns the integer difference between date-time 2 and date-time 1, counted in the specified unit. Fractions are truncated toward zero.<br />
`day` and larger units are counted using the calendar in the `--tz=` zone. For example, if date-time 2 is specified as a date only (midnight that day), the number of days remaining decreases by one at midnight in the `--tz=` zone. `month` / `year` are counted in calendar months; the result is the largest number that can be added with [Add](internal_time.Add.md) without passing date-time 2 (from January 31, one month later is the same time on February 28 in a common year, or February 29 in a leap year).

- **Argument1**: Date-time 1
- **Argument2**: Date-time 2
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

If you need the difference between calendar dates (that is, “how many days from today”), specify date-time 1 as a date only as well (you can create today's date with `%Y-%m-%d` in [Format](internal_time.Format.md)).

**対応:** SSP 2.9.13
