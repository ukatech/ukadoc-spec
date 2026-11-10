# `\![set,sticky-window,スコープID,スコープID,...]`

**カテゴリ:** Surface command

Make the windows for the specified scopes move together while being dragged or while a move tag is running.<br />
For example, specifying 1,0 makes the `\0` (kero) and `\1` (sakura) windows move together when dragged or moved by other means.

You can create multiple groups by running the tag multiple times with different scope IDs.<br />
Example: Running `\![set,sticky-window,1,0]` and `\![set,sticky-window,3,2]` groups `\1` with `\0`, and `\p[3]` with `\p[2]`.

There is no limit to the number of scope IDs you can specify, but specifying **a lot** of them will significantly affect performance, so 2–3 is recommended.<br />
Running a tag that includes scope IDs already in a pair causes an error. To change the combinations, use the `\![reset]` tag before trying again.

If window position is constrained by `\![set,alignmenttodesktop]` or a similar tag, that constraint takes precedence, and only the freely movable axis of X and Y follows.<br />
Moving one of the grouped windows with the `\![move]` tag also moves the other windows in the group.<br />
However, the --option=ignore-sticky-window option of the move tag allows a window to move independently.

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
