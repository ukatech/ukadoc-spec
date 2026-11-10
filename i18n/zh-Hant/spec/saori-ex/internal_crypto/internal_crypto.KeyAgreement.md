# KeyAgreement

**カテゴリ:** internal_crypto

從自己的私密金鑰和對方的公開金鑰計算出只有雙方能取得相同值的共享秘密（ECDH）。結果為 32 位元組，不會進行雜湊（`secp256k1`直接使用點的 x 座標，與 nostr 的 NIP-44 相同；`x25519`直接使用 RFC 7748 的結果；`p256`直接使用點的 x 座標）。<br />
**請勿將結果直接用作加密金鑰。**請先經過 [DeriveKey](internal_crypto.DeriveKey.md) 的`hkdf`（或`hkdf-extract`）再使用。

- **Argument1**: 方法：`secp256k1` / `x25519`（\[SSP 2.9.27\]） / `p256`（\[SSP 2.9.27\]。NIST P-256 = secp256r1 = prime256v1）
- **Argument2**: 私密金鑰（32 位元組。預設格式為`hex`）
- **Argument3**: 對方的公開金鑰（預設格式為`hex`）
- **選項**: `--key-in=` / `--peer-in=` / `--out=`（預設為`hex`）

金鑰是原始值，不是 DER / PEM 格式。

- **secp256k1**: 對方的公開金鑰可以是只有 x 座標的 32 位元組（BIP-340 / nostr 格式）、壓縮格式的 33 位元組，或非壓縮格式的 65 位元組。
- **x25519**: 私密金鑰和對方的公開金鑰皆為 32 位元組（RFC 7748。SSP 會調整私密金鑰的位元（clamping））。不接受會使結果全為 0 的公開金鑰（低階點）。
- **p256**: 對方的公開金鑰可以是壓縮格式的 33 位元組（開頭為`02`或`03`），或非壓縮格式的 65 位元組（開頭為`04`）。不接受只有 x 座標的 32 位元組格式（與`secp256k1`不同，這不是 P-256 公開金鑰的格式）。

私密金鑰超出範圍（為 0 或大於等於曲線階數；`x25519`時不是 32 位元組）、對方的公開金鑰不在曲線上或長度不符時，會回傳 400（`invalid key`）。`x25519` / `p256`的金鑰可用 [GenerateKeyPair](internal_crypto.GenerateKeyPair.md) 建立。

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

（NIP-44 的對話金鑰。NIP-44 測試向量）

```
Argument0: KeyAgreement
Argument1: x25519
Argument2: 77076d0a7318a57d3c16c17251b26645df4c2f87ebc0992ab177fba51db92c2a
Argument3: de9edb7d7b7dc1b4d35b61c2ece435373f8343c85b78674dadfc7e146f882b4f

→ Result: 4a5d9d5ba4ce2de1728e3bf480350f25e07e21c947d19e3376f09b3c1e161742
```

（RFC 7748 §6.1 的測試向量。`p256`使用 RFC 5903 §8.1 的`i`作為私密金鑰，對方的公開金鑰則設為`04`＋`gr`的 x、y 座標，即可得到`d6840f6b42f6edafd13116e0e12565202fef8e9ece7dce03812464d04b9442de`）

**対応:** SSP 2.9.14（`x25519` / `p256`為 SSP 2.9.27）
