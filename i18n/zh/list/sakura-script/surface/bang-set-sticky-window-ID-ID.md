# `\![set,sticky-window,スコープID,スコープID,...]`

**カテゴリ:** Surface command

Make the specified scope windows move together while dragging or when a move tag is executed.<br />
For example, specifying 1,0 makes the `\0` (kero) and `\1` (sakura) windows move together when dragged with the mouse or moved by other means.

Multiple groups can be created by executing the tag multiple times with different scope IDs.<br />
Example: executing `\![set,sticky-window,1,0]` and `\![set,sticky-window,3,2]` groups `\1` with `\0`, and `\p[3]` with `\p[2]`.

There is no limit to the number of scope IDs that can be specified, but specifying **too many** will significantly slow things down, so around 2–3 is recommended.<br />
Executing a tag that includes a scope ID already paired with another will cause an error. To change the pairings, first use the `\![reset]` tag and then try again.

If window positions are constrained by `\![set,alignmenttodesktop]` or similar, those constraints take precedence, and only the freely movable coordinates among X and Y will follow.<br />
Even if one window in a group is moved using the `\![move]` tag, the other windows will follow.<br />
However, the --option=ignore-sticky-window option of the move tag allows a window to be moved independently.

Effective until the ghost ends.

**対応:** SSP 2.3.77

## 記述例

```sakurascript
\![set,sticky-window,1,0]相方側が、本体側とセットで動く。
```

```sakurascript
\![set,sticky-window,0,1,2]本体側と相方側と3人目がセットで動く。
```

```sakurascript
\1\![move,40,100,0,0,left.top,left.top]相方側の左上を、本体側の左上に合わせた後、右へ40pixel下へ100pixel移動させる。\![set,sticky-window,1,0]その状態で、相方側と本体側をセットで動くようにする。
```
