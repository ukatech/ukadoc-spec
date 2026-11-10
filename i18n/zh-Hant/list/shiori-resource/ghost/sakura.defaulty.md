# sakura.defaulty

**カテゴリ:** Ghost information

The default Y coordinate of the main character (`\0`). The surface's origin (normally the bottom center of the surface) is placed at this position.<br />
The circumstances in which the default position is used, and the units and coordinate system of the value are the same as for [sakura.defaultx](sakura.defaultx.md).<br />
A negative value is the distance from the bottom edge of the primary monitor's work area. -0 is the bottom edge itself. The bottom edge here is shifted upward by the amount set in SSP's "Desktop bottom offset" setting.\[2.9.13\]<br />
Prefixing the value with two hyphens gives the negative coordinate itself (--100 is Y coordinate -100).\[2.9.13\]<br />
If [sakura.defaulttop](sakura.defaulttop.md) is also specified for the same axis, this setting (defaulty) takes precedence.<br />
The same item can also be specified in the descript.txt of a [ghost](../../../descript/ghost/descript-txt/sakura.defaulty.md) or [shell](../../../descript/shell/descript-txt/sakura.defaulty.md)\[2.9.13\]. The SHIORI Resource takes precedence.<br />
When configured to display along the top or bottom edge of the desktop, the Y coordinate is determined by that setting and is ignored (it is enabled in modes such as free-movement mode).

**対応:** SSP
