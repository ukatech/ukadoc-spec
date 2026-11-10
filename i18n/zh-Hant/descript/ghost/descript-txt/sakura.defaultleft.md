# sakura.defaultleft,X 座標

**カテゴリ:** descript.txt

本體側(`\0`)預設位置的 X 座標。將角色視窗的左端放在此位置。<br />
值的格式與意義(單位、座標系、負值、--的處理方式、無效的條件)與 SHIORI 資源的[sakura.defaultleft](../../../list/shiori-resource/ghost/sakura.defaultleft.md)相同。負值表示距離右端的留白。\[2.9.13\]<br />
優先順序為 SHIORI 資源＞[shell 側的descript.txt](../../shell/descript-txt/sakura.defaultleft.md)＞ghost 側的descript.txt。同一個 descript.txt 也有記載[sakura.defaultx](sakura.defaultx.md)時，則以該項目為優先。

**既定値:** 無值(本體側會放在主要螢幕工作區的右下角)

**対応:** SSP
