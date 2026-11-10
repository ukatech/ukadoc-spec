# OnExecuteWebSocket_SSLInfo

**カテゴリ:** Other communication events

Occurs when an SSL/TLS connection is established for a wss:// connection. Fires only during the initial connection, regardless of whether the Upgrade succeeds. The event name is always fixed and cannot be changed with the --async option.

- **Reference0**: Event identifier specified with Sakura Script's --async option.
- **Reference1～**: [Same as Reference1 onward of OnExecuteHTTPSSLInfo](OnExecuteHTTPSSLInfo.md).

**対応:** SSP 2.8.05
