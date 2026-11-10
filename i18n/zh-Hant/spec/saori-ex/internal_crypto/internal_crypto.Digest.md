# Digest

**カテゴリ:** internal_crypto

計算雜湊值。

- **Argument1**: 演算法名稱（除了[清單](index.md)中的雜湊函式外，也可使用\[SSP 2.9.27\]非供加密用途的檢查值`crc32` / `adler32`）
- **Argument2**: data（預設格式為`text`。也可使用`file`）
- **オプション**: `--data-in=` / `--out=`（預設為`hex`） / `--charset=`

## 記述例

```
Argument0: Digest
Argument1: sha256
Argument2: abc

→ Result: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
```

字串預設會以UTF-8位元組序列進行雜湊。若要計算Shift_JIS位元組序列的雜湊，請加上`--charset=Shift_JIS`。

\[SSP 2.9.27\] `crc32`（CRC-32，與zlib、gzip、PNG相同）和`adler32`（Adler-32，與zlib相同）是用來確認檔案是否損毀的檢查值，不具備密碼學安全性（不可用於偵測竄改；應改用SHA-256等演算法）。結果為4位元組（由高位元組開始）；使用`--out=`的預設值`hex`時，結果會是8個字元（`123456789`的`crc32`為`cbf43926`，`adler32`為`091e01de`）。也可使用`file`。不能用於`HMAC`、`DeriveKey`與`TOTP`的演算法（會回傳400 `unsupported algorithm`）。

**対応:** SSP 2.9.13
