# プロパティシステム

## 概要

プロパティシステムはベースウェアが起動中に保持している各種パラメータに、ゴースト側からアクセスして読み書きする仕組みである。

- [参考:CROW テスト項目資料](http://crow.aqrs.jp/devtest.html)

## 記述例

プロパティシステムを利用するには、環境変数と通常のタグの二つの方法がある。<br />
SAKURA Scriptおよび環境変数のプロパティシステムの項もそれぞれ参照のこと。

- **[%property\[プロパティ名\]](../../sakura-script/environment-variable/pct-property.md)**: 環境変数としてプロパティを参照し、値を埋め込む。<br />
  単に値をそのまま表示したい場合に用いる。<br />
  以下はベースウェアの名前とバージョンをその場に埋め込む（表示する）。

  ```
  %property[baseware.name] ver,%property[baseware.version]
  ```

- **[`\![get,property,イベント名,プロパティ名]`](../../sakura-script/property-system-operation/bang-get-property.md)**: さくらスクリプトのタグによって任意名のSHIORI Eventを発生させ、そのReferenceを通じてプロパティを取得する。<br />
  プロパティをもとにSHIORI側でアクションを起こしたい場合に用いる。<br />
  以下はID「OnGetSakuraName」というSHIORI Eventを発生させ、そのreference0としてゴースト「Emily/Phase4.5」の相方側名（Teddy）を通知させる。

  ```
  \![get,property,OnGetSakuraName,ghostlist(Emily/Phase4.5).keroname]
  ```

- **[`\![set,property,プロパティ名,値]`](../../sakura-script/property-system-operation/bang-set-property.md)**: さくらスクリプトのタグによってプロパティを書き替える。<br />
  全てのプロパティに対して書き込みが許されているわけではないが、このページの項目で*\[SET有効\]*とあるものはこのようにして操作可能。<br />
  以下はシェル「ULTIMATE FORM」を、オーナードローメニューのシェル切り替えメニューから隠す例。

  ```
  \![set,property,currentghost.shelllist(ULTIMATE FORM).menu,hidden]
  ```
