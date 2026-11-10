# `\f[cursormethod,描画方法]`

**カテゴリ:** 修改選項標記指令

修改選取中標記的繪製方法。只有形狀為 square 或 square+underline 時有效。<br />
可以指定 Win32 API 的 SetROP2 函式所支援的所有運算子。<br />
指定 default 可恢復為 balloon 設定的預設值。<br />
參考：[SetROP2 函式（外部網站）](https://learn.microsoft.com/ja-jp/windows/win32/api/wingdi/nf-wingdi-setrop2)<br />
※指定時不包含「R2\_」，使用小寫模式名稱。例如：notmaskpen

**対応:** SSP

## 記述例

```sakurascript
\f[cursormethod,copypen]\f[cursorbrushcolor,red]\q[選択肢,OnTest]選択中の選択肢の、枠内の描画方法を変更する。copypenの場合、cursorbrushcolorの色がそのまま描画される。
```
