# sakura.defaulty

**カテゴリ:** ghost 資訊

本體側（`\0`）預設位置的 Y 座標。將 surface 的基準點（通常是 surface 的下方中央）置於此位置。<br />
使用預設位置的時機、值的單位及座標系統皆與 [sakura.defaultx](sakura.defaultx.md) 相同。<br />
負值表示距離主要螢幕工作區域下邊緣的距離。-0 表示下邊緣本身。此處的下邊緣是依 SSP 設定中的「桌面下邊緣偏移量」向上偏移後的位置。\[2.9.13\]<br />
連續使用兩個 - 即表示負座標本身（--100 為 Y 座標 -100）。\[2.9.13\]<br />
若同一軸也指定了 [sakura.defaulttop](sakura.defaulttop.md)，則以此項（defaulty）優先。<br />
[ghost](../../../descript/shell/descript-txt/sakura.defaulty.md) 與 [shell](../../../descript/shell/descript-txt/sakura.defaulty.md) 的 descript.txt 也可寫入相同項目\[2.9.13\]。SHIORI 資源的優先順序較高。<br />
設定為沿桌面上邊緣／下邊緣顯示時，Y 座標由該設定決定，因此此項無效（在自由移動模式等情況下有效）。

**対応:** SSP
