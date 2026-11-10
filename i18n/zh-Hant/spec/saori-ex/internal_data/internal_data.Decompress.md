# Decompress

**カテゴリ:** internal_data

Decompresses compressed data. `gzip` can also read concatenated members.<br />
If the data is corrupted, truncated, or followed by extraneous data, 400 (`invalid encoding`) is returned. The decompressed size is also limited to 8MB (exceeding this returns 400 `too large`).

- **Argument1**: format: `gzip` / `zlib` / `deflate` / `brotli` / `zstd` (`brotli` and `zstd` support decompression only)
- **Argument2**: data (default format is `base64`)
- **オプション**: `--data-in=` / `--out=` (default is `text`) / `--charset=`

## 記述例

```
Argument0: Decompress
Argument1: gzip
Argument2: H4sIAAAAAAAACvNIzcnJBwCCidH3BQAAAA==

→ Result: Hello
```

**対応:** SSP 2.9.13
