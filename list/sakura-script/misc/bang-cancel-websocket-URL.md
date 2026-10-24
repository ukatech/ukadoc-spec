# `\![cancel,websocket,URL]`

**カテゴリ:** 未分類コマンド

Closeフレームを送らずに接続を強制中断する。自動再接続のバックオフ待機中でも即座に中断する。切断後に[OnExecuteWebSocketClose](../../shiori-event/other-communication/OnExecuteWebSocketClose.md) (Reference2="userbreak") が発生する。正常に会話を終わらせる場合は`\![close,websocket,...]`を使用すること。

- URL……接続時に使ったURLと同じ文字列。

**対応:** SSP 2.8.05
