# GenerateKeyPair

**カテゴリ:** internal_crypto

公開鍵暗号の鍵ペアを作る。`Value0`に秘密鍵（PKCS#8）、`Value1`に公開鍵（SubjectPublicKeyInfo）が、どちらもDERのbase64で入る。`Result`は`Value0`と同じ。<br />
RSAの鍵の生成は数秒かかることがあるので、[`--async`](../async.md)を推奨（非同期の呼び出しでは、秘密鍵がReference4、公開鍵がReference5に入る）。<br />
秘密鍵は必要なら[Protect](internal_crypto.Protect.md)で包んで保存してください。

- **Argument1**: 方式：`ed25519` / `es256`（P-256） / `es384`（P-384。\[SSP 2.9.27\]） / `es512`（P-521。\[SSP 2.9.27\]） / `rsa-2048` / `rsa-3072` / `rsa-4096`（RSAの鍵は`rs256`～`ps512`のどれにも使える） / `bip340`（secp256k1） / `x25519`（\[SSP 2.9.27\]） / `p256`（\[SSP 2.9.27\]）

`bip340` `x25519` `p256`だけは、DERではなく生の値が、どちらも16進（小文字）で入る。

- **bip340**: `Value0`に秘密鍵（32バイト）、`Value1`にx座標だけの公開鍵（32バイト）。nostrの`nsec` / `npub`にするときは[Convert](../internal_data/internal_data.Convert.md)の`--out=bech32`を使う。この鍵は[KeyAgreement](internal_crypto.KeyAgreement.md)の`secp256k1`にもそのまま使える。
- **x25519**: `Value0`に秘密鍵（32バイト）、`Value1`に公開鍵（32バイト）。[KeyAgreement](internal_crypto.KeyAgreement.md)の`x25519`にそのまま使える。
- **p256**: `Value0`に秘密鍵（32バイト）、`Value1`に非圧縮形式の公開鍵（65バイト。先頭が`04`）。[KeyAgreement](internal_crypto.KeyAgreement.md)の`p256`にそのまま使える。署名用の`es256`の鍵（DER）とは形が違う。

**対応:** SSP 2.9.14（`es384` `es512` `x25519` `p256`は SSP 2.9.27）
