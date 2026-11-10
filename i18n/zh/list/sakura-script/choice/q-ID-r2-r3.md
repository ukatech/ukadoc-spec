# `\q`\[标题,ID,r*2*,r*3*...\]

**カテゴリ:** 选项命令

显示选项。<br />
选择后，将触发 SHIORI 事件[OnChoiceSelect*Ex*](../../shiori-event/choice/OnChoiceSelectEx.md)。<br />
r\*存入 OnChoiceSelectEx 的 Reference\*。<br />
在 OnChoiceSelectEx 之后也会触发 OnChoiceSelect，但 Reference1 之后没有任何内容，因此这种写法下该事件没有意义。

**対応:** SSP

## 記述例

```sakurascript
好きな季節は？\q[春,LikeSeason,花見,桜]\q[夏,LikeSeason,花火,ひまわり]\q[秋,LikeSeason,月見,菊]\q[冬,LikeSeason,年越し,山茶花]。選択時に、OnChoiceSelectExイベントが発生し、例えば「秋」を選択したなら、Reference0に「秋」、Reference1に「LikeSeason」、Reference2に「月見」、Reference3に「菊」が格納されている。
```
