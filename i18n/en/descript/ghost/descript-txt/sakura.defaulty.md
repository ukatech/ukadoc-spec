# sakura.defaulty,Y coordinate

**カテゴリ:** descript.txt

The default Y coordinate of the main character (`\0`). The surface's reference point (normally the bottom center of the surface) is placed at this position.\[2.9.13\]<br />
The format and meaning of the value (units, coordinate system, negative values, handling of --, and conditions under which it is invalid) are the same as for the SHIORI resource [sakura.defaulty](../../../list/shiori-resource/ghost/sakura.defaulty.md).<br />
The priority order is SHIORI resource > [shell-side descript.txt](../../shell/descript-txt/sakura.defaulty.md) > ghost-side descript.txt.<br />
If [sakura.defaulttop](sakura.defaulttop.md) is also specified in the same descript.txt, this value (defaulty) takes precedence.

**既定値:** No value (the main character is placed at the bottom edge of the work area)

**対応:** SSP
