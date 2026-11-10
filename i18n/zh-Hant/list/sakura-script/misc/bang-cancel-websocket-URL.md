# `\![cancel,websocket,URL]`

**カテゴリ:** 未分類指令

不傳送 Close frame，強制中斷連線。即使正在等待自動重新連線的退避時間，也會立即中斷。中斷後會觸發 [OnExecuteWebSocketClose](../../shiori-event/other-communication/OnExecuteWebSocketClose.md) (Reference2="userbreak")。若要正常結束連線，請使用 `\![close,websocket,...]`。

- URL……與連線時使用的 URL 相同的字串。

**対応:** SSP 2.8.05
