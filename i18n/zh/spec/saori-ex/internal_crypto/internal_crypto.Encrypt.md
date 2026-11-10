# Encrypt

**カテゴリ:** internal_crypto

使用对称密钥加密进行加密。

- **Argument1**: 算法名称（参阅[对称密钥加密](internal_crypto_cipher.md)）
- **Argument2**: key（默认格式为`text`）
- **Argument3**: data（默认格式为`text`）
- **选项**: `--key-in=` / `--data-in=` / `--aad=`（附加认证数据，仅用于带认证的加密；`--aad-in=`，默认格式为`text`） / `--iv=`（`--iv-in=`，默认格式为`hex`） / `--pack=none` / `--out=`（默认值为`base64`） / `--charset=`

## 記述例

```
Argument0: Encrypt
Argument1: aes-256-gcm
Argument2: 000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f
Argument3: secret message
Argument4: --key-in=hex

→ Result: （毎回違うbase64）
```

**対応:** SSP 2.9.13
