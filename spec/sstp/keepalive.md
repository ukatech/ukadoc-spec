# keep-alive

SSP 2.9.03以降、(Socket) SSTPでもHTTPと同様のkeep-aliveにより、1本のTCP接続で複数のリクエストを続けて送ることができます \[SSP 2.9.03\]。<br />
接続確立の手間を省けるので、短い間隔で何度もSSTPを送るクライアントに向いています。

- requestに `Connection: keep-alive` ヘッダを付けたときだけ接続が維持されます(HTTP/1.0と同じ明示指定方式)。付けなければ従来どおり応答後に切断され、応答の内容も従来と変わりません。
- SSTP/1.xのみが対象です。それ以外のバージョンではConnectionヘッダは無視され、常に切断されます。
- Direct SSTPは接続の概念が無いため対象外です。SSTP over HTTPはHTTP側のkeep-aliveの規則に従います([SSTP over HTTP](http.md)参照)。
- requestにConnectionヘッダがあった場合、responseにも必ずConnectionヘッダが付きます。<br />
  `Connection: keep-alive` と `Keep-Alive: timeout=秒数` が返れば接続は維持されています。<br />
  `Connection: close` が返った場合は応答後に切断されます(同時に維持できる接続数の上限に達した場合など)。
- 接続が維持される応答では、追加データがあれば必ずCharsetとContent-Lengthヘッダが付き、追加データの後ろに空行は付きません。追加データが無ければヘッダ直後の空行で終わります。<br />
  また、切断される従来の応答の末尾に付いていたゼロ終端(0x00)は送られません。応答の終わりは空行とContent-Lengthだけで判断してください。
- 次のrequestは、前のresponseを受け取り終えてから送ってください(パイプライン非対応)。responseより先に次のrequestを送った場合、その応答で切断されることがあります。
- requestの末尾にゼロ終端などの余分なバイトを付けないでください。次のrequestの一部とみなされます。
- responseの後、Keep-Aliveのtimeoutで示された秒数(SSP 2.9.03では5秒)の間に次のrequestが無ければ、SSP側から切断されます。クライアントはいつ切断されても再接続して送り直せるようにしてください。

## requestサンプル

```
EXECUTE SSTP/1.4
Charset: UTF-8
Sender: SSTPクライアント
Command: GetVersion
Connection: keep-alive
```

## responseサンプル(接続維持・データあり)

```
SSTP/1.4 200 OK
Charset: UTF-8
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 24

追加データはここ
```

## responseサンプル(切断・データなし)

```
SSTP/1.4 204 No Content
Charset: UTF-8
Connection: close
```
