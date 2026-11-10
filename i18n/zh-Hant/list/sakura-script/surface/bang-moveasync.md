# `\![moveasync]`

**カテゴリ:** Surface command

Move asynchronously to the specified coordinates. [※See below](bang-moveasync.note.md)

Movement started by `\![moveasync]` can be stopped midway using `\![moveasync,cancel]`.

**対応:** SSP

## 記述例

```sakurascript
\1\![moveasync,--X=-175,--Y=200,--time=5000,--base=screen,--base-offset=right.top,--move-offset=right.bottom]相方側が、現在表示されているモニタの右上(screen,right.top)から数えて、左方向に175pixel下方向に400pixelの座標に、サーフェスの右下ピクセルを合わせた位置(right.bottom)へ、5秒で移動しようとする。
```

```sakurascript
\1\![moveasync,--X=-175,--Y=200,--time=5000,--base=screen,--base-offset=right.top,--move-offset=right.bottom]相方側が移動開始。\![moveasync,cancel]ここで移動キャンセル。移動中に、別のイベントが発生しその中でキャンセルのさくらスクリプトが実行された場合も、移動をキャンセルできる。ダブルクリックすると移動を中断する、という演出などに使える。
```
