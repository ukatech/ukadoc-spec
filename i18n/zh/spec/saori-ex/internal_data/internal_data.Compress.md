# Compress

**カテゴリ:** internal_data

压缩数据。

- **Argument1**: 算法：`gzip` / `zlib` / `deflate`（不带标头的原始 deflate）
- **Argument2**: data（默认格式为`text`）
- **选项**: `--data-in=` / `--level=`（0～9。省略时和设为`-1`时使用 zlib 默认值；超出范围会返回 400 `out of range`） / `--out=`（默认为`base64`） / `--charset=`

**対応:** SSP 2.9.13
