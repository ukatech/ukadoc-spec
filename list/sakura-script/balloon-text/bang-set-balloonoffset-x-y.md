# `\![set,balloonoffset,x,y]`

**カテゴリ:** バルーン、テキストコマンド

バルーンのオフセット値をXY座標に変更。この値にユーザーがバルーンドラッグ移動で決定した座標が加算され、バルーン表示座標が決まる。<br />
通常に数値を指定すればdescript.txtのデフォルトのoffset値は無視されるが、頭に@をつけるとdescript.txtやsurfaces.txt内のオフセット値からの相対座標指定となる。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![set,balloonoffset,100,-50]バルーン位置の基準点をX:100,Y:-50に移動。
```

```sakurascript
\![set,balloonoffset,@100,@-50]バルーン位置の基準点をdescript.txtやsurfaces.txtの指定プラスX:100,Y:-50(相対座標)に移動。
```
