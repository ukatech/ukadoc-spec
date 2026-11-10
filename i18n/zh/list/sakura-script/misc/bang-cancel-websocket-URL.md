# `\![cancel,websocket,URL]`

**カテゴリ:** 未分类命令

强制中断连接，不发送 Close 帧。即使正在等待自动重连的退避时间，也会立即中断。断开后会触发 [OnExecuteWebSocketClose](../../shiori-event/other-communication/OnExecuteWebSocketClose.md) (Reference2="userbreak")。若要正常结束会话，请使用 `\![close,websocket,...]`。

- URL……与连接时使用的 URL 字符串相同。

**対応:** SSP 2.8.05
