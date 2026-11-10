# OnExecuteWebSocketReconnect

**カテゴリ:** 其他通訊事件

錯誤中斷後自動重新連線成功時觸發。OnExecuteWebSocketOpen 不會觸發，此事件則負責執行相當於 Open 的功能。重新連線後收到資料時，會照常透過 OnExecuteWebSocketReceive 通知。<br />
若以 --async 選項指定的 eventID 以 "On" 開頭，事件名稱會是 eventID+"Reconnect"。

- **Reference0**: Sakura Script 的 --async 選項所指定的事件識別碼。
- **Reference1**: 連線 URL。
- **Reference2**: 固定為 "200"。

**対応:** SSP 2.8.05
