# `\f[cursormethod,描画方法]`

**カテゴリ:** Choice marker change command

Changes the drawing method for the selected marker. It is effective only when the shape is square or square+underline.<br />
Any operator available for use with the Win32API SetROP2 function can be specified.<br />
default returns to the balloon setting's default.<br />
See: [SetROP2 function (external site)](https://learn.microsoft.com/ja-jp/windows/win32/api/wingdi/nf-wingdi-setrop2)<br />
※Specify the mode name in lowercase, without "R2\_". Example: notmaskpen

**対応:** SSP

## 記述例

```sakurascript
\f[cursormethod,copypen]\f[cursorbrushcolor,red]\q[選択肢,OnTest]選択中の選択肢の、枠内の描画方法を変更する。copypenの場合、cursorbrushcolorの色がそのまま描画される。
```
