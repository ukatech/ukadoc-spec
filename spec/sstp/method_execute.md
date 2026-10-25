# メソッド：EXECUTE

EXECUTEメソッドで、ゴーストの各種情報取得や、SakuraScriptによらない各種コマンド実行などを行うことができます。<br />
このメソッドの実行では、ゴーストは喋りませんが、内部状態が書き換わる可能性があります。

## EXECUTEサンプル

```
EXECUTE SSTP/1.1
Charset: UTF-8
Sender: SSTPクライアント
Command: GetName
```

## request固有ヘッダ

- **Command または Command\[param1,param2...\]**: 実行すべきコマンド。実行する内容と返ってくる情報は後述。<br />
  大かっこ以降は実行すべきコマンドに渡すパラメータを指定する。
- **Reference\* \[SSP\]**: 大かっこ指定の代わりにReference0～のヘッダでパラメータを指定することもできる。

Commandヘッダに指定できる文字列と、responseの「追加データ」で返ってくる結果については、下記を参照してください。

## Commandヘッダに指定できるコマンドと、返ってくる追加データ

- **GetName**: 起動中のゴーストの (`\0`名),(`\1`名) カンマ区切り
- **GetNames \[SSP\]**: 現在インストールされている`\0`名のリスト。改行区切り。空行で終端。
- **GetFMO \[SSP 2.5.57\] \[リモート制限あり\]**: [FMO](../fmo-mutex/index.md)の中身と同等の情報を取得する。<br />
  ただしSSTPで通信したアプリケーション内部での管理分に限り、同時実行中のアプリケーション群共用である本来のFMOとは異なる。<br />
  主にウインドウを持たずDirect SSTPを送信できないコンソールアプリなどで、Socket SSTPのみでReceiverGhostHWndヘッダを活用しDirect SSTP相当の機能を実現するために用いられる。<br />
  改行区切り、空行で終端。<br />
  リモートからの要求の場合は、各パス情報が抜け、ヘッダとhwndがダミーに置き換わる。
