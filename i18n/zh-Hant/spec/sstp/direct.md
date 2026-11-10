# Direct SSTP

Direct SSTP 是利用高度依賴 OS 的 IPC 機制進行通訊的規格。通訊協定規格與 (Socket) SSTP 相同，但不使用處理負擔相對較重的 TCP/IP，而是以直接指定 ghost 進行輕量通訊為目的。<br />
目前僅在 Windows 上定義規格，詳如下所述。

使用 SendMessage 系列函式傳送 [WM_COPYDATA](https://docs.microsoft.com/en-us/windows/win32/dataxchg/wm-copydata)（不可使用 Post）<br />
SendMessage 的 hWnd = 通訊對象 ghost 的 HWND [從 FMO 取得](../fmo-mutex/index.md)<br />
wParam = 回覆對象的「自身」HWND。回應會由指定 WM_COPYDATA 的 HWND（視窗）接收。<br />
lParam = 指向 [COPYDATASTRUCT](https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-copydatastruct) 的指標<br />
copydatastruct.lpData = 符合 SSTP 通訊協定的字串<br />
copydatastruct.cbData = 字串長度<br />
copydatastruct.dwData = 9801<br />
備註：<br />
為確保安全，傳送端應在 lpData 中準備以零結尾的字串，並建議 cbData 包含零結尾字元。<br />
為確保安全，接收端不得預期字串以零結尾，並務必考量 cbData 進行處理。<br />
接收端應將指定為通訊對象的 HWND，視為與 SSTP 通訊協定內指定的接收 ghost 相同，並盡可能優先選擇該 ghost。<br />
本規格假設接收端與傳送端都是至少有一個視窗的 GUI 應用程式，無法用於主控台應用程式。

也可以用相同方式傳送 SAORI/1.0 要求，呼叫 baseware 的內建模組。請參閱 [SAORI over DirectSSTP](../saori-ex/index.md)。\[SSP 2.9.13\]
