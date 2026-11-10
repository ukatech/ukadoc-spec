# Sign

**カテゴリ:** internal_crypto

使用私密金鑰對資料簽章。

- **Argument1**: 方法（請參閱[公開金鑰密碼學](internal_crypto_pkey.md)）
- **Argument2**: 私密金鑰
- **Argument3**: data（預設格式為`text`）
- **選項**: `--data-in=` / `--out=`（預設為`base64url`。`bip340`為`hex`） / `--charset=` / `--key-in=`（僅限`bip340`。預設為`hex`） / `--aux=`（僅限`bip340`。BIP-340 的輔助亂數，32 位元組。`--aux-in=`，預設格式為`hex`。省略時每次使用亂數。除非要與測試向量比對，否則請勿使用）

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

（BIP-340 測試向量 1）

Ed25519 和 RSA（rs256 / rs384 / rs512）使用相同金鑰和資料時，每次都會產生相同簽章。es256 / es384 / es512、ps256 / ps384 / ps512、bip340 每次則會產生不同簽章（皆可透過[Verify](internal_crypto.Verify.md)驗證）。

**対応:** SSP 2.9.14
