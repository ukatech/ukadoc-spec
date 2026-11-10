# sakura.defaultleft,X 座標

**カテゴリ:** descript.txt

設定本體端（`\0`）的預設位置 X 座標。將角色視窗左端置於此位置。<br />
數值格式和意義（單位、座標系、負值、-- 的處理方式、失效條件）與 SHIORI 資源的 [sakura.defaultleft](../../../list/shiori-resource/ghost/sakura.defaultleft.md) 相同。負值表示距離右端的邊界間距。\[2.9.13\]<br />
優先順序為 SHIORI 資源＞shell 端的 descript.txt（此項目）＞[ghost 端的 descript.txt](../../ghost/descript-txt/sakura.defaultleft.md)。若同一個 descript.txt 也設定了 [sakura.defaultx](sakura.defaultx.md)，則以該設定為優先。

**既定値:** ghost 的 descript 設定

**対応:** SSP
