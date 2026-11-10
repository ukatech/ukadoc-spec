# descript.txt（Balloon的）

## 概述

balloon的基本设置文件。<br />
除balloon名称和作者信息外，还可设置部件的显示位置、文字显示方式等。

descript.txt是balloon整体的标准设置；在此基础上，还可以通过[balloon(s/k)\*s.txt](../balloonsoption/index.md)这一各个balloon surface的单独设置文件，分别调整各个surface。

## 記述例与基本写法

```
charset,Shift_JIS
type,balloon
name,凡例さんの吹き出し
homeurl,http://ssp.shillest.net/ukadoc/manual/hogehoge/example/

craftman,ukadog
craftmanw,うか犬
craftmanurl,http://ssp.shillest.net/ukadoc/manual/index.html

origin.x,14
origin.y,14

validrect.left,0
validrect.top,0
validrect.right,0
validrect.bottom,-12

wordwrappoint.x,-20

font.color.r,0
font.color.g,0
font.color.b,0

cursor.blendmethod,mergepennot
cursor.style,square
cursor.brush.color.r,0
cursor.brush.color.g,127
cursor.brush.color.b,127
cursor.pen.color.r,0
cursor.pen.color.g,0
cursor.pen.color.b,0
cursor.font.color.r,0
cursor.font.color.g,0
cursor.font.color.b,0

arrow0.x,296
arrow0.y,8
arrow1.x,296
arrow1.y,-18

onlinemarker.x,16
onlinemarker.y,-27

sstpmarker.x,16
sstpmarker.y,-20
sstpmessage.x,28
sstpmessage.y,-21
sstpmessage.font.name,ＭＳ ゴシック
sstpmessage.font.height,7
number.font.name,Arial
number.font.height,10
number.font.color.r,0
number.font.color.g,0
number.font.color.b,0
number.xr,-28
number.y,-24

communicatebox.x,8
communicatebox.y,21
communicatebox.width,385
communicatebox.height,20
```

与ghost或shell的descript.txt相比，这类文件有一个特点：从规格和实际情况来看，必需设置的项目非常多。

在SSP中，为balloon设置homeurl后，也可以从资源管理器等位置执行网络更新。

另外，以\\或%开头的字符串会被视为Sakura Script或环境变量标签，出于安全风险考虑会被丢弃。如果想将它们作为普通字符包含在字符串中，则需要使用\\\\或\\%等形式进行转义。
