# response

## サンプル

```
SHIORI/3.0 200 OK
Charset: UTF-8
Sender: AYA
Value: \1\s[10]\0\s[0]\e
```

※改行コードはCR+LF。<br />
※最後は空行（前行の終端と合わせて(CR+LF)x2）で終わること。

- **ステータスコード**: HTTPと同じく、200番台が成功、ほかはなにかしらの失敗（エラー）を示す。<br />
  現在主に使用されているのは下記の通り。

  - **200**: 200 OK<br />
    成功、返り値(Value)あり。
  - **204**: 204 No Content<br />
    成功、返り値なし。
  - **311**: 311 Not Enough<br />
    ID: OnTeach (SHIORI/2系のTEACHメソッド)において、さらなる追加情報を必要とすることを示す。<br />
    入力ボックスを再度開いてユーザーに問い合わせ、入力完了後に入力文字列を含むReferenceを追加する。
  - **312**: 312 Advice<br />
    ID: OnTeach (SHIORI/2系のTEACHメソッド)において、直近で入力された文字列が解釈不能のため破棄すべきことを示す。<br />
    一番最後のReferenceを破棄し、入力ボックスを再度開いてユーザーに問い合わせ、入力完了後に入力文字列を含むReferenceを追加する。
  - **400**: 400 Bad Request<br />
    リクエスト文字列が解釈不能だった。
  - **500**: 500 Internal Server Error<br />
    SHIORI内部でなにかしらのエラーが起き、レスポンスを返せなかった。

- **Charset**: 文字コード。最初の行、または少なくとも文字コードがASCII範囲以外の行の前が望ましい。

- **Sender**: 送り主。通常はSHIORIの名前。

- **Value**: 喋りたいスクリプト。

- **ValueNotify \[SSP拡張 2.5.35\]**: *\[実験的機能\]*<br />
  リクエストメソッドがNOTIFYの場合でもSakuraScriptを実行するための拡張機能。<br />
  このヘッダでSakuraScriptを返すと、即時実行される。GETの場合はValueヘッダのスクリプトを実行する前に実行される。<br />
  実行できるタグは極めて限られ、他のタグやその他文字列は全て無視される。<br />
  <del>メソッドがNOTIFYでない時や、Valueヘッダがすでにある時は無視される。</del> 2.6.76で制限廃止<br />
  現在実行できるタグは以下の通り：

  - `\![sound]`
  - `\![set,trayicon]`
  - `\![set,trayballoon]`
  - `\![raise]`
  - `\![raiseother]`
  - `\![raiseplugin]`
  - `\![timerraiseother]`
  - `\![timerraiseplugin]`
  - `\![notify]`
  - `\![notifyother]`
  - `\![notifyplugin]`
  - `\![get,property]` ＋2.6.82
  - `\![set,property]` ＋2.6.82

- **SecurityLevel \[SSP拡張\]**: 下記のいずれか。

  - **local**: 実行中の端末内からのスクリプト相当のセキュリティレベル。
  - **external**: 実行中の端末の外部からのスクリプト相当のセキュリティレベル。

  喋りたいスクリプトのSecurityLevel。externalだと一部のスクリプトがセキュリティ機能により実行不能になる。

- **Marker \[SSP拡張\]**: バルーンマーカー(バルーン下側の追加情報)に表示したい文字列。

- **ErrorLevel \[SSP拡張\]**: SHIORI内部で起きたエラーのレベル。下記のいずれか。複数のエラーを表現したい時はバイト値1で区切る。

  - **info**: 情報。エラーではない。
  - **notice**: 通知。エラーとは言い難いものの修正すべき記述など。
  - **warning**: 警告。記述ミスなどがあり、処理は停止していないが対処したほうがいいもの。
  - **error**: 通常のエラー。記述ミスなどで何か処理が停止して再開できない。
  - **critical**: 致命的エラー。errorより酷く、すぐに何かしら対処をしたほうが良いもの。

  このヘッダがある場合は、ユーザーになにかしらのエラーが起きたことが通知される。<br />
  通知されるレベルはユーザーが設定変更可能。通常はerror以上。<br />
  SSPの場合はエラーログに記録され、エラーアイコンが通知領域に出る。

- **ErrorDescription \[SSP拡張\]**: SHIORI内部で起きたエラーの詳細情報。ErrorLevelがある場合のみ有効。<br />
  複数のエラーを表現したい時はバイト値1で区切る。<br />
  ErrorLevelとErrorDescriptionの要素数は必ず同じでないといけない。

- **BalloonOffset \[SSP拡張\]**: バルーンのオフセット値(X,Y)。

- **Reference0**: コミュニケートを送りたい場合、ゴーストの`\0`側の名前。

- **Reference1～**: コミュニケートの追加情報。<br />
  レスポンスのReference1＝SSTP CommunicateのReference0＝受け手のOnCommunicateのReference2<br />
  互換性の問題で以上のようにずれてしまうことに注意。

- **Age \[SSP拡張\]**: コミュニケートの世代数。初回はゼロ。やりとりを重ねるたびに+1。<br />
  SSP拡張だが、実質はSHIORI/2.x互換処理。

- **MarkerSend \[SSP拡張\]**: コミュニケート中に「相手側に」表示したいバルーンマーカー文字列。<br />
  SSTPのMarkerヘッダとして送信される。

- **X-SSTP-PassThru-(任意の文字列) \[SSP 2.5.03～拡張\]**: SSTPからイベント通知が来た場合のレスポンスに限り、このヘッダがSSTPのレスポンスにそのまま追加される。<br />
  SSTP以外の時は無視される。<br />
  複数のヘッダを指定可能だが、複数返したい場合はヘッダ名を変えること。<br />
  （旧ヘッダ名：X-SSTP-Return- は廃止予定）
