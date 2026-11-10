# `\![send,websocket,URL,data1,data2,...]`

**カテゴリ:** 未分類コマンド

以文字框架傳送至已連線的WebSocket工作階段。以URL指定目標工作階段。指定兩個以上的data時，會以CRLF連接後傳送文字。若工作階段不存在（尚未連線或已中斷），則會忽略此標籤。

- URL……與連線時使用的URL相同的字串。
- data1,data2,……要傳送的UTF-8文字。指定兩個以上時，會以CRLF連接。

**対応:** SSP 2.8.05

## 記述例

```sakurascript
\![send,websocket,ws://example.com/chat,Hello!,World]ws://example.com/chat に "Hello!\r\nWorld" をテキストフレームとして送信する。
```
