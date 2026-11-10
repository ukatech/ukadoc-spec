# sakura.defaulttop,Y coordinate

**カテゴリ:** descript.txt

The default Y coordinate of the main body side (`\0`). The top edge of the character window is placed at this position.<br />
The format and meaning of the value (unit, coordinate system, negative values, handling of --, and conditions under which it becomes invalid) are the same as for the SHIORI resource [sakura.defaulttop](../../../list/shiori-resource/ghost/sakura.defaulttop.md). Negative values specify the margin from the bottom edge.\[2.9.13\]<br />
This setting is effective only when the position is not aligned with the top or bottom edge, such as when [seriko.alignmenttodesktop](seriko.alignmenttodesktop.md) is set to free.<br />
The priority is SHIORI resource > [shell-side descript.txt](../../shell/descript-txt/sakura.defaulttop.md) > ghost-side descript.txt. If [sakura.defaulty](sakura.defaulty.md) is also specified in the same descript.txt, that setting takes precedence.

**既定値:** No value (the main body side is placed at the bottom edge of the work area)

**対応:** SSP
