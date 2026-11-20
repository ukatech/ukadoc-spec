# menu.foreground.color,顏色

**カテゴリ:** descript.txt

owner draw 選單中，選取項目（游標所在項目）的背景色。選取項目的背景圖片（[menu.foreground.bitmap.filename](menu.foreground.bitmap.filename.md)）未覆蓋的部分（未指定圖片時為整個項目）會以此顏色填滿。<br />
顏色可指定為色名（例如 `red`）、`#RRGGBB` 或 `#RGB`（`#` 可省略）。<br />
也可以在 `menu.foreground.color.r` / `menu.foreground.color.g` / `menu.foreground.color.b` 中填入 0～255 的數值，分別指定紅、綠、藍色。

也可以寫在 ghost 的 descript.txt 中。若 shell 中有設定，則優先使用 shell 的值；否則使用 ghost 的值。

**既定値:** OS 的選取項目（反白）顏色

**対応:** SSP
