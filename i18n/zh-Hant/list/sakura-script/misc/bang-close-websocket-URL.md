# `\![close,websocket,URL]`

**カテゴリ:** 未分類指令

遵循 RFC 6455 傳送 Close frame，正常中斷連線。等待伺服器回應 Close frame 後再關閉連線。中斷後會觸發 [OnExecuteWebSocketClose](../../shiori-event/other-communication/OnExecuteWebSocketClose.md) (Reference2="1000")。

- URL……與連線時使用的 URL 相同的字串。
- status_code……省略時為 1000（正常結束）。1001=going away、1008=policy violation 等 (RFC 6455 §7.4.1)。

**対応:** SSP 2.8.05

## 記述例

```sakurascript
\![close,websocket,ws://example.com/chat]ws://example.com/chat を正常に切断する。
```

```sakurascript
\![close,websocket,ws://example.com/chat,1001]ステータスコード1001 (going away) で切断する。
```
