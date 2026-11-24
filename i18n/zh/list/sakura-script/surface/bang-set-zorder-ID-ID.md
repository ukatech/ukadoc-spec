# `\![set,zorder,スコープID,スコープID,...]`

**カテゴリ:** surface 命令

将指定 scope 的窗口按从左到右的顺序依次置于更前方。<br />
例：指定 `\![set,zorder,1,0]` 后，`\1` 始终显示在 `\0` 窗口的前方。

如果要同时控制 balloon 的 Z 顺序，请按照以下示例操作。<br />
例：`\![set,zorder,balloon1,surface1,balloon0,surface0]`<br />
例（简写法）：!\[set,zorder,b1,s1,b0,s0\]<br />
指定后，将严格按照 `\1` 的 balloon、`\1` 的立绘、`\0` 的 balloon、`\0` 的立绘的顺序排列。

多次执行 scope ID 各不相同的标签，可以创建多个组。<br />
例：执行 `\![set,zorder,1,0]` `\![set,zorder,3,2]` 后，`\1` 显示在 `\0` 前方，`\p[3]` 显示在 `\p[2]` 前方。<br />
同时指定 balloon 的写法也一样。

可指定的 scope ID 数量没有限制，但指定大量 ID 会稍微影响性能，建议使用2～3个。<br />
执行包含已配对的 scope ID 的标签会出错。要更改组合，请先使用 `\![reset]` 标签，然后重新设置。

如果只想将特定角色置于最前面或最后面，可在 scope ID 前加上 `front` 或 `back`。对于角色众多的 ghost，这样就不必列出所有角色。<br />
例：指定 `\![set,zorder,front,0]` 后，`\0` 显示在所有其他角色的前方。<br />
例：指定 `\![set,zorder,back,3]` 后，`\p[3]` 显示在所有其他角色的后方。<br />
指定多个 scope ID 时，按书写顺序从前向后排列。`front` 和 `back` 可以连续书写。<br />
例：指定 `\![set,zorder,front,1,0,back,3,2]` 后，从前向后的顺序为 `\1`、`\0`、（其他角色）、`\p[3]`、`\p[2]`。

指定 `front` 或 `back` 后，其他角色按 scope ID 越小越靠前的顺序排列。<br />
`front` 和 `back` 分别可以分多次执行。每次执行时，按执行顺序追加到各自的末尾。再次指定已经指定过的 scope ID 时，它会移动到新位置。不能同时将其指定在前面和后面，以后指定的为准。<br />
与只列出 scope ID 的写法一样，balloon 排列在最前方角色的前面。<br />
`front` 和 `back` 不能与只列出 scope ID 的写法或 s,b 写法同时使用。系统会切换到后执行的写法，并丢弃之前的指定。

在 ghost 结束前有效。

**対応:** SSP 2.3.77/2.7.34(s,b 写法)/2.9.35(front,back 写法)

## 記述例

```sakurascript
\![set,zorder,1,0]相方側が、必ず本体側の手前に表示される。
```
