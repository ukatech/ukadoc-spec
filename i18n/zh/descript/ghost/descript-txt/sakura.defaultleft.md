# sakura.defaultleft,X coordinate

**カテゴリ:** descript.txt

The default X coordinate for the baseware side (`\0`). The left edge of the character window is placed at this position.<br />
The format and meaning of the value (unit, coordinate system, negative values, handling of --, and conditions under which it becomes invalid) are the same as for the SHIORI resource [sakura.defaultleft](../../../list/shiori-resource/ghost/sakura.defaultleft.md). Negative values specify the margin from the right edge.\[2.9.13\]<br />
The priority order is SHIORI resource > [shell-side descript.txt](../../shell/descript-txt/sakura.defaultleft.md) > ghost-side descript.txt. If [sakura.defaultx](sakura.defaultx.md) is also specified in the same descript.txt, that setting takes precedence.

**既定値:** No value (the baseware side is placed at the bottom right of the primary monitor's work area)

**対応:** SSP
