# Compress

**カテゴリ:** internal_data

壓縮資料。

- **Argument1**: 方式：`gzip` / `zlib` / `deflate`（不含標頭的原始deflate）
- **Argument2**: data（預設格式為`text`）
- **選項**: `--data-in=` / `--level=`（0～9。省略時與`-1`使用zlib預設值。超出範圍時回傳400 `out of range`） / `--out=`（預設為`base64`） / `--charset=`

**対応:** SSP 2.9.13
