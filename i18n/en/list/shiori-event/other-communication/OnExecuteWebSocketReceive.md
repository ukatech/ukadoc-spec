# OnExecuteWebSocketReceive

**カテゴリ:** Other communication events

Occurs each time a data frame is received from the server while the WebSocket connection is active. Fragmented frames are automatically reassembled before the event fires. Does not fire for Ping/Pong/Close frames.<br />
If the eventID specified with the --async option begins with "On", the event name is the eventID itself.

- **Reference0**: Event identifier specified with Sakura Script's --async option.
- **Reference1**: Connection URL.
- **Reference2**: Opcode type. "1"=text frame (UTF-8), "2"=binary frame.
- **Reference3**: Received data. For a text frame, the UTF-8 string as-is (line breaks are converted to byte value 1); for a binary frame, a Base64-encoded string.

**対応:** SSP 2.8.05
