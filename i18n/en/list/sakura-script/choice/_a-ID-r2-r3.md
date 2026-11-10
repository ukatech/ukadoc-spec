# `\_a[ID,r2,r3...]`

**カテゴリ:** Choice command

The range up to `\_a` becomes an anchor. The choice does not time out, but the balloon times out as it does during normal talk.<br />
Clicking the anchor starts the SHIORI event [OnAnchorSelect*Ex*](../../shiori-event/choice/OnAnchorSelectEx.md).<br />
The text used as the anchor is stored in Reference0, the ID in Reference1, and subsequent arguments in Reference2 and onward.<br />
OnAnchorSelect also occurs after OnAnchorSelectEx, but nothing is stored in Reference1 or later, so it serves no purpose with this syntax.

**対応:** SSP

## 記述例

```sakurascript
\_a[CharactorName,対象テディ,年齢不詳]テディ\_aはいいやつだったのに。\_a[CharactorName,対象エミリ,0x10歳]エミリ\_aのとっておきのおやつを食べたばかりに……。アンカークリック時、OnAnchorSelectExイベントが発生する。「テディ」をクリックした場合、reference0に「テディ」、reference1に「CharactorName」、reference2に「対象テディ」、reference3に「年齢不詳」が格納されている。
```
