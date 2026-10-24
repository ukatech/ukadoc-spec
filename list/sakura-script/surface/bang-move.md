# `\![move]`

**カテゴリ:** サーフェスコマンド

指定座標まで移動。[※下記参照](notes_move.md)

**対応:** SSP / CROW

## 記述例

```sakurascript
\![move,--X=80,--Y=-400,--time=2500,--base=screen,--base-offset=left.bottom,--move-offset=left.top]本体側が、画面の左下(screen,left.bottom)から数えて、右方向に80pixel上方向に400pixelの座標に、サーフェスの左上ピクセルを合わせた位置(left.top)へ、2.5秒かけて移動する。
```
