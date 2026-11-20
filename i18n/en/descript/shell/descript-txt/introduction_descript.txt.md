# descript.txt (shell)

## Overview

The shell's basic configuration file.<br />
In addition to the shell name and author information, it configures balloon display positions, images for the owner draw menu (right-click menu), and how dressup items are displayed in the owner draw menu.

!!! note "Items that can also be written in the ghost's descript.txt"
    Items on this page marked as "can also be written in the ghost's descript.txt" can be written in the same format in the [ghost's `descript.txt`](../../ghost/descript-txt/index.md). Values written on the ghost side become defaults shared by all shells. If the same item is present in the shell's `descript.txt`, the shell's value takes precedence (overrides it).

## 記述例 and basic usage

```
charset,Shift_JIS
type,shell
name,master

craftman,ukadog
craftmanw,うか犬
craftmanurl,http://ssp.shillest.net/ukadoc/manual/index.html

menu.background.bitmap.filename,menu_background.png
menu.foreground.bitmap.filename,menu_foreground.png
menu.sidebar.bitmap.filename,menu_sidebar.png

sakura.balloon.offsetx,0
sakura.balloon.offsety,80
kero.balloon.offsetx,-20
kero.balloon.offsety,10
sakura.balloon.alignment,none
kero.balloon.alignment,none

sakura.bindgroup0.name,服,エプロンドレス,apron
sakura.bindgroup1.name,リボン,白リボン,ribbonwhite
sakura.bindgroup2.name,服,黒服,black
sakura.bindgroup3.name,リボン,黒リボン,ribbonblack
sakura.bindgroup0.default,1
sakura.bindgroup1.default,1

kero.bindgroup0.name,ネクタイ,ネクタイ
kero.bindgroup1.name,腕章,黒腕章
kero.bindgroup2.name,腕,ドリル
kero.bindgroup0.default,1
kero.bindgroup1.default,1

sakura.menuitem0,2
sakura.menuitem1,3
sakura.menuitem2,-
sakura.menuitem3,0
sakura.menuitem4,1

kero.menuitem0,0
kero.menuitem1,1
kero.menuitem2,-
kero.menuitem3,2
```

type and name are required.

In SSP, setting homeurl for a shell also enables network updates from Explorer and similar tools.

See the respective sections below for each dressup setting.<br />
The basic mechanism requires assigning a dressup name and category name to an animationID with bind timing defined in [surfaces.txt](../../shell-surfaces/index.md) (sakura(kero).bindgroup\*.name,...) and specifying its placement in the owner draw menu (sakura(kero).menuitem\*,...).

Strings beginning with \\ or % are treated as Sakura Script or environment variable tags and discarded due to security risks. To include them as literal characters, escape them as \\\\ or \\%, respectively.
