# sakura.defaulttop,Y coordinate

**カテゴリ:** descript.txt

The Y coordinate of the main character's (`\0`) default position. Places the top edge of the character window at this position.<br />
The value's format and meaning (units, coordinate system, negative values, treatment of --, and conditions under which it is disabled) are the same as for the SHIORI resource [sakura.defaulttop](../../../list/shiori-resource/ghost/sakura.defaulttop.md). A negative value specifies the margin from the bottom edge. \[2.9.13\]<br />
Only effective when the character is not aligned to the top or bottom edge, such as when [seriko.alignmenttodesktop](seriko.alignmenttodesktop.md) is free.<br />
The order of precedence is the SHIORI resource, the shell's descript.txt (this setting), then the ghost's descript.txt. If [sakura.defaulty](sakura.defaulty.md) is also specified in the same descript.txt, it takes precedence.

This can also be specified in the ghost's descript.txt. If specified in the shell, the shell's value takes precedence; otherwise, the ghost's value is used.

**既定値:** No value (the main character is placed at the bottom edge of the work area)

**対応:** SSP
