# `\q`\[Title,ID,r*2*,r*3*...\]

**カテゴリ:** Choice command

Displays a choice.<br />
After a selection, the SHIORI event [OnChoiceSelect*Ex*](../../shiori-event/choice/OnChoiceSelectEx.md) starts.<br />
r\* is stored in Reference\* of OnChoiceSelectEx.<br />
OnChoiceSelect also occurs after OnChoiceSelectEx, but nothing is stored in Reference1 or later, so it serves no purpose with this syntax.

**対応:** SSP

## 記述例

```sakurascript
好きな季節は？\q[春,LikeSeason,花見,桜]\q[夏,LikeSeason,花火,ひまわり]\q[秋,LikeSeason,月見,菊]\q[冬,LikeSeason,年越し,山茶花]。選択時に、OnChoiceSelectExイベントが発生し、例えば「秋」を選択したなら、Reference0に「秋」、Reference1に「LikeSeason」、Reference2に「月見」、Reference3に「菊」が格納されている。
```
