# http/rss/ical/websocket 选项

- **--accept=Accept请求头内容 \[2.7.34\]**: 指定Accept请求头，用于指定可接收的Content-Type格式。
- **--accept-language=Accept-Language请求头内容 \[2.7.34\]**: 指定用于控制国际化相关行为的Accept-Language请求头。
- **--async=识别ID**: 不等待处理完成，继续执行Sakura Script，并在处理完成后通知事件。<br />
  HTTP时为[OnExecuteHTTPComplete](../../shiori-event/other-communication/OnExecuteHTTPComplete.md)或[OnExecuteHTTPFailure](../../shiori-event/other-communication/OnExecuteHTTPFailure.md)。<br />
  RSS时为[OnExecuteRSSComplete](../../shiori-event/other-communication/OnExecuteRSSComplete.md)或[OnExecuteRSSFailure](../../shiori-event/other-communication/OnExecuteRSSFailure.md)。<br />
  iCal时为[OnExecuteICalComplete](../../shiori-event/other-communication/OnExecuteICalComplete.md)或[OnExecuteICalFailure](../../shiori-event/other-communication/OnExecuteICalFailure.md)。 \[2.8.90\]<br />
  WebSocket时会在连接、接收、断开连接的各个时机触发[OnExecuteWebSocketOpen](../../shiori-event/other-communication/OnExecuteWebSocketOpen.md)/[Receive](../../shiori-event/other-communication/OnExecuteWebSocketReceive.md)/[Reconnect](../../shiori-event/other-communication/OnExecuteWebSocketReconnect.md)/[Close](../../shiori-event/other-communication/OnExecuteWebSocketClose.md)/[Failure](../../shiori-event/other-communication/OnExecuteWebSocketFailure.md)（始终为Async模式，因此不能使用--sync）。<br />
  如果指定的ID不以On开头，则会触发与上述事件名一致的事件。<br />
  如果指定的ID以On开头，HTTP/RSS/iCal会触发\[指定的ID\]（成功）/\[指定的ID\]Failure（失败）。WebSocket会触发\[指定的ID\]Open/\[指定的ID\]（接收）/\[指定的ID\]Reconnect/\[指定的ID\]Close/\[指定的ID\]Failure。<br />
  示例：--async=OnExample时，HTTP/RSS/iCal→OnExample/OnExampleFailure，WebSocket→OnExampleOpen/OnExample/OnExampleReconnect/OnExampleClose/OnExampleFailure<br />
  但是，SSLInfo类事件([OnExecuteHTTPSSLInfo](../../shiori-event/other-communication/OnExecuteHTTPSSLInfo.md)/[OnExecuteRSS_SSLInfo](../../shiori-event/other-communication/OnExecuteRSS_SSLInfo.md)/[OnExecuteICal_SSLInfo](../../shiori-event/other-communication/OnExecuteICal_SSLInfo.md)/[OnExecuteWebSocket_SSLInfo](../../shiori-event/other-communication/OnExecuteWebSocket_SSLInfo.md))不受此选项影响，即使指定以On开头的ID，也始终会以以上事件名通知。<br />
  如果要暂时中断Sakura Script的执行，请改用--sync（不能用于WebSocket）。
- **--authorization=Authorization请求头内容 \[2.6.37\]**: 需要Authorization请求头（例如OAuth）时，预先设置该请求头。
- **--cookie=Cookie数据**: Cookie数据；必要时可直接指定OnExecuteHTTPComplete的Reference5值。
- **--content-type=(multipart/form-data | application/x-www-form-urlencoded | 其他任意指定)**: 仅限http-post。指定如何发送通过param指定的参数。<br />
  未指定时使用application/x-www-form-urlencoded。<br />
  请注意，根据指定的格式，param的写法可能会受到限制。<br />
  从\[2.6.37\]起，该信息会直接反映到Content-Type请求头中。
- **--expand 或 --expand=天数 \[2.8.90\]**: 仅限ical-get/ical-post。请参阅[※iCal筛选选项](bang-execute-ical-post-URL.note.md)。<br />
  展开RRULE重复项，并为每次「发生」分别返回一条记录。指定天数时，该值将作为未指定--to时的时间段长度（默认30天）。
- **--file=文件名**: 指定所获取数据的保存名称。数据将保存到\[执行此操作的ghost文件夹\]/ghost/master/var/文件名。
- **--from=yyyymmdd \[2.8.90\]**: 仅限ical-get/ical-post、rss-get/rss-post \[2.8.92\]。请参阅[※iCal筛选选项](bang-execute-ical-post-URL.note.md)和[※RSS筛选选项](bang-execute-rss-post-URL.note.md)。<br />
  返回事件的时间段起始日期。省略时为当天。<br />
  \[2.8.92\] 对于rss-get/rss-post，这是返回项目的更新时间下限（从当天0点开始）。省略时不设下限。
- **--header=SomeHeader: 请求头内容 \[2.6.40\]**: 设置任意名称的请求头。名称与内容之间必须使用冒号分隔。<br />
  该选项会覆盖SSP提供的请求头信息，使用时请注意不要指定冲突的内容。
