# OnExecuteWebSocketClose

**カテゴリ:** Other communication events

Occurs when the WebSocket connection is finally disconnected. If automatic reconnection is attempted, this event fires afterward. Does not fire on Failure.<br />
If the eventID specified with the --async option begins with "On", the event name is eventID+"Close".

- **Reference0**: Event identifier specified with Sakura Script's --async option.
- **Reference1**: Connection URL.
- **Reference2**: Disconnection cause code. "1000"=normal disconnection (by the server or `\![close,websocket]`), "userbreak"=forced interruption by `\![cancel,websocket]` or ghost termination.

**対応:** SSP 2.8.05
