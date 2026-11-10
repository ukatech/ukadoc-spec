# KeyAgreement

**カテゴリ:** internal_crypto

Derive a shared secret from your private key and the other party's public key, such that both parties obtain the same value (ECDH). The result is 32 bytes and is not hashed (`secp256k1` returns the point's x-coordinate as-is, matching nostr NIP-44; `x25519` returns the RFC 7748 result as-is; `p256` returns the point's x-coordinate as-is).<br />
**Do not use the result directly as an encryption key.** Pass it through `hkdf` (or `hkdf-extract`) in [DeriveKey](internal_crypto.DeriveKey.md) before using it.

- **Argument1**: method: `secp256k1` / `x25519` (\[SSP 2.9.27\]) / `p256` (\[SSP 2.9.27\]. NIST P-256 = secp256r1 = prime256v1)
- **Argument2**: private key (32 bytes; default format is `hex`)
- **Argument3**: other party's public key (default format is `hex`)
- **Options**: `--key-in=` / `--peer-in=` / `--out=` (default is `hex`)

Keys are raw values, not DER / PEM.

- **secp256k1**: The other party's public key can be 32 bytes containing only the x-coordinate (BIP-340 / nostr format), 33 bytes in compressed format, or 65 bytes in uncompressed format.
- **x25519**: Both the private key and the other party's public key are 32 bytes (RFC 7748. SSP performs the private-key bit adjustment (clamping)). A public key that produces an all-zero result (a low-order point) is not accepted.
- **p256**: The other party's public key must be 33 bytes in compressed format (starting with `02` or `03`) or 65 bytes in uncompressed format (starting with `04`). A 32-byte value containing only the x-coordinate is not accepted (unlike `secp256k1`, this is not a valid P-256 public-key format).

If the private key is out of range (0 or greater than or equal to the curve order; for `x25519`, not 32 bytes), or the other party's public key is not a point on the curve or has the wrong length, the result is 400 (`invalid key`). Keys for `x25519` / `p256` can be generated with [GenerateKeyPair](internal_crypto.GenerateKeyPair.md).

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

(NIP-44 conversation key. NIP-44 test vector)

```
Argument0: KeyAgreement
Argument1: x25519
Argument2: 77076d0a7318a57d3c16c17251b26645df4c2f87ebc0992ab177fba51db92c2a
Argument3: de9edb7d7b7dc1b4d35b61c2ece435373f8343c85b78674dadfc7e146f882b4f

→ Result: 4a5d9d5ba4ce2de1728e3bf480350f25e07e21c947d19e3376f09b3c1e161742
```

(RFC 7748 §6.1 test vector. For `p256`, use `i` from RFC 5903 §8.1 as the private key and `04` + the x and y coordinates of `gr` as the other party's public key to obtain `d6840f6b42f6edafd13116e0e12565202fef8e9ece7dce03812464d04b9442de`)

**対応:** SSP 2.9.14 (`x25519` / `p256` are supported in SSP 2.9.27)
