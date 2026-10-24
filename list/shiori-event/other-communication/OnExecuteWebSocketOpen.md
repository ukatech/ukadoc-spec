# OnExecuteWebSocketOpen

**カテゴリ:** その他通信イベント

WebSocket接続確立時（HTTP 101 Upgrade成功後）に発生。初回接続のみ発火し、再接続成功時はOnExecuteWebSocketReconnectが発生する。<br />
--asyncオプションで指定したeventIDが "On" で始まる場合はeventID+"Open" がイベント名となる。

- **Reference0**: Sakura Scriptの--asyncオプションで指定されたイベント識別子。
- **Reference1**: 接続URL (ws:// または wss://)。
- **Reference2**: "200"（固定）。

**対応:** SSP 2.8.05
