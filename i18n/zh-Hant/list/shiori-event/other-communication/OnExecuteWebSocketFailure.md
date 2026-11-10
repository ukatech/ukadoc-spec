# OnExecuteWebSocketFailure

**カテゴリ:** Other communication events

Occurs if the initial connection fails to perform an HTTP 101 Upgrade, or if an error causes disconnection during a connection and all five automatic reconnection attempts fail.<br />
If the eventID specified with the --async option starts with "On", the event name is eventID+"Failure".

- **Reference0**: Event identifier specified with Sakura Script's --async option.
- **Reference1**: Connection URL.
- **Reference2**: Error message string. On initial connection failure, this is the SPHttp error text; if all automatic reconnection attempts fail, this is "reconnect failed" (fixed).

**対応:** SSP 2.8.05
