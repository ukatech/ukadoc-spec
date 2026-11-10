# sakura.defaultx,X 座標

**カテゴリ:** descript.txt

本體側(`\0`)預設位置的 X 座標。將 surface 的基準點(通常是 surface 的中央下方)放在此位置。\[2.9.13\]<br />
值的格式與意義(單位、座標系、負值、--的處理方式、無效的條件)與 SHIORI 資源的[sakura.defaultx](../../../list/shiori-resource/ghost/sakura.defaultx.md)相同。<br />
優先順序為 SHIORI 資源＞[shell 側的descript.txt](../../shell/descript-txt/sakura.defaultx.md)＞ghost 側的descript.txt。<br />
同一個 descript.txt 也有記載[sakura.defaultleft](sakura.defaultleft.md)時，則以此項目(defaultx)為優先。

**既定値:** 無值(本體側會放在主要螢幕工作區的右下角)

**対応:** SSP
