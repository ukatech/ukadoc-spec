# internal_jwt

Creation and verification of JWTs (RFC 7519). The format is limited to the compact form of JWS (`header.payload.signature`).<br />
The supported algorithms are as follows (case-insensitive in arguments and `--alg=`). Any other value, including `none`, returns 400 (`unsupported algorithm`).

- **HS256 / HS384 / HS512**: HMAC (symmetric key). Pass the key in the format specified by `--key-in=` (default is `text`; strings are UTF-8). If the key is shorter than the hash length (32 bytes for HS256, 48 bytes for HS384, and 64 bytes for HS512), 400 is returned (`invalid key`; required by RFC 7518).
- **RS256 / RS384 / RS512 / PS256 / PS384 / PS512 / ES256 / ES384 / ES512 / EdDSA**: Public-key cryptography. Key handling and details of the algorithms are the same as in [Public-key cryptography in internal_crypto](../internal_crypto/internal_crypto_pkey.md) (`EdDSA` supports only Ed25519; the curves for `ES256`, `ES384`, and `ES512` are P-256, P-384, and P-521, respectively). `--key-in=` cannot be used (400 `invalid parameter`). \[SSP 2.9.27\] `RS384`, `RS512`, `PS384`, `PS512`, `ES384`, and `ES512` were added.

## 一覧

- [Sign](internal_jwt.Sign.md)
- [Verify](internal_jwt.Verify.md)
