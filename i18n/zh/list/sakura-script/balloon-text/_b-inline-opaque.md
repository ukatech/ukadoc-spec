# `\_b[文件路径,inline,opaque]`

**カテゴリ:** 气球、文本命令

将图像插入气球的文本行内，并按一个字符处理。<br />
显示时不对左上角的颜色进行透明处理。<br />
\[已执行的 ghost 的文件夹\]/ghost/master 是基准文件夹。<br />
※可以使用 base64 编码或 exe/dll 资源代替文件名来指定图像，[※参见下文](note-1.md#補足)。

**対応:** SSP

## 記述例

```sakurascript
本体側バルーンに、\_b["data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAOCAIAAACpTQvdAAAAl0lEQVR42oVSCQ7AIAiDl6MvZyCMQ122JQSh5agiM0P/JmL4dGQxCIEjruSd6QRBE7D86nRCibMTTvScQPTazsEBfgaECUoQHAyfzXytLbMtTutQOdZhQ2uHc4dNlssOTrBWr40q2tNsXTq186myikUCsJYuU1bV81g2TJUs7bm8WC8fmKtKXC4O/1XaCVeVYmL6eIsRfwDNfLdu1l4zPAAAAABJRU5ErkJggg==",inline,opaque]文字と同じ扱いとして、base64エンコード(文字列化)した画像データを、透過せずに表示する。
```
