# `\![send,websocket-binary,URL,base64data]`

**カテゴリ:** 未分類命令

向已连接的 WebSocket 会话发送二进制帧。通过 URL 确定目标会话。如果会话不存在，则忽略此标签。

- URL……与连接时使用的 URL 相同的字符串。
- base64data……经过 Base64 编码的二进制数据。

**対応:** SSP 2.8.05

## 記述例

```sakurascript
\![send,websocket-binary,ws://example.com/stream,SGVsbG8=]ws://example.com/stream に Base64デコードしたバイナリデータをバイナリフレームとして送信する。
```
