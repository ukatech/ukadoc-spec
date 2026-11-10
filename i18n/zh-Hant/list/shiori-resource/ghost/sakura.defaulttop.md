# sakura.defaulttop

**カテゴリ:** ghost 資訊

本體側(`\0`)預設位置的 Y 座標。將角色視窗的上緣放在此位置。<br />
預設位置的使用時機、值的單位與座標系，以及失效條件皆與[sakura.defaulty](sakura.defaulty.md)相同（在自由移動模式等情況下有效）。若也指定了[sakura.defaulty](sakura.defaulty.md)，則以該項目為優先。<br />
負值表示從主螢幕工作區下緣到角色下緣的距離。-0 會剛好貼齊下緣。此處的下緣是依 SSP 設定中的「桌面下緣偏移」向上移動後的位置。\[2.9.13\]<br />
連續寫兩個-會指定負的座標值本身（--100 表示 Y 座標 -100）。\[2.9.13\]<br />
也可以在[ghost](../../../descript/ghost/descript-txt/sakura.defaulttop.md)與[shell](../../../descript/shell/descript-txt/sakura.defaulttop.md)的 descript.txt 中寫入相同項目。SHIORI Resource 的設定優先。

**対応:** SSP
