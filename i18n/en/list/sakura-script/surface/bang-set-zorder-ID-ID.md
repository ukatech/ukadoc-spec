# `\![set,zorder,スコープID,スコープID,...]`

**カテゴリ:** Surface commands

Places the windows of the specified scopes in order from left to right, from front to back.<br />
Example: `\![set,zorder,1,0]` always displays `\1` in front of the `\0` window.

To control the Z-order of balloons as well, follow the examples below.<br />
Example: `\![set,zorder,balloon1,surface1,balloon0,surface0]`<br />
Example (abbreviated syntax): !\[set,zorder,b1,s1,b0,s0\]<br />
This strictly controls the order as follows: `\1` balloon - `\1` character image - `\0` balloon - `\0` character image.

Executing multiple tags with different scope IDs creates multiple groups.<br />
Example: Executing `\![set,zorder,1,0]` and `\![set,zorder,3,2]` displays `\1` in front of `\0` and `\p[3]` in front of `\p[2]`.<br />
The same applies to the syntax that includes balloons.

There is no limit on the number of scope IDs that can be specified, but specifying many can be somewhat resource-intensive, so about 2–3 are recommended.<br />
Executing a tag that includes a scope ID already paired with another causes an error. To change the combination, use the `\![reset]` tag and try again.

To place only specific characters at the very front or back, prefix their scope IDs with `front` or `back`. This avoids having to list every character in a ghost with many characters.<br />
Example: `\![set,zorder,front,0]` displays `\0` in front of all other characters.<br />
Example: `\![set,zorder,back,3]` displays `\p[3]` behind all other characters.<br />
When multiple scope IDs are specified, they are arranged from front to back in the order written. `front` and `back` can be written consecutively.<br />
Example: `\![set,zorder,front,1,0,back,3,2]` arranges them from front to back as `\1`, `\0`, (all other characters), `\p[3]`, `\p[2]`.

When `front` or `back` is specified, the other characters are arranged with lower scope IDs closer to the front.<br />
`front` and `back` can each be executed multiple times. Each execution appends its IDs to the end of the respective list. Specifying an already specified scope ID again moves it to the new position. An ID cannot be specified in both the front and back lists; the later specification takes precedence.<br />
As with the syntax that lists only scope IDs, balloons are placed in front of the foremost character.<br />
`front` and `back` cannot be combined with the scope-ID-only syntax or the s,b syntax. The syntax used by the later execution takes precedence, and the previous specification is discarded.

Effective until the ghost exits.

**対応:** SSP 2.3.77/2.7.34 (s,b syntax)/2.9.35 (front,back syntax)

## 記述例

```sakurascript
\![set,zorder,1,0]相方側が、必ず本体側の手前に表示される。
```
