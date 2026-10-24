# sakura.defaulttop

**カテゴリ:** ゴースト情報

本体側(`\0`)の既定位置のY座標。キャラクターウィンドウの上端をこの位置に置く。<br />
既定位置が使われる場面と、値の単位・座標系・無効になる条件は[sakura.defaulty](sakura.defaulty.md)と同じ(自由移動モードなどのときに有効)。[sakura.defaulty](sakura.defaulty.md)も指定されている場合はそちらが優先される。<br />
負の値は、プライマリモニタの作業領域の下端から、キャラクターの下端までの距離になる。-0で下端にぴったり付く。ここでの下端は、SSPの設定の「デスクトップ下端オフセット」の分だけ上にずらした位置。\[2.9.13\]<br />
-を2つ重ねると負の座標そのものになる(--100はY座標-100)。\[2.9.13\]<br />
[ゴースト](../../../descript/ghost/descript-txt/sakura.defaulttop.md)・[シェル](../../../descript/shell/descript-txt/sakura.defaulttop.md)のdescript.txtにも同じ項目を書ける。SHIORIリソースのほうが優先される。

**対応:** SSP
