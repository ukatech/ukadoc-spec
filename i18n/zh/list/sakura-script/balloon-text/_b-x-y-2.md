# `\_b`\[file path,x,y,[options](note-1.md#_bファイルパスについて),options...\]

**カテゴリ:** Balloon, text commands

Embeds an image at the XY coordinates of a balloon.<br />
The base folder is \[the folder of the running ghost\]/ghost/master.<br />
※Instead of a file name, an image can be specified using base64 encoding or an exe/dll resource; [see below](note-1.md#補足).

For the options that can be specified, [see below](note-1.md#_bファイルパスについて).

**対応:** SSP

## 記述例

```sakurascript
\_b[test.png,10,20,--option=use_self_alpha,--clipping=100 30 150 90,--option=foreground]本体側バルーンに、[実行したゴーストのフォルダ]/ghost/masterフォルダにあるtest.pngを、バルーン内座標X:10,Y:20に、ファイルの透過情報付きpngとして、画像の横100～150pixel縦30～90pixelの範囲を、バルーンの文字の上に表示する。
```
