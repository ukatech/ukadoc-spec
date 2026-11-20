# menu.sidebar.color,顏色

**カテゴリ:** descript.txt

owner draw 選單中側邊欄的背景色。側邊欄圖片（[menu.sidebar.bitmap.filename](menu.sidebar.bitmap.filename.md)）未覆蓋的部分會以此顏色填滿。若沒有側邊欄圖片，僅指定 [menu.sidebar.text](menu.sidebar.text.md) 或 [menu.sidebar.width](menu.sidebar.width.md)，則整個側邊欄會以此顏色填滿。<br />
顏色可指定為色名（例如 `red`）、`#RRGGBB` 或 `#RGB`（`#` 可省略）。<br />
也可以在 `menu.sidebar.color.r` / `menu.sidebar.color.g` / `menu.sidebar.color.b` 中填入 0～255 的數值，分別指定紅、綠、藍色。

也可以寫在 ghost 的 descript.txt 中。若 shell 中有設定，則優先使用 shell 的值；否則使用 ghost 的值。

**既定値:** 與 [menu.foreground.color](menu.foreground.color.md) 相同的顏色

**対応:** SSP
