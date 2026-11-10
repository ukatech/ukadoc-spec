# UUID

**カテゴリ:** internal_random

以小寫標準格式（`xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`）回傳 UUID（RFC 9562）。<br />
版本4的整體內容皆為隨機值。版本7的前48位元是目前時間（UNIX 時間的毫秒），便於依建立順序排列（不保證同一毫秒內的順序）。

- **オプション**: `--version=4`（預設） / `--version=7`（其他值回傳 400 `invalid parameter`）

**対応:** SSP 2.9.13
