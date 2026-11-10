# OnExecuteWebSocketFailure

**カテゴリ:** 其他通信事件

首次连接时 HTTP 101 Upgrade 失败，或连接期间发生错误断开且自动重新连接尝试 5 次后仍全部失败时触发。<br />
--async 选项指定的 eventID 以 "On" 开头时，事件名为 eventID+"Failure"。

- **Reference0**: Sakura Script 的 --async 选项指定的事件标识符。
- **Reference1**: 连接 URL。
- **Reference2**: 错误内容字符串。首次连接失败时为 SPHttp 的错误文本，自动重新连接全部失败时为固定值 "reconnect failed"。

**対応:** SSP 2.8.05
