# `\_b`\[文件路径,x,y,[选项](note-1.md#_bファイルパスについて),选项...\]

**カテゴリ:** 气球、文本命令

将图像插入气球的 XY 坐标处。<br />
\[已执行的 ghost 的文件夹\]/ghost/master 是基准文件夹。<br />
※可以使用 base64 编码或 exe/dll 资源代替文件名来指定图像，[※参见下文](note-1.md#補足)。

可指定的选项请参见[※下文](note-1.md#_bファイルパスについて)。

**対応:** SSP

## 記述例

```sakurascript
\_b[test.png,10,20,--option=use_self_alpha,--clipping=100 30 150 90,--option=foreground]本体側バルーンに、[実行したゴーストのフォルダ]/ghost/masterフォルダにあるtest.pngを、バルーン内座標X:10,Y:20に、ファイルの透過情報付きpngとして、画像の横100～150pixel縦30～90pixelの範囲を、バルーンの文字の上に表示する。
```
