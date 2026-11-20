# descript.txt（shell 的）

## 概要

shell 的基本配置文件。<br />
除了 shell 名称和作者信息外，还在此设置 balloon 的显示位置、owner draw 菜单（右键菜单）的图像，以及 dressup 在 owner draw 菜单中的显示方式等。

!!! note "也可写入 ghost 的 descript.txt 的项目"
    本页中标注为“也可写入 ghost 侧的 descript.txt”的项目，也可以用相同格式写入 [ghost 的 `descript.txt`](../../ghost/descript-txt/index.md)。写在 ghost 侧的项目将成为所有 shell 共用的默认值；如果 shell 的 `descript.txt` 中有相同项目，则优先使用 shell 侧的值（覆盖默认值）。

## 記述例 与基本写法

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

type、name 为必填项。

在 SSP 中，为 shell 设置 homeurl 后，也可以从资源管理器等进行 network update。

关于 dressup 设置的各个项目，请参阅后文各节。<br />
其基本机制是：需要为 [surfaces.txt](../../shell-surfaces/index.md) 中定义的、时机为 bind 的 animationID 指定 dressup 名称和 dressup 类别名（sakura(kero).bindgroup\*.name,～），并指定其在 owner draw 菜单中的排列位置（sakura(kero).menuitem\*,～）。

另外，以 \\ 或 % 开头的字符串会被视为 Sakura Script 或环境变量的标签，因安全风险而被丢弃。若要将它们作为普通字符使用，需要分别转义为 \\\\ 或 \\% 等。
