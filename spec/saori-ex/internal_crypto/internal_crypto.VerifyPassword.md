# VerifyPassword

**カテゴリ:** internal_crypto

パスワードがPHC文字列と一致するかを調べ、一致すれば`1`、しなければ`0`を返す。パラメータはPHC文字列から読む。[`--async`](../async.md)を推奨。<br />
[HashPassword](internal_crypto.HashPassword.md)の出力のほか、同じ形のものなら他の実装が作った文字列も読める（`$argon2id$`（`v=`の無いもの・`v=16`も可） / `$scrypt$` / `$pbkdf2-sha1$` / `$pbkdf2-sha256$` / `$pbkdf2-sha512$`）。ただしメモリの上限（12MiB）を超えるパラメータのもの（argon2-cffiの既定の64MiBなど）は400（`out of range`）で照合できない。<br />
\[SSP 2.9.23\] crypt(3)の形式も読める（`$2a$` / `$2b$` / `$2y$`（bcrypt。3つとも同じに扱う） / `$6$` / `$5$`（`rounds=`の無いもの・1000未満を1000に切り上げるものも可） / `$1$` / `$apr1$` / `_`で始まる20文字（BSDiの拡張DES） / 13文字（伝統的なDES））。bcryptのコストは16まで、SHA-cryptの`rounds=`は10000000までで、それを超えると400（`out of range`）。`$2x$`・`$2$`は扱わない。<br />
これ以外の方式は400（`unsupported algorithm`）、形の誤りは400（`invalid parameter`）、パラメータが[DeriveKey](internal_crypto.DeriveKey.md)の範囲の外なら400（`out of range`）。

- **Argument1**: password（既定の形式は`text`）
- **Argument2**: PHC文字列（\[SSP 2.9.23\] またはcrypt(3)の形式の文字列）
- **オプション**: `--password-in=` / `--charset=`

**対応:** SSP 2.9.13
