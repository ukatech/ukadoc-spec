# `\_b[ファイルパス,x,y,opaque]`

**カテゴリ:** 氣球、文字指令

將圖片貼至氣球的 XY 座標。圖片會顯示在文字下方。<br />
顯示時不會將左上角的顏色設為透明。<br />
\[執行中的 ghost 資料夾\]/ghost/master 為基準資料夾。<br />
※也可以不使用檔名，而改以 base64 編碼或 exe/dll 資源指定圖片，[※請參閱下方](note-1.md#補足)。

**対応:** SSP

## 記述例

```sakurascript
\_b[..\..\shell\master\surface0.png,0,15,opaque]本体側バルーンに、[実行したゴーストのフォルダ]/shell\masterフォルダにあるsurface0.pngを、バルーン内座標X:0,Y:15に、透過せずに表示する。
```
