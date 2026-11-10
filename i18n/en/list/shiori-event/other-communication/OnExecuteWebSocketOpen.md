# OnExecuteWebSocketOpen

**カテゴリ:** Other communication events

Occurs when the WebSocket connection is established (after a successful HTTP 101 Upgrade). Fires only for the initial connection; on a successful reconnection, OnExecuteWebSocketReconnect fires instead.<br />
If the eventID specified with the --async option begins with "On", the event name is eventID+"Open".

- **Reference0**: Event identifier specified with Sakura Script's --async option.
- **Reference1**: Connection URL (ws:// or wss://).
- **Reference2**: "200" (fixed).

**対応:** SSP 2.8.05
