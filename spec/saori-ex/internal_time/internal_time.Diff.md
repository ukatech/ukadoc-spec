# Diff

**カテゴリ:** internal_time

日時2－日時1を、単位で数えた整数で返す。端数は0の方向へ切り捨てる。<br />
`day`以上は`--tz=`のゾーンの暦で数える。たとえば日時2が日付だけ（その日の0時）なら、「あと何日」は`--tz=`のゾーンで日付が変わる時刻に1つ減る。`month` / `year`は暦の月で数え、[Add](internal_time.Add.md)で足して越えない最大の数を返す（1月31日からは、平年なら2月28日、うるう年なら2月29日の同じ時刻で1か月）。

- **Argument1**: 日時1
- **Argument2**: 日時2
- **Argument3**: 単位（[Add](internal_time.Add.md)と同じ）
- **オプション**: `--tz=`

## 記述例

```
Argument0: Diff
Argument1: 2026-12-20T10:00
Argument2: 2026-12-24
Argument3: day

→ Result: 3（3日と14時間なので3）
```

カレンダーの日付どうしの差（「今日から何日後か」）がほしいときは、日時1も日付だけにしてください（[Format](internal_time.Format.md)の`%Y-%m-%d`で今日の日付を作れる）。

**対応:** SSP 2.9.13
