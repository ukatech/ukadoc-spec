# `\![set,zorder,スコープID,スコープID,...]`

**カテゴリ:** surface 指令

將指定 scope 的視窗依由左至右的順序排列於前方。<br />
範例：指定 `\![set,zorder,1,0]` 時，`\1` 一定會顯示在 `\0` 視窗前方。

若要連同 balloon 控制 Z 順序，請參照以下範例。<br />
範例：`\![set,zorder,balloon1,surface1,balloon0,surface0]`<br />
範例（簡寫）：!\[set,zorder,b1,s1,b0,s0\]<br />
如此指定後，會嚴格依照 `\1` 的 balloon、`\1` 的立繪、`\0` 的 balloon、`\0` 的立繪之順序控制。

多次執行各自指定不同 scope ID 的標籤，即可建立多個群組。<br />
範例：執行 `\![set,zorder,1,0]` `\![set,zorder,3,2]` 時，`\1` 會顯示在 `\0` 前方，`\p[3]` 會顯示在 `\p[2]` 前方。<br />
連同 balloon 指定的寫法也是如此。

可指定的 scope ID 數量沒有限制，但大量指定會稍微增加負載，建議以 2～3 個左右為宜。<br />
執行包含已配對 scope ID 的標籤會發生錯誤。若要變更組合，請先使用 `\![reset]` 標籤再重新指定。

若只想將特定角色置於最前方或最後方，可在 scope ID 前加上 `front` 或 `back`。對於角色眾多的 ghost，這樣就不必列舉所有角色。<br />
範例：指定 `\![set,zorder,front,0]` 時，`\0` 會顯示在所有其他角色前方。<br />
範例：指定 `\![set,zorder,back,3]` 時，`\p[3]` 會顯示在所有其他角色後方。<br />
若指定多個 scope ID，會依照書寫順序由前至後排列。`front` 和 `back` 可以接續書寫。<br />
範例：指定 `\![set,zorder,front,1,0,back,3,2]` 時，由前至後依序為 `\1`、`\0`、（其他角色）、`\p[3]`、`\p[2]`。

指定 `front` 或 `back` 時，其他角色會依 scope ID 由小至大的順序由前至後排列。<br />
`front` 和 `back` 各自可以分多次執行。項目會依執行順序附加至各自的末尾。若再次指定已指定的 scope ID，該項目會移至新位置。不能同時指定於前方與後方，會採用後指定的位置。<br />
balloon 與僅列出 scope ID 的寫法相同，會排列在最前方角色的前面。<br />
`front`、`back` 不能與僅列出 scope ID 的寫法或 s,b 寫法併用。會切換為後執行的寫法，先前的指定會被捨棄。

有效至 ghost 結束。

**対応:** SSP 2.3.77/2.7.34（s,b 寫法）/2.9.35（front,back 寫法）

## 記述例

```sakurascript
\![set,zorder,1,0]相方側が、必ず本体側の手前に表示される。
```
