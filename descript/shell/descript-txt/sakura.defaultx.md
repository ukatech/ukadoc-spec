# sakura.defaultx,X座標

**カテゴリ:** descript.txt

本体側(`\0`)の既定位置のX座標。サーフェスの基準点(通常はサーフェスの中央下)をこの位置に置く。\[2.9.13\]<br />
値の書式と意味(単位・座標系・負の値・--の扱い・無効になる条件)は、SHIORIリソースの[sakura.defaultx](../../../list/shiori-resource/ghost/sakura.defaultx.md)と同じ。<br />
優先順位は、SHIORIリソース＞シェル側のdescript.txt(これ)＞[ゴースト側のdescript.txt](../../ghost/descript-txt/sakura.defaultx.md)。<br />
同じdescript.txtに[sakura.defaultleft](sakura.defaultleft.md)も書かれている場合は、こちら(defaultx)が優先される。

**既定値:** ghostのdescript設定

**対応:** SSP
