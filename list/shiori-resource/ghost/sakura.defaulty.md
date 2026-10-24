# sakura.defaulty

**カテゴリ:** ゴースト情報

本体側(`\0`)の既定位置のY座標。サーフェスの基準点(通常はサーフェスの中央下)をこの位置に置く。<br />
既定位置が使われる場面と、値の単位・座標系は[sakura.defaultx](sakura.defaultx.md)と同じ。<br />
負の値は、プライマリモニタの作業領域の下端からの距離になる。-0は下端そのもの。ここでの下端は、SSPの設定の「デスクトップ下端オフセット」の分だけ上にずらした位置。\[2.9.13\]<br />
-を2つ重ねると負の座標そのものになる(--100はY座標-100)。\[2.9.13\]<br />
同じ軸に[sakura.defaulttop](sakura.defaulttop.md)も指定されている場合は、こちら(defaulty)が優先される。<br />
[ゴースト](../../../descript/ghost/descript-txt/sakura.defaulty.md)・[シェル](../../../descript/shell/descript-txt/sakura.defaulty.md)のdescript.txtにも同じ項目を書ける\[2.9.13\]。SHIORIリソースのほうが優先される。<br />
デスクトップの上端/下端に沿って表示する設定のときは、Y座標はその設定で決まるため無効(自由移動モードなどのときに有効)。

**対応:** SSP
