# `\![set,sticky-window,スコープID,スコープID,...]`

**カテゴリ:** surface 命令

使指定 scope 的窗口在拖动过程中或执行 move 标签时成组移动。<br />
例如指定1,0后，执行鼠标拖动等操作时，`\0`(相方側)和`\1`(本体側)窗口会一起移动。

多次执行此标签并指定不同的 scope ID，可以建立多个组。<br />
例如：执行`\![set,sticky-window,1,0]` `\![set,sticky-window,3,2]`后，`\1`和`\0`组成一组，`\p[3]`和`\p[2]`组成一组。

可指定的 scope ID 数量没有限制，但指定过多会**显著**降低性能，因此建议指定2～3个。<br />
执行包含已配对 scope ID 的标签时会出错。若要更改组合，请先使用`\![reset]`标签，再重新设置。

如果通过`\![set,alignmenttodesktop]`等限制了窗口位置，则优先遵循该限制，只有X、Y中可自由移动的方向会跟随。<br />
即使通过`\![move]`标签移动组内某个窗口，其他窗口也会跟随。<br />
但可通过 move 标签的 --option=ignore-sticky-window 单独移动窗口。

在 ghost 结束前有效。

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
