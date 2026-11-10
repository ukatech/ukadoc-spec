# sakura.defaultx,X coordinate

**カテゴリ:** descript.txt

The default X coordinate of the main character (`\0`). The surface's reference point (normally the bottom center of the surface) is placed at this position.\[2.9.13\]<br />
The format and meaning of the value (units, coordinate system, negative values, handling of --, and conditions under which it is invalid) are the same as for the SHIORI resource [sakura.defaultx](../../../list/shiori-resource/ghost/sakura.defaultx.md).<br />
The priority order is SHIORI resource > [shell-side descript.txt](../../shell/descript-txt/sakura.defaultx.md) > ghost-side descript.txt.<br />
If [sakura.defaultleft](sakura.defaultleft.md) is also specified in the same descript.txt, this value (defaultx) takes precedence.

**既定値:** No value (the main character is placed at the bottom right of the primary monitor's work area)

**対応:** SSP
