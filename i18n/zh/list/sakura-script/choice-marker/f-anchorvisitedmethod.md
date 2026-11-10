# `\f[anchorvisitedmethod,描画方法]`

**カテゴリ:** 选择标记更改命令

更改已访问锚点的绘制方法。仅当形状为square或square+underline时有效。<br />
可以指定Win32API的SetROP2函数支持的所有运算符。<br />
指定default时，恢复为气球设置的默认值。<br />
参考：[SetROP2函数（外部网站）](https://learn.microsoft.com/ja-jp/windows/win32/api/wingdi/nf-wingdi-setrop2)<br />
※指定小写模式名称，不包含「R2\_」。

**対応:** SSP

## 記述例

```sakurascript
\f[anchorvisitedmethod,copypen]\f[anchorvisitedbrushcolor,red]\_a[OnTest]アンカー\_a訪問済みのアンカーの、枠内の描画方法を変更する。copypenの場合、anchorvisitedbrushcolorの色がそのまま描画される。
```
