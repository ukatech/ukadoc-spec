# `\![set,zorder,スコープID,スコープID,...]`

**カテゴリ:** Surface command

Arrange the windows for the specified scopes from front to back, in order from left to right.<br />
For example, specifying `\![set,zorder,1,0]` ensures that `\1` is always displayed in front of the `\0` window.

To control the Z-order of balloons along with surfaces, use the following syntax.<br />
Example: `\![set,zorder,balloon1,surface1,balloon0,surface0]`<br />
Example (abbreviated syntax): !\[set,zorder,b1,s1,b0,s0\]<br />
This strictly controls the order as follows: `\1` balloon - `\1` standing image - `\0` balloon - `\0` standing image.

You can create multiple groups by running the tag multiple times with different scope IDs.<br />
Example: Running `\![set,zorder,1,0]` and `\![set,zorder,3,2]` displays `\1` in front of `\0`, and `\p[3]` in front of `\p[2]`.<br />
The same applies to the syntax that includes balloons.

There is no limit to the number of scope IDs you can specify, but specifying a lot of them may affect performance, so 2–3 is recommended.<br />
Running a tag that includes scope IDs already in a pair causes an error. To change the combinations, use the `\![reset]` tag before trying again.

Effective until the ghost ends.

**対応:** SSP 2.3.77/2.7.34(s,b syntax)

## 記述例

```sakurascript
\![set,zorder,1,0]相方側が、必ず本体側の手前に表示される。
```
