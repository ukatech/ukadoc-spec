# `\_b`\[檔案路徑,x,y,[選項](note-1.md#_bファイルパスについて),選項...\]

**カテゴリ:** バルーン、テキストコマンド

將圖片貼到 balloon 的 XY 座標。<br />
\[執行中 ghost 的資料夾\]/ghost/master 為基準資料夾。<br />
※可使用 base64 編碼或 exe/dll 資源作為圖片，而非檔名，[※請參閱下方](note-1.md#補足)。

可指定的選項請參閱[※下方](note-1.md#_bファイルパスについて)。

**対応:** SSP

## 記述例

```sakurascript
\_b[test.png,10,20,--option=use_self_alpha,--clipping=100 30 150 90,--option=foreground]本体側バルーンに、[実行したゴーストのフォルダ]/ghost/masterフォルダにあるtest.pngを、バルーン内座標X:10,Y:20に、ファイルの透過情報付きpngとして、画像の横100～150pixel縦30～90pixelの範囲を、バルーンの文字の上に表示する。
```
