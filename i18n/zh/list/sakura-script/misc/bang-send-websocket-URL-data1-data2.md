# `\![send,websocket,URL,data1,data2,...]`

**カテゴリ:** 未分類命令

向已连接的 WebSocket 会话发送文本帧。通过 URL 确定目标会话。指定两个或更多 data 时，会将它们用 CRLF 连接后发送。如果会话不存在（连接前或断开后），则忽略此标签。

- URL……与连接时使用的 URL 相同的字符串。
- data1,data2,……要发送的 UTF-8 文本。指定两个或更多时，会用 CRLF 连接。

**対応:** SSP 2.8.05

## 記述例

```sakurascript
\![send,websocket,ws://example.com/chat,Hello!,World]ws://example.com/chat に "Hello!\r\nWorld" をテキストフレームとして送信する。
```
