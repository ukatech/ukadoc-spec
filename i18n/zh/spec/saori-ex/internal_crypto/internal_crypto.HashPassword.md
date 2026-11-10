# HashPassword

**カテゴリ:** internal_crypto

将密码哈希后用于保存，并以 PHC 字符串（将方式、参数、salt 和哈希值合并成一行的字符串）返回。每次使用 16 字节随机数生成 salt，哈希值为 32 字节，参数固定如下表（采用 OWASP 推荐且内存用量不超过上限 12MiB 的参数）。<br />
保存的字符串可通过[VerifyPassword](internal_crypto.VerifyPassword.md)进行验证。建议使用[`--async`](../async.md)。

- **Argument1**: password（默认格式为`text`）
- **选项**: `--method=`（见下表，默认值为`argon2id`） / `--password-in=` / `--charset=`

- **argon2id**: `$argon2id$v=19$m=12288,t=3,p=1$ソルト$ハッシュ`
- **scrypt**: `$scrypt$ln=13,r=8,p=10$ソルト$ハッシュ`（ln 是以 2 为底的 N 的对数）
- **pbkdf2-sha256**: `$pbkdf2-sha256$i=600000,l=32$ソルト$ハッシュ`
- **bcrypt**: \[SSP 2.9.23\] `$2b$12$`＋22 个字符的 salt＋31 个字符的哈希值。密码只使用开头的 72 字节。
- **sha512-crypt**: \[SSP 2.9.23\] `$6$rounds=656000$ソルト$ハッシュ`（salt 为 16 个字符）
- **sha256-crypt**: \[SSP 2.9.23\] `$5$rounds=535000$ソルト$ハッシュ`（salt 为 16 个字符）
- **md5-crypt**: \[SSP 2.9.23\] `$1$ソルト$ハッシュ`（salt 为 8 个字符）
- **apr1**: \[SSP 2.9.23\] `$apr1$ソルト$ハッシュ`（salt 为 8 个字符，Apache htpasswd 格式）
- **bsdi-crypt**: \[SSP 2.9.23\] `_`＋4 个字符的迭代次数＋4 个字符的 salt＋11 个字符的哈希值（BSDi 扩展 DES，迭代次数为 5001）
- **des-crypt**: \[SSP 2.9.23\] 2 个字符的 salt＋11 个字符的哈希值（传统 crypt(3) DES）。密码只使用开头的 8 个字符。

salt 和哈希值采用 base64（不带填充）。<br />
\[SSP 2.9.23\] bcrypt 及以下方式采用 crypt(3) 格式，用于与其他系统（/etc/shadow、htpasswd、PHP 的`password_hash`等）交互。`--method=`名称中的连字符、下划线以及大小写均会被忽略。salt 和哈希值使用各格式对应的字符（`./0-9A-Za-z`），参数固定如上表。md5-crypt、apr1、bsdi-crypt、des-crypt 现已属于弱算法，除互操作用途外请勿使用。crypt(3) 格式的密码不能包含 NUL（0x00）；若包含则返回 400（`invalid parameter`）。密码超过 1024 字节时返回 400（`out of range`）。

**対応:** SSP 2.9.13
