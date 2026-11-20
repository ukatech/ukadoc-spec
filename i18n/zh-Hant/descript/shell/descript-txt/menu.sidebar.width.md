# menu.sidebar.width,數值

**カテゴリ:** descript.txt

owner draw 選單中側邊欄的寬度（像素）。0 視為未指定。<br />
若指定的值大於側邊欄圖片（[menu.sidebar.bitmap.filename](menu.sidebar.bitmap.filename.md)），多餘的部分會以 [menu.sidebar.color](menu.sidebar.color.md) 填滿。若沒有圖片和 [menu.sidebar.text](menu.sidebar.text.md)，僅指定此值，則會顯示指定寬度、只有顏色的側邊欄。

也可以寫在 ghost 的 descript.txt 中。若 shell 中有設定，則優先使用 shell 的值；否則使用 ghost 的值。

**既定値:** 側邊欄圖片的寬度（若沒有圖片，只有 [menu.sidebar.text](menu.sidebar.text.md)，則為配合文字高度的寬度）

**対応:** SSP
