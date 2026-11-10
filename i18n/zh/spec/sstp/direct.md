# Direct SSTP

Direct SSTP是一种利用高度依赖操作系统的IPC机制进行通信的规范。协议规范与(Socket) SSTP相同，但其目的是不使用处理开销相对较大的TCP/IP，而是直接指定ghost进行轻量级通信。<br />
目前仅针对Windows制定了规范，具体如下。

通过SendMessage系列函数发送[WM_COPYDATA](https://docs.microsoft.com/en-us/windows/win32/dataxchg/wm-copydata)（不可使用Post）<br />
SendMessage的hWnd = 通信目标ghost的HWND [从FMO获取](../fmo-mutex/index.md)<br />
wParam = 用于回复的“自身”HWND。响应通过指定WM_COPYDATA的HWND（窗口）接收。<br />
lParam = 指向[COPYDATASTRUCT](https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-copydatastruct)的指针<br />
copydatastruct.lpData = 遵循SSTP协议的字符串<br />
copydatastruct.cbData = 字符串长度<br />
copydatastruct.dwData = 9801<br />
备注：<br />
为确保安全，发送方应在lpData中准备以零结尾的字符串，并建议在cbData中包含零终止符。<br />
为确保安全，接收方不应假定字符串以零结尾，必须考虑cbData进行处理。<br />
接收方应将指定为通信目标的HWND，视为等同于SSTP协议中指定的应接收请求的ghost，并尽可能优先选择该ghost。<br />
接收方和发送方均假定为至少拥有一个窗口的GUI应用程序，无法用于控制台应用程序。

也可以通过相同方式发送SAORI/1.0请求，调用baseware的内置模块。请参阅[SAORI over DirectSSTP](../saori-ex/index.md)。\[SSP 2.9.13\]
