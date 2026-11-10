# keep-alive

Since SSP 2.9.03, (Socket) SSTP also supports sending multiple requests consecutively over a single TCP connection using keep-alive, as with HTTP \[SSP 2.9.03\].<br />
This avoids the overhead of establishing a connection, making it suitable for clients that send SSTP repeatedly at short intervals.

- The connection is kept open only when the request includes a `Connection: keep-alive` header (the same explicit opt-in method as HTTP/1.0). Without this header, the connection is closed after the response as before, and the response content remains unchanged.
- This applies only to SSTP/1.x. For other versions, the Connection header is ignored and the connection is always closed.
- Direct SSTP is not covered because it has no concept of a connection. SSTP over HTTP follows the HTTP keep-alive rules (see [SSTP over HTTP](http.md)).
- If the request has a Connection header, the response always includes a Connection header as well.<br />
  If `Connection: keep-alive` and `Keep-Alive: timeout=seconds` are returned, the connection is kept open.<br />
  If `Connection: close` is returned, the connection is closed after the response (for example, when the maximum number of simultaneously maintained connections has been reached).
- Responses that keep the connection open always include Charset and Content-Length headers if there is additional data, and no blank line is appended after the additional data. If there is no additional data, the response ends with the blank line immediately after the headers.<br />
  Also, the zero terminator (0x00) that was appended to the end of responses when the connection was closed is not sent. Determine the end of the response using only the blank line and Content-Length.
- Send the next request only after receiving the entire previous response (pipelining is not supported). If you send the next request before the response, the connection may be closed with that response.
- Do not append extra bytes such as a zero terminator to the end of a request. They will be treated as part of the next request.
- If there is no next request within the number of seconds specified by the Keep-Alive timeout after the response (5 seconds in SSP 2.9.03), SSP will close the connection. Ensure that the client can reconnect and resend the request if the connection is closed at any time.

## request sample

```
EXECUTE SSTP/1.4
Charset: UTF-8
Sender: SSTPクライアント
Command: GetVersion
Connection: keep-alive
```

## response sample (connection kept open, with data)

```
SSTP/1.4 200 OK
Charset: UTF-8
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 24

追加データはここ
```

## response sample (connection closed, no data)

```
SSTP/1.4 204 No Content
Charset: UTF-8
Connection: close
```
