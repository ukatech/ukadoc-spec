# Base surface

## Base surface

各 surface 的基本狀態，也就是動畫合成前的影像，稱為 base surface。

動畫通常會繪製在 base surface 上方（畫面前側）。

## Base surface 的實際內容

某個 surface 的 base surface，是由對應 ID 的 surface\*.png，以及該 ID 的 surface brace 中的 [element 指定](element-star.md)所定義。

有 surface\*.png 的 surface，其影像會成為 surface\* 的 base surface。但若同時定義了 element0，surface\*.png 的內容會被捨棄，並以 element0 的定義內容取代（這是為確保相容性而制定的規格）。

若有 element1 以後的定義，會依序疊加合成於其上，最終的合成結果會作為 base surface。
