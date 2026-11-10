# currentghost.seriko.cursor.scope(ID).mouse????list(hit region name).path

**カテゴリ:** Property system

The cursor file name for the specified hit region name (relative path: searched in the shell folder first, then the ghost folder).<br />
The following values can be specified for mouse????list: mouseuplist, mousedownlist, mousehoverlist, mousewheellist<br />
When SET to an empty string, the definition is treated as deleted, restoring the shell's default cursor.<br />
The same cursor specifications as in the [cursor section of surfaces.txt](../../../descript/shell-surfaces/cursor-brace/introduction_cursorbrace.md) can be used.<br />
*\[SET supported\]*

**対応:** SSP (2.3.83)

## 記述例

```
\![set,property,currentghost.seriko.cursor.scope(0).mouseuplist(Head).path,頭.cur]Head当たり判定で使うカーソルを頭.curに変更\![set,property,currentghost.seriko.cursor.scope(0).mouseuplist(Head).path,]空っぽの指定だと定義削除となりシェルの標準カーソルとなる
```
