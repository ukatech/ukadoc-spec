# Direct SSTP

Direct SSTP is a communication specification that uses an IPC mechanism strongly dependent on the OS. The protocol specification is the same as (Socket) SSTP, but its purpose is to communicate lightly by specifying a ghost directly, without using TCP/IP, which has relatively high processing overhead.<br />
At present, the specification is defined only for Windows, as follows.

Send [WM_COPYDATA](https://docs.microsoft.com/en-us/windows/win32/dataxchg/wm-copydata) using a SendMessage-family function (Post is not allowed)<br />
SendMessage hWnd = the HWND of the destination ghost [obtained from FMO](../fmo-mutex/index.md)<br />
wParam = the HWND of “your own” reply destination. The response is received by the HWND (window) specified for WM_COPYDATA.<br />
lParam = pointer to [COPYDATASTRUCT](https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-copydatastruct)<br />
copydatastruct.lpData = a string following the SSTP protocol<br />
copydatastruct.cbData = string length<br />
copydatastruct.dwData = 9801<br />
Notes:<br />
For safety, the sender should prepare a null-terminated string in lpData and preferably include the null terminator in cbData.<br />
For safety, the receiver should not expect a null terminator and must always process the data with cbData taken into account.<br />
The receiver should treat the HWND specified as the communication destination as equivalent to the ghost specified in the SSTP protocol, and prioritize that ghost as much as possible.<br />
Both the receiver and sender are assumed to be GUI applications with at least one window; console applications cannot use this.

You can also send a SAORI/1.0 request in the same way to call a baseware's built-in module. See [SAORI over DirectSSTP](../saori-ex/index.md). \[SSP 2.9.13\]
