# sakura.defaulttop

**カテゴリ:** ghost 資訊

本體側（`\0`）預設位置的 Y 座標。將角色視窗的上端放在此位置。<br />
使用預設位置的時機、值的單位、座標系及失效條件皆與 [sakura.defaulty](sakura.defaulty.md) 相同（在自由移動模式等情況下有效）。若也指定了 [sakura.defaulty](sakura.defaulty.md)，則以該項為優先。<br />
負值表示從主要螢幕工作區域的下端到角色下端的距離。-0 會使角色緊貼下端。此處的下端是依 SSP 設定中的「桌面下端偏移量」向上移動後的位置。\[2.9.13\]<br />
連續使用2個 - 時，表示負座標本身（--100 表示 Y 座標 -100）。\[2.9.13\]<br />
[ghost](../../../descript/shell/descript-txt/sakura.defaulttop.md) 與 [shell](../../../descript/shell/descript-txt/sakura.defaulttop.md) 的 descript.txt 也可以記載相同項目。SHIORI 資源的設定優先。

**対応:** SSP
