# OnExecuteWebSocketOpen

**カテゴリ:** 其他通信事件

WebSocket 连接建立时（HTTP 101 Upgrade 成功后）触发。仅在首次连接时触发，重新连接成功时会触发 OnExecuteWebSocketReconnect。<br />
--async 选项指定的 eventID 以 "On" 开头时，事件名为 eventID+"Open"。

- **Reference0**: Sakura Script 的 --async 选项指定的事件标识符。
- **Reference1**: 连接 URL (ws:// 或 wss://)。
- **Reference2**: 固定值 "200"。

**対応:** SSP 2.8.05
