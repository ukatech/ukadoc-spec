# currentghost.seriko.tooltip.scope(ID).textlist(当たり判定名).text

**カテゴリ:** 属性系统

指定命中区域的工具提示显示文本。<br />
将空字符串设为SET值时，会视为删除工具提示定义，从而不再显示工具提示。<br />
*\[SET有效\]*

**対応:** SSP (2.3.83)

## 記述例

```
\![set,property,currentghost.seriko.tooltip.scope(0).textlist(Head).text,頭をなでる]Head当たり判定で表示するツールチップを「頭をなでる」に変更\![set,property,currentghost.seriko.tooltip.scope(0).textlist(Head).text,]空っぽの指定だと定義削除となり表示されなくなる
```
