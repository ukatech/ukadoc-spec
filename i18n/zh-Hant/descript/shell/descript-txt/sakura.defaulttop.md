# sakura.defaulttop,Y座標

**カテゴリ:** descript.txt

本體側（`\0`）預設位置的 Y 座標。將角色視窗的上緣放在此位置。<br />
值的格式與意義（單位、座標系、負值、-- 的處理方式及失效條件）與 SHIORI 資源的 [sakura.defaulttop](../../../list/shiori-resource/ghost/sakura.defaulttop.md) 相同。負值表示距下緣的邊距。\[2.9.13\]<br />
僅在設定為不沿上緣或下緣排列時有效，例如 [seriko.alignmenttodesktop](seriko.alignmenttodesktop.md) 為 free 時。<br />
優先順序為 SHIORI 資源＞shell 側的 descript.txt（此項）＞ghost 側的 descript.txt。若同一個 descript.txt 也記載了 [sakura.defaulty](sakura.defaulty.md)，則優先使用該值。

也可以寫在 ghost 側的 descript.txt。若 shell 側有記載，則優先使用 shell 側的值；否則使用 ghost 側的值。

**既定値:** 無值（本體側放置於工作區域的下緣）

**対応:** SSP
