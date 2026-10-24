# Direct SSTP

Direct SSTPはOSに強く依存したIPCの仕組みを利用した通信仕様です。プロトコル仕様は(Socket) SSTPと同じですが、比較的処理が重いTCP/IPを使用せず、直接ゴーストを指定して軽量な通信を行うことを目的としています。<br />
現在のところWindows上のみ仕様が決まっており、下記の通りとなります。

[WM_COPYDATA](https://docs.microsoft.com/en-us/windows/win32/dataxchg/wm-copydata)をSendMessage系関数で送信(Postは不可)<br />
SendMessageのhWnd = 通信先ゴーストのHWND [FMOから取得](../fmo-mutex/index.md)<br />
wParam = 返信先の「自身の」HWND レスポンスはWM_COPYDATAを指定したHWND（ウインドウ）で受ける。<br />
lParam = [COPYDATASTRUCT](https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-copydatastruct)へのポインタ<br />
copydatastruct.lpData = SSTPプロトコルに従った文字列<br />
copydatastruct.cbData = 文字列の長さ<br />
copydatastruct.dwData = 9801<br />
備考：<br />
送信側は安全のためlpDataにゼロ終端の文字列を用意し、cbDataにはゼロ終端を含むことが望ましい。<br />
受信側は安全のためゼロ終端を期待せず、必ずcbDataを考慮して処理を行うこと。<br />
受信側は通信先として指定されたHWNDを、受信すべきゴーストがSSTPプロトコル内で指定されたものと同等として取り扱い、できる限りそのゴーストを優先する。<br />
受信側・送信側共にウインドウを1つ以上持つGUIアプリのみを想定しており、コンソールアプリでは使用できない。

同じ方法でSAORI/1.0の要求を送り、ベースウェアの内蔵モジュールを呼び出すこともできます。[SAORI over DirectSSTP](../saori-ex/index.md)を参照してください。\[SSP 2.9.13\]
