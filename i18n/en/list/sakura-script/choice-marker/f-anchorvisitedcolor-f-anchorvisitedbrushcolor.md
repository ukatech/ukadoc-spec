# `\f[anchorvisitedcolor,色指定]` or `\f[anchorvisitedbrushcolor,色指定]`

**カテゴリ:** Choice marker modification command

Change the color inside the rectangle of a visited anchor. Note that the color is determined by the effect of `\f[anchorvisitedmethod,描画方法]`.<br />
For how to specify the color, see [※refer below](note-1.md#形状指定の方法).

**対応:** SSP

## 記述例

```sakurascript
\f[anchorvisitedbrushcolor,red]\_a[OnTest]アンカー\_a訪問済みのアンカーの形状がsquareの場合、背景色が赤色になる。
```
