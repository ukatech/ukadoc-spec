# currentghost.seriko.tooltip.scope(ID).textlist(hit region name).text

**カテゴリ:** Property system

The text displayed in the tooltip for the specified hit region name.<br />
When SET to an empty string, the tooltip definition is treated as deleted, preventing the tooltip from being displayed.<br />
*\[SET supported\]*

**対応:** SSP (2.3.83)

## 記述例

```
\![set,property,currentghost.seriko.tooltip.scope(0).textlist(Head).text,頭をなでる]Head当たり判定で表示するツールチップを「頭をなでる」に変更\![set,property,currentghost.seriko.tooltip.scope(0).textlist(Head).text,]空っぽの指定だと定義削除となり表示されなくなる
```
