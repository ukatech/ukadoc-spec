# `\![close,websocket,URL]`

**カテゴリ:** 未分类命令

按照 RFC 6455 发送 Close 帧并正常断开连接。等待服务器响应 Close 帧后再关闭连接。断开后会触发 [OnExecuteWebSocketClose](../../shiori-event/other-communication/OnExecuteWebSocketClose.md) (Reference2="1000")。

- URL……与连接时使用的 URL 字符串相同。
- status_code……省略时为 1000（正常结束）。例如，1001=going away、1008=policy violation（RFC 6455 §7.4.1）。

**対応:** SSP 2.8.05

## 記述例

```sakurascript
\![close,websocket,ws://example.com/chat]ws://example.com/chat を正常に切断する。
```

```sakurascript
\![close,websocket,ws://example.com/chat,1001]ステータスコード1001 (going away) で切断する。
```
