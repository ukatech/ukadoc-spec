# sakura.defaultleft

**カテゴリ:** Ghost information

The X coordinate of the default position for the main character (`\0`). The left edge of the character window is placed at this position.<br />
The situations in which the default position is used, the value's units and coordinate system, and the conditions under which it is ignored are the same as for [sakura.defaultx](sakura.defaultx.md). If [sakura.defaultx](sakura.defaultx.md) is also specified, it takes precedence.<br />
A negative value is the distance from the right edge of the primary monitor's work area to the right edge of the character. -0 aligns it exactly with the right edge. This allows the position to be specified as a margin from the right edge of the screen without regard to the surface width.\[2.9.13\]<br />
Using two consecutive minus signs specifies a negative coordinate itself (--100 is X coordinate -100).\[2.9.13\]<br />
The same item can also be specified in the [ghost](../../../descript/shell/descript-txt/sakura.defaultleft.md) and [shell](../../../descript/shell/descript-txt/sakura.defaultleft.md) descript.txt files. The SHIORI resource takes precedence.

**対応:** Materia / SSP / CROW
