# descript.txt (for balloons)

## Overview

The basic settings file for a balloon.<br />
In addition to the balloon name and author information, it configures things such as the display positions of parts and text display.

descript.txt contains the standard settings for the entire balloon. On top of these settings, each surface of the balloon can be further adjusted in its own individual settings file, [balloon(s/k)\*s.txt](../balloonsoption/index.md).

## 記述例 and basic usage

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

Compared with descript.txt files for ghosts and shells, this file has the distinctive feature of having many settings that are mandatory, either by specification or in practice.

In SSP, setting homeurl for a balloon also enables network updates from Explorer and similar tools.

Note that strings beginning with \\ or % are treated as Sakura Script or environment variable tags and discarded for security reasons. To include them as literal characters, escape them as \\\\ or \\%.
