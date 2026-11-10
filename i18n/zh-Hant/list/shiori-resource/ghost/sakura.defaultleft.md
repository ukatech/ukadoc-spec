# sakura.defaultleft

**カテゴリ:** ghost 資訊

本體側（`\0`）預設位置的X座標。將角色視窗左端放置於此位置。<br />
預設位置的使用時機、值的單位與座標系，以及停用條件，皆與[sakura.defaultx](sakura.defaultx.md)相同。若也指定了[sakura.defaultx](sakura.defaultx.md)，則以該項目為優先。<br />
負值表示從主螢幕工作區右端到角色右端的距離。-0會讓角色緊貼右端。可直接指定與螢幕右端的間距，不必考慮surface寬度。\[2.9.13\]<br />
連續使用兩個-會表示負座標本身（--100即X座標-100）。\[2.9.13\]<br />
[ghost](../../../descript/ghost/descript-txt/sakura.defaultleft.md)和[shell](../../../descript/shell/descript-txt/sakura.defaultleft.md)的descript.txt也可設定相同項目。SHIORI資源的設定優先。

**対応:** Materia / SSP / CROW
