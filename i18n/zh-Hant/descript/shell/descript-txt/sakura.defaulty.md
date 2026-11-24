# sakura.defaulty,Y 座標

**カテゴリ:** descript.txt

本體側（`\0`）預設位置的 Y 座標。將 surface 的基準點（通常為 surface 的中央下方）置於此位置。\[2.9.13\]<br />
值的格式與意義（單位、座標系、負值、-- 的處理方式及失效條件）與 SHIORI 資源的 [sakura.defaulty](../../../list/shiori-resource/ghost/sakura.defaulty.md) 相同。<br />
優先順序為 SHIORI 資源＞shell 端的 descript.txt（此項）＞ghost 端的 descript.txt。<br />
若同一個 descript.txt 中也寫有 [sakura.defaulttop](sakura.defaulttop.md)，則優先使用此項（defaulty）。

也可以寫在 ghost 端的 descript.txt 中。若 shell 端有設定，則優先使用 shell 端的值；否則使用 ghost 端的值。

**既定値:** 無值（本體側置於工作區域的下邊緣）

**対応:** SSP
