# SAORI over DirectSSTP

## Sending a request

As with [Direct SSTP](../sstp/direct.md), use `WM_COPYDATA` (`dwData = 9801`), put a SAORI/1.0 request in `lpData` instead of an SSTP request, and send it to your ghost's window (`hwnd` in [FMO](../fmo-mutex/index.md)).<br />
Window and `WM_COPYDATA` handling (sending with SendMessage functions, `cbData`, and so on) is the same as for Direct SSTP.

```
EXECUTE SAORI/1.0
Module: internal_crypto
Charset: UTF-8
Sender: YAYA
SecurityLevel: Local
HWnd: 1234
Argument0: Digest
Argument1: sha256
Argument2: abc
```

- **Module**: Required. The name of the module to call. Specify the DLL name without `.dll` (e.g., `internal_crypto`, `string`). Case-insensitive.<br />
  If absent, returns 400 (`ErrorDescription: invalid parameter`); if the module is unknown, returns 400 (`ErrorDescription: unknown module`).
- **HWnd**: The window that receives the response. If omitted, the window in `wParam` of `WM_COPYDATA` is used (the same rule as for SSTP over Direct SSTP).
- **Charset**: The request's character encoding. The response uses the same encoding.
- **SecurityLevel**: Always treated as `Local` over Direct SSTP (the header value is ignored).
- **Sender**: The caller's name. The baseware does not use it.
- **Argument\[n\]**: Arguments. The same as in SAORI/1.0.

## Receiving a response

The response is sent to the `HWnd` (or `wParam`) window via `WM_COPYDATA` (`dwData = 9801`). It is a SAORI/1.0 response beginning with `SAORI/`.<br />
The baseware sends the response while processing the request, so it arrives before the sender's SendMessage call returns.

## Accepted transports

SAORI over DirectSSTP is accepted only over Direct SSTP.<br />
Sending a SAORI/1.0 request over socket SSTP or SSTP over HTTP returns `SAORI/1.0 400 Bad Request` and `ErrorDescription: direct sstp only` (for SSTP over HTTP, this response is returned as the body of an HTTP 200 response).<br />
SAORI requests are not recorded in the SSTP log.

## Calling ghost

When sent to a ghost's window, that ghost is the caller.<br />
If the calling ghost cannot be identified, such as when sent to the baseware's main window, the request is treated as having no ghost (unlike SSTP over Direct SSTP, a displayed ghost is not substituted). Operations that do not use a ghost work normally, while operations that depend on a ghost ([asynchronous calls](async.md) that deliver results via events, relative paths based on the ghost's folder, and so on) return 400 (`ErrorDescription: ghost required`).<br />
The `ReceiverGhostName` / `ReceiverGhostHWnd` / `ReceiverGhostUUID` headers are ignored.

## Preventing response mix-ups

The baseware treats incoming messages beginning with `SAORI/` (or `SSTP/`) as responses, not requests.

## Feature detection

To check whether a module is available, send `GET Version SAORI/1.0` with `Module`. If available, it returns `SAORI/1.0 200 OK` (`Result: SSP Internal` in SSP).<br />
Versions of SSP that do not support this extension (2.9.12 and earlier) read SAORI/1.0 requests as SSTP requests and return an SSTP error (`SSTP/1.0 501 Not Implemented` for `GET Version`, `SSTP/1.0 400 Bad Request` for `EXECUTE`).<br />
The sender should consider the module unavailable if the response does not begin with `SAORI/1.0 200` or if no response arrives.<br />
A list of SSP's built-in modules and their functions can be obtained from [internal_system](internal_system/index.md). The options and algorithm names accepted by functions, including those added in newer versions of SSP, can be checked with [Describe](internal_system/internal_system.Describe.md).

## ErrorDescription

On failure, the response includes an `ErrorDescription` header giving the reason as a fixed English string. This header is not in the original SAORI/1.0 specification; it follows the header of the same name in SHIORI/3.0.<br />
The following values are used by all modules. For others, see each module's documentation.

- **direct sstp only**: 400. Sent over a transport other than Direct SSTP.
- **unknown module**: 400. The module specified by `Module` does not exist.
- **unknown function**: 400. The function name (`Argument0`) does not exist in the module.
- **ghost required**: 400. An operation dependent on a ghost was requested when the calling ghost could not be identified.
- **invalid parameter**: 400. `Module` is missing, or an argument is missing or invalid.

Compatibility modules (compatible with DLL SAORI modules) may return 400 without `ErrorDescription`, as in the original implementations.

## Values that cannot be written in headers

SAORI header values cannot contain newlines or leading or trailing whitespace (commas are allowed). For built-in modules, pass such data using a [format](internal.md#バイト列の入力の形式) such as `--data-in=base64`.
