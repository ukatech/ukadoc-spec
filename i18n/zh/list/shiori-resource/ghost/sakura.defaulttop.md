# sakura.defaulttop

**カテゴリ:** ghost信息

本体侧(`\0`)默认位置的Y坐标。将角色窗口的上端放在此位置。<br />
默认位置的使用场景、值的单位和坐标系，以及使其无效的条件与[sakura.defaulty](sakura.defaulty.md)相同（在自由移动模式等情况下有效）。如果也指定了[sakura.defaulty](sakura.defaulty.md)，则优先使用该项。<br />
负值表示从主显示器工作区下端到角色下端的距离。-0表示紧贴下端。此处的下端是向上偏移SSP设置中“桌面下端偏移量”后的边缘。\[2.9.13\]<br />
连续写两个-表示负坐标本身（--100表示Y坐标-100）。\[2.9.13\]<br />
也可以在[ghost](../../../descript/ghost/descript-txt/sakura.defaulttop.md)和[shell](../../../descript/shell/descript-txt/sakura.defaulttop.md)的descript.txt中写入相同项目。SHIORI资源优先。

**対応:** SSP
