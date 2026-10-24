# Add

**カテゴリ:** internal_time

日時に量を足した日時を、エポック秒で返す。量は負でもよい。<br />
`second` / `minute` / `hour`は経過時間で足す。`day`以上は`--tz=`のゾーンの暦で足す（夏時間の切り替えをまたいでも同じ時刻になる）。<br />
月末は丸める（1月31日＋1か月＝2月28日または29日）。

- **Argument1**: 日時
- **Argument2**: 量（整数）
- **Argument3**: 単位：`second` `minute` `hour` `day` `week` `month` `year`（複数形の`days`なども可）
- **オプション**: `--tz=`

**対応:** SSP 2.9.13
