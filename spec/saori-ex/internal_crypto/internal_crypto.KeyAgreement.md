# KeyAgreement

**カテゴリ:** internal_crypto

自分の秘密鍵と相手の公開鍵から、2人だけが同じ値を得られる共有の秘密を求める（ECDH）。結果は32バイトで、ハッシュはしない（`secp256k1`は点のx座標そのままで、nostrのNIP-44と同じ。`x25519`はRFC 7748の結果そのまま、`p256`は点のx座標そのまま）。<br />
**結果をそのまま暗号の鍵にしないこと。**[DeriveKey](internal_crypto.DeriveKey.md)の`hkdf`（または`hkdf-extract`）を通してから使ってください。

- **Argument1**: 方式：`secp256k1` / `x25519`（\[SSP 2.9.27\]） / `p256`（\[SSP 2.9.27\]。NIST P-256 = secp256r1 = prime256v1）
- **Argument2**: 秘密鍵（32バイト。既定の形式は`hex`）
- **Argument3**: 相手の公開鍵（既定の形式は`hex`）
- **オプション**: `--key-in=` / `--peer-in=` / `--out=`（既定は`hex`）

鍵は、DER / PEMではなく生の値である。

- **secp256k1**: 相手の公開鍵は、x座標だけの32バイト（BIP-340 / nostrの形）、圧縮形式の33バイト、非圧縮形式の65バイトのどれでもよい。
- **x25519**: 秘密鍵も相手の公開鍵も32バイト（RFC 7748。秘密鍵のビットの調整（clamping）はSSPがする）。結果が全部0になる公開鍵（位数の小さい点）は、受け付けない。
- **p256**: 相手の公開鍵は、圧縮形式の33バイト（先頭が`02`か`03`）か、非圧縮形式の65バイト（先頭が`04`）。x座標だけの32バイトは受け付けない（`secp256k1`と違い、P-256の公開鍵の形ではない）。

秘密鍵が範囲外（0や位数以上、`x25519`では32バイトでない）、相手の公開鍵が曲線上の点でない・長さが違うときは400（`invalid key`）。`x25519` / `p256`の鍵は[GenerateKeyPair](internal_crypto.GenerateKeyPair.md)で作れる。

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

（NIP-44の会話鍵。NIP-44のテストベクタ）

```
Argument0: KeyAgreement
Argument1: x25519
Argument2: 77076d0a7318a57d3c16c17251b26645df4c2f87ebc0992ab177fba51db92c2a
Argument3: de9edb7d7b7dc1b4d35b61c2ece435373f8343c85b78674dadfc7e146f882b4f

→ Result: 4a5d9d5ba4ce2de1728e3bf480350f25e07e21c947d19e3376f09b3c1e161742
```

（RFC 7748 §6.1のテストベクタ。`p256`は、RFC 5903 §8.1の`i`を秘密鍵に、相手の公開鍵を`04`＋`gr`のx・yにして、`d6840f6b42f6edafd13116e0e12565202fef8e9ece7dce03812464d04b9442de`が得られる）

**対応:** SSP 2.9.14（`x25519` / `p256`は SSP 2.9.27）
