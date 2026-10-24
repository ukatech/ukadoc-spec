# Decompress

**カテゴリ:** internal_data

圧縮されたデータを展開する。`gzip`は複数のメンバーをつないだものも読む。<br />
壊れている・途中で切れている・後ろに余計なデータがあるときは400（`invalid encoding`）。展開した後の大きさも8MBまで（超えると400 `too large`）。

- **Argument1**: 方式：`gzip` / `zlib` / `deflate` / `brotli` / `zstd`（`brotli`と`zstd`は展開だけ）
- **Argument2**: data（既定の形式は`base64`）
- **オプション**: `--data-in=` / `--out=`（既定は`text`） / `--charset=`

## 記述例

```
Argument0: Decompress
Argument1: gzip
Argument2: H4sIAAAAAAAACvNIzcnJBwCCidH3BQAAAA==

→ Result: Hello
```

**対応:** SSP 2.9.13
