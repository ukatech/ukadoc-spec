# internal_crypto

雜湊、MAC、對稱式金鑰加密、金鑰衍生、密碼雜湊、資料保護（DPAPI）、一次性密碼（TOTP）、公開金鑰密碼學的簽章與金鑰協議。<br />
`Digest` / `HMAC`的演算法名稱（`DeriveKey` / `TOTP`的`--digest=`也相同）如下。連字號與底線是否存在，以及大小寫皆不區分（`SHA-256`、`sha_256`和`sha256`都視為相同）。其他值會回傳400（`unsupported algorithm`）。<br />
`md5` `sha1` `sha224` `sha256` `sha384` `sha512` `sha512-256` `sha3-224` `sha3-256` `sha3-384` `sha3-512` `blake2b512` `blake2s256`<br />
只有`Digest`除了上述演算法外，也接受非供加密用途的檢查值`crc32` / `adler32`（\[SSP 2.9.27\]）。<br />
可使用的演算法名稱與選項，可透過[internal_system的Describe](../internal_system/internal_system.Describe.md)查詢。

## 一覧

- [Digest](internal_crypto.Digest.md)
- [HMAC](internal_crypto.HMAC.md)
- [Compare](internal_crypto.Compare.md)
- [對稱式金鑰加密（Encrypt / Decrypt）](internal_crypto_cipher.md)
- [Encrypt](internal_crypto.Encrypt.md)
- [Decrypt](internal_crypto.Decrypt.md)
- [DeriveKey](internal_crypto.DeriveKey.md)
- [HashPassword](internal_crypto.HashPassword.md)
- [VerifyPassword](internal_crypto.VerifyPassword.md)
- [Protect](internal_crypto.Protect.md)
- [Unprotect](internal_crypto.Unprotect.md)
- [TOTP](internal_crypto.TOTP.md)
- [公開金鑰密碼學（GenerateKeyPair / Sign / Verify / KeyAgreement）](internal_crypto_pkey.md)
- [GenerateKeyPair](internal_crypto.GenerateKeyPair.md)
- [Sign](internal_crypto.Sign.md)
- [Verify](internal_crypto.Verify.md)
- [KeyAgreement](internal_crypto.KeyAgreement.md)
