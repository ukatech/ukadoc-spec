# VerifyPassword

**カテゴリ:** internal_crypto

Checks whether the password matches the PHC string, returning `1` if it does and `0` otherwise. Parameters are read from the PHC string. [`--async`](../async.md) is recommended.<br />
In addition to the output of [HashPassword](internal_crypto.HashPassword.md), strings created by other implementations can also be read if they have the same format (`$argon2id$` (with or without `v=`, including `v=16`) / `$scrypt$` / `$pbkdf2-sha1$` / `$pbkdf2-sha256$` / `$pbkdf2-sha512$`). However, parameters that exceed the memory limit (12MiB)—such as argon2-cffi's default of 64MiB—cannot be verified and return 400 (`out of range`).<br />
\[SSP 2.9.23\] crypt(3) formats can also be read (`$2a$` / `$2b$` / `$2y$` (bcrypt; all three are handled identically) / `$6$` / `$5$` (with or without `rounds=`, including values below 1000, which are rounded up to 1000) / `$1$` / `$apr1$` / 20 characters beginning with `_` (BSDi extended DES) / 13 characters (traditional DES)). The bcrypt cost is limited to 16, and `rounds=` for SHA-crypt is limited to 10000000; values above these limits return 400 (`out of range`). `$2x$` and `$2$` are not supported.<br />
Other algorithms return 400 (`unsupported algorithm`), malformed formats return 400 (`invalid parameter`), and parameters outside the range of [DeriveKey](internal_crypto.DeriveKey.md) return 400 (`out of range`; for scrypt, `ln=` must be from 1 to 62). If the pbkdf2 `l=` does not match the hash length, this is also treated as a malformed format and returns 400 (`invalid parameter`).

- **Argument1**: password (default format is `text`)
- **Argument2**: PHC string (or a string in crypt(3) format) (\[SSP 2.9.23\])
- **オプション**: `--password-in=` / `--charset=`

**対応:** SSP 2.9.13
