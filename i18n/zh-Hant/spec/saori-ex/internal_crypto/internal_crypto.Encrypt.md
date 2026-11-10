# Encrypt

**カテゴリ:** internal_crypto

使用對稱式金鑰加密進行加密。

- **Argument1**: 演算法名稱（請參閱[對稱式金鑰加密](internal_crypto_cipher.md)）
- **Argument2**: key（預設格式為`text`）
- **Argument3**: data（預設格式為`text`）
- **オプション**: `--key-in=` / `--data-in=` / `--aad=`（額外驗證資料。僅限認證加密。`--aad-in=`，預設格式為`text`） / `--iv=`（`--iv-in=`，預設格式為`hex`） / `--pack=none` / `--out=`（預設為`base64`） / `--charset=`

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
