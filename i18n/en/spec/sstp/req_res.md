# request/response

Like SHIORI and other protocols, SSTP is a proprietary protocol modeled after HTTP.<br />
Specifying the request charset is required. If it is not specified, an error may occur, or the request may be interpreted using the OS default charset.

- The line ending is CR+LF.
- A request ends with a blank line (a total of (CR+LF)x2, including the end of the preceding line).
- A response may contain additional data at the end, for example in the case of EXECUTE. After the headers end, there is a blank line, then the additional data, then another blank line before the end. If there is no additional data, the response may end with only the blank line immediately after the headers.
- For compatibility, a response with additional data may contain no headers at all, including Charset, and return only the additional data. In that case, you can assume it uses the same charset as the request.
- The SSTP version in the request and response may differ. Do not make interpretations that depend on the version number.

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

For method-specific headers, see the descriptions of each method below.

- **Charset**: The request charset. It is recommended that this appear on the first line.<br />
  UTF-8 is recommended unless there is a particular reason to use another charset.
- **Sender**: A string identifying the sender, such as "SSTP送信ツール". For the COMMUNICATE method, this is the name of the source ghost's `\0`.
- **SecurityLevel**: Specifies the security level for processing by SHIORI or Sakura Script. Either local or external.<br />
  Valid only for DirectSSTP, or for requests that clearly come from the local machine, such as those from 127.0.0.1.<br />
  SSTP over HTTP is always treated as external, except when sent from HTML and similar content served from localhost.
- **SecurityOrigin \[SSP 2.6.59\]**: A URL-like string identifying the source server. It has the following formats. The concept is the same as that of the [Origin HTTP header](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Origin).<br />
  SecurityOrigin: null<br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\><br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\>:&lt;port\><br />
  The scheme is usually one of http, https, or sstp. The hostname is the source server name or IP address. The port is the port that can receive replies.<br />
  If not specified, null is assumed.<br />
  For SSTP over HTTP, the contents of the HTTP Origin header are always set, and SecurityOrigin in SSTP is ignored.
- **Option**: Specifies options for how Sakura Script executed by SSTP is handled.<br />
  Multiple values can be specified as a comma-separated list. The available values are as follows.<br />
  nodescript : Disable SSTP display in the balloon (SSTP from remote sources is disabled)<br />
  notranslate : Do not perform translation using OnTranslate or MAKOTO<br />
  nobreak : Wait for the currently executing script to finish without interrupting it<br />
  strict : Log locations where Sakura Script parsing fails. This applies to references to nonexistent surfaces (`\s`), animations (`\i`), or balloons (`\b`); unknown tags, `\![コマンド]`, and `\&[実体参照]`; missing required \[\] or numbers; and invalid values for `\p`, `\b`, `\n`, `\c`, or `\q`. Applies to scripts in SEND and scripts returned by ghosts in NOTIFY/GIVE \[SSP 2.8.94\]
- **ID**: Identifies what is called "Owned SSTP". Specifying an ID received via [SHIORI uniqueid](../../list/shiori-event/notify/uniqueid.md) or an [FMO identifier (SSP only)](../fmo-mutex/index.md) causes this SSTP to be handled with the same priority as processing inside the ghost, ignoring various security checks, locks, and so on.<br />
  This sets SecurityLevel to local and also allows forced interruption and playback, even when interruption is disabled by `\t` and similar tags.
- **X-SSTP-PassThru-(arbitrary string)**: A header passed directly to SHIORI when communicating with the ghost, such as with NOTIFY.<br />
  Only minimal processing, such as charset conversion, is performed; the (arbitrary string) portion and its contents are relayed as-is.
- **HWnd**: For DirectSSTP only, specifies the window handle to which the response should be sent.<br />
  The window handle (pointer equivalent) is treated as an unsigned decimal integer and converted to a string.<br />
  If omitted, WM_COMMUNICATE's wParam is used.
- **ReceiverGhostHWnd \[SSP 2.5.57\]**: For (Socket)SSTP only, specifies the window handle of the ghost's `\0` to which the request should be sent.<br />
  Specifying this fixes which ghost handles the request, allowing the same processing as DirectSSTP even over a socket.<br />
  If no match is found, processing immediately fails with 404 Not Found.
- **ReceiverGhostName \[SSP 2.5.57\]**: For (Socket)SSTP only, specifies the name of the ghost's `\0` to which the request should be sent.<br />
  Specifying this fixes which ghost handles the request, allowing the same processing as DirectSSTP even over a socket. This is the name-based equivalent of HWnd.<br />
  If no match is found, processing immediately fails with 404 Not Found.

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

- **Charset**: The request charset. It is recommended that this appear on the first line.<br />
  UTF-8 is recommended unless there is a particular reason to use another charset.<br />
  It may be deliberately omitted for compatibility. In that case, assume the same charset as the request.
- **X-SSTP-PassThru-(arbitrary string)**: A header returned directly from SHIORI when communicating with the ghost, such as with NOTIFY.<br />
  Only minimal processing, such as charset conversion, is performed; the (arbitrary string) portion and its contents are relayed as-is.

### Response status codes

As with HTTP, codes in the 200 range indicate successful acceptance; all others indicate errors.

- **200 OK**: Completed successfully (with a return value)
- **204 No Content**: Completed successfully (without a return value)
- **210 Break**: Executed, but interrupted while the script was running<br />
  ※Only occurs in very limited situations, such as SEND/1.x with Entry; normally returns 200 or 204 immediately.
- **400 Bad Request**: The request contains an issue that cannot be handled
- **404 Not Found ※SSP only**: For SSTP specifying a ghost, the specified ghost is not installed or running
- **408 Request Timeout**: Timeout: unable to communicate with the ghost/SHIORI, for example (this rarely occurs in normal operation)
- **409 Conflict**: Interruption is disabled by a tag such as `\t`, or another request is being processed
- **413 Payload Too Large ※SSP only**: The SSTP request was too long and was rejected
- **420 Refuse**: Reception was refused due to the ghost's settings
- **500 Internal Server Error ※SSP only**: Unable to complete processing due to an issue detected internally by the processing system
- **501 Not Implemented**: Unable to process because the request contains an unimplemented command or similar
- **503 Service Unavailable**: SSTP cannot be accepted due to internal conditions in the processing system
- **505 Version Not Supported ※SSP only**: The SSTP version is invalid (for example, below 1.0 or 3.0 and above)
- **512 Invisible**: The ghost is not displayed, for example because it is minimized, and cannot process anything
