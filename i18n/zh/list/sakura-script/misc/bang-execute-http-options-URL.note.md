# http/rss/ical/websocket options

- **--accept=Accept request header contents \[2.7.34\]**: Specify the Accept header, which specifies the Content-Type formats that can be received.
- **--accept-language=Accept-Language request header contents \[2.7.34\]**: Specify the Accept-Language header, which controls internationalization-related behavior.
- **--async=identifier**: Continue executing Sakura Script without waiting for processing to finish, and notify an event after processing is complete.<br />
  For HTTP, this is [OnExecuteHTTPComplete](../../shiori-event/other-communication/OnExecuteHTTPComplete.md) or [OnExecuteHTTPFailure](../../shiori-event/other-communication/OnExecuteHTTPFailure.md).<br />
  For RSS, this is [OnExecuteRSSComplete](../../shiori-event/other-communication/OnExecuteRSSComplete.md) or [OnExecuteRSSFailure](../../shiori-event/other-communication/OnExecuteRSSFailure.md).<br />
  For iCal, this is [OnExecuteICalComplete](../../shiori-event/other-communication/OnExecuteICalComplete.md) or [OnExecuteICalFailure](../../shiori-event/other-communication/OnExecuteICalFailure.md). \[2.8.90\]<br />
  For WebSocket, [OnExecuteWebSocketOpen](../../shiori-event/other-communication/OnExecuteWebSocketOpen.md)/[Receive](../../shiori-event/other-communication/OnExecuteWebSocketReceive.md)/[Reconnect](../../shiori-event/other-communication/OnExecuteWebSocketReconnect.md)/[Close](../../shiori-event/other-communication/OnExecuteWebSocketClose.md)/[Failure](../../shiori-event/other-communication/OnExecuteWebSocketFailure.md) occur at the respective times of connection, receiving, and disconnection (because operation is always asynchronous, --sync cannot be used).<br />
  If an ID that does not start with On is specified, events with the names listed above occur.<br />
  If an ID that starts with On is specified, HTTP/RSS/iCal trigger \[specified ID\] (success)/\[specified ID\]Failure (failure). WebSocket triggers \[specified ID\]Open/\[specified ID\] (receive)/\[specified ID\]Reconnect/\[specified ID\]Close/\[specified ID\]Failure.<br />
  Example: with --async=OnExample, HTTP/RSS/iCal → OnExample/OnExampleFailure; WebSocket → OnExampleOpen/OnExample/OnExampleReconnect/OnExampleClose/OnExampleFailure<br />
  However, SSLInfo events ([OnExecuteHTTPSSLInfo](../../shiori-event/other-communication/OnExecuteHTTPSSLInfo.md)/[OnExecuteRSS_SSLInfo](../../shiori-event/other-communication/OnExecuteRSS_SSLInfo.md)/[OnExecuteICal_SSLInfo](../../shiori-event/other-communication/OnExecuteICal_SSLInfo.md)/[OnExecuteWebSocket_SSLInfo](../../shiori-event/other-communication/OnExecuteWebSocket_SSLInfo.md)) are excluded, and are always reported using the event names listed above even if an ID starting with On is specified.<br />
  To temporarily pause Sakura Script processing, write --sync instead (not applicable to WebSocket).
- **--authorization=Authorization request header contents \[2.6.37\]**: Set this in advance when an Authorization header is required, such as for OAuth.
- **--cookie=cookie data**: Cookie data; if needed, specify the value of Reference5 from OnExecuteHTTPComplete as-is.
- **--content-type=(multipart/form-data | application/x-www-form-urlencoded | any other value)**: Only for http-post. Specify the format used to send parameters specified with param.<br />
  If nothing is specified, application/x-www-form-urlencoded is used.<br />
  Note that some formats constrain how param can be written.<br />
  Since \[2.6.37\], this information is applied directly to the Content-Type request header.
- **--expand or --expand=number of days \[2.8.90\]**: Only for ical-get/ical-post. See [※iCal filtering options](bang-execute-ical-post-URL.note.md).<br />
  Expand RRULE recurrences and return one item per occurrence. If a number of days is specified, it becomes the period length used when --to is omitted (default: 30 days).
- **--file=filename**: Specify the name to use when saving the retrieved data. It is saved to \[the folder of the executing ghost\]/ghost/master/var/filename.
- **--from=yyyymmdd \[2.8.90\]**: Only for ical-get/ical-post and rss-get/rss-post \[2.8.92\]. See [※iCal filtering options](bang-execute-ical-post-URL.note.md) and [※RSS filtering options](bang-execute-rss-post-URL.note.md).<br />
  The start date of the period for returned events. Defaults to today if omitted.<br />
  \[2.8.92\] For rss-get/rss-post, this is the lower bound for the update date of returned items (from 0:00 on that day). There is no lower bound if omitted.
- **--header=SomeHeader: request header contents \[2.6.40\]**: Set a request header with an arbitrary name. The colon separating the name and contents is required.<br />
  This overrides header information set by SSP, so take care not to specify conflicting values.
