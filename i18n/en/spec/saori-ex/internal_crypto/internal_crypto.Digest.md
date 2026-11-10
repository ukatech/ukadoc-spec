# Digest

**カテゴリ:** internal_crypto

Calculates a hash value.

- **Argument1**: Algorithm name (hash functions in the [list](index.md), as well as `crc32` / `adler32`, checksums that are not for cryptographic use \[SSP 2.9.27\])
- **Argument2**: data (the default format is `text`; `file` can also be used)
- **Options**: `--data-in=` / `--out=` (default is `hex`) / `--charset=`

## 記述例

```
Argument0: Digest
Argument1: sha256
Argument2: abc

→ Result: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
```

Strings are hashed by default as UTF-8 byte sequences. To hash a Shift_JIS byte sequence, specify `--charset=Shift_JIS`.

\[SSP 2.9.27\] `crc32` (CRC-32, same as zlib, gzip, and PNG) and `adler32` (Adler-32, same as zlib) are checksums used to verify that a file is not corrupted; they are not cryptographically secure (do not use them to detect tampering; use SHA-256 or similar for that). The result is 4 bytes (most significant byte first), and with the default `hex` for `--out=`, it is 8 characters (`crc32` of `123456789` is `cbf43926`, and `adler32` is `091e01de`). `file` can also be used. These algorithms cannot be used with `HMAC`, `DeriveKey`, or `TOTP` (400 `unsupported algorithm`).

**対応:** SSP 2.9.13
