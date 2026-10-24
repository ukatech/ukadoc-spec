# Decrypt

**カテゴリ:** internal_crypto

[Encrypt](internal_crypto.Encrypt.md)の暗号文を復号する。<br />
復号できなければ500（`authentication failed`）。認証付き暗号では、暗号文・認証タグ・`--aad=`のどれかが違えばこれになる。CBCではパディングが合わないとき。CTRは間違った鍵でも何かしらの値を返す。

- **Argument1**: アルゴリズム名
- **Argument2**: key（既定の形式は`text`）
- **Argument3**: ciphertext（既定の形式は`base64`）
- **オプション**: `--key-in=` / `--ciphertext-in=` / `--aad=` / `--aad-in=` / `--iv=` / `--iv-in=` / `--pack=none` / `--out=`（既定は`text`） / `--charset=`

`--pack=none`のときは`--iv=`が要ります。`--pack=none`でないとき（nonce / IVが暗号文の先頭にあるとき）に`--iv=`を付けると400（`invalid parameter`）です。

**対応:** SSP 2.9.13
