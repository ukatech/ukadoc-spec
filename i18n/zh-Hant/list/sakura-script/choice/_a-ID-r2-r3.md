# `\_a[ID,r2,r3...]`

**カテゴリ:** 選択肢コマンド

The range up to `\_a` becomes an anchor. Choices do not time out, but the balloon times out as with normal talk.<br />
Clicking the anchor starts the SHIORI event [OnAnchorSelect*Ex*](../../shiori-event/choice/OnAnchorSelectEx.md).<br />
The text used as the anchor is stored in Reference0, the ID in Reference1, and subsequent arguments in Reference2 and later.<br />
OnAnchorSelect also occurs after OnAnchorSelectEx, but since Reference1 and later contain nothing, this syntax is meaningless.

**対応:** SSP

## 記述例

```sakurascript
\_a[CharactorName,対象テディ,年齢不詳]テディ\_aはいいやつだったのに。\_a[CharactorName,対象エミリ,0x10歳]エミリ\_aのとっておきのおやつを食べたばかりに……。アンカークリック時、OnAnchorSelectExイベントが発生する。「テディ」をクリックした場合、reference0に「テディ」、reference1に「CharactorName」、reference2に「対象テディ」、reference3に「年齢不詳」が格納されている。
```
