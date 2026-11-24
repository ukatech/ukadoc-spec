# sakura.defaulttop,Y coordinate

**カテゴリ:** descript.txt

The Y coordinate of the default position of the main character (`\0`). The top edge of the character window is placed at this position.<br />
The format and meaning of the value (units, coordinate system, negative values, handling of --, and conditions under which it is ignored) are the same as the SHIORI resource [sakura.defaulttop](../../../list/shiori-resource/ghost/sakura.defaulttop.md). A negative value specifies the margin from the bottom edge.\[2.9.13\]<br />
This is effective only when the settings do not align the character with the top or bottom edge, such as when [seriko.alignmenttodesktop](seriko.alignmenttodesktop.md) is free.<br />
The order of precedence is SHIORI resource > shell's descript.txt (this entry) > ghost's descript.txt. If [sakura.defaulty](sakura.defaulty.md) is also specified in the same descript.txt, it takes precedence.

This can also be specified in the ghost's descript.txt. If specified in the shell's descript.txt, the shell's value takes precedence; otherwise, the ghost's value is used.

**既定値:** No value (the main character is placed at the bottom edge of the work area)

**対応:** SSP
