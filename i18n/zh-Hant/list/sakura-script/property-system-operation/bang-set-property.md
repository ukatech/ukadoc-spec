# `\![set,property,プロパティ名,値]`

**カテゴリ:** 屬性系統操作命令

將值寫入屬性系統。<br />
※屬性系統的詳細資訊請參閱[屬性系統](../../propertysystem/index.md)頁面。

**対応:** SSP / CROW

## 記述例

```sakurascript
\![set,property,currentghost.shelllist(master).menu,hidden]オーナードローメニューのシェル(S)から、masterシェルを非表示にし手動で変更出来ないようにする。\![set,property,currentghost.shelllist(master).menu,]masterシェルを再度オーナードローメニューに表示する。
```
