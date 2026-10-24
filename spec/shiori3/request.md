# request

## サンプル

```
GET SHIORI/3.0
Charset: UTF-8
Sender: SSP
SenderType: internal,raise
SecurityLevel: local
Status: choosing,balloon(0=0)
ID: OnFirstBoot
BaseID: OnBoot
Reference0: 1
```

※改行コードはCR+LF。<br />
※最後は空行（前行の終端と合わせて(CR+LF)x2）で終わること。

- **メソッド**:

  - **GET**: レスポンスのValueヘッダでなにかしらを返すことを前提としているメソッド。
  - **NOTIFY**: 何も値を返さないことを前提としているメソッド。レスポンスのValueヘッダは無視される。<br />
    主に何かしらのモードの制約で「喋れない」状態の時や、起動直後の状態通知イベントに使用される。<br />
    同じID(イベント名)でGET/NOTIFYの両方とも使われる場合があるので注意。

- **Charset**: 文字コード。最初の行、または少なくとも文字コードがASCII範囲以外の行の前が望ましい。

- **Sender**: イベント送信元。

- **SenderType \[SSP 2.5.05～拡張\]**: イベント送信元の属性。下記の通り。複数ある場合はカンマでつなげたもの。<br />
  ID: OnTranslateについては、トランスレート元のイベントの属性を引き継ぐ。

  - **internal**: アプリケーション内部からのイベント。
  - **external**: アプリケーション外部からのイベント。
  - **sakuraapi**: Sakura APIによって起こされたイベント。
  - **embed**: `\![embed]`タグによって起こされたイベント。
  - **raise**: `\![raise]`タグによって起こされたイベント。
  - **property**: プロパティシステムの参照命令の結果起こされたイベント。
  - **plugin**: プラグインによって起こされたイベント。
  - **sstp**: SSTPによって起こされたイベント。
  - **communicate**: コミュニケート仕様によって起こされたイベント。

- **SecurityLevel**: スクリプト実行時のセキュリティレベル。下記のいずれか。<br />
  ID: OnTranslateについては、トランスレート元のイベントの属性を引き継ぐ。<br />
  できるだけ最初のほうの行で通知される。少なくともIDヘッダより前に現れる。

  - **local**: 実行中の端末内からの通知。
  - **external**: 実行中端末の外部からの通知。

  externalの場合は実行中マシンの外部からの通知なので、セキュリティ的に取り扱いに注意を要する。<br />
  SenderTypeのinternal/externalとは別の概念であり、アプリケーション外から発生したイベントであっても、安全とみなして良いものはlocal判定となるので、SenderTypeがexternalでもSecurityLevelがlocalとなる場合がある。

- **SecurityOrigin \[SSP拡張\]**: 送信元サーバを示すURL風の文字列。以下の形式となる。[HTTPヘッダのOrigin](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Origin)と考え方は同じ。<br />
  SecurityOrigin: null<br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\><br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\>:&lt;port\><br />
  scheme は通常、http,https,sstpのいずれか。hostnameは送信元サーバ名かIP。portは返信受付可能なポート。<br />
  SSTPなどでヘッダが指定されていない、そもそも送信元の概念がないなど、情報なしの場合はnullとなる。<br />
  SSTP仕様のSecurityOriginも参照すること。

- **Status \[SSP拡張\]**: ゴーストの実行状態。下記の通り。複数ある場合はカンマでつなげたもの。

  - **talking**: 喋っている途中
  - **choosing**: 選択肢表示中
  - **minimizing**: 最小化中
  - **induction**: `\![enter,inductionmode]`中
  - **passive**: `\![enter,passivemode]`中
  - **timecritical**: タイムクリティカルセクション(`\t`)中
  - **nouserbreak**: `\![enter,nouserbreak]`中
  - **online**: ネットワーク通信中
  - **opening(種類)**: 入力ボックス等が開いている。<br />
    複数種類が開いている場合は/区切りで列挙される。<br />
    "dialog"はファイル選択・カラーピッカー等。<br />
    例：opening(communicate/input/teach/dialog)
  - **balloon(ID群)**: バルーンが表示状態。<br />
    キャラクターID=バルーンID の形式で列挙される。<br />
    複数開いている場合は/区切りで列挙される。<br />
    例：balloon(0=2/1=0) で、`\0`が大きいバルーン、`\1`が通常のバルーンを表示中の意。

- **ID**: イベント名、またはテキストリソースの識別子。

- **BaseID \[SSP拡張\]**: 互換可能な基本のイベント名。<br />
  例：OnFirstBootはOnBootと互換で、かつOnFirstBootはOnBootの亜種なので、OnFirstBootのBaseIDにはOnBootが入る。

- **Reference\***: イベントに付随する追加情報群。Referenceの後には数字が入る。入れられる行数は制限なし（メモリが許す限り）

- **X-SSTP-PassThru-(任意の文字列) \[SSP 2.5.05～拡張\]**: SSTPからイベント通知が来た場合に限り、SSTPのリクエストヘッダ内で"X-SSTP-PassThru-"ではじまるものがそのまま通知される。<br />
  SSTP以外の時は追加されない。
