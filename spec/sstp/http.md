# SSTP over HTTP

SSTP over HTTPは、SSP 2.6.32で実装された、HTTPリクエストメッセージボディにSSTPリクエストをそのまま突っ込み、HTTPレスポンスボディにSSTPレスポンスがそのまま返ってくるきわめて単純な仕組みです。<br />
ElectronなどJavaScriptを使ってアプリを作った時に、より簡単にSSTP通信をやりとりするために使うのを想定しています。<br />
localhost:9801(または別途指定されたSSTPポート) に対して、 /api/sstp/v1 に Content-Type: text/plainでHTTP/1.1でPOSTしてください。<br />
レスポンスもそのまま、HTTP/1.1 200 OKのContent-Type: text/plainで返ってきます。<br />
SSTPがエラーでもHTTPは200 OKな点に注意してください。<br />
なお、Content-Lengthヘッダは必須で、無ければエラーになります。<br />
HTTPのkeep-aliveに対応しています。HTTP/1.1では既定で接続が維持され、Connection: close で切断されます(HTTP/1.0は Connection: keep-alive の明示時のみ維持)。Transfer-Encoding(chunked等)付きのリクエストでは維持されません。このとき接続の維持はHTTP側の指定だけで決まり、メッセージボディ中のSSTPのConnectionヘッダは無視されます \[SSP 2.9.03\]。

[お試し](http://localhost:9801/api/sstp/v1)

[既存のjsライブラリ](https://github.com/ukatech/jsstp-lib/blob/master/docs/README_JP.md)は、jsでSSTP over HTTPを行うために使用できます。

注意：Originヘッダがlocalhostを指していない場合は、強制的にリモートアドレスからのSSTPリクエストとして扱われ、SakuraScriptタグや実行できるSSTPメソッドに強い制約がかかり、かつSecurityLevelヘッダも無視されます。<br />
この制約は、HTTPのOriginがlocalhost、かつSSTPのSecurityLevelがlocalの場合のみ緩和されます。
