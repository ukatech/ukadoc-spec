# sakura.defaultx

**カテゴリ:** ghost 資訊

本體側（`\0`）預設位置的 X 座標。將 surface 的基準點（通常是 surface 的下方中央）置於此位置。<br />
未記錄顯示位置時（例如首次啟動或初始化顯示位置時），會使用預設位置。若均未指定，則會置於主要螢幕工作區域的右下角。<br />
值的單位為像素，使用以主要螢幕左上角為原點的螢幕座標（多螢幕時為虛擬桌面整體中的位置）。<br />
負值表示距離主要螢幕工作區域右邊緣的距離。-0 表示右邊緣本身。\[2.9.13\]<br />
若要直接指定負座標，例如指向主要螢幕左側的螢幕，請如 --100 般連續使用兩個 -（此例為 X 座標 -100）。\[2.9.13\]<br />
若同一軸也指定了 [sakura.defaultleft](sakura.defaultleft.md)，則以此項（defaultx）優先。<br />
[ghost](../../../descript/shell/descript-txt/sakura.defaultx.md) 與 [shell](../../../descript/shell/descript-txt/sakura.defaultx.md) 的 descript.txt 也可寫入相同項目\[2.9.13\]。SHIORI 資源的優先順序較高。<br />
設定為沿桌面左邊緣／右邊緣顯示時，X 座標由該設定決定，因此此項無效。

**対応:** SSP
