# seriko.zorder,scope ID,scope ID,...

**カテゴリ:** descript.txt

[`\![set,zorder,スコープID,スコープID,...]`](../../../list/sakura-script/surface/bang-set-zorder-ID-ID.md)的descript版本。无需执行标签即可预先设置。

也可使用`front`和`back`写法（SSP 2.9.35及以后版本）。descript.txt只能写一行，因此`front`和`back`要连续写在同一行。<br />
例：`seriko.zorder,front,0` → 将`\0`置于最前面。<br />
例：`seriko.zorder,back,0,front,2,1` → 将`\0`置于最后面，并将`\p[2]`、`\p[1]`按顺序排列在最前面。

**既定値:** 无值

**対応:** SSP 2.4/2.9.35（front,back写法）
