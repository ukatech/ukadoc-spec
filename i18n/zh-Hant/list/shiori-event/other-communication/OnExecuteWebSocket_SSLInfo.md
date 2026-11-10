# OnExecuteWebSocket_SSLInfo

**カテゴリ:** 其他通訊事件

使用 wss:// 連線時，SSL/TLS 連線建立後觸發。只會在初次連線時觸發，且不論 Upgrade 是否成功都會觸發。事件名稱固定，無法透過 --async 選項變更。

- **Reference0**: Sakura Script 的 --async 選項所指定的事件識別碼。
- **Reference1～**: [與 OnExecuteHTTPSSLInfo 的 Reference1 之後相同](OnExecuteHTTPSSLInfo.md)。

**対応:** SSP 2.8.05
