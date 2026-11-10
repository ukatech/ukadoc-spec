# `\![set,sticky-window,スコープID,スコープID,...]`

**カテゴリ:** Surface command

Make the specified scope windows move together while being dragged or while a move tag is executing.<br />
For example, specifying 1,0 makes the `\0` (kero) and `\1` (sakura) windows move together when dragged with the mouse or otherwise moved.

Running this tag multiple times with different scope IDs creates multiple groups.<br />
Example: Running `\![set,sticky-window,1,0]` and `\![set,sticky-window,3,2]` makes `\1` and `\0` move together, and `\p[3]` and `\p[2]` move together.

There is no limit to the number of scope IDs that can be specified, but specifying a large number makes it **considerably** slower, so 2–3 is recommended.<br />
Running a tag that includes a scope ID already in a pair causes an error. To change the combinations, use the `\![reset]` tag before trying again.

If window positions are constrained by `\![set,alignmenttodesktop]` or a similar tag, those constraints take priority, and only the unconstrained X and/or Y coordinates follow.<br />
Moving one of the windows grouped by the `\![move]` tag also moves the other windows in the group.<br />
However, the --option=ignore-sticky-window option of the move tag allows a window to move independently.

Valid until the ghost ends.

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
