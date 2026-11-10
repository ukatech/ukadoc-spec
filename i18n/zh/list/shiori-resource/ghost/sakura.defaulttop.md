# sakura.defaulttop

**カテゴリ:** Ghost information

The default Y coordinate for the main character (`\0`). The character window's top edge is placed at this position.<br />
The situations in which the default position is used, the units and coordinate system of the value, and the conditions under which it is invalid are the same as for [sakura.defaulty](sakura.defaulty.md) (it is effective in modes such as free-movement mode). If [sakura.defaulty](sakura.defaulty.md) is also specified, it takes precedence.<br />
A negative value is the distance from the bottom edge of the primary monitor's work area to the character's bottom edge. -0 places it exactly at the bottom edge. Here, the bottom edge is shifted upward by the amount specified by SSP's "Desktop bottom edge offset" setting.\[2.9.13\]<br />
Prefixing a negative value with another - specifies the negative coordinate itself (--100 is Y coordinate -100).\[2.9.13\]<br />
The same item can also be written in the descript.txt of the [ghost](../../../descript/ghost/descript-txt/sakura.defaulttop.md) or [shell](../../../descript/shell/descript-txt/sakura.defaulttop.md). The SHIORI Resource takes precedence.

**対応:** SSP
