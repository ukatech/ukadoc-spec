# Decrypt

**カテゴリ:** internal_crypto

解密[Encrypt](internal_crypto.Encrypt.md)生成的密文。<br />
如果无法解密，则返回 500（`authentication failed`）。对于带认证的加密，只要密文、认证标签或`--aad=`中任意一项不匹配，就会返回此错误。对于 CBC，如果填充不匹配，也会返回此错误。如果密文短于开头的 nonce / IV（对于带认证的加密，还包括末尾的认证标签），也会返回此错误。对于不带认证的 CTR 和`chacha20`，即使密钥错误也会返回某个值。

- **Argument1**: 算法名称
- **Argument2**: key（默认格式为`text`）
- **Argument3**: ciphertext（默认格式为`base64`）
- **选项**: `--key-in=` / `--ciphertext-in=` / `--aad=` / `--aad-in=` / `--iv=` / `--iv-in=` / `--pack=none` / `--out=`（默认值为`text`） / `--charset=`

使用`--pack=none`时必须指定`--iv=`。不使用`--pack=none`时（nonce / IV 位于密文开头），如果指定`--iv=`，则返回 400（`invalid parameter`）。

**対応:** SSP 2.9.13
