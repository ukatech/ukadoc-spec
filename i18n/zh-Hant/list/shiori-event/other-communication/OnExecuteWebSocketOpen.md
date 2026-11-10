# OnExecuteWebSocketOpen

**カテゴリ:** 其他通訊事件

WebSocket 連線建立時（HTTP 101 Upgrade 成功後）觸發。只會在初次連線時觸發；重新連線成功時則會觸發 OnExecuteWebSocketReconnect。<br />
若以 --async 選項指定的 eventID 以 "On" 開頭，事件名稱會是 eventID+"Open"。

- **Reference0**: Sakura Script 的 --async 選項所指定的事件識別碼。
- **Reference1**: 連線 URL（ws:// 或 wss://）。
- **Reference2**: 固定為 "200"。

**対応:** SSP 2.8.05
