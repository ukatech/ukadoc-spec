# http/rss/ical/websocket options

- **--accept=Accept request header contents \[2.7.34\]**: Specify the Accept header, which indicates the Content-Type formats that can be received.
- **--accept-language=Accept-Language request header contents \[2.7.34\]**: Specify the Accept-Language header, which controls internationalization-related behavior.
- **--async=ID**: Continue executing Sakura Script without waiting for the process to finish, and notify an event when it completes.<br />
  For HTTP, the event is [OnExecuteHTTPComplete](../../shiori-event/other-communication/OnExecuteHTTPComplete.md) or [OnExecuteHTTPFailure](../../shiori-event/other-communication/OnExecuteHTTPFailure.md).<br />
  For RSS, the event is [OnExecuteRSSComplete](../../shiori-event/other-communication/OnExecuteRSSComplete.md) or [OnExecuteRSSFailure](../../shiori-event/other-communication/OnExecuteRSSFailure.md).<br />
  For iCal, the event is [OnExecuteICalComplete](../../shiori-event/other-communication/OnExecuteICalComplete.md) or [OnExecuteICalFailure](../../shiori-event/other-communication/OnExecuteICalFailure.md). \[2.8.90\]<br />
  For WebSocket, [OnExecuteWebSocketOpen](../../shiori-event/other-communication/OnExecuteWebSocketOpen.md)/[Receive](../../shiori-event/other-communication/OnExecuteWebSocketReceive.md)/[Reconnect](../../shiori-event/other-communication/OnExecuteWebSocketReconnect.md)/[Close](../../shiori-event/other-communication/OnExecuteWebSocketClose.md)/[Failure](../../shiori-event/other-communication/OnExecuteWebSocketFailure.md) events occur at connection, receive, and disconnection, respectively (because it always operates asynchronously, --sync cannot be used).<br />
  If the ID does not begin with On, events with the names listed above occur.<br />
  If the ID begins with On, HTTP/RSS/iCal trigger \[the specified ID\] (success)/\[the specified ID\]Failure (failure). WebSocket triggers \[the specified ID\]Open/\[the specified ID\] (receive)/\[the specified ID\]Reconnect/\[the specified ID\]Close/\[the specified ID\]Failure.<br />
  Example: with --async=OnExample, HTTP/RSS/iCal → OnExample/OnExampleFailure, WebSocket → OnExampleOpen/OnExample/OnExampleReconnect/OnExampleClose/OnExampleFailure<br />
  However, SSLInfo-related events ([OnExecuteHTTPSSLInfo](../../shiori-event/other-communication/OnExecuteHTTPSSLInfo.md)/[OnExecuteRSS_SSLInfo](../../shiori-event/other-communication/OnExecuteRSS_SSLInfo.md)/[OnExecuteICal_SSLInfo](../../shiori-event/other-communication/OnExecuteICal_SSLInfo.md)/[OnExecuteWebSocket_SSLInfo](../../shiori-event/other-communication/OnExecuteWebSocket_SSLInfo.md)) are not affected; even if an ID beginning with On is specified, notifications always use the event names listed above.<br />
  To temporarily pause Sakura Script execution, write --sync instead (not applicable to WebSocket).
- **--authorization=Authorization request header contents \[2.6.37\]**: Set this in advance when an Authorization header is required, such as for OAuth.
- **--cookie=cookie data**: Cookie data. If needed, specify the value of Reference5 from OnExecuteHTTPComplete as-is.
- **--content-type=(multipart/form-data | application/x-www-form-urlencoded | any other value)**: Only for http-post. Specify the format used to send parameters specified with param.<br />
  If nothing is specified, application/x-www-form-urlencoded is used.<br />
  Note that the format specified may impose restrictions on how param is written.<br />
  Starting with \[2.6.37\], this information is also applied directly to the Content-Type request header.
- **--expand or --expand=number of days \[2.8.90\]**: Only for ical-get/ical-post. See [※iCal filtering options](bang-execute-ical-post-URL.note.md).<br />
  Expand RRULE recurrences and return one item for each occurrence. If a number of days is specified, it is the period length used when --to is omitted (default: 30 days).
- **--file=filename**: Specify the name to use when saving the retrieved data. It is saved to \[the folder of the executing ghost\]/ghost/master/var/filename.
- **--from=yyyymmdd \[2.8.90\]**: Only for ical-get/ical-post and rss-get/rss-post \[2.8.92\]. See [※iCal filtering options](bang-execute-ical-post-URL.note.md) and [※RSS filtering options](bang-execute-rss-post-URL.note.md).<br />
  The start date of the period for events to return. Defaults to today if omitted.<br />
  \[2.8.92\] For rss-get/rss-post, this is the lower bound for the update dates of returned items (from 00:00 on that day). No lower bound applies if omitted.
- **--header=SomeHeader: request header contents \[2.6.40\]**: Set a request header with an arbitrary name. The colon separating the name and contents is required.<br />
  This overrides header information set by SSP, so ensure that the specified values do not conflict.
