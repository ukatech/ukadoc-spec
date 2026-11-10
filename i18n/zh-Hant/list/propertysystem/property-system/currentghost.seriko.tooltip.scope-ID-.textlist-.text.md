# currentghost.seriko.tooltip.scope(ID).textlist(当たり判定名).text

**カテゴリ:** 屬性系統

指定的命中判定名稱所對應的工具提示顯示文字。<br />
指定空字串執行 SET 時，會視為刪除工具提示定義，因此可設定為不顯示工具提示。<br />
*\[SET有效\]*

**対応:** SSP (2.3.83)

## 記述例

```
\![set,property,currentghost.seriko.tooltip.scope(0).textlist(Head).text,頭をなでる]Head当たり判定で表示するツールチップを「頭をなでる」に変更\![set,property,currentghost.seriko.tooltip.scope(0).textlist(Head).text,]空っぽの指定だと定義削除となり表示されなくなる
```
