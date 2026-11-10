# sakura.balloon.offsetx,座標

**カテゴリ:** surface brace

僅適用於該 surface 的本體側 balloon 位置 X 座標。<br />
在 offsetx / offsety 後方加上表示方向的 1 個字元，即可根據 balloon 的顯示位置使用不同的值（僅限 SSP）。

- **offsetx / offsety**: 未指定方向。以下項目未設定時使用的預設值。
- **offsetxl / offsetyl**: balloon 顯示在 shell 左側時。
- **offsetxr / offsetyr**: balloon 顯示在 shell 右側時。
- **offsetxc / offsetyc**: balloon 顯示在 shell 頭上或腳下時。共用於兩種置中情況。
- **offsetxb / offsetyb**: balloon 顯示在 shell 腳下時。要讓頭上與腳下使用不同值時使用。

若未設定 offsetxb，則使用 offsetxc；若也未設定，則使用 offsetx。若未設定 offsetxc / offsetxl / offsetxr，則使用 offsetx。X 座標與 Y 座標分別獨立決定。<br />
此處設定的值優先於 shell 的[descript.txt](../../shell/descript-txt/sakura.balloon.offsetx.md)中設定的同名值。

正負號的方向與[descript.txt 的 sakura.balloon.offsetx](../../shell/descript-txt/sakura.balloon.offsetx.md)相同。

**既定値:** 顯示在左右時：使 balloon 的左右端與 surface 的左右端對齊的位置<br />
顯示在頭上或腳下時：surface 的中央

**対応:** Materia / SSP / CROW
