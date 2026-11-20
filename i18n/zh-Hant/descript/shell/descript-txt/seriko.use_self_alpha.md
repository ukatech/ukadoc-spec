# seriko.use_self_alpha,值

**カテゴリ:** descript.txt

指定 1 或 true 時，對於具有透明度的影像（含 alpha 通道的 PNG）以及有 .pna 的影像，參照其 alpha 通道作為透明度。若 alpha 通道和 .pna 均不存在，則採用以影像左上角顏色為鍵色的傳統行為。<br />
指定 full 時，除了上述行為，也將所有沒有 alpha 通道的影像視為不透明（不以左上角的鍵色處理透明度）。

也可寫在 ghost 側的 descript.txt。若 shell 側有指定，則優先使用 shell 側的值；否則使用 ghost 側的值。

**既定値:** 0

**対応:** SSP
