# SAORI over DirectSSTP

## Sending

As with [Direct SSTP](../sstp/direct.md), use `WM_COPYDATA` (`dwData = 9801`), put a SAORI/1.0 request in `lpData` instead of an SSTP request, and send it to your own ghost's window (the `hwnd` from [FMO](../fmo-mutex/index.md)).<br />
Window and `WM_COPYDATA` handling (sending with SendMessage-type functions, `cbData`, etc.) are the same as for Direct SSTP.

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

- **Module**: Required. The name of the module to call. Write it without the `.dll` extension from the DLL name (e.g. `internal_crypto`, `string`). Case is not significant.<br />
  If absent, returns 400 (`ErrorDescription: invalid parameter`); if the module is unknown, returns 400 (`ErrorDescription: unknown module`).
- **HWnd**: The window to receive the response. If omitted, the window in `wParam` of `WM_COPYDATA` is used (the same rule as for SSTP in Direct SSTP).
- **Charset**: The character encoding of the request. The response is returned in the same encoding.
- **SecurityLevel**: In Direct SSTP, this is always treated as `Local` (the header value is ignored).
- **Sender**: The name of the caller. The baseware does not use this.
- **Argument\[n\]**: An argument. Same as in SAORI/1.0.

## Receiving responses

The response is returned to the `HWnd` (or `wParam`) window via `WM_COPYDATA` (`dwData = 9801`). The content is an SAORI/1.0 response beginning with `SAORI/`.<br />
The baseware sends the reply while processing the request, so it arrives before the sender's SendMessage returns.

## Accepted routes

SAORI over DirectSSTP is accepted only over Direct SSTP.<br />
If an SAORI/1.0 request is sent over socket SSTP or SSTP over HTTP, `SAORI/1.0 400 Bad Request` and `ErrorDescription: direct sstp only` are returned (for SSTP over HTTP, this response is returned as the body of the HTTP 200 response).<br />
SAORI requests are not recorded in the SSTP log.

## Calling ghost

If the request is sent to a ghost's window, that ghost is treated as the caller.<br />
If the calling ghost cannot be identified, such as when the request is sent to the baseware's main window, it is treated as "no ghost" (unlike SSTP over Direct SSTP, the ghost currently being displayed is not used as a fallback). Operations that do not use a ghost work normally, while operations that depend on a ghost (such as [asynchronous calls](async.md) that deliver results through events, or relative paths based on the ghost's folder) return 400 (`ErrorDescription: ghost required`).<br />
The `ReceiverGhostName` / `ReceiverGhostHWnd` headers are ignored.

## Preventing response mix-ups

The baseware treats received messages that begin with `SAORI/` (and `SSTP/`) as responses, not requests.

## Checking supported features

To check whether a module is available, send `GET Version SAORI/1.0` with `Module` attached. If it is available, the response is `SAORI/1.0 200 OK` (`Result: SSP Internal` in SSP).<br />
SSP versions that do not support this extension (2.9.12 and earlier) read SAORI/1.0 requests as SSTP requests and return SSTP errors (`SSTP/1.0 501 Not Implemented` for `GET Version`, and `SSTP/1.0 400 Bad Request` for `EXECUTE`).<br />
The sender should determine that the module is unavailable if the response does not begin with `SAORI/1.0 200`, or if no response is received.<br />
The list of SSP's built-in modules and their functions is available at [internal_system](internal_system/index.md). Use [Describe](internal_system/internal_system.Describe.md) to find the options and algorithm names accepted by each function (including those added in newer SSP versions).

## ErrorDescription

On failure, the response includes an `ErrorDescription` header giving the reason for the failure (a fixed English string). This header is not in the original SAORI/1.0 specification; it follows the header of the same name in SHIORI/3.0.<br />
The following are used by all modules. For others, see the description of each module.

- **direct sstp only**: 400. When sent through a route other than Direct SSTP.
- **unknown module**: 400. When the module specified by `Module` does not exist.
- **unknown function**: 400. When the function name (`Argument0`) does not exist in the module.
- **ghost required**: 400. When a ghost-dependent operation is requested but the calling ghost cannot be identified.
- **invalid parameter**: 400. When `Module` is missing, or an argument is missing or invalid.

Compatibility modules (SAORI compatibility for DLLs) may return a 400 without an `ErrorDescription`, as in the original implementation.

## Values That Cannot Be Written in Headers

SAORI header values cannot contain line breaks or leading or trailing whitespace (commas are allowed). Pass such data using a [format](internal.md#バイト列の入力の形式) such as `--data-in=base64` with built-in modules.
