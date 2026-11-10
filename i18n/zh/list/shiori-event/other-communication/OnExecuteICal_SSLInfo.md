# OnExecuteICal_SSLInfo

**カテゴリ:** 其他通信事件

即使获取失败（HTTP响应不是200），由于SSL/TLS层面的连接已成功，仍会发送通知。

即使通过--async・--sync指定了以On开头的ID，事件名也不会被替换，始终通过本事件发送通知。

- **Reference0～**: [与OnExecuteHTTPSSLInfo相同](OnExecuteHTTPSSLInfo.md)

**対応:** SSP 2.8.90
