# sakura.defaulty,Y coordinate

**カテゴリ:** descript.txt

Default Y position of the baseware-side (`\0`); places the surface's reference point (usually the bottom center of the surface) at this position.\[2.9.13\]<br />
The value format and meaning (units, coordinate system, negative values, handling of --, and conditions under which it is invalid) are the same as for the SHIORI resource [sakura.defaulty](../../../list/shiori-resource/ghost/sakura.defaulty.md).<br />
Priority order: SHIORI resource > shell-side descript.txt (this entry) > [ghost-side descript.txt](../../ghost/descript-txt/sakura.defaulty.md).<br />
If [sakura.defaulttop](sakura.defaulttop.md) is also specified in the same descript.txt, this entry (defaulty) takes precedence.

**既定値:** ghost's descript settings

**対応:** SSP
