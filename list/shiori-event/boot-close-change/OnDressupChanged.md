# OnDressupChanged

**カテゴリ:** 起動・終了・切り替えイベント

着せ替えが切替えられた際に発生する。<br />
複数回通知される場合があり、その場合は一番最後のOnDressupChangedが*\[GET\]*、それ以外が*\[NOTIFY\]*となる。<br />
このイベントの後に発生する[OnNotifyDressupInfo](../notify/OnNotifyDressupInfo.md)も参照すること。

**着せ替えフラグ変更差分が大量になった場合(今のところ100要素)この通知はスキップされる。大量変更の受け取りはOnNotifyDressupInfoを利用すること。**

- **Reference0**: 着せ替え対象のキャラクターID。
- **Reference1**: パーツの名称。
- **Reference2**: 有効になった時に1、無効になった時に0。
- **Reference3**: パーツのカテゴリ名。
- **Reference4**: スクリプトから実行された時はscript、メニューから実行された時はuser \[2.5.90～\]

**対応:** SSP / Ninix
