# `\![set,zorder,スコープID,スコープID,...]`

**カテゴリ:** surface命令

将指定scope的窗口按从左到右的顺序从前到后排列。<br />
例：指定`\![set,zorder,1,0]`时，`\1`始终显示在`\0`窗口前面。

如果要同时控制balloon的Z顺序，请参照以下示例。<br />
例：`\![set,zorder,balloon1,surface1,balloon0,surface0]`<br />
例（简写）：!\[set,zorder,b1,s1,b0,s0\]<br />
指定后，将严格按照`\1`的balloon - `\1`的立绘 - `\0`的balloon - `\0`的立绘的顺序排列。

多次执行scope ID各不相同的标签，可以创建多个组。<br />
例：执行`\![set,zorder,1,0]` `\![set,zorder,3,2]`后，`\1`显示在`\0`前面，`\p[3]`显示在`\p[2]`前面。<br />
同时指定balloon的写法也是如此。

可指定的scope ID数量没有限制，但指定过多会略微影响性能，建议指定2～3个。<br />
执行包含已配对的scope ID的标签会导致错误。要更改组合，请先使用`\![reset]`标签，再重新指定。

如果只想将特定角色置于最前面或最后面，可在scope ID前加上`front`或`back`。对于角色众多的ghost，这样就不必列举所有角色。<br />
例：指定`\![set,zorder,front,0]`时，`\0`显示在所有其他角色前面。<br />
例：指定`\![set,zorder,back,3]`时，`\p[3]`显示在所有其他角色后面。<br />
指定多个scope ID时，按书写顺序从前到后排列。`front`和`back`可以连续书写。<br />
例：指定`\![set,zorder,front,1,0,back,3,2]`时，从前到后的顺序为`\1`、`\0`、（其他角色）、`\p[3]`、`\p[2]`。

指定`front`或`back`后，其他角色按scope ID从小到大的顺序从前到后排列。<br />
`front`和`back`各自都可以分多次执行。每次指定的内容按执行顺序追加到各自的末尾。重新指定已指定的scope ID时，它会移到新指定的位置。同一个scope ID不能同时指定在前面和后面，以后一次指定为准。<br />
与只列出scope ID的写法相同，balloon排列在最前面的角色之前。<br />
`front`和`back`不能与只列出scope ID的写法或s,b写法并用。执行时会切换到后执行的写法，之前的指定会被丢弃。

有效期持续到ghost退出。

**対応:** SSP 2.3.77/2.7.34（s,b写法）/2.9.35（front,back写法）

## 記述例

```sakurascript
\![set,zorder,1,0]相方側が、必ず本体側の手前に表示される。
```
