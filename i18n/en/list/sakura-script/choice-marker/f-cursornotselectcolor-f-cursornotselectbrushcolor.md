# `\f[cursornotselectcolor,色指定]` or `\f[cursornotselectbrushcolor,色指定]`

**カテゴリ:** Choice marker change command

Changes the color inside the rectangle of the non-selected marker. Note that the color is determined by the effect of `\f[cursornotselectmethod,描画方法]`.<br />
For details on how to specify it, [see below](note-1.md#形状指定の方法).

**対応:** SSP

## 記述例

```sakurascript
\f[cursornotselectbrushcolor,red]\q[選択肢,OnTest]非選択中の選択肢の形状がsquareの場合、背景色が赤色になる。
```
