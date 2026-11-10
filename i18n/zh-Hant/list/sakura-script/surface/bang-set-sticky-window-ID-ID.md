# `\![set,sticky-window,スコープID,スコープID,...]`

**カテゴリ:** surface 指令

讓指定 scope 的視窗在拖曳或執行 move 標籤時一起移動。<br />
例如指定 1,0 時，執行滑鼠拖曳移動等操作後，`\0`(夥伴側)與`\1`(本體側)的視窗會一起移動。

多次執行 scope ID 不同的標籤時，可以建立多個群組。<br />
例：執行 `\![set,sticky-window,1,0]` `\![set,sticky-window,3,2]` 後，`\1`與`\0`會成為一組，`\p[3]`與`\p[2]`會成為一組。

可指定的 scope ID 數量沒有限制，但指定大量 ID 會讓效能**大幅**降低，因此建議指定 2～3 個。<br />
執行包含已配對 scope ID 的標籤會發生錯誤。若要變更配對方式，請先使用`\![reset]`標籤，再重新設定。

若使用`\![set,alignmenttodesktop]`等設定了視窗位置限制，會優先套用該限制，只有 X,Y 中可自由移動的方向會跟著移動。<br />
即使移動以`\![move]`標籤群組化的視窗之一，其他視窗也會跟著移動。<br />
不過，move 標籤的 --option=ignore-sticky-window 可讓視窗單獨移動。

此設定在 ghost 結束前有效。

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
