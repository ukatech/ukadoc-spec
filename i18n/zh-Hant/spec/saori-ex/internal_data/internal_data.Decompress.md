# Decompress

**カテゴリ:** internal_data

解壓縮資料。`gzip`也能讀取串接多個成員的資料。<br />
資料損毀、未完整或後方有多餘資料時，會回傳400（`invalid encoding`）。解壓縮後的大小上限也是8MB（超過時回傳400 `too large`）。

- **Argument1**: 方式：`gzip` / `zlib` / `deflate` / `brotli` / `zstd`（`brotli`與`zstd`僅支援解壓縮）
- **Argument2**: data（預設格式為`base64`）
- **選項**: `--data-in=` / `--out=`（預設為`text`） / `--charset=`

## 記述例

```
Argument0: Decompress
Argument1: gzip
Argument2: H4sIAAAAAAAACvNIzcnJBwCCidH3BQAAAA==

→ Result: Hello
```

**対応:** SSP 2.9.13
