# `\f[anchormethod,描画方法]`

**カテゴリ:** 選項標記變更命令

變更選取中 anchor 的繪製方式。僅在形狀為 square 或 square+underline 時有效。<br />
可指定 Win32API 的 SetROP2 函式可使用的所有運算子。<br />
指定 default 可還原為氣球設定的預設值。<br />
參考：[SetROP2函數(外部サイト)](https://learn.microsoft.com/ja-jp/windows/win32/api/wingdi/nf-wingdi-setrop2)<br />
※指定時不包含「R2\_」，請使用小寫的模式名稱。

**対応:** SSP

## 記述例

```sakurascript
\f[anchormethod,copypen]\f[anchorbrushcolor,red]\_a[OnTest]アンカー\_a選択中のアンカーの、枠内の描画方法を変更する。copypenの場合、anchorbrushcolorの色がそのまま描画される。
```
