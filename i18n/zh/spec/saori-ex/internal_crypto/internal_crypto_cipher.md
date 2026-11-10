# 对称密钥加密（Encrypt / Decrypt）

算法如下（名称中的连字符和下划线有无、以及大小写均不区分）。其他算法会返回 400（`unsupported algorithm`）。

- **aes-256-gcm（推荐） / aes-128-gcm / chacha20-poly1305**: 带认证的加密。被篡改的密文无法解密。密文格式为“nonce（12 字节）＋密文＋认证标签（16 字节）”。
- **aes-256-cbc / aes-128-cbc**: 使用 PKCS#7 填充。密文格式为“IV（16 字节）＋密文”。无法检测篡改，因此仅在与其他系统交互时使用。
- **aes-256-ctr**: 密文格式为“IV（16 字节）＋密文”。无法检测篡改。
- **chacha20**: \[SSP 2.9.14\] 不带认证的 ChaCha20（RFC 8439。nonce 为 12 字节，块计数器从 0 开始）。密文格式为“nonce（12 字节）＋密文”。无法检测篡改，因此仅在与其他系统（如 nostr 的 NIP-44，这类单独附加 MAC 的方式）交互时使用。

密钥（key）的长度必须恰好等于算法要求的密钥长度（AES-256 和 ChaCha20 为 32 字节，AES-128 为 16 字节），否则会返回 400（`invalid key`）。从密码生成密钥时，请使用[DeriveKey](internal_crypto.DeriveKey.md)。<br />
每次加密时都应使用随机数生成 nonce / IV，并将其附加到密文开头。`--iv=`（指定 nonce / IV）和`--pack=none`（不附加到开头）仅用于与其他系统单独传递 nonce 的情况。**使用相同密钥重复使用相同 nonce / IV 会导致 GCM、ChaCha20-Poly1305 和 CTR 被攻破**（明文会泄露，且可被篡改）。请勿在`--iv=`中填写固定值并重复使用。

任何选项错误都会返回 400（`invalid parameter`）。

- 将`--aad=`用于不带认证的算法（CBC、CTR、`chacha20`）。
- `--iv=`的长度与该算法的 nonce / IV 长度（上文所述的“12 字节”或“16 字节”）不一致。
- `--pack=`的值不是`none`。
