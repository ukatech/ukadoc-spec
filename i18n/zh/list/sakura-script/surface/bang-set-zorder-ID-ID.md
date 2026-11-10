# `\![set,zorder,スコープID,スコープID,...]`

**カテゴリ:** surface 命令

将指定 scope 的窗口从左到右依次置于前方。<br />
例如：指定`\![set,zorder,1,0]`后，`\1`一定会显示在`\0`窗口前面。

如需同时控制 balloon 的 Z 顺序，请参照以下示例。<br />
示例：`\![set,zorder,balloon1,surface1,balloon0,surface0]`<br />
示例（省略写法）：!\[set,zorder,b1,s1,b0,s0\]<br />
指定后，将严格按`\1`的 balloon - `\1`的立绘 - `\0`的 balloon - `\0`的立绘的顺序控制显示。

多次执行此标签并指定不同的 scope ID，可以建立多个组。<br />
例如：执行`\![set,zorder,1,0]` `\![set,zorder,3,2]`后，`\1`显示在`\0`前面，`\p[3]`显示在`\p[2]`前面。<br />
同时控制 balloon 时也同样如此。

可指定的 scope ID 数量没有限制，但指定过多会稍微降低性能，因此建议指定2～3个。<br />
执行包含已配对 scope ID 的标签时会出错。若要更改组合，请先使用`\![reset]`标签，再重新设置。

在 ghost 结束前有效。

**対応:** SSP 2.3.77/2.7.34(s,b記法)

## 記述例

```sakurascript
\![set,zorder,1,0]相方側が、必ず本体側の手前に表示される。
```
