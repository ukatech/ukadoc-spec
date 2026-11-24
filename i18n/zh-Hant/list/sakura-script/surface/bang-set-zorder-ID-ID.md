# `\![set,zorder,スコープID,スコープID,...]`

**カテゴリ:** surface 指令

將指定 scope 的視窗從左到右依序排列在較前方。<br />
例：指定 `\![set,zorder,1,0]` 時，`\1` 一定會顯示在 `\0` 視窗的前方。

若要同時控制 balloon 的 Z 順序，請參照以下範例。<br />
例：`\![set,zorder,balloon1,surface1,balloon0,surface0]`<br />
例（省略寫法）：!\[set,zorder,b1,s1,b0,s0\]<br />
指定後，會嚴格依照 `\1` 的 balloon、`\1` 的立繪、`\0` 的 balloon、`\0` 的立繪的順序排列。

多次執行各自包含不同 scope ID 的標籤，可建立多個群組。<br />
例：執行 `\![set,zorder,1,0]` `\![set,zorder,3,2]` 時，`\1` 會顯示在 `\0` 前方，`\p[3]` 會顯示在 `\p[2]` 前方。<br />
同時指定 balloon 的寫法也一樣。

可指定的 scope ID 數量沒有限制，但指定大量 ID 會稍微影響效能，建議使用 2～3 個左右。<br />
執行包含已配對 scope ID 的標籤會發生錯誤。若要變更組合，請先使用 `\![reset]` 標籤再重新設定。

若只想將特定角色置於最前方或最後方，請在 scope ID 前加上 `front` 或 `back`。如此一來，角色眾多的 ghost 就不必列舉所有角色。<br />
例：指定 `\![set,zorder,front,0]` 時，`\0` 會顯示在所有其他角色的前方。<br />
例：指定 `\![set,zorder,back,3]` 時，`\p[3]` 會顯示在所有其他角色的後方。<br />
指定多個 scope ID 時，會依照指定順序由前往後排列。`front` 和 `back` 可連續指定。<br />
例：指定 `\![set,zorder,front,1,0,back,3,2]` 時，由前往後依序為 `\1`、`\0`、（其他角色）、`\p[3]`、`\p[2]`。

指定 `front` 或 `back` 時，其他角色會依 scope ID 由小到大的順序由前往後排列。<br />
`front` 和 `back` 也可各自分多次執行，並依執行順序分別加入末尾。再次指定已指定的 scope ID 時，該角色會移至新位置。無法同時指定在前方和後方，會以後指定的位置為準。<br />
與僅列出 scope ID 的寫法相同，balloon 會排列在最前方角色的前面。<br />
`front`、`back` 無法與僅列出 scope ID 的寫法或 s,b 寫法併用。會切換為後執行的寫法，並捨棄先前的設定。

有效至 ghost 結束為止。

**対応:** SSP 2.3.77/2.7.34(s,b 寫法)/2.9.35(front,back 寫法)

## 記述例

```sakurascript
\![set,zorder,1,0]相方側が、必ず本体側の手前に表示される。
```
