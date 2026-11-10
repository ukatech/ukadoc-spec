# `\![set,balloonoffset,x,y]`

**カテゴリ:** balloon, text command

Changes the balloon offset values to XY coordinates. The coordinates set by the user by dragging the balloon are added to these values to determine the balloon's display coordinates.<br />
Normally, specifying numbers ignores the default offset values in descript.txt, but prefixing them with @ specifies coordinates relative to the offset values in descript.txt or surfaces.txt.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![set,balloonoffset,100,-50]バルーン位置の基準点をX:100,Y:-50に移動。
```

```sakurascript
\![set,balloonoffset,@100,@-50]バルーン位置の基準点をdescript.txtやsurfaces.txtの指定プラスX:100,Y:-50(相対座標)に移動。
```
