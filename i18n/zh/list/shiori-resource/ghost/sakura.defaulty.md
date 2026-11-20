# sakura.defaulty

**カテゴリ:** ghost信息

本体侧(`\0`)默认位置的Y坐标。将surface的基准点（通常为surface的底部中央）置于此位置。<br />
默认位置的使用场景以及值的单位和坐标系与[sakura.defaultx](sakura.defaultx.md)相同。<br />
负值表示距主显示器工作区下边缘的距离。-0表示下边缘本身。此处的下边缘是按SSP设置中的“桌面下边缘偏移量”向上偏移后的位置。\[2.9.13\]<br />
将两个-重叠可直接指定负坐标（--100为Y坐标-100）。\[2.9.13\]<br />
如果同一轴上也指定了[sakura.defaulttop](sakura.defaulttop.md)，则此项(defaulty)优先。<br />
[ghost](../../../descript/shell/descript-txt/sakura.defaulty.md)和[shell](../../../descript/shell/descript-txt/sakura.defaulty.md)的descript.txt中也可以写入相同项目\[2.9.13\]。SHIORI资源优先。<br />
设置为沿桌面上边缘/下边缘显示时，Y坐标由该设置决定，因此此项无效（在自由移动模式等情况下有效）。

**対応:** SSP
