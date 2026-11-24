# menu.background.color,顏色

**カテゴリ:** descript.txt

owner draw 選單中，一般狀態下項目的背景色。背景圖片（[menu.background.bitmap.filename](menu.background.bitmap.filename.md)）未覆蓋的部分（未指定圖片時為整個項目）會填入此顏色。<br />
顏色可指定為顏色名稱（例如 `red`）、`#RRGGBB` 或 `#RGB`（可省略 `#`）。<br />
也可以在 `menu.background.color.r` / `menu.background.color.g` / `menu.background.color.b` 中填入 0～255 的數值，分別指定紅、綠、藍。

也可以寫在 ghost 端的 descript.txt 中。若 shell 端有設定，則優先使用 shell 端的值；否則使用 ghost 端的值。

**既定値:** OS 的選單顏色

**対応:** SSP