- **GetGhostName \[SSP\]**: 起動中のゴースト本体の名前(descript.txtのname)
- **GetShellName \[SSP\]**: 起動中のゴーストの現在使用中のシェルの名前
- **GetBalloonName \[SSP\]**: 起動中のゴーストの現在使用中のバルーンの名前
- **GetVersion**: ベースウェア(実行中のソフト)のバージョン
- **GetGhostNameList \[SSP 2.6.53\]**: SSPで認識している全ゴーストの名前(descript.txtのname)の改行区切りリスト
- **GetShellNameList \[SSP 2.6.53\]**: 起動中のゴーストで認識している全シェルの名前(descript.txtのname)の改行区切りリスト
- **GetBalloonNameList \[SSP 2.6.53\]**: SSPで認識している全バルーンの名前(descript.txtのname)の改行区切りリスト
- **GetHeadlineNameList \[SSP 2.6.53\]**: SSPで認識している全ヘッドラインの名前(descript.txtのname)の改行区切りリスト
- **GetPluginNameList \[SSP 2.6.53\]**: SSPで認識している全プラグインの名前(descript.txtのname)の改行区切りリスト
- **GetShortVersion \[SSP 2.6.53\]**: ベースウェア(実行中のソフト)のバージョン(ピリオド区切りのバージョン番号のみ)<br />
  [version.json](https://ssp.shillest.net/archive/version.json)のssp.full.versionなどと単純比較すると最新版かどうかチェックできる
- **GetStatus \[SSP 2.8.94\]**: 起動中のゴーストの現在の実行状態。SHIORI/3.0 requestのStatusヘッダや、プロパティシステムの[currentghost.status](../../list/propertysystem/property-system/currentghost.status.md)と同じ内容。<br />
  複数の状態に当てはまる場合はカンマ区切り。各値の意味は[※SHIORI Statusヘッダ](../../list/propertysystem/property-system/currentghost.status.md)を参照。<br />
  どの状態にも当てはまらない場合は追加データなし(ステータスコード200)
- **Quiet \[リモート不可\]**: Restoreを実行するか、16秒間が経過するまで黙る。追加データなし(ステータスコード200番台で成功)
- **Restore**: Quietを解除。追加データなし(ステータスコード200番台で成功)
- **CompressArchive \[SSP 2.7.23\] \[リモート不可\]**: 指定したフォルダ内のファイル群をZIPファイルに圧縮する。<br />
  パラメータ0：圧縮ファイル名(フルパスで指定、相対パス指定不可)<br />
  パラメータ1：圧縮すべきフォルダのフルパス<br />
  パラメータ2以降：オプション(省略可)<br />
  オプションは以下の通り。<br />
  --event=イベント識別子……イベント識別子を指定すると、レスポンス後に圧縮を続け、終わり次第イベントが起きる。識別子がOnではじまる場合はその識別子のイベントが発生し、それ以外の場合はOnCompressArchiveCompleteまたはOnCompressArchiveFailureが発生する。省略時は処理が完了するまでレスポンスが返らない。<br />
  --password=パスワード……指定したパスワードを使用してAES暗号化ZIPを有効にする。<br />
  動作後のイベントに関する仕様は[OnCompressArchiveComplete](../../list/shiori-event/other/OnCompressArchiveComplete.md)・[OnCompressArchiveFailure](../../list/shiori-event/other/OnCompressArchiveFailure.md)を参照。<br />
  \[SSP 2.9.25\] SAORI over DirectSSTPからは、[internal_fileのCompressArchive](../saori-ex/internal_file/internal_file.CompressArchive.md)でも呼べる（相対パス指定や`/`区切りも書ける）。<br />
  セキュリティ上の観点から、圧縮先は、SSP管理下のフォルダ(ghostフォルダ、balloonフォルダなど「フォルダ」設定で指定した場所)以下への展開に制限される。<br />
  また、この制限は適宜強化される可能性があるため、ゴースト自身のデータが置かれているフォルダ以下に限定するのが無難。<br />
  追加データなし(ステータスコード200番台で成功)
- **ExtractArchive \[SSP 2.7.23\] \[リモート不可\]**: 指定したZIPファイルを解凍する。<br />
  パラメータ0：圧縮ファイル名(フルパスで指定、相対パス指定不可)<br />
  パラメータ1：解凍先のフォルダのフルパス<br />
  パラメータ2以降：オプション(省略可)<br />
  オプションは以下の通り。<br />
  --event=イベント識別子……イベント識別子を指定すると、レスポンス後に解凍を続け、終わり次第イベントが起きる。識別子がOnではじまる場合はその識別子のイベントが発生し、それ以外の場合はOnExtractArchiveCompleteまたはOnExtractArchiveFailureが発生する。省略時は処理が完了するまでレスポンスが返らない。<br />
  --password=パスワード……指定したパスワードを使用して展開する。\[SSP 2.9.26\] パスワード入力ダイアログは出さない。パスワードが要るのに指定が無い、または違うときは、ダイアログを出さずに失敗する（レスポンスは500、イベントを指定していれば識別子＋Failure、または[OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md)）。\[SSP 2.9.25\]以前は、このオプションが無視されてダイアログが出ていた。<br />
  \[SSP 2.9.26\] 展開先に`..`を含む絶対パスを指定しても、解決した結果でSSP管理下のフォルダの外なら拒否される（以前は、管理下の外にも展開できた）。<br />
  動作後のイベントに関する仕様は[OnExtractArchiveComplete](../../list/shiori-event/other/OnExtractArchiveComplete.md)・[OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md)を参照。<br />
  \[SSP 2.9.25\] SAORI over DirectSSTPからは、[internal_fileのExtractArchive](../saori-ex/internal_file/internal_file.ExtractArchive.md)でも呼べる（相対パス指定や`/`区切りも書ける）。<br />
  セキュリティ上の観点から、解凍先は、SSP管理下のフォルダ(ghostフォルダ、balloonフォルダなど「フォルダ」設定で指定した場所)以下への展開に制限される。<br />
  また、この制限は適宜強化される可能性があるため、ゴースト自身のデータが置かれているフォルダ以下に限定するのが無難。<br />
  追加データなし(ステータスコード200番台で成功)
- **DumpSurface \[SSP 2.5.98\] \[リモート不可\]**: 合成済みのサーフェス画像を指定したディレクトリに出力する。パラメータは[`\![execute,dumpsurface]`](../../list/sakura-script/misc/bang-execute-dumpsurface-ID-prefix-ID-ID.md)と同じ。<br />
  ただしイベントIDは指定できず、ディレクトリ・スコープID・サーフェスリスト・prefix・ゼロ位置切り出し・アニメーションID \[SSP 2.9.05\] の順に指定する。<br />
  \[SSP 2.9.08\] SakuraScript版と同じく、--dir= / --scope= / --surface= / --prefix= / --fromzero= / --animation= の形式でも順不同で指定でき、上記の順による指定と混在してもよい（--で始まらないパラメータは、現れた順に上記の順で割り当てられる）。ディレクトリ以外は省略でき、スコープIDの省略時は0になる。--event=は無視される。<br />
  DumpSurface\[...\]の形式ではパラメータ中にカンマを書けないため、カンマを含むサーフェスリストはReference0以降で指定すること。<br />
  処理が終わるまでレスポンスが返らないので注意。<br />
  追加データなし(ステータスコード200番台で成功)
- **MoveAsync \[SSP\] \[リモート不可\]**: [`\![moveasync]`](../../list/sakura-script/surface/notes_move.md)と同じことをSakuraScriptを介さずに実行する。パラメータ指定方法はSakuraScript版と同じ。<br />
  SSTPのタイムアウトまでにresponseを返せないのとデッドロックの原因になるため、asyncなしのmoveは実行できない。<br />
  追加データなし(ステータスコード200番台で成功)
- **SetTrayIcon \[SSP\] \[リモート不可\]**: [`\![set,tasktrayicon]`](../../list/sakura-script/event/bang-set-tasktrayicon-.ico-duration-eq-runcount-eq.md)と同じことをSakuraScriptを介さずに実行する。パラメータ指定方法はSakuraScript版と同じ。<br />
  追加データなし(ステータスコード200番台で成功)
- **SetTrayBalloon \[SSP\] \[リモート不可\]**: [`\![set,trayballoon]`](../../list/sakura-script/event/bang-set-trayballoon.md)と同じことをSakuraScriptを介さずに実行する。パラメータ指定方法はSakuraScript版と同じ。<br />
  追加データなし(ステータスコード200番台で成功)
- **SetProperty \[SSP\] \[リモート不可\]**: [プロパティシステム](../../list/propertysystem/index.md)に値を書き込む。<br />
  パラメータ0：プロパティの名前<br />
  パラメータ1：設定すべき値<br />
  追加データなし(ステータスコード200番台で成功)
- **GetProperty \[SSP\]**: [プロパティシステム](../../list/propertysystem/index.md)から値を読み出す。<br />
  パラメータ0：プロパティの名前<br />
  追加データは取得したプロパティの値。
- **SetCookie**: Senderで指定したクライアント名ごとに保存される、汎用データ保存領域に書き込む。<br />
  ブラウザの「クッキー」と同様の使い方を想定している。<br />
  パラメータ0：クッキーの名前<br />
  パラメータ1：設定すべき値<br />
  追加データなし(ステータスコード200番台で成功)
- **GetCookie**: Senderで指定したクライアント名ごとに保存される、汎用データ保存領域から読み出す。<br />
  パラメータ0：クッキーの名前<br />
  追加データは取得したクッキーの値。
