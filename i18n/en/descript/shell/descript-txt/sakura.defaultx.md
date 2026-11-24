# sakura.defaultx,X coordinate

**カテゴリ:** descript.txt

The X coordinate of the default position of the main character (`\0`). The surface's reference point (normally the bottom center of the surface) is placed at this position.\[2.9.13\]<br />
The format and meaning of the value (units, coordinate system, negative values, handling of --, and conditions under which it is ignored) are the same as the SHIORI resource [sakura.defaultx](../../../list/shiori-resource/ghost/sakura.defaultx.md).<br />
The order of precedence is SHIORI resource > shell's descript.txt (this entry) > ghost's descript.txt.<br />
If [sakura.defaultleft](sakura.defaultleft.md) is also specified in the same descript.txt, this entry (defaultx) takes precedence.

This can also be specified in the ghost's descript.txt. If specified in the shell's descript.txt, the shell's value takes precedence; otherwise, the ghost's value is used.

**既定値:** No value (the main character is placed at the bottom right of the primary monitor's work area)

**対応:** SSP
