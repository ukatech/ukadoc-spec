# `\![close,websocket,URL]`

**カテゴリ:** 未分類コマンド

RFC 6455に従いCloseフレームを送信して正常に切断する。サーバー側のCloseフレーム応答を待ってから接続を閉じる。切断後に[OnExecuteWebSocketClose](../../shiori-event/other-communication/OnExecuteWebSocketClose.md) (Reference2="1000") が発生する。

- URL……接続時に使ったURLと同じ文字列。
- status_code……省略時は1000（正常終了）。1001=going away、1008=policy violation等 (RFC 6455 §7.4.1)。

**対応:** SSP 2.8.05

## 記述例

```sakurascript
\![close,websocket,ws://example.com/chat]ws://example.com/chat を正常に切断する。
```

```sakurascript
\![close,websocket,ws://example.com/chat,1001]ステータスコード1001 (going away) で切断する。
```
