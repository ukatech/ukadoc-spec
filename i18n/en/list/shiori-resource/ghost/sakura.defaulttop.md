# sakura.defaulttop

**カテゴリ:** Ghost information

The Y coordinate of the default position for the main character (`\0`). The top edge of the character window is placed at this position.<br />
The situations in which the default position is used, the value's units and coordinate system, and the conditions under which it is ignored are the same as for [sakura.defaulty](sakura.defaulty.md) (effective in free movement mode, among others). If [sakura.defaulty](sakura.defaulty.md) is also specified, it takes precedence.<br />
A negative value is the distance from the bottom edge of the primary monitor's work area to the bottom edge of the character. -0 aligns it exactly with the bottom edge. Here, the bottom edge is shifted upward by the amount specified in SSP's "Desktop bottom offset" setting.\[2.9.13\]<br />
Using two consecutive minus signs specifies a negative coordinate itself (--100 is Y coordinate -100).\[2.9.13\]<br />
The same item can also be specified in the [ghost](../../../descript/shell/descript-txt/sakura.defaulttop.md) and [shell](../../../descript/shell/descript-txt/sakura.defaulttop.md) descript.txt files. The SHIORI resource takes precedence.

**対応:** SSP
