# sakura.defaultleft

**カテゴリ:** ゴースト情報

本体側(`\0`)の既定位置のX座標。キャラクターウィンドウの左端をこの位置に置く。<br />
既定位置が使われる場面と、値の単位・座標系・無効になる条件は[sakura.defaultx](sakura.defaultx.md)と同じ。[sakura.defaultx](sakura.defaultx.md)も指定されている場合はそちらが優先される。<br />
負の値は、プライマリモニタの作業領域の右端から、キャラクターの右端までの距離になる。-0で右端にぴったり付く。サーフェスの幅を気にせず、画面右端からの余白として指定できる。\[2.9.13\]<br />
-を2つ重ねると負の座標そのものになる(--100はX座標-100)。\[2.9.13\]<br />
[ゴースト](../../../descript/ghost/descript-txt/sakura.defaultleft.md)・[シェル](../../../descript/shell/descript-txt/sakura.defaultleft.md)のdescript.txtにも同じ項目を書ける。SHIORIリソースのほうが優先される。

**対応:** Materia / SSP / CROW
