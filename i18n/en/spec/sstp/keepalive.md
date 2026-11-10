# keep-alive

Starting with SSP 2.9.03, (Socket) SSTP supports sending multiple requests consecutively over a single TCP connection using keep-alive, just like HTTP \[SSP 2.9.03\].<br />
This avoids the overhead of establishing a connection, making it suitable for clients that send SSTP repeatedly at short intervals.

- The connection is kept alive only when the request includes a `Connection: keep-alive` header (the same explicit opt-in as HTTP/1.0). If it is not included, the connection is closed after the response as before, and the response content is unchanged.
- This applies only to SSTP/1.x. For other versions, the Connection header is ignored and the connection is always closed.
- Direct SSTP is not covered because it has no concept of a connection. SSTP over HTTP follows the HTTP keep-alive rules (see [SSTP over HTTP](http.md)).
- If the request includes a Connection header, the response always includes a Connection header as well.<br />
  If `Connection: keep-alive` and `Keep-Alive: timeout=seconds` are returned, the connection is being kept alive.<br />
  If `Connection: close` is returned, the connection is closed after the response (for example, when the maximum number of simultaneous connections has been reached).
- Responses that keep the connection alive always include Charset and Content-Length headers if there is additional data, and no blank line follows the additional data. If there is no additional data, the response ends with the blank line immediately after the headers.<br />
  Also, the zero terminator (0x00) that was appended to the end of responses when the connection was closed as before is not sent. Determine the end of the response using only the blank line and Content-Length.
- Send the next request only after the previous response has been fully received (pipelining is not supported). If you send the next request before receiving the response, the connection may be closed after that response.
- Do not append extra bytes, such as a zero terminator, to the end of a request. They will be treated as part of the next request.
- If no next request arrives within the number of seconds specified by the Keep-Alive timeout after the response (5 seconds in SSP 2.9.03), SSP closes the connection. The client should be prepared to reconnect and resend the request if the connection is closed at any time.

## request sample

```
EXECUTE SSTP/1.4
Charset: UTF-8
Sender: SSTPクライアント
Command: GetVersion
Connection: keep-alive
```

## response sample (connection kept alive, with data)

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
