# seriko.zorder,scope ID,scope ID,...

**カテゴリ:** descript.txt

The descript equivalent of [`\![set,zorder,スコープID,スコープID,...]`](../../../list/sakura-script/surface/bang-set-zorder-ID-ID.md). This can be configured in advance without executing the tag.

The `front` and `back` syntax can also be used (SSP 2.9.35 and later). Since only one line can be written in descript.txt, write `front` and `back` consecutively on the same line.<br />
Example: `seriko.zorder,front,0` → Places `\0` at the front.<br />
Example: `seriko.zorder,back,0,front,2,1` → Places `\0` at the back and arranges `\p[2]` and `\p[1]` toward the front in that order.

This can also be specified in the ghost's descript.txt. The shell's setting takes precedence if present; otherwise, the ghost's value is used.

**既定値:** No value

**対応:** SSP 2.4/2.9.35 (front,back syntax)
