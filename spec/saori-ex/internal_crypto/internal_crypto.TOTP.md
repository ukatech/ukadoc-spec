# TOTP

**カテゴリ:** internal_crypto

時刻ベースのワンタイムパスワード（RFC 6238。2段階認証のアプリが出す数字）を求める。桁数に満たなければ先頭を0で埋める。

- **Argument1**: key（既定の形式は`base32`。認証アプリに登録する秘密鍵の文字列）
- **オプション**: `--key-in=` / `--digits=`（既定は6。6～10） / `--period=`（秒。既定は30。1～86400） / `--digest=`（既定は`sha1`。`md5`は使えない） / `--time=`（日時。[internal_time](../internal_time/index.md)の日時の引数と同じ書き方で、ゾーンの無いものはOSのタイムゾーンの時刻。既定は現在時刻） / `--charset=`

## 記述例

```
Argument0: TOTP
Argument1: GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ
Argument2: --time=59
Argument3: --digits=8

→ Result: 94287082
```

**対応:** SSP 2.9.13
