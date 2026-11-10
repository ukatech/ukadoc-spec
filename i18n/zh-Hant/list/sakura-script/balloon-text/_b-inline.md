# `\_b[ファイルパス,inline]`

**カテゴリ:** バルーン、テキストコマンド

將圖片貼入 balloon 文字行內，並視為一個字元。<br />
\[執行中 ghost 的資料夾\]/ghost/master 為基準資料夾。<br />
※可使用 base64 編碼或 exe/dll 資源作為圖片，而非檔名，[※請參閱下方](note-1.md#補足)。

**対応:** SSP / Ninix

## 記述例

```sakurascript
本体側バルーンに、[実行したゴーストのフォルダ]/ghost/masterフォルダにあるtest.png\_b[test.png,inline]を、現在のバルーン内の文字表示位置に、左上のドットを透過色として、表示する。
```
