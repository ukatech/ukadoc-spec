# `\![set,balloonoffset,x,y]`

**カテゴリ:** balloon、文字指令

將 balloon 的 offset 值變更為 XY 座標。使用者透過拖曳 balloon 移動所決定的座標會加到此值上，據此決定 balloon 的顯示座標。<br />
一般指定數值時會忽略 descript.txt 的預設 offset 值；若在數值前加上 @，則表示以 descript.txt 或 surfaces.txt 中的 offset 值為基準指定相對座標。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![set,balloonoffset,100,-50]バルーン位置の基準点をX:100,Y:-50に移動。
```

```sakurascript
\![set,balloonoffset,@100,@-50]バルーン位置の基準点をdescript.txtやsurfaces.txtの指定プラスX:100,Y:-50(相対座標)に移動。
```
