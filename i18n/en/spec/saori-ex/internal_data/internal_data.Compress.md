# Compress

**カテゴリ:** internal_data

Compresses data.

- **Argument1**: algorithm: `gzip` / `zlib` / `deflate` (raw deflate without a header)
- **Argument2**: data (default format is `text`)
- **Options**: `--data-in=` / `--level=` (0–9. If omitted or set to `-1`, zlib's default is used. Values outside the range return 400 `out of range`) / `--out=` (default is `base64`) / `--charset=`

**対応:** SSP 2.9.13
