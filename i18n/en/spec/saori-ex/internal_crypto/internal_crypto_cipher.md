# Symmetric-key encryption (Encrypt / Decrypt)

The supported algorithms are as follows (hyphens and underscores in names, and letter case, are ignored). Other algorithms return 400 (`unsupported algorithm`).

- **aes-256-gcm (recommended) / aes-128-gcm / chacha20-poly1305**: Authenticated encryption. Tampered ciphertext cannot be decrypted. The ciphertext format is “nonce (12 bytes) + ciphertext + authentication tag (16 bytes).”
- **aes-256-cbc / aes-128-cbc**: PKCS#7 padding. The ciphertext format is “IV (16 bytes) + ciphertext.” This cannot detect tampering, so use it only when communicating with other systems.
- **aes-256-ctr**: The ciphertext format is “IV (16 bytes) + ciphertext.” This cannot detect tampering.
- **chacha20**: \[SSP 2.9.14\] Unauthenticated ChaCha20 (RFC 8439; 12-byte nonce, block counter starts at 0). The ciphertext format is “nonce (12 bytes) + ciphertext.” This cannot detect tampering, so use it only when communicating with other systems that use a separate MAC, such as nostr's NIP-44.

The key length must exactly match the algorithm's key length (32 bytes for AES-256 and ChaCha20, 16 bytes for AES-128); otherwise, 400 (`invalid key`) is returned. To derive a key from a password, use [DeriveKey](internal_crypto.DeriveKey.md).<br />
Generate the nonce / IV randomly for each encryption and prepend it to the ciphertext. `--iv=` (to specify a nonce / IV) and `--pack=none` (not to prepend it) are intended only for cases where another system passes the nonce separately. **Reusing the same nonce / IV twice with the same key breaks GCM, ChaCha20-Poly1305, and CTR as encryption** (plaintext is exposed and tampering becomes possible). Do not use a fixed value for `--iv=` or reuse it.

All invalid options return 400 (`invalid parameter`).

- `--aad=` was specified for an unauthenticated algorithm (CBC, CTR, or `chacha20`).
- The length of `--iv=` is not exactly the length of the algorithm's nonce / IV (“12 bytes” or “16 bytes” above).
- A value other than `none` was specified for `--pack=`.
