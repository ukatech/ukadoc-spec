# TOTP

**カテゴリ:** internal_crypto

计算基于时间的一次性密码（RFC 6238；即双重认证应用生成的数字）。位数不足时在前面补0。

- **Argument1**: key（默认格式为`base32`。要在认证应用中注册的密钥字符串）
- **选项**: `--key-in=` / `--digits=`（默认值为6。范围为6～10） / `--period=`（秒。默认值为30。范围为1～86400）（超出范围时返回400 `out of range`） / `--digest=`（默认值为`sha1`。不能使用`md5`，会返回400 `unsupported algorithm`） / `--time=`（日期时间。写法与[internal_time](../internal_time/index.md)的日期时间参数相同；未指定时区的值按OS时区的时间处理。默认值为当前时间） / `--charset=`

## 記述例

```
Argument0: TOTP
Argument1: GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ
Argument2: --time=59
Argument3: --digits=8

→ Result: 94287082
```

**対応:** SSP 2.9.13
