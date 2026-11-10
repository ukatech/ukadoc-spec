# `\f[cursorcolor,色指定]` or `\f[cursorbrushcolor,色指定]`

**カテゴリ:** Choice marker change command

The color inside the rectangle of the selected marker changes. Note that the color is determined by the effect of `\f[cursormethod,描画方法]`.<br />
For how to specify it, [※see below](note-1.md#形状指定の方法).

**対応:** SSP

## 記述例

```sakurascript
\f[cursorbrushcolor,red]\q[選択肢,OnTest]選択中の選択肢の形状がsquareの場合、背景色が赤色になる。
```
