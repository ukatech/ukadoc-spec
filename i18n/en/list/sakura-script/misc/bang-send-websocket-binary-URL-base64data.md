# `\![send,websocket-binary,URL,base64data]`

**カテゴリ:** Unclassified command

Send a binary frame to the connected WebSocket session. The URL identifies the target session. If the session does not exist, the tag is ignored.

- URL……The same string as the URL used when connecting.
- base64data……Binary data encoded in Base64.

**対応:** SSP 2.8.05

## 記述例

```sakurascript
\![send,websocket-binary,ws://example.com/stream,SGVsbG8=]ws://example.com/stream に Base64デコードしたバイナリデータをバイナリフレームとして送信する。
```
