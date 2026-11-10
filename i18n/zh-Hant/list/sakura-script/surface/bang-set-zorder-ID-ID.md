# `\![set,zorder,スコープID,スコープID,...]`

**カテゴリ:** 表面指令

將指定 scope 的視窗依序由左至右排列在前方。<br />
例如：指定 `\![set,zorder,1,0]` 時，`\1` 一定會顯示在 `\0` 視窗前方。

若要一併控制 balloon 的 Z 順序，請參照以下範例。<br />
例如：`\![set,zorder,balloon1,surface1,balloon0,surface0]`<br />
例如（省略寫法）：!\[set,zorder,b1,s1,b0,s0\]<br />
指定此項目後，會嚴格依照 `\1` 的 balloon - `\1` 的立繪 - `\0` 的 balloon - `\0` 的立繪順序控制。

分別多次執行包含不同 scope ID 的標籤，即可建立多個群組。<br />
例如：執行 `\![set,zorder,1,0]` `\![set,zorder,3,2]` 時，`\1` 會顯示在 `\0` 前方，`\p[3]` 會顯示在 `\p[2]` 前方。<br />
包含 balloon 的寫法也相同。

可指定的 scope ID 數量沒有限制，但指定大量 ID 會稍微變慢，因此建議指定 2～3 個。<br />
執行包含已配對 scope ID 的標籤時會發生錯誤。若要更改組合，請先使用 `\![reset]` 標籤，再重新設定。

在 ghost 結束前皆有效。

**対応:** SSP 2.3.77/2.7.34（s、b 寫法）

## 記述例

```sakurascript
\![set,zorder,1,0]相方側が、必ず本体側の手前に表示される。
```
