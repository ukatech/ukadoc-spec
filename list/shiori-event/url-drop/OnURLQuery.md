# OnURLQuery

**カテゴリ:** URLドロップイベント

URLがキャラクターウィンドウにドラッグ＆ドロップされた際に通知される。<br />
これに対してスクリプトを返すと、通常のダウンロード処理がキャンセルされる。<br />
ゴースト側でURLを独自に処理したい場合のみスクリプトを返すこと。

- **Reference0**: URLパス。
- **Reference1**: 本体の場合は0、相方の場合は1。SSP/CROWでは2以降もある。
- **Reference2**: ドロップされたURLのMIMEタイプ
- **Reference3**: 反応しなかった場合にSSPがこの後実行予定の処理。<br />
  feed・nar・homeurl・ical・ssf・unknownのいずれか。<br />
  unknownの場合は本体が処理に対応できないURLであり、本体側ではこれ以上の処理ができないことを示す。<br />
  それ以外はReference0とともにそのまま [`\![execute,dropdefault,url]`](../../sakura-script/misc/bang-execute-dropdefault-file-.-bang-execute-dropdefault-url-URL.md)\[2.9.10\] または [`\![execute,install,url]`](../../sakura-script/misc/bang-execute-install-url-URL.md) に渡すと処理の続きが行われる。

**対応:** SSP Ref3は2.6.35
