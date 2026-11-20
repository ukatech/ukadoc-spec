# 解决错误消息

## 解决错误消息

开发时，偶尔会遇到报告SSP出现某种错误的缺陷报告。<br />
这里列出了一些有助于解决错误消息的参考信息。<br />
这并不是彻底解决问题的手册，但或许能提供一些提示。

## 目次

1. [～ 不存在。](shell-error.md#-存在していません)
2. [提示旧定义/新定义相关问题](shell-error.md#旧定義新定義がどうこう言われた)

## ～ 不存在。

这是最常见的错误。大多数情况下是动画ID写错或遗漏定义等容易修正的问题，但也有一些较难处理的情况。

### \[GHOST\]default(master) shell 不存在。

根据伺か (Ukagaka)的规格，必须有shell/master文件夹，否则会发生兼容性问题。<br />
不过，如果确实不想创建master shell，可以通过以下定义避免此问题。

[seriko.defaultsurfacedirectoryname](../descript/ghost/descript-txt/seriko.defaultsurfacedirectoryname.md)

### \[SERIKO\]Surface=0(或10) 不存在。

根据伺か (Ukagaka)的规格，0号和10号surface受到特殊处理，作为使用`\s`标签指定不存在的编号等情况下代替显示的「默认surface」。<br />
即使创建了0号surface，也可能有不少情况下不想创建10号surface，此时请尝试添加以下定义。

[sakura.seriko.defaultsurface](../descript/shell/descript-txt/sakura.seriko.defaultsurface.md)

[kero.seriko.defaultsurface](../descript/shell/descript-txt/kero.seriko.defaultsurface.md)

[char\*.seriko.defaultsurface](../descript/shell/descript-txt/char-star-.seriko.defaultsurface.md)

## 提示旧定义/新定义相关问题

「使用旧定义时，却使用了新的定义方法」<br />
「使用新定义时，却使用了旧的定义方法」<br />
遇到类似错误消息时，请参阅以下内容。

[descript - version](../descript/shell-surfaces/descript-brace/version.md)

[关于SERIKO的旧定义和新定义](../descript/shell-surfaces/surface-brace/caption_seriko-redefine.md)

有时只需在surfaces.txt的最上方添加以下内容，就能消除错误。

```
descript
{
version,1
}
```
