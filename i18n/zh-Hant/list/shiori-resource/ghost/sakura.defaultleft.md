# sakura.defaultleft

**カテゴリ:** ghost 資訊

本體側（`\0`）預設位置的 X 座標。將角色視窗的左端放在此位置。<br />
使用預設位置的時機、值的單位、座標系及失效條件皆與 [sakura.defaultx](sakura.defaultx.md) 相同。若也指定了 [sakura.defaultx](sakura.defaultx.md)，則以該項為優先。<br />
負值表示從主要螢幕工作區域的右端到角色右端的距離。-0 會使角色緊貼右端。可不必考慮 surface 的寬度，直接指定與螢幕右端的間距。\[2.9.13\]<br />
連續使用2個 - 時，表示負座標本身（--100 表示 X 座標 -100）。\[2.9.13\]<br />
[ghost](../../../descript/shell/descript-txt/sakura.defaultleft.md) 與 [shell](../../../descript/shell/descript-txt/sakura.defaultleft.md) 的 descript.txt 也可以記載相同項目。SHIORI 資源的設定優先。

**対応:** Materia / SSP / CROW
