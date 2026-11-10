# internal_crypto

哈希、MAC、对称密钥加密、密钥派生、密码哈希、数据保护（DPAPI）、一次性密码（TOTP）、公钥加密签名和密钥协商。<br />
`Digest` / `HMAC`的算法名称（`DeriveKey` / `TOTP`的`--digest=`也相同）如下。是否带连字符或下划线，以及大小写均不影响识别（`SHA-256`和`sha_256`都与`sha256`相同）。其他算法返回400（`unsupported algorithm`）。<br />
`md5` `sha1` `sha224` `sha256` `sha384` `sha512` `sha512-256` `sha3-224` `sha3-256` `sha3-384` `sha3-512` `blake2b512` `blake2s256`<br />
`Digest`还接受这些算法之外的非加密校验值`crc32` / `adler32`（\[SSP 2.9.27\]）。<br />
可通过[internal_system的Describe](../internal_system/internal_system.Describe.md)查询可用的算法名称和选项。

## 一覧

- [Digest](internal_crypto.Digest.md)
- [HMAC](internal_crypto.HMAC.md)
- [Compare](internal_crypto.Compare.md)
- [对称密钥加密（Encrypt / Decrypt）](internal_crypto_cipher.md)
- [Encrypt](internal_crypto.Encrypt.md)
- [Decrypt](internal_crypto.Decrypt.md)
- [DeriveKey](internal_crypto.DeriveKey.md)
- [HashPassword](internal_crypto.HashPassword.md)
- [VerifyPassword](internal_crypto.VerifyPassword.md)
- [Protect](internal_crypto.Protect.md)
- [Unprotect](internal_crypto.Unprotect.md)
- [TOTP](internal_crypto.TOTP.md)
- [公钥加密（GenerateKeyPair / Sign / Verify / KeyAgreement）](internal_crypto_pkey.md)
- [GenerateKeyPair](internal_crypto.GenerateKeyPair.md)
- [Sign](internal_crypto.Sign.md)
- [Verify](internal_crypto.Verify.md)
- [KeyAgreement](internal_crypto.KeyAgreement.md)
