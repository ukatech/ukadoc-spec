# sakura.defaultx

**カテゴリ:** ghost信息

本体侧(`\0`)默认位置的X坐标。将surface的基准点（通常为surface的底部中央）置于此位置。<br />
默认位置用于没有保存显示位置时（如首次启动或重置显示位置时）。如果均未指定，则放置在主显示器工作区的右下角。<br />
值的单位为像素，使用以主显示器左上角为原点的屏幕坐标（多显示器时为整个虚拟桌面中的位置）。<br />
负值表示距主显示器工作区右边缘的距离。-0表示右边缘本身。\[2.9.13\]<br />
需要直接指定负坐标时，例如指向主显示器左侧的显示器，可将两个-重叠，如--100（此例为X坐标-100）。\[2.9.13\]<br />
如果同一轴上也指定了[sakura.defaultleft](sakura.defaultleft.md)，则此项(defaultx)优先。<br />
[ghost](../../../descript/shell/descript-txt/sakura.defaultx.md)和[shell](../../../descript/shell/descript-txt/sakura.defaultx.md)的descript.txt中也可以写入相同项目\[2.9.13\]。SHIORI资源优先。<br />
设置为沿桌面左边缘/右边缘显示时，X坐标由该设置决定，因此此项无效。

**対応:** SSP
