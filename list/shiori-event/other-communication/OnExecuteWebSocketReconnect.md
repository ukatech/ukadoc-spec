# OnExecuteWebSocketReconnect

**カテゴリ:** その他通信イベント

エラー切断後の自動再接続が成功したときに発生。OnExecuteWebSocketOpenは発火せず、このイベントがOpenに相当する役割を担う。再接続後の受信は通常どおりOnExecuteWebSocketReceiveで通知される。<br />
--asyncオプションで指定したeventIDが "On" で始まる場合はeventID+"Reconnect" がイベント名となる。

- **Reference0**: Sakura Scriptの--asyncオプションで指定されたイベント識別子。
- **Reference1**: 接続URL。
- **Reference2**: "200"（固定）。

**対応:** SSP 2.8.05
