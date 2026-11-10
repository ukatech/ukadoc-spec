# sakura.balloon.offsetx,座標

**カテゴリ:** descript.txt

本體端氣球位置的 X 座標。<br />
在 offsetx / offsety 後方加上表示方向的 1 個字元，即可依氣球顯示位置使用不同數值（僅限 SSP）。

- **offsetx / offsety**: 未指定方向。未設定下列項目時使用的預設值。
- **offsetxl / offsetyl**: 氣球顯示在 shell 左側時。
- **offsetxr / offsetyr**: 氣球顯示在 shell 右側時。
- **offsetxc / offsetyc**: 氣球顯示在 shell 上方或下方時。用於兩種置中情況。
- **offsetxb / offsetyb**: 氣球顯示在 shell 下方時。若要讓上方和下方使用不同數值，請使用此設定。

未設定時使用的數值如下。X 座標和 Y 座標各自獨立決定。

- **沒有 offsetxb 時**: 依序尋找 offsetxc → offsetx。
- **沒有 offsetxc / offsetxl / offsetxr 時**: 使用 offsetx。

氣球顯示在哪一側，由氣球的 descript.txt 中的 [windowposition.x](../../balloon/descript-txt/windowposition.x.md)、shell 的 [sakura.balloon.alignment](sakura.balloon.alignment.md)，以及 Sakura Script 的 [`\![set,balloonalign,ID]`](../../../list/sakura-script/balloon-text/bang-set-balloonalign-ID.md) 決定。

**注意正負號。**X 座標的 ＋ 在所有情況下都表示朝 shell 靠近的方向；顯示在左側時，右方為正，顯示在右側時，**左方**為正（上方、下方則是右方為正）。Y 座標的 ＋ 永遠表示下方。<br />
但各方向的 0 位置（基準）不同。左右兩側的基準是氣球上緣與 shell 圖片上緣對齊的位置；上方的基準是氣球下緣接觸 shell 圖片上緣的位置；下方的基準是氣球上緣接觸 shell 圖片下緣的位置。

**既定値:** ghost 的 descript 設定

**対応:** Materia / SSP / CROW
