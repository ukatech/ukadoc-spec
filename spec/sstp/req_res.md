# request/response

SHIORIなど他のプロトコルと同じく、HTTPに似せた独自プロトコルです。<br />
リクエストのCharset指定は必須で、指定が無い場合はエラーとなるか、OS標準指定の文字コードとして解釈されます。

- 改行コードはCR+LF。
- リクエストの最後は空行（前行の終端と合わせて(CR+LF)x2）で終わる。
- レスポンスの最後にはEXECUTEなどの場合追加データが入ることがある。ヘッダ終了後空行を一つ挟み、追加データが入り、さらに空行が1つ入って終了となる。追加データが無い場合はヘッダ直後の空行だけで終わる場合がある。
- 追加データありのレスポンスでは、互換性の都合でCharsetを含むヘッダが一切無く追加データだけが返る場合がある。その場合はリクエストの文字コードと同じと仮定して良い。
- リクエストとレスポンスのSSTPバージョンが異なる場合がある。バージョン番号に依存する解釈はしないこと。

## request

### requestサンプル

```
SEND SSTP/1.0
Charset: UTF-8
Sender: SSTPクライアント
Script: \h\s0テストー。\u\s[10]テストやな。
Option: notranslate
```

### requestの各メソッドに共通するヘッダ

メソッド固有のものについては、後ろのメソッド別の説明を確認すること。

- **Charset**: リクエストの文字コード。一番最初の行に現れるのが望ましい。<br />
  特に理由がなければUTF-8を推奨する。
- **Sender**: 送信者を示す文字列。「SSTP送信ツール」など。COMMUNICATEメソッドの場合は、送信元のゴースト`\0`名。
- **SecurityLevel**: SHIORIやSakuraScriptで処理する際のセキュリティレベルの指定。local/externalのいずれか。<br />
  DirectSSTP、または127.0.0.1等明らかにローカルから来たリクエストのみ有効。<br />
  SSTP over HTTPは、localhostから配信されたhtml等から送られた場合を除き、常にexternalとみなされる。
- **SecurityOrigin \[SSP 2.6.59\]**: 送信元サーバを示すURL風の文字列。以下の形式となる。[HTTPヘッダのOrigin](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Origin)と考え方は同じ。<br />
  SecurityOrigin: null<br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\><br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\>:&lt;port\><br />
  scheme は通常、http,https,sstpのいずれか。hostnameは送信元サーバ名かIP。portは返信受付可能なポート。<br />
  特に指定がない場合は、nullが指定されたものとみなされる。<br />
  SSTP over HTTPは、HTTPのOriginヘッダの中身が常に設定され、SSTPの中のSecurityOriginは無視される。
- **Option**: SSTPで実行されるSakuraScriptがどのように扱われるかのオプションを指定する。<br />
  カンマ区切りで複数指定可能。指定する文字列は以下の通り。<br />
  nodescript : バルーンのSSTP表示を無効にする(リモートからのSSTPは無効)<br />
  notranslate : OnTranslateやMAKOTOでのトランスレート処理を行わない<br />
  nobreak : 現在実行中のスクリプトを中断せず、終わるまで待つ<br />
  strict : SakuraScriptの解釈に失敗した箇所をエラーログに記録する。対象は存在しないサーフェス(`\s`)・アニメーション(`\i`)・バルーン(`\b`)の指定、未知のタグ・`\![コマンド]`・`\&[実体参照]`、必要な\[\]や数字の欠け、`\p`・`\b`・`\n`・`\c`・`\q`の不正な値。SENDのスクリプトと、NOTIFY/GIVEでゴーストが返したスクリプトに有効 \[SSP 2.8.94\]
- **ID**: "Owned SSTP"と呼ばれるもの。[SHIORI uniqueid](../../list/shiori-event/notify/uniqueid.md)で送られてきたIDか、[FMOの識別ID(SSPのみ)](../fmo-mutex/index.md)を指定すると、各種セキュリティチェックやロック等を無視して、本SSTPをゴースト内部での処理と同じ優先度で扱う。<br />
  SecurityLevel指定がlocalになり、さらに`\t`などの割り込み禁止状態でも強制的に割り込み再生を可能とする。
