# request/response

Like SHIORI and other protocols, this is a custom protocol modeled on HTTP.<br />
The request must specify a Charset. If omitted, an error occurs or the request is interpreted using the OS default character encoding.

- The line ending is CR+LF.
- A request ends with a blank line ((CR+LF)x2, including the end of the preceding line).
- A response may contain additional data at the end, as in the case of EXECUTE. After the headers, a blank line is followed by the additional data and another blank line. If there is no additional data, the response may end with just the blank line immediately after the headers.
- For compatibility, a response with additional data may contain no headers at all, including Charset, and return only the additional data. In that case, the encoding may be assumed to be the same as the request's.
- The SSTP versions of the request and response may differ. Do not interpret them based on the version number.

## request

### request example

```
SEND SSTP/1.0
Charset: UTF-8
Sender: SSTPクライアント
Script: \h\s0テストー。\u\s[10]テストやな。
Option: notranslate
```

### Headers common to all request methods

For method-specific headers, see the descriptions of individual methods below.

- **Charset**: The character encoding of the request. It should preferably appear on the first line.<br />
  UTF-8 is recommended unless there is a reason to use another encoding.
- **Sender**: A string identifying the sender, such as "SSTP sending tool". For the COMMUNICATE method, this is the sending ghost's `\0` name.
- **SecurityLevel**: Specifies the security level when processing with SHIORI or Sakura Script. Either local or external.<br />
  Only valid for DirectSSTP or requests that clearly originate locally, such as from 127.0.0.1.<br />
  SSTP over HTTP is always treated as external, except when sent from HTML or similar content served from localhost.
- **SecurityOrigin \[SSP 2.6.59\]**: A URL-like string identifying the source server, in one of the following formats. It follows the same concept as the [HTTP Origin header](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Origin).<br />
  SecurityOrigin: null<br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\><br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\>:&lt;port\><br />
  scheme is usually one of http, https, or sstp. hostname is the source server name or IP. port is a port that can receive replies.<br />
  If not specified, it is treated as null.<br />
  For SSTP over HTTP, the HTTP Origin header's value is always used, and SecurityOrigin in the SSTP request is ignored.
- **Option**: Specifies options for how Sakura Script executed via SSTP is handled.<br />
  Multiple options can be specified, separated by commas. The strings are as follows.<br />
  nodescript : Disables SSTP display in the balloon (remote SSTP is disabled)<br />
  notranslate : Does not perform translation processing via OnTranslate or MAKOTO<br />
  nobreak : Waits for the currently executing script to finish without interrupting it<br />
  strict : Records Sakura Script interpretation failures in the error log. These include references to nonexistent surfaces (`\s`), animations (`\i`), or balloons (`\b`); unknown tags, `\![コマンド]`, or `\&[実体参照]`; missing required \[\] or numbers; and invalid values for `\p`, `\b`, `\n`, `\c`, or `\q`. Applies to SEND scripts and scripts returned by a ghost for NOTIFY/GIVE \[SSP 2.8.94\]
- **ID**: What is known as "Owned SSTP". If an ID sent by [SHIORI uniqueid](../../list/shiori-event/notify/uniqueid.md) or the [FMO identification ID (SSP only)](../fmo-mutex/index.md) is specified, this SSTP is treated with the same priority as processing internal to the ghost, bypassing security checks, locks, and so on.<br />
  SecurityLevel is set to local, and playback can forcibly interrupt even when interruptions are prohibited, such as by `\t`.
- **X-SSTP-PassThru-(arbitrary string)**: A header passed directly to SHIORI when communicating with a ghost, such as via NOTIFY.<br />
  Only minimal processing, such as character encoding conversion, is performed; the (arbitrary string) portion and the content are relayed unchanged.
- **HWnd**: DirectSSTP only. Specifies the window handle to which the response should be sent.<br />
  The window handle (equivalent to a pointer) is treated as an unsigned decimal integer and converted to a string.<br />
  If omitted, WM_COMMUNICATE's wParam is used.
