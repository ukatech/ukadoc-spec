# Public-key cryptography (GenerateKeyPair / Sign / Verify / KeyAgreement)

The supported signature algorithms are as follows (hyphens and underscores in names, and letter case, are ignored). Other algorithms return 400 (`unsupported algorithm`). `ed25519` through `ps512` produce signatures equivalent to the JWT (JWS) alg values `EdDSA` / `ES256` / `ES384` / `ES512` / `RS256` / `RS384` / `RS512` / `PS256` / `PS384` / `PS512`, respectively. \[SSP 2.9.27\] `es384` `es512` `rs384` `rs512` `ps384` `ps512` were added.

- **ed25519**: Ed25519 (RFC 8032). Signatures are 64 bytes.
- **es256 / es384 / es512**: ECDSA (es256 is P-256 + SHA-256, es384 is P-384 + SHA-384, es512 is P-521 + SHA-512). Signatures are r‖s, 64 / 96 / 132 bytes (the same format as JWS, not DER; r and s for P-521 are 66 bytes each).
- **rs256 / rs384 / rs512**: RSA (RSASSA-PKCS1-v1_5) + SHA-256 / SHA-384 / SHA-512.
- **ps256 / ps384 / ps512**: RSA (RSASSA-PSS) + SHA-256 / SHA-384 / SHA-512. MGF1 uses the same hash, and the salt length is the hash length (32 / 48 / 64 bytes; the same as JWA's PS256 / PS384 / PS512).
- **bip340**: secp256k1 Schnorr signature (BIP-340; the same as nostr event signatures). Signatures are 64 bytes. The message is signed as-is without hashing (any length is allowed; for nostr, pass the event ID (32 bytes) using `--data-in=hex`). Keys are passed differently from the other algorithms (see below).

Pass keys as single-line DER base64 or PEM. [GenerateKeyPair](internal_crypto.GenerateKeyPair.md) outputs the former (private key is PKCS#8, public key is SubjectPublicKeyInfo).<br />
PEM includes newlines and cannot be written in a SAORI header, so pass it with newlines replaced by spaces (or with newlines removed to make it a single line). If it starts with `-----BEGIN`, it is read as PEM, with the content between `-----BEGIN ...-----` and `-----END` read as base64.<br />
Private keys can be read in PKCS#8 (`PRIVATE KEY`), as well as PKCS#1 (`RSA PRIVATE KEY`) for RSA and SEC1 (`EC PRIVATE KEY`) for ECDSA. Password-encrypted private keys cannot be read. Public keys use SubjectPublicKeyInfo (`PUBLIC KEY`).<br />
RSA keys must be 2048–4096 bits, and ECDSA keys must use the curve for the algorithm (P-256 for es256, P-384 for es384, P-521 for es512). Unreadable keys, or keys whose type or size does not match the algorithm, return 400 (`invalid key`).

**`bip340` uses raw values, not DER / PEM**. The private key is 32 bytes; the public key is only the 32-byte x-coordinate (BIP-340 format, the same as a nostr public key). The default format is `hex`. The input format can be changed with `--key-in=` (with `--key-in=bech32`, `nsec1...` / `npub1...` can be passed as-is).<br />
Keys with an incorrect length, or private keys equal to 0 or greater than or equal to the curve order, return 400 (`invalid key`). `--key-in=` can only be used with `bip340` (using it with another algorithm returns 400 `invalid parameter`).

The keys for [KeyAgreement](internal_crypto.KeyAgreement.md) (`secp256k1` `x25519` `p256`) are also raw values (see the `KeyAgreement` description for their format).
