# Diff

**カテゴリ:** internal_time

以指定單位計算日期時間2－日期時間1，並傳回整數。小數部分會朝 0 的方向截斷。<br />
`day`以上的單位會依`--tz=`時區的曆法計算。例如，若日期時間2只有日期（當日 0 時），「還有幾天」會在`--tz=`時區跨日時減少 1。`month` / `year`會依曆月計算，傳回透過[Add](internal_time.Add.md)加算後不超過日期時間2的最大數量（從 1 月 31 日起算，平年為 2 月 28 日、閏年為 2 月 29 日的相同時間算 1 個月）。

- **Argument1**: 日期時間1
- **Argument2**: 日期時間2
- **Argument3**: 單位（與[Add](internal_time.Add.md)相同）
- **選項**: `--tz=`

## 記述例

```
Argument0: Diff
Argument1: 2026-12-20T10:00
Argument2: 2026-12-24
Argument3: day

→ Result: 3（3日と14時間なので3）
```

若要取得日曆日期之間的差值（「從今天起幾天後」），請將日期時間1也只指定日期（可用[Format](internal_time.Format.md)的`%Y-%m-%d`產生今天的日期）。

**対応:** SSP 2.9.13
