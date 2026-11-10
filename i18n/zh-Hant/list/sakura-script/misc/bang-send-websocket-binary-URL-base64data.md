# `\![send,websocket-binary,URL,base64data]`

**カテゴリ:** 未分類コマンド

以二進位框架傳送至已連線的WebSocket工作階段。以URL指定目標工作階段。若工作階段不存在，則會忽略此標籤。

- URL……與連線時使用的URL相同的字串。
- base64data……以Base64編碼的二進位資料。

**対応:** SSP 2.8.05

## 記述例

```sakurascript
\![send,websocket-binary,ws://example.com/stream,SGVsbG8=]ws://example.com/stream に Base64デコードしたバイナリデータをバイナリフレームとして送信する。
```
