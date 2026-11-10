# OnExecuteRSS_SSLInfo

**カテゴリ:** Other communication events

This event is notified even if retrieval fails (the HTTP response is not 200), because the connection succeeded at the SSL/TLS level.

Even if an ID starting with On is specified with --async or --sync, the event name is not replaced; this event is always notified.

- **Reference0～**: [The same as for OnExecuteHTTPSSLInfo](OnExecuteHTTPSSLInfo.md)

**対応:** SSP
