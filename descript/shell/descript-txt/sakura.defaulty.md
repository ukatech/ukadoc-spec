# sakura.defaulty,Y座標

**カテゴリ:** descript.txt

本体側(`\0`)の既定位置のY座標。サーフェスの基準点(通常はサーフェスの中央下)をこの位置に置く。\[2.9.13\]<br />
値の書式と意味(単位・座標系・負の値・--の扱い・無効になる条件)は、SHIORIリソースの[sakura.defaulty](../../../list/shiori-resource/ghost/sakura.defaulty.md)と同じ。<br />
優先順位はSHIORIリソース＞シェル側のdescript.txt(これ)＞ゴースト側のdescript.txt。<br />
同じdescript.txtに[sakura.defaulttop](sakura.defaulttop.md)も書かれている場合は、こちら(defaulty)が優先される。

ゴースト側のdescript.txtにも書ける。シェル側に書かれていればシェル側が優先され、書かれていなければゴースト側の値が使われる。

**既定値:** 値なし(本体側は作業領域の下端に置かれる)

**対応:** SSP
