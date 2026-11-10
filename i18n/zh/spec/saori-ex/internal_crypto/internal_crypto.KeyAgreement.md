# KeyAgreement

**カテゴリ:** internal_crypto

根据自己的私钥和对方的公钥，求出只有双方才能得到相同值的共享秘密（ECDH）。结果为32字节，不进行哈希（`secp256k1`直接使用点的x坐标，与nostr的NIP-44相同；`x25519`直接使用RFC 7748的结果；`p256`直接使用点的x坐标）。<br />
**不要直接将结果用作加密密钥。**请先通过[DeriveKey](internal_crypto.DeriveKey.md)的`hkdf`（或`hkdf-extract`）处理后再使用。

- **Argument1**: 方式：`secp256k1` / `x25519`（\[SSP 2.9.27\]） / `p256`（\[SSP 2.9.27\]。NIST P-256 = secp256r1 = prime256v1）
- **Argument2**: 私钥（32字节。默认格式为`hex`）
- **Argument3**: 对方的公钥（默认格式为`hex`）
- **选项**: `--key-in=` / `--peer-in=` / `--out=`（默认格式为`hex`）

密钥使用原始值，而不是DER / PEM格式。

- **secp256k1**: 对方的公钥可以是仅包含x坐标的32字节形式（BIP-340 / nostr格式）、33字节压缩形式或65字节非压缩形式。
- **x25519**: 私钥和对方的公钥均为32字节（RFC 7748。SSP会调整私钥位（clamping））。不接受会产生全0结果的公钥（低阶点）。
- **p256**: 对方的公钥可以是33字节压缩形式（前缀为`02`或`03`），或65字节非压缩形式（前缀为`04`）。不接受仅包含x坐标的32字节形式（与`secp256k1`不同，这不是P-256公钥的形式）。

私钥超出范围（为0或不小于阶；`x25519`的私钥不是32字节）、对方的公钥不是曲线上的点或长度不正确时，返回400（`invalid key`）。`x25519` / `p256`的密钥可通过[GenerateKeyPair](internal_crypto.GenerateKeyPair.md)生成。

## 記述例

```
Argument0: KeyAgreement
Argument1: secp256k1
Argument2: 315e59ff51cb9209768cf7da80791ddcaae56ac9775eb25b6dee1234bc5d2268
Argument3: c2f9d9948dc8c7c38321e4b85c8558872eafa0641cd269db76848a6073e69133

→ Result: 5ad01c0fc57ed5f92a0518b6440ca876eb1f247ddbb237ba1caaabbf4cebbdce
```

```
Argument0: DeriveKey
Argument1: hkdf-extract
Argument2: 5ad01c0fc57ed5f92a0518b6440ca876eb1f247ddbb237ba1caaabbf4cebbdce
Argument3: nip44-v2
Argument4: 32
Argument5: --password-in=hex

→ Result: 3dfef0ce2a4d80a25e7a328accf73448ef67096f65f79588e358d9a0eb9013f1
```

（NIP-44会话密钥。NIP-44测试向量）

```
Argument0: KeyAgreement
Argument1: x25519
Argument2: 77076d0a7318a57d3c16c17251b26645df4c2f87ebc0992ab177fba51db92c2a
Argument3: de9edb7d7b7dc1b4d35b61c2ece435373f8343c85b78674dadfc7e146f882b4f

→ Result: 4a5d9d5ba4ce2de1728e3bf480350f25e07e21c947d19e3376f09b3c1e161742
```

（RFC 7748 §6.1的测试向量。对于`p256`，将RFC 5903 §8.1中的`i`作为私钥，并将`04`＋`gr`的x、y坐标作为对方的公钥，可得到`d6840f6b42f6edafd13116e0e12565202fef8e9ece7dce03812464d04b9442de`）

**対応:** SSP 2.9.14（`x25519` / `p256`为 SSP 2.9.27）
