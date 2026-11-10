# `\f[anchormethod,描画方法]`

**カテゴリ:** Choice marker modification command

Change the drawing method for the selected anchor. Effective only when the shape is square or square+underline.<br />
All operators supported by the Win32API SetROP2 function can be specified.<br />
Specify default to restore the balloon's default setting.<br />
Reference: [SetROP2 function (external site)](https://learn.microsoft.com/ja-jp/windows/win32/api/wingdi/nf-wingdi-setrop2)<br />
Note: Specify the lowercase mode name without "R2\_".

**対応:** SSP

## 記述例

```sakurascript
\f[anchormethod,copypen]\f[anchorbrushcolor,red]\_a[OnTest]アンカー\_a選択中のアンカーの、枠内の描画方法を変更する。copypenの場合、anchorbrushcolorの色がそのまま描画される。
```
