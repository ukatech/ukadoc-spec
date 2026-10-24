# UUID

**カテゴリ:** internal_random

UUID（RFC 9562）を小文字の正規の表記（`xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`）で返す。<br />
バージョン4は全体がランダム。バージョン7は先頭の48ビットが現在時刻（UNIX時刻のミリ秒）で、作った順に並べやすい（同じミリ秒の中での順序は保証しない）。

- **オプション**: `--version=4`（既定） / `--version=7`

**対応:** SSP 2.9.13
