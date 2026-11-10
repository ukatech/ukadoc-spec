# sakura.defaulttop,Y coordinate

**カテゴリ:** descript.txt

Default Y position of the baseware-side (`\0`); places the top edge of the character window at this position.<br />
The value format and meaning (units, coordinate system, negative values, handling of --, and conditions under which it is invalid) are the same as for the SHIORI resource [sakura.defaulttop](../../../list/shiori-resource/ghost/sakura.defaulttop.md). Negative values specify the margin from the bottom edge.\[2.9.13\]<br />
Effective only for settings that do not align with the top or bottom edge, such as when [seriko.alignmenttodesktop](seriko.alignmenttodesktop.md) is set to free.<br />
Priority order: SHIORI resource > shell-side descript.txt (this entry) > [ghost-side descript.txt](../../ghost/descript-txt/sakura.defaulttop.md). If [sakura.defaulty](sakura.defaulty.md) is also specified in the same descript.txt, that entry takes precedence.

**既定値:** ghost's descript settings

**対応:** SSP
