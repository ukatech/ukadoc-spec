# `\_b[file path,inline,opaque]`

**カテゴリ:** Balloon, text commands

Embeds an image within a line of balloon text, treating it as one character.<br />
Displays the image without making the color at the top left transparent.<br />
The base folder is \[the folder of the running ghost\]/ghost/master.<br />
※Instead of a file name, an image can be specified using base64 encoding or an exe/dll resource; [see below](note-1.md#補足).

**対応:** SSP

## 記述例

```sakurascript
本体側バルーンに、\_b["data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAOCAIAAACpTQvdAAAAl0lEQVR42oVSCQ7AIAiDl6MvZyCMQ122JQSh5agiM0P/JmL4dGQxCIEjruSd6QRBE7D86nRCibMTTvScQPTazsEBfgaECUoQHAyfzXytLbMtTutQOdZhQ2uHc4dNlssOTrBWr40q2tNsXTq186myikUCsJYuU1bV81g2TJUs7bm8WC8fmKtKXC4O/1XaCVeVYmL6eIsRfwDNfLdu1l4zPAAAAABJRU5ErkJggg==",inline,opaque]文字と同じ扱いとして、base64エンコード(文字列化)した画像データを、透過せずに表示する。
```
