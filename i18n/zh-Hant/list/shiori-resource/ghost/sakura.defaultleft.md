# sakura.defaultleft

**カテゴリ:** Ghost information

The default X coordinate of the main character (`\0`). The left edge of the character window is placed at this position.<br />
The circumstances in which the default position is used, the units and coordinate system of the value, and the conditions under which it is invalid are the same as for [sakura.defaultx](sakura.defaultx.md). If [sakura.defaultx](sakura.defaultx.md) is also specified, that setting takes precedence.<br />
A negative value is the distance from the right edge of the primary monitor's work area to the character's right edge. -0 places it exactly at the right edge. This lets you specify a margin from the right edge of the screen without regard to the surface width.\[2.9.13\]<br />
Prefixing the value with two hyphens gives the negative coordinate itself (--100 is X coordinate -100).\[2.9.13\]<br />
The same item can also be specified in the descript.txt of a [ghost](../../../descript/ghost/descript-txt/sakura.defaultleft.md) or [shell](../../../descript/shell/descript-txt/sakura.defaultleft.md). The SHIORI Resource takes precedence.

**対応:** Materia / SSP / CROW
