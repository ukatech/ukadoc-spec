# sakura.defaultx,X coordinate

**カテゴリ:** descript.txt

The default X coordinate for the main character (`\0`). The surface reference point (usually the bottom center of the surface) is placed at this position.\[2.9.13\]<br />
The value format and meaning (unit, coordinate system, negative values, handling of --, and conditions under which the value becomes invalid) are the same as for the SHIORI resource [sakura.defaultx](../../../list/shiori-resource/ghost/sakura.defaultx.md).<br />
The priority order is SHIORI resource > [shell-side descript.txt](../../shell/descript-txt/sakura.defaultx.md) > ghost-side descript.txt.<br />
If [sakura.defaultleft](sakura.defaultleft.md) is also specified in the same descript.txt, this value (defaultx) takes precedence.

**既定値:** No value (the main character is placed at the bottom right of the primary monitor's work area)

**対応:** SSP
