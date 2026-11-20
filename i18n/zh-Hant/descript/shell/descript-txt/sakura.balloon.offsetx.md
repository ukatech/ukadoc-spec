# sakura.balloon.offsetx,座標

**カテゴリ:** descript.txt

本體側 balloon 位置的 X 座標。<br />
在 offsetx / offsety 後面加上代表方向的單一字元，可依 balloon 顯示的位置使用不同的值（僅限 SSP）。

- **offsetx / offsety**: 未指定方向。未記載下列項目時使用的預設值。
- **offsetxl / offsetyl**: 在 shell 左側顯示 balloon 時使用。
- **offsetxr / offsetyr**: 在 shell 右側顯示 balloon 時使用。
- **offsetxc / offsetyc**: 在 shell 頭頂或腳邊顯示 balloon 時使用。這兩種置中顯示的情況共用。
- **offsetxb / offsetyb**: 在 shell 腳邊顯示 balloon 時使用。頭頂和腳邊需要不同的值時使用。

未記載時使用的值如下。X 座標和 Y 座標各自獨立決定。

- **沒有 offsetxb 時**: 依序尋找 offsetxc → offsetx。
- **沒有 offsetxc / offsetxl / offsetxr 時**: 使用 offsetx。

顯示位置由 balloon 的 descript.txt 中的 [windowposition.x](../../balloon/descript-txt/windowposition.x.md)、shell 的 [sakura.balloon.alignment](sakura.balloon.alignment.md)、Sakura Script 的 [`\![set,balloonalign,ID]`](../../../list/sakura-script/balloon-text/bang-set-balloonalign-ID.md) 決定。

**注意正負號。**X 座標的正方向在所有情況下都朝向 shell；顯示於左側時向右為正，顯示於右側時向**左**為正（頭頂和腳邊則向右為正）。Y 座標始終向下為正。<br />
但 0 的位置（基準）依方向而異。左右兩側的基準是 balloon 上緣與 shell 圖片上緣對齊的位置；頭頂的基準是 balloon 下緣與 shell 圖片上緣相接的位置；腳邊的基準是 balloon 上緣與 shell 圖片下緣相接的位置。

也可以寫在 ghost 側的 descript.txt。若 shell 側有記載，則優先使用 shell 側的值；否則使用 ghost 側的值。

**既定値:** 無值

**対応:** Materia / SSP / CROW
