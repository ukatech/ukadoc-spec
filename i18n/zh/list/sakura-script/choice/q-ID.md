# `\q[タイトル,ID]`

**カテゴリ:** 选项命令

显示选项。<br />
选择后，将触发 SHIORI 事件 [OnChoiceSelect](../../shiori-event/choice/OnChoiceSelect.md)（仅 SSP 会在此之前触发 [OnChoiceSelectEx](../../shiori-event/choice/OnChoiceSelectEx.md)）。<br />
ID 会存储在 Reference0 中。<br />
要自动换行文本，请使用 `\__q[]` 标签。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
さくらスクリプトは好き？\q[好き,Like]\q[嫌い,Hate]。選択時に発生するOnChoiceSelectのReference0に、選んだものによって「like」か「hate」が格納されている。
```
