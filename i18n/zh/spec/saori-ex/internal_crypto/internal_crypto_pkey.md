# 公钥加密（GenerateKeyPair / Sign / Verify / KeyAgreement）

签名算法如下（名称中的连字符和下划线有无、以及大小写均不区分）。其他算法会返回 400（`unsupported algorithm`）。`ed25519`～`ps512`分别生成与 JWT（JWS）的 alg `EdDSA` / `ES256` / `ES384` / `ES512` / `RS256` / `RS384` / `RS512` / `PS256` / `PS384` / `PS512`相同的签名。\[SSP 2.9.27\] 新增了`es384` `es512` `rs384` `rs512` `ps384` `ps512`。

- **ed25519**: Ed25519（RFC 8032）。签名为 64 字节。
- **es256 / es384 / es512**: ECDSA（es256 为 P-256 + SHA-256，es384 为 P-384 + SHA-384，es512 为 P-521 + SHA-512）。签名为 r‖s，长度为 64 / 96 / 132 字节（格式与 JWS 相同，不是 DER 格式。P-521 的 r 和 s 各为 66 字节）。
- **rs256 / rs384 / rs512**: RSA（RSASSA-PKCS1-v1_5）+ SHA-256 / SHA-384 / SHA-512。
- **ps256 / ps384 / ps512**: RSA（RSASSA-PSS）+ SHA-256 / SHA-384 / SHA-512。MGF1 使用相同的哈希算法，盐的长度等于该哈希的长度（32 / 48 / 64 字节。与 JWA 的 PS256 / PS384 / PS512 相同）。
- **bip340**: secp256k1 的 Schnorr 签名（BIP-340。与 nostr 事件的签名相同）。签名为 64 字节。消息不经哈希，直接签名（长度不限；nostr 中将事件 ID（32 字节）通过`--data-in=hex`传入）。密钥的传递方式与其他算法不同（见下文）。

密钥以单行 DER base64 或 PEM 格式传递。[GenerateKeyPair](internal_crypto.GenerateKeyPair.md)输出前一种格式（私钥为 PKCS#8，公钥为 SubjectPublicKeyInfo）。<br />
PEM 含有换行符，无法写入 SAORI 标头，因此请传入将换行符替换为空格的内容（或去掉换行符后合并成一行的内容）。如果以`-----BEGIN`开头，则按 PEM 处理，并将`-----BEGIN ...-----`与`-----END`之间的内容作为 base64 读取。<br />
私钥除 PKCS#8（`PRIVATE KEY`）外，RSA 还支持 PKCS#1（`RSA PRIVATE KEY`），ECDSA 还支持 SEC1（`EC PRIVATE KEY`）。不支持读取经密码加密的私钥。公钥格式为 SubjectPublicKeyInfo（`PUBLIC KEY`）。<br />
RSA 密钥长度必须为 2048～4096 位，ECDSA 密钥必须使用算法指定的曲线（es256 为 P-256，es384 为 P-384，es512 为 P-521）。无法读取的密钥，以及类型或大小与算法不匹配的密钥会返回 400（`invalid key`）。

**`bip340`使用原始值，而非 DER / PEM**。私钥为 32 字节，公钥仅包含 x 坐标，为 32 字节（BIP-340 格式。与 nostr 公钥相同），默认格式为`hex`。可以通过`--key-in=`更改读取方式（使用`--key-in=bech32`时，可以直接传入`nsec1...` / `npub1...`）。<br />
密钥长度不正确、私钥为 0 或不小于曲线阶数时，会返回 400（`invalid key`）。`--key-in=`仅适用于`bip340`（用于其他算法时会返回 400 `invalid parameter`）。

[KeyAgreement](internal_crypto.KeyAgreement.md)使用的密钥（`secp256k1` `x25519` `p256`）同样是原始值（格式请参阅`KeyAgreement`的说明）。
