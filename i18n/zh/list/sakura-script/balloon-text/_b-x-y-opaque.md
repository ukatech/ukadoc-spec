# `\_b[ファイルパス,x,y,opaque]`

**カテゴリ:** 气球、文本命令

将图像粘贴到气球的XY坐标处。图像显示在文字下方。<br />
显示时不将左上角的颜色设为透明。<br />
\[执行该命令的ghost的文件夹\]/ghost/master为基准文件夹。<br />
※可以用base64编码或exe/dll资源代替文件名来指定图像，[※参见下文](note-1.md#補足)。

**対応:** SSP

## 記述例

```sakurascript
\_b[..\..\shell\master\surface0.png,0,15,opaque]本体側バルーンに、[実行したゴーストのフォルダ]/shell\masterフォルダにあるsurface0.pngを、バルーン内座標X:0,Y:15に、透過せずに表示する。
```
