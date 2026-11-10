# `\_b`\[File path,inline,[options](note-1.md#_bファイルパスについて),options...\]

**カテゴリ:** Balloon, text command

Embeds an image within a line of balloon text, treating it as one character.<br />
\[The running ghost's folder\]/ghost/master is the base folder.<br />
※A base64-encoded string or a resource in an exe/dll can be specified as an image instead of a file name; [see below](note-1.md#補足).

For available options, [see below](note-1.md#_bファイルパスについて).

## 記述例

```sakurascript
本体側バルーンに、[実行したゴーストのフォルダ]/ghost/masterフォルダにあるtest.png\_b[test.png,inline,--option=use_self_alpha,--clipping=100 30 150 90]を、文字扱い、ファイルの透過情報付きpngとして、画像の横100～150pixel縦30～90pixelの範囲を表示する。
```

**対応:** SSP
