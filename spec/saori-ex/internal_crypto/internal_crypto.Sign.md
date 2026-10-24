# Sign

**カテゴリ:** internal_crypto

秘密鍵でデータに署名する。

- **Argument1**: 方式（[公開鍵暗号](internal_crypto_pkey.md)を参照）
- **Argument2**: 秘密鍵
- **Argument3**: data（既定の形式は`text`）
- **オプション**: `--data-in=` / `--out=`（既定は`base64url`。`bip340`は`hex`） / `--charset=` / `--key-in=`（`bip340`だけ。既定は`hex`） / `--aux=`（`bip340`だけ。BIP-340の補助の乱数32バイト。`--aux-in=`、既定の形式は`hex`。省略時は毎回乱数。テストベクタと突き合わせるとき以外は使わないこと）

## 記述例

```
Argument0: Sign
Argument1: ed25519
Argument2: MC4CAQAwBQYDK2VwBCIEIJ1hsZ3v/VpguoRK9JLsLMREScVpezJpGXA7rAMcrn9g
Argument3: eyJhbGciOiJFZERTQSJ9.RXhhbXBsZSBvZiBFZDI1NTE5IHNpZ25pbmc

→ Result: hgyY0il_MGCjP0JzlnLWG1PPOt7-09PGcvMg3AIbQR6dWbhijcNR4ki4iylGjg5BhVsPt9g7sVvpAr_MuM0KAg
```

```
Argument0: Sign
Argument1: bip340
Argument2: b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d9045190cfef
Argument3: 243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89
Argument4: --data-in=hex
Argument5: --aux=0000000000000000000000000000000000000000000000000000000000000001

→ Result: 6896bd60eeae296db48a229ff71dfe071bde413e6d43f917dc8dcf8c78de33418906d11ac976abccb20b091292bff4ea897efcb639ea871cfa95f6de339e4b0a
```

（BIP-340のテストベクタ1）

Ed25519とRSA（rs256）は、同じ鍵とデータなら毎回同じ署名になります。es256・ps256・bip340は毎回違う署名になります（どれも[Verify](internal_crypto.Verify.md)で検証できる）。

**対応:** SSP 2.9.14
