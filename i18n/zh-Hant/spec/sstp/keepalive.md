# keep-alive

自 SSP 2.9.03 起，(Socket) SSTP 也能像 HTTP 一樣透過 keep-alive，在單一 TCP 連線上連續傳送多個要求 \[SSP 2.9.03\]。<br />
由於可省去建立連線的步驟，因此適合短時間內多次傳送 SSTP 的用戶端。

- 只有在 request 中附加 `Connection: keep-alive` 標頭時，才會維持連線（與 HTTP/1.0 相同，必須明確指定）。若未附加，則會如以往一樣在回應後中斷連線，回應內容也與以往相同。
- 僅適用於 SSTP/1.x。其他版本會忽略 Connection 標頭，並一律中斷連線。
- Direct SSTP 沒有連線的概念，因此不適用。SSTP over HTTP 依照 HTTP 端的 keep-alive 規則處理（請參閱 [SSTP over HTTP](http.md)）。
- 若 request 中有 Connection 標頭，response 也必定會附加 Connection 標頭。<br />
  若回傳 `Connection: keep-alive` 與 `Keep-Alive: timeout=秒數`，表示連線會維持。<br />
  若回傳 `Connection: close`，則會在回應後中斷連線（例如同時維持的連線數已達上限）。
- 維持連線的回應若有附加資料，必定會帶有 Charset 與 Content-Length 標頭，且附加資料後方不會有空行。若沒有附加資料，則會以標頭後方的空行結束。<br />
  此外，不會傳送以往在中斷連線的回應末尾附加的零結尾（0x00）。請只根據空行與 Content-Length 判斷回應結尾。
- 請在接收完前一個 response 後，再傳送下一個 request（不支援管線化）。若在 response 前傳送下一個 request，連線可能會在該回應後中斷。
- 請勿在 request 末尾附加零結尾等多餘位元組，這些位元組會被視為下一個 request 的一部分。
- response 後若在 Keep-Alive 的 timeout 所指定的秒數內（SSP 2.9.03 為 5 秒）沒有下一個 request，SSP 端會中斷連線。請讓用戶端能在連線隨時中斷時重新連線並重新傳送。

## request 範例

```
EXECUTE SSTP/1.4
Charset: UTF-8
Sender: SSTPクライアント
Command: GetVersion
Connection: keep-alive
```

## response 範例（維持連線・有資料）

```
SSTP/1.4 200 OK
Charset: UTF-8
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 24

追加データはここ
```

## response 範例（中斷連線・無資料）

```
SSTP/1.4 204 No Content
Charset: UTF-8
Connection: close
```
