# `\f[height,数値]`

**カテゴリ:** 文字更改命令

将文本更改为指定字号。<br />
可以使用 + 或 - 进行相对调整。<br />
也可以使用样式表指定字号。<br />
指定 default 时恢复为 balloon 设置的默认值。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\f[height,15]15pixelで表示。\f[height,+3]3pixel大きくする。\f[height,200%]デフォルトサイズの200%で表示。\f[height,default]元のサイズに戻す。
```
