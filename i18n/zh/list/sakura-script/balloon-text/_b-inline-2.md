# `\_b`\[file path,inline,[options](note-1.md#_bファイルパスについて),options...\]

**カテゴリ:** Balloon, text commands

Embeds an image within a line of balloon text, treating it as one character.<br />
The base folder is \[the folder of the running ghost\]/ghost/master.<br />
※Instead of a file name, an image can be specified using base64 encoding or an exe/dll resource; [see below](note-1.md#補足).

For the options that can be specified, [see below](note-1.md#_bファイルパスについて).

## 記述例

```sakurascript
本体側バルーンに、[実行したゴーストのフォルダ]/ghost/masterフォルダにあるtest.png\_b[test.png,inline,--option=use_self_alpha,--clipping=100 30 150 90]を、文字扱い、ファイルの透過情報付きpngとして、画像の横100～150pixel縦30～90pixelの範囲を表示する。
```

**対応:** SSP
