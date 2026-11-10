# VerifyPassword

**カテゴリ:** internal_crypto

檢查密碼是否與PHC字串相符，相符時回傳`1`，否則回傳`0`。參數會從PHC字串讀取。建議使用[`--async`](../async.md)。<br />
除了[HashPassword](internal_crypto.HashPassword.md)的輸出外，也可以讀取其他實作產生的相同格式字串（`$argon2id$`（可省略`v=`，也可以是`v=16`） / `$scrypt$` / `$pbkdf2-sha1$` / `$pbkdf2-sha256$` / `$pbkdf2-sha512$`）。不過，參數超過記憶體上限（12MiB）的項目（例如argon2-cffi預設的64MiB）會回傳400（`out of range`），無法進行比對。<br />
\[SSP 2.9.23\] 也可以讀取crypt(3)格式（`$2a$` / `$2b$` / `$2y$`（bcrypt。三者視為相同） / `$6$` / `$5$`（可省略`rounds=`，也可以是小於1000、會向上取整至1000的值） / `$1$` / `$apr1$` / 以`_`開頭的20個字元（BSDi擴充DES） / 13個字元（傳統DES））。bcrypt的成本最高為16，SHA-crypt的`rounds=`最高為10000000，超過時會回傳400（`out of range`）。不支援`$2x$`・`$2$`。<br />
其他方式會回傳400（`unsupported algorithm`），格式錯誤會回傳400（`invalid parameter`），參數超出[DeriveKey](internal_crypto.DeriveKey.md)的範圍時會回傳400（`out of range`。scrypt的`ln=`必須介於1～62，否則會回傳此錯誤）。pbkdf2的`l=`與雜湊長度不一致時，也會視為格式錯誤並回傳400（`invalid parameter`）。

- **Argument1**: password（預設格式為`text`）
- **Argument2**: PHC字串（\[SSP 2.9.23\] 或crypt(3)格式的字串）
- **選項**: `--password-in=` / `--charset=`

**対応:** SSP 2.9.13
