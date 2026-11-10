# keep-alive

从 SSP 2.9.03 开始，(Socket) SSTP 也可以像 HTTP 一样使用 keep-alive，在一个 TCP 连接上连续发送多个请求 \[SSP 2.9.03\]。<br />
这样可以省去建立连接的开销，适合短时间内多次发送 SSTP 的客户端。

- 只有在 request 中添加 `Connection: keep-alive` 头时，连接才会保持（与 HTTP/1.0 相同，必须显式指定）。若未添加，则仍会在响应后断开连接，响应内容也与以往相同。
- 仅适用于 SSTP/1.x。对于其他版本，Connection 头会被忽略，连接始终会断开。
- Direct SSTP 没有连接的概念，因此不适用。SSTP over HTTP 遵循 HTTP 的 keep-alive 规则（参见 [SSTP over HTTP](http.md)）。
- 如果 request 中包含 Connection 头，response 中也一定会包含 Connection 头。<br />
  若返回 `Connection: keep-alive` 和 `Keep-Alive: timeout=秒数`，则连接会保持。<br />
  若返回 `Connection: close`，则响应后会断开连接（例如，同时保持的连接数已达到上限）。
- 对于连接保持期间的响应，如果有附加数据，则一定会包含 Charset 和 Content-Length 头，附加数据后面不会跟空行。如果没有附加数据，则以头之后的空行结束。<br />
  此外，不会发送以往断开连接的响应末尾所带的零终止符（0x00）。请仅根据空行和 Content-Length 判断响应结束。
- 请在接收完前一个 response 后再发送下一个 request（不支持流水线）。如果在收到 response 之前发送下一个 request，连接可能会在该响应后断开。
- 请勿在 request 末尾添加零终止符等多余字节。这些字节会被视为下一个 request 的一部分。
- response 之后，如果在 Keep-Alive 的 timeout 指定的秒数内（SSP 2.9.03 中为 5 秒）没有收到下一个 request，SSP 会主动断开连接。客户端应确保无论何时连接断开，都能重新连接并重新发送请求。

## request 示例

```
EXECUTE SSTP/1.4
Charset: UTF-8
Sender: SSTPクライアント
Command: GetVersion
Connection: keep-alive
```

## response 示例（保持连接，有数据）

```
SSTP/1.4 200 OK
Charset: UTF-8
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 24

追加データはここ
```

## response 示例（断开连接，无数据）

```
SSTP/1.4 204 No Content
Charset: UTF-8
Connection: close
```
