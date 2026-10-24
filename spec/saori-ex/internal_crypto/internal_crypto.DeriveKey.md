# DeriveKey

**カテゴリ:** internal_crypto

パスワードなどから、暗号の鍵などに使うバイト列を導出する。方式ごとのパラメータはオプションで指定し、その方式で使わないオプションを書くと400（`invalid parameter`）。<br />
時間とメモリを使う処理なので、[`--async`](../async.md)を推奨。

- **Argument1**: 方式：`pbkdf2` / `hkdf` / `hkdf-extract` / `hkdf-expand` / `scrypt` / `argon2id`
- **Argument2**: password（既定の形式は`text`）
- **Argument3**: salt（既定の形式は`text`）
- **Argument4**: 長さ（バイト。1～1024）
- **オプション**: `--password-in=` / `--salt-in=` / 下の方式ごとのオプション / `--out=`（既定は`hex`） / `--charset=`

- **pbkdf2**: `--digest=`（既定は`sha256`） / `--iterations=`（既定は600000。1～10000000）
- **hkdf**: `--digest=`（既定は`sha256`） / `--info=`（`--info-in=`、既定の形式は`text`）。passwordが入力の鍵（IKM）で、空にはできない。saltは空でもよい。
- **hkdf-extract**: \[SSP 2.9.14\] HKDFのextractだけ（RFC 5869 §2.2）。`--digest=`（既定は`sha256`）。passwordが入力の鍵（IKM。空にはできない）、saltはそのまま。結果はPRKで、長さはハッシュの長さちょうど（sha256なら32）でなければ400（`out of range`）。
- **hkdf-expand**: \[SSP 2.9.14\] HKDFのexpandだけ（RFC 5869 §2.3）。`--digest=`（既定は`sha256`） / `--info=`。passwordがPRK（空にはできない）。saltは空にする（空でなければ400 `invalid parameter`）。長さはハッシュの長さ×255まで。
- **scrypt**: `--n=`（既定は8192。2の累乗） / `--r=`（既定は8） / `--p=`（既定は10。1～16）。N×r×128バイトが12MiBまで。
- **argon2id**: `--iterations=`（既定は3。1～1000） / `--memory=`（KiB。既定は12288。lanes×8～12288） / `--lanes=`（既定は1。1～16）。saltは8バイト以上、長さは4以上。バージョンは1.3（0x13）。秘密鍵（secret）と関連データ（associated data）は使えない。

範囲の外は400（`out of range`）です。既定のパラメータは、OWASPの推奨のうちメモリの上限（12MiB）に収まる組み合わせです。

## 記述例

```
Argument0: DeriveKey
Argument1: pbkdf2
Argument2: password
Argument3: salt
Argument4: 20
Argument5: --digest=sha1
Argument6: --iterations=4096

→ Result: 4b007901b765489abead49d926f721d065a429c1
```

**対応:** SSP 2.9.13
