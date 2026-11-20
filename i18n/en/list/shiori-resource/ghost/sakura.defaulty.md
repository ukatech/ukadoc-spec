# sakura.defaulty

**カテゴリ:** Ghost information

The Y coordinate of the default position for the main character (`\0`). The surface's reference point (usually its bottom center) is placed at this position.<br />
The situations in which the default position is used, the unit, and the coordinate system are the same as for [sakura.defaultx](sakura.defaultx.md).<br />
A negative value specifies the distance from the bottom edge of the primary monitor's work area. -0 is the bottom edge itself. Here, the bottom edge is shifted upward by the amount specified in SSP's "Desktop bottom edge offset" setting.\[2.9.13\]<br />
Two consecutive minus signs specify a negative coordinate directly (--100 is Y coordinate -100).\[2.9.13\]<br />
If [sakura.defaulttop](sakura.defaulttop.md) is also specified for the same axis, this setting (defaulty) takes precedence.<br />
The same entry can also be specified in the [ghost](../../../descript/shell/descript-txt/sakura.defaulty.md) or [shell](../../../descript/shell/descript-txt/sakura.defaulty.md) descript.txt\[2.9.13\]. The SHIORI resource takes precedence.<br />
This setting has no effect when the character is configured to appear along the top or bottom edge of the desktop, because the Y coordinate is determined by that setting (it takes effect in free movement mode, for example).

**対応:** SSP
