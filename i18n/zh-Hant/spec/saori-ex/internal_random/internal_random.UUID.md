# UUID

**カテゴリ:** internal_random

Return a UUID (RFC 9562) in lowercase canonical form (`xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`).<br />
Version 4 is entirely random. For version 7, the first 48 bits are the current time (UNIX time in milliseconds), making UUIDs easier to sort in creation order (the order within the same millisecond is not guaranteed).

- **オプション**: `--version=4` (default) / `--version=7` (any other value returns 400 `invalid parameter`)

**対応:** SSP 2.9.13
