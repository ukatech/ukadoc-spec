# currentghost.seriko.tooltip.scope(ID).textlist(当たり判定名).text

**カテゴリ:** プロパティシステム

指定した当たり判定名のツールチップ表示文字列。<br />
空文字列を指定してSETすると、ツールチップ定義削除扱いとなり、ツールチップを表示しないようにできる。<br />
*\[SET有効\]*

**対応:** SSP (2.3.83)

## 記述例

```
\![set,property,currentghost.seriko.tooltip.scope(0).textlist(Head).text,頭をなでる]Head当たり判定で表示するツールチップを「頭をなでる」に変更\![set,property,currentghost.seriko.tooltip.scope(0).textlist(Head).text,]空っぽの指定だと定義削除となり表示されなくなる
```
