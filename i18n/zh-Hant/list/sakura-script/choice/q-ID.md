# `\q[タイトル,ID]`

**カテゴリ:** 選択肢コマンド

Displays choices.<br />
After selection, the SHIORI event [OnChoiceSelect](../../shiori-event/choice/OnChoiceSelect.md) starts (SSP alone first starts [OnChoiceSelectEx](../../shiori-event/choice/OnChoiceSelectEx.md)).<br />
The ID is stored in Reference0.<br />
To enable automatic line wrapping of text, use the `\__q[]` tag.

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
さくらスクリプトは好き？\q[好き,Like]\q[嫌い,Hate]。選択時に発生するOnChoiceSelectのReference0に、選んだものによって「like」か「hate」が格納されている。
```
