# `\q[タイトル,OnID,r0,r1,...]`

**カテゴリ:** 選択肢コマンド

Displays choices.<br />
As above, if the ID begins with "On", selecting it starts the SHIORI event OnID (the event as written).<br />
Those parameters are stored in Reference0 and later, in the order r0, r1, ....

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
好きな季節は？\q[春,OnLikeSeason,花見,桜]\q[夏,OnLikeSeason,花火,ひまわり]\q[秋,OnLikeSeason,月見,菊]\q[冬,OnLikeSeason,年越し,山茶花]。選択時に、OnLikeSeasonイベントが発生し、例えば「春」を選択したならReference0に「花見」、Reference1に「桜」が格納されている。
```
