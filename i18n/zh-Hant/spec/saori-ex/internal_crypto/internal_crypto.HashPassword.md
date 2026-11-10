# HashPassword

**カテゴリ:** internal_crypto

Hashes a password for storage and returns it as a PHC string (a single-line string containing the method, parameters, salt, and hash). A new 16-byte random salt is generated each time, the hash is 32 bytes, and the parameters are fixed as shown in the table below (using an OWASP-recommended configuration that fits within the 12 MiB memory limit).<br />
Use [VerifyPassword](internal_crypto.VerifyPassword.md) to verify the stored string. [`--async`](../async.md) is recommended.

- **Argument1**: password (default format is `text`)
- **Options**: `--method=` (see table below; default is `argon2id`) / `--password-in=` / `--charset=`

- **argon2id**: `$argon2id$v=19$m=12288,t=3,p=1$ソルト$ハッシュ`
- **scrypt**: `$scrypt$ln=13,r=8,p=10$ソルト$ハッシュ` (ln is the base-2 logarithm of N)
- **pbkdf2-sha256**: `$pbkdf2-sha256$i=600000,l=32$ソルト$ハッシュ`
- **bcrypt**: \[SSP 2.9.23\] `$2b$12$`＋ソルト22文字＋ハッシュ31文字。Only the first 72 bytes of the password are used.
- **sha512-crypt**: \[SSP 2.9.23\] `$6$rounds=656000$ソルト$ハッシュ` (salt is 16 characters)
- **sha256-crypt**: \[SSP 2.9.23\] `$5$rounds=535000$ソルト$ハッシュ` (salt is 16 characters)
- **md5-crypt**: \[SSP 2.9.23\] `$1$ソルト$ハッシュ` (salt is 8 characters)
- **apr1**: \[SSP 2.9.23\] `$apr1$ソルト$ハッシュ` (salt is 8 characters; Apache htpasswd format)
- **bsdi-crypt**: \[SSP 2.9.23\] `_`＋反復回数4文字＋ソルト4文字＋ハッシュ11文字 (BSDi's extended DES; the iteration count is 5001)
- **des-crypt**: \[SSP 2.9.23\] ソルト2文字＋ハッシュ11文字 (traditional crypt(3) DES). Only the first 8 characters of the password are used.

The salt and hash are base64 (without padding).<br />
\[SSP 2.9.23\] bcrypt and the methods below use the crypt(3) format, for interoperability with other systems (such as /etc/shadow, htpasswd, and PHP's `password_hash`). Hyphens and underscores, and letter case, in `--method=` names are ignored. The salt and hash use the characters defined for each format (`./0-9A-Za-z`), and the parameters are fixed as shown in the table above. md5-crypt, apr1, bsdi-crypt, and des-crypt are weak methods by today's standards, so use them only for interoperability. Passwords in the crypt(3) format cannot contain NUL (0x00); if they do, the result is 400 (`invalid parameter`). Passwords longer than 1024 bytes result in 400 (`out of range`).

**対応:** SSP 2.9.13
