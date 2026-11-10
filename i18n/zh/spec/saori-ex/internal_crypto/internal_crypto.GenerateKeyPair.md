# GenerateKeyPair

**カテゴリ:** internal_crypto

生成公钥加密的密钥对。`Value0`中存放私钥（PKCS#8），`Value1`中存放公钥（SubjectPublicKeyInfo），两者均以DER的base64格式表示。`Result`与`Value0`相同。<br />
生成RSA密钥可能需要数秒，因此推荐使用[`--async`](../async.md)（异步调用时，私钥存放在Reference4，公钥存放在Reference5中）。<br />
如有需要，请使用[Protect](internal_crypto.Protect.md)加密私钥后再保存。

- **Argument1**: 方式：`ed25519` / `es256`（P-256） / `es384`（P-384。\[SSP 2.9.27\]） / `es512`（P-521。\[SSP 2.9.27\]） / `rsa-2048` / `rsa-3072` / `rsa-4096`（RSA密钥可用于`rs256`～`ps512`中的任何算法） / `bip340`（secp256k1） / `x25519`（\[SSP 2.9.27\]） / `p256`（\[SSP 2.9.27\]）

仅`bip340` `x25519` `p256`使用原始值而非DER格式，且两者均以十六进制（小写）表示。

- **bip340**: `Value0`中存放私钥（32字节），`Value1`中存放仅包含x坐标的公钥（32字节）。转换为nostr的`nsec` / `npub`时，请使用[Convert](../internal_data/internal_data.Convert.md)的`--out=bech32`。此密钥也可直接用于[KeyAgreement](internal_crypto.KeyAgreement.md)的`secp256k1`。
- **x25519**: `Value0`中存放私钥（32字节），`Value1`中存放公钥（32字节）。此密钥可直接用于[KeyAgreement](internal_crypto.KeyAgreement.md)的`x25519`。
- **p256**: `Value0`中存放私钥（32字节），`Value1`中存放未压缩格式的公钥（65字节，首字节为`04`）。此密钥可直接用于[KeyAgreement](internal_crypto.KeyAgreement.md)的`p256`。它与用于签名的`es256`密钥（DER）格式不同。

**対応:** SSP 2.9.14（`es384` `es512` `x25519` `p256`为 SSP 2.9.27）
