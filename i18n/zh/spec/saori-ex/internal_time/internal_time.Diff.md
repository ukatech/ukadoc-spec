# Diff

**カテゴリ:** internal_time

返回以指定单位计算的日期时间2－日期时间1的整数。小数部分向0方向舍去。<br />
`day`及以上单位按`--tz=`时区的日历计算。例如，日期时间2只有日期（当天0时）时，“还有几天”会在`--tz=`时区日期变更的时刻减1。`month` / `year`按日历月计算，并返回使用[Add](internal_time.Add.md)递增且不会超过日期时间2的最大数值（从1月31日开始，平年时为2月28日、闰年时为2月29日的同一时刻算作1个月）。

- **Argument1**: 日期时间1
- **Argument2**: 日期时间2
- **Argument3**: 单位（与[Add](internal_time.Add.md)相同）
- **选项**: `--tz=`

## 記述例

```
Argument0: Diff
Argument1: 2026-12-20T10:00
Argument2: 2026-12-24
Argument3: day

→ Result: 3（3日と14時間なので3）
```

如果需要计算日历日期之间的差值（“从今天起几天后”），请将日期时间1也设为仅日期（可通过[Format](internal_time.Format.md)的`%Y-%m-%d`生成今天的日期）。

**対応:** SSP 2.9.13
