# OnExecuteWebSocketReconnect

**カテゴリ:** Other communication events

Occurs when automatic reconnection succeeds after an error disconnect. OnExecuteWebSocketOpen does not fire; this event serves the equivalent role of Open. Data received after reconnection is reported as usual through OnExecuteWebSocketReceive.<br />
If the eventID specified with the --async option begins with "On", the event name is eventID+"Reconnect".

- **Reference0**: Event identifier specified with Sakura Script's --async option.
- **Reference1**: Connection URL.
- **Reference2**: "200" (fixed).

**対応:** SSP 2.8.05
