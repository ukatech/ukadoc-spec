# GenerateKeyPair

**カテゴリ:** internal_crypto

公開鍵暗号の鍵ペアを作る。`Value0`に秘密鍵（PKCS#8）、`Value1`に公開鍵（SubjectPublicKeyInfo）が、どちらもDERのbase64で入る。`Result`は`Value0`と同じ。<br />
RSAの鍵の生成は数秒かかることがあるので、[`--async`](../async.md)を推奨（非同期の呼び出しでは、秘密鍵がReference4、公開鍵がReference5に入る）。<br />
秘密鍵は必要なら[Protect](internal_crypto.Protect.md)で包んで保存してください。

- **Argument1**: 方式：`ed25519` / `es256`（P-256） / `rsa-2048` / `rsa-3072` / `rsa-4096`（RSAの鍵は`rs256`と`ps256`のどちらにも使える） / `bip340`（secp256k1）

`bip340`だけは`Value0`に秘密鍵（32バイト）、`Value1`にx座標だけの公開鍵（32バイト）が、どちらも16進（小文字）で入る。nostrの`nsec` / `npub`にするときは[Convert](../internal_data/internal_data.Convert.md)の`--out=bech32`を使う。この鍵は[KeyAgreement](internal_crypto.KeyAgreement.md)の`secp256k1`にもそのまま使える。

**対応:** SSP 2.9.14
