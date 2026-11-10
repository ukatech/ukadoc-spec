# balloons\*s.txt/balloonk\*s.txt

## 概要

針對 balloon 的各個 surface（balloons0.png、balloonk0.png、...）及輸入框所設定的個別設定檔。<br />
descript.txt 的設定會作為預設設定；若在此設定相同項目，則只有指定的項目會被覆寫。

每個 surface 可以準備一個設定檔（例如，balloons0.png 對應 balloons0s.txt。請注意檔名結尾的 s）。

原則上所有項目都可以設定，但無法設定與整個 balloon 相關的 name、type、craftman、craftmanurl、id、homeurl、readme（設定了也沒有意義）。<br />
此外，新增了 windowposition.x、windowposition.y 設定，用於調整 shell surface 的顯示位置（只有 SSP 也可在 descript.txt 中設定）。

用於多行輸入框的 balloonc5.png（SSP 2.9.10）中，balloonc5s.txt 的 communicatebox.x/y/width/height 會涵蓋輸入欄位及其下方按鈕列的範圍。<br />
此範圍不會沿用 descript.txt 中的值（該值適用於單行輸入框）。若未在 balloonc5s.txt 中指定，範圍會是距離圖片四邊各 8 像素的區域。<br />
文字大小依據 balloonc5s.txt 的 font.height（省略時使用 descript.txt 的 font.height），字型與顏色則依據 communicatebox.font.name/font.color/background.color。

**対応:** Materia / SSP / CROW
