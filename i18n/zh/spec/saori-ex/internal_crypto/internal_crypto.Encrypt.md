# Encrypt

**カテゴリ:** internal_crypto

Encrypt data using symmetric-key encryption.

- **Argument1**: algorithm name (see [symmetric-key encryption](internal_crypto_cipher.md))
- **Argument2**: key (default format is `text`)
- **Argument3**: data (default format is `text`)
- **Options**: `--key-in=` / `--data-in=` / `--aad=` (additional authenticated data; authenticated encryption only; `--aad-in=`, default format is `text`) / `--iv=` (`--iv-in=`, default format is `hex`) / `--pack=none` / `--out=` (default is `base64`) / `--charset=`

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
