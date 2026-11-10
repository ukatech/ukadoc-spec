# SSTP over HTTP

SSTP over HTTP是在SSP 2.6.32中实现的一种极其简单的机制：将SSTP请求直接放入HTTP请求消息体，并将SSTP响应原样返回到HTTP响应消息体中。<br />
预期用于使用Electron等技术，通过JavaScript创建应用程序时更轻松地进行SSTP通信。<br />
请向localhost:9801（或另行指定的SSTP端口）的/api/sstp/v1发送HTTP/1.1 POST请求，Content-Type设为text/plain。<br />
响应也会直接以HTTP/1.1 200 OK返回，Content-Type为text/plain。<br />
请注意，即使SSTP出错，HTTP也会返回200 OK。<br />
另外，Content-Length标头为必填项，缺少时会报错。<br />
支持HTTP keep-alive。在HTTP/1.1中，连接默认保持；使用Connection: close时断开（HTTP/1.0仅在明确指定Connection: keep-alive时保持连接）。带有Transfer-Encoding（如chunked）的请求不会保持连接。此时连接是否保持仅由HTTP侧的设置决定，消息体中的SSTP Connection标头会被忽略 \[SSP 2.9.03\]。

[试用](http://localhost:9801/api/sstp/v1)

[现有的js库](https://github.com/ukatech/jsstp-lib/blob/master/docs/README_JP.md)可用于通过js进行SSTP over HTTP通信。

注意：如果Origin标头未指向localhost，则会强制将其视为来自远程地址的SSTP请求，Sakura Script标签和可执行的SSTP方法将受到严格限制，并且SecurityLevel标头也会被忽略。<br />
只有当HTTP的Origin为localhost，且SSTP的SecurityLevel为local时，才会放宽这些限制。
