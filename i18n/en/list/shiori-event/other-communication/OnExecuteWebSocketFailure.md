# OnExecuteWebSocketFailure

**カテゴリ:** Other communication events

Occurs when the initial connection fails to complete the HTTP 101 Upgrade, or when an error disconnects an active connection and all five automatic reconnection attempts fail.<br />
If the eventID specified with the --async option begins with "On", the event name is eventID+"Failure".

- **Reference0**: Event identifier specified with Sakura Script's --async option.
- **Reference1**: Connection URL.
- **Reference2**: Error message string. For an initial connection failure, this is the SPHttp error text; if all automatic reconnection attempts fail, it is "reconnect failed" (fixed).

**対応:** SSP 2.8.05