- **--insecure \[2.7.34\]**: Skip TLS certificate verification.
- **--limit=number of items \[2.8.90\]**: Only for ical-get/ical-post and rss-get/rss-post \[2.8.92\]. See [※iCal filtering options](bang-execute-ical-post-URL.note.md) and [※RSS filtering options](bang-execute-rss-post-URL.note.md).<br />
  The maximum number of events to return. Defaults to 200; specify 0 for no limit.<br />
  If only --limit is specified, period mode is used with today as the start date. If none of --from, --to, --expand, or --limit is specified, there is no item limit (all items are returned).<br />
  \[2.8.92\] For rss-get/rss-post, specifying this option truncates the results to the specified number, in newest-first order. If omitted or set to 0, there is no limit; specifying only --limit does not restrict the period.
- **--log=filename**: Log all communication with the server. Mainly for debugging during development.
- **--nodescript**: Do not display the online view or download status.
- **--nofile=parameter (character encoding) \[2.5.77\]**: Retrieve and expand data in memory without creating a temporary file, and store it in the event's Reference3.<br />
  The parameter specifies the character encoding to use when interpreting the retrieved data. If omitted, UTF-8 is assumed.<br />
  Since Reference cannot contain line breaks, line breaks are converted to byte value 1.<br />
  The maximum retrievable size is 128KB.<br />
  \[2.8.90\] For rss-get/rss-post and ical-get/ical-post, this option is ignored because a file is required for parsing.
- **--no-cache \[2.7.34\]**: Specify Cache-Control: no-cache to suppress the use of cached data.
- **--param=parameter**: Specify parameters for get/post/put. This option can be specified multiple times.<br />
  For multipart/form-data:<br />
  　Repeat the form --param=field name=data as many times as needed.<br />
  　Example: --param=message_body=data<br />
  For application/x-www-form-urlencoded:<br />
  　If repeated in the form --param=field name=data, all values are joined with & and sent to the server.<br />
  　Otherwise, all values are joined with line breaks (CRLF) and sent to the server (for backward compatibility).<br />
  For other content-type values:<br />
  　If defined multiple times, all values are joined with line breaks (CRLF) and sent to the server.
- **--param-charset=character encoding**: Specify the character encoding. For example, Shift_JIS, EUC-JP, or UTF-8. The default is UTF-8.
- **--param-input-file=filename \[2.6.40\]**: To send a large amount of data that cannot be specified with the --param option, specify a file containing the data to send.<br />
  If the specified path is not absolute, it is interpreted as a path relative to \[the folder of the executing ghost\]/ghost/master/.<br />
  Do not specify --param at the same time.<br />
  The contents are generally not inspected, so the caller is responsible for handling character encoding, encoding, and other details.<br />
  However, for multipart/form-data only, the first line is read and interpreted as a delimiter between fields.<br />
  The specified file path must be under SSP's control (at or below the location of SSP.exe, or below a folder specified for listing ghosts, etc.).
- **--progress-notify \[2.6.44\]**: During downloads, notify the [OnExecuteHTTPProgress](../../shiori-event/other-communication/OnExecuteHTTPProgress.md) event (or [OnExecuteICalProgress](../../shiori-event/other-communication/OnExecuteICalProgress.md) for ical-get/ical-post \[2.8.90\]); if the event ID begins with On, notify an event with Progress appended to it.<br />
  If an ID beginning with On is specified, SHIORI Event \[the specified ID\]Progress occurs instead of the event listed above.<br />
  Example: with --async=OnExample, OnExampleProgress<br />
  Events are notified continuously while downloading, which reduces download speed.<br />
  Also note that when outputting to a file, the file is temporarily closed when an event is notified and reopened after the response is received, further reducing download speed.
- **--streaming or --streaming=type \[2.8.14\]**: Specify streaming behavior for HTTP requests. Use --streaming=sse for Server-Sent Events, or --streaming=text for newline-delimited streaming (such as NDJSON).<br />
  If --streaming is specified without a type, streaming is handled appropriately according to the response Content-Type from the server.<br />
  Received data is notified through the [OnExecuteHTTPStreaming](../../shiori-event/other-communication/OnExecuteHTTPStreaming.md) event, or, if the event ID begins with On, through an event with Streaming appended, such as OnHogehogeStreaming.
- **--sync=ID \[2.6.44\]**: Behaves the same as --async, except that Sakura Script execution is paused until the process completes.
- **--timeout=seconds**: Specify how long to wait for a response (not the time required for the download). The maximum is 300 seconds.<br />
  If no response is received within the specified time, the SHIORI event "OnExecuteHTTPFailure" is notified, and Reference4 contains "timeout".
- **--to=yyyymmdd \[2.8.90\]**: Only for ical-get/ical-post and rss-get/rss-post \[2.8.92\]. See [※iCal filtering options](bang-execute-ical-post-URL.note.md) and [※RSS filtering options](bang-execute-rss-post-URL.note.md).<br />
  The end date of the period for events to return (inclusive).<br />
  \[2.8.92\] For rss-get/rss-post, this is the upper bound for the update dates of returned items (through the end of that day). No upper bound applies if omitted.
- **--m_websocketProtocol=Sec-Websocket-Protocol \[2.8.08\]**: Specify the Sec-Websocket-Protocol header to use when connecting to a WebSocket. If not specified, this header is not sent.
