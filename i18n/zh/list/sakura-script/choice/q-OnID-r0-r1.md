# `\q[タイトル,OnID,r0,r1,...]`

**カテゴリ:** 选项命令

显示选项。<br />
如上所述，如果 ID 以 "On" 开头，选择后将触发 SHIORI 事件 OnID（即所写的事件）。<br />
这些参数会按 r0、r1……的顺序存储在 Reference0 及之后的 Reference 中。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
好きな季節は？\q[春,OnLikeSeason,花見,桜]\q[夏,OnLikeSeason,花火,ひまわり]\q[秋,OnLikeSeason,月見,菊]\q[冬,OnLikeSeason,年越し,山茶花]。選択時に、OnLikeSeasonイベントが発生し、例えば「春」を選択したならReference0に「花見」、Reference1に「桜」が格納されている。
```
