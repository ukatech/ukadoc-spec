# HashPassword

**カテゴリ:** internal_crypto

パスワードを保存用にハッシュし、PHC文字列（方式・パラメータ・ソルト・ハッシュをまとめた1行の文字列）で返す。ソルトは毎回16バイトの乱数、ハッシュは32バイト、パラメータは下の表で固定（OWASPの推奨のうち、メモリの上限12MiBに収まるもの）。<br />
保存した文字列は[VerifyPassword](internal_crypto.VerifyPassword.md)で照合する。[`--async`](../async.md)を推奨。

- **Argument1**: password（既定の形式は`text`）
- **オプション**: `--method=`（下の表。既定は`argon2id`） / `--password-in=` / `--charset=`

- **argon2id**: `$argon2id$v=19$m=12288,t=3,p=1$ソルト$ハッシュ`
- **scrypt**: `$scrypt$ln=13,r=8,p=10$ソルト$ハッシュ`（ln は N の2を底とする対数）
- **pbkdf2-sha256**: `$pbkdf2-sha256$i=600000,l=32$ソルト$ハッシュ`
- **bcrypt**: \[SSP 2.9.23\] `$2b$12$`＋ソルト22文字＋ハッシュ31文字。パスワードは先頭の72バイトまでしか使われない。
- **sha512-crypt**: \[SSP 2.9.23\] `$6$rounds=656000$ソルト$ハッシュ`（ソルトは16文字）
- **sha256-crypt**: \[SSP 2.9.23\] `$5$rounds=535000$ソルト$ハッシュ`（ソルトは16文字）
- **md5-crypt**: \[SSP 2.9.23\] `$1$ソルト$ハッシュ`（ソルトは8文字）
- **apr1**: \[SSP 2.9.23\] `$apr1$ソルト$ハッシュ`（ソルトは8文字。Apacheのhtpasswdの形式）
- **bsdi-crypt**: \[SSP 2.9.23\] `_`＋反復回数4文字＋ソルト4文字＋ハッシュ11文字（BSDiの拡張DES。反復回数は5001）
- **des-crypt**: \[SSP 2.9.23\] ソルト2文字＋ハッシュ11文字（伝統的なcrypt(3)のDES）。パスワードは先頭の8文字までしか使われない。

ソルトとハッシュはbase64（パディングなし）である。<br />
\[SSP 2.9.23\] bcrypt以下はcrypt(3)の形式で、ほかのシステム（/etc/shadow、htpasswd、PHPの`password_hash`など）とやりとりするためのもの。`--method=`の名前のハイフン・アンダースコアと大文字小文字は無視する。ソルトとハッシュは各形式の文字（`./0-9A-Za-z`）で、パラメータは上の表で固定。md5-crypt・apr1・bsdi-crypt・des-cryptは今では弱い方式なので、相互運用のほかには使わないこと。crypt(3)の形式ではパスワードにNUL（0x00）を含められず、含めると400（`invalid parameter`）。1024バイトを超えるパスワードは400（`out of range`）。

**対応:** SSP 2.9.13
