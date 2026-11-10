# sakura.defaulttop

**カテゴリ:** Ghost information

The default Y coordinate of the main character (`\0`). The top edge of the character window is placed at this position.<br />
The situations in which the default position is used, the value's unit and coordinate system, and the conditions under which it is ignored are the same as for [sakura.defaulty](sakura.defaulty.md) (it is effective in modes such as free-movement mode). If [sakura.defaulty](sakura.defaulty.md) is also specified, that setting takes precedence.<br />
A negative value specifies the distance from the bottom edge of the primary monitor's work area to the character's bottom edge. -0 places it exactly at the bottom edge. Here, the bottom edge is shifted up by the amount specified by SSP's “Desktop bottom offset” setting.\[2.9.13\]<br />
Prefixing - twice specifies the negative coordinate itself (--100 means Y coordinate -100).\[2.9.13\]<br />
The same item can also be specified in the descript.txt of the [ghost](../../../descript/ghost/descript-txt/sakura.defaulttop.md) or [shell](../../../descript/shell/descript-txt/sakura.defaulttop.md). The SHIORI resource takes precedence.

**対応:** SSP
