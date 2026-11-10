# `\_b[ファイルパス,x,y,opaque]`

**カテゴリ:** Balloon, text command

Paste an image at the balloon's XY coordinates. The image is displayed underneath the text.<br />
Display the image without making the color of the top-left pixel transparent.<br />
The base folder is \[folder of the ghost that executed this\]/ghost/master.<br />
※Base64-encoded data or an exe/dll resource can be specified as the image instead of a filename; [see below](note-1.md#補足).

**対応:** SSP

## 記述例

```sakurascript
\_b[..\..\shell\master\surface0.png,0,15,opaque]本体側バルーンに、[実行したゴーストのフォルダ]/shell\masterフォルダにあるsurface0.pngを、バルーン内座標X:0,Y:15に、透過せずに表示する。
```
