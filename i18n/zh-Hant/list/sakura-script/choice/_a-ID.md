# `\_a[ID]`

**カテゴリ:** 選項指令

將直到`\_a`為止的範圍設為錨點。選項不會逾時，但與一般對話相同，氣球會逾時。<br />
點擊跳轉文字後，會觸發 SHIORI 事件[OnAnchorSelect](../../shiori-event/choice/OnAnchorSelect.md)（只有 SSP 會先觸發[OnAnchorSelectEx](../../shiori-event/choice/OnAnchorSelectEx.md)）。<br />
ID 會存入 Reference0。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\_a[Hint]アンカー\_aをクリックするとOnAnchorSelectExイベント(トークがなければOnAnchorSelectイベント)が発生する。reference0には「Hint」が格納されている。
```
