# `\_a[ID]`

**カテゴリ:** Choice command

The range up to `\_a` is treated as an anchor. Choices do not time out, but the balloon times out as with normal talk.<br />
Clicking the link triggers the SHIORI event [OnAnchorSelect](../../shiori-event/choice/OnAnchorSelect.md) (SSP first triggers [OnAnchorSelectEx](../../shiori-event/choice/OnAnchorSelectEx.md)).<br />
The ID is stored in Reference0.

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\_a[Hint]アンカー\_aをクリックするとOnAnchorSelectExイベント(トークがなければOnAnchorSelectイベント)が発生する。reference0には「Hint」が格納されている。
```
