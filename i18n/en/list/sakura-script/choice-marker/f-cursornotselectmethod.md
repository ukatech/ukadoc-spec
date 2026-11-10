# `\f[cursornotselectmethod,描画方法]`

**カテゴリ:** Choice marker change command

Changes how the unselected marker is drawn. Effective only when the shape is square or square+underline.<br />
All operators available for use with the Win32API SetROP2 function can be specified.<br />
default returns to the balloon setting's standard.<br />
Reference: [SetROP2 function (external site)](https://learn.microsoft.com/ja-jp/windows/win32/api/wingdi/nf-wingdi-setrop2)<br />
※Specify a lowercase mode name without 「R2\_」.

**対応:** SSP

## 記述例

```sakurascript
\f[cursornotselectmethod,copypen]\f[cursornotselectbrushcolor,red]\q[選択肢,OnTest]非選択中の選択肢の、枠内の描画方法を変更する。copypenの場合、cursornotselectbrushcolorの色がそのまま描画される。
```
