# seriko.zorder,scope ID,scope ID,...

**カテゴリ:** descript.txt

The descript version of [`\![set,zorder,スコープID,スコープID,...]`](../../../list/sakura-script/surface/bang-set-zorder-ID-ID.md). This can be set in advance without executing the tag.

The `front` and `back` syntax is also supported (SSP 2.9.35 and later). Since descript.txt can contain only one line, write `front` and `back` consecutively on the same line.<br />
Example: `seriko.zorder,front,0` → Places `\0` at the front.<br />
Example: `seriko.zorder,back,0,front,2,1` → Places `\0` at the back and arranges `\p[2]` and `\p[1]` toward the front in that order.

**既定値:** No value

**対応:** SSP 2.4/2.9.35 (front,back syntax)
