# `\q`\[標題,ID,r*2*,r*3*...\]

**カテゴリ:** 選項指令

顯示選項。<br />
選擇後，會觸發 SHIORI 事件[OnChoiceSelect*Ex*](../../shiori-event/choice/OnChoiceSelectEx.md)。<br />
r\*會存入 OnChoiceSelectEx 的 Reference\*。<br />
OnChoiceSelectEx 之後也會觸發 OnChoiceSelect，但 Reference1 以後沒有資料，因此這種寫法沒有意義。

**対応:** SSP

## 記述例

```sakurascript
好きな季節は？\q[春,LikeSeason,花見,桜]\q[夏,LikeSeason,花火,ひまわり]\q[秋,LikeSeason,月見,菊]\q[冬,LikeSeason,年越し,山茶花]。選択時に、OnChoiceSelectExイベントが発生し、例えば「秋」を選択したなら、Reference0に「秋」、Reference1に「LikeSeason」、Reference2に「月見」、Reference3に「菊」が格納されている。
```
