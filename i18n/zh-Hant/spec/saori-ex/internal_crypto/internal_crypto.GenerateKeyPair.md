# GenerateKeyPair

**カテゴリ:** internal_crypto

產生公開金鑰密碼學的金鑰組。`Value0`存放秘密金鑰（PKCS#8），`Value1`存放公開金鑰（SubjectPublicKeyInfo），兩者皆為DER的base64編碼。`Result`與`Value0`相同。<br />
產生RSA金鑰可能需要數秒，因此建議使用[`--async`](../async.md)（非同步呼叫時，秘密金鑰會放在Reference4，公開金鑰會放在Reference5）。<br />
如有需要，請使用[Protect](internal_crypto.Protect.md)封裝秘密金鑰後再儲存。

- **Argument1**: 方法：`ed25519` / `es256`（P-256） / `es384`（P-384。\[SSP 2.9.27\]） / `es512`（P-521。\[SSP 2.9.27\]） / `rsa-2048` / `rsa-3072` / `rsa-4096`（RSA金鑰可用於任何`rs256`～`ps512`） / `bip340`（secp256k1） / `x25519`（\[SSP 2.9.27\]） / `p256`（\[SSP 2.9.27\]）

僅`bip340`、`x25519`、`p256`會以原始值而非DER格式存放，兩者皆為十六進位（小寫）。

- **bip340**: `Value0`存放秘密金鑰（32位元組），`Value1`存放僅含x座標的公開金鑰（32位元組）。轉換為nostr的`nsec` / `npub`時，請使用[Convert](../internal_data/internal_data.Convert.md)的`--out=bech32`。此金鑰也可直接用於[KeyAgreement](internal_crypto.KeyAgreement.md)的`secp256k1`。
- **x25519**: `Value0`存放秘密金鑰（32位元組），`Value1`存放公開金鑰（32位元組）。可直接用於[KeyAgreement](internal_crypto.KeyAgreement.md)的`x25519`。
- **p256**: `Value0`存放秘密金鑰（32位元組），`Value1`存放未壓縮格式的公開金鑰（65位元組，開頭為`04`）。可直接用於[KeyAgreement](internal_crypto.KeyAgreement.md)的`p256`。其格式與簽章用的`es256`金鑰（DER）不同。

**対応:** SSP 2.9.14（`es384` `es512` `x25519` `p256`為 SSP 2.9.27）
