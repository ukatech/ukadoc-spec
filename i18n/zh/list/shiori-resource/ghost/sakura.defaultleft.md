# sakura.defaultleft

**カテゴリ:** ghost信息

本体侧(`\0`)默认位置的X坐标。将角色窗口的左端放在此位置。<br />
默认位置的使用场景、值的单位和坐标系，以及使其无效的条件与[sakura.defaultx](sakura.defaultx.md)相同。如果也指定了[sakura.defaultx](sakura.defaultx.md)，则优先使用该项。<br />
负值表示从主显示器工作区右端到角色右端的距离。-0表示紧贴右端。无需考虑surface宽度，可将其指定为距屏幕右端的边距。\[2.9.13\]<br />
连续写两个-表示负坐标本身（--100表示X坐标-100）。\[2.9.13\]<br />
也可以在[ghost](../../../descript/ghost/descript-txt/sakura.defaultleft.md)和[shell](../../../descript/shell/descript-txt/sakura.defaultleft.md)的descript.txt中写入相同项目。SHIORI资源优先。

**対応:** Materia / SSP / CROW
