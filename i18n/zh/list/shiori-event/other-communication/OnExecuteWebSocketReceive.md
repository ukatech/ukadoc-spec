# OnExecuteWebSocketReceive

**カテゴリ:** 其他通信事件

WebSocket 连接期间，每当从服务器收到数据帧时触发。分片帧会在重新组装后触发。Ping/Pong/Close 帧不会触发。<br />
--async 选项指定的 eventID 以 "On" 开头时，事件名与 eventID 相同。

- **Reference0**: Sakura Script 的 --async 选项指定的事件标识符。
- **Reference1**: 连接 URL。
- **Reference2**: opcode 类型。"1"=文本帧 (UTF-8)、"2"=二进制帧。
- **Reference3**: 接收的数据。文本帧为原样的 UTF-8 字符串（换行符转换为字节值 1），二进制帧为 Base64 编码字符串。

**対応:** SSP 2.8.05
