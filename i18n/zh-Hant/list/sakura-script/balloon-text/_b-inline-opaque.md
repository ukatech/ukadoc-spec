# `\_b[ファイルパス,inline,opaque]`

**カテゴリ:** バルーン、テキストコマンド

將圖片貼入 balloon 文字行內，並視為一個字元。<br />
顯示時不將左上角的顏色設為透明。<br />
\[執行中 ghost 的資料夾\]/ghost/master 為基準資料夾。<br />
※可使用 base64 編碼或 exe/dll 資源作為圖片，而非檔名，[※請參閱下方](note-1.md#補足)。

**対応:** SSP

## 記述例

```sakurascript
本体側バルーンに、\_b["data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAOCAIAAACpTQvdAAAAl0lEQVR42oVSCQ7AIAiDl6MvZyCMQ122JQSh5agiM0P/JmL4dGQxCIEjruSd6QRBE7D86nRCibMTTvScQPTazsEBfgaECUoQHAyfzXytLbMtTutQOdZhQ2uHc4dNlssOTrBWr40q2tNsXTq186myikUCsJYuU1bV81g2TJUs7bm8WC8fmKtKXC4O/1XaCVeVYmL6eIsRfwDNfLdu1l4zPAAAAABJRU5ErkJggg==",inline,opaque]文字と同じ扱いとして、base64エンコード(文字列化)した画像データを、透過せずに表示する。
```
