# internal_crypto

Hashing, MAC, symmetric-key encryption, key derivation, password hashing, data protection (DPAPI), one-time passwords (TOTP), public-key signatures and key agreement.<br />
The algorithm names for `Digest` / `HMAC` (and `--digest=` for `DeriveKey` / `TOTP`) are as follows. Hyphens, underscores, and letter case are ignored (`SHA-256`, `sha_256`, and `sha256` are equivalent). Other names return 400 (`unsupported algorithm`).<br />
`md5` `sha1` `sha224` `sha256` `sha384` `sha512` `sha512-256` `sha3-224` `sha3-256` `sha3-384` `sha3-512` `blake2b512` `blake2s256`<br />
`Digest` also accepts the non-cryptographic checksums `crc32` / `adler32` (\[SSP 2.9.27\]).<br />
Available algorithm names and options can be checked with [internal_system's Describe](../internal_system/internal_system.Describe.md).

## 一覧

- [Digest](internal_crypto.Digest.md)
- [HMAC](internal_crypto.HMAC.md)
- [Compare](internal_crypto.Compare.md)
- [Symmetric-key encryption (Encrypt / Decrypt)](internal_crypto_cipher.md)
- [Encrypt](internal_crypto.Encrypt.md)
- [Decrypt](internal_crypto.Decrypt.md)
- [DeriveKey](internal_crypto.DeriveKey.md)
- [HashPassword](internal_crypto.HashPassword.md)
- [VerifyPassword](internal_crypto.VerifyPassword.md)
- [Protect](internal_crypto.Protect.md)
- [Unprotect](internal_crypto.Unprotect.md)
- [TOTP](internal_crypto.TOTP.md)
- [Public-key cryptography (GenerateKeyPair / Sign / Verify / KeyAgreement)](internal_crypto_pkey.md)
- [GenerateKeyPair](internal_crypto.GenerateKeyPair.md)
- [Sign](internal_crypto.Sign.md)
- [Verify](internal_crypto.Verify.md)
- [KeyAgreement](internal_crypto.KeyAgreement.md)
