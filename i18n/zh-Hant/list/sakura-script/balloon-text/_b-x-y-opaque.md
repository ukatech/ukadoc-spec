# `\_b[ファイルパス,x,y,opaque]`

**カテゴリ:** balloon, text command

Paste an image at the balloon's XY coordinates. The image is displayed behind the text.<br />
Display without making the color in the upper-left corner transparent.<br />
\[folder of the running ghost\]/ghost/master is the base folder.<br />
※Instead of a file name, you can specify a base64-encoded image or an image resource from an exe/dll. [※See below](note-1.md#補足).

**対応:** SSP

## 記述例

```sakurascript
\_b[..\..\shell\master\surface0.png,0,15,opaque]本体側バルーンに、[実行したゴーストのフォルダ]/shell\masterフォルダにあるsurface0.pngを、バルーン内座標X:0,Y:15に、透過せずに表示する。
```
