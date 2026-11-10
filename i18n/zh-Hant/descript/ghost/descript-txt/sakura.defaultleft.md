# sakura.defaultleft,X coordinate

**カテゴリ:** descript.txt

The X coordinate of the baseware-side (`\0`) default position. The left edge of the character window is placed at this position.<br />
The format and meaning of the value (unit, coordinate system, negative values, how -- is handled, and conditions under which it becomes invalid) are the same as for the SHIORI resource [sakura.defaultleft](../../../list/shiori-resource/ghost/sakura.defaultleft.md). Negative values specify the margin from the right edge.\[2.9.13\]<br />
The priority order is SHIORI resource > [shell-side descript.txt](../../shell/descript-txt/sakura.defaultleft.md) > ghost-side descript.txt. If [sakura.defaultx](sakura.defaultx.md) is also specified in the same descript.txt, that value takes precedence.

**既定値:** No value (the baseware-side is placed at the lower right of the primary monitor's work area)

**対応:** SSP
