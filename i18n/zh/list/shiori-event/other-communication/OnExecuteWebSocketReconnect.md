# OnExecuteWebSocketReconnect

**カテゴリ:** 其他通信事件

错误断开后自动重新连接成功时触发。不会触发 OnExecuteWebSocketOpen，此事件承担相当于 Open 的作用。重新连接后的接收数据仍会按通常方式通过 OnExecuteWebSocketReceive 通知。<br />
--async 选项指定的 eventID 以 "On" 开头时，事件名为 eventID+"Reconnect"。

- **Reference0**: Sakura Script 的 --async 选项指定的事件标识符。
- **Reference1**: 连接 URL。
- **Reference2**: 固定值 "200"。

**対応:** SSP 2.8.05
