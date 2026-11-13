# request/response

Like SHIORI and other protocols, this is a custom protocol modeled on HTTP.<br />
The request must specify a Charset. If it is omitted, the request either results in an error or is interpreted using the OS default encoding.

- The line ending is CR+LF.
- The request ends with a blank line ((CR+LF)x2 including the end of the preceding line).
- In cases such as EXECUTE, additional data may be included at the end of the response. After the headers, one blank line precedes the additional data, and another blank line marks the end. If there is no additional data, the response may end with just the blank line immediately after the headers.
- For compatibility, a response with additional data may contain only the additional data, with no headers, including Charset. In that case, it may be assumed to use the same encoding as the request.
- The SSTP versions of the request and response may differ. Do not interpret them based on the version number.

## request

### request sample

```
SEND SSTP/1.0
Charset: UTF-8
Sender: SSTPクライアント
Script: \h\s0テストー。\u\s[10]テストやな。
Option: notranslate
```

### Headers common to all request methods

For method-specific headers, see the descriptions of the individual methods below.

- **Charset**: The character encoding of the request. It should appear on the first line.<br />
  UTF-8 is recommended unless there is a reason to use another encoding.
- **Sender**: A string identifying the sender, such as "SSTP sending tool". For the COMMUNICATE method, this is the sending ghost's `\0` name.
- **SecurityLevel**: Specifies the security level used when processing with SHIORI or Sakura Script. Either local or external.<br />
  Valid only for DirectSSTP or requests that clearly originate locally, such as from 127.0.0.1.<br />
  SSTP over HTTP is always considered external, except when sent from HTML or similar content served from localhost.
- **SecurityOrigin \[SSP 2.6.59\]**: A URL-like string identifying the originating server. It uses the following formats. The concept is the same as the [HTTP Origin header](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Origin).<br />
  SecurityOrigin: null<br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\><br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\>:&lt;port\><br />
  scheme is usually one of http, https, or sstp. hostname is the originating server name or IP address. port is the port available for receiving replies.<br />
  If omitted, it is treated as null.<br />
  For SSTP over HTTP, the value of the HTTP Origin header is always used, and SecurityOrigin in SSTP is ignored.
- **Option**: Specifies options for how Sakura Script executed via SSTP is handled.<br />
  Multiple options can be specified, separated by commas. The supported strings are as follows.<br />
  nodescript : Disables SSTP display in the balloon (remote SSTP is disabled)<br />
  notranslate : Skips translation processing by OnTranslate or MAKOTO<br />
  nobreak : Waits until the currently running script finishes without interrupting it<br />
  strict : Records Sakura Script interpretation failures in the error log. These include references to nonexistent surfaces (`\s`), animations (`\i`), or balloons (`\b`); unknown tags, `\![コマンド]`, or `\&[実体参照]`; missing required \[\] or numbers; and invalid values for `\p`, `\b`, `\n`, `\c`, or `\q`. Applies to SEND scripts and scripts returned by ghosts for NOTIFY/GIVE \[SSP 2.8.94\]
- **ID**: Used for what is called "Owned SSTP". Specifying the ID sent by [SHIORI uniqueid](../../list/shiori-event/notify/uniqueid.md) or the [FMO identification ID (SSP only)](../fmo-mutex/index.md) bypasses security checks, locks, and similar restrictions, and treats this SSTP with the same priority as processing within the ghost.<br />
  SecurityLevel is set to local, and interrupting playback is forced even when interruptions are prohibited, such as by `\t`.
- **X-SSTP-PassThru-(arbitrary string)**: A header passed directly to SHIORI when communicating with the ghost, such as through NOTIFY.<br />
  Only minimal processing, such as character encoding conversion, is performed; the (arbitrary string) portion and the content are relayed unchanged.
- **HWnd**: DirectSSTP only. Specifies the window handle to which the response should be sent.<br />
  The window handle data (equivalent to a pointer) is treated as an unsigned decimal integer and converted to a string.<br />
  If omitted, WM_COMMUNICATE's wParam is used.
