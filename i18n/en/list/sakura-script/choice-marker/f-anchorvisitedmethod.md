# `\f[anchorvisitedmethod,描画方法]`

**カテゴリ:** Choice marker modification command

Change the drawing method for visited anchors. Effective only when the shape is square or square+underline.<br />
All operators supported by the Win32API SetROP2 function can be specified.<br />
Specify default to restore the balloon's default setting.<br />
Reference: [SetROP2 function (external site)](https://learn.microsoft.com/ja-jp/windows/win32/api/wingdi/nf-wingdi-setrop2)<br />
Note: Specify the lowercase mode name without "R2\_".

**対応:** SSP

## 記述例

```sakurascript
\f[anchorvisitedmethod,copypen]\f[anchorvisitedbrushcolor,red]\_a[OnTest]アンカー\_a訪問済みのアンカーの、枠内の描画方法を変更する。copypenの場合、anchorvisitedbrushcolorの色がそのまま描画される。
```
