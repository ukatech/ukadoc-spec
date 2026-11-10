# windowposition.x,座標

**カテゴリ:** descript.txt

相對於 balloon 基本位置的 x 座標方向位移。<br />
可用像素數值或關鍵字指定。<br />
以數值指定時，**無論 balloon 顯示在左側或右側，向右一律為+**。請注意，這與 shell 的[balloon.offsetx](../../shell/descript-txt/sakura.balloon.offsetx.md)不同，顯示在右側時符號也不會反轉。<br />
指定center時，會固定在 shell 的中央上方（僅限 SSP，指定top也相同）。<br />
指定bottom時，會固定在 shell 的中央下方（僅限 SSP）。<br />
不接受上述以外的字串（例如 left、right、free），並會視為0。SSP 會在錯誤記錄中顯示警告。<br />
此外，僅限 SSP，也可以寫在 descript.txt 中。

**既定値:** 0

**対応:** Materia / SSP / CROW
