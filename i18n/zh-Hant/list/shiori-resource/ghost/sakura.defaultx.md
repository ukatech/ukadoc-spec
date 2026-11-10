# sakura.defaultx

**カテゴリ:** ghost 資訊

本體側(`\0`)預設位置的 X 座標。將 surface 的基準點（通常是 surface 的底部中央）放在此位置。<br />
若沒有已記憶的顯示位置（例如首次啟動時或初始化顯示位置時），便會使用預設位置。若未指定任何項目，則會放在主螢幕工作區的右下角。<br />
值的單位為像素，使用以主螢幕左上角為原點的螢幕座標（多螢幕時，位置以整個虛擬桌面為準）。<br />
負值表示從主螢幕工作區右緣起算的距離。-0 表示右緣本身。\[2.9.13\]<br />
若要指定負的座標值本身，例如指向位於主螢幕左側的螢幕，請連續寫兩個-，例如 --100（此例為 X 座標 -100）。\[2.9.13\]<br />
若同一軸也指定了[sakura.defaultleft](sakura.defaultleft.md)，則以此項目（defaultx）為優先。<br />
也可以在[ghost](../../../descript/ghost/descript-txt/sakura.defaultx.md)與[shell](../../../descript/shell/descript-txt/sakura.defaultx.md)的 descript.txt 中寫入相同項目\[2.9.13\]。SHIORI Resource 的設定優先。<br />
若設定為沿桌面左緣／右緣顯示，X 座標會由該設定決定，因此此項目無效。

**対応:** SSP
