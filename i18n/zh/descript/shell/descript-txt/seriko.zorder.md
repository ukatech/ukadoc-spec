# seriko.zorder,scope ID,scope ID,...

**カテゴリ:** descript.txt

[`\![set,zorder,スコープID,スコープID,...]`](../../../list/sakura-script/surface/bang-set-zorder-ID-ID.md)的 descript 版。无需执行标签即可预先设置。

也可使用 `front` 和 `back` 写法（SSP 2.9.35 及以后版本）。由于 descript.txt 中只能写一行，因此 `front` 和 `back` 要连续写在同一行中。<br />
例：`seriko.zorder,front,0` → 将 `\0` 置于最前面。<br />
例：`seriko.zorder,back,0,front,2,1` → 将 `\0` 置于最后面，并按 `\p[2]`、`\p[1]` 的顺序向最前面排列。

也可写在 ghost 侧的 descript.txt 中。如果 shell 侧已指定，则优先使用 shell 侧的值；否则使用 ghost 侧的值。

**既定値:** 无值

**対応:** SSP 2.4/2.9.35（front、back 写法）
