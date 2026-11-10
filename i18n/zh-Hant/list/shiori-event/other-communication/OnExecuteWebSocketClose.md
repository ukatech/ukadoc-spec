# OnExecuteWebSocketClose

**カテゴリ:** 其他通訊事件

WebSocket 連線最終中斷時觸發。若曾嘗試自動重新連線，則會在重新連線後觸發。Failure 時不會觸發。<br />
若以 --async 選項指定的 eventID 以 "On" 開頭，事件名稱會是 eventID+"Close"。

- **Reference0**: Sakura Script 的 --async 選項所指定的事件識別碼。
- **Reference1**: 連線 URL。
- **Reference2**: 中斷原因代碼。"1000"=正常中斷（由伺服器或 `\![close,websocket]` 引起）、"userbreak"=`\![cancel,websocket]` 或因 ghost 結束而強制中斷。

**対応:** SSP 2.8.05
