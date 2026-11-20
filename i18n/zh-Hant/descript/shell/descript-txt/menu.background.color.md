# menu.background.color,顏色

**カテゴリ:** descript.txt

owner draw 選單中，一般狀態項目的背景色。背景圖片（[menu.background.bitmap.filename](menu.background.bitmap.filename.md)）未覆蓋的部分（未指定圖片時為整個項目）會以此顏色填滿。<br />
顏色可指定為色名（例如 `red`）、`#RRGGBB` 或 `#RGB`（可省略 `#`）。<br />
也可在 `menu.background.color.r` / `menu.background.color.g` / `menu.background.color.b` 中填入 0～255 的數值，分別指定紅、綠、藍。

也可寫在 ghost 側的 descript.txt 中。若 shell 側有設定，則優先使用 shell 側的值；否則使用 ghost 側的值。

**既定値:** OS 的選單顏色

**対応:** SSP
