# UUID

**カテゴリ:** internal_random

以小写规范形式（`xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`）返回 UUID（RFC 9562）。<br />
版本 4 的整体内容为随机值。版本 7 的前 48 位是当前时间（UNIX 时间的毫秒数），便于按创建顺序排列（不保证同一毫秒内的顺序）。

- **オプション**：`--version=4`（默认值） / `--version=7`（其他值均返回 400 `invalid parameter`）

**対応:** SSP 2.9.13
