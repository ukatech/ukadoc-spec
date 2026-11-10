# sakura.defaultleft,X coordinate

**カテゴリ:** descript.txt

Default X position of the baseware-side (`\0`); places the left edge of the character window at this position.<br />
The value format and meaning (units, coordinate system, negative values, handling of --, and conditions under which it is invalid) are the same as for the SHIORI resource [sakura.defaultleft](../../../list/shiori-resource/ghost/sakura.defaultleft.md). Negative values specify the margin from the right edge.\[2.9.13\]<br />
Priority order: SHIORI resource > shell-side descript.txt (this entry) > [ghost-side descript.txt](../../ghost/descript-txt/sakura.defaultleft.md). If [sakura.defaultx](sakura.defaultx.md) is also specified in the same descript.txt, that entry takes precedence.

**既定値:** ghost's descript settings

**対応:** SSP
