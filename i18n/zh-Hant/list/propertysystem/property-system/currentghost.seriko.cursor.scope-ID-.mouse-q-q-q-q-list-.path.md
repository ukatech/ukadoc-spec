# currentghost.seriko.cursor.scope(ID).mouse????list(hit region name).path

**カテゴリ:** Property System

Cursor file name for the specified hit region name (relative path: searched in the shell first, then in the ghost folder)<br />
mouse????list can be specified as follows: mouseuplist・mousedownlist・mousehoverlist・mousewheellist<br />
If SET to an empty string, the definition is treated as deleted, and the shell's default cursor can be displayed again.<br />
The cursor can be specified in the same way as in the [cursor section of surfaces.txt](../../../descript/shell-surfaces/cursor-brace/introduction_cursorbrace.md).<br />
*\[SET enabled\]*

**対応:** SSP (2.3.83)

## 記述例

```
\![set,property,currentghost.seriko.cursor.scope(0).mouseuplist(Head).path,頭.cur]Head当たり判定で使うカーソルを頭.curに変更\![set,property,currentghost.seriko.cursor.scope(0).mouseuplist(Head).path,]空っぽの指定だと定義削除となりシェルの標準カーソルとなる
```
