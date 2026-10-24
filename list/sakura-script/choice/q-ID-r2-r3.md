# `\q`\[タイトル,ID,r*2*,r*3*...\]

**カテゴリ:** 選択肢コマンド

選択肢を表示。<br />
選択後、SHIORIイベント[OnChoiceSelect*Ex*](../../shiori-event/choice/OnChoiceSelectEx.md)が開始される。<br />
r\*はOnChoiceSelectExのReference\*に格納される。<br />
OnChoiceSelectExに続いてOnChoiceSelectも発生するが、Reference1以降に何も入らずこの書き方では無意味。

**対応:** SSP

## 記述例

```sakurascript
好きな季節は？\q[春,LikeSeason,花見,桜]\q[夏,LikeSeason,花火,ひまわり]\q[秋,LikeSeason,月見,菊]\q[冬,LikeSeason,年越し,山茶花]。選択時に、OnChoiceSelectExイベントが発生し、例えば「秋」を選択したなら、Reference0に「秋」、Reference1に「LikeSeason」、Reference2に「月見」、Reference3に「菊」が格納されている。
```
