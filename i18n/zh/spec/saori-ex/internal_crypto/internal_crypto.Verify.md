# Verify

**カテゴリ:** internal_crypto

使用公钥验证签名。验证成功时返回`1`，失败时返回`0`（签名长度不符时也返回`0`）。也可以传入私钥代替公钥（`bip340`除外）。<br />
对于`bip340`，32 字节但不是曲线上点的公钥也会按照 BIP-340 的规定返回`0`（长度不符时返回 400 `invalid key`）。

- **Argument1**: 方式（参见[公钥密码学](internal_crypto_pkey.md)）
- **Argument2**: 公钥
- **Argument3**: data（默认格式为`text`）
- **Argument4**: signature（默认格式为`base64url`。`bip340`为`hex`）
- **选项**: `--data-in=` / `--signature-in=` / `--charset=` / `--key-in=`（仅限`bip340`。默认值为`hex`）

**対応:** SSP 2.9.14
