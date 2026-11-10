# sakura.defaultx

**カテゴリ:** ghost信息

本体侧(`\0`)默认位置的X坐标。将surface的基准点（通常为surface底部中央）放在此位置。<br />
没有保存显示位置时（例如首次启动或重置显示位置后）会使用默认位置。如果均未指定，则放在主显示器工作区的右下角。<br />
值的单位为像素，使用屏幕坐标，原点为主显示器左上角（多显示器环境中，坐标相对于整个虚拟桌面）。<br />
负值表示距主显示器工作区右端的距离。-0表示右端本身。\[2.9.13\]<br />
若要指定负坐标本身（例如指向主显示器左侧的显示器），请连续写两个-，如--100（此例表示X坐标-100）。\[2.9.13\]<br />
同一轴上也指定了[sakura.defaultleft](sakura.defaultleft.md)时，优先使用此项(defaultx)。<br />
也可以在[ghost](../../../descript/ghost/descript-txt/sakura.defaultx.md)和[shell](../../../descript/shell/descript-txt/sakura.defaultx.md)的descript.txt中写入相同项目\[2.9.13\]。SHIORI资源优先。<br />
设置为沿桌面左端/右端显示时，X坐标由该设置决定，因此此项无效。

**対応:** SSP
