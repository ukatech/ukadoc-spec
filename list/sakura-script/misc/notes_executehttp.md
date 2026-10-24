# http/rss/ical/websocket オプション

- **--accept=Acceptリクエストヘッダの中身 \[2.7.34\]**: 受け取れるContent-Type形式を指定するAcceptヘッダを指定する。
- **--accept-language=Accept-Languageリクエストヘッダの中身 \[2.7.34\]**: 国際化関連の挙動を制御するためのAccept-Languageヘッダを指定する。
- **--async=識別ID**: 処理を待たずにSakuraScriptの続きを実行し、処理が完了してからイベントを通知する。<br />
  HTTPの場合は[OnExecuteHTTPComplete](../../shiori-event/other-communication/OnExecuteHTTPComplete.md)または[OnExecuteHTTPFailure](../../shiori-event/other-communication/OnExecuteHTTPFailure.md)。<br />
  RSSの場合は[OnExecuteRSSComplete](../../shiori-event/other-communication/OnExecuteRSSComplete.md)か[OnExecuteRSSFailure](../../shiori-event/other-communication/OnExecuteRSSFailure.md)。<br />
  iCalの場合は[OnExecuteICalComplete](../../shiori-event/other-communication/OnExecuteICalComplete.md)か[OnExecuteICalFailure](../../shiori-event/other-communication/OnExecuteICalFailure.md)。 \[2.8.90\]<br />
  WebSocketの場合は接続・受信・切断の各タイミングで[OnExecuteWebSocketOpen](../../shiori-event/other-communication/OnExecuteWebSocketOpen.md)/[Receive](../../shiori-event/other-communication/OnExecuteWebSocketReceive.md)/[Reconnect](../../shiori-event/other-communication/OnExecuteWebSocketReconnect.md)/[Close](../../shiori-event/other-communication/OnExecuteWebSocketClose.md)/[Failure](../../shiori-event/other-communication/OnExecuteWebSocketFailure.md)が発生する（常にAsync動作のため--syncは適用不可）。<br />
  Onから始まらないIDを指定した場合は、上記イベント名通りのイベントが発生する。<br />
  Onから始まるIDを指定した場合、HTTP/RSS/iCalは\[指定したID\]（成功）/\[指定したID\]Failure（失敗）が発生する。WebSocketは\[指定したID\]Open/\[指定したID\]（受信）/\[指定したID\]Reconnect/\[指定したID\]Close/\[指定したID\]Failureが発生する。<br />
  例:--async=OnExampleのとき HTTP/RSS/iCal→OnExample/OnExampleFailure、WebSocket→OnExampleOpen/OnExample/OnExampleReconnect/OnExampleClose/OnExampleFailure<br />
  ただし、SSLInfo系イベント([OnExecuteHTTPSSLInfo](../../shiori-event/other-communication/OnExecuteHTTPSSLInfo.md)/[OnExecuteRSS_SSLInfo](../../shiori-event/other-communication/OnExecuteRSS_SSLInfo.md)/[OnExecuteICal_SSLInfo](../../shiori-event/other-communication/OnExecuteICal_SSLInfo.md)/[OnExecuteWebSocket_SSLInfo](../../shiori-event/other-communication/OnExecuteWebSocket_SSLInfo.md))はこの対象外で、Onから始まるIDを指定しても常に上記のイベント名で通知される。<br />
  SakuraScriptの処理を一旦中断したい場合は、代わりに--syncと書く（WebSocketには適用不可）。
- **--authorization=Authorizationリクエストヘッダの中身 \[2.6.37\]**: OAuthなどAuthorizationヘッダが必須の場合にあらかじめ設定する。
- **--cookie=クッキーデータ**: Cookieのデータ、必要に応じてOnExecuteHTTPCompleteのReference5の値をそのまま指定する。
- **--content-type=(multipart/form-data | application/x-www-form-urlencoded | そのほか任意指定)**: http-post限定。param指定のパラメータをどのような形式で送るか指定する。<br />
  何も指定しなければapplication/x-www-form-urlencoded。<br />
  指定形式によってはparamの書き方に制約があるので注意。<br />
  \[2.6.37\] より、Content-Typeリクエストヘッダに直接この情報を反映するようになった。
- **--expand または --expand=日数 \[2.8.90\]**: ical-get/ical-post限定。[※iCal絞り込みオプション](notes_executeical.md)を参照。<br />
  RRULEによる繰り返しを展開し、「発生」1回ごとに1件返す。日数を書いた場合は--to省略時の期間長（既定30日）になる。
- **--file=ファイル名**: 取得するデータの保存名を指定。\[実行したゴーストのフォルダ\]/ghost/master/var/ファイル名に保存される。
- **--from=yyyymmdd \[2.8.90\]**: ical-get/ical-post・rss-get/rss-post \[2.8.92\] 限定。[※iCal絞り込みオプション](notes_executeical.md)・[※RSS絞り込みオプション](notes_executerss.md)を参照。<br />
  返すイベントの期間の開始日。省略時は当日。<br />
  \[2.8.92\] rss-get/rss-postでは返す項目の更新日時の下限（その日の0時から）。省略時は下限なし。
- **--header=SomeHeader: リクエストヘッダの中身 \[2.6.40\]**: 任意の名前のリクエストヘッダを設定する。名前と中身を区切るコロンは必須。<br />
  SSPが用意したヘッダ情報を上書きするため、指定に矛盾がないよう利用時に注意すること。
