# seriko.zorder,scope ID,scope ID,...

**カテゴリ:** descript.txt

[`\![set,zorder,スコープID,スコープID,...]`](../../../list/sakura-script/surface/bang-set-zorder-ID-ID.md)的 descript 版本。無須執行標籤即可預先設定。

也可使用 `front`、`back` 寫法（SSP 2.9.35 以後）。descript.txt 只能寫一行，因此須將 `front` 和 `back` 接續寫在同一行。<br />
範例：`seriko.zorder,front,0` → 將 `\0` 置於最前方。<br />
範例：`seriko.zorder,back,0,front,2,1` → 將 `\0` 置於最後方，並依 `\p[2]`、`\p[1]` 的順序排列於最前方。

**既定値:** 無值

**対応:** SSP 2.4/2.9.35（front,back 寫法）
