# OnExecuteWebSocketClose

**カテゴリ:** 其他通信事件

WebSocket 连接最终断开时触发。尝试自动重新连接时，会在重新连接尝试后触发。Failure 时不触发。<br />
--async 选项指定的 eventID 以 "On" 开头时，事件名为 eventID+"Close"。

- **Reference0**: Sakura Script 的 --async 选项指定的事件标识符。
- **Reference1**: 连接 URL。
- **Reference2**: 断开原因代码。"1000"=正常断开（由服务器或 `\![close,websocket]` 引起），"userbreak"=`\![cancel,websocket]` 或因 ghost 结束而强制中断。

**対応:** SSP 2.8.05
