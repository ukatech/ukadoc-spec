# seriko.zorder,scope ID,scope ID,...

**カテゴリ:** descript.txt

[`\![set,zorder,スコープID,スコープID,...]`](../../../list/sakura-script/surface/bang-set-zorder-ID-ID.md) 的 descript 版。無須執行標籤即可預先設定。

也可使用 `front`、`back` 的寫法（SSP 2.9.35 以後）。由於 descript.txt 只能寫一行，`front` 和 `back` 須接續寫在同一行。<br />
例：`seriko.zorder,front,0` → 將 `\0` 置於最前面。<br />
例：`seriko.zorder,back,0,front,2,1` → 將 `\0` 置於最後面，並依 `\p[2]`、`\p[1]` 的順序排列在最前面。

也可寫在 ghost 側的 descript.txt。若 shell 側有指定，則優先使用 shell 側的值；否則使用 ghost 側的值。

**既定値:** 無值

**対応:** SSP 2.4/2.9.35（front,back 寫法）
