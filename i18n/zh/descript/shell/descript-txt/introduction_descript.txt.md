# descript.txt（Shell）

## 概要

Shell的基本设置文件。<br />
除了Shell名称和作者信息外，气球的显示位置、owner draw菜单（右键菜单）的图像，以及dressup在owner draw菜单中的显示设置等也在此处进行。

## 記述例与基本写法

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

type和name为必需项。

在SSP中，为Shell设置homeurl后，也可以从资源管理器等位置进行网络更新。

关于dressup设置的各个项目，请参阅下文对应的章节。<br />
其基本机制是：对于在[surfaces.txt](../../shell-surfaces/index.md)中定义的计时bind的animationID，设置dressup名称和dressup类别名称（sakura(kero).bindgroup\*.name,～），并指定其在owner draw菜单中的位置（sakura(kero).menuitem\*,～）。

另外，以\\或%开头的字符串会被视为Sakura Script或环境变量标签，并因安全风险而被丢弃。如果要将它们作为普通字符使用，需要写成\\\\或\\%等形式进行转义。
