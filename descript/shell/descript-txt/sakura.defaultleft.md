# sakura.defaultleft,X座標

**カテゴリ:** descript.txt

本体側(`\0`)の既定位置のX座標。キャラクターウィンドウの左端をこの位置に置く。<br />
値の書式と意味(単位・座標系・負の値・--の扱い・無効になる条件)は、SHIORIリソースの[sakura.defaultleft](../../../list/shiori-resource/ghost/sakura.defaultleft.md)と同じ。負の値は右端からの余白になる。\[2.9.13\]<br />
優先順位は、SHIORIリソース＞シェル側のdescript.txt(これ)＞[ゴースト側のdescript.txt](../../ghost/descript-txt/sakura.defaultleft.md)。同じdescript.txtに[sakura.defaultx](sakura.defaultx.md)も書かれている場合はそちらが優先される。

**既定値:** ghostのdescript設定

**対応:** SSP
