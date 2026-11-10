# `\_b[ファイルパス,x,y]`

**カテゴリ:** 气球、文本命令

将图像粘贴到气球的XY坐标处。图像显示在文字下方。<br />
左上像素的颜色将作为透明色。<br />
\[执行该命令的ghost的文件夹\]/ghost/master为基准文件夹。<br />
※仅SSP可以用base64编码或exe/dll资源代替文件名来指定图像，[※参见下文](note-1.md#補足)。<br />
※仅SSP可以指定图像URL。<br />
※仅SSP会搜索插件文件夹内的文件。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\_b[image\test.png,50,100]本体側バルーンに、[実行したゴーストのフォルダ]/ghost/master/imageフォルダにあるtest.pngを左上のpixelを透過色として、バルーン内座標X:50,Y:100に表示する。
```
