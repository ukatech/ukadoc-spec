# VerifyPassword

**カテゴリ:** internal_crypto

Checks whether a password matches a PHC string, returning `1` if it does and `0` otherwise. Parameters are read from the PHC string. [`--async`](../async.md) is recommended.<br />
In addition to output from [HashPassword](internal_crypto.HashPassword.md), strings produced by other implementations can also be read if they have the same format (`$argon2id$` (with no `v=` or with `v=16`) / `$scrypt$` / `$pbkdf2-sha1$` / `$pbkdf2-sha256$` / `$pbkdf2-sha512$`). However, parameters that exceed the memory limit (12MiB), such as argon2-cffi's default of 64MiB, cannot be verified and return 400 (`out of range`).<br />
\[SSP 2.9.23\] crypt(3) formats can also be read (`$2a$` / `$2b$` / `$2y$` (bcrypt; all three are treated identically) / `$6$` / `$5$` (with no `rounds=` or with values below 1000 rounded up to 1000) / `$1$` / `$apr1$` / 20 characters beginning with `_` (BSDi extended DES) / 13 characters (traditional DES)). The bcrypt cost is limited to 16, and `rounds=` for SHA-crypt is limited to 10000000; exceeding these limits returns 400 (`out of range`). `$2x$` and `$2$` are not supported.<br />
Other algorithms return 400 (`unsupported algorithm`), malformed formats return 400 (`invalid parameter`), and parameters outside the range of [DeriveKey](internal_crypto.DeriveKey.md) return 400 (`out of range`; for scrypt, `ln=` must be between 1 and 62). If the pbkdf2 `l=` does not match the hash length, it is also treated as a malformed format and returns 400 (`invalid parameter`).

- **Argument1**: password (default format is `text`)
- **Argument2**: PHC string (or \[SSP 2.9.23\] a crypt(3)-format string)
- **Options**: `--password-in=` / `--charset=`

**対応:** SSP 2.9.13
