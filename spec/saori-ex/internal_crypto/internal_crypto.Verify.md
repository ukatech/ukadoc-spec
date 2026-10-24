# Verify

**カテゴリ:** internal_crypto

署名を公開鍵で検証する。正しければ`1`、正しくなければ`0`（署名の長さが違うときも`0`）。公開鍵の代わりに秘密鍵を渡してもよい（`bip340`を除く）。<br />
`bip340`では、32バイトだが曲線上の点にならない公開鍵も、BIP-340の決まりどおり`0`になる（長さが違えば400 `invalid key`）。

- **Argument1**: 方式（[公開鍵暗号](internal_crypto_pkey.md)を参照）
- **Argument2**: 公開鍵
- **Argument3**: data（既定の形式は`text`）
- **Argument4**: signature（既定の形式は`base64url`。`bip340`は`hex`）
- **オプション**: `--data-in=` / `--signature-in=` / `--charset=` / `--key-in=`（`bip340`だけ。既定は`hex`）

**対応:** SSP 2.9.14
