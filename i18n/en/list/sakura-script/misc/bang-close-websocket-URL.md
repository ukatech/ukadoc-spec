# `\![close,websocket,URL]`

**カテゴリ:** Miscellaneous commands

Send a Close frame and disconnect normally, in accordance with RFC 6455. The connection is closed after receiving the server's response Close frame. After disconnection, [OnExecuteWebSocketClose](../../shiori-event/other-communication/OnExecuteWebSocketClose.md) (Reference2="1000") is raised.

- URL……The same string as the URL used when connecting.
- status_code……If omitted, defaults to 1000 (normal closure). 1001=going away, 1008=policy violation, etc. (RFC 6455 §7.4.1).

**対応:** SSP 2.8.05

## 記述例

```sakurascript
\![close,websocket,ws://example.com/chat]ws://example.com/chat を正常に切断する。
```

```sakurascript
\![close,websocket,ws://example.com/chat,1001]ステータスコード1001 (going away) で切断する。
```
