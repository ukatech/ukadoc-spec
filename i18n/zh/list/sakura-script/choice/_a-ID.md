# `\_a[ID]`

**カテゴリ:** 选项命令

将`\_a`之前的范围设为锚点。选项不会超时，但与普通对话一样会触发气球超时。<br />
点击跳转链接时，将触发 SHIORI 事件[OnAnchorSelect](../../shiori-event/choice/OnAnchorSelect.md)（仅 SSP 会先触发[OnAnchorSelectEx](../../shiori-event/choice/OnAnchorSelectEx.md)）。<br />
ID 存入 Reference0。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\_a[Hint]アンカー\_aをクリックするとOnAnchorSelectExイベント(トークがなければOnAnchorSelectイベント)が発生する。reference0には「Hint」が格納されている。
```
