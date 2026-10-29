# internal_crypto

ハッシュ・MAC・共通鍵暗号・鍵の導出・パスワードのハッシュ・データの保護（DPAPI）・ワンタイムパスワード（TOTP）・公開鍵暗号の署名と鍵共有。<br />
`Digest` / `HMAC`のアルゴリズム名（`DeriveKey` / `TOTP`の`--digest=`も同じ）は次のとおり。ハイフン・アンダースコアの有無と大文字小文字は区別しない（`SHA-256`も`sha_256`も`sha256`と同じ）。これ以外は400（`unsupported algorithm`）。<br />
`md5` `sha1` `sha224` `sha256` `sha384` `sha512` `sha512-256` `sha3-224` `sha3-256` `sha3-384` `sha3-512` `blake2b512` `blake2s256`

## 一覧

- [Digest](internal_crypto.Digest.md)
- [HMAC](internal_crypto.HMAC.md)
- [Compare](internal_crypto.Compare.md)
- [共通鍵暗号（Encrypt / Decrypt）](internal_crypto_cipher.md)
- [Encrypt](internal_crypto.Encrypt.md)
- [Decrypt](internal_crypto.Decrypt.md)
- [DeriveKey](internal_crypto.DeriveKey.md)
- [HashPassword](internal_crypto.HashPassword.md)
- [VerifyPassword](internal_crypto.VerifyPassword.md)
- [Protect](internal_crypto.Protect.md)
- [Unprotect](internal_crypto.Unprotect.md)
- [TOTP](internal_crypto.TOTP.md)
- [公開鍵暗号（GenerateKeyPair / Sign / Verify / KeyAgreement）](internal_crypto_pkey.md)
- [GenerateKeyPair](internal_crypto.GenerateKeyPair.md)
- [Sign](internal_crypto.Sign.md)
- [Verify](internal_crypto.Verify.md)
- [KeyAgreement](internal_crypto.KeyAgreement.md)
