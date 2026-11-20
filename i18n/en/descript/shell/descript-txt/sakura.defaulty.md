# sakura.defaulty,Y coordinate

**カテゴリ:** descript.txt

The Y coordinate of the main character's (`\0`) default position. Places the surface's reference point (normally the bottom center of the surface) at this position. \[2.9.13\]<br />
The value's format and meaning (units, coordinate system, negative values, treatment of --, and conditions under which it is disabled) are the same as for the SHIORI resource [sakura.defaulty](../../../list/shiori-resource/ghost/sakura.defaulty.md).<br />
The order of precedence is the SHIORI resource, the shell's descript.txt (this setting), then the ghost's descript.txt.<br />
If [sakura.defaulttop](sakura.defaulttop.md) is also specified in the same descript.txt, this setting (defaulty) takes precedence.

This can also be specified in the ghost's descript.txt. If specified in the shell, the shell's value takes precedence; otherwise, the ghost's value is used.

**既定値:** No value (the main character is placed at the bottom edge of the work area)

**対応:** SSP
