# seriko.paint_transparent_region_black,數值

**カテゴリ:** descript.txt

設定影像中顏色為透明色（影像左上角的顏色），但透明度值並非透明的區域如何顯示。<br />
為 0 時，以指定的透明度顯示影像原本的顏色（透明色）。<br />
為 1 時，以黑色取代影像顏色填滿後，再以指定的透明度顯示。<br />
例如，指定 0 並為影像準備全白的 pna 時，影像會原樣顯示，不使用透明色。

也可寫在 ghost 側的 descript.txt。若 shell 側有指定，則優先使用 shell 側的值；否則使用 ghost 側的值。

**既定値:** 未指定（使用 pna 作為透明度的影像，其行為相當於 1；[使用影像本身的 alpha 通道作為透明度的影像](seriko.use_self_alpha.md)，其行為相當於 0）

**対応:** SSP
