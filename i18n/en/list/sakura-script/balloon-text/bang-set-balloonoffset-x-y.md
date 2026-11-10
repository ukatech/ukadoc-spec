# `\![set,balloonoffset,x,y]`

**カテゴリ:** Balloon, text command

Changes the balloon offset to the specified XY coordinates. The coordinates set by the user by dragging the balloon are added to this value to determine the balloon's display position.<br />
Normally, specifying a number overrides the default offset value in descript.txt. Prefixing the number with @ instead specifies coordinates relative to the offset values in descript.txt or surfaces.txt.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![set,balloonoffset,100,-50]バルーン位置の基準点をX:100,Y:-50に移動。
```

```sakurascript
\![set,balloonoffset,@100,@-50]バルーン位置の基準点をdescript.txtやsurfaces.txtの指定プラスX:100,Y:-50(相対座標)に移動。
```
