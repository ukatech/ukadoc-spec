# `\![set,zorder,スコープID,スコープID,...]`

**カテゴリ:** Surface command

Places the windows of the specified scopes from front to back in the order listed from left to right.<br />
Example: `\![set,zorder,1,0]` ensures that `\1` is displayed in front of the `\0` window.

To control the Z-order of balloons as well, follow the examples below.<br />
Example: `\![set,zorder,balloon1,surface1,balloon0,surface0]`<br />
Example (abbreviated notation): !\[set,zorder,b1,s1,b0,s0\]<br />
This strictly controls the order as follows: `\1` balloon, `\1` character image, `\0` balloon, `\0` character image.

Multiple groups can be created by executing tags with different scope IDs.<br />
Example: Executing `\![set,zorder,1,0]` and `\![set,zorder,3,2]` displays `\1` in front of `\0`, and `\p[3]` in front of `\p[2]`.<br />
The same applies to notation that includes balloons.

There is no limit on the number of scope IDs that can be specified, but specifying many can affect performance, so approximately 2–3 are recommended.<br />
Executing a tag that contains a scope ID already paired with another results in an error. To change the grouping, use the `\![reset]` tag and try again.

To place only certain characters at the very front or back, add `front` or `back` before the scope IDs. This avoids listing every character in a ghost with many characters.<br />
Example: `\![set,zorder,front,0]` displays `\0` in front of all other characters.<br />
Example: `\![set,zorder,back,3]` displays `\p[3]` behind all other characters.<br />
When multiple scope IDs are specified, they are arranged from front to back in the order listed. `front` and `back` can be specified together.<br />
Example: `\![set,zorder,front,1,0,back,3,2]` arranges them from front to back as `\1`, `\0`, (all other characters), `\p[3]`, and `\p[2]`.

When `front` or `back` is specified, all other characters are arranged with smaller scope IDs closer to the front.<br />
`front` and `back` can each be specified in multiple executions. The IDs are appended to the end of their respective lists in execution order. Specifying an already specified scope ID again moves it to the new position. An ID cannot be specified in both the front and back lists; the later specification takes precedence.<br />
As with the notation that lists only scope IDs, balloons are arranged in front of the foremost character.<br />
`front` and `back` cannot be combined with the notation that lists only scope IDs or with s,b notation. The most recently executed notation takes effect, and the previous specification is discarded.

Effective until the ghost exits.

**対応:** SSP 2.3.77/2.7.34(s,b notation)/2.9.35(front,back notation)

## 記述例

```sakurascript
\![set,zorder,1,0]相方側が、必ず本体側の手前に表示される。
```
