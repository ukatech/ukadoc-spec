# vertical,0/1

**カテゴリ:** descript.txt

指定1時，此 balloon 的文字會以日文直書方式顯示（文字由上往下排列，行由右往左排列）。

設定直書後，descript.txt 中座標指定的意義會如下變更。座標本身仍與以往相同，以 balloon 影像左上角為原點。

- origin.x … *第1列的右端*。列會從此處開始往左延伸。通常不指定，而是交由 validrect 定義。
- origin.y … 字元排列的起始位置（第1個字元的上端）。通常不指定，而是交由 validrect 定義。
- validrect … 不變。文字可繪製的範圍。
- 換行位置以[wordwrappoint.y](wordwrappoint.y.md)指定。wordwrappoint.x會被忽略。
- SSTP 訊息的顯示結束位置以[sstpmessage.yb](sstpmessage.yb.md)指定。sstpmessage.xr會被忽略。
- [number.y](number.y.md)（＝number.yb） … 計數器數值的*底端*。數值會從此處往上延伸。[number.x](number.x.md)（＝number.xr）則是數值所在列的位置。

如 origin.x 或 number.x 等以右端為基準的座標，可依[\*1](../index.md#balloon設定)的規則使用負值指定（例如：origin.x,-14 表示從 balloon 影像右端往左14像素）。

指定的字型會自動改用其直書異體字型（字型名稱前加上@）。<br />
如果指定的字型沒有直書異體字型（例如放在 balloon 資料夾中的字型檔案或西文字型），則會自動替換為環境標準 Gothic 字型的直書異體字型。

另請注意，下列項目會依據「文字排列方向」而非「畫面上的方向」運作。

- `\f[align,～]`會設定列內的文字對齊方式（left＝靠上、right＝靠下），`\f[valign,～]`則會設定行厚度方向的對齊方式（top＝靠右、bottom＝靠左）。
- arrow0（向上捲動）・arrow1（向下捲動）實際上分別表示向右、向左捲動。請在 balloon 端準備圖像和位置。
- 底線（font.underline、`\f[underline,true]`、錨點底線）會畫在列的右側。

限制：SSTP 標記的傳送來源顯示和網路更新進度顯示也會以直書繪製。輸入框（communicatebox）仍為橫書。

也可以在 balloon 各 surface 的設定檔[balloon(s/k)\*s.txt](../balloonsoption/index.md)中指定，但若在同一個 balloon 中依 surface 切換直書和橫書，切換前顯示的文字版面會錯亂。

**既定値:** 0（橫書）

**対応:** SSP 2.8.80
