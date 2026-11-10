# currentghost.seriko.cursor.scope(ID).mouse????list(当たり判定名).path

**カテゴリ:** 属性系统

指定的命中区域所对应的光标文件名（相对路径：依次在 shell 和 ghost 文件夹内查找）<br />
mouse????list可指定以下值：mouseuplist・mousedownlist・mousehoverlist・mousewheellist<br />
将空字符串设为SET值时，会视为删除定义，并恢复显示 shell 的默认光标。<br />
可以使用与[surfaces.txt的cursor区段](../../../descript/shell-surfaces/cursor-brace/introduction_cursorbrace.md)相同的指定方式。<br />
*\[SET有效\]*

**対応:** SSP (2.3.83)

## 記述例

```
\![set,property,currentghost.seriko.cursor.scope(0).mouseuplist(Head).path,頭.cur]Head当たり判定で使うカーソルを頭.curに変更\![set,property,currentghost.seriko.cursor.scope(0).mouseuplist(Head).path,]空っぽの指定だと定義削除となりシェルの標準カーソルとなる
```
