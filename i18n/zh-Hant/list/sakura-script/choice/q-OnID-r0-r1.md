# `\q[タイトル,OnID,r0,r1,...]`

**カテゴリ:** 選項指令

顯示選項。<br />
如上所述，ID 以「On」開頭時，選擇後會觸發 SHIORI 事件 OnID（即所寫的事件）。<br />
參數會依照 r0、r1、... 的順序存入 Reference0 以後。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
好きな季節は？\q[春,OnLikeSeason,花見,桜]\q[夏,OnLikeSeason,花火,ひまわり]\q[秋,OnLikeSeason,月見,菊]\q[冬,OnLikeSeason,年越し,山茶花]。選択時に、OnLikeSeasonイベントが発生し、例えば「春」を選択したならReference0に「花見」、Reference1に「桜」が格納されている。
```
