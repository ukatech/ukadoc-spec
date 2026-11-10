# descript.txt (for shells)

## Overview

The shell's basic settings file.<br />
In addition to the shell name and author information, this file is also used to configure balloon display positions, images for the owner-draw menu (right-click menu), and how dressup items appear in the owner-draw menu.

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

In SSP, setting homeurl for a shell also enables network updates from Explorer and similar applications.

For details about each dressup setting, see the corresponding sections below.<br />
The basic mechanism is to assign a dressup name and dressup category name (sakura(kero).bindgroup\*.name,～) to the timing bind's animationID defined in [surfaces.txt](../../shell-surfaces/index.md), and also specify its placement in the owner-draw menu (sakura(kero).menuitem\*,～).

Strings beginning with \\ or % are treated as Sakura Script or environment-variable tags and discarded as a security measure. To include them as literal characters, escape them as \\\\ or \\%.
