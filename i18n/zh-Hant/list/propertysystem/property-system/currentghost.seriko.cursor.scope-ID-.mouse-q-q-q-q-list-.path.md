# currentghost.seriko.cursor.scope(ID).mouse????list(當て判定名).path

**カテゴリ:** 屬性系統

指定當碰撞區域名稱所使用的游標檔名（相對路徑：依序在 shell → ghost 資料夾中搜尋）<br />
mouse????list 可指定以下項目：mouseuplist・mousedownlist・mousehoverlist・mousewheellist<br />
以空字串執行 SET 時，會視為刪除定義，並可恢復顯示 shell 的標準游標。<br />
游標可使用與[surfaces.txt 的 cursor 區段](../../../descript/shell-surfaces/cursor-brace/introduction_cursorbrace.md)相同的指定方式。<br />
*\[SET 有效\]*

**対応:** SSP (2.3.83)

## 記述例

```
\![set,property,currentghost.seriko.cursor.scope(0).mouseuplist(Head).path,頭.cur]Head当たり判定で使うカーソルを頭.curに変更\![set,property,currentghost.seriko.cursor.scope(0).mouseuplist(Head).path,]空っぽの指定だと定義削除となりシェルの標準カーソルとなる
```
