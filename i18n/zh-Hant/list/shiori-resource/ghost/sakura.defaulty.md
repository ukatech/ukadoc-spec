# sakura.defaulty

**カテゴリ:** ghost 資訊

本體側(`\0`)預設位置的 Y 座標。將 surface 的基準點（通常是 surface 的底部中央）放在此位置。<br />
預設位置的使用時機、值的單位與座標系皆與[sakura.defaultx](sakura.defaultx.md)相同。<br />
負值表示從主螢幕工作區下緣起算的距離。-0 表示下緣本身。此處的下緣是依 SSP 設定中的「桌面下緣偏移」向上移動後的位置。\[2.9.13\]<br />
連續寫兩個-會指定負的座標值本身（--100 表示 Y 座標 -100）。\[2.9.13\]<br />
若同一軸也指定了[sakura.defaulttop](sakura.defaulttop.md)，則以此項目（defaulty）為優先。<br />
也可以在[ghost](../../../descript/ghost/descript-txt/sakura.defaulty.md)與[shell](../../../descript/shell/descript-txt/sakura.defaulty.md)的 descript.txt 中寫入相同項目\[2.9.13\]。SHIORI Resource 的設定優先。<br />
若設定為沿桌面上緣／下緣顯示，Y 座標會由該設定決定，因此此項目無效（在自由移動模式等情況下有效）。

**対応:** SSP
