# `\![send,websocket,URL,data1,data2,...]`

**カテゴリ:** Unclassified command

Send a text frame to the connected WebSocket session. The URL identifies the target session. If two or more data values are specified, they are joined with CRLF and sent as text. If the session does not exist (before connection or after disconnection), the tag is ignored.

- URL……The same string as the URL used when connecting.
- data1,data2,……UTF-8 text to send. If two or more values are specified, they are joined with CRLF.

**対応:** SSP 2.8.05

## 記述例

```sakurascript
\![send,websocket,ws://example.com/chat,Hello!,World]ws://example.com/chat に "Hello!\r\nWorld" をテキストフレームとして送信する。
```