- **--insecure \[2.7.34\]**: 跳过TLS证书验证。
- **--limit=条数 \[2.8.90\]**: 仅限ical-get/ical-post、rss-get/rss-post \[2.8.92\]。请参阅[※iCal筛选选项](bang-execute-ical-post-URL.note.md)和[※RSS筛选选项](bang-execute-rss-post-URL.note.md)。<br />
  返回事件的最大条数。省略时为200条，指定0则不限制。<br />
  只写--limit时，时间段模式的起始日期为当天。如果--from、--to、--expand、--limit均未指定，则不限制返回条数（返回全部记录）。<br />
  \[2.8.92\] 对于rss-get/rss-post，仅在指定时才会按新到旧的顺序截取指定条数。省略或指定0时不限制；只写--limit也不会筛选时间段。
- **--log=文件名**: 将与服务器之间的所有通信内容记录到日志中。主要用于开发时调试。
- **--nodescript**: 不显示在线显示和下载状态。
- **--nofile=参数(字符编码) \[2.5.77\]**: 不创建临时文件，而是在内存中展开获取的数据，并将其存入事件的Reference3。<br />
  参数用于指定解读所获取数据时使用的字符编码。未指定时视为UTF-8。<br />
  Reference中不能包含换行符，因此换行符会被转换为字节值1。<br />
  可获取的数据大小上限为128KB。<br />
  \[2.8.90\] 对于rss-get/rss-post、ical-get/ical-post，由于需要用于解析的文件，因此会忽略此选项。
- **--no-cache \[2.7.34\]**: 指定Cache-Control: no-cache，以抑制缓存的使用。
- **--param=参数**: 指定get/post/put的参数。可重复指定。<br />
  multipart/form-data时：<br />
  　按--param=字段名=数据的格式重复指定所需数量。<br />
  　示例： --param=message_body=数据<br />
  application/x-www-form-urlencoded时：<br />
  　按--param=字段名=数据的格式重复指定所需数量时，所有参数会以&连接后发送到服务器。<br />
  　除此以外，所有参数都会以换行符(CRLF)连接后发送到服务器（为兼容旧版本而保留的处理方式）。<br />
  使用其他content-type时：<br />
  　指定多个参数时，所有参数都会以换行符(CRLF)连接后发送到服务器。
- **--param-charset=字符编码**: 指定字符编码。可使用Shift_JIS、EUC-JP、UTF-8等；默认值为UTF-8。
- **--param-input-file=文件名 \[2.6.40\]**: 如果要发送无法通过--param选项指定的大容量数据，请指定存储发送数据的文件。<br />
  如果指定的不是绝对路径，则视为相对于\[执行此操作的ghost文件夹\]/ghost/master/的路径。<br />
  不要同时指定--param。<br />
  原则上不会检查文件内容，因此字符编码、编码方式等应由使用方负责处理。<br />
  但是，仅在multipart/form-data时，会读取第一行并将其解释为字段间分隔符。<br />
  指定的文件路径必须位于SSP管辖范围内（SSP.exe所在位置及其子目录，或用于枚举ghost等的指定文件夹及其子目录）。
- **--progress-notify \[2.6.44\]**: 下载过程中通知[OnExecuteHTTPProgress](../../shiori-event/other-communication/OnExecuteHTTPProgress.md)事件（ical-get/ical-post时为[OnExecuteICalProgress](../../shiori-event/other-communication/OnExecuteICalProgress.md) \[2.8.90\]）；如果事件ID以On开头，则通知在其后添加Progress的事件。<br />
  如果指定的ID以On开头，则会触发SHIORI Event \[指定的ID\]Progress，而不是上述事件。<br />
  示例：--async=OnExample时为OnExampleProgress<br />
  下载过程中会逐次执行事件通知，因此下载速度会下降。<br />
  另外，输出到文件时，每次事件通知都会暂时关闭文件，并在收到响应后重新打开文件，因此下载速度还会进一步下降，请注意。
- **--streaming 或 --streaming=类型 \[2.8.14\]**: 指定HTTP请求的流式处理方式。--streaming=sse表示Server-Sent Events，--streaming=text表示按换行符分隔的流式处理（例如NDJSON）<br />
  使用不带类型的--streaming时，会根据服务器响应的Content-Type进行相应的流式处理。<br />
  接收的数据会通过[OnExecuteHTTPStreaming](../../shiori-event/other-communication/OnExecuteHTTPStreaming.md)事件通知；如果事件ID以On开头，则会通知在其后添加Streaming的事件，例如OnHogehogeStreaming。
- **--sync=识别ID \[2.6.44\]**: 除了会暂时停止Sakura Script的执行并等待处理完成以外，其行为与指定--async相同。
- **--timeout=秒数**: 指定等待响应的时间（不是下载所需的时间）。最长为300秒。<br />
  如果在指定的秒数内未收到响应，则会通知SHIORI事件「OnExecuteHTTPFailure」，并在Reference4中写入「timeout」。
- **--to=yyyymmdd \[2.8.90\]**: 仅限ical-get/ical-post、rss-get/rss-post \[2.8.92\]。请参阅[※iCal筛选选项](bang-execute-ical-post-URL.note.md)和[※RSS筛选选项](bang-execute-rss-post-URL.note.md)。<br />
  返回事件的时间段结束日期（包含当天）。<br />
  \[2.8.92\] 对于rss-get/rss-post，这是返回项目的更新时间上限（截至当天结束）。省略时不设上限。
- **--m_websocketProtocol=Sec-Websocket-Protocol \[2.8.08\]**: 指定WebSocket连接时使用的Sec-Websocket-Protocol请求头。未指定时不会发送此请求头。