- **--insecure \[2.7.34\]**: Skip TLS certificate verification.
- **--limit=count \[2.8.90\]**: Only for ical-get/ical-post and rss-get/rss-post \[2.8.92\]. See [※iCal filtering options](bang-execute-ical-post-URL.note.md) and [※RSS filtering options](bang-execute-rss-post-URL.note.md).<br />
  The maximum number of events to return. Defaults to 200; specify 0 for unlimited.<br />
  Writing only --limit enables period mode with today as the start date. If none of --from, --to, --expand, or --limit is specified, there is no limit on the number of items returned (all items are returned).<br />
  \[2.8.92\] For rss-get/rss-post, if specified, the results are truncated to the specified count in descending order of recency. If omitted or set to 0, there is no limit, and writing only --limit does not filter by period.
- **--log=filename**: Log all communication with the server. Mainly for debugging during development.
- **--nodescript**: Do not display the online display or download status.
- **--nofile=parameter (character encoding) \[2.5.77\]**: Retrieve and expand data in memory without creating a temporary file, then store it in the event's Reference3.<br />
  Specify the character encoding to use when interpreting the retrieved data. If omitted, UTF-8 is assumed.<br />
  Because Reference cannot contain line breaks, line break characters are converted to byte value 1.<br />
  The maximum retrievable size is 128KB.<br />
  \[2.8.90\] For rss-get/rss-post and ical-get/ical-post, this option is ignored because a file is required for parsing.
- **--no-cache \[2.7.34\]**: Specify Cache-Control: no-cache to suppress the use of cached data.
- **--param=parameter**: Specify parameters for get/post/put. This can be specified multiple times.<br />
  For multipart/form-data:<br />
  　Repeat the format --param=field name=data as many times as needed.<br />
  　Example: --param=message_body=data<br />
  For application/x-www-form-urlencoded:<br />
  　When the format --param=field name=data is repeated as many times as needed, all values are joined with & and sent to the server.<br />
  　Otherwise, all values are joined with newline characters (CRLF) and sent to the server (for backward compatibility).<br />
  For other content-type values:<br />
  　If defined multiple times, all values are joined with newline characters (CRLF) and sent to the server.
- **--param-charset=character encoding**: Specify the character encoding, such as Shift_JIS, EUC-JP, or UTF-8. Defaults to UTF-8.
- **--param-input-file=filename \[2.6.40\]**: To send large data that cannot be specified entirely with the --param option, specify the file containing the data to send.<br />
  If the specified path is not absolute, it is interpreted relative to \[the folder of the executing ghost\]/ghost/master/.<br />
  Do not specify --param at the same time.<br />
  The contents are generally not inspected, so the caller is responsible for handling character encoding, encoding, and other processing.<br />
  However, for multipart/form-data only, the first line is read and interpreted as the separator between fields.<br />
  The specified file path must be under SSP's control (at or below the location of SSP.exe, or below a folder specified for listing ghosts, etc.).
- **--progress-notify \[2.6.44\]**: During download processing, notify the [OnExecuteHTTPProgress](../../shiori-event/other-communication/OnExecuteHTTPProgress.md) event (for ical-get/ical-post, [OnExecuteICalProgress](../../shiori-event/other-communication/OnExecuteICalProgress.md) \[2.8.90\]), or, if the event ID starts with On, an event with Progress appended to it.<br />
  If an ID starting with On is specified, SHIORI Event \[specified ID\]Progress occurs instead of the above event.<br />
  Example: with --async=OnExample, OnExampleProgress<br />
  Events are notified one by one during download processing, which reduces the download speed.<br />
  Also note that when outputting to a file, the file is temporarily closed when an event is notified and then reopened after the response is received, which further slows the download.
- **--streaming or --streaming=type \[2.8.14\]**: Specify streaming processing for HTTP requests. Use --streaming=sse for Server-Sent Events and --streaming=text for newline-delimited streaming (such as NDJSON).<br />
  If --streaming is specified without a type, streaming is handled appropriately based on the Content-Type of the server response.<br />
  Received data is reported through the [OnExecuteHTTPStreaming](../../shiori-event/other-communication/OnExecuteHTTPStreaming.md) event or, if the event ID starts with On, an event with Streaming appended to it, such as OnHogehogeStreaming.
- **--sync=identifier \[2.6.44\]**: Behaves the same as --async, except that Sakura Script execution is paused while waiting for processing to finish.
- **--timeout=seconds**: Specify how long to wait for a response (not the time required for downloading). The maximum is 300 seconds.<br />
  If no response is received within the specified time, the SHIORI event "OnExecuteHTTPFailure" is notified, and Reference4 contains "timeout".
- **--to=yyyymmdd \[2.8.90\]**: Only for ical-get/ical-post and rss-get/rss-post \[2.8.92\]. See [※iCal filtering options](bang-execute-ical-post-URL.note.md) and [※RSS filtering options](bang-execute-rss-post-URL.note.md).<br />
  The end date of the period for returned events (inclusive).<br />
  \[2.8.92\] For rss-get/rss-post, this is the upper bound for the update date of returned items (through the end of that day). There is no upper bound if omitted.
- **--m_websocketProtocol=Sec-Websocket-Protocol \[2.8.08\]**: Specify the Sec-Websocket-Protocol header to use when connecting to WebSocket. If not specified, this header is not sent.
