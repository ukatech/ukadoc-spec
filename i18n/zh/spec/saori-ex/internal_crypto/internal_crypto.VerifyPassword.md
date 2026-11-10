# VerifyPassword

**カテゴリ:** internal_crypto

检查密码是否与 PHC 字符串匹配；匹配时返回`1`，否则返回`0`。参数从 PHC 字符串中读取。推荐使用[`--async`](../async.md)。<br />
除[HashPassword](internal_crypto.HashPassword.md)的输出外，也可以读取其他实现生成的同格式字符串（`$argon2id$`（可以没有`v=`或使用`v=16`） / `$scrypt$` / `$pbkdf2-sha1$` / `$pbkdf2-sha256$` / `$pbkdf2-sha512$`）。但参数超出内存上限（12MiB）的字符串（例如 argon2-cffi 默认的 64MiB）无法用于验证，会返回 400（`out of range`）。<br />
\[SSP 2.9.23\] 也可以读取 crypt(3) 格式（`$2a$` / `$2b$` / `$2y$`（bcrypt。三者处理方式相同） / `$6$` / `$5$`（可以没有`rounds=`，也可以将小于 1000 的值向上调整为 1000） / `$1$` / `$apr1$` / 以`_`开头的 20 个字符（BSDi 扩展 DES） / 13 个字符（传统 DES））。bcrypt 的成本最多为 16，SHA-crypt 的`rounds=`最多为 10000000；超出时会返回 400（`out of range`）。不支持`$2x$`和`$2$`。<br />
其他算法会返回 400（`unsupported algorithm`），格式错误会返回 400（`invalid parameter`），参数超出[DeriveKey](internal_crypto.DeriveKey.md)的范围时会返回 400（`out of range`。scrypt 的`ln=`必须在 1～62 之间，否则会返回此错误）。pbkdf2 的`l=`与哈希长度不一致时，也会作为格式错误返回 400（`invalid parameter`）。

- **Argument1**: password（默认格式为`text`）
- **Argument2**: PHC 字符串（\[SSP 2.9.23\] 或 crypt(3) 格式的字符串）
- **选项**: `--password-in=` / `--charset=`

**対応:** SSP 2.9.13
