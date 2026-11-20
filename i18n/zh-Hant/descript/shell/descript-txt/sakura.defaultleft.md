# sakura.defaultleft,X座標

**カテゴリ:** descript.txt

本體側（`\0`）預設位置的 X 座標。將角色視窗的左緣放在此位置。<br />
值的格式與意義（單位、座標系、負值、-- 的處理方式及失效條件）與 SHIORI 資源的 [sakura.defaultleft](../../../list/shiori-resource/ghost/sakura.defaultleft.md) 相同。負值表示距右緣的邊距。\[2.9.13\]<br />
優先順序為 SHIORI 資源＞shell 側的 descript.txt（此項）＞ghost 側的 descript.txt。若同一個 descript.txt 也記載了 [sakura.defaultx](sakura.defaultx.md)，則優先使用該值。

也可以寫在 ghost 側的 descript.txt。若 shell 側有記載，則優先使用 shell 側的值；否則使用 ghost 側的值。

**既定値:** 無值（本體側放置於主要螢幕工作區域的右下角）

**対応:** SSP
