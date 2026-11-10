# sakura.defaulty,Y 座標

**カテゴリ:** descript.txt

本體側(`\0`)預設位置的 Y 座標。將 surface 的基準點（通常是 surface 的底部中央）置於此位置。\[2.9.13\]<br />
值的格式與意義（單位、座標系、負值、-- 的處理方式、無效的條件）與 SHIORI 資源的[sakura.defaulty](../../../list/shiori-resource/ghost/sakura.defaulty.md)相同。<br />
優先順序為 SHIORI 資源＞[shell 端的 descript.txt](../../shell/descript-txt/sakura.defaulty.md)＞ghost 端的 descript.txt。<br />
若同一個 descript.txt 也寫有[sakura.defaulttop](sakura.defaulttop.md)，則此項（defaulty）優先。

**既定値:** 無值（本體側會置於工作區域的下緣）

**対応:** SSP
