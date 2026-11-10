# `\_b`\[File path,x,y,[options](note-1.md#_bファイルパスについて),options...\]

**カテゴリ:** Balloon, text command

Embeds an image at the specified XY coordinates in the balloon.<br />
\[The running ghost's folder\]/ghost/master is the base folder.<br />
※A base64-encoded string or a resource in an exe/dll can be specified as an image instead of a file name; [see below](note-1.md#補足).

For available options, [see below](note-1.md#_bファイルパスについて).

**対応:** SSP

## 記述例

```sakurascript
\_b[test.png,10,20,--option=use_self_alpha,--clipping=100 30 150 90,--option=foreground]本体側バルーンに、[実行したゴーストのフォルダ]/ghost/masterフォルダにあるtest.pngを、バルーン内座標X:10,Y:20に、ファイルの透過情報付きpngとして、画像の横100～150pixel縦30～90pixelの範囲を、バルーンの文字の上に表示する。
```