- **ReceiverGhostHWnd \[SSP 2.5.57\]**: (Socket)SSTP only. Specifies the window handle of the `\0` of the ghost to which the request should be sent.<br />
  Specifying this fixes the ghost that handles the request, allowing the same processing as DirectSSTP even over a socket.<br />
  If it is not found, processing ends immediately with a 404 Not Found error.
- **ReceiverGhostName \[SSP 2.5.57\]**: (Socket)SSTP only. Specifies the `\0` name of the ghost to which the request should be sent.<br />
  Specifying this fixes the ghost that handles the request, allowing the same processing as DirectSSTP even over a socket. This is the name-based equivalent of HWnd.<br />
  If it is not found, processing ends immediately with a 404 Not Found error.
- **ReceiverGhostUUID \[SSP 2.9.35\]**: (Socket)SSTP only. Specifies the [UUID](../../list/propertysystem/property-system/general-property/uuid.md) of the running ghost to which the request should be sent.<br />
  Specifying this fixes the ghost that handles the request, allowing the same processing as DirectSSTP even over a socket. This is the UUID-based equivalent of HWnd and avoids confusing ghosts with the same name.<br />
  If multiple ghosts with the same UUID are running, the displayed ghost is selected; if none is displayed, the first one in the list of running ghosts is selected.<br />
  If no running ghost has a matching UUID, processing ends immediately with a 404 Not Found error (the same applies to values that are not in UUID format).<br />
  If multiple ReceiverGhostHWnd, ReceiverGhostUUID, or ReceiverGhostName headers are specified, they are evaluated in that order, and the first ghost found is used.

## response

### response sample (no data)

```
SSTP/1.4 200 OK
Charset: UTF-8
Script: \h\s0テストー。\u\s[10]テストやな。
```

### response sample (with data)

```
SSTP/1.4 200 OK
Charset: UTF-8
Script: \h\s0テストー。\u\s[10]テストやな。

追加データはここ
```

### Headers common to all response methods

- **Charset**: The character encoding of the request. It should appear on the first line.<br />
  UTF-8 is recommended unless there is a reason to use another encoding.<br />
  It may be deliberately omitted to resolve compatibility issues. In that case, assume the same encoding as the request.
- **X-SSTP-PassThru-(arbitrary string)**: A header returned directly from SHIORI when communicating with the ghost, such as through NOTIFY.<br />
  Only minimal processing, such as character encoding conversion, is performed; the (arbitrary string) portion and the content are relayed unchanged.

### response status codes

As with HTTP, 200-series codes indicate successful acceptance; all others indicate errors.

- **200 OK**: Completed successfully (with a return value)
- **204 No Content**: Completed successfully (without a return value)
- **210 Break**: Execution started but was interrupted during script execution<br />
  Note: This occurs only in extremely limited circumstances, such as SEND/1.x with Entry; normally 200 or 204 is returned immediately.
- **400 Bad Request**: The request has a problem that cannot be handled
- **404 Not Found (SSP only)**: The ghost specified in the SSTP request is not installed or running
- **408 Request Timeout**: Timeout: communication with the ghost/SHIORI failed, for example (rarely occurs under normal conditions)
- **409 Conflict**: Interruptions are prohibited, such as by the `\t` tag, or another request is being processed
- **413 Payload Too Large (SSP only)**: The SSTP request was too long and processing was refused
- **420 Refuse**: Reception was refused due to the ghost's settings
- **500 Internal Server Error (SSP only)**: Processing could not be completed due to a problem detected internally by the implementation
- **501 Not Implemented**: Processing failed because the request contained an unimplemented command or similar
- **503 Service Unavailable**: SSTP cannot be accepted due to internal conditions in the implementation
- **505 Version Not Supported (SSP only)**: The SSTP version is invalid (below 1.0, 3.0 or later, etc.)
- **512 Invisible**: The ghost is not displayed, such as when minimized, and cannot process anything
