# KeyAgreement

**カテゴリ:** internal_crypto

自分の秘密鍵と相手の公開鍵から、2人だけが同じ値を得られる共有の秘密を求める（ECDH）。結果は点のx座標（32バイト）そのままで、ハッシュはしない（nostrのNIP-44と同じ）。<br />
**結果をそのまま暗号の鍵にしないこと。**[DeriveKey](internal_crypto.DeriveKey.md)の`hkdf`（または`hkdf-extract`）を通してから使ってください。

- **Argument1**: 方式：`secp256k1`
- **Argument2**: 秘密鍵（32バイト。既定の形式は`hex`）
- **Argument3**: 相手の公開鍵（既定の形式は`hex`）。x座標だけの32バイト（BIP-340 / nostrの形）、圧縮形式の33バイト、非圧縮形式の65バイトのどれでもよい
- **オプション**: `--key-in=` / `--peer-in=` / `--out=`（既定は`hex`）

秘密鍵が範囲外、相手の公開鍵が曲線上の点でない・長さが違うときは400（`invalid key`）。

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

**対応:** SSP 2.9.14
