# Decompress

**カテゴリ:** internal_data

解压缩数据。`gzip`也可以读取由多个成员串联而成的数据。<br />
数据损坏、被截断或末尾存在多余数据时，会返回 400（`invalid encoding`）。解压后的大小也不得超过 8MB（超出时会返回 400 `too large`）。

- **Argument1**: 算法：`gzip` / `zlib` / `deflate` / `brotli` / `zstd`（`brotli`和`zstd`仅支持解压）
- **Argument2**: data（默认格式为`base64`）
- **选项**: `--data-in=` / `--out=`（默认为`text`） / `--charset=`

## 記述例

```
Argument0: Decompress
Argument1: gzip
Argument2: H4sIAAAAAAAACvNIzcnJBwCCidH3BQAAAA==

→ Result: Hello
```

**対応:** SSP 2.9.13
