# `\_a[ID]`

**カテゴリ:** 選択肢コマンド

`\_a`がくるまでの範囲をアンカーとする。選択肢タイムアウトしないが、通常トーク同様バルーンタイムアウトする。<br />
ジャンパをクリックするとSHIORIイベント[OnAnchorSelect](../../shiori-event/choice/OnAnchorSelect.md)が開始される(SSPのみ先立って[OnAnchorSelectEx](../../shiori-event/choice/OnAnchorSelectEx.md)が開始される)。<br />
IDはReference0に格納される。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\_a[Hint]アンカー\_aをクリックするとOnAnchorSelectExイベント(トークがなければOnAnchorSelectイベント)が発生する。reference0には「Hint」が格納されている。
```
