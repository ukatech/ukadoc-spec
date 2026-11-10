# `\![cancel,websocket,URL]`

**カテゴリ:** Miscellaneous commands

Forcefully interrupt the connection without sending a Close frame. This interrupts immediately, even during an automatic-reconnection backoff wait. After disconnection, [OnExecuteWebSocketClose](../../shiori-event/other-communication/OnExecuteWebSocketClose.md) (Reference2="userbreak") is raised. Use `\![close,websocket,...]` to end the conversation normally.

- URL……The same string as the URL used when connecting.

**対応:** SSP 2.8.05
