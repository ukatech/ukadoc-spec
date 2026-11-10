# sakura.defaulty

**カテゴリ:** 幽灵信息

本体侧（`\0`）的默认位置 Y 坐标。将 surface 的基准点（通常是 surface 的中央下方）放置在此位置。<br />
默认位置的适用场景、值的单位和坐标系均与[sakura.defaultx](sakura.defaultx.md)相同。<br />
负值表示距主显示器工作区域下边缘的距离。-0 表示下边缘本身。此处的下边缘是根据 SSP 设置中的“桌面下边缘偏移量”向上移后的位置。\[2.9.13\]<br />
连续写两个-号时，表示负坐标本身（--100 表示 Y 坐标为-100）。\[2.9.13\]<br />
同一轴上也指定了[sakura.defaulttop](sakura.defaulttop.md)时，此项（defaulty）优先。<br />
[幽灵](../../../descript/ghost/descript-txt/sakura.defaulty.md)和[外壳](../../../descript/shell/descript-txt/sakura.defaulty.md)的 descript.txt 中也可以写入相同项目\[2.9.13\]。SHIORI Resource 的优先级更高。<br />
设定为沿桌面上边缘/下边缘显示时，Y 坐标由该设置决定，因此此项无效（在自由移动模式等情况下有效）。

**対応:** SSP
