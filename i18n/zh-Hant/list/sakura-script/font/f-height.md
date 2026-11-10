# `\f[height,数値]`

**カテゴリ:** 文字變更指令

將文字變更為指定字型大小。<br />
可以使用 + 或 - 進行相對調整。<br />
也可以使用樣式表的尺寸指定方式。<br />
指定 default 時，會恢復 balloon 設定的預設值。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\f[height,15]15pixelで表示。\f[height,+3]3pixel大きくする。\f[height,200%]デフォルトサイズの200%で表示。\f[height,default]元のサイズに戻す。
```
