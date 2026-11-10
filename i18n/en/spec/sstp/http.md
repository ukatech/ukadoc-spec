# SSTP over HTTP

SSTP over HTTP, implemented in SSP 2.6.32, is a very simple mechanism: an SSTP request is placed directly in the HTTP request message body, and the SSTP response is returned directly in the HTTP response body.<br />
It is intended to make SSTP communication easier when building applications with JavaScript, such as Electron.<br />
Send an HTTP/1.1 POST request with Content-Type: text/plain to localhost:9801 (or a separately specified SSTP port), at /api/sstp/v1.<br />
The response is returned as-is with HTTP/1.1 200 OK and Content-Type: text/plain.<br />
Note that HTTP returns 200 OK even if SSTP encounters an error.<br />
The Content-Length header is required; if it is missing, an error occurs.<br />
HTTP keep-alive is supported. In HTTP/1.1, the connection is maintained by default and closed with Connection: close (for HTTP/1.0, it is maintained only when Connection: keep-alive is specified explicitly). Connections are not maintained for requests with Transfer-Encoding (such as chunked). In this case, connection persistence is determined only by the HTTP settings, and the SSTP Connection header in the message body is ignored \[SSP 2.9.03\].

[Try it](http://localhost:9801/api/sstp/v1)

[Existing js libraries](https://github.com/ukatech/jsstp-lib/blob/master/docs/README_JP.md) can be used to communicate via SSTP over HTTP in js.

Note: If the Origin header does not point to localhost, the request is forcibly treated as an SSTP request from a remote address. This imposes strong restrictions on Sakura Script tags and executable SSTP methods, and the SecurityLevel header is also ignored.<br />
These restrictions are relaxed only when the HTTP Origin is localhost and the SSTP SecurityLevel is local.
