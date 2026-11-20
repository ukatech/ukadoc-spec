# sakura.defaulttop

**カテゴリ:** ghost信息

主体侧（`\0`）默认位置的Y坐标。将角色窗口的上边缘置于此位置。<br />
使用默认位置的场景，以及值的单位、坐标系和失效条件均与[sakura.defaulty](sakura.defaulty.md)相同（在自由移动模式等情况下有效）。如果同时指定了[sakura.defaulty](sakura.defaulty.md)，则后者优先。<br />
负值表示从主显示器工作区域的下边缘到角色下边缘的距离。-0表示紧贴下边缘。这里的下边缘是按SSP设置中的「桌面下边缘偏移量」向上移动后的位置。\[2.9.13\]<br />
连续使用两个-表示负坐标本身（--100表示Y坐标-100）。\[2.9.13\]<br />
也可以在[ghost](../../../descript/shell/descript-txt/sakura.defaulttop.md)和[shell](../../../descript/shell/descript-txt/sakura.defaulttop.md)的descript.txt中填写相同项目。SHIORI资源的设置优先。

**対応:** SSP