- **--insecure \[2.7.34\]**: TLS証明書の検証をスキップする。
- **--limit=件数 \[2.8.90\]**: ical-get/ical-post・rss-get/rss-post \[2.8.92\] 限定。[※iCal絞り込みオプション](notes_executeical.md)・[※RSS絞り込みオプション](notes_executerss.md)を参照。<br />
  返すイベントの最大件数。省略時は200件、0を指定すると無制限。<br />
  --limitだけを書いた場合は、開始日を当日とする期間モードになる。--from・--to・--expand・--limitをどれも書かなかった場合は件数の上限も無い（全件返す）。<br />
  \[2.8.92\] rss-get/rss-postでは、書いた場合だけ新しい順にその件数で打ち切る。省略時・0は無制限で、--limitだけを書いても期間は絞り込まれない。
- **--log=ファイル名**: サーバとの通信内容をすべてログに記録する。主に開発時のデバッグ用。
- **--nodescript**: オンライン表示とダウンロード状況を表示しない。
- **--nofile=パラメータ(文字コード) \[2.5.77\]**: 一時ファイルを作成せずメモリ上に取得したデータを展開し、イベントのReference3に格納する。<br />
  パラメータ指定は取得したデータを解釈すべき文字コード。指定しない場合はUTF-8とみなす。<br />
  Referenceには改行を含められないので、改行コードはバイト値1に変換される。<br />
  取得可能なサイズは128KBまで。<br />
  \[2.8.90\] rss-get/rss-post・ical-get/ical-postでは解析用のファイルが必要なため、この指定は無視される。
- **--no-cache \[2.7.34\]**: Cache-Control: no-cacheを指定し、キャッシュ利用を抑制する。
- **--param=パラメータ**: get/post/putのパラメータを指定する。複数回の指定が可能。<br />
  multipart/form-dataの時：<br />
  　--param=フィールド名=データ の形式を必要な数だけ繰り返す。<br />
  　例： --param=message_body=データ<br />
  application/x-www-form-urlencodedの時：<br />
  　--param=フィールド名=データ の形式を必要な数だけ繰り返した時は、すべて&でつないでサーバに送る。<br />
  　それ以外の時はすべてを改行文字(CRLF)でつないでサーバに送る(過去互換処理)。<br />
  他のcontent-type指定の時：<br />
  　複数定義するとすべてを改行文字(CRLF)でつないでサーバに送る。
- **--param-charset=文字コード**: 文字コードを指定。Shift_JIS、EUC-JP、UTF-8など、デフォルトではUTF-8。
- **--param-input-file=ファイル名 \[2.6.40\]**: --paramオプションで指定し切れない大容量データを送信したい場合に、送信データの格納されたファイルを指定する。<br />
  指定したのが絶対パス指定でない場合、\[実行したゴーストのフォルダ\]/ghost/master/ からの相対指定として解釈される。<br />
  --paramを同時には指定しないこと。<br />
  中身は基本的に関知しないので、文字コードやエンコード等は使う側で責任を持って処理すること。<br />
  ただし、multipart/form-dataの時のみ、1行目を読み取ってフィールド間区切りとして解釈する。<br />
  指定するファイルパスはSSP管轄下(SSP.exeと同じ場所以下か、ゴースト等を列挙するよう指定したフォルダ以下)に限られる。
- **--progress-notify \[2.6.44\]**: ダウンロード処理中に[OnExecuteHTTPProgress](../../shiori-event/other-communication/OnExecuteHTTPProgress.md)イベント(ical-get/ical-postの場合は[OnExecuteICalProgress](../../shiori-event/other-communication/OnExecuteICalProgress.md) \[2.8.90\])、またはイベントIDがOnではじまる場合は後ろにProgressをつけたイベントを通知する。<br />
  Onから始まるIDを指定した場合、上記の代わりにSHIORI Event \[指定したID\]Progress が発生する。<br />
  例:--async=OnExampleのとき OnExampleProgress<br />
  ダウンロード処理中に、逐一イベント通知処理が行われるため、ダウンロード速度の低下が発生する。<br />
  また、ファイルに出力する場合は、イベント通知時に一旦ファイルを閉じ、レスポンスを受けた後で再度ファイルを開く操作が加わるので、さらにダウンロード速度が遅くなる点に注意。
- **--streaming または --streaming=種類 \[2.8.14\]**: HTTPリクエストのストリーミング処理を指定する。 --streaming=sse でServer-Sent Events、 --streaming=text で改行区切りストリーミング(NDJSONなど)<br />
  種類指定なしで--streamingとした場合は、サーバからのレスポンスのContent-Typeに応じて適切にストリーミング処理を行う。<br />
  受信したデータは[OnExecuteHTTPStreaming](../../shiori-event/other-communication/OnExecuteHTTPStreaming.md)イベント、またはイベントIDがOnではじまる場合はOnHogehogeStreamingのように後ろにStreamingをつけたイベントを通知する。
- **--sync=識別ID \[2.6.44\]**: SakuraScriptの実行を一旦止めて処理待ちする点を除き、--async指定と同じ挙動となる。
- **--timeout=秒数**: レスポンスを待つ時間(※ダウンロードに要する時間ではない)を指定する。最大300秒。<br />
  指定秒数までにレスポンスがなかった場合、SHIORIイベント「OnExecuteHTTPFailure」が通知され、Reference4に「timeout」が入っている。
- **--to=yyyymmdd \[2.8.90\]**: ical-get/ical-post・rss-get/rss-post \[2.8.92\] 限定。[※iCal絞り込みオプション](notes_executeical.md)・[※RSS絞り込みオプション](notes_executerss.md)を参照。<br />
  返すイベントの期間の終了日（この日を含む）。<br />
  \[2.8.92\] rss-get/rss-postでは返す項目の更新日時の上限（その日の終わりまで）。省略時は上限なし。
- **--m_websocketProtocol=Sec-Websocket-Protocol \[2.8.08\]**: WebSocket接続の際に使用する、Sec-Websocket-Protocolヘッダを指定する。指定しなければこのヘッダ自体が送られれない。
