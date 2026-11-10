# HashPassword

**カテゴリ:** internal_crypto

Hashes a password for storage and returns it as a PHC string (a single-line string combining the method, parameters, salt, and hash). The salt is a 16-byte random value generated each time, the hash is 32 bytes, and the parameters are fixed as shown in the table below (using an OWASP-recommended configuration that fits within the 12 MiB memory limit).<br />
Verify the stored string with [VerifyPassword](internal_crypto.VerifyPassword.md). [`--async`](../async.md) is recommended.

- **Argument1**: password (the default format is `text`)
- **Options**: `--method=` (see the table below; default is `argon2id`) / `--password-in=` / `--charset=`

- **argon2id**: `$argon2id$v=19$m=12288,t=3,p=1$ソルト$ハッシュ`
- **scrypt**: `$scrypt$ln=13,r=8,p=10$ソルト$ハッシュ` (ln is the logarithm of N to base 2)
- **pbkdf2-sha256**: `$pbkdf2-sha256$i=600000,l=32$ソルト$ハッシュ`
- **bcrypt**: \[SSP 2.9.23\] `$2b$12$` + 22 salt characters + 31 hash characters. Only the first 72 bytes of the password are used.
- **sha512-crypt**: \[SSP 2.9.23\] `$6$rounds=656000$ソルト$ハッシュ` (the salt is 16 characters)
- **sha256-crypt**: \[SSP 2.9.23\] `$5$rounds=535000$ソルト$ハッシュ` (the salt is 16 characters)
- **md5-crypt**: \[SSP 2.9.23\] `$1$ソルト$ハッシュ` (the salt is 8 characters)
- **apr1**: \[SSP 2.9.23\] `$apr1$ソルト$ハッシュ` (the salt is 8 characters; the Apache htpasswd format)
- **bsdi-crypt**: \[SSP 2.9.23\] `_` + 4 iteration-count characters + 4 salt characters + 11 hash characters (BSDi's extended DES; the iteration count is 5001)
- **des-crypt**: \[SSP 2.9.23\] 2 salt characters + 11 hash characters (traditional crypt(3) DES). Only the first 8 characters of the password are used.

The salt and hash are base64-encoded (without padding).<br />
\[SSP 2.9.23\] bcrypt and the methods below use the crypt(3) format, intended for interoperability with other systems (/etc/shadow, htpasswd, PHP's `password_hash`, etc.). Hyphens and underscores, and letter case, in the `--method=` name are ignored. The salt and hash use the characters allowed by each format (`./0-9A-Za-z`), and the parameters are fixed as shown in the table above. md5-crypt, apr1, bsdi-crypt, and des-crypt are weak methods today and should only be used for interoperability. The crypt(3) format does not allow NUL (0x00) in passwords; if present, the result is 400 (`invalid parameter`). Passwords longer than 1024 bytes result in 400 (`out of range`).

**対応:** SSP 2.9.13
