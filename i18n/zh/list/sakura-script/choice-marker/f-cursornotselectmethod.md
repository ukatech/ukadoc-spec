# `\f[cursornotselectmethod,描画方法]`

**カテゴリ:** 选项标记更改命令

更改未选中标记的绘制方法。仅当形状为 square 或 square+underline 时有效。<br />
可以指定 Win32API 的 SetROP2 函数支持的所有运算符。<br />
指定 default 可恢复为 balloon 设置的默认值。<br />
参考：[SetROP2 函数（外部网站）](https://learn.microsoft.com/ja-jp/windows/win32/api/wingdi/nf-wingdi-setrop2)<br />
※指定时不包含「R2\_」，使用小写模式名。

**対応:** SSP

## 記述例

```sakurascript
\f[cursornotselectmethod,copypen]\f[cursornotselectbrushcolor,red]\q[選択肢,OnTest]非選択中の選択肢の、枠内の描画方法を変更する。copypenの場合、cursornotselectbrushcolorの色がそのまま描画される。
```
