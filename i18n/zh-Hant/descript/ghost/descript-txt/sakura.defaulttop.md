# sakura.defaulttop,Y 座標

**カテゴリ:** descript.txt

本體側（`\0`）預設位置的 Y 座標。將角色視窗的上緣置於此位置。<br />
值的格式與意義（單位、座標系、負值、-- 的處理方式、失效條件）與 SHIORI 資源的 [sakura.defaulttop](../../../list/shiori-resource/ghost/sakura.defaulttop.md) 相同。負值表示距離下緣的邊距。\[2.9.13\]<br />
僅在設定不沿著上緣／下緣等情況下有效，例如 [seriko.alignmenttodesktop](seriko.alignmenttodesktop.md) 為 free 時。<br />
優先順序為 SHIORI 資源＞[shell 的 descript.txt](../../shell/descript-txt/sakura.defaulttop.md)＞ghost 的 descript.txt。若同一個 descript.txt 也有寫入 [sakura.defaulty](sakura.defaulty.md)，則以該設定為優先。

**既定値:** 無值（本體側會置於工作區域的下緣）

**対応:** SSP
