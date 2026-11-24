# menu.sidebar.color,顏色

**カテゴリ:** descript.txt

owner draw 選單側邊欄的背景色。側邊欄圖片（[menu.sidebar.bitmap.filename](menu.sidebar.bitmap.filename.md)）未覆蓋的部分會填入此顏色。沒有側邊欄圖片，且只指定 [menu.sidebar.text](menu.sidebar.text.md) 或 [menu.sidebar.width](menu.sidebar.width.md) 時，整個側邊欄會填入此顏色。<br />
顏色可指定為顏色名稱（例如 `red`）、`#RRGGBB` 或 `#RGB`（可省略 `#`）。<br />
也可以在 `menu.sidebar.color.r` / `menu.sidebar.color.g` / `menu.sidebar.color.b` 中填入 0～255 的數值，分別指定紅、綠、藍。

也可以寫在 ghost 端的 descript.txt 中。若 shell 端有設定，則優先使用 shell 端的值；否則使用 ghost 端的值。

**既定値:** 與 [menu.foreground.color](menu.foreground.color.md) 相同的顏色

**対応:** SSP
