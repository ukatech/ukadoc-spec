# TOTP

**カテゴリ:** internal_crypto

Generates a time-based one-time password (RFC 6238; the number displayed by two-factor authentication apps). If the result has fewer than the specified number of digits, it is padded with leading zeroes.

- **Argument1**: key (default format is `base32`; the secret key string to register in an authentication app)
- **Options**: `--key-in=` / `--digits=` (default is 6; 6–10) / `--period=` (seconds; default is 30; 1–86400) (values outside the range result in 400 `out of range`) / `--digest=` (default is `sha1`; `md5` is not available and results in 400 `unsupported algorithm`) / `--time=` (date and time. Use the same format as the date/time argument in [internal_time](../internal_time/index.md); values without a zone are interpreted in the OS time zone. Defaults to the current time) / `--charset=`

## 記述例

```
Argument0: TOTP
Argument1: GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ
Argument2: --time=59
Argument3: --digits=8

→ Result: 94287082
```

**対応:** SSP 2.9.13
