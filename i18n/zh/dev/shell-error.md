# 解决错误消息

## 解决错误消息

开发过程中，有时会遇到这样的 bug 报告：SSP 抛出了某个错误。<br />
这里列出了一些有助于解决错误消息的信息。<br />
这不是一份能彻底解决问题的手册，但应该能提供一些小提示。

## 目次

1. [～ 不存在。](shell-error.md#-存在していません)
2. [提示旧定义/新定义相关错误](shell-error.md#旧定義新定義がどうこう言われた)

## ～ 不存在。

这是最常见的错误。大多数情况下是动画 ID 写错或漏写定义等，通常很容易修正，但也有一些情况会让人难以处理。

### \[GHOST\]default(master) shell 不存在。

根据伺か的规格，shell/master 文件夹是必需的；如果没有，会产生兼容性问题。<br />
不过，如果确实不想创建 master shell，可以通过以下定义来避免。

[seriko.defaultsurfacedirectoryname](../descript/ghost/descript-txt/seriko.defaultsurfacedirectoryname.md)

### \[SERIKO\]Surface=0(或10) 不存在。

根据伺か的规格，编号0和10的 surface 有特殊用途，是在`\s`标签指定不存在的编号等情况下显示的「默认 surface」。<br />
先不考虑编号0，有时确实不想创建编号10的 surface，因此可以尝试添加以下定义。

[sakura.seriko.defaultsurface](../descript/ghost/descript-txt/sakura.seriko.defaultsurface.md)

[kero.seriko.defaultsurface](../descript/ghost/descript-txt/kero.seriko.defaultsurface.md)

[char\*.seriko.defaultsurface](../descript/ghost/descript-txt/char-star-.seriko.defaultsurface.md)

## 提示旧定义/新定义相关错误

遇到类似以下错误消息时，请检查下面的内容。<br />
「使用了旧定义，但采用了新定义方法」<br />
「使用了新定义，但采用了旧定义方法」

[descript - version](../descript/shell-surfaces/descript-brace/version.md)

[SERIKO 的旧定义与新定义](../descript/shell-surfaces/surface-brace/caption_seriko-redefine.md)

在某些情况下，只需将以下内容添加到surfaces.txt的最上方，就能消除错误。

```
descript
{
version,1
}
```
