# Compress

**カテゴリ:** internal_data

データを圧縮する。

- **Argument1**: 方式：`gzip` / `zlib` / `deflate`（ヘッダの無い生のdeflate）
- **Argument2**: data（既定の形式は`text`）
- **オプション**: `--data-in=` / `--level=`（0～9。省略時はzlibの既定） / `--out=`（既定は`base64`） / `--charset=`

**対応:** SSP 2.9.13