- **X-SSTP-PassThru-(任意の文字列)**: NOTIFYなどゴースト側との通信の際に、SHIORIに直接渡されるヘッダ。<br />
  文字コード変換等最低限の処理が行われるだけで、(任意の文字列)の部分や中身はそのまま中継される。
- **HWnd**: DirectSSTP限定で、responseを返信すべきウインドウハンドルを示す。<br />
  ウインドウハンドル(ポインタ相当)のデータを符号なし10進整数として扱い、それを文字列化したもの。<br />
  省略時はWM_COMMUNICATEのwParam。
- **ReceiverGhostHWnd \[SSP 2.5.57\]**: (Socket)SSTP限定で、requestを送るべきゴーストの`\0`のウインドウハンドルを示す。<br />
  これを指定すると、処理すべきゴーストが固定され、Socket経由でもDirectSSTPと同じ処理が可能になる。<br />
  見つからなかった場合は、404 Not Foundで即時エラー終了する。
- **ReceiverGhostName \[SSP 2.5.57\]**: (Socket)SSTP限定で、requestを送るべきゴーストの`\0`名を示す。<br />
  これを指定すると、処理すべきゴーストが固定され、Socket経由でもDirectSSTPと同じ処理が可能になる。HWndの名前版。<br />
  見つからなかった場合は、404 Not Foundで即時エラー終了する。

## response

### responseサンプル(データなし)

```
SSTP/1.4 200 OK
Charset: UTF-8
Script: \h\s0テストー。\u\s[10]テストやな。
```

### responseサンプル(データあり)

```
SSTP/1.4 200 OK
Charset: UTF-8
Script: \h\s0テストー。\u\s[10]テストやな。

追加データはここ
```

### responseの各メソッドに共通するヘッダ

- **Charset**: リクエストの文字コード。一番最初の行に現れるのが望ましい。<br />
  特に理由がなければUTF-8を推奨する。<br />
  互換性の問題解消のため、わざと省略される場合がある。その場合はrequestと同じ文字コードと仮定すること。
- **X-SSTP-PassThru-(任意の文字列)**: NOTIFYなどゴースト側との通信の際に、SHIORIから直接返されてきたヘッダ。<br />
  文字コード変換等最低限の処理が行われるだけで、(任意の文字列)の部分や中身はそのまま中継される。

### responseのステータスコード

HTTPと同じく、200番台は正常受理、その他はエラー。

- **200 OK**: 正常終了（返り値つき）
- **204 No Content**: 正常終了（返り値なし）
- **210 Break**: 実行はされたがスクリプト実行中にブレークされた<br />
  ※EntryつきのSEND/1.xなど極めて限られた状況に限り、通常は即時200か204リターン。
- **400 Bad Request**: リクエストに何かしらカバーしきれない不備がある
- **404 Not Found ※SSPのみ**: ゴースト指定のSSTPで該当ゴーストがインストールや起動がされていない
- **408 Request Timeout**: タイムアウト：ゴースト/SHIORI側と通信できない時など（普段はほぼ起こらない）
- **409 Conflict**: `\t`タグなどの割り込み禁止状態か、他のリクエストの処理中
- **413 Payload Too Large ※SSPのみ**: SSTPリクエストが長すぎて処理を拒否した
- **420 Refuse**: ゴースト側の設定の都合で受信拒否された
- **500 Internal Server Error ※SSPのみ**: 処理系内部で検出されたなにかしらの問題で処理しきれなかった
- **501 Not Implemented**: 未実装のコマンドなどが含まれて処理できなかった
- **503 Service Unavailable**: 処理系内部の都合でSSTPを受け付けられない状態
- **505 Version Not Supported ※SSPのみ**: SSTPのバージョンがおかしい（1.0未満、3.0以上など）
- **512 Invisible**: 最小化などでゴーストが表示されておらず、何も処理できない状態
