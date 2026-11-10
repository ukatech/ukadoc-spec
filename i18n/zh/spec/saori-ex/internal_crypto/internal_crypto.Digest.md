# Digest

**カテゴリ:** internal_crypto

计算哈希值。

- **Argument1**: 算法名称（除[列表](index.md)中的哈希函数外，还包括 \[SSP 2.9.27\] 非加密用途的校验值`crc32` / `adler32`）
- **Argument2**: data（默认格式为`text`，也可使用`file`）
- **选项**: `--data-in=` / `--out=`（默认值为`hex`） / `--charset=`

## 記述例

```
Argument0: Digest
Argument1: sha256
Argument2: abc

→ Result: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
```

字符串默认按 UTF-8 字节序列进行哈希。若需要计算 Shift_JIS 字节序列的哈希，请指定`--charset=Shift_JIS`。

\[SSP 2.9.27\] `crc32`（CRC-32，与 zlib、gzip、PNG 相同）和`adler32`（Adler-32，与 zlib 相同）是用于检查文件是否损坏的校验值，不具备密码学强度（不能用于检测篡改；检测篡改应使用 SHA-256 等算法）。结果为 4 字节（从高位开始），使用`--out=`的默认值`hex`时会得到 8 个字符（`123456789`的`crc32`为`cbf43926`，`adler32`为`091e01de`）。也可使用`file`。不能用于`HMAC`、`DeriveKey`、`TOTP`的算法（返回 400 `unsupported algorithm`）。

**対応:** SSP 2.9.13
