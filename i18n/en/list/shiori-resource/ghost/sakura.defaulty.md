# sakura.defaulty

**カテゴリ:** Ghost information

The default Y coordinate of the main character (`\0`). The surface's reference point (usually the bottom center of the surface) is placed at this position.<br />
The situations in which the default position is used, and the value's unit and coordinate system are the same as for [sakura.defaultx](sakura.defaultx.md).<br />
A negative value specifies the distance from the bottom edge of the primary monitor's work area. -0 is the bottom edge itself. Here, the bottom edge is shifted up by the amount specified by SSP's “Desktop bottom offset” setting.\[2.9.13\]<br />
Prefixing - twice specifies the negative coordinate itself (--100 means Y coordinate -100).\[2.9.13\]<br />
If [sakura.defaulttop](sakura.defaulttop.md) is also specified for the same axis, this setting (defaulty) takes precedence.<br />
The same item can also be specified in the descript.txt of the [ghost](../../../descript/ghost/descript-txt/sakura.defaulty.md) or [shell](../../../descript/shell/descript-txt/sakura.defaulty.md)\[2.9.13\]. The SHIORI resource takes precedence.<br />
This setting is ignored when configured to display along the top or bottom edge of the desktop, because the Y coordinate is determined by that setting (it is effective in modes such as free-movement mode).

**対応:** SSP
