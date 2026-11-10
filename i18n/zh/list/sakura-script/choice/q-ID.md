# `\q[タイトル,ID]`

**カテゴリ:** Choice command

Displays a choice.<br />
After selection, the SHIORI event [OnChoiceSelect](../../shiori-event/choice/OnChoiceSelect.md) is triggered (SSP first triggers [OnChoiceSelectEx](../../shiori-event/choice/OnChoiceSelectEx.md)).<br />
The ID is stored in Reference0.<br />
Use the `\__q[]` tag to automatically wrap the text.

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
さくらスクリプトは好き？\q[好き,Like]\q[嫌い,Hate]。選択時に発生するOnChoiceSelectのReference0に、選んだものによって「like」か「hate」が格納されている。
```
