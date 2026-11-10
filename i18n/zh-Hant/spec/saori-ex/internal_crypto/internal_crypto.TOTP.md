# TOTP

**カテゴリ:** internal_crypto

計算以時間為基礎的一次性密碼（RFC 6238；即雙重驗證應用程式產生的數字）。若位數不足，會在前面補 0。

- **Argument1**: key（預設格式為`base32`。登記至驗證應用程式的密鑰字串）
- **選項**: `--key-in=` / `--digits=`（預設為 6。6～10） / `--period=`（秒。預設為 30。1～86400）（超出範圍時回傳 400 `out of range`） / `--digest=`（預設為`sha1`。不能使用`md5`，會回傳 400 `unsupported algorithm`） / `--time=`（日期時間。寫法與 [internal_time](../internal_time/index.md) 的日期時間引數相同；未指定時區的值會視為作業系統時區的時間。預設為目前時間） / `--charset=`

## 記述例

```
Argument0: TOTP
Argument1: GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ
Argument2: --time=59
Argument3: --digits=8

→ Result: 94287082
```

**対応:** SSP 2.9.13
