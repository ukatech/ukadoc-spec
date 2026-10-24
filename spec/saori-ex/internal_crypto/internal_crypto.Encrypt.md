# Encrypt

**カテゴリ:** internal_crypto

共通鍵暗号で暗号化する。

- **Argument1**: アルゴリズム名（[共通鍵暗号](internal_crypto_cipher.md)を参照）
- **Argument2**: key（既定の形式は`text`）
- **Argument3**: data（既定の形式は`text`）
- **オプション**: `--key-in=` / `--data-in=` / `--aad=`（追加認証データ。認証付き暗号だけ。`--aad-in=`、既定の形式は`text`） / `--iv=`（`--iv-in=`、既定の形式は`hex`） / `--pack=none` / `--out=`（既定は`base64`） / `--charset=`

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
