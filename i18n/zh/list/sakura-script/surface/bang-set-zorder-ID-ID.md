# `\![set,zorder,スコープID,スコープID,...]`

**カテゴリ:** Surface command

Arrange the specified scope windows in front-to-back order, from left to right.<br />
Example: specifying `\![set,zorder,1,0]` ensures that `\1` is always displayed in front of the `\0` window.

To control Z-order together with balloons, follow the examples below.<br />
Example: `\![set,zorder,balloon1,surface1,balloon0,surface0]`<br />
Example (shorthand): !\[set,zorder,b1,s1,b0,s0\]<br />
This strictly controls the order as follows: the `\1` balloon - the `\1` standing image - the `\0` balloon - the `\0` standing image.

Multiple groups can be created by executing the tag multiple times with different scope IDs.<br />
Example: executing `\![set,zorder,1,0]` and `\![set,zorder,3,2]` displays `\1` in front of `\0`, and `\p[3]` in front of `\p[2]`.<br />
The same applies to the notation that includes balloons.

There is no limit to the number of scope IDs that can be specified, but specifying too many will slow things down somewhat, so around 2–3 is recommended.<br />
Executing a tag that includes a scope ID already paired with another will cause an error. To change the pairings, first use the `\![reset]` tag and then try again.

Effective until the ghost ends.

**対応:** SSP 2.3.77/2.7.34(s,b notation)

## 記述例

```sakurascript
\![set,zorder,1,0]相方側が、必ず本体側の手前に表示される。
```
