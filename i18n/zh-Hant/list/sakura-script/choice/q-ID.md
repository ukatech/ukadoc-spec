# `\q[タイトル,ID]`

**カテゴリ:** 選項指令

顯示選項。<br />
選擇後，會觸發 SHIORI 事件[OnChoiceSelect](../../shiori-event/choice/OnChoiceSelect.md)（只有 SSP 會先觸發[OnChoiceSelectEx](../../shiori-event/choice/OnChoiceSelectEx.md)）。<br />
ID 會存入 Reference0。<br />
若要讓文字自動換行，請使用`\__q[]`標籤。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
さくらスクリプトは好き？\q[好き,Like]\q[嫌い,Hate]。選択時に発生するOnChoiceSelectのReference0に、選んだものによって「like」か「hate」が格納されている。
```
