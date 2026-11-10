# GenerateKeyPair

**カテゴリ:** internal_crypto

Creates a public-key cryptography key pair. `Value0` contains the private key (PKCS#8), and `Value1` contains the public key (SubjectPublicKeyInfo), both base64-encoded DER. `Result` is the same as `Value0`.<br />
RSA key generation can take several seconds, so [`--async`](../async.md) is recommended (for asynchronous calls, the private key is placed in Reference4 and the public key in Reference5).<br />
If needed, wrap the private key with [Protect](internal_crypto.Protect.md) before saving it.

- **Argument1**: Algorithm: `ed25519` / `es256` (P-256) / `es384` (P-384. \[SSP 2.9.27\]) / `es512` (P-521. \[SSP 2.9.27\]) / `rsa-2048` / `rsa-3072` / `rsa-4096` (RSA keys can be used with any of `rs256` through `ps512`) / `bip340` (secp256k1) / `x25519` (\[SSP 2.9.27\]) / `p256` (\[SSP 2.9.27\])

Only for `bip340`, `x25519`, and `p256`, the values are raw rather than DER, and both are in lowercase hexadecimal.

- **bip340**: `Value0` contains the private key (32 bytes), and `Value1` contains the public key with only the x-coordinate (32 bytes). To convert them to nostr `nsec` / `npub`, use `--out=bech32` with [Convert](../internal_data/internal_data.Convert.md). This key can also be used as-is with `secp256k1` in [KeyAgreement](internal_crypto.KeyAgreement.md).
- **x25519**: `Value0` contains the private key (32 bytes), and `Value1` contains the public key (32 bytes). It can be used as-is with `x25519` in [KeyAgreement](internal_crypto.KeyAgreement.md).
- **p256**: `Value0` contains the private key (32 bytes), and `Value1` contains the uncompressed public key (65 bytes; begins with `04`). It can be used as-is with `p256` in [KeyAgreement](internal_crypto.KeyAgreement.md). Its format differs from the signing key for `es256` (DER).

**対応:** SSP 2.9.14 (`es384` `es512` `x25519` `p256` are supported in SSP 2.9.27)
