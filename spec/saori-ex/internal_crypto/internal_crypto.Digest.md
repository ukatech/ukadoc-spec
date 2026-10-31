# Digest

**カテゴリ:** internal_crypto

ハッシュ値を求める。

- **Argument1**: アルゴリズム名（[一覧](index.md)のハッシュ関数のほか、\[SSP 2.9.27\] 暗号用ではない検査値の`crc32` / `adler32`）
- **Argument2**: data（既定の形式は`text`。`file`も使える）
- **オプション**: `--data-in=` / `--out=`（既定は`hex`） / `--charset=`

## 記述例

```
Argument0: Digest
Argument1: sha256
Argument2: abc

→ Result: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
```

文字列は既定でUTF-8のバイト列としてハッシュする。Shift_JISのバイト列のハッシュがほしいときは`--charset=Shift_JIS`を付けてください。

\[SSP 2.9.27\] `crc32`（CRC-32。zlib・gzip・PNGと同じ）と`adler32`（Adler-32。zlibと同じ）は、ファイルが壊れていないかを確かめるための検査値で、暗号としての強さは無い（改ざんの検出には使わない。それにはSHA-256などを使う）。結果は4バイト（上位から）で、`--out=`の既定の`hex`では8文字になる（`123456789`の`crc32`は`cbf43926`、`adler32`は`091e01de`）。`file`も使える。`HMAC`・`DeriveKey`・`TOTP`のアルゴリズムには使えない（400 `unsupported algorithm`）。

**対応:** SSP 2.9.13
