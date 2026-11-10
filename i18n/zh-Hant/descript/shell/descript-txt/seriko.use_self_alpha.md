# seriko.use_self_alpha,值

**カテゴリ:** descript.txt

指定 1 或 true 時，具有透明度的圖片（附有 alpha 通道的 PNG）以及具有 .pna 的圖片，會參照 alpha 通道並將其用作透明度。若沒有 alpha 通道也沒有 .pna，則會採用傳統行為，以圖片左上角的顏色作為鍵色。<br />
指定 full 時，除了上述行為外，沒有 alpha 通道的圖片也一律視為不透明（不會將左上角的鍵色設為透明）。

**既定値:** 0

**対応:** SSP
