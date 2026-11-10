# HashPassword

**カテゴリ:** internal_crypto

將密碼雜湊後供儲存使用，並以 PHC 字串（將方法、參數、salt、雜湊整合成一行的字串）回傳。每次使用的 salt 都是 16 位元組的亂數，雜湊為 32 位元組，參數固定如下表（採用 OWASP 建議中可符合 12MiB 記憶體上限的設定）。<br />
儲存的字串可用 [VerifyPassword](internal_crypto.VerifyPassword.md) 進行比對。建議使用 [`--async`](../async.md)。

- **Argument1**: password（預設格式為`text`）
- **選項**: `--method=`（如下表；預設為`argon2id`） / `--password-in=` / `--charset=`

- **argon2id**: `$argon2id$v=19$m=12288,t=3,p=1$ソルト$ハッシュ`
- **scrypt**: `$scrypt$ln=13,r=8,p=10$ソルト$ハッシュ`（ln 是以 2 為底的 N 對數）
- **pbkdf2-sha256**: `$pbkdf2-sha256$i=600000,l=32$ソルト$ハッシュ`
- **bcrypt**: \[SSP 2.9.23\] `$2b$12$`＋22 個字元的 salt＋31 個字元的雜湊。密碼只會使用前 72 個位元組。
- **sha512-crypt**: \[SSP 2.9.23\] `$6$rounds=656000$ソルト$ハッシュ`（salt 為 16 個字元）
- **sha256-crypt**: \[SSP 2.9.23\] `$5$rounds=535000$ソルト$ハッシュ`（salt 為 16 個字元）
- **md5-crypt**: \[SSP 2.9.23\] `$1$ソルト$ハッシュ`（salt 為 8 個字元）
- **apr1**: \[SSP 2.9.23\] `$apr1$ソルト$ハッシュ`（salt 為 8 個字元。Apache htpasswd 格式）
- **bsdi-crypt**: \[SSP 2.9.23\] `_`＋4 個字元的迭代次數＋4 個字元的 salt＋11 個字元的雜湊（BSDi 擴充 DES。迭代次數為 5001）
- **des-crypt**: \[SSP 2.9.23\] 2 個字元的 salt＋11 個字元的雜湊（傳統 crypt(3) 的 DES）。密碼只會使用前 8 個字元。

salt 和雜湊皆採用 base64（不含填充）。<br />
\[SSP 2.9.23\] bcrypt 以下採用 crypt(3) 格式，用於與其他系統（/etc/shadow、htpasswd、PHP 的`password_hash`等）互通。`--method=`名稱中的連字號與底線，以及大小寫皆會忽略。salt 和雜湊使用各格式的字元（`./0-9A-Za-z`），參數則固定如下表。md5-crypt、apr1、bsdi-crypt、des-crypt 目前都屬於較弱的方法，除互通用途外請勿使用。crypt(3) 格式的密碼不能包含 NUL（0x00）；若包含則回傳 400（`invalid parameter`）。超過 1024 位元組的密碼會回傳 400（`out of range`）。

**対応:** SSP 2.9.13
