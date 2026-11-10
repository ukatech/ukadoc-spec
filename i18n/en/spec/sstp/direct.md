# Direct SSTP

Direct SSTP is a communication specification that uses an IPC mechanism strongly dependent on the operating system. Its protocol specification is the same as (Socket) SSTP, but it is intended to provide lightweight communication by directly specifying a ghost, without using the comparatively resource-intensive TCP/IP.<br />
At present, the specification has been established only for Windows, as follows.

Send [WM_COPYDATA](https://docs.microsoft.com/en-us/windows/win32/dataxchg/wm-copydata) using a SendMessage-family function (Post is not allowed)<br />
SendMessage's hWnd = HWND of the destination ghost [obtained from FMO](../fmo-mutex/index.md)<br />
wParam = HWND of “your own” reply destination. The response is received on the HWND (window) specified for WM_COPYDATA.<br />
lParam = pointer to [COPYDATASTRUCT](https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-copydatastruct)<br />
copydatastruct.lpData = string conforming to the SSTP protocol<br />
copydatastruct.cbData = length of the string<br />
copydatastruct.dwData = 9801<br />
Notes:<br />
For safety, the sender should provide a null-terminated string in lpData, and it is preferable for cbData to include the null terminator.<br />
For safety, the receiver must not assume a null terminator and must always process the data based on cbData.<br />
The receiver should treat the HWND specified as the destination as equivalent to the ghost specified in the SSTP protocol, and prioritize that ghost as much as possible.<br />
Both the receiver and sender are assumed to be GUI applications with at least one window; this cannot be used with console applications.

SAORI/1.0 requests can also be sent in the same way to call a baseware built-in module. See [SAORI over DirectSSTP](../saori-ex/index.md).\[SSP 2.9.13\]
