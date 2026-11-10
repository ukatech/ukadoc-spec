# `\![set,balloonoffset,x,y]`

**カテゴリ:** 气球、文本命令

将气球的偏移值改为 XY 坐标。用户通过拖动气球确定的坐标会加到此值上，并据此确定气球的显示坐标。<br />
通常指定数值时，会忽略 descript.txt 中的默认 offset 值；在数值前加上 @ 时，则表示相对于 descript.txt 或 surfaces.txt 中偏移值的坐标。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![set,balloonoffset,100,-50]バルーン位置の基準点をX:100,Y:-50に移動。
```

```sakurascript
\![set,balloonoffset,@100,@-50]バルーン位置の基準点をdescript.txtやsurfaces.txtの指定プラスX:100,Y:-50(相対座標)に移動。
```
