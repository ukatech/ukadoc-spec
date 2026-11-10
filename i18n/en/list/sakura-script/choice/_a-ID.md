# `\_a[ID]`

**カテゴリ:** Choice command

The range up to `\_a` becomes an anchor. The choice does not time out, but the balloon times out as it does during normal talk.<br />
Clicking the anchor starts the SHIORI event [OnAnchorSelect](../../shiori-event/choice/OnAnchorSelect.md) (SSP alone starts [OnAnchorSelectEx](../../shiori-event/choice/OnAnchorSelectEx.md) first).<br />
The ID is stored in Reference0.

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\_a[Hint]アンカー\_aをクリックするとOnAnchorSelectExイベント(トークがなければOnAnchorSelectイベント)が発生する。reference0には「Hint」が格納されている。
```
