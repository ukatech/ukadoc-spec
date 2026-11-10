# SSTP over HTTP

SSTP over HTTP 是在 SSP 2.6.32 中實作的極簡機制：將 SSTP 要求直接放入 HTTP 要求訊息本文，並將 SSTP 回應原樣放入 HTTP 回應本文傳回。<br />
預期用於使用 Electron 等技術，以 JavaScript 開發應用程式時，更簡單地傳送與接收 SSTP 通訊。<br />
請以 HTTP/1.1 對 localhost:9801（或另行指定的 SSTP 通訊埠）上的 /api/sstp/v1，使用 Content-Type: text/plain 傳送 POST 要求。<br />
回應也會原樣以 HTTP/1.1 200 OK、Content-Type: text/plain 傳回。<br />
請注意，即使 SSTP 發生錯誤，HTTP 狀態仍為 200 OK。<br />
另外，Content-Length 標頭為必填，缺少時會發生錯誤。<br />
支援 HTTP keep-alive。HTTP/1.1 預設會維持連線，使用 Connection: close 時則會中斷連線（HTTP/1.0 僅在明確指定 Connection: keep-alive 時維持連線）。帶有 Transfer-Encoding（例如 chunked）的要求不會維持連線。此時，連線是否維持僅由 HTTP 端的指定決定，會忽略訊息本文中的 SSTP Connection 標頭 \[SSP 2.9.03\]。

[試用](http://localhost:9801/api/sstp/v1)

[現有的 js 程式庫](https://github.com/ukatech/jsstp-lib/blob/master/docs/README_JP.md)可用於透過 js 傳送 SSTP over HTTP。

注意：若 Origin 標頭未指向 localhost，要求會一律視為來自遠端位址的 SSTP 要求，Sakura Script 標籤與可執行的 SSTP 方法都會受到嚴格限制，且 SecurityLevel 標頭也會被忽略。<br />
只有在 HTTP Origin 為 localhost，且 SSTP SecurityLevel 為 local 時，才會放寬這些限制。
