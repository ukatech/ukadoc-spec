# Symmetric-key encryption (Encrypt / Decrypt)

The algorithms are as follows (the presence of hyphens or underscores in names, and letter case, are ignored). Other algorithms return 400 (`unsupported algorithm`).

- **aes-256-gcm（recommended） / aes-128-gcm / chacha20-poly1305**: Authenticated encryption. Tampered ciphertext cannot be decrypted. The ciphertext format is “nonce (12 bytes) + ciphertext + authentication tag (16 bytes).”
- **aes-256-cbc / aes-128-cbc**: PKCS#7 padding. The ciphertext format is “IV (16 bytes) + ciphertext.” Tampering cannot be detected, so use this only when exchanging data with other systems.
- **aes-256-ctr**: The ciphertext format is “IV (16 bytes) + ciphertext.” Tampering cannot be detected.
- **chacha20**: \[SSP 2.9.14\] Unauthenticated ChaCha20 (RFC 8439; 12-byte nonce, block counter starts at 0). The ciphertext format is “nonce (12 bytes) + ciphertext.” Tampering cannot be detected, so use this only when exchanging data with other systems that add a separate MAC, such as nostr's NIP-44.

The key length must exactly match the algorithm's key length (32 bytes for AES-256 and ChaCha20, 16 bytes for AES-128); otherwise, 400 (`invalid key`) is returned. To derive a key from a password, use [DeriveKey](internal_crypto.DeriveKey.md).<br />
A nonce / IV is generated randomly for each encryption and prepended to the ciphertext. `--iv=` (specifying a nonce / IV) and `--pack=none` (not prepending it) are intended only for cases where another system passes the nonce separately. **Using the same nonce / IV twice with the same key breaks GCM, ChaCha20-Poly1305, and CTR as ciphers** (plaintext is exposed and tampering becomes possible). Do not use a fixed value for `--iv=` and reuse it.

All errors in options return 400 (`invalid parameter`).

- `--aad=` was specified for an unauthenticated mode (CBC, CTR, or `chacha20`).
- The length of `--iv=` does not exactly match the nonce / IV length for the mode (“12 bytes” or “16 bytes” above).
- A value other than `none` was specified for `--pack=`.