- **ReceiverGhostHWnd \[SSP 2.5.57\]**: (Socket)SSTP only. Specifies the window handle of the `\0` of the ghost to which the request should be sent.<br />
  Specifying this fixes the ghost that handles the request, allowing the same processing as DirectSSTP even over a socket.<br />
  If it is not found, processing immediately ends with a 404 Not Found error.
- **ReceiverGhostName \[SSP 2.5.57\]**: (Socket)SSTP only. Specifies the `\0` name of the ghost to which the request should be sent.<br />
  Specifying this fixes the ghost that handles the request, allowing the same processing as DirectSSTP even over a socket. This is the name-based version of HWnd.<br />
  \[SSP 2.9.35\] A UUID may be specified instead of a name to select the ghost with that UUID (equivalent to the dedicated ReceiverGhostUUID).<br />
  If it is not found, processing immediately ends with a 404 Not Found error.
- **ReceiverGhostUUID \[SSP 2.9.35\]**: (Socket)SSTP only. Specifies the [UUID](../../list/propertysystem/property-system/general-property/uuid.md) of the running ghost to which the request should be sent.<br />
  Specifying this fixes the ghost that handles the request, allowing the same processing as DirectSSTP even over a socket. This is the UUID-based version of HWnd and avoids confusing ghosts with the same name.<br />
  If multiple ghosts with the same UUID are running, the displayed ghost is selected, or otherwise the first in the list of running ghosts.<br />
  If no running ghost has a matching UUID, processing immediately ends with a 404 Not Found error (the same applies to values that are not in UUID format).<br />
  If more than one of ReceiverGhostHWnd, ReceiverGhostUUID, and ReceiverGhostName is specified, they are evaluated in that order, and the first ghost found is used.

## response

### response example (without data)

```
SSTP/1.4 200 OK
Charset: UTF-8
Script: \h\s0テストー。\u\s[10]テストやな。
```

### response example (with data)

```
SSTP/1.4 200 OK
Charset: UTF-8
Script: \h\s0テストー。\u\s[10]テストやな。

追加データはここ
```

### Headers common to all response methods

- **Charset**: The character encoding of the request. It should preferably appear on the first line.<br />
  UTF-8 is recommended unless there is a reason to use another encoding.<br />
  This may be deliberately omitted to resolve compatibility issues. In that case, assume the same character encoding as the request.
- **X-SSTP-PassThru-(arbitrary string)**: A header returned directly from SHIORI when communicating with a ghost, such as via NOTIFY.<br />
  Only minimal processing, such as character encoding conversion, is performed; the (arbitrary string) portion and the content are relayed unchanged.

### response status codes

As with HTTP, 200-series codes indicate successful acceptance; all others indicate errors.

- **200 OK**: Completed successfully (with a return value)
- **204 No Content**: Completed successfully (without a return value)
- **210 Break**: Executed, but interrupted during script execution<br />
  Note: This is limited to very specific situations, such as SEND/1.x with Entry; normally, 200 or 204 is returned immediately.
- **400 Bad Request**: The request has a problem that cannot be handled
- **404 Not Found ※SSP only**: In an SSTP request specifying a ghost, the specified ghost is not installed or running
- **408 Request Timeout**: Timeout: unable to communicate with the ghost/SHIORI, for example (rarely occurs under normal conditions)
- **409 Conflict**: Interruptions are prohibited by a `\t` tag or similar, or another request is being processed
- **413 Payload Too Large ※SSP only**: The SSTP request was too long and processing was refused
- **420 Refuse**: Reception was refused due to the ghost's settings
- **500 Internal Server Error ※SSP only**: Processing could not be completed due to a problem detected internally by the implementation
- **501 Not Implemented**: Processing could not be completed because the request included an unimplemented command or similar
- **503 Service Unavailable**: The implementation cannot accept SSTP due to internal circumstances
- **505 Version Not Supported ※SSP only**: The SSTP version is invalid (below 1.0, 3.0 or higher, etc.)
- **512 Invisible**: The ghost is not displayed, for example because it is minimized, and cannot process anything
