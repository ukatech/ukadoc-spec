# `\q[タイトル,ID]`

**カテゴリ:** 選択肢コマンド

選択肢を表示。<br />
選択後、SHIORIイベント[OnChoiceSelect](../../shiori-event/choice/OnChoiceSelect.md)が開始される(SSPのみそれに先立って[OnChoiceSelectEx](../../shiori-event/choice/OnChoiceSelectEx.md)が開始される)。<br />
IDはReference0に格納される。<br />
テキストの自動改行を求める場合は`\__q[]`タグを使うこと。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
さくらスクリプトは好き？\q[好き,Like]\q[嫌い,Hate]。選択時に発生するOnChoiceSelectのReference0に、選んだものによって「like」か「hate」が格納されている。
```
