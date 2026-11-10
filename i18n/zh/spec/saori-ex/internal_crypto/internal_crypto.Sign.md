# Sign

**カテゴリ:** internal_crypto

使用私钥对数据签名。

- **Argument1**: 方式（参见[公开密钥密码](internal_crypto_pkey.md)）
- **Argument2**: 私钥
- **Argument3**: data（默认格式为`text`）
- **选项**: `--data-in=` / `--out=`（默认格式为`base64url`。`bip340`为`hex`） / `--charset=` / `--key-in=`（仅`bip340`。默认格式为`hex`） / `--aux=`（仅`bip340`。BIP-340的32字节辅助随机数。使用`--aux-in=`指定输入格式，默认格式为`hex`。省略时每次都会生成随机数。除非要与测试向量进行比对，否则不要使用）

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

（BIP-340测试向量1）

Ed25519和RSA（rs256 / rs384 / rs512）在密钥和数据相同时，每次都会生成相同的签名。es256 / es384 / es512・ps256 / ps384 / ps512・bip340每次都会生成不同的签名（均可通过[Verify](internal_crypto.Verify.md)验证）。

**対応:** SSP 2.9.14
