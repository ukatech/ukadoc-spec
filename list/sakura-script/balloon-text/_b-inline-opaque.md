# `\_b[ファイルパス,inline,opaque]`

**カテゴリ:** バルーン、テキストコマンド

バルーンのテキスト行内に1文字分扱いとして画像を貼り付ける。<br />
左上の色を透過しないで表示する。<br />
\[実行したゴーストのフォルダ\]/ghost/masterが基準のフォルダとなる。<br />
※ファイル名の代わりにbase64エンコードやexe/dllのリソースを画像として指定可能、[※下記参照](note-1.md#補足)。

**対応:** SSP

## 記述例

```sakurascript
本体側バルーンに、\_b["data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAOCAIAAACpTQvdAAAAl0lEQVR42oVSCQ7AIAiDl6MvZyCMQ122JQSh5agiM0P/JmL4dGQxCIEjruSd6QRBE7D86nRCibMTTvScQPTazsEBfgaECUoQHAyfzXytLbMtTutQOdZhQ2uHc4dNlssOTrBWr40q2tNsXTq186myikUCsJYuU1bV81g2TJUs7bm8WC8fmKtKXC4O/1XaCVeVYmL6eIsRfwDNfLdu1l4zPAAAAABJRU5ErkJggg==",inline,opaque]文字と同じ扱いとして、base64エンコード(文字列化)した画像データを、透過せずに表示する。
```
