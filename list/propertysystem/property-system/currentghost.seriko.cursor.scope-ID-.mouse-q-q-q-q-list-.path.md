# currentghost.seriko.cursor.scope(ID).mouse????list(当たり判定名).path

**カテゴリ:** プロパティシステム

指定した当たり判定名のカーソルファイル名(相対パス：シェル→ゴーストフォルダ内の順で探索)<br />
mouse????listは以下の指定が可能：mouseuplist・mousedownlist・mousehoverlist・mousewheellist<br />
空文字列を指定してSETすると、定義削除扱いとなり、シェルの標準カーソルの表示に戻すことができる。<br />
カーソル指定は[surfaces.txtのcursorセクション](../../../descript/shell-surfaces/cursor-brace/introduction_cursorbrace.md)と同じ指定が可能。<br />
*\[SET有効\]*

**対応:** SSP (2.3.83)

## 記述例

```
\![set,property,currentghost.seriko.cursor.scope(0).mouseuplist(Head).path,頭.cur]Head当たり判定で使うカーソルを頭.curに変更\![set,property,currentghost.seriko.cursor.scope(0).mouseuplist(Head).path,]空っぽの指定だと定義削除となりシェルの標準カーソルとなる
```
