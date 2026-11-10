# sakura.defaulttop

**カテゴリ:** Ghost information

The default Y coordinate of the main character (`\0`). The top edge of the character window is placed at this position.<br />
The circumstances in which the default position is used, the units and coordinate system of the value, and the conditions under which it is invalid are the same as for [sakura.defaulty](sakura.defaulty.md) (it is enabled in modes such as free-movement mode). If [sakura.defaulty](sakura.defaulty.md) is also specified, that setting takes precedence.<br />
A negative value is the distance from the bottom edge of the primary monitor's work area to the character's bottom edge. -0 places it exactly at the bottom edge. The bottom edge here is shifted upward by the amount set in SSP's "Desktop bottom offset" setting.\[2.9.13\]<br />
Prefixing the value with two hyphens gives the negative coordinate itself (--100 is Y coordinate -100).\[2.9.13\]<br />
The same item can also be specified in the descript.txt of a [ghost](../../../descript/ghost/descript-txt/sakura.defaulttop.md) or [shell](../../../descript/shell/descript-txt/sakura.defaulttop.md). The SHIORI Resource takes precedence.

**対応:** SSP
