# sakura.defaulttop,Y座標

**カテゴリ:** descript.txt

本体側(`\0`)の既定位置のY座標。キャラクターウィンドウの上端をこの位置に置く。<br />
値の書式と意味(単位・座標系・負の値・--の扱い・無効になる条件)は、SHIORIリソースの[sakura.defaulttop](../../../list/shiori-resource/ghost/sakura.defaulttop.md)と同じ。負の値は下端からの余白になる。\[2.9.13\]<br />
[seriko.alignmenttodesktop](seriko.alignmenttodesktop.md)がfreeである場合など、上端/下端に沿わない設定のときだけ有効。<br />
優先順位は、SHIORIリソース＞シェル側のdescript.txt(これ)＞[ゴースト側のdescript.txt](../../ghost/descript-txt/sakura.defaulttop.md)。同じdescript.txtに[sakura.defaulty](sakura.defaulty.md)も書かれている場合はそちらが優先される。

**既定値:** ghostのdescript設定

**対応:** SSP
