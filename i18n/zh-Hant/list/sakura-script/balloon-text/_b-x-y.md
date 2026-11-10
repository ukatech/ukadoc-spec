# `\_b[ファイルパス,x,y]`

**カテゴリ:** 氣球、文字指令

將圖片貼至氣球的 XY 座標。圖片會顯示在文字下方。<br />
左上角像素的顏色會設為透明色。<br />
\[執行中的 ghost 資料夾\]/ghost/master 為基準資料夾。<br />
※僅 SSP 可不使用檔名，而改以 base64 編碼或 exe/dll 資源指定圖片，[※請參閱下方](note-1.md#補足)。<br />
※僅 SSP 可指定圖片 URL。<br />
※僅 SSP 會搜尋 plugin 資料夾內的檔案。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\_b[image\test.png,50,100]本体側バルーンに、[実行したゴーストのフォルダ]/ghost/master/imageフォルダにあるtest.pngを左上のpixelを透過色として、バルーン内座標X:50,Y:100に表示する。
```
