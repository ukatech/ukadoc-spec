# seriko.zorder,スコープID,スコープID,...

**カテゴリ:** descript.txt

[`\![set,zorder,スコープID,スコープID,...]`](../../../list/sakura-script/surface/bang-set-zorder-ID-ID.md)のdescript版。タグを実行しなくてもあらかじめ設定できる。

`front`・`back`の記法も使える(SSP 2.9.35以降)。descript.txtは1行しか書けないので、`front`と`back`は同じ行に続けて書く。<br />
例：`seriko.zorder,front,0` → `\0`を最前面にする。<br />
例：`seriko.zorder,back,0,front,2,1` → `\0`を最背面、`\p[2]`・`\p[1]`の順に最前面側へ並べる。

**既定値:** 値なし

**対応:** SSP 2.4/2.9.35(front,back記法)
